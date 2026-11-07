"""B1.1 persistence/integrity fixtures live only in pytest temporary projects."""

from collections import Counter
from copy import deepcopy
from pathlib import Path
import shutil

import pytest
import yaml

from bafras_web.adapters import editorial_files, yaml_files
from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application import editorial as application
from bafras_web.application.configuration import ConfigurationError, load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import assess_integrity, build_editorial_bundle

ROOT = Path(__file__).resolve().parents[2]
SYNTHETIC = "Contrato sintético B1.1; no publicable."


def write(paths, name, data):
    file = paths.content / "es" / name
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return file


def page(id, **values):
    return {"page_id": id, "review": {"status": "draft"}, "seo": {},
            "sections": [{"id": "hero", "kind": "hero", "title": SYNTHETIC}], **values}


def inspect(paths, policy="INCREMENTAL", locale="es"):
    return inspect_editorial(paths, EditorialLoadRequest(locale=locale, policy=policy))


@pytest.fixture
def project(tmp_path):
    (tmp_path / "config").mkdir()
    for name in ("locales.yaml", "routes.yaml"):
        shutil.copyfile(ROOT / "config" / name, tmp_path / "config" / name)
    return ProjectPaths(tmp_path)


def fill_pages(paths):
    for id in load_site_routing(paths).routes.pages:
        write(paths, f"pages/{id}.yaml", page(id))


@pytest.mark.parametrize("policy", ["INCREMENTAL", "COMPLETE"])
def test_real_inicio_acceptance(policy, project):
    # Preserve B1.1's Inicio-only acceptance scenario as other pages migrate.
    # A3 tests the evolving real checkout separately, including Capacidades.
    target = project.content / "es/pages/inicio.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "content/es/pages/inicio.yaml", target)
    result = inspect(project, policy)
    assert len(result.expected_page_ids) == 9
    assert list(result.valid_pages) == ["inicio"]
    assert len(result.missing_page_ids) == 8 and not result.invalid_page_ids
    assert Counter(d.code for d in result.diagnostics) == {
        "DOCUMENT_MISSING": 8, "REFERENCE_TARGET_UNAVAILABLE": 14, "EDITORIAL_PENDING": 8}
    assert {d.severity for d in result.diagnostics if d.code == "DOCUMENT_MISSING"} == {"error" if policy == "COMPLETE" else "warning"}
    assert {d.reference_status for d in result.diagnostics if d.code == "REFERENCE_TARGET_UNAVAILABLE"} == {"UNVERIFIABLE"}
    assert not result.can_build_bundle and not result.documents_complete
    assert result.has_errors == (policy == "COMPLETE")
    with pytest.raises(ValueError):
        build_editorial_bundle(result)


@pytest.mark.parametrize("policy", ["INCREMENTAL", "COMPLETE"])
def test_complete_draft_and_approved_pending_are_not_publication(project, policy):
    fill_pages(project)
    write(project, "pages/inicio.yaml", page("inicio", review={"status": "approved"}, pending=[
        {"field": "seo.title", "reason_code": "approval_required"},
        {"field": "sections/hero/media", "reason_code": "integration_pending"}]))
    result = inspect(project, policy)
    assert result.documents_complete and result.can_build_bundle
    assert not result.has_errors
    bundle = build_editorial_bundle(result)
    assert len(bundle.pages) == 9 and bundle.people == [] and bundle.resources == []
    assert bundle.get_page("inicio").review.status == "approved"
    assert len(bundle.get_page("inicio").pending) == 2
    assert bundle.get_page("inicio").seo.title is None


@pytest.mark.parametrize("text,code", [
    ("a: [1\n", "YAML_ERROR"), ("page_id: inicio\npage_id: contacto\n", "YAML_ERROR"),
    ("", "DOCUMENT_ROOT_INVALID"), ("42", "DOCUMENT_ROOT_INVALID"), ("- one\n", "DOCUMENT_ROOT_INVALID"),
    ("? [a,b]\n: value\n", "YAML_ERROR"),
])
def test_invalid_yaml_roots_are_not_absent(project, text, code):
    file = write(project, "pages/inicio.yaml", page("inicio"))
    file.write_text(text, encoding="utf-8")
    write(project, "pages/contacto.yaml", page("contacto"))
    result = inspect(project)
    assert result.invalid_page_ids == ("inicio",)
    assert "contacto" in result.valid_pages
    assert any(d.code == code and d.document_id == "page/inicio" for d in result.diagnostics)
    assert result.has_errors


