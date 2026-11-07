"""Unresolved semantic destinations and local/shared editorial actions."""

from typing import Annotated, Literal

from pydantic import Field, HttpUrl

from .primitives import EditorialId, EditorialModel, PageIdentity, PublicText


class InternalLink(EditorialModel):
    kind: Literal["internal"] = "internal"
    page_id: PageIdentity
    section_id: EditorialId | None = None


class ExternalLink(EditorialModel):
    kind: Literal["external"] = "external"
    url: HttpUrl


class ContactLink(EditorialModel):
    kind: Literal["contact"] = "contact"
    channel: Literal["email", "phone"]


class ResourceLink(EditorialModel):
    kind: Literal["resource"] = "resource"
    catalog_id: EditorialId


LinkRef = Annotated[InternalLink | ExternalLink | ContactLink | ResourceLink, Field(discriminator="kind")]


class CallToAction(EditorialModel):
    id: EditorialId
    label: PublicText
    target: LinkRef


class SharedActionRef(EditorialModel):
    id: EditorialId
    common_ref: EditorialId


# Shapes are mutually exclusive because unknown fields are forbidden.
Action = CallToAction | SharedActionRef
