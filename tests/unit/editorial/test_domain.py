"""Negative and boundary tests for the A1 editorial domain."""

from copy import deepcopy

import pytest
from pydantic import TypeAdapter, ValidationError

from bafras_web.editorial import (
    CallToAction, CommonContent, ContactLink, DownloadableResource, EditorialBundle,
    EditorialReview, Experience, ExternalLink, InternalLink, PageContent, Paragraph,
    PendingField, Person, ResourceLink, Section, SharedActionRef, TextSection,
)
from bafras_web.editorial.entities import DocumentedResult
from bafras_web.editorial.primitives import EditorialId, PublicText, Verification
from bafras_web.editorial.references import Action, LinkRef


@pytest.mark.parametrize("value", ["home", "h01", "inf-03", "dig-w03", "turismo-terciario"])
def test_editorial_ids(value):
    assert TypeAdapter(EditorialId).validate_python(value) == value


@pytest.mark.parametrize("value", ["", " home", "with space", "two--hyphens", "UPPER", "a_b", "área", 1, True])
def test_invalid_editorial_ids(value):
    with pytest.raises(ValidationError):
        TypeAdapter(EditorialId).validate_python(value)


@pytest.mark.parametrize("value", ["", " \t\n", 1, None, True, "[PENDIENTE]", "Texto [pendiente de confirmar]"])
def test_invalid_public_text(value):
    with pytest.raises(ValidationError):
        TypeAdapter(PublicText).validate_python(value)


def test_public_copy_is_preserved_and_fields_frozen():
    text = "  Àngel — Ingeniería.\nSegunda línea.  "
    paragraph = Paragraph(id="original", text=text)
    assert paragraph.text == text
    with pytest.raises(ValidationError, match="frozen_instance"):
        paragraph.text = "Changed"
    with pytest.raises(ValidationError, match="extra_forbidden"):
        Paragraph(id="original", text=text, css="layout")


@pytest.mark.parametrize("reason", ["approval_required", "verification_required", "authorization_required", "source_missing", "integration_pending"])
def test_typed_pending_reasons(reason):
    assert PendingField(field="sections/h01/media", reason_code=reason).reason_code == reason


def test_unknown_states_and_empty_pending_fields_are_rejected():
    for model, data in [(EditorialReview, {"status": "published"}),
                        (PendingField, {"field": " ", "reason_code": "source_missing"}),
                        (PendingField, {"field": "seo.title", "reason_code": "maybe"})]:
        with pytest.raises(ValidationError):
            model.model_validate(data)


@pytest.mark.parametrize("data, model", [
    ({"kind": "internal", "page_id": "sistemas_energeticos", "section_id": "ene-03"}, InternalLink),
    ({"kind": "external", "url": "https://example.org/reference"}, ExternalLink),
    ({"kind": "contact", "channel": "email"}, ContactLink),
    ({"kind": "resource", "catalog_id": "catalog-example"}, ResourceLink),
])
def test_discriminated_destinations(data, model):
    value = TypeAdapter(LinkRef).validate_python(data)
    assert isinstance(value, model)
    assert TypeAdapter(LinkRef).validate_json(value.model_dump_json()) == value


@pytest.mark.parametrize("data", [
    {"kind": "unknown"}, {"page_id": "inicio"},
    {"kind": "internal", "page_id": "inicio", "url": "/"},
    {"kind": "internal", "page_id": "/inicio/"},
    {"kind": "contact", "channel": "whatsapp"},
    {"kind": "contact", "channel": "email", "email": "private@example.org"},
    {"kind": "resource", "catalog_id": "example", "file_path": "example.pdf"},
])
def test_invalid_destinations(data):
    with pytest.raises(ValidationError):
        TypeAdapter(LinkRef).validate_python(data)


@pytest.mark.parametrize("url", ["javascript:alert(1)", "file:///secret", "mailto:info@example.org", "/local", "https://"])
def test_external_urls_are_http_only(url):
    with pytest.raises(ValidationError):
        ExternalLink(url=url)


def test_action_shapes_cannot_be_combined():
    local = {"id": "contact", "label": "Contacto", "target": {"kind": "internal", "page_id": "contacto"}}
    assert isinstance(TypeAdapter(Action).validate_python(local), CallToAction)
    assert isinstance(TypeAdapter(Action).validate_python({"id": "contact", "common_ref": "contact"}), SharedActionRef)
    with pytest.raises(ValidationError):
        TypeAdapter(Action).validate_python({**local, "common_ref": "contact"})


def test_nine_section_families_round_trip(editorial_bundle):
    sections = [section for page in editorial_bundle.pages for section in page.sections]
    assert {s.kind for s in sections} == {"hero", "text", "cards", "item_list", "process", "sector_index", "experience_index", "team", "form"}
    for section in sections:
        assert TypeAdapter(Section).validate_json(section.model_dump_json()) == section