@pytest.mark.parametrize("updates,code", [
    ({"page_id": "contacto"}, "DOCUMENT_ID_MISMATCH"),
    ({"locale": "en"}, "DOCUMENT_LOCALE_MISMATCH"),
    ({"extra": True}, "DOCUMENT_INVALID"),
    ({"sections": [{"id": "hero", "kind": "hero", "title": True}]}, "DOCUMENT_INVALID"),
])
def test_present_invalid_documents_fail_both_policies(project, updates, code):
    write(project, "pages/inicio.yaml", {**page("inicio"), **updates})
    for policy in ("INCREMENTAL", "COMPLETE"):
        result = inspect(project, policy)
        assert result.invalid_page_ids == ("inicio",)
        assert any(d.code == code for d in result.diagnostics)
        assert not result.can_build_bundle


def test_matching_declared_locale_is_accepted(project):
    write(project, "pages/inicio.yaml", page("inicio", locale="es"))
    assert "inicio" in inspect(project).valid_pages


@pytest.mark.parametrize("locale", ["zz", "../../secret"])
def test_unknown_locale_never_discovers_or_loads_content(project, monkeypatch, locale):
    def forbidden(*args):
        pytest.fail("unknown locale must not discover content")
    monkeypatch.setattr(application, "discover_editorial_sources", forbidden)
    result = inspect(project, locale=locale)
    assert result.documents == () and result.expected_page_ids == ()
    assert result.diagnostics[0].code == "LOCALE_UNKNOWN"
    assert not result.documents_complete and not result.can_build_bundle


def test_unpublished_locale_has_no_fallback(project):
    fill_pages(project)
    result = inspect(project, locale="en")
    assert len(result.missing_page_ids) == 9 and not result.valid_pages
    assert all(d.source.startswith("en/") for d in result.documents)


@pytest.mark.parametrize("name", ["pages/extra.yaml", "pages/inicio.yml", "unknown.yaml", "entities/unknown.yaml"])
def test_unexpected_documents_are_errors(project, name):
    fill_pages(project)
    write(project, name, {})
    result = inspect(project)
    assert any(d.code == "DOCUMENT_UNEXPECTED" for d in result.diagnostics)
    assert result.documents_complete and not result.can_build_bundle


def test_auxiliary_files_are_not_content(project):
    fill_pages(project)
    (project.content / "es/pages/README.md").write_text("Auxiliar", encoding="utf-8")
    assert inspect(project).can_build_bundle


def test_invalid_utf8_and_multiple_errors_accumulate(project):
    write(project, "pages/inicio.yaml", {}).write_bytes(b'\xff')
    write(project, "pages/contacto.yaml", {}).write_text("x: [", encoding="utf-8")
    write(project, "pages/sectores.yaml", page("sectores"))
    result = inspect(project)
    assert set(result.invalid_page_ids) == {"inicio", "contacto"}
    assert "sectores" in result.valid_pages
    assert len([d for d in result.diagnostics if d.code == "YAML_ERROR"]) == 2


def test_read_error_is_contained(project, monkeypatch):
    write(project, "pages/inicio.yaml", page("inicio"))
    original = yaml_files.load_yaml
    def fail_one(path):
        if path.name == "inicio.yaml":
            raise yaml_files.YamlFileError(path, "test read failure")
        return original(path)
    monkeypatch.setattr(yaml_files, "load_yaml", fail_one)
    result = inspect(project)
    assert result.invalid_page_ids == ("inicio",)
    assert result.has_errors


