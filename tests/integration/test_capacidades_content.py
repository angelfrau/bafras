"""A3: D03 is the independent text oracle; CAP V1 fixes contextual link order.

Markdown interpretation is test-only. Production uses the existing YAML loader.
No expected value is read from the migrated YAML.
"""

from copy import deepcopy
from pathlib import Path
import re
import shutil

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.yaml_files import load_yaml
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import assess_integrity, build_editorial_bundle
from bafras_web.editorial.pages import PageContent
from bafras_web.editorial.pending import validate_pending_fields

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/project_v02/03_contenido_editorial_V1_22_baseline_G1.md"
CONTENT = ROOT / "content/es/pages/capacidades.yaml"
AREAS = (
    ("infrastructure", "Infraestructuras e instalaciones", "infraestructuras"),
    ("energy", "Sistemas energéticos", "sistemas_energeticos"),
    ("automation", "Automatización y control", "automatizacion_control"),
)


@pytest.fixture(scope="module")
def capacidades():
    raw = load_yaml(CONTENT)
    assert "locale" not in raw
    return PageContent.model_validate({**raw, "locale": "es"})


def compact(value):
    """Keep all populated fields, including unexpected copy and hierarchy."""
    if isinstance(value, dict):
        return {k: compact(v) for k, v in value.items() if v is not None and v != []}
    if isinstance(value, list):
        return [compact(v) for v in value]
    return value


def expected_sections():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    blocks = {}
    for number in range(1, 6):
        start = next(i for i, line in enumerate(lines) if line.startswith(f"## C0{number} ·"))
        end = next(i for i in range(start + 1, len(lines))
                   if lines[i].startswith("## ") or lines[i] == "---")
        blocks[number] = [line for line in lines[start + 1:end] if line]

    def field(number, name):
        prefix = f"**{name}:** "
        return next(line[len(prefix):] for line in blocks[number] if line.startswith(prefix))

    def paragraph(text):
        return [{"id": "description", "text": text}]

    def action(id, label, page, section=None):
        target = {"kind": "internal", "page_id": page}
        if section:
            target["section_id"] = section
        return {"id": id, "label": label, "target": target}

    def base(number, id, kind):
        return {"id": id, "source_block": f"C0{number}", "kind": kind,
                "title": field(number, "H1" if number == 1 else "H2")}

    hero = dict(base(1, "c01", "hero"), eyebrow=field(1, "Antetítulo"),
                paragraphs=paragraph(field(1, "Introducción")),
                actions=[action("explore", field(1, "Enlace de orientación").split(" → ")[0],
                                "capacidades", "especialidades")])
    cards = []
    for id, title, page in AREAS:
        start = blocks[2].index("### " + title)
        area = blocks[2][start + 1:start + 4]
        assert area[1].startswith("**Ámbitos destacados:** ")
        assert area[2].startswith("**Enlace:** ")
        scopes = area[1].removeprefix("**Ámbitos destacados:** ").split(" · ")
        assert len(scopes) == 4
        cards.append({"kind": "capability", "id": id, "title": title,
                      "paragraphs": paragraph(area[0]),
                      "examples": [{"id": f"scope-{i}", "text": text}
                                   for i, text in enumerate(scopes, 1)],
                      "actions": [action("explore", area[2].removeprefix("**Enlace:** ").split(" → ")[0], page)]})
    areas = dict(base(2, "especialidades", "cards"), purpose="capabilities",
                 introduction=paragraph(field(2, "Introducción")), items=cards)
    examples = []
    # D03 requests contextual discipline links; the approved CAP V1 supplies
    # their exact association/order. They are navigation, not project evidence.
    orders = ((0, 1, 2), (1, 0, 2), (0, 2, 1))
    ids = ("thermal-modernization", "self-consumption-storage", "installation-performance")
    for i, (id, order) in enumerate(zip(ids, orders), 1):
        line = next(line for line in blocks[3] if line.startswith(f"**Ejemplo {i} — "))
        title, description = line.removeprefix(f"**Ejemplo {i} — ").split("** ", 1)
        examples.append({"kind": "application_example", "id": id, "title": title,
                         "description": paragraph(description),
                         "disciplines": [action(*AREAS[j]) for j in order]})
    integration = dict(base(3, "c03", "cards"), purpose="application_examples",
                       eyebrow="Ejemplos de aplicación", introduction=paragraph(field(3, "Texto")),
                       items=examples)
    modalities = []
    ids = ("diagnosis-studies", "design-project", "assistance-coordination",
           "programming-integration-verification")
    entries = [line for line in blocks[4] if re.match(r"^\*\*[^*]+\.\*\* ", line)]
    assert len(entries) == 4
    for id, line in zip(ids, entries):
        title, description = line.removeprefix("**").split("** ", 1)
        modalities.append({"kind": "delivery", "id": id, "title": title,
                           "paragraphs": paragraph(description)})
    collaboration = dict(base(4, "c04", "item_list"), purpose="modalities",
                         introduction=paragraph(field(4, "Introducción")), items=modalities)
    contact = dict(base(5, "c05", "text"), paragraphs=paragraph(field(5, "Texto")), actions=[
        action("contact", field(5, "CTA principal").split(" → ")[0], "contacto"),
        action("experience", field(5, "Enlace secundario").split(" → ")[0], "proyectos_experiencia")])
    return [hero, areas, integration, collaboration, contact]


