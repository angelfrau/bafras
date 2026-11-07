"""Caso de uso: generar una página a HTML estático desde el bundle editorial validado.

CONTENT (bundle) + SITE (rutas, enlaces, composición, contacto) + MEDIA (manifiesto) → contexto →
Jinja2 → archivos. Todo se valida antes de escribir; los recursos se copian antes que el HTML.
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
from bafras_web.site.publication import PublicationMode, publication_blockers
from bafras_web.site.routes import SiteRouting
from bafras_web.site.settings import SiteContact

from .configuration import load_media_manifest, load_site_composition, load_site_routing, load_site_settings
from .editorial import EditorialLoadRequest, inspect_editorial
from .presentation import (PresentationError, SECTION_COMPONENTS, SUPPORTED_SECTIONS, STATIC_ASSETS, prepare_page_context)

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


def _load_inputs(paths: ProjectPaths, locale: str) -> BuildInputs:
    routing = load_site_routing(paths)
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


def render_page(paths: ProjectPaths, request: BuildRequest, *, inputs: BuildInputs | None = None) -> RenderedPage:
    """Mismo renderizado para build individual y multipágina; inputs pertenece solo a esta ejecución."""
    inputs = inputs if inputs is not None else _load_inputs(paths, request.locale)
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
    try:
        context = prepare_page_context(bundle, page, routing, inputs.contact, composition, images)
    except PresentationError as error:
        raise BuildError(error.problems) from error
    html = render_html("pages/sections.html", context)
    return RenderedPage(html=html, assets=(*STATIC_ASSETS, *sorted({i.source_path for i in images.values()})))


def _generate(paths: ProjectPaths, locale: str, mode: PublicationMode, page_id: str | None,
              build_root: Path | None) -> tuple[Path, ...]:
    inputs = _load_inputs(paths, locale)
    selected = (page_id,) if page_id is not None else tuple(inputs.routing.routes.pages)
    try:
        rendered = {pid: render_page(paths, BuildRequest(locale, pid, mode), inputs=inputs) for pid in selected}
        if mode != "preview":
            raise BuildError(["release no produce salida en WEB-V03"])
        urls = {pid: inputs.routing.url(pid, locale) for pid in inputs.routing.routes.pages}
        if any(urls[pid] is None for pid in selected):
            raise BuildError([f"{locale}: página seleccionada sin URL de routing"])
        html_by_url = {url: rendered[pid].html for pid in selected if (url := urls[pid]) is not None}
        assets = tuple(sorted({asset for page in rendered.values() for asset in page.assets}))
        output = ((build_root if build_root is not None else paths.build) / "preview").absolute()
        alias = preview_path(output.parent, locale, page_id).relative_to(output.resolve()) if page_id else None
        targets = materialize_preview(paths, output, html_by_url, assets,
                                      allowed_missing_pages={url for pid, url in urls.items() if pid not in selected and url},
                                      legacy_alias=alias)
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