def test_discovery_read_race_is_invalid_not_absent(project, monkeypatch):
    file = write(project, "pages/inicio.yaml", page("inicio"))
    original = application.discover_editorial_sources
    def disappear(*args):
        result = original(*args)
        file.unlink()
        return result
    monkeypatch.setattr(application, "discover_editorial_sources", disappear)
    result = inspect(project)
    assert result.invalid_page_ids == ("inicio",)
    assert any(d.code == "DOCUMENT_READ_ERROR" for d in result.diagnostics)


def test_directory_where_document_expected(project):
    (project.content / "es/pages/inicio.yaml").mkdir(parents=True)
    result = inspect(project)
    assert result.invalid_page_ids == ("inicio",)
    assert any(d.code == "DOCUMENT_READ_ERROR" for d in result.diagnostics)


def test_symlink_escape_is_rejected_without_reading(project, tmp_path, monkeypatch):
    outside = tmp_path / "outside.yaml"
    outside.write_text("private: true", encoding="utf-8")
    link = project.content / "es/pages/inicio.yaml"
    link.parent.mkdir(parents=True)
    try:
        link.symlink_to(outside)
    except OSError:
        # Some Windows tokens cannot create symlinks. Exercise the containment
        # boundary with resolve rather than skipping the assertion.
        link.write_text("placeholder", encoding="utf-8")
        original = Path.resolve
        def resolve(path, *args, **kwargs):
            return outside if path == link else original(path, *args, **kwargs)
        monkeypatch.setattr(Path, "resolve", resolve)
    result = inspect(project)
    assert result.invalid_page_ids == ("inicio",)
    assert any(d.code == "DOCUMENT_READ_ERROR" for d in result.diagnostics)


def test_configuration_error_propagates(project):
    project.locales_file.write_text("invalid: true", encoding="utf-8")
    with pytest.raises(ConfigurationError):
        inspect(project)


def test_reciprocal_page_and_section_references(project):
    fill_pages(project)
    for id, target in (("inicio", "contacto"), ("contacto", "inicio")):
        data = page(id)
        data["sections"][0]["actions"] = [{"id": "next", "label": SYNTHETIC,
            "target": {"kind": "internal", "page_id": target, "section_id": "hero"}}]
        write(project, f"pages/{id}.yaml", data)
    result = inspect(project)
    assert result.can_build_bundle
    report = assess_integrity(result.documents, result.expected_page_ids, report_resolved=True)
    assert len([d for d in report.diagnostics if d.reference_status == "RESOLVED"]) == 2
    data["sections"][0]["actions"][0]["target"]["section_id"] = "missing"
    write(project, "pages/contacto.yaml", data)
    result = inspect(project)
    assert any(d.code == "REFERENCE_SECTION_UNKNOWN" for d in result.diagnostics)
    assert not result.can_build_bundle


def test_unknown_page_differs_from_missing_or_invalid_target(project):
    data = page("inicio")
    data["sections"][0]["actions"] = [{"id": "next", "label": SYNTHETIC,
        "target": {"kind": "internal", "page_id": "unknown", "section_id": "missing"}}]
    write(project, "pages/inicio.yaml", data)
    assert any(d.code == "REFERENCE_UNKNOWN" for d in inspect(project).diagnostics)
    data["sections"][0]["actions"][0]["target"]["page_id"] = "contacto"
    write(project, "pages/inicio.yaml", data)
    for invalid in (False, True):
        if invalid:
            write(project, "pages/contacto.yaml", {})
        result = inspect(project)
        assert any(d.code == "REFERENCE_TARGET_UNAVAILABLE" for d in result.diagnostics)
        assert not any(d.code == "REFERENCE_SECTION_UNKNOWN" for d in result.diagnostics)


