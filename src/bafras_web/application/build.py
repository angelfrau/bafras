"""Caso de uso: generar una página a HTML estático desde el bundle editorial validado.

CONTENT (bundle) + SITE (rutas, enlaces, composición, contacto) + MEDIA (manifiesto) → contexto →
Jinja2 → archivos. Todo se valida antes de escribir; los recursos se copian antes que el HTML.

Preview resuelve también los idiomas no publicados (`SiteRouting.for_preview`); release no cambia.
Las fichas de entidad (experiencias) se generan con una única plantilla a partir de las rutas de entidad de SITE.
Cada idioma se genera por separado y conserva en la salida los resultados ya generados de los demás idiomas.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.build_output import OutputError, materialize_preview, image_file_problems
from bafras_web.adapters.jinja import render_html
from bafras_web.editorial.integrity import build_editorial_bundle
from bafras_web.editorial.pages import EditorialBundle, PageContent
from bafras_web.editorial.pending import resolve_pending_selector
from bafras_web.media.assets import MediaError, MediaManifest, ResolvedImage, resolve_image, media_publication_blockers
from bafras_web.site.composition import PageComposition, SiteComposition, media_key, composition_problems
from bafras_web.site.publication import PublicationMode, entity_publication_blockers, publication_blockers
from bafras_web.site.routes import SiteRouting
from bafras_web.site.settings import SiteContact

from .configuration import load_media_manifest, load_site_composition, load_site_routing, load_site_settings
from .editorial import EditorialLoadRequest, inspect_editorial
from .presentation import (PresentationError, SECTION_COMPONENTS, SUPPORTED_SECTIONS, STATIC_ASSETS,
                           prepare_experience_context, prepare_page_context)

_SAFE_LOCALE = re.compile(r"^[a-z]{2}$")
_SAFE_PAGE_ID = re.compile(r"^[a-z][a-z0-9_]*$")


class BuildError(Exception):
    """La página no puede generarse; `problems` explica cada motivo."""

    def __init__(self, problems: list[str]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


@dataclass(frozen=True)
class BuildRequest:
    locale: str
    page_id: str
    mode: PublicationMode


@dataclass(frozen=True)
class RenderedPage:
    html: str
    assets: tuple[str, ...]  # rutas relativas a la raíz del proyecto, que se copian a la salida


def preview_path(build_root: Path, locale: str, page_id: str) -> Path:
    """`build/preview/<locale>/<page_id>/index.html`, solo con identificadores validados."""
    if not _SAFE_LOCALE.match(locale) or not _SAFE_PAGE_ID.match(page_id):
        raise BuildError([f"identificador no válido para una ruta de salida: {locale!r}/{page_id!r}"])
    preview_root = (build_root / "preview").resolve()
    target = (preview_root / locale / page_id / "index.html").resolve()
    if not target.is_relative_to(preview_root):
        raise BuildError([f"ruta de salida fuera de {preview_root}"])
    return target


def _page_images(page: PageContent, composition: PageComposition, manifest: MediaManifest, locale: str,
                 paths: ProjectPaths) -> dict[tuple[str, str | None], ResolvedImage]:
    """Imágenes asignadas por D05 a los huecos `media` de la página, verificadas contra el archivo real."""
    images: dict[tuple[str, str | None], ResolvedImage] = {}
    problems: list[str] = []
    section_ids = {s.id for s in page.sections}
    for selector, asset_id in composition.media.items():
        if media_key(selector)[0] not in section_ids or resolve_pending_selector(page, selector).status != "none":
            problems.append(f"{selector}: no es un hueco de imagen vacío de {page.page_id!r}")
            continue
        try:
            image = resolve_image(manifest.get(asset_id), locale)
        except MediaError as error:
            problems.extend(f"{selector}: {problem}" for problem in error.problems)
            continue
        file_problems = image_file_problems(paths.root, image, manifest.get(asset_id).output_sha256)
        problems.extend(f"{selector}: {problem}" for problem in file_problems)
        if not file_problems:
            images[media_key(selector)] = image
    if problems:
        raise BuildError(problems)
    return images


@dataclass(frozen=True)
class BuildInputs:
    """Dependencias compartidas de una ejecución; sin caché global ni modelos editoriales duplicados."""
    routing: SiteRouting
    bundle: EditorialBundle
    manifest: MediaManifest
    composition: SiteComposition
    contact: SiteContact


def _load_inputs(paths: ProjectPaths, locale: str, mode: PublicationMode = "preview") -> BuildInputs:
    routing = load_site_routing(paths)
    if mode == "preview":
        routing = routing.for_preview()
    inspection = inspect_editorial(paths, EditorialLoadRequest(locale=locale, policy="COMPLETE"))
    if not inspection.can_build_bundle:
        raise BuildError([
            f"{d.code} {d.source or ''} {d.selector or ''}: {d.message}".replace("  ", " ")
            for d in inspection.diagnostics if d.severity == "error"
        ] or ["el contenido editorial no permite construir el bundle"])
    bundle = build_editorial_bundle(inspection)
    composition = load_site_composition(paths)
    problems = composition_problems(composition, bundle)
    if problems:
        raise BuildError(problems)
    return BuildInputs(routing, bundle, load_media_manifest(paths), composition, load_site_settings(paths).contact)


def _experience_images(inputs: BuildInputs, locale: str, paths: ProjectPaths,
                       experience_ids: list[str]) -> dict[str, tuple[ResolvedImage, ...]]:
    """Imagen principal y galería asignadas por composición, verificadas contra el archivo real (MEDIA)."""
    found: dict[str, tuple[ResolvedImage, ...]] = {}
    problems: list[str] = []
    for experience_id in experience_ids:
        media = inputs.composition.experiences.get(experience_id)
        if media is None:
            continue
        resolved = []
        for asset_id in media.assets:
            try:
                asset = inputs.manifest.get(asset_id)
                image = resolve_image(asset, locale)
            except MediaError as error:
                problems.extend(f"experiences/{experience_id}: {problem}" for problem in error.problems)
                continue
            file_problems = image_file_problems(paths.root, image, asset.output_sha256)
            problems.extend(f"experiences/{experience_id}: {problem}" for problem in file_problems)
            resolved.append(image)
        found[experience_id] = tuple(resolved)
    if problems:
        raise BuildError(problems)
    return found


def _indexed_experiences(page: PageContent) -> list[str]:
    return [entry.experience_ref for section in page.sections if section.kind == "experience_index"
            for group in section.groups for entry in group.entries]


def _experience_index_page(inputs: BuildInputs) -> str | None:
    route = inputs.routing.routes.entities.get("experience")
    return route.parent if route is not None else None


def entity_ids(inputs: BuildInputs) -> list[str]:
    """Experiencias con ficha: las enlazadas desde su página índice, en orden editorial."""
    parent = _experience_index_page(inputs)
    if parent is None or parent not in {page.page_id for page in inputs.bundle.pages}:
        return []
    return list(dict.fromkeys(_indexed_experiences(inputs.bundle.get_page(parent))))


def render_experience(paths: ProjectPaths, locale: str, experience_id: str, mode: PublicationMode, *,
                      inputs: BuildInputs | None = None) -> RenderedPage:
    """Ficha estándar: una plantilla para cualquier experiencia válida, sin código por identificador."""
    inputs = inputs if inputs is not None else _load_inputs(paths, locale, mode)
    parent = _experience_index_page(inputs)
    if parent is None:
        raise BuildError(["config/routes.yaml: sin ruta de entidad 'experience'"])
    try:
        experience = inputs.bundle.get_experience(experience_id)
    except KeyError:
        raise BuildError([f"experiencia inexistente: {experience_id!r}"]) from None
    problems = entity_publication_blockers(experience.review.status, locale, inputs.routing, mode)
    if problems:
        raise BuildError(problems)
    images = _experience_images(inputs, locale, paths, [experience_id]).get(experience_id, ())
    composition = inputs.composition.for_page(parent)
    try:
        context = prepare_experience_context(inputs.bundle, inputs.bundle.get_page(parent), experience, inputs.routing,
                                             inputs.contact, composition, images)
    except PresentationError as error:
        raise BuildError(error.problems) from error
    html = render_html("pages/experience.html", context)
    return RenderedPage(html=html, assets=(*STATIC_ASSETS, *sorted({i.source_path for i in images})))


def render_page(paths: ProjectPaths, request: BuildRequest, *, inputs: BuildInputs | None = None) -> RenderedPage:
    """Mismo renderizado para build individual y multipágina; inputs pertenece solo a esta ejecución."""
    inputs = inputs if inputs is not None else _load_inputs(paths, request.locale, request.mode)
    routing, bundle = inputs.routing, inputs.bundle
    if bundle.locale != request.locale:
        raise BuildError([f"bundle {bundle.locale!r} incompatible con locale {request.locale!r}"])
    if request.page_id not in routing.routes.pages:
        raise BuildError([f"página no configurada: {request.page_id!r}"])
    page = bundle.get_page(request.page_id)
    composition = inputs.composition.for_page(page.page_id)
    problems = publication_blockers(page, bundle.locale, routing, request.mode)
    if request.mode == "release":
        for asset_id in sorted(set(composition.media.values())):
            problems.extend(media_publication_blockers(inputs.manifest.get(asset_id)))
    if problems:
        raise BuildError(problems)
    images = _page_images(page, composition, inputs.manifest, bundle.locale, paths)
    cards = _experience_images(inputs, bundle.locale, paths, _indexed_experiences(page))
    cards = {ref: found[:1] for ref, found in cards.items()}  # la tarjeta usa solo la imagen principal
    try:
        context = prepare_page_context(bundle, page, routing, inputs.contact, composition, images, cards)
    except PresentationError as error:
        raise BuildError(error.problems) from error
    html = render_html("pages/sections.html", context)
    used = {i.source_path for i in images.values()} | {i.source_path for found in cards.values() for i in found}
    return RenderedPage(html=html, assets=(*STATIC_ASSETS, *sorted(used)))


def _routable_urls(inputs: BuildInputs) -> set[str]:
    """Todas las URL que SITE puede producir (páginas y fichas, todos los idiomas visibles)."""
    routing = inputs.routing
    urls = {routing.url(pid, code) for pid in routing.routes.pages for code in routing.visible_codes}
    urls |= {routing.entity_url("experience", eid, code) for eid in entity_ids(inputs) for code in routing.visible_codes}
    return {url for url in urls if url}


def _preserved_by(locale: str, routing: SiteRouting):
    """HTML de la salida previa que pertenece a otros idiomas y debe conservarse.

    `assets/` no se traslada: todos los idiomas comparten composición y recursos, y la integridad del árbol
    completo falla si una página conservada referencia un recurso que la generación actual no aporta.
    """
    default = routing.locales.default_locale
    others = set(routing.locales.codes) - {locale}

    def preserve(relative: Path) -> bool:
        first = relative.parts[0] if relative.parts else ""
        if first == "assets":
            return False
        return first in others if locale == default else first != locale
    return preserve


def _generate(paths: ProjectPaths, locale: str, mode: PublicationMode, page_id: str | None,
              build_root: Path | None) -> tuple[Path, ...]:
    inputs = _load_inputs(paths, locale, mode)
    selected = (page_id,) if page_id is not None else tuple(inputs.routing.routes.pages)
    try:
        rendered = {pid: render_page(paths, BuildRequest(locale, pid, mode), inputs=inputs) for pid in selected}
        entities = {eid: render_experience(paths, locale, eid, mode, inputs=inputs)
                    for eid in (entity_ids(inputs) if page_id is None else ())}
        if mode != "preview":
            raise BuildError(["release no produce salida en WEB-V03"])
        urls = {pid: inputs.routing.url(pid, locale) for pid in inputs.routing.routes.pages}
        if any(urls[pid] is None for pid in selected):
            raise BuildError([f"{locale}: página seleccionada sin URL de routing"])
        html_by_url = {url: rendered[pid].html for pid in selected if (url := urls[pid]) is not None}
        for eid, page in entities.items():
            url = inputs.routing.entity_url("experience", eid, locale)
            if url is None or url in html_by_url:
                raise BuildError([f"{locale}: ficha {eid!r} sin URL propia o en colisión"])
            html_by_url[url] = page.html
        assets = tuple(sorted({asset for page in (*rendered.values(), *entities.values()) for asset in page.assets}))
        output = ((build_root if build_root is not None else paths.build) / "preview").absolute()
        alias = preview_path(output.parent, locale, page_id).relative_to(output.resolve()) if page_id else None
        targets = materialize_preview(paths, output, html_by_url, assets,
                                      allowed_missing_pages=_routable_urls(inputs) - set(html_by_url),
                                      legacy_alias=alias, preserve=_preserved_by(locale, inputs.routing))
    except (OutputError, OSError) as error:
        problems = error.problems if isinstance(error, OutputError) else [f"preparación/promoción de {locale}: {error}"]
        raise BuildError(problems) from error
    return targets


def build_page(paths: ProjectPaths, request: BuildRequest, build_root: Path | None = None) -> Path:
    """Build individual compatible; añade también la ubicación correcta según SITE."""
    _generate(paths, request.locale, request.mode, request.page_id, build_root)
    return preview_path(build_root if build_root is not None else paths.build, request.locale, request.page_id)


def build_site(paths: ProjectPaths, locale: str, mode: PublicationMode, build_root: Path | None = None) -> tuple[Path, ...]:
    """Sitio completo: catálogo SITE, bundle único, staging y comprobación global antes de promover."""
    return _generate(paths, locale, mode, None, build_root)
