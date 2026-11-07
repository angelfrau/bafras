"""Contexto Jinja tipado: referencias ya resueltas y modelos CONTENT originales, sin lectura de archivos."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict

from bafras_web.editorial.entities import Person, Sector, Experience
from bafras_web.editorial.pages import EditorialBundle, PageContent
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
STATIC_ASSETS = ("assets/css/site.css", "assets/js/site.js")
# D05 VIS-020: la página de contacto es el botón destacado de la cabecera, no una entrada de menú más.
HEADER_CTA_PAGE = "contacto"
# CommonContent requerido por el layout (ids en content/<idioma>/common.yaml).
REQUIRED_MESSAGES = ("skip-link", "menu", "main-navigation")
BRAND_TEXT_ID = "brand"
PREVIEW_NOTICE = "Vista previa interna · contenido en revisión, no publicable"

@dataclass(frozen=True)
class NavLink:
    page_id: str
    label: str
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
    locales: tuple[str, ...]
    email: str
    email_href: str
    phone: str
    phone_href: str


def _layout(bundle: EditorialBundle, page: PageContent, routing: SiteRouting, contact: SiteContact) -> Layout:
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

    return Layout(
        brand=brand, home_url=labels[home][1], messages=messages,
        navigation=tuple(link(p) for p in top_level if p != HEADER_CTA_PAGE), cta=link(HEADER_CTA_PAGE),
        locales=tuple(c for c in routing.locales.published_codes if routing.url(page.page_id, c)),
        email=contact.email, email_href=contact_href(contact, "email"),
        phone=contact.phone_display, phone_href=contact_href(contact, "phone"),
    )


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


def prepare_page_context(bundle: EditorialBundle, page: PageContent, routing: SiteRouting, contact: SiteContact,
                         composition: PageComposition, images: dict[tuple[str, str | None], ResolvedImage]) -> PageContext:
    """Resolver entidades/enlaces una vez; Jinja recibe modelos originales y destinos explícitos."""
    components = component_templates(page)
    sectors = {ref: bundle.get_sector(ref) for section in page.sections if section.kind == "sector_index" for ref in section.sector_refs}
    people = {ref: bundle.get_person(ref) for section in page.sections if section.kind == "team" for ref in section.person_refs}
    experiences = {entry.experience_ref: bundle.get_experience(entry.experience_ref)
                   for section in page.sections if section.kind == "experience_index" for group in section.groups for entry in group.entries}
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
        images=images, variants=composition.variants, layout=_layout(bundle, page, routing, contact),
        stylesheet="/" + STATIC_ASSETS[0], script="/" + STATIC_ASSETS[1],
    )
