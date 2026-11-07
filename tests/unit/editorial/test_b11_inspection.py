"""B1.1 contracts validate inventory rather than asserting publication."""

from copy import deepcopy

import pytest
from pydantic import ValidationError

from bafras_web.editorial import PageContent, Person, Sector
from bafras_web.editorial.inspection import EditorialDiagnostic, EditorialDocument, EditorialInspection
from bafras_web.editorial.integrity import assess_integrity, build_editorial_bundle


@pytest.fixture
def inventory(editorial_bundle):
    documents = []
    for page in editorial_bundle.pages:
        data = page.model_dump()
        # The A1 synthetic fixture has a future form selector outside A2.1's
        # explicit grammar. This fixture tests B1 references, not that limitation.
        data["pending"] = [p for p in data["pending"] if p["field"] != "sections/co-02/privacy_text"]
        page = PageContent.model_validate(data)
        documents.append(EditorialDocument(document_id=f"page/{page.page_id}", kind="page",
                         source=f"es/pages/{page.page_id}.yaml", required=True, state="VALID", value=page))
    documents.append(EditorialDocument(document_id="common", kind="common", source="es/common.yaml",
                     required=False, state="VALID", value=editorial_bundle.common))
    for kind in ("people", "sectors", "experiences", "resources"):
        documents.append(EditorialDocument(document_id=f"catalog/{kind}", kind=kind,
                         source=f"es/entities/{kind}.yaml", required=kind != "resources", state="VALID",
                         value=tuple(getattr(editorial_bundle, kind))))
    return tuple(documents)


def inspection(documents, **values):
    return EditorialInspection(locale="es", policy="INCREMENTAL",
        expected_page_ids=tuple(d.document_id[5:] for d in documents if d.kind == "page"),
        documents=documents, **values)


@pytest.mark.parametrize("state,value", [("VALID", None), ("ABSENT", "page"), ("INVALID", "page")])
def test_document_state_requires_compatible_value(state, value, editorial_bundle):
    with pytest.raises(ValidationError):
        EditorialDocument(document_id="page/inicio", kind="page", source="es/pages/inicio.yaml",
            required=True, state=state, value=editorial_bundle.pages[0] if value else None)


@pytest.mark.parametrize("kind", ["people", "sectors", "experiences", "resources", "common"])
def test_wrong_value_kind_is_rejected(kind, editorial_bundle):
    wrong = (editorial_bundle.sectors[0],) if kind == "people" else (editorial_bundle.people[0],)
    if kind == "common":
        wrong = editorial_bundle.pages[0]
    with pytest.raises(ValidationError):
        EditorialDocument(document_id="common" if kind == "common" else f"catalog/{kind}", kind=kind,
            source=f"es/entities/{kind}.yaml", required=False, state="VALID", value=wrong)


@pytest.mark.parametrize("source", ["/etc/config.yaml", "C:/private/a.yaml", "../a.yaml", "es/../a.yaml", "es\\a.yaml", "es//a.yaml"])
def test_relative_sources_only(source):
    with pytest.raises(ValidationError):
        EditorialDiagnostic(code="YAML_ERROR", severity="error", message="Error YAML", source=source)


@pytest.mark.parametrize("update", [{"required": True}, {"state": "VALID"}, {"state": "ABSENT"}])
def test_unexpected_documents_cannot_satisfy_expected_content(update):
    data = dict(document_id="unexpected/es/extra.yaml", kind="unexpected", source="es/extra.yaml", required=False, state="INVALID")
    with pytest.raises(ValidationError):
        EditorialDocument(**{**data, **update})


def test_strict_extra_fields_and_frozen_models(inventory):
    data = inventory[0].model_dump()
    for changed in ({**data, "required": 1}, {**data, "state": "published"}, {**data, "published": True}):
        with pytest.raises(ValidationError):
            EditorialDocument.model_validate(changed)
    with pytest.raises(ValidationError):
        inventory[0].required = False
    result = inspection(inventory)
    with pytest.raises(TypeError):
        result.valid_pages["extra"] = inventory[0].value
    assert isinstance(result.documents, tuple) and isinstance(result.diagnostics, tuple)


def test_inventory_identity_locale_and_sources(inventory):
    data = inspection(inventory).model_dump()
    for mutation in ("duplicate", "missing", "locale", "source"):
        changed = deepcopy(data)
        if mutation == "duplicate":
            changed["documents"] += (changed["documents"][0],)
        elif mutation == "missing":
            changed["expected_page_ids"] += ("missing",)
        elif mutation == "locale":
            changed["locale"] = "en"
        else:
            changed["documents"][0]["source"] = "es/pages/wrong.yaml"
        with pytest.raises(ValidationError):
            EditorialInspection.model_validate(changed)


def test_invalid_context_is_not_vacuously_complete():
    result = EditorialInspection(locale="zz", policy="INCREMENTAL", expected_page_ids=(), documents=(), diagnostics=(
        EditorialDiagnostic(code="LOCALE_UNKNOWN", severity="error", message="Idioma desconocido"),))
    assert not result.documents_complete and not result.can_build_bundle
    assert result.has_errors
    with pytest.raises(ValueError, match="does not permit"):
        build_editorial_bundle(result)


