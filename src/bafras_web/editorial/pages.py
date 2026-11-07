"""Pages and an in-memory bundle. No file loading or cross-file resolution."""

from __future__ import annotations

from pydantic import Field, model_validator

from .entities import DownloadableResource, Experience, Person, Sector
from .primitives import (
    EditorialModel, EditorialReview, LanguageCode, PageIdentity,
    PendingField, PublicText, TextItem,
)
from .references import CallToAction
from .sections import Section


class SeoMeta(EditorialModel):
    title: PublicText | None = None
    description: PublicText | None = None


class PageContent(EditorialModel):
    page_id: PageIdentity
    locale: LanguageCode
    review: EditorialReview
    seo: SeoMeta
    sections: list[Section] = Field(min_length=1)
    pending: list[PendingField] = Field(default_factory=list)

    @model_validator(mode="after")
    def _one_hero(self) -> PageContent:
        if sum(section.kind == "hero" for section in self.sections) != 1:
            raise ValueError("page must contain exactly one hero")
        return self


class CommonContent(EditorialModel):
    navigation_labels: list[TextItem] = Field(default_factory=list)
    footer_texts: list[TextItem] = Field(default_factory=list)
    actions: list[CallToAction] = Field(default_factory=list)
    interface_messages: list[TextItem] = Field(default_factory=list)


class EditorialBundle(EditorialModel):
    locale: LanguageCode
    pages: list[PageContent] = Field(default_factory=list)
    common: CommonContent = Field(default_factory=CommonContent)
    people: list[Person] = Field(default_factory=list)
    sectors: list[Sector] = Field(default_factory=list)
    experiences: list[Experience] = Field(default_factory=list)
    resources: list[DownloadableResource] = Field(default_factory=list)

    @model_validator(mode="after")
    def _local_identity(self) -> EditorialBundle:
        page_ids = [page.page_id for page in self.pages]
        catalog_ids = [resource.catalog_id for resource in self.resources]
        if len(page_ids) != len(set(page_ids)) or len(catalog_ids) != len(set(catalog_ids)):
            raise ValueError("duplicate page/catalog IDs")
        if any(page.locale != self.locale for page in self.pages):
            raise ValueError("all pages must have the bundle locale")
        return self

    def get_page(self, page_id: str) -> PageContent:
        for page in self.pages:
            if page.page_id == page_id:
                return page
        raise KeyError(page_id)

    def get_common(self) -> CommonContent:
        return self.common

    def get_person(self, person_id: str) -> Person:
        for person in self.people:
            if person.id == person_id:
                return person
        raise KeyError(person_id)

    def get_sector(self, sector_id: str) -> Sector:
        for sector in self.sectors:
            if sector.id == sector_id:
                return sector
        raise KeyError(sector_id)

    def get_experience(self, experience_id: str) -> Experience:
        for experience in self.experiences:
            if experience.id == experience_id:
                return experience
        raise KeyError(experience_id)

    def get_resource(self, catalog_id: str) -> DownloadableResource:
        for resource in self.resources:
            if resource.catalog_id == catalog_id:
                return resource
        raise KeyError(catalog_id)
