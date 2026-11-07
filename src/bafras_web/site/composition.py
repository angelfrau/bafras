"""Composición de páginas aprobada en D05: imagen asignada a cada hueco `media` y variantes de sección.

D03 delega la selección de imágenes en D05 («Documento rector: D05 §18/§26»), así que la
asignación vive en configuración WEB (config/composition.yaml) y no en el contenido editorial.
Los selectores son los mismos que los pendientes `integration_pending` de CONTENT.
"""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from bafras_web.media.assets import AssetId
from bafras_web.editorial.pages import EditorialBundle
from bafras_web.editorial.pending import resolve_pending_selector

PageId = Annotated[str, StringConstraints(pattern=r"^[a-z][a-z0-9_]*$")]
MediaSelector = Annotated[str, StringConstraints(pattern=r"^sections/[a-z0-9-]+(/items/[a-z0-9-]+)?/media$")]
SectionId = Annotated[str, StringConstraints(pattern=r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")]
SectionVariant = Literal["closing_band", "editorial_rows", "sand_band", "decision_grid", "technical_chapters", "dark_band", "direct_contact"]


class PageComposition(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    media: dict[MediaSelector, AssetId] = Field(default_factory=dict)
    variants: dict[SectionId, SectionVariant] = Field(default_factory=dict)


class SiteComposition(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    schema_version: Literal[1]
    pages: dict[PageId, PageComposition] = Field(default_factory=dict)

    def for_page(self, page_id: str) -> PageComposition:
        return self.pages.get(page_id, PageComposition())


def media_key(selector: str) -> tuple[str, str | None]:
    """`sections/h02/items/energy/media` → ('h02', 'energy'); `sections/h01/media` → ('h01', None)."""
    parts = selector.split("/")
    return parts[1], parts[3] if len(parts) == 5 else None


def composition_problems(composition: SiteComposition, bundle: EditorialBundle) -> list[str]:
    """Selectores y variantes coherentes con las secciones CONTENT; no lee archivos ni decide HTML."""
    problems = []
    for page_id, config in composition.pages.items():
        if page_id not in {page.page_id for page in bundle.pages}:
            problems.append(f"composición: página desconocida {page_id!r}")
            continue
        page = bundle.get_page(page_id)
        for selector in config.media:
            if resolve_pending_selector(page, selector).status != "none":
                problems.append(f"{page_id}/{selector}: no es un hueco de imagen vacío")
        sections = {s.id: s for s in page.sections}
        variant_sections = {
            "closing_band": {("text", None)}, "direct_contact": {("text", None)}, "editorial_rows": {("cards", "capabilities")},
            "sand_band": {("text", None), ("cards", "discipline_relations")},
            "decision_grid": {("item_list", "needs")}, "technical_chapters": {("cards", "technical_areas")},
            "dark_band": {("item_list", "deliverables")},
        }
        for section_id, variant in config.variants.items():
            if section_id not in sections:
                problems.append(f"composición {page_id}: sección inexistente {section_id!r}")
            elif (sections[section_id].kind, getattr(sections[section_id], "purpose", None)) not in variant_sections[variant]:
                problems.append(f"composición {page_id}/{section_id}: variante {variant!r} incompatible")
    return problems
