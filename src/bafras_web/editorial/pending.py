"""Pure, bounded pending selectors. Resolution never approves or publishes.

Grammar: seo.<field>, sections/<id>/<field>, or
sections/<id>/items/<id>/<field>. Only the explicit fields below are exposed;
IDs select list members, never positions. This is not a general object query API.
"""

from dataclasses import dataclass
import re
from typing import Literal

from pydantic import TypeAdapter, ValidationError

from .pages import PageContent
from .primitives import EditorialId
from .sections import (
    CapabilityCard, Card, CardsSection, ContactFormSection, ExperienceGroup,
    ExperienceIndexSection, HeroSection, ItemListSection,
    ListItem, ProcessItem, ProcessSection, Section,
)

ResolutionStatus = Literal[
    "value", "none", "collection", "invalid_syntax", "section_not_found",
    "item_not_found", "field_not_allowed",
]
SelectedItems = list[Card] | list[ListItem] | list[ProcessItem]
SelectedValue = str | SelectedItems | list[ExperienceGroup] | None
_EDITORIAL_ID = TypeAdapter(EditorialId)
_FIELD = re.compile(r"[a-z][a-z0-9_]*", re.ASCII)


@dataclass(frozen=True)
class SelectorResolution:
    status: ResolutionStatus
    value: SelectedValue = None
    message: str = ""


@dataclass(frozen=True)
class PendingDiagnostic:
    page_id: str
    selector: str
    reason_code: str
    code: ResolutionStatus
    message: str


def _is_id(value: str) -> bool:
    try:
        _EDITORIAL_ID.validate_python(value)
    except ValidationError:
        return False
    return True


def _items(section: Section) -> SelectedItems | None:
    if isinstance(section, (CardsSection, ItemListSection, ProcessSection)):
        return section.items
    return None


def _section_field(section: Section, field: str) -> tuple[bool, SelectedValue]:
    # Explicit allowlist; no getattr or access to Pydantic internals.
    if field == "privacy_text" and isinstance(section, ContactFormSection):
        return True, section.privacy_text
    if field == "groups" and isinstance(section, ExperienceIndexSection):
        return True, section.groups
    if field == "title":
        return True, section.title
    if field == "items":
        items = _items(section)
        return items is not None, items
    if field == "media" and isinstance(section, (HeroSection, CardsSection, ItemListSection)):
        return True, section.media
    if field == "eyebrow" and isinstance(section, (HeroSection, CardsSection)):
        return True, section.eyebrow
    if field == "subtitle" and isinstance(section, HeroSection):
        return True, section.subtitle
    return False, None


def _resolved(allowed: bool, value: SelectedValue, context: str) -> SelectorResolution:
    if not allowed:
        return SelectorResolution("field_not_allowed", message=f"Campo no admitido: {context}")
    if isinstance(value, list):
        return SelectorResolution("collection", value)
    return SelectorResolution("none" if value is None else "value", value)


def resolve_pending_selector(page: PageContent, selector: str) -> SelectorResolution:
    """Resolve one selector without changing content, pending reasons or review.

Fields: SEO title/description; section title, items (cards/lists/process),
media (hero/cards/list), eyebrow (hero/cards), subtitle (hero), groups
(experience index), privacy_text (form); item title,
and media only on capability cards. New fields require an explicit extension.
"""
    if selector.startswith("seo."):
        field = selector[4:]
        if not _FIELD.fullmatch(field):
            return SelectorResolution("invalid_syntax", message="Sintaxis esperada: seo.<field>")
        if field == "title":
            return _resolved(True, page.seo.title, selector)
        if field == "description":
            return _resolved(True, page.seo.description, selector)
        return _resolved(False, None, selector)

    parts = selector.split("/")
    valid = (
        len(parts) in (3, 5) and parts[0] == "sections" and _is_id(parts[1])
        and bool(_FIELD.fullmatch(parts[-1]))
    )
    if valid and len(parts) == 5:
        valid = parts[2] == "items" and _is_id(parts[3])
    if not valid:
        return SelectorResolution("invalid_syntax", message="Usar sections/<id>/<field> o sections/<id>/items/<id>/<field>")

    section = next((section for section in page.sections if section.id == parts[1]), None)
    if section is None:
        return SelectorResolution("section_not_found", message=f"Sección inexistente: {parts[1]}")
    if len(parts) == 3:
        allowed, value = _section_field(section, parts[2])
        return _resolved(allowed, value, f"{section.id}/{parts[2]} ({section.kind})")

    items = _items(section)
    if items is None:
        return _resolved(False, None, f"{section.id}/items ({section.kind})")
    item = next((item for item in items if item.id == parts[3]), None)
    if item is None:
        return SelectorResolution("item_not_found", message=f"Elemento inexistente: {section.id}/items/{parts[3]}")
    if parts[4] == "title":
        return _resolved(True, item.title, selector)
    if parts[4] == "media" and isinstance(item, CapabilityCard):
        return _resolved(True, item.media, selector)
    return _resolved(False, None, selector)


def validate_pending_fields(page: PageContent) -> list[PendingDiagnostic]:
    """Report invalid targets only. Existing values/collections may remain pending.

    Structural validation is Pydantic's job. These diagnostics establish local
    selector integrity, never publication eligibility or automatic resolution.
    """
    diagnostics = []
    for pending in page.pending:
        result = resolve_pending_selector(page, pending.field)
        if result.status not in ("value", "none", "collection"):
            diagnostics.append(PendingDiagnostic(
                page.page_id, pending.field, pending.reason_code, result.status,
                f"{page.page_id}: {pending.field}: {result.message} (motivo: {pending.reason_code})",
            ))
    return diagnostics
