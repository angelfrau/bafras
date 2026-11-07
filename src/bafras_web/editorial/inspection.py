"""Inspection contracts: inventory and integrity are not review or publication."""

from __future__ import annotations

import re
from types import MappingProxyType
from typing import Annotated, Literal, Mapping

from pydantic import AfterValidator, TypeAdapter, field_validator, model_validator
from pydantic_core import PydanticCustomError

from .entities import DownloadableResource, Experience, Person, Sector
from .pages import CommonContent, PageContent
from .primitives import EditorialModel, PageIdentity, PublicText

CompletenessPolicy = Literal["INCREMENTAL", "COMPLETE"]
DiagnosticSeverity = Literal["error", "warning", "info"]
ReferenceStatus = Literal["RESOLVED", "UNRESOLVED", "UNVERIFIABLE"]
DocumentState = Literal["ABSENT", "VALID", "INVALID"]
CatalogKind = Literal["common", "people", "sectors", "experiences", "resources"]
DocumentKind = Literal["page", "common", "people", "sectors", "experiences", "resources", "unexpected"]
DiagnosticCode = Literal[
    "LOCALE_UNKNOWN", "DOCUMENT_MISSING", "DOCUMENT_UNEXPECTED", "DOCUMENT_READ_ERROR",
    "YAML_ERROR", "DOCUMENT_ROOT_INVALID", "DOCUMENT_INVALID", "DOCUMENT_ID_MISMATCH",
    "DOCUMENT_LOCALE_MISMATCH", "DUPLICATE_ENTITY_ID", "REFERENCE_RESOLVED",
    "REFERENCE_UNKNOWN", "REFERENCE_SECTION_UNKNOWN", "REFERENCE_TARGET_UNAVAILABLE",
    "RESOURCE_SECTOR_MISMATCH", "REFERENCES_SKIPPED_INVALID_SOURCE", "PENDING_SELECTOR_INVALID",
    "EDITORIAL_PENDING", "ENTITY_PENDING_UNCHECKED", "EXTERNAL_CONTACT_UNCHECKED",
    "EXTERNAL_RESOURCE_UNCHECKED", "EXTERNAL_EVIDENCE_UNCHECKED", "EXTERNAL_URL_UNCHECKED",
]
CATALOG_FILES: Mapping[CatalogKind, str] = MappingProxyType({
    "common": "common.yaml", "people": "entities/people.yaml", "sectors": "entities/sectors.yaml",
    "experiences": "entities/experiences.yaml", "resources": "entities/resources.yaml",
})
_PAGE_ID = TypeAdapter(PageIdentity)


def _relative_source(value: str) -> str:
    if "\\" in value or ":" in value or any(part in ("", ".", "..") for part in value.split("/")):
        raise ValueError("source must be a relative POSIX path without traversal")
    return value


RelativeSource = Annotated[PublicText, AfterValidator(_relative_source)]
DocumentValue = (
    PageContent | CommonContent | tuple[Person, ...] | tuple[Sector, ...]
    | tuple[Experience, ...] | tuple[DownloadableResource, ...]
)


class EditorialDiagnostic(EditorialModel):
    code: DiagnosticCode
    severity: DiagnosticSeverity
    message: PublicText
    document_id: PublicText | None = None
    source: RelativeSource | None = None
    selector: str | None = None
    target_id: str | None = None
    target_document_id: str | None = None
    reference_status: ReferenceStatus | None = None
    reason_code: str | None = None

    @field_validator("message")
    @classmethod
    def _no_absolute_paths(cls, value: str) -> str:
        if re.search(r"[A-Za-z]:[\\/]|\\\\|(?<!\w)/[^\s]", value):
            raise ValueError("diagnostic messages must not contain absolute paths")
        return value

    @property
    def identity(self) -> tuple[str, ...]:
        # source matters for diagnostics without a document, e.g. discovery errors.
        return tuple(value or "" for value in (
            self.code, self.document_id, self.source, self.selector,
            self.target_document_id, self.target_id, self.reason_code,
        ))


def ordered_diagnostics(values: tuple[EditorialDiagnostic, ...]) -> tuple[EditorialDiagnostic, ...]:
    rank = {"error": 0, "warning": 1, "info": 2}
    unique: dict[tuple[str, ...], EditorialDiagnostic] = {}
    for value in sorted(values, key=lambda d: (d.identity, rank[d.severity], d.message)):
        unique.setdefault(value.identity, value)
    return tuple(sorted(unique.values(), key=lambda d: (
        d.source or "", d.document_id or "", d.selector or "", d.code,
        d.target_document_id or "", d.target_id or "", d.reason_code or "",
    )))