def test_conditional_people_experiences_and_reciprocal_entities(project):
    fill_pages(project)
    data = page("inicio")
    data["sections"].append({"id": "team", "kind": "team", "title": SYNTHETIC,
        "corporate_presentation": [{"id": "presentation", "text": SYNTHETIC}], "person_refs": ["person"]})
    write(project, "pages/inicio.yaml", data)
    result = inspect(project)
    assert next(d for d in result.documents if d.kind == "people").required
    assert any(d.target_document_id == "catalog/people" and d.reference_status == "UNVERIFIABLE" for d in result.diagnostics)
    person = {"id": "person", "public_name": SYNTHETIC, "review": {"status": "draft"}, "experience_refs": ["experience"],
              "pending": [{"field": "profile", "reason_code": "verification_required"}]}
    write(project, "entities/people.yaml", [person])
    result = inspect(project)
    assert next(d for d in result.documents if d.kind == "experiences").required
    write(project, "entities/experiences.yaml", [{"id": "experience", "kind": "founder_previous", "title": SYNTHETIC,
        "review": {"status": "draft"}, "person_refs": ["person"],
        "results": [{"id": "result", "text": SYNTHETIC, "evidence_refs": ["Referencia sintética"]}]}])
    result = inspect(project)
    assert result.can_build_bundle
    assert any(d.code == "ENTITY_PENDING_UNCHECKED" for d in result.diagnostics)
    assert any(d.code == "EXTERNAL_EVIDENCE_UNCHECKED" for d in result.diagnostics)
    assert not build_editorial_bundle(result).people[0].verification.authorized
    person["id"] = "different"
    write(project, "entities/people.yaml", [person])
    assert any(d.code == "REFERENCE_UNKNOWN" for d in inspect(project).diagnostics)


def test_shared_action_missing_and_valid(project):
    fill_pages(project)
    data = page("inicio")
    data["sections"][0]["actions"] = [{"id": "shared", "common_ref": "contact"}]
    write(project, "pages/inicio.yaml", data)
    assert any(d.target_document_id == "common" and d.reference_status == "UNVERIFIABLE" for d in inspect(project).diagnostics)
    write(project, "common.yaml", {})
    assert any(d.target_document_id == "common" and d.reference_status == "UNRESOLVED" for d in inspect(project).diagnostics)
    write(project, "common.yaml", {"actions": [{"id": "contact", "label": SYNTHETIC,
        "target": {"kind": "internal", "page_id": "contacto"}}]})
    assert inspect(project).can_build_bundle


def test_resources_sector_membership_and_external_limits(project):
    fill_pages(project)
    data = page("sectores")
    data["sections"].append({"id": "sectors", "kind": "sector_index", "title": SYNTHETIC, "sector_refs": ["turismo-terciario"]})
    write(project, "pages/sectores.yaml", data)
    sector = {"id": "turismo-terciario", "title": SYNTHETIC, "description": [{"id": "description", "text": SYNTHETIC}],
              "contextual_actions": [{"id": "contact", "label": SYNTHETIC, "target": {"kind": "contact", "channel": "email"}}],
              "catalog_refs": [{"kind": "resource", "catalog_id": "catalog"}]}
    write(project, "entities/sectors.yaml", [sector])
    write(project, "entities/resources.yaml", [{"catalog_id": "catalog", "sector_id": "turismo-terciario", "title": SYNTHETIC}])
    result = inspect(project)
    assert result.can_build_bundle
    assert any(d.code == "EXTERNAL_CONTACT_UNCHECKED" for d in result.diagnostics)
    assert any(d.code == "EXTERNAL_RESOURCE_UNCHECKED" for d in result.diagnostics)
    other = {**deepcopy(sector), "id": "salud-educacion-equipamientos", "catalog_refs": []}
    write(project, "entities/sectors.yaml", [sector, other])
    write(project, "entities/resources.yaml", [{"catalog_id": "catalog", "sector_id": other["id"], "title": SYNTHETIC}])
    result = inspect(project)
    assert any(d.code == "RESOURCE_SECTOR_MISMATCH" for d in result.diagnostics)
    assert not result.can_build_bundle


@pytest.mark.parametrize("value", [{"wrong": True}, [1], "scalar"])
def test_optional_present_catalog_is_validated(project, value):
    fill_pages(project)
    write(project, "entities/people.yaml", value)
    result = inspect(project)
    assert next(d for d in result.documents if d.kind == "people").state == "INVALID"
    assert not result.can_build_bundle


def test_duplicate_catalog_ids_are_invalid(project):
    fill_pages(project)
    person = {"id": "same", "public_name": SYNTHETIC, "review": {"status": "draft"}}
    write(project, "entities/people.yaml", [person, person])
    result = inspect(project)
    assert any(d.code == "DUPLICATE_ENTITY_ID" for d in result.diagnostics)
    assert not result.can_build_bundle


