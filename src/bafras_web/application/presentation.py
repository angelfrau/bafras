"""Contexto Jinja tipado: referencias ya resueltas y modelos CONTENT originales, sin lectura de archivos."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict

from bafras_web.editorial.entities import Person, Sector, Experience
from bafras_web.editorial.pages import EditorialBundle, PageContent
from bafras_web.editorial.sections import ExperienceEntry, ExperienceGroup, Section
from bafras_web.editorial.references import InternalLink, ContactLink
from bafras_web.media.assets import ResolvedImage
from bafras_web.site.composition import PageComposition, SectionVariant
from bafras_web.site.links import LinkResolutionError, LinkTarget, contact_href, resolve_links
from bafras_web.site.routes import SiteRouting
from bafras_web.site.settings import SiteContact


class PresentationError(ValueError):
    def __init__(self, problems: list[str]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


# Mapeo exhaustivo y explícito; nunca se deduce una ruta de plantilla del contenido.
SECTION_COMPONENTS = {
    ("hero", None): "hero.html", ("text", None): "text.html",
    ("cards", "capabilities"): "cards_capabilities.html",
    ("cards", "sector_preview"): "cards_sector_preview.html",
    ("cards", "technical_areas"): "cards_technical_areas.html",
    ("cards", "application_examples"): "cards_application_examples.html",
    ("cards", "discipline_relations"): "cards_discipline_relations.html",
    ("item_list", "needs"): "item_list.html",
    ("item_list", "deliverables"): "item_list.html",
    ("item_list", "modalities"): "item_list.html",
    ("process", "workflow"): "process.html", ("process", "principles"): "process.html",
    ("sector_index", None): "sector_index.html", ("team", None): "team.html",
    ("experience_index", None): "experience_index.html",
}
SUPPORTED_SECTIONS = frozenset(SECTION_COMPONENTS)
# Recursos propios de la presentación (fuente en assets/, se copian a la raíz de salida).
# Logotipo: maestro oficial deep para fondos claros (cabecera y pie); ver WEB_EXPERIENCE_03 §2.
LOGO_ASSET = "assets/images/brand/logos/BAFRAS_logo_horizontal_deep.svg"
FAVICON_ASSET = "assets/images/brand/favicon/favicon.ico"
STATIC_ASSETS = ("assets/css/site.css", "assets/js/site.js", LOGO_ASSET, FAVICON_ASSET)
# Textos de interfaz de la vertical de experiencias (content/<idioma>/common.yaml).
EXPERIENCE_MESSAGES = (
    "experience-areas", "experience-area", "experience-view", "experience-facts", "experience-professional",
    "experience-figures", "experience-context", "experience-systems", "experience-phases", "experience-intervention",
    "experience-deliverables", "experience-results", "experience-links", "experience-gallery", "experience-back",
    "external-link", "experience-portfolio", "experience-previous-work",
)
# WEB-EXPERIENCE-04: el índice separa la cartera propia (bloque 01) de la experiencia previa del equipo (bloque 02)
# según `Experience.kind` (dominio editorial). Ningún nombre de proyecto interviene en la clasificación.
PORTFOLIO_KIND = "bafras_project"
# Controles del carrusel: solo se exigen cuando hay dos o más proyectos (con uno, tarjeta estática sin controles).
PORTFOLIO_CONTROL_MESSAGES = ("experience-portfolio-previous", "experience-portfolio-next")
# Mensaje del estado vacío: opcional. Solo se muestra si CONTENT lo aporta para ese idioma; WEB no lo redacta.
PORTFOLIO_EMPTY_MESSAGE = "experience-portfolio-empty"
# Indicación de adaptación en créditos de imagen con licencia (CC BY/BY-SA): exigida si se muestra un crédito adaptado.
IMAGE_ADAPTED_MESSAGE = "image-adapted"
# Magnitudes visibles por presentación (el resto, en la ficha).
ROW_FIGURES = 3
PORTFOLIO_FIGURES = 2
# D05 VIS-020: la página de contacto es el botón destacado de la cabecera, no una entrada de menú más.
HEADER_CTA_PAGE = "contacto"
# CommonContent requerido por el layout (ids en content/<idioma>/common.yaml).
REQUIRED_MESSAGES = ("skip-link", "menu", "main-navigation", "language")
BRAND_TEXT_ID = "brand"
PREVIEW_NOTICE = "Vista previa interna · contenido en revisión, no publicable"

@dataclass(frozen=True)
class NavLink:
    page_id: str
    label: str
    url: str
    current: bool


@dataclass(frozen=True)
class LocaleLink:
    code: str
    url: str
    current: bool


@dataclass(frozen=True)
class Layout:
    """Cabecera y pie: textos de CommonContent, destinos de SiteRouting y contacto de config/site.yaml."""

    brand: str
    home_url: str
    messages: dict[str, str]
    navigation: tuple[NavLink, ...]
    cta: NavLink
    locales: tuple[LocaleLink, ...]
    logo_url: str
    favicon_url: str
    email: str
    email_href: str
    phone: str
    phone_href: str


def _layout(bundle: EditorialBundle, page: PageContent, routing: SiteRouting, contact: SiteContact,
            alternates: dict[str, str] | None = None) -> Layout:
    """`page` es la página actual o, en una ficha, su página índice (estado actual de la navegación)."""
    common = bundle.common
    try:
        urls = resolve_links(bundle, common, routing, contact)
    except LinkResolutionError as error:
        raise PresentationError([str(problem) for problem in error.problems]) from error
    labels = {a.target.page_id: (a.label, urls[a.target]) for a in common.actions
              if isinstance(a.target, InternalLink) and a.target.section_id is None}
    messages = {m.id: m.text for m in common.interface_messages}
    brand = next((t.text for t in common.footer_texts if t.id == BRAND_TEXT_ID), None)
    locale = bundle.locale
    home = next(pid for pid in routing.routes.pages if routing.routes.segments(pid, routing.locales.default_locale) == [])
    top_level = [pid for pid, route in routing.routes.pages.items() if route.parent is None and pid != home]
    problems = [f"common.yaml ({locale}): falta interface_messages {m!r}" for m in REQUIRED_MESSAGES if m not in messages]
    problems += [f"common.yaml ({locale}): falta la acción de navegación a {p!r}" for p in (home, *top_level) if p not in labels]
    if brand is None:
        problems.append(f"common.yaml ({locale}): falta footer_texts {BRAND_TEXT_ID!r}")
    if problems:
        raise PresentationError(problems)

    def link(page_id: str) -> NavLink:
        label, url = labels[page_id]
        return NavLink(page_id, label, url, page_id == page.page_id)

    found = alternates if alternates is not None else routing.alternates(page.page_id)
    return Layout(
        brand=brand, home_url=labels[home][1], messages=messages,
        navigation=tuple(link(p) for p in top_level if p != HEADER_CTA_PAGE), cta=link(HEADER_CTA_PAGE),
        locales=tuple(LocaleLink(code, url, code == locale) for code, url in found.items()) if len(found) > 1 else (),
        logo_url="/" + LOGO_ASSET, favicon_url="/" + FAVICON_ASSET,
        email=contact.email, email_href=contact_href(contact, "email"),
        phone=contact.phone_display, phone_href=contact_href(contact, "phone"),
    )


@dataclass(frozen=True)
class IndexEntry:
    """Una experiencia tal como la presenta el índice: entidad CONTENT, ámbito, ficha (SITE) e imagen (MEDIA)."""

    entry: ExperienceEntry
    experience: Experience
    group: ExperienceGroup
    url: str
    image: ResolvedImage | None


@dataclass(frozen=True)
class IndexGroup:
    group: ExperienceGroup
    entries: tuple[IndexEntry, ...]


@dataclass(frozen=True)
class ExperienceIndexView:
    """Bloque 01 (cartera BAFRAS, orden editorial) y bloque 02 (ámbitos con experiencia previa del equipo).

    Una sola fuente: las entradas de la sección `experience_index`. Un ámbito sin experiencia previa no se muestra
    en el bloque 02; sus proyectos BAFRAS siguen en el bloque 01 con el ámbito como categoría.
    """

    portfolio: tuple[IndexEntry, ...]
    groups: tuple[IndexGroup, ...]
    empty_message: str | None


def experience_index_view(section: Section, experiences: dict[str, Experience], urls: dict[str, str],
                          images: dict[str, tuple[ResolvedImage, ...]], messages: dict[str, str]) -> ExperienceIndexView:
    portfolio: list[IndexEntry] = []
    groups: list[IndexGroup] = []
    for group in section.groups:
        previous: list[IndexEntry] = []
        for entry in group.entries:
            experience = experiences[entry.experience_ref]
            found = images.get(entry.experience_ref) or ()
            item = IndexEntry(entry, experience, group, urls[entry.experience_ref], found[0] if found else None)
            (portfolio if experience.kind == PORTFOLIO_KIND else previous).append(item)
        if previous:
            groups.append(IndexGroup(group, tuple(previous)))
    return ExperienceIndexView(tuple(portfolio), tuple(groups), messages.get(PORTFOLIO_EMPTY_MESSAGE))


def _credit_messages(bundle: EditorialBundle, images: list[ResolvedImage]) -> list[str]:
    known = {m.id for m in bundle.common.interface_messages}
    if any(image.credit and image.credit.adapted for image in images) and IMAGE_ADAPTED_MESSAGE not in known:
        return [f"common.yaml ({bundle.locale}): falta interface_messages {IMAGE_ADAPTED_MESSAGE!r}"]
    return []


class PageContext(TypedDict):
    lang: str
    title: str
    robots: str
    preview_notice: str
    page: PageContent
    components: dict[str, str]
    sectors: dict[str, Sector]
    people: dict[str, Person]
    experiences: dict[str, Experience]
    links: dict[LinkTarget, str]
    contact_values: dict[ContactLink, str]
    images: dict[tuple[str, str | None], ResolvedImage]
    variants: dict[str, SectionVariant]
    layout: Layout
    stylesheet: str
    script: str
    experience_urls: dict[str, str]
    experience_images: dict[str, tuple[ResolvedImage, ...]]
    experience_index: dict[str, ExperienceIndexView]
    row_figures: int
    portfolio_figures: int


@dataclass(frozen=True)
class ExperienceView:
    """Ficha: la entidad CONTENT original y lo que SITE/MEDIA resuelven para ella; sin textos propios de WEB."""

    experience: Experience
    group: ExperienceGroup
    index_url: str
    index_label: str
    images: tuple[ResolvedImage, ...]
    closing: Section | None


class ExperienceContext(TypedDict):
    lang: str
    title: str
    robots: str
    preview_notice: str
    view: ExperienceView
    links: dict[LinkTarget, str]
    variants: dict[str, SectionVariant]
    images: dict[tuple[str, str | None], ResolvedImage]
    layout: Layout
    stylesheet: str
    script: str


def component_templates(page: PageContent) -> dict[str, str]:
    problems = [
        f"página {page.page_id}, sección {section.id}: kind={section.kind!r} "
        f"purpose={getattr(section, 'purpose', None)!r} sin componente"
        for section in page.sections
        if (section.kind, getattr(section, "purpose", None)) not in SECTION_COMPONENTS
    ]
    if problems:
        raise PresentationError(problems)
    return {section.id: "components/" + SECTION_COMPONENTS[(section.kind, getattr(section, "purpose", None))]
            for section in page.sections}


def _experience_messages(bundle: EditorialBundle) -> list[str]:
    known = {m.id for m in bundle.common.interface_messages}
    return [f"common.yaml ({bundle.locale}): falta interface_messages {m!r}" for m in EXPERIENCE_MESSAGES if m not in known]


def experience_urls(bundle: EditorialBundle, page: PageContent, routing: SiteRouting) -> dict[str, str]:
    """Fichas enlazadas desde los índices de experiencia de la página; un fallo de ruta es un error, no un omitido."""
    urls: dict[str, str] = {}
    problems: list[str] = []
    for section in page.sections:
        if section.kind != "experience_index":
            continue
        for group in section.groups:
            for entry in group.entries:
                url = routing.entity_url("experience", entry.experience_ref, bundle.locale)
                if url is None:
                    problems.append(f"{bundle.locale}/{page.page_id}: sin ruta de ficha para {entry.experience_ref!r}")
                else:
                    urls[entry.experience_ref] = url
    if problems:
        raise PresentationError(problems)
    return urls


def prepare_page_context(bundle: EditorialBundle, page: PageContent, routing: SiteRouting, contact: SiteContact,
                         composition: PageComposition, images: dict[tuple[str, str | None], ResolvedImage],
                         experience_images: dict[str, tuple[ResolvedImage, ...]] | None = None) -> PageContext:
    """Resolver entidades/enlaces una vez; Jinja recibe modelos originales y destinos explícitos."""
    components = component_templates(page)
    sectors = {ref: bundle.get_sector(ref) for section in page.sections if section.kind == "sector_index" for ref in section.sector_refs}
    people = {ref: bundle.get_person(ref) for section in page.sections if section.kind == "team" for ref in section.person_refs}
    experiences = {entry.experience_ref: bundle.get_experience(entry.experience_ref)
                   for section in page.sections if section.kind == "experience_index" for group in section.groups for entry in group.entries}
    if experiences and (problems := _experience_messages(bundle)):
        raise PresentationError(problems)
    shown_experience_images = {ref: found for ref, found in (experience_images or {}).items() if ref in experiences}
    messages = {m.id: m.text for m in bundle.common.interface_messages}
    urls = experience_urls(bundle, page, routing) if experiences else {}
    index_views = {section.id: experience_index_view(section, experiences, urls, shown_experience_images, messages)
                   for section in page.sections if section.kind == "experience_index"}
    problems = _credit_messages(bundle, [*images.values(), *(i for found in shown_experience_images.values() for i in found)])
    if any(len(view.portfolio) > 1 for view in index_views.values()):
        problems += [f"common.yaml ({bundle.locale}): falta interface_messages {m!r}"
                     for m in PORTFOLIO_CONTROL_MESSAGES if m not in messages]
    try:  # el layout informa primero de su CommonContent ausente; después, los textos propios de esta página
        layout = _layout(bundle, page, routing, contact)
    except PresentationError as error:
        raise PresentationError([*error.problems, *problems]) from error
    if problems:
        raise PresentationError(problems)
    try:
        links = resolve_links(bundle, page, routing, contact)
        for sector in sectors.values():
            links.update(resolve_links(bundle, sector, routing, contact))
    except LinkResolutionError as error:
        raise PresentationError([str(problem) for problem in error.problems]) from error
    # SITE es la única autoridad de los datos operativos; las etiquetas siguen en CONTENT.
    contact_values = {channel.target: contact.email if channel.target.channel == "email" else contact.phone_display
                      for section in page.sections if section.kind == "text" for channel in section.contact_channels}
    return PageContext(
        lang=bundle.locale, title=f"PREVIEW · {page.sections[0].title} · {bundle.locale}",
        robots="noindex, nofollow", preview_notice=PREVIEW_NOTICE, page=page, components=components,
        sectors=sectors, people=people, experiences=experiences, links=links, contact_values=contact_values,
        images=images, variants=composition.variants, layout=layout,
        stylesheet="/" + STATIC_ASSETS[0], script="/" + STATIC_ASSETS[1],
        experience_urls=urls, experience_images=shown_experience_images, experience_index=index_views,
        row_figures=ROW_FIGURES, portfolio_figures=PORTFOLIO_FIGURES,
    )


def experience_group(page: PageContent, experience_id: str) -> ExperienceGroup | None:
    """Ámbito del índice que contiene la experiencia (o None si la página no la enlaza)."""
    for section in page.sections:
        if section.kind == "experience_index":
            for group in section.groups:
                if any(entry.experience_ref == experience_id for entry in group.entries):
                    return group
    return None


def prepare_experience_context(bundle: EditorialBundle, index_page: PageContent, experience: Experience,
                               routing: SiteRouting, contact: SiteContact, composition: PageComposition,
                               images: tuple[ResolvedImage, ...]) -> ExperienceContext:
    """Ficha estándar de una experiencia. La misma entidad alimenta tarjeta, ficha y navegación."""
    group = experience_group(index_page, experience.id)
    index_url = routing.url(index_page.page_id, bundle.locale)
    problems = _experience_messages(bundle) + _credit_messages(bundle, list(images))
    if group is None:
        problems.append(f"{experience.id}: no figura en el índice {index_page.page_id!r}")
    if index_url is None:
        problems.append(f"{experience.id}: índice {index_page.page_id!r} sin URL en {bundle.locale!r}")
    closing_id = next((sid for sid, variant in composition.variants.items() if variant == "closing_band"), None)
    closing = next((s for s in index_page.sections if s.id == closing_id), None)
    links: dict[LinkTarget, str] = {}
    try:
        links.update(resolve_links(bundle, experience, routing, contact))
        if closing is not None:
            links.update(resolve_links(bundle, index_page, routing, contact))
    except LinkResolutionError as error:
        problems.extend(str(problem) for problem in error.problems)
    alternates = {code: url for code in routing.visible_codes
                  if (url := routing.entity_url("experience", experience.id, code)) is not None}
    try:
        layout = _layout(bundle, index_page, routing, contact, alternates)
    except PresentationError as error:
        raise PresentationError([*problems, *error.problems]) from error
    index_label = next((item.label for item in (*layout.navigation, layout.cta) if item.page_id == index_page.page_id), None)
    if index_label is None:
        problems.append(f"common.yaml ({bundle.locale}): sin etiqueta de navegación para {index_page.page_id!r}")
    if problems:
        raise PresentationError(problems)
    view = ExperienceView(experience=experience, group=group, index_url=index_url, index_label=index_label,
                          images=images, closing=closing)
    return ExperienceContext(
        lang=bundle.locale, title=f"PREVIEW · {experience.title} · {bundle.locale}", robots="noindex, nofollow",
        preview_notice=PREVIEW_NOTICE, view=view, links=links,
        variants={closing.id: "closing_band"} if closing is not None else {}, images={}, layout=layout,
        stylesheet="/" + STATIC_ASSETS[0], script="/" + STATIC_ASSETS[1],
    )
