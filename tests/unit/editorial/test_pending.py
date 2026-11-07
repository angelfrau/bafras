"""Pending identity/integrity is independent of copy review and publication."""

from copy import deepcopy
from pathlib import Path

import pytest
from pydantic import ValidationError

from bafras_web.adapters.yaml_files import load_yaml
from bafras_web.editorial import EditorialReview, PageContent
from bafras_web.editorial.pending import resolve_pending_selector, validate_pending_fields
from bafras_web.editorial.primitives import Verification

ROOT = Path(__file__).resolve().parents[3]


@pytest.fixture
def inicio_page():
    return PageContent.model_validate({**load_yaml(ROOT / "content/es/pages/inicio.yaml"), "locale": "es"})


@pytest.mark.parametrize("selector,status", [
    ("seo.title", "none"), ("seo.description", "none"),
    ("sections/h05/items", "collection"), ("sections/h01/media", "none"),
    ("sections/h02/items/infrastructure/media", "none"),
    ("sections/h02/items/energy/media", "none"),
    ("sections/h02/items/automation/media", "none"), ("sections/h03/media", "none"),
])
def test_eight_real_selectors(selector, status, inicio_page):
    result = resolve_pending_selector(inicio_page, selector)
    assert result.status == status
    if status == "collection":
        assert [item.id for item in result.value] == ["hospitality", "industry", "tertiary", "public-facilities"]
    else:
        assert result.value is None
    assert validate_pending_fields(inicio_page) == []


@pytest.mark.parametrize("selector", ["seo.title", "seo.description", "sections/h01/title", "sections/h01/subtitle",
                                       "sections/h01/eyebrow", "sections/h02/items/infrastructure/title"])
def test_populated_field_value(selector, inicio_page):
    data = inicio_page.model_dump()
    data["seo"] = {"title": "Título de prueba", "description": "Descripción de prueba"}
    page = PageContent.model_validate(data)
    assert resolve_pending_selector(page, selector).status == "value"
    assert isinstance(resolve_pending_selector(page, selector).value, str)
    # A supplied title does not implicitly clear approval_required.
    assert validate_pending_fields(page) == []
    assert page.pending == inicio_page.pending


@pytest.mark.parametrize("selector,status", [
    ("sections/missing/media", "section_not_found"),
    ("sections/h02/items/missing/media", "item_not_found"),
    ("seo.robots", "field_not_allowed"),
    ("sections/h01/model_fields", "field_not_allowed"),
    ("sections/h01/actions", "field_not_allowed"),
    ("sections/h04/media", "field_not_allowed"),
    ("sections/h01/items", "field_not_allowed"),
    ("sections/h01/items/example/title", "field_not_allowed"),
    ("sections/h05/items/hospitality/media", "field_not_allowed"),
    ("sections/h02/items/energy/model_dump", "field_not_allowed"),
    ("", "invalid_syntax"), ("seo/title", "invalid_syntax"),
    ("seo.title.extra", "invalid_syntax"), (" seo.title", "invalid_syntax"),
    ("sections/0/media", "invalid_syntax"),
    ("sections/h02/items/0/media", "invalid_syntax"),
    ("sections/h02/items/energy/media/extra", "invalid_syntax"),
    ("sections/h02/paragraphs/description/text", "invalid_syntax"),
    ("sections/h02/items//media", "invalid_syntax"),
    ("sections/h01/__dict__", "invalid_syntax"),
])
def test_bad_selectors_have_local_diagnostics(selector, status, inicio_page):
    assert resolve_pending_selector(inicio_page, selector).status == status
    data = inicio_page.model_dump()
    data["pending"] = [{"field": selector or " ", "reason_code": "integration_pending"}]
    if not selector:
        with pytest.raises(ValidationError):
            PageContent.model_validate(data)
        return
    page = PageContent.model_validate(data)
    diagnostics = validate_pending_fields(page)
    assert len(diagnostics) == 1
    diagnostic = diagnostics[0]
    assert (diagnostic.page_id, diagnostic.selector, diagnostic.reason_code, diagnostic.code) == (
        "inicio", selector, "integration_pending", status)
    assert "inicio" in diagnostic.message and selector in diagnostic.message
    assert "integration_pending" in diagnostic.message


def test_card_reordering_preserves_selector_identity(inicio_page):
    selector = "sections/h02/items/infrastructure/title"
    before = resolve_pending_selector(inicio_page, selector)
    data = deepcopy(inicio_page.model_dump())
    data["sections"][1]["items"].reverse()
    data["sections"].reverse()
    reordered = PageContent.model_validate(data)
    assert resolve_pending_selector(reordered, selector) == before
    assert validate_pending_fields(reordered) == []


def test_duplicate_section_and_item_ids_still_rejected(inicio_page):
    for field in ("sections", "items"):
        data = deepcopy(inicio_page.model_dump())
        collection = data["sections"] if field == "sections" else data["sections"][1]["items"]
        collection.append(deepcopy(collection[-1]))
        with pytest.raises(ValidationError, match="duplicate"):
            PageContent.model_validate(data)


@pytest.mark.parametrize("status", ["draft", "reviewed", "approved"])
def test_structural_validity_local_integrity_and_review_are_independent(status, inicio_page):
    data = inicio_page.model_dump()
    data["review"] = {"status": status, "source_ref": "D03 H01–H07"}
    page = PageContent.model_validate(data)
    snapshot = deepcopy(page.model_dump())
    assert validate_pending_fields(page) == []
    assert all(resolve_pending_selector(page, pending.field).status in ("none", "collection") for pending in page.pending)
    assert page.model_dump() == snapshot
    assert page.review.status == status
    assert len(page.pending) == 8 and page.seo.title is None
    assert "published" not in type(page).model_fields
    # A documentary reference records review; it is not an authorization grant.
    assert not Verification().authorized


def test_structural_validity_does_not_prove_selector_integrity(inicio_page):
    data = inicio_page.model_dump()
    data["pending"] = [{"field": "sections/missing/media", "reason_code": "integration_pending"}]
    page = PageContent.model_validate(data)
    assert validate_pending_fields(page)[0].code == "section_not_found"
    assert page.review.status == "draft"


def test_no_extra_review_states_or_document_implied_authorization():
    with pytest.raises(ValidationError):
        EditorialReview(status="published")
    assert EditorialReview(status="approved", source_ref="D03").status == "approved"
    assert not Verification(evidence_refs=["D03"]).authorized


@pytest.mark.parametrize("selector,status", [
    ("sections/h03/items", "collection"), ("sections/h04/items", "collection"),
    ("sections/h02/eyebrow", "none"),
    ("sections/h03/items/installation-performance/title", "value"),
    ("sections/h04/items/understand/title", "value"),
])
def test_explicit_section_and_item_fields(selector, status, inicio_page):
    assert resolve_pending_selector(inicio_page, selector).status == status


def test_diagnostics_accumulate_without_changing_the_page(inicio_page):
    data = inicio_page.model_dump()
    data["pending"] = [
        {"field": "sections/missing/title", "reason_code": "approval_required"},
        {"field": "seo.robots", "reason_code": "integration_pending"},
    ]
    page = PageContent.model_validate(data)
    snapshot = deepcopy(page.model_dump())
    assert [issue.code for issue in validate_pending_fields(page)] == ["section_not_found", "field_not_allowed"]
    assert page.model_dump() == snapshot
