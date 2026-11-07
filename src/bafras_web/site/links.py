"""Resolución de destinos editoriales a URL públicas: único lugar donde se construye un `href`.

La URL de un enlace depende solo de su destino tipado y del idioma, así que el resultado se
indexa por el propio destino (los modelos editoriales son inmutables y comparables). Los
errores identifican el enlace por su selector estable, formado con los `id` editoriales.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel

from bafras_web.editorial.entities import Sector
from bafras_web.editorial.pages import CommonContent, EditorialBundle, PageContent
from bafras_web.editorial.references import ContactLink, ExternalLink, InternalLink, ResourceLink, SharedActionRef

from .routes import SiteRouting
from .settings import SiteContact

LinkTarget = InternalLink | ExternalLink | ContactLink | ResourceLink
ProblemKind = Literal["integrity", "availability", "unsupported"]


@dataclass(frozen=True)
class LinkProblem:
    page_id: str
    locale: str
    selector: str
    target: str
    kind: ProblemKind
    reason: str

    def __str__(self) -> str:
        return f"{self.locale}/{self.page_id} · {self.selector} → {self.target}: {self.reason} ({self.kind})"


class LinkResolutionError(ValueError):
    """Uno o más enlaces de una página no tienen destino público válido."""

    def __init__(self, problems: tuple[LinkProblem, ...]) -> None:
        super().__init__("\n".join(str(problem) for problem in problems))
        self.problems = problems


def iter_link_targets(value: object, selector: str = "") -> Iterator[tuple[str, LinkTarget | SharedActionRef]]:
    """Destinos de enlace contenidos en un modelo editorial, en orden, con su selector estable."""
    if isinstance(value, (InternalLink, ExternalLink, ContactLink, ResourceLink, SharedActionRef)):
        yield selector, value
    elif isinstance(value, BaseModel):
        for name in type(value).model_fields:
            yield from iter_link_targets(getattr(value, name), f"{selector}/{name}" if selector else name)
    elif isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            key = getattr(item, "id", None) if isinstance(item, BaseModel) else None
            yield from iter_link_targets(item, f"{selector}/{key if key is not None else index}")


def _describe(target: LinkTarget | SharedActionRef) -> str:
    if isinstance(target, InternalLink):
        return target.page_id + (f"#{target.section_id}" if target.section_id else "")
    if isinstance(target, SharedActionRef):
        return f"common:{target.common_ref}"
    return target.model_dump_json()


def _resolve_internal(target: InternalLink, bundle: EditorialBundle, routing: SiteRouting) -> tuple[str | None, ProblemKind, str]:
    if target.page_id not in routing.routes.pages:
        return None, "integrity", "página no configurada en config/routes.yaml"
    if target.section_id is not None:
        try:
            sections = {section.id for section in bundle.get_page(target.page_id).sections}
        except KeyError:
            return None, "integrity", "página destino ausente del bundle"
        if target.section_id not in sections:
            return None, "integrity", "sección destino inexistente"
    url = routing.url(target.page_id, bundle.locale)
    if url is None:
        return None, "availability", "sin URL pública en este idioma (no publicado o sin slug)"
    return url + (f"#{target.section_id}" if target.section_id else ""), "integrity", ""


def contact_href(contact: SiteContact, channel: Literal["email", "phone"]) -> str:
    """`mailto:` / `tel:` a partir de los datos validados de config/site.yaml (D04 §13)."""
    return f"mailto:{contact.email}" if channel == "email" else f"tel:{contact.phone_e164}"


def resolve_links(
    bundle: EditorialBundle, source: PageContent | CommonContent | Sector, routing: SiteRouting,
    contact: SiteContact | None = None,
) -> dict[LinkTarget, str]:
    """URL de cada destino de `source` (una página o el contenido común) en el idioma del bundle.

    Sin `contact`, los `ContactLink` se rechazan como no soportados. `LinkResolutionError` reúne todos los fallos.
    """
    origin = source.page_id if isinstance(source, PageContent) else (source.id if isinstance(source, Sector) else "common")
    resolved: dict[LinkTarget, str] = {}
    problems: list[LinkProblem] = []
    for selector, target in iter_link_targets(source):
        def fail(kind: ProblemKind, reason: str) -> None:
            problems.append(LinkProblem(origin, bundle.locale, selector, _describe(target), kind, reason))

        if isinstance(target, InternalLink):
            url, kind, reason = _resolve_internal(target, bundle, routing)
            if url is None:
                fail(kind, reason)
            else:
                resolved[target] = url
        elif isinstance(target, ExternalLink):
            if target.url.scheme != "https":
                fail("integrity", "solo se admiten enlaces externos https")
            else:
                resolved[target] = str(target.url)
        elif isinstance(target, ContactLink) and contact is not None:
            resolved[target] = contact_href(contact, target.channel)
        else:
            fail("unsupported", f"tipo de enlace {type(target).__name__} aún no soportado por WEB")
    if problems:
        raise LinkResolutionError(tuple(problems))
    return resolved