def test_diagnostics_are_deterministic_and_keep_origins(inventory):
    base = dict(code="REFERENCE_UNKNOWN", severity="error", message="Referencia desconocida", selector="actions/a", target_id="missing")
    a = EditorialDiagnostic(**base, document_id="page/inicio", source="es/pages/inicio.yaml")
    b = EditorialDiagnostic(**base, document_id="page/contacto", source="es/pages/contacto.yaml")
    result = inspection(inventory, diagnostics=(b, a, a))
    assert len(result.diagnostics) == 2
    assert result.diagnostics == inspection(tuple(reversed(inventory)), diagnostics=(a, b)).diagnostics
    assert not result.can_build_bundle
    assert a.identity == EditorialDiagnostic(**{**a.model_dump(), "message": "Otro texto"}).identity


def test_catalog_duplicate_ids_rejected(editorial_bundle):
    person = editorial_bundle.people[0]
    with pytest.raises(ValidationError, match="Duplicate catalog identities"):
        EditorialDocument(document_id="catalog/people", kind="people", source="es/entities/people.yaml",
                          required=True, state="VALID", value=(person, person))


def test_complete_draft_bundle_preserves_content_and_no_publication(inventory):
    result = inspection(inventory)
    assert result.documents_complete and result.can_build_bundle
    assert not result.has_errors
    bundle = build_editorial_bundle(result)
    assert len(bundle.pages) == 9
    assert all(p.review.status == "draft" for p in bundle.pages)
    assert bundle.get_page("inicio").sections == result.valid_pages["inicio"].sections
    assert bundle.get_page("inicio").seo.title is None
    assert "publishable" not in type(result).model_fields
    assert "bundle" not in type(result).model_fields


def test_partial_bundle_and_invalid_optional_document_are_rejected(inventory):
    data = inventory[0]
    absent = EditorialDocument(document_id=data.document_id, kind="page", source=data.source, required=True, state="ABSENT")
    result = inspection((absent, *inventory[1:]))
    assert result.missing_page_ids == (data.value.page_id,)
    assert not result.can_build_bundle
    bad = EditorialDocument(document_id="unexpected/es/extra.yaml", kind="unexpected", source="es/extra.yaml", required=False, state="INVALID")
    result = inspection((*inventory, bad))
    assert result.documents_complete and not result.can_build_bundle
    with pytest.raises(ValueError):
        build_editorial_bundle(result)


def test_eligibility_does_not_trust_missing_diagnostics(inventory):
    data = list(inventory)
    doc = next(d for d in data if d.document_id == "page/inicio")
    page = doc.value.model_dump()
    page["sections"][0]["actions"][0]["target"]["page_id"] = "unknown"
    data[data.index(doc)] = EditorialDocument(document_id=doc.document_id, kind=doc.kind, source=doc.source,
                         required=True, state="VALID", value=PageContent.model_validate(page))
    result = inspection(tuple(data))
    assert result.diagnostics == () and not result.can_build_bundle
    with pytest.raises(ValueError):
        build_editorial_bundle(result)


@pytest.mark.parametrize("selector", ["sections/missing/media", "sections/h01/model_fields"])
def test_pending_grammar_is_reused(selector, inventory):
    doc = next(d for d in inventory if d.document_id == "page/inicio")
    page = doc.value.model_dump()
    page["pending"] = [{"field": selector, "reason_code": "integration_pending"}]
    changed = EditorialDocument(document_id=doc.document_id, kind="page", source=doc.source, required=True, state="VALID", value=PageContent.model_validate(page))
    documents = tuple(changed if d is doc else d for d in inventory)
    report = assess_integrity(documents, inspection(documents).expected_page_ids)
    assert any(d.code == "PENDING_SELECTOR_INVALID" and d.selector == selector for d in report.diagnostics)
    assert not inspection(documents).can_build_bundle


@pytest.mark.parametrize("location", ["hero", "text", "cards", "capability", "example", "preview", "discipline", "need", "process"])
def test_every_action_location_is_visited(location, inventory):
    pages = {d.value.page_id: d for d in inventory if d.kind == "page"}
    page_id = "capacidades" if location == "example" else ("automatizacion_control" if location == "discipline" else "inicio")
    doc = pages[page_id]
    data = doc.value.model_dump()
    sections = data["sections"]
    if location == "hero": target = sections[0]["actions"][0]["target"]
    elif location == "text": target = sections[-1]["actions"][0]["target"]
    elif location == "cards": target = sections[1]["actions"][0]["target"]
    elif location == "capability": target = sections[1]["items"][0]["actions"][0]["target"]
    elif location == "example": target = sections[2]["items"][0]["disciplines"][0]["target"]
    elif location == "preview":
        sections[4]["items"][0]["action"] = {"id": "test", "label": "Prueba", "target": {"kind": "internal", "page_id": "unknown"}}
        target = sections[4]["items"][0]["action"]["target"]
    elif location == "discipline": target = sections[4]["items"][0]["discipline"]
    elif location == "need": target = sections[2]["items"][0]["actions"][0]["target"]
    else: target = sections[3]["actions"][0]["target"]
    target["page_id"] = "unknown"
    changed = EditorialDocument(document_id=doc.document_id, kind="page", source=doc.source, required=True, state="VALID", value=PageContent.model_validate(data))
    documents = tuple(changed if d is doc else d for d in inventory)
    report = assess_integrity(documents, inspection(documents).expected_page_ids)
    assert any(d.code == "REFERENCE_UNKNOWN" and d.document_id == doc.document_id and d.target_id == "unknown" for d in report.diagnostics)