def assert_parity(page):
    assert compact([s.model_dump() for s in page.sections]) == expected_sections()


def test_full_ordered_semantics_from_approved_sources(capacidades):
    assert_parity(capacidades)
    assert capacidades.page_id == CONTENT.stem == "capacidades"
    assert capacidades.locale == "es"
    assert PageContent.model_validate_json(capacidades.model_dump_json()) == capacidades


def test_review_seo_pending_and_deliberate_absence_of_media(capacidades):
    assert capacidades.review.status == "draft"
    assert capacidades.review.source_ref == "D03 V1.22 · C01–C05 · 03.G1-01/02"
    assert capacidades.seo.title is capacidades.seo.description is None
    assert [p.model_dump() for p in capacidades.pending] == [
        {"field": f"seo.{name}", "reason_code": "approval_required", "source_ref": "DEC-05"}
        for name in ("title", "description")]
    assert not validate_pending_fields(capacidades)
    # D05 §35 approves no photographs: no invented MediaRef or media pending.
    assert all(getattr(s, "media", None) is None for s in capacidades.sections)
    assert all(card.media is None for card in capacidades.sections[1].items)


def mutate(data, case):
    s = data["sections"]
    if case == "text": s[0]["paragraphs"][0]["text"] += " Cambio."
    elif case == "section-order": s[2], s[3] = s[3], s[2]
    elif case == "omit-block": s.pop(4)
    elif case == "omit-card": s[1]["items"].pop()
    elif case == "cta": s[4]["actions"][0]["label"] = "Contacta"
    elif case == "destination": s[4]["actions"][0]["target"]["page_id"] = "inicio"
    elif case == "hierarchy": s[0]["subtitle"] = s[0]["paragraphs"].pop()["text"]
    elif case == "replacement": s[2]["items"][0]["description"][0]["text"] = "Proyecto ejecutado por BAFRAS."
    elif case == "addition": s[4]["notes"] = [{"id": "extra", "text": "Servicio adicional."}]
    elif case == "card-order": s[1]["items"].reverse()
    elif case == "scope-order": s[1]["items"][0]["examples"].reverse()
    elif case == "scope-parent":
        a, b = s[1]["items"][:2]
        a["examples"], b["examples"] = b["examples"], a["examples"]
    elif case == "description-parent":
        a, b = s[2]["items"][:2]
        a["description"], b["description"] = b["description"], a["description"]
    elif case == "discipline-order": s[2]["items"][1]["disciplines"].reverse()
    elif case == "discipline-target": s[2]["items"][0]["disciplines"][0]["target"]["page_id"] = "contacto"
    elif case == "anchor": s[0]["actions"][0]["target"]["section_id"] = "c03"
    elif case == "modality-order": s[3]["items"].reverse()
    elif case == "source": s[4]["source_block"] = "C04"
    else: raise AssertionError(case)


