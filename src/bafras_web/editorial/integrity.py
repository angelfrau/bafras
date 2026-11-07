"""Pure cross-document identity checks and the shared bundle eligibility rule."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import get_args

from .entities import DownloadableResource, Experience, Person, Sector, SectorId
from .inspection import (
    CatalogKind, DiagnosticCode, DiagnosticSeverity, EditorialDiagnostic, EditorialDocument,
    EditorialInspection, IntegrityResult, ReferenceStatus, ordered_diagnostics,
)
from .pages import CommonContent, EditorialBundle, PageContent
from .pending import validate_pending_fields
from .primitives import EditorialModel
from .references import Action, ContactLink, ExternalLink, InternalLink, LinkRef, ResourceLink, SharedActionRef
from .sections import (
    ApplicationExampleCard, CapabilityCard, CardsSection, DisciplineRelationCard,
    ExperienceIndexSection, HeroSection, ItemListSection, NeedItem, ProcessSection,
    SectorIndexSection, SectorPreviewCard, TeamSection, TextSection,
)

ReferenceTarget = LinkRef | SharedActionRef | tuple[CatalogKind, str]
ReferenceUse = tuple[str, ReferenceTarget]
_SECTOR_IDS = frozenset(get_args(SectorId))


def _actions(actions: Sequence[Action], prefix: str) -> Iterator[ReferenceUse]:
    for action in actions:
        selector = f"{prefix}/{action.id}"
        yield (selector, action) if isinstance(action, SharedActionRef) else (f"{selector}/target", action.target)


def _page_references(page: PageContent) -> Iterator[ReferenceUse]:
    for section in page.sections:
        prefix = f"sections/{section.id}"
        if isinstance(section, (HeroSection, TextSection, CardsSection, ProcessSection)):
            yield from _actions(section.actions, f"{prefix}/actions")
        if isinstance(section, TextSection):
            for channel in section.contact_channels:
                yield f"{prefix}/contact_channels/{channel.id}/target", channel.target
        elif isinstance(section, CardsSection):
            for item in section.items:
                path = f"{prefix}/items/{item.id}"
                if isinstance(item, CapabilityCard):
                    yield from _actions(item.actions, f"{path}/actions")
                elif isinstance(item, ApplicationExampleCard):
                    yield from _actions(item.disciplines, f"{path}/disciplines")
                elif isinstance(item, SectorPreviewCard) and item.action is not None:
                    yield from _actions([item.action], f"{path}/action")
                elif isinstance(item, DisciplineRelationCard):
                    yield f"{path}/discipline", item.discipline
        elif isinstance(section, ItemListSection):
            for item in section.items:
                if isinstance(item, NeedItem):
                    yield from _actions(item.actions, f"{prefix}/items/{item.id}/actions")
        elif isinstance(section, SectorIndexSection):
            for ref in section.sector_refs:
                yield f"{prefix}/sector_refs/{ref}", ("sectors", ref)
        elif isinstance(section, TeamSection):
            for ref in section.person_refs:
                yield f"{prefix}/person_refs/{ref}", ("people", ref)
        elif isinstance(section, ExperienceIndexSection):
            for group in section.groups:
                for entry in group.entries:
                    yield f"{prefix}/groups/{group.id}/entries/{entry.id}", ("experiences", entry.experience_ref)


def _references(doc: EditorialDocument) -> Iterator[ReferenceUse]:
    value = doc.value
    if isinstance(value, PageContent):
        yield from _page_references(value)
    elif isinstance(value, CommonContent):
        yield from _actions(value.actions, "actions")
    elif isinstance(value, tuple):
        for entity in value:
            if isinstance(entity, Person):
                for ref in entity.experience_refs:
                    yield f"people/{entity.id}/experience_refs/{ref}", ("experiences", ref)
            elif isinstance(entity, Experience):
                for ref in entity.person_refs:
                    yield f"experiences/{entity.id}/person_refs/{ref}", ("people", ref)
            elif isinstance(entity, Sector):
                yield from _actions(entity.contextual_actions, f"sectors/{entity.id}/contextual_actions")
                for ref in entity.catalog_refs:
                    yield f"sectors/{entity.id}/catalog_refs/{ref.catalog_id}", ref
            elif isinstance(entity, DownloadableResource):
                yield f"resources/{entity.catalog_id}/sector_id", ("sectors", entity.sector_id)


def assess_integrity(
    documents: tuple[EditorialDocument, ...], expected_page_ids: tuple[str, ...], *,
    report_resolved: bool = False,
) -> IntegrityResult:
    """Resolve only the explicitly typed relationships; reciprocal links are valid."""
    docs = {doc.document_id: doc for doc in documents}
    pages = {doc.value.page_id: doc.value for doc in documents if isinstance(doc.value, PageContent)}
    indexes: dict[str, dict[str, EditorialModel]] = {}
    for doc in documents:
        if isinstance(doc.value, CommonContent):
            indexes[doc.document_id] = {a.id: a for a in doc.value.actions}
        elif isinstance(doc.value, tuple):
            indexes[doc.document_id] = {
                e.catalog_id if isinstance(e, DownloadableResource) else e.id: e for e in doc.value
            }
    diagnostics: list[EditorialDiagnostic] = []
    required: set[CatalogKind] = set()
    for doc in documents:
        def emit(
            code: DiagnosticCode, severity: DiagnosticSeverity, selector: str, message: str,
            target_id: str | None = None, target_document_id: str | None = None,
            status: ReferenceStatus | None = None, reason: str | None = None,
        ) -> None:
            diagnostics.append(EditorialDiagnostic(
                code=code, severity=severity, message=message, document_id=doc.document_id,
                source=doc.source, selector=selector, target_id=target_id,
                target_document_id=target_document_id, reference_status=status, reason_code=reason,
            ))

        if doc.state == "INVALID":
            emit("REFERENCES_SKIPPED_INVALID_SOURCE", "info", "", "Referencias no examinadas en documento inválido")
        for selector, target in _references(doc):
            if isinstance(target, (ExternalLink, ContactLink)):
                code: DiagnosticCode = "EXTERNAL_URL_UNCHECKED" if isinstance(target, ExternalLink) else "EXTERNAL_CONTACT_UNCHECKED"
                emit(code, "info", selector, "Forma validada; disponibilidad externa no comprobada", status="UNVERIFIABLE")
                continue
            if isinstance(target, InternalLink):
                target_doc = f"page/{target.page_id}"
                if target.page_id not in expected_page_ids:
                    emit("REFERENCE_UNKNOWN", "error", selector, "Página no configurada", target.page_id, target_doc, "UNRESOLVED")
                elif target.page_id not in pages:
                    emit("REFERENCE_TARGET_UNAVAILABLE", "warning", selector, "Documento destino ausente o inválido", target.page_id, target_doc, "UNVERIFIABLE")
                elif target.section_id is not None and target.section_id not in {s.id for s in pages[target.page_id].sections}:
                    emit("REFERENCE_SECTION_UNKNOWN", "error", selector, "Sección destino inexistente", target.section_id, target_doc, "UNRESOLVED")
                elif report_resolved:
                    emit("REFERENCE_RESOLVED", "info", selector, "Referencia editorial resuelta", target.section_id or target.page_id, target_doc, "RESOLVED")
                continue
            if isinstance(target, SharedActionRef):
                kind, target_id = "common", target.common_ref
            elif isinstance(target, ResourceLink):
                kind, target_id = "resources", target.catalog_id
            else:
                kind, target_id = target
            required.add(kind)
            target_doc = "common" if kind == "common" else f"catalog/{kind}"
            if kind == "sectors" and target_id not in _SECTOR_IDS:
                emit("REFERENCE_UNKNOWN", "error", selector, "Identidad sectorial no canónica", target_id, target_doc, "UNRESOLVED")
            elif target_doc not in indexes:
                emit("REFERENCE_TARGET_UNAVAILABLE", "warning", selector, "Catálogo destino ausente o inválido", target_id, target_doc, "UNVERIFIABLE")
            elif target_id not in indexes[target_doc]:
                emit("REFERENCE_UNKNOWN", "error", selector, "Identidad inexistente en catálogo válido", target_id, target_doc, "UNRESOLVED")
            else:
                if report_resolved:
                    emit("REFERENCE_RESOLVED", "info", selector, "Referencia editorial resuelta", target_id, target_doc, "RESOLVED")
                entity = indexes[target_doc][target_id]
                if isinstance(entity, DownloadableResource) and isinstance(doc.value, tuple):
                    for sector in doc.value:
                        if isinstance(sector, Sector) and selector.startswith(f"sectors/{sector.id}/catalog_refs/") and sector.id != entity.sector_id:
                            emit("RESOURCE_SECTOR_MISMATCH", "error", selector, "El catálogo pertenece a otro sector", target_id, target_doc, "UNRESOLVED")
        if isinstance(doc.value, PageContent):
            invalid = {issue.selector for issue in validate_pending_fields(doc.value)}
            for pending in doc.value.pending:
                emit(
                    "PENDING_SELECTOR_INVALID" if pending.field in invalid else "EDITORIAL_PENDING",
                    "error" if pending.field in invalid else "info", pending.field,
                    "Selector de pendiente inválido" if pending.field in invalid else "Pendiente editorial declarado",
                    reason=pending.reason_code,
                )
        elif isinstance(doc.value, tuple):
            for entity in doc.value:
                if isinstance(entity, (Person, Experience)):
                    for pending in entity.pending:
                        emit("ENTITY_PENDING_UNCHECKED", "warning", f"{doc.kind}/{entity.id}/{pending.field}",
                             "Selector de entidad conservado sin resolver", reason=pending.reason_code)
                    evidence = entity.verification.evidence_refs
                    if isinstance(entity, Experience):
                        evidence = [*evidence, *entity.evidence_refs, *(ref for result in entity.results for ref in result.evidence_refs)]
                    if evidence:
                        emit("EXTERNAL_EVIDENCE_UNCHECKED", "info", f"{doc.kind}/{entity.id}/evidence_refs", "Evidencia declarada no verificada", status="UNVERIFIABLE")
                elif isinstance(entity, DownloadableResource):
                    emit("EXTERNAL_RESOURCE_UNCHECKED", "info", f"resources/{entity.catalog_id}", "Disponibilidad física y derechos fuera de alcance", status="UNVERIFIABLE")
    return IntegrityResult(required_catalogs=tuple(sorted(required)), diagnostics=ordered_diagnostics(tuple(diagnostics)))


def bundle_is_eligible(inspection: EditorialInspection) -> bool:
    """Single rule used by both can_build_bundle and the controlled constructor."""
    if not inspection.documents_complete or inspection.has_errors or any(d.state == "INVALID" for d in inspection.documents):
        return False
    report = assess_integrity(inspection.documents, inspection.expected_page_ids)
    docs = {doc.kind: doc for doc in inspection.documents if doc.kind != "page"}
    if any(kind not in docs or docs[kind].state != "VALID" for kind in report.required_catalogs):
        return False
    return not any(
        d.severity == "error" or (d.reference_status in ("UNRESOLVED", "UNVERIFIABLE") and not d.code.startswith("EXTERNAL_"))
        for d in (*inspection.diagnostics, *report.diagnostics)
    )


def build_editorial_bundle(inspection: EditorialInspection) -> EditorialBundle:
    if not inspection.can_build_bundle:
        raise ValueError("Editorial inspection does not permit a complete, integral bundle")
    common = next((d.value for d in inspection.documents if isinstance(d.value, CommonContent)), CommonContent())
    entities = [entity for d in inspection.documents if isinstance(d.value, tuple) for entity in d.value]
    return EditorialBundle(
        locale=inspection.locale, pages=list(inspection.valid_pages.values()), common=common,
        people=[e for e in entities if isinstance(e, Person)], sectors=[e for e in entities if isinstance(e, Sector)],
        experiences=[e for e in entities if isinstance(e, Experience)],
        resources=[e for e in entities if isinstance(e, DownloadableResource)],
    )