def test_determinism_discovery_order_and_relative_diagnostics(project, tmp_path, monkeypatch):
    write(project, "pages/inicio.yaml", page("inicio", extra=True))
    first = inspect(project)
    assert first == inspect(project)
    original = application.discover_editorial_sources
    monkeypatch.setattr(application, "discover_editorial_sources", lambda *args: tuple(reversed(original(*args))))
    assert first == inspect(project)
    other = tmp_path / "other"
    shutil.copytree(project.config, other / "config")
    shutil.copytree(project.content, other / "content")
    second = inspect(ProjectPaths(other))
    assert first.model_dump(mode="json") == second.model_dump(mode="json")
    assert str(project.root) not in first.model_dump_json()


def test_all_reads_reuse_shared_yaml_loader(project, monkeypatch):
    write(project, "pages/inicio.yaml", page("inicio"))
    calls = []
    original = yaml_files.load_yaml
    def spy(path):
        calls.append(path)
        return original(path)
    monkeypatch.setattr(yaml_files, "load_yaml", spy)
    assert "inicio" in inspect(project).valid_pages
    assert calls == [project.content / "es/pages/inicio.yaml"]


def test_directory_access_errors_do_not_become_a_complete_empty_set(project, monkeypatch):
    original = Path.iterdir
    def deny(path):
        if path == project.content / "es/pages":
            raise PermissionError("private absolute path must not enter diagnostics")
        return original(path)
    monkeypatch.setattr(Path, "iterdir", deny)
    result = inspect(project)
    assert result.has_errors and not result.documents_complete
    assert any(d.code == "DOCUMENT_READ_ERROR" for d in result.diagnostics)


def test_two_pages_and_missing_identities_do_not_discard_valid_content(project):
    write(project, "pages/inicio.yaml", page("inicio"))
    write(project, "pages/contacto.yaml", page("contacto"))
    result = inspect(project)
    assert set(result.valid_pages) == {"inicio", "contacto"}
    assert len(result.missing_page_ids) == 7


def test_external_links_contact_channels_and_resource_actions(project):
    fill_pages(project)
    data = page("inicio")
    data["sections"][0]["actions"] = [{"id": "external", "label": SYNTHETIC,
        "target": {"kind": "external", "url": "https://example.org/"}}]
    data["sections"].append({"id": "contact", "kind": "text", "contact_channels": [
        {"id": "phone", "label": SYNTHETIC, "target": {"kind": "contact", "channel": "phone"}}]})
    write(project, "pages/inicio.yaml", data)
    result = inspect(project)
    assert result.can_build_bundle
    assert {d.code for d in result.diagnostics} >= {"EXTERNAL_URL_UNCHECKED", "EXTERNAL_CONTACT_UNCHECKED"}
    data["sections"][0]["actions"][0]["target"] = {"kind": "resource", "catalog_id": "missing"}
    write(project, "pages/inicio.yaml", data)
    result = inspect(project)
    assert next(d for d in result.documents if d.kind == "resources").required
    assert any(d.target_id == "missing" and d.reference_status == "UNVERIFIABLE" for d in result.diagnostics)


def test_noncanonical_sector_is_known_to_be_invalid_even_without_catalog(project):
    data = page("inicio")
    data["sections"].append({"id": "sectors", "kind": "sector_index", "title": SYNTHETIC, "sector_refs": ["made-up"]})
    write(project, "pages/inicio.yaml", data)
    assert any(d.target_id == "made-up" and d.reference_status == "UNRESOLVED" for d in inspect(project).diagnostics)


@pytest.mark.parametrize("error_type", [RuntimeError, TypeError])
def test_unexpected_loader_programming_errors_are_not_content_errors(project, monkeypatch, error_type):
    write(project, "pages/inicio.yaml", page("inicio"))
    def broken_loader(path):
        raise error_type("programming error")
    monkeypatch.setattr(yaml_files, "load_yaml", broken_loader)
    with pytest.raises(error_type, match="programming error"):
        inspect(project)
