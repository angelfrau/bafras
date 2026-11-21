"""Identified editorial entities; facts and permissions remain explicit."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, model_validator

from .primitives import (
    EditorialId, EditorialModel, EditorialReview, Paragraph, PendingField,
    PublicText, SourceRef, TextItem, Verification,
)
from .references import CallToAction, ExternalLink, ResourceLink

SectorId = Literal[
    "turismo-terciario", "industria-logistica-agroindustria",
    "infraestructuras-servicios-publicos", "salud-educacion-equipamientos",
    "edificacion-rehabilitacion-activos",
    "comunidades-energeticas-infraestructuras-tecnologicas",
]


class Person(EditorialModel):
    id: EditorialId
    public_name: PublicText
    qualification: PublicText | None = None
    specialty: PublicText | None = None
    biography: list[Paragraph] = Field(default_factory=list)
    portrait: None = None  # Await WEB MediaRef; do not invent a parallel identity.
    experience_refs: list[EditorialId] = Field(default_factory=list)
    review: EditorialReview
    verification: Verification = Field(default_factory=Verification)
    pending: list[PendingField] = Field(default_factory=list)


class Sector(EditorialModel):
    id: SectorId
    title: PublicText
    description: list[Paragraph] = Field(min_length=1)
    examples: list[TextItem] = Field(default_factory=list)
    contextual_actions: list[CallToAction] = Field(default_factory=list)
    catalog_refs: list[ResourceLink] = Field(default_factory=list)

    @model_validator(mode="after")
    def _unique_catalogs(self) -> Sector:
        refs = [ref.catalog_id for ref in self.catalog_refs]
        if len(refs) != len(set(refs)):
            raise ValueError("duplicate catalog references")
        return self


class DocumentedResult(EditorialModel):
    id: EditorialId
    text: PublicText
    evidence_refs: list[SourceRef] = Field(min_length=1)


class Experience(EditorialModel):
    id: EditorialId
    kind: Literal["founder_previous", "bafras_project"]
    title: PublicText
    summary: list[Paragraph] = Field(default_factory=list)
    person_refs: list[EditorialId] = Field(default_factory=list)
    attribution: PublicText | None = None
    context: list[Paragraph] = Field(default_factory=list)
    intervention: list[Paragraph] = Field(default_factory=list)
    systems: list[TextItem] = Field(default_factory=list)
    phases: list[TextItem] = Field(default_factory=list)
    deliverables: list[TextItem] = Field(default_factory=list)
    results: list[DocumentedResult] = Field(default_factory=list)
    evidence_refs: list[SourceRef] = Field(default_factory=list)
    # EXPERIENCE-02: datos de tarjeta y ficha técnica (maqueta C04-PE). Opcionales y sin inferencias.
    role: PublicText | None = None  # responsabilidad breve del profesional («Profesional y rol»)
    key_figures: list[TextItem] = Field(default_factory=list)  # magnitudes del proyecto, no logros individuales
    links: list[CallToAction] = Field(default_factory=list)  # solo destinos externos públicos (noticia, DOI)
    review: EditorialReview
    verification: Verification = Field(default_factory=Verification)
    pending: list[PendingField] = Field(default_factory=list)

    @model_validator(mode="after")
    def _external_links_only(self) -> Experience:
        if any(not isinstance(link.target, ExternalLink) for link in self.links):
            raise ValueError("experience links must be external references")
        return self


class DownloadableResource(EditorialModel):
    """Editorial catalog identity only. Physical PDF metadata belongs to WEB."""

    catalog_id: EditorialId
    sector_id: SectorId
    title: PublicText
    description: list[Paragraph] = Field(default_factory=list)