@pytest.mark.parametrize("kind", ["hero", "text", "cards", "item_list", "process", "sector_index", "experience_index", "team", "form"])
def test_unknown_section_fields(kind, editorial_bundle):
    section = next(s for p in editorial_bundle.pages for s in p.sections if s.kind == kind)
    data = section.model_dump()
    data["layout"] = "three-columns"
    with pytest.raises(ValidationError, match="extra_forbidden"):
        TypeAdapter(Section).validate_python(data)


def test_empty_and_unknown_sections_are_rejected():
    for data in [{"id": "empty", "kind": "text"}, {"id": "unknown", "kind": "html"},
                 {"id": "hero", "kind": "hero"}, {"id": "cards", "kind": "cards"}]:
        with pytest.raises(ValidationError):
            TypeAdapter(Section).validate_python(data)
    assert TextSection(id="t", title="Un título significativo").title


@pytest.mark.parametrize("block", ["H02", "INF-03", "ENE-03", "DIG-W03", "C03", "H05", "DIG-W05"])
def test_card_purpose_matches_item_type(block, editorial_bundle):
    section = next(s for p in editorial_bundle.pages for s in p.sections if s.source_block == block)
    data = section.model_dump()
    data["purpose"] = "capabilities" if section.purpose != "capabilities" else "technical_areas"
    with pytest.raises(ValidationError, match="requires"):
        TypeAdapter(Section).validate_python(data)


def test_transversal_cannot_be_attached_to_capabilities(editorial_bundle):
    home = editorial_bundle.get_page("inicio")
    data = home.sections[1].model_dump()
    data["transversal"] = {"id": "scope", "paragraphs": [{"id": "scope", "text": "Dato sintético."}]}
    with pytest.raises(ValidationError, match="transversal"):
        TypeAdapter(Section).validate_python(data)


def test_list_purposes_and_minimum_cardinalities(editorial_bundle):
    need = editorial_bundle.get_page("inicio").sections[2].model_dump()
    need["purpose"] = "deliverables"
    with pytest.raises(ValidationError, match="requires delivery"):
        TypeAdapter(Section).validate_python(need)
    for page in editorial_bundle.pages:
        for section in page.sections:
            data = section.model_dump()
            for field in ("items", "fields", "groups", "sector_refs", "person_refs", "corporate_presentation"):
                if field in data:
                    invalid = deepcopy(data)
                    invalid[field] = []
                    with pytest.raises(ValidationError):
                        TypeAdapter(Section).validate_python(invalid)


def test_local_collection_ids_are_unique(editorial_bundle):
    for page in editorial_bundle.pages:
        for section in page.sections:
            data = section.model_dump()
            for field in ("paragraphs", "items", "actions", "fields", "groups", "sector_refs", "person_refs"):
                if data.get(field):
                    invalid = deepcopy(data)
                    invalid[field].append(deepcopy(invalid[field][0]))
                    with pytest.raises(ValidationError, match="duplicate"):
                        TypeAdapter(Section).validate_python(invalid)


def test_page_has_exactly_one_hero_and_unique_sections(bundle_data):
    original = bundle_data["pages"][0]
    for sections in [[], original["sections"][1:], [original["sections"][0]] * 2,
                     original["sections"] + [original["sections"][1]]]:
        with pytest.raises(ValidationError):
            PageContent.model_validate({**original, "sections": sections})
    # D03's current cardinalities are acceptance requirements, not universal rules.
    assert len(PageContent.model_validate({**original, "sections": original["sections"][:1]}).sections) == 1


def test_seo_pending_order_and_serialization(editorial_bundle):
    page = editorial_bundle.get_page("inicio")
    assert page.seo.title is None
    assert {p.field for p in page.pending} >= {"seo.title", "seo.description"}
    rebuilt = EditorialBundle.model_validate_json(editorial_bundle.model_dump_json())
    assert rebuilt == editorial_bundle
    assert [s.id for s in rebuilt.pages[0].sections] == [s.id for s in page.sections]
    data = page.model_dump()
    data["slug"] = "inicio"
    with pytest.raises(ValidationError, match="extra_forbidden"):
        PageContent.model_validate(data)


def test_incomplete_person_and_unverified_experience_are_valid_drafts():
    person = Person(id="example", public_name="Nombre sintético", review={"status": "draft"})
    assert person.qualification is None and not person.verification.authorized
    for kind in ("founder_previous", "bafras_project"):
        experience = Experience(id="example", kind=kind, title="Referencia sintética", review={"status": "approved"})
        assert not experience.verification.verified and not experience.verification.authorized
    with pytest.raises(ValidationError):
        Verification(verified=True)
    assert Verification(authorized=True, evidence_refs=["Autorización sintética de prueba"]).authorized
    with pytest.raises(ValidationError):
        DocumentedResult(id="result", text="Resultado sintético", evidence_refs=[])


