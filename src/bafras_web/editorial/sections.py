"""Nine semantic section families; visual composition belongs to WEB."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import Field, model_validator

from .primitives import EditorialId, EditorialModel, Paragraph, PublicText, SourceRef, TextItem
from .references import Action, CallToAction, ContactLink, InternalLink


class SectionBase(EditorialModel):
    id: EditorialId
    source_block: SourceRef | None = None


class HeroSection(SectionBase):
    kind: Literal["hero"] = "hero"
    eyebrow: PublicText | None = None
    title: PublicText
    subtitle: PublicText | None = None
    paragraphs: list[Paragraph] = Field(default_factory=list)
    actions: list[Action] = Field(default_factory=list)
    # Deliberately unavailable until WEB supplies MediaRef. No alternate ID type.
    media: None = None
    attribution: PublicText | None = None


class ContactChannel(EditorialModel):
    id: EditorialId
    label: PublicText
    target: ContactLink
    # Approved public datum; delivery/operability belongs to WEB, not this value.
    value: PublicText | None = None


class TextSection(SectionBase):
    kind: Literal["text"] = "text"
    title: PublicText | None = None
    paragraphs: list[Paragraph] = Field(default_factory=list)
    notes: list[TextItem] = Field(default_factory=list)
    actions: list[Action] = Field(default_factory=list)
    contact_channels: list[ContactChannel] = Field(default_factory=list)

    @model_validator(mode="after")
    def _meaningful(self) -> TextSection:
        if not (self.title or self.paragraphs or self.notes or self.actions or self.contact_channels):
            raise ValueError("text section must contain meaningful editorial content")
        return self


class CapabilityCard(EditorialModel):
    kind: Literal["capability"] = "capability"
    id: EditorialId
    title: PublicText
    paragraphs: list[Paragraph] = Field(min_length=1)
    examples: list[TextItem] = Field(default_factory=list)
    actions: list[Action] = Field(min_length=1)
    media: None = None


class TechnicalAreaCard(EditorialModel):
    kind: Literal["technical_area"] = "technical_area"
    id: EditorialId
    title: PublicText
    paragraphs: list[Paragraph] = Field(min_length=1)
    included: list[TextItem] = Field(default_factory=list)
    tags: list[TextItem] = Field(default_factory=list)


class ApplicationExampleCard(EditorialModel):
    kind: Literal["application_example"] = "application_example"
    id: EditorialId
    title: PublicText
    description: list[Paragraph] = Field(min_length=1)
    disciplines: list[CallToAction] = Field(min_length=1)

    @model_validator(mode="after")
    def _internal_disciplines(self) -> ApplicationExampleCard:
        if any(not isinstance(action.target, InternalLink) for action in self.disciplines):
            raise ValueError("application disciplines require internal references")
        return self


class SectorPreviewCard(EditorialModel):
    kind: Literal["sector_preview"] = "sector_preview"
    id: EditorialId
    title: PublicText
    paragraphs: list[Paragraph] = Field(default_factory=list)
    action: CallToAction | None = None


class DisciplineRelationCard(EditorialModel):
    kind: Literal["discipline_relation"] = "discipline_relation"
    id: EditorialId
    title: PublicText
    description: list[Paragraph] = Field(min_length=1)
    discipline: InternalLink


Card = Annotated[
    CapabilityCard | TechnicalAreaCard | ApplicationExampleCard | SectorPreviewCard | DisciplineRelationCard,
    Field(discriminator="kind"),
]


class EditorialAside(EditorialModel):
    """A transversal scope/diagnosis note, never an extra technical area."""

    id: EditorialId
    title: PublicText | None = None
    paragraphs: list[Paragraph] = Field(min_length=1)


class CardsSection(SectionBase):
    kind: Literal["cards"] = "cards"
    purpose: Literal["capabilities", "technical_areas", "application_examples", "sector_preview", "discipline_relations"]
    eyebrow: PublicText | None = None
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    items: list[Card] = Field(min_length=1)
    transversal: EditorialAside | None = None
    closing: list[Paragraph] = Field(default_factory=list)
    actions: list[Action] = Field(default_factory=list)
    media: None = None

    @model_validator(mode="after")
    def _purpose_matches_items(self) -> CardsSection:
        expected = {
            "capabilities": "capability", "technical_areas": "technical_area",
            "application_examples": "application_example", "sector_preview": "sector_preview",
            "discipline_relations": "discipline_relation",
        }[self.purpose]
        if any(item.kind != expected for item in self.items):
            raise ValueError(f"{self.purpose} requires {expected} items")
        if self.transversal is not None and self.purpose != "technical_areas":
            raise ValueError("transversal is only valid for technical areas")
        return self


class NeedItem(EditorialModel):
    kind: Literal["need"] = "need"
    id: EditorialId
    title: PublicText
    paragraphs: list[Paragraph] = Field(min_length=1)
    actions: list[Action] = Field(default_factory=list)


class DeliveryItem(EditorialModel):
    """Deliverables and modalities have the same editorial shape, not chronology."""

    kind: Literal["delivery"] = "delivery"
    id: EditorialId
    title: PublicText
    paragraphs: list[Paragraph] = Field(min_length=1)


ListItem = Annotated[NeedItem | DeliveryItem, Field(discriminator="kind")]


class ItemListSection(SectionBase):
    kind: Literal["item_list"] = "item_list"
    purpose: Literal["needs", "deliverables", "modalities"]
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    items: list[ListItem] = Field(min_length=1)
    notes: list[TextItem] = Field(default_factory=list)
    media: None = None

    @model_validator(mode="after")
    def _purpose_matches_items(self) -> ItemListSection:
        expected = "need" if self.purpose == "needs" else "delivery"
        if any(item.kind != expected for item in self.items):
            raise ValueError(f"{self.purpose} requires {expected} items")
        return self


class ProcessItem(EditorialModel):
    id: EditorialId
    title: PublicText
    paragraphs: list[Paragraph] = Field(min_length=1)


class ProcessSection(SectionBase):
    kind: Literal["process"] = "process"
    purpose: Literal["workflow", "principles"]
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    items: list[ProcessItem] = Field(min_length=1)
    closing: list[Paragraph] = Field(default_factory=list)
    actions: list[Action] = Field(default_factory=list)


class SectorIndexSection(SectionBase):
    kind: Literal["sector_index"] = "sector_index"
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    sector_refs: list[EditorialId] = Field(min_length=1)


class ExperienceEntry(EditorialModel):
    id: EditorialId
    experience_ref: EditorialId
    emphasis: Literal["featured", "complementary"]


class ExperienceGroup(EditorialModel):
    id: EditorialId
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    entries: list[ExperienceEntry] = Field(default_factory=list)

    @model_validator(mode="after")
    def _unique_experiences(self) -> ExperienceGroup:
        refs = [entry.experience_ref for entry in self.entries]
        if len(refs) != len(set(refs)):
            raise ValueError("duplicate experience references")
        return self


class ExperienceIndexSection(SectionBase):
    kind: Literal["experience_index"] = "experience_index"
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    groups: list[ExperienceGroup] = Field(min_length=1)


class TeamSection(SectionBase):
    kind: Literal["team"] = "team"
    title: PublicText
    introduction: list[Paragraph] = Field(default_factory=list)
    corporate_presentation: list[Paragraph] = Field(min_length=1)
    person_refs: list[EditorialId] = Field(min_length=1)


class FormField(EditorialModel):
    id: EditorialId
    label: PublicText
    # None preserves older editorial data without assuming its optionality.
    required: bool | None = None
    help: PublicText | None = None
    placeholder: PublicText | None = None


class FormMessages(EditorialModel):
    success: PublicText
    error: PublicText


class ContactFormSection(SectionBase):
    kind: Literal["form"] = "form"
    title: PublicText
    fields: list[FormField] = Field(min_length=1)
    help: list[TextItem] = Field(default_factory=list)
    submit_label: PublicText
    messages: FormMessages
    privacy_text: PublicText | None = None


Section = Annotated[
    HeroSection | TextSection | CardsSection | ItemListSection | ProcessSection
    | SectorIndexSection | ExperienceIndexSection | TeamSection | ContactFormSection,
    Field(discriminator="kind"),
]
