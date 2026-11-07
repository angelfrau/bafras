"""CONTENT-I18N-02: the four locales load, keep the ES structure and stay isolated.

Spanish is the structural baseline. The translatable keys come from
LOCALIZATION_CONTRACT.md («Campos traducibles»); every other scalar is protected.
No translated text is snapshotted here: only structure, identity and provenance.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from copy import deepcopy
from collections import Counter
from pathlib import Path

import pytest
import yaml

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.yaml_files import load_yaml
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import build_editorial_bundle
from bafras_web.editorial.pages import EditorialBundle, PageContent

ROOT = Path(__file__).resolve().parents[2]
SOURCE_LOCALE = "es"
TRANSLATED = ("ca", "en", "de")
POLICIES = ("INCREMENTAL", "COMPLETE")
MANIFEST = ROOT / "docs/project_v02/editorial/quality/ES_BASELINE_MANIFEST.md"
# LOCALIZATION_CONTRACT.md: values of these keys may differ between locales.
TRANSLATABLE = frozenset({
    "text", "title", "description", "eyebrow", "subtitle", "attribution", "label", "submit_label",
    "success", "error", "privacy_text", "help", "placeholder", "qualification", "specialty",
})


# Spanish-only documents awaiting a reviewed translation (WEB-V01-B). They must not exist in
# translated locales until translated: no copy of the Spanish text, no fallback.
PENDING_TRANSLATION = frozenset({"common.yaml"})


def _sources(locale: str) -> list[str]:
    """Documents that every locale must mirror (pages and entities)."""
    base = ROOT / "content" / locale
    return sorted(s for p in base.rglob("*.yaml") if (s := p.relative_to(base).as_posix()) not in PENDING_TRANSLATION)


@pytest.mark.parametrize("locale", TRANSLATED)
def test_pending_translations_exist_only_in_spanish(locale):
    for name in PENDING_TRANSLATION:
        assert (ROOT / "content" / SOURCE_LOCALE / name).is_file()
        assert not (ROOT / "content" / locale / name).exists(), f"{locale}/{name}: traducción no revisada"


def _inspect(paths: ProjectPaths, locale: str, policy: str = "COMPLETE"):
    return inspect_editorial(paths, EditorialLoadRequest(locale=locale, policy=policy))


def _fingerprint(bundle: EditorialBundle) -> str:
    data = json.dumps(bundle.model_dump(mode="json"), sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def _structure_differences(es, tr, path: str, key: str | None = None):
    """Yield every protected or structural difference; translatable strings only need to stay strings."""
    if type(es) is not type(tr):
        yield f"{path}: tipo {type(es).__name__} → {type(tr).__name__}"
    elif isinstance(es, dict):
        if list(es) != list(tr):
            yield f"{path}: claves/orden {list(es)} → {list(tr)}"
        for name in es.keys() & tr.keys():
            yield from _structure_differences(es[name], tr[name], f"{path}.{name}", name)
    elif isinstance(es, list):
        if len(es) != len(tr):
            yield f"{path}: cardinalidad {len(es)} → {len(tr)}"
            return
        for index, (a, b) in enumerate(zip(es, tr)):
            label = a.get("id", index) if isinstance(a, dict) else index
            yield from _structure_differences(a, b, f"{path}[{label}]", key)
    elif not (isinstance(es, str) and key in TRANSLATABLE) and es != tr:
        yield f"{path}: valor protegido {es!r} → {tr!r}"


def _contact_r1_comparison(es, tr):
    """Proyección de test del cambio autorizado; nunca transforma documentos del loader.

    CA/EN/DE mantienen el contrato anterior, pendiente de adaptación CONTACT-R1.
    Se comprueba exactamente esa divergencia antes de comparar el resto de su estructura.
    """
    es, tr = deepcopy(es), deepcopy(tr)
    assert es["review"]["source_ref"] == tr["review"]["source_ref"] + " · CONTACT-R1 / WEB-V03 R2"
    es["review"]["source_ref"] = tr["review"]["source_ref"]
    assert es["pending"] == []
    assert tr["pending"] == [{"field": "sections/co-02/privacy_text", "reason_code": "source_missing",
                              "source_ref": "D03 CO-02 · 03.K §4 · política real pendiente de revisión legal"}]
    tr["pending"] = []
    current, previous = es["sections"][1], tr["sections"][1]
    assert current["kind"] == "text" and previous["kind"] == "form"
    assert list(previous) == ["id", "source_block", "kind", "title", "fields", "submit_label", "messages"]
    assert [(f["id"], f["required"]) for f in previous["fields"]] == [
        ("name", True), ("company", False), ("email", True), ("message", True)]
    assert all(list(f) == ["id", "label", "required"] for f in previous["fields"][:-1])
    assert list(previous["fields"][-1]) == ["id", "label", "required", "help"]
    assert list(previous["messages"]) == ["success", "error"]
    assert all(isinstance(t, str) and t for t in [previous["submit_label"], *previous["messages"].values()])
    tr["sections"][1] = {"id": previous["id"], "source_block": previous["source_block"], "kind": "text",
                         "title": previous["title"], "paragraphs": [{"id": "consultation-guidance", "text": previous["fields"][-1]["help"]}]}
    for channel, expected in zip(tr["sections"][2]["contact_channels"], ("info@bafras.com", "+34 610 903 179")):
        assert channel.pop("value") == expected
    return es, tr


@pytest.fixture(scope="module")
def project() -> ProjectPaths:
    return ProjectPaths(ROOT)


def test_configured_locales_are_the_content_locales(project):
    assert load_site_routing(project).locales.codes == [SOURCE_LOCALE, *TRANSLATED]


@pytest.mark.parametrize("locale", TRANSLATED)
def test_inventory_matches_spanish_baseline(locale):
    assert len(_sources(SOURCE_LOCALE)) == 11
    assert _sources(locale) == _sources(SOURCE_LOCALE), f"{locale}: inventario distinto de es"


@pytest.mark.parametrize("locale", TRANSLATED)
def test_structure_and_protected_values_match_spanish(locale):
    problems = []
    for source in _sources(SOURCE_LOCALE):
        es = load_yaml(ROOT / "content" / SOURCE_LOCALE / source)
        tr = load_yaml(ROOT / "content" / locale / source)
        if source == "pages/contacto.yaml":
            es, tr = _contact_r1_comparison(es, tr)
        problems += [f"{locale}/{source}: {p}" for p in _structure_differences(es, tr, "")]
    assert not problems, "\n".join(problems)


def test_contract_translatable_keys_exist_in_content():
    """Guards the key list against drift: each declared key is really used by ES data."""
    used: set[str] = set()

    def walk(value, key=None):
        if isinstance(value, dict):
            for name, child in value.items():
                walk(child, name)
        elif isinstance(value, list):
            for child in value:
                walk(child, key)
        elif isinstance(value, str):
            used.add(key)

    for source in _sources(SOURCE_LOCALE):
        walk(load_yaml(ROOT / "content" / SOURCE_LOCALE / source))
    # CONTACT-R1 retira los estados y controles de envío de ES; sus modelos/traducciones siguen cubiertos.
    unused = TRANSLATABLE - used - {"attribution", "placeholder", "privacy_text", "submit_label", "success", "error", "help"}
    assert not unused, unused


@pytest.mark.parametrize("policy", POLICIES)
@pytest.mark.parametrize("locale", TRANSLATED)
def test_translated_inspection_has_spanish_integrity_profile(project, locale, policy):
    """Selectors are locale-independent, so diagnostics must coincide one by one with ES."""
    def profile(result):
        return Counter((d.code, d.severity, d.document_id, d.selector, d.reason_code) for d in result.diagnostics)

    es, tr = _inspect(project, SOURCE_LOCALE, policy), _inspect(project, locale, policy)
    assert tr.locale == locale and not tr.has_errors, [d for d in tr.diagnostics if d.severity == "error"]
    assert tr.documents_complete and tr.can_build_bundle
    assert all(d.source.startswith(f"{locale}/") for d in tr.documents), f"{locale}: documento de otro idioma"
    translated_profile = profile(tr)
    privacy = ("EDITORIAL_PENDING", "info", "page/contacto", "sections/co-02/privacy_text", "source_missing")
    assert translated_profile[privacy] == 1 and profile(es)[privacy] == 0
    translated_profile.subtract({privacy: 1})
    assert +translated_profile == profile(es), f"{locale}/{policy}: diagnósticos distintos fuera de CONTACT-R1"


@pytest.mark.parametrize("locale", TRANSLATED)
def test_bundle_serves_the_requested_locale_files(project, locale):
    bundle = build_editorial_bundle(_inspect(project, locale))
    spanish = build_editorial_bundle(_inspect(project, SOURCE_LOCALE))
    assert bundle.locale == locale and len(bundle.pages) == 9 and sum(len(p.sections) for p in bundle.pages) == 51
    assert len(bundle.sectors) == 6 and len(bundle.people) == 3 and bundle.experiences == bundle.resources == []
    assert all(page.review.status == "draft" for page in bundle.pages)
    for page in bundle.pages:
        source = load_yaml(ROOT / "content" / locale / "pages" / f"{page.page_id}.yaml")
        assert page == PageContent.model_validate({**source, "locale": locale}), f"{locale}/{page.page_id}"
        es_page = spanish.get_page(page.page_id)
        expected_sections = [(s.id, "form" if page.page_id == "contacto" and s.id == "co-02" else s.kind) for s in es_page.sections]
        assert [(s.id, s.kind) for s in page.sections] == expected_sections
        if page.page_id == "contacto":
            assert len(page.pending) == 1 and page.pending[0].field == "sections/co-02/privacy_text"
            assert es_page.pending == []
        else:
            assert page.pending == es_page.pending
        assert page.sections[0].title != es_page.sections[0].title, f"{locale}/{page.page_id}: hero sin traducir"
    assert [s.id for s in bundle.sectors] == [s.id for s in spanish.sectors]
    assert [p.public_name for p in bundle.people] == [p.public_name for p in spanish.people]


def test_interleaved_loads_are_isolated_and_deterministic(project):
    sequence = ["es", "ca", "en", "de", "es", "de", "ca", "en", "es"]
    bundles = [build_editorial_bundle(_inspect(project, locale)) for locale in sequence]
    by_locale: dict[str, set[str]] = {}
    for locale, bundle in zip(sequence, bundles):
        assert bundle.locale == locale
        by_locale.setdefault(locale, set()).add(_fingerprint(bundle))
    assert all(len(prints) == 1 for prints in by_locale.values()), by_locale
    assert len({next(iter(prints)) for prints in by_locale.values()}) == 4
    first_es, second_es = bundles[0], bundles[4]
    assert first_es == second_es and first_es.pages[0] is not second_es.pages[0]


def test_spanish_bundle_matches_baseline_manifest(project):
    text = MANIFEST.read_text(encoding="utf-8")
    recorded = re.search(r"Huella del bundle completo[^`]*`([0-9a-f]{64})`", text, re.S).group(1)
    for policy in POLICIES:
        assert _fingerprint(build_editorial_bundle(_inspect(project, SOURCE_LOCALE, policy))) == recorded


@pytest.fixture
def copied_project(tmp_path) -> ProjectPaths:
    shutil.copytree(ROOT / "config", tmp_path / "config")
    for locale in (SOURCE_LOCALE, *TRANSLATED):
        shutil.copytree(ROOT / "content" / locale, tmp_path / "content" / locale)
    return ProjectPaths(tmp_path)


@pytest.mark.parametrize("locale", TRANSLATED)
def test_missing_translated_page_never_falls_back_to_spanish(copied_project, locale):
    (copied_project.content / locale / "pages" / "contacto.yaml").unlink()
    for policy, severity in (("INCREMENTAL", "warning"), ("COMPLETE", "error")):
        result = _inspect(copied_project, locale, policy)
        assert result.missing_page_ids == ("contacto",) and "contacto" not in result.valid_pages
        assert ("DOCUMENT_MISSING", severity) in {(d.code, d.severity) for d in result.diagnostics}
        assert not result.can_build_bundle
        with pytest.raises(ValueError):
            build_editorial_bundle(result)
    assert "contacto" in _inspect(copied_project, SOURCE_LOCALE).valid_pages


@pytest.mark.parametrize("locale", TRANSLATED)
def test_invalid_translated_document_is_explicit(copied_project, locale):
    path = copied_project.content / locale / "pages" / "inicio.yaml"
    data = load_yaml(path)
    data["sections"][0]["unexpected"] = "x"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    result = _inspect(copied_project, locale)
    assert result.invalid_page_ids == ("inicio",) and not result.can_build_bundle
    assert any(d.code == "DOCUMENT_INVALID" and d.source == f"{locale}/pages/inicio.yaml" for d in result.diagnostics)


@pytest.mark.parametrize("locale", TRANSLATED)
def test_broken_translated_reference_is_an_error(copied_project, locale):
    path = copied_project.content / locale / "pages" / "sectores.yaml"
    data = load_yaml(path)
    index = next(s for s in data["sections"] if s["kind"] == "sector_index")
    index["sector_refs"][0] = "sector-inexistente"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    result = _inspect(copied_project, locale)
    assert any(d.code == "REFERENCE_UNKNOWN" and d.source == f"{locale}/pages/sectores.yaml" for d in result.diagnostics)
    assert not result.can_build_bundle


def test_unsupported_locale_is_rejected_even_with_content_on_disk(copied_project):
    shutil.copytree(copied_project.content / "ca", copied_project.content / "fr")
    result = _inspect(copied_project, "fr")
    assert [d.code for d in result.diagnostics] == ["LOCALE_UNKNOWN"]
    assert result.documents == () and not result.can_build_bundle