def test_resources_have_no_physical_metadata():
    data = {"catalog_id": "example", "sector_id": "turismo-terciario", "title": "Catálogo sintético no publicable"}
    assert DownloadableResource.model_validate(data).catalog_id == "example"
    for field in ("file_path", "language", "version", "rights", "available"):
        with pytest.raises(ValidationError):
            DownloadableResource.model_validate({**data, field: "unexpected"})


def test_shared_content_and_bundle_lookup(editorial_bundle):
    assert editorial_bundle.get_common().actions[0].id == "project-contact"
    assert editorial_bundle.get_person("murti").public_name == "Murti"
    assert editorial_bundle.get_sector("turismo-terciario").catalog_refs == []
    assert editorial_bundle.get_experience("formentor").kind == "founder_previous"
    for getter in (editorial_bundle.get_page, editorial_bundle.get_person, editorial_bundle.get_sector,
                   editorial_bundle.get_experience, editorial_bundle.get_resource):
        with pytest.raises(KeyError):
            getter("missing")
    with pytest.raises(ValidationError):
        CommonContent(actions=[{"id": "shared", "common_ref": "recursive"}])


def test_bundle_local_consistency_and_missing_refs_are_not_resolved(bundle_data):
    for field in ("pages", "people", "sectors", "experiences"):
        data = deepcopy(bundle_data)
        data[field].append(deepcopy(data[field][0]))
        with pytest.raises(ValidationError, match="duplicate"):
            EditorialBundle.model_validate(data)
    data = deepcopy(bundle_data)
    data["pages"][0]["locale"] = "en"
    with pytest.raises(ValidationError, match="locale"):
        EditorialBundle.model_validate(data)
    # Cross-file resolution deliberately belongs to A2, not A1.
    assert InternalLink(page_id="not_registered").page_id == "not_registered"


def test_media_identity_is_explicitly_blocked(editorial_bundle):
    hero = editorial_bundle.pages[0].sections[0].model_dump()
    hero["media"] = {"id": "R24"}
    with pytest.raises(ValidationError):
        TypeAdapter(Section).validate_python(hero)


def test_application_examples_do_not_link_to_contact_channels(editorial_bundle):
    section = editorial_bundle.get_page("capacidades").sections[2].model_dump()
    section["items"][0]["disciplines"][0]["target"] = {"kind": "contact", "channel": "email"}
    with pytest.raises(ValidationError, match="internal references"):
        TypeAdapter(Section).validate_python(section)


@pytest.mark.parametrize("block,field", [("H02", "examples"), ("H02", "paragraphs"),
                                          ("ENE-03", "included"), ("DIG-W03", "tags")])
def test_nested_card_ids_are_unique(block, field, editorial_bundle):
    section = next(s for p in editorial_bundle.pages for s in p.sections if s.source_block == block).model_dump()
    values = section["items"][0][field]
    values.append(deepcopy(values[0]))
    with pytest.raises(ValidationError, match="duplicate"):
        TypeAdapter(Section).validate_python(section)


@pytest.mark.parametrize("field", ["slug", "canonical", "hreflang", "robots", "url"])
def test_page_does_not_duplicate_web_metadata(field, editorial_bundle):
    data = editorial_bundle.pages[0].model_dump()
    with pytest.raises(ValidationError, match="extra_forbidden"):
        PageContent.model_validate({**data, field: "unexpected"})


def test_duplicate_catalogs_and_invalid_sectors(editorial_bundle):
    from bafras_web.editorial import Sector

    data = editorial_bundle.sectors[0].model_dump()
    data["catalog_refs"] = [{"kind": "resource", "catalog_id": "example"}] * 2
    with pytest.raises(ValidationError, match="duplicate"):
        Sector.model_validate(data)
    data["catalog_refs"] = []
    data["id"] = "alternative-taxonomy"
    with pytest.raises(ValidationError):
        Sector.model_validate(data)


def test_resource_lookup_and_uniqueness(editorial_bundle):
    resource = {"catalog_id": "synthetic-example", "sector_id": "turismo-terciario", "title": "Ejemplo sintético no publicable"}
    data = editorial_bundle.model_dump()
    data["resources"] = [resource]
    assert EditorialBundle.model_validate(data).get_resource("synthetic-example").title == resource["title"]
    data["resources"].append(deepcopy(resource))
    with pytest.raises(ValidationError, match="duplicate"):
        EditorialBundle.model_validate(data)
