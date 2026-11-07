"""Editorial values. No routing, locale registry, I/O or publication policy."""

from __future__ import annotations

import re
from typing import Annotated, Literal

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, StringConstraints, model_validator


def _public_text(value: str) -> str:
    if not value.strip():
        raise ValueError("public text must contain non-whitespace characters")
    if re.search(r"\[\s*(?:pendiente|pending)\b", value, re.IGNORECASE):
        raise ValueError("record pending requirements in PendingField, not public text")
    return value


EditorialId = Annotated[str, StringConstraints(strict=True, pattern=r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")]
# WEB owns page identities. Its existing IDs include underscores (DEC-16).
# This is a boundary value constraint, not another page registry or routing model.
PageIdentity = Annotated[str, StringConstraints(strict=True, pattern=r"^[a-z][a-z0-9_]*$")]
# A code, not WEB's Locale configuration object. Membership is checked by A2's
# application context; importing localization here would invert the architecture.
LanguageCode = Annotated[str, StringConstraints(strict=True, pattern=r"^[a-z]{2}$")]
PublicText = Annotated[str, StringConstraints(strict=True), AfterValidator(_public_text)]
SourceRef = Annotated[str, StringConstraints(strict=True, min_length=1), AfterValidator(_public_text)]


class EditorialModel(BaseModel):
    """Frozen fields; ordered lists remain lists (not deeply immutable)."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True, validate_default=True)

    @model_validator(mode="after")
    def _unique_collection_ids(self) -> EditorialModel:
        for name in type(self).model_fields:
            values = getattr(self, name)
            if not isinstance(values, list):
                continue
            ids = [value.id for value in values if isinstance(value, BaseModel) and hasattr(value, "id")]
            if name.endswith("_refs") and all(isinstance(value, str) for value in values):
                ids = values
            if len(ids) != len(set(ids)):
                raise ValueError(f"duplicate IDs in {name}")
        return self


class Paragraph(EditorialModel):
    id: EditorialId
    text: PublicText


class TextItem(EditorialModel):
    id: EditorialId
    text: PublicText


class EditorialReview(EditorialModel):
    """Declared copy review, independent of structural validity and WEB release.

    approved may retain technical pending fields. A source reference records
    provenance; it never grants authorization or automatically changes status.
    """

    status: Literal["draft", "reviewed", "approved"]
    source_ref: SourceRef | None = None


class PendingField(EditorialModel):
    """Stable field selector, e.g. sections/h01/media; never a list offset."""

    field: Annotated[str, StringConstraints(strict=True, min_length=1), AfterValidator(_public_text)]
    reason_code: Literal[
        "approval_required", "verification_required", "authorization_required",
        "source_missing", "integration_pending",
    ]
    source_ref: SourceRef | None = None


class Verification(EditorialModel):
    """Evidence state, independent of copy approval and final publication."""

    verified: bool = False
    authorized: bool = False
    evidence_refs: list[SourceRef] = Field(default_factory=list)

    @model_validator(mode="after")
    def _evidence_required(self) -> Verification:
        if (self.verified or self.authorized) and not self.evidence_refs:
            raise ValueError("verification/authorization requires evidence")
        return self