def test_empty_inspection_and_extra_fields_rejected_or_incomplete():
    result = EditorialInspection(locale="es", policy="COMPLETE", expected_page_ids=(), documents=())
    assert not result.documents_complete and not result.can_build_bundle
    with pytest.raises(ValidationError):
        EditorialInspection(locale="es", policy="COMPLETE", expected_page_ids=(), documents=(), success=True)


@pytest.mark.parametrize("location", ["team", "sector_index", "experience_index", "person", "experience", "common", "sector_action"])
def test_catalog_and_common_reference_locations(location, inventory):
    from bafras_web.editorial import CommonContent, Experience

    if location in ("team", "sector_index", "experience_index"):
        page_id, section_id = {
            "team": ("sobre_bafras", "sb-02"), "sector_index": ("sectores", "sec-02"),
            "experience_index": ("proyectos_experiencia", "pe-02"),
        }[location]
        doc = next(d for d in inventory if d.document_id == f"page/{page_id}")
        data = doc.value.model_dump()
        section = next(s for s in data["sections"] if s["id"] == section_id)
        if location == "team": section["person_refs"][0] = "unknown"
        elif location == "sector_index": section["sector_refs"][0] = "unknown"
        else: section["groups"][0]["entries"][0]["experience_ref"] = "unknown"
        value = PageContent.model_validate(data)
    elif location == "common":
        doc = next(d for d in inventory if d.kind == "common")
        data = doc.value.model_dump()
        data["actions"][0]["target"]["page_id"] = "unknown"
        value = CommonContent.model_validate(data)
    else:
        kind = {"person": "people", "experience": "experiences", "sector_action": "sectors"}[location]
        doc = next(d for d in inventory if d.kind == kind)
        data = doc.value[0].model_dump()
        if location == "person":
            data["experience_refs"] = ["unknown"]
            entity = Person.model_validate(data)
        elif location == "experience":
            data["person_refs"] = ["unknown"]
            entity = Experience.model_validate(data)
        else:
            data["contextual_actions"][0]["target"]["page_id"] = "unknown"
            entity = Sector.model_validate(data)
        value = (entity, *doc.value[1:])
    changed = EditorialDocument(document_id=doc.document_id, kind=doc.kind, source=doc.source,
                                 required=doc.required, state="VALID", value=value)
    documents = tuple(changed if d is doc else d for d in inventory)
    result = assess_integrity(documents, inspection(documents).expected_page_ids)
    assert any(d.code == "REFERENCE_UNKNOWN" and d.target_id == "unknown" for d in result.diagnostics)


def test_inspection_json_round_trip_and_diagnostic_path_guards(inventory):
    result = inspection(inventory)
    assert EditorialInspection.model_validate_json(result.model_dump_json()) == result
    for message in ("C:/private/file.yaml", "/private/file.yaml", "\\\\server\\file.yaml"):
        with pytest.raises(ValidationError):
            EditorialDiagnostic(code="DOCUMENT_INVALID", severity="error", message=message)


def test_valid_source_error_diagnostic_also_blocks_bundle(inventory):
    issue = EditorialDiagnostic(code="DOCUMENT_INVALID", severity="error", message="Error declarado")
    result = inspection(inventory, diagnostics=(issue,))
    assert result.documents_complete and not result.can_build_bundle
    with pytest.raises(ValueError):
        build_editorial_bundle(result)


@pytest.mark.parametrize("data", [
    {"code": "YAML_ERROR", "severity": "fatal", "message": "Error"},
    {"code": "UNKNOWN_CODE", "severity": "error", "message": "Error"},
    {"code": "YAML_ERROR", "severity": "error", "message": 1},
    {"code": "YAML_ERROR", "severity": "error", "message": "Error", "extra": True},
])
def test_diagnostic_contract_rejects_unknown_values_and_coercions(data):
    with pytest.raises(ValidationError):
        EditorialDiagnostic.model_validate(data)


def test_discovery_source_has_one_explicit_state():
    from pathlib import Path
    from bafras_web.adapters.editorial_files import EditorialSource

    assert EditorialSource(source="es/pages/inicio.yaml", path=Path("inicio.yaml")).error is None
    assert EditorialSource(source="es/pages/inicio.yaml", error="not_file").path is None
    for data in ({}, {"path": Path("inicio.yaml"), "error": "not_file"}):
        with pytest.raises(ValidationError):
            EditorialSource(source="es/pages/inicio.yaml", **data)