class EditorialDocument(EditorialModel):
    document_id: PublicText
    kind: DocumentKind
    source: RelativeSource
    required: bool
    state: DocumentState
    value: DocumentValue | None = None

    @model_validator(mode="after")
    def _contract(self) -> EditorialDocument:
        if self.kind == "unexpected":
            if self.required or self.state != "INVALID" or self.document_id != f"unexpected/{self.source}":
                raise ValueError("unexpected documents must be invalid, optional and identified by source")
        elif self.kind == "page":
            if not self.document_id.startswith("page/") or not self.required:
                raise ValueError("page documents require a page identity and are required")
            _PAGE_ID.validate_python(self.document_id.removeprefix("page/"))
        elif self.document_id != ("common" if self.kind == "common" else f"catalog/{self.kind}"):
            raise ValueError("catalog document identity does not match kind")
        if self.state != "VALID":
            if self.value is not None:
                raise ValueError("absent/invalid documents cannot contain a value")
            return self
        if self.kind == "page":
            if not isinstance(self.value, PageContent) or self.document_id != f"page/{self.value.page_id}":
                raise ValueError("page value must match its document identity")
        elif self.kind == "common":
            if not isinstance(self.value, CommonContent):
                raise ValueError("common requires CommonContent")
        else:
            expected = {"people": Person, "sectors": Sector, "experiences": Experience, "resources": DownloadableResource}.get(self.kind)
            if expected is None or not isinstance(self.value, tuple) or any(not isinstance(v, expected) for v in self.value):
                raise ValueError("catalog value is incompatible with kind")
            ids = [v.catalog_id if isinstance(v, DownloadableResource) else v.id for v in self.value]
            if len(ids) != len(set(ids)):
                raise PydanticCustomError("duplicate_entity_id", "Duplicate catalog identities")
        return self


class IntegrityResult(EditorialModel):
    required_catalogs: tuple[CatalogKind, ...] = ()
    diagnostics: tuple[EditorialDiagnostic, ...] = ()


class EditorialInspection(EditorialModel):
    locale: PublicText
    policy: CompletenessPolicy
    expected_page_ids: tuple[PageIdentity, ...]
    documents: tuple[EditorialDocument, ...]
    diagnostics: tuple[EditorialDiagnostic, ...] = ()

    @field_validator("expected_page_ids")
    @classmethod
    def _expected_ids(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        if len(values) != len(set(values)):
            raise ValueError("duplicate expected page IDs")
        return tuple(sorted(values))

    @field_validator("documents")
    @classmethod
    def _documents(cls, values: tuple[EditorialDocument, ...]) -> tuple[EditorialDocument, ...]:
        if len({v.document_id for v in values}) != len(values) or len({v.source for v in values}) != len(values):
            raise ValueError("duplicate document identities or sources")
        return tuple(sorted(values, key=lambda v: (v.source, v.document_id)))

    @field_validator("diagnostics")
    @classmethod
    def _diagnostics(cls, values: tuple[EditorialDiagnostic, ...]) -> tuple[EditorialDiagnostic, ...]:
        return ordered_diagnostics(values)

    @model_validator(mode="after")
    def _inventory(self) -> EditorialInspection:
        pages = {d.document_id.removeprefix("page/"): d for d in self.documents if d.kind == "page"}
        if set(pages) != set(self.expected_page_ids):
            raise ValueError("inventory must contain exactly the expected page documents")
        if any(d.code == "LOCALE_UNKNOWN" for d in self.diagnostics) and (self.documents or self.expected_page_ids):
            raise ValueError("invalid locale context cannot contain content")
        for doc in self.documents:
            if doc.kind == "page":
                relative = f"pages/{doc.document_id.removeprefix('page/')}.yaml"
                if isinstance(doc.value, PageContent) and doc.value.locale != self.locale:
                    raise ValueError("page locale differs from inspection")
            elif doc.kind in CATALOG_FILES:
                relative = CATALOG_FILES[doc.kind]
            else:
                if not doc.source.startswith(f"{self.locale}/"):
                    raise ValueError("unexpected source outside the requested locale")
                continue
            if doc.source != f"{self.locale}/{relative}":
                raise ValueError("source differs from its expected document location")
        return self

    @property
    def valid_pages(self) -> Mapping[str, PageContent]:
        return MappingProxyType({d.value.page_id: d.value for d in self.documents if isinstance(d.value, PageContent)})

    @property
    def missing_page_ids(self) -> tuple[str, ...]:
        return tuple(pid for pid in self.expected_page_ids if any(d.document_id == f"page/{pid}" and d.state == "ABSENT" for d in self.documents))

    @property
    def invalid_page_ids(self) -> tuple[str, ...]:
        return tuple(pid for pid in self.expected_page_ids if any(d.document_id == f"page/{pid}" and d.state == "INVALID" for d in self.documents))

    @property
    def documents_complete(self) -> bool:
        return bool(self.expected_page_ids) and all(d.state == "VALID" for d in self.documents if d.required)

    @property
    def has_errors(self) -> bool:
        return any(d.severity == "error" for d in self.diagnostics)

    @property
    def can_build_bundle(self) -> bool:
        # The rule also rechecks content so a hand-built inspection cannot omit
        # diagnostics to bypass integrity. Local import avoids an eager module cycle.
        from .integrity import bundle_is_eligible

        return bundle_is_eligible(self)