@pytest.mark.parametrize("case", [
    "text", "section-order", "omit-block", "omit-card", "cta", "destination",
    "hierarchy", "replacement", "addition", "card-order", "scope-order", "scope-parent",
    "description-parent", "discipline-order", "discipline-target", "anchor", "modality-order", "source",
])
def test_semantic_mutations_validate_but_fail_parity(capacidades, case):
    data = deepcopy(capacidades.model_dump())
    mutate(data, case)
    edited = PageContent.model_validate(data)
    with pytest.raises(AssertionError):
        assert_parity(edited)


@pytest.mark.parametrize("policy", ["INCREMENTAL", "COMPLETE"])
def test_real_b11_inventory_and_every_reference(capacidades, policy, tmp_path):
    # Preserve A3's two-page acceptance scenario as specialties migrate.
    # A4 separately inspects every reference in the evolving real checkout.
    shutil.copytree(ROOT / "config", tmp_path / "config")
    pages = tmp_path / "content/es/pages"
    pages.mkdir(parents=True)
    for name in ("inicio", "capacidades"):
        shutil.copyfile(ROOT / f"content/es/pages/{name}.yaml", pages / f"{name}.yaml")
    paths = ProjectPaths(tmp_path)
    routing = load_site_routing(paths)
    result = inspect_editorial(paths, EditorialLoadRequest(locale="es", policy=policy))
    assert set(result.valid_pages) == {"inicio", "capacidades"}
    assert set(result.missing_page_ids) == set(routing.routes.pages) - set(result.valid_pages)
    assert len(result.expected_page_ids) == 9 and len(result.missing_page_ids) == 7
    assert not result.invalid_page_ids
    assert result.has_errors == (policy == "COMPLETE")
    assert not result.documents_complete and not result.can_build_bundle
    with pytest.raises(ValueError):
        build_editorial_bundle(result)
    report = assess_integrity(result.documents, result.expected_page_ids, report_resolved=True)
    assert report.required_catalogs == ()
    assert not any(d.code == "PENDING_SELECTOR_INVALID" for d in report.diagnostics)
    assert not any(d.reference_status == "UNRESOLVED" for d in report.diagnostics)
    expected = expected_sections()
    expected_links = [(f"sections/{s['id']}/actions/{a['id']}/target", a["target"])
                      for s in expected for a in s.get("actions", [])]
    for section in expected:
        for card in section.get("items", []):
            for field in ("actions", "disciplines"):
                expected_links.extend((f"sections/{section['id']}/items/{card['id']}/{field}/{a['id']}/target", a["target"])
                                      for a in card.get(field, []))
    actual = {d.selector: d for d in report.diagnostics
              if d.document_id == "page/capacidades" and d.reference_status}
    assert set(actual) == {selector for selector, _ in expected_links}
    for selector, target in expected_links:
        diagnostic = actual[selector]
        assert target["page_id"] in routing.routes.pages
        assert diagnostic.target_document_id == "page/" + target["page_id"]
        assert diagnostic.target_id == target.get("section_id", target["page_id"])
        assert diagnostic.reference_status == ("RESOLVED" if target["page_id"] in result.valid_pages else "UNVERIFIABLE")
    inicio_resolved = [d for d in report.diagnostics if d.document_id == "page/inicio"
                       and d.target_document_id == "page/capacidades"]
    assert len(inicio_resolved) == 3
    assert all(d.reference_status == "RESOLVED" for d in inicio_resolved)
    pending = [d for d in result.diagnostics if d.code == "EDITORIAL_PENDING"]
    assert len(pending) == sum(len(p.pending) for p in result.valid_pages.values())
    assert {d.severity for d in result.diagnostics if d.code == "DOCUMENT_MISSING"} == {
        "error" if policy == "COMPLETE" else "warning"}
