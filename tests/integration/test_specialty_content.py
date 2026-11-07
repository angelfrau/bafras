"""A4: complete ordered semantics from D03, independent of migrated YAML.

One parameterized contract covers all three specialties without duplicating
the documentary oracle or the mutation/integrity machinery. No production
code interprets Markdown. Explicit identities below are migration decisions.
"""

from collections import Counter
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
PAGES = ("infraestructuras", "sistemas_energeticos", "automatizacion_control")
PREFIXES = dict(zip(PAGES, ("INF-", "ENE-", "DIG-W")))
NEEDS = dict(zip(PAGES, (
    ("new-installation", "operating-incidents", "technical-infrastructure", "technical-safety", "investment-decisions"),
    ("reduce-consumption", "generation-storage", "electrification", "charging-assets", "cost-monitoring", "decarbonization"),
    ("missing-data", "unstable-control", "disconnected-equipment", "modernization", "data-decisions"),
)))
AREAS = dict(zip(PAGES, (
    ("electrical", "thermal", "hydraulic", "protection"),
    ("diagnosis-efficiency", "renewables-storage", "electrification-thermal", "mobility-integrated", "management-costs", "decarbonization"),
    ("instrumentation", "automation-programming", "supervision", "ot-integration", "technical-software", "energy-assets"),
)))
DELIVERIES = dict(zip(PAGES, (
    ("diagnosis-studies", "design-project", "assistance-coordination", "testing-verification"),
    ("diagnosis-audit", "feasibility-alternatives", "engineering-project", "integration-monitoring"),
    ("diagnosis-definition", "design", "development-integration", "testing-documentation"),
)))


def source_blocks(page_id):
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    blocks = []
    for number in range(1, 8):
        block = f"{PREFIXES[page_id]}{number:02}"
        start = next(i for i, line in enumerate(lines) if line.startswith(f"## {block} ·"))
        end = next(i for i in range(start + 1, len(lines))
                   if lines[i].startswith("## ") or lines[i] == "---")
        blocks.append([line for line in lines[start + 1:end] if line])
    return blocks


def marked(lines, label):
    """Read one marked field, including inline INF action fields."""
    text = "\n".join(lines).split(f"**{label}:** ", 1)[1]
    return text.split("\n", 1)[0].split(" **", 1)[0]


def paragraphs(text, id="description"):
    return [{"id": id, "text": text}]


def action(id, label, target, section=None):
    destination = {"kind": "internal", "page_id": target}
    if section:
        destination["section_id"] = section
    return {"id": id, "label": label, "target": destination}


def expected_sections(page_id):
    blocks = source_blocks(page_id)
    prefix = PREFIXES[page_id]
    section_ids = (prefix.lower() + "01", "necesidades", "ambitos", "entregables", "integracion",
                   prefix.lower() + "06", prefix.lower() + "07")

    def base(number, kind):
        return {"id": section_ids[number - 1], "source_block": f"{prefix}{number:02}", "kind": kind,
                "title": marked(blocks[number - 1], "H1" if number == 1 else "H2")}

    hero = dict(base(1, "hero"), eyebrow=marked(blocks[0], "Eyebrow"))
    if page_id == "infraestructuras":
        hero["subtitle"] = marked(blocks[0], "Subtítulo")
        hero["paragraphs"] = paragraphs(marked(blocks[0], "Texto de apoyo"), "support")
        secondary = "Enlace secundario"
    else:
        hero["paragraphs"] = [
            {"id": "main", "text": marked(blocks[0], "Texto principal")},
            {"id": "support", "text": marked(blocks[0], "Texto de apoyo")},
        ]
        secondary = "CTA secundario"
    hero["actions"] = [
        action("contact", marked(blocks[0], "CTA principal").split(" → ")[0], "contacto"),
        action("explore", marked(blocks[0], secondary).split(" → ")[0], page_id, "ambitos"),
    ]
    needs = []
    entries = [line for line in blocks[1] if re.match(r"^\d+\. \*\*", line)]
    assert len(entries) == len(NEEDS[page_id])
    for id, line in zip(NEEDS[page_id], entries):
        title, description = line.split("**", 2)[1:]
        needs.append({"id": id, "kind": "need", "title": title,
                      "paragraphs": paragraphs(description.removeprefix(" "))})
    need_section = dict(base(2, "item_list"), purpose="needs",
                        introduction=paragraphs(marked(blocks[1], "Introducción"), "introduction"), items=needs)
    areas = []
    headings = [i for i, line in enumerate(blocks[2]) if line.startswith("### ")]
    assert len(headings) == len(AREAS[page_id]) + (page_id != "automatizacion_control")
    for id, index in zip(AREAS[page_id], headings):
        title = re.sub(r"^\d+\. ", "", blocks[2][index].removeprefix("### "))
        card = {"id": id, "kind": "technical_area", "title": title,
                "paragraphs": paragraphs(blocks[2][index + 1])}
        if page_id != "infraestructuras":
            field, key, separator = (("Incluye", "included", "; ") if page_id == "sistemas_energeticos"
                                     else ("Etiquetas", "tags", " · "))
            texts = marked([blocks[2][index + 2]], field).split(separator)
            card[key] = [{"id": f"{key}-{i}", "text": text} for i, text in enumerate(texts, 1)]
        areas.append(card)
    if page_id == "automatizacion_control":
        index = next(i for i, line in enumerate(blocks[2]) if line.startswith("**Bloque transversal — "))
        title = blocks[2][index].removeprefix("**Bloque transversal — ").removesuffix("**")
        aside = {"id": "transversal", "title": title, "paragraphs": paragraphs(blocks[2][index + 1])}
    else:
        index = headings[-1]
        # INF's treatment instruction is internal metadata; ENE's note is copy.
        aside = {"id": "transversal", "title": blocks[2][index].removeprefix("### "),
                 "paragraphs": paragraphs(blocks[2][index + (2 if page_id == "infraestructuras" else 1)])}
    area_section = dict(base(3, "cards"), purpose="technical_areas",
                        introduction=paragraphs(marked(blocks[2], "Introducción"), "introduction"),
                        items=areas, transversal=aside)
    deliveries = []
    entries = [line for line in blocks[3] if line.startswith("- **")]
    assert len(entries) == 4
    for id, line in zip(DELIVERIES[page_id], entries):
        title, description = line.removeprefix("- **").split(":** ", 1)
        deliveries.append({"kind": "delivery", "id": id, "title": title,
                           "paragraphs": paragraphs(description)})
    note_name = {"infraestructuras": "Nota de precisión", "sistemas_energeticos": "Criterio",
                 "automatizacion_control": "Nota"}[page_id]
    deliverable_section = dict(base(4, "item_list"), purpose="deliverables", items=deliveries,
                               notes=[{"id": "scope", "text": marked(blocks[3], note_name)}])
    if page_id == "infraestructuras":
        deliverable_section["introduction"] = paragraphs(marked(blocks[3], "Introducción"), "introduction")
    if page_id == "automatizacion_control":
        relations = []
        for id, title, target in (("infrastructure", "Infraestructuras e instalaciones", "infraestructuras"),
                                  ("energy", "Sistemas energéticos", "sistemas_energeticos")):
            body = marked(blocks[4], title).split(" → ")[0]
            relations.append({"id": id, "kind": "discipline_relation", "title": title,
                              "description": paragraphs(body),
                              "discipline": {"kind": "internal", "page_id": target}})
        related = dict(base(5, "cards"), purpose="discipline_relations", items=relations,
                       closing=paragraphs(marked(blocks[4], "Texto de cierre"), "closing"))
    else:
        body = marked(blocks[4], "Texto") if page_id == "infraestructuras" else blocks[4][1]
        labels = ([marked(blocks[4], f"Enlace {n}").split(" → ")[0] for n in (1, 2)]
                  if page_id == "infraestructuras" else
                  [line.removeprefix("**Enlace:** ").split(" → ")[0] for line in blocks[4] if line.startswith("**Enlace:** ")])
        targets = (("energy", "sistemas_energeticos"), ("automation", "automatizacion_control")) if page_id == "infraestructuras" else (
            ("infrastructure", "infraestructuras"), ("automation", "automatizacion_control"))
        related = dict(base(5, "text"), paragraphs=paragraphs(body),
                       actions=[action(id, label, target) for label, (id, target) in zip(labels, targets)])
    closing_sections = []
    for number, id, target, label_name in ((6, "experience", "proyectos_experiencia", "Enlace"),
                                           (7, "contact", "contacto", "CTA")):
        lines = blocks[number - 1]
        body = lines[1] if page_id == "sistemas_energeticos" else marked(lines, "Texto")
        closing_sections.append(dict(base(number, "text"), paragraphs=paragraphs(body),
                                     actions=[action(id, marked(lines, label_name).split(" → ")[0], target)]))
    return [hero, need_section, area_section, deliverable_section, related, *closing_sections]


def compact(value):
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items() if item is not None and item != []}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def assert_parity(page):
    assert compact([s.model_dump() for s in page.sections]) == expected_sections(page.page_id)


@pytest.mark.parametrize("page_id", PAGES)
def test_documentary_omission_is_detected_before_parity(page_id, monkeypatch):
    original = Path.read_text
    source = SOURCE.read_text(encoding="utf-8")
    start = source.index(f"## {PREFIXES[page_id]}02 ·")
    line = next(line for line in source[start:].splitlines() if line.startswith("1. **"))
    omitted = source.replace(line + "\n", "", 1)
    monkeypatch.setattr(Path, "read_text", lambda path, *args, **kwargs:
                        omitted if path == SOURCE else original(path, *args, **kwargs))
    with pytest.raises(AssertionError):
        expected_sections(page_id)


@pytest.fixture(params=PAGES)
def specialty(request):
    file = ROOT / "content/es/pages" / f"{request.param}.yaml"
    raw = load_yaml(file)
    assert raw["page_id"] == request.param == file.stem
    assert "locale" not in raw
    return PageContent.model_validate({**raw, "locale": "es"})


def test_complete_ordered_copy_and_hierarchy(specialty):
    assert_parity(specialty)
    assert specialty.locale == "es"
    assert len(specialty.sections) == 7
    assert specialty.review.status == "draft"
    prefix = PREFIXES[specialty.page_id]
    assert specialty.review.source_ref == f"D03 V1.22 · {prefix}01–{prefix}07 · 03.G1-01/02"
    assert PageContent.model_validate_json(specialty.model_dump_json()) == specialty


def test_seo_and_exact_pending_contract(specialty):
    page_id = specialty.page_id
    expected = []
    if page_id != "automatizacion_control":
        assert specialty.seo.title is specialty.seo.description is None
        expected.extend({"field": f"seo.{field}", "reason_code": "approval_required", "source_ref": "DEC-05"}
                        for field in ("title", "description"))
    else:
        source = SOURCE.read_text(encoding="utf-8")
        seo = source.split("## Navegación, diseño y SEO", 1)[1].split("## ", 1)[0].splitlines()
        assert specialty.seo.title == next(line.removeprefix("- SEO title: ") for line in seo if line.startswith("- SEO title: "))
        assert specialty.seo.description == next(line.removeprefix("- Meta description: ") for line in seo if line.startswith("- Meta description: "))
    media = {
        "infraestructuras": (("inf-01", "D05 §26 · R18"),),
        "sistemas_energeticos": (("ene-01", "D05 §29 · R10"), ("ambitos", "D05 §29 · R08")),
        "automatizacion_control": (("dig-w01", "D05 §31 · R01"), ("ambitos", "D05 §31 · R03")),
    }
    expected.extend({"field": f"sections/{section}/media", "reason_code": "integration_pending",
                     "source_ref": source + " · contrato MediaRef pendiente de WEB"}
                    for section, source in media[page_id])
    assert [pending.model_dump() for pending in specialty.pending] == expected
    assert not validate_pending_fields(specialty)
    assert specialty.sections[0].media is specialty.sections[2].media is None


def mutate(data, case):
    s = data["sections"]
    if case == "text": s[0]["paragraphs"][0]["text"] += " Cambio."
    elif case == "order": s[1], s[2] = s[2], s[1]
    elif case == "omission": s.pop(5)
    elif case == "card-omission": s[2]["items"].pop()
    elif case == "cta": s[0]["actions"][0]["label"] = "Solicita presupuesto"
    elif case == "target": s[0]["actions"][0]["target"]["page_id"] = "inicio"
    elif case == "grouping":
        a, b = s[2]["items"][:2]
        a["paragraphs"], b["paragraphs"] = b["paragraphs"], a["paragraphs"]
    elif case == "absolute-claim": s[1]["items"][0]["paragraphs"][0]["text"] = "Garantizamos todos los resultados en cualquier encargo."
    elif case == "addition": s[2]["closing"] = [{"id": "extra", "text": "Certificaciones propias."}]
    elif case == "transversal": s[2]["transversal"] = None
    elif case == "note": s[3]["notes"] = []
    elif case == "card-order": s[2]["items"].reverse()
    elif case == "need-order": s[1]["items"].reverse()
    elif case == "hierarchy": s[0]["attribution"] = s[0]["paragraphs"].pop()["text"]
    elif case == "punctuation": s[0]["title"] = s[0]["title"].rstrip(".")
    elif case == "anchor": s[0]["actions"][1]["target"]["section_id"] = "entregables"
    else: raise AssertionError(case)


@pytest.mark.parametrize("case", [
    "text", "order", "omission", "card-omission", "cta", "target", "grouping", "absolute-claim",
    "addition", "transversal", "note", "card-order", "need-order", "hierarchy", "punctuation", "anchor",
])
def test_valid_pydantic_mutations_fail_documentary_parity(specialty, case):
    data = deepcopy(specialty.model_dump())
    mutate(data, case)
    edited = PageContent.model_validate(data)
    with pytest.raises(AssertionError):
        assert_parity(edited)


@pytest.mark.parametrize("page_id,key", [("sistemas_energeticos", "included"),
                                        ("automatizacion_control", "tags")])
@pytest.mark.parametrize("case", ("order", "omission", "parent"))
def test_services_and_tags_keep_their_approved_parent_and_order(page_id, key, case):
    raw = load_yaml(ROOT / f"content/es/pages/{page_id}.yaml")
    cards = raw["sections"][2]["items"]
    if case == "order":
        cards[0][key].reverse()
    elif case == "omission":
        cards[0][key].pop()
    else:
        cards[0][key], cards[1][key] = cards[1][key], cards[0][key]
    edited = PageContent.model_validate({**raw, "locale": "es"})
    with pytest.raises(AssertionError):
        assert_parity(edited)


def internal_links(value, path=""):
    """Independent inventory from serialized data, including item identities."""
    if isinstance(value, dict):
        if value.get("kind") == "internal":
            yield path, value
        else:
            for key, item in value.items():
                yield from internal_links(item, f"{path}/{key}".lstrip("/"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            if isinstance(item, dict):
                yield from internal_links(item, f"{path}/{item.get('id', index)}")


def expected_links(page_id):
    links = {}
    for section in expected_sections(page_id):
        prefix = f"sections/{section['id']}"
        for a in section.get("actions", []):
            links[f"{prefix}/actions/{a['id']}/target"] = a["target"]
        for item in section.get("items", []):
            if "discipline" in item:
                links[f"{prefix}/items/{item['id']}/discipline"] = item["discipline"]
    return links


@pytest.mark.parametrize("policy", ("INCREMENTAL", "COMPLETE"))
def test_real_five_page_integrity_and_each_outgoing_reference(policy, tmp_path):
    # Freeze A4's historical scenario; A5 inspects the complete real checkout.
    shutil.copytree(ROOT / "config", tmp_path / "config")
    pages = tmp_path / "content/es/pages"
    pages.mkdir(parents=True)
    for page_id in ("inicio", "capacidades", *PAGES):
        shutil.copyfile(ROOT / f"content/es/pages/{page_id}.yaml", pages / f"{page_id}.yaml")
    paths = ProjectPaths(tmp_path)
    routing = load_site_routing(paths)
    inspection = inspect_editorial(paths, EditorialLoadRequest(locale="es", policy=policy))
    assert set(inspection.valid_pages) == {"inicio", "capacidades", *PAGES}
    assert set(inspection.missing_page_ids) == set(routing.routes.pages) - set(inspection.valid_pages)
    assert len(inspection.expected_page_ids) == 9 and len(inspection.missing_page_ids) == 4
    assert not inspection.invalid_page_ids and not inspection.documents_complete
    assert not inspection.can_build_bundle
    assert inspection.has_errors == (policy == "COMPLETE")
    with pytest.raises(ValueError):
        build_editorial_bundle(inspection)
    report = assess_integrity(inspection.documents, inspection.expected_page_ids, report_resolved=True)
    assert report.required_catalogs == ()
    assert not any(d.reference_status == "UNRESOLVED" for d in report.diagnostics)
    assert not any(d.code == "PENDING_SELECTOR_INVALID" for d in report.diagnostics)
    # Match every reference, not just aggregate warning/resolution counts.
    for page in inspection.valid_pages.values():
        inventory = dict(internal_links(page.model_dump()))
        diagnostics = {d.selector: d for d in report.diagnostics
                       if d.document_id == f"page/{page.page_id}" and d.reference_status}
        assert inventory.keys() == diagnostics.keys()
        for selector, target in inventory.items():
            d = diagnostics[selector]
            assert d.target_document_id == f"page/{target['page_id']}"
            assert target["page_id"] in routing.routes.pages
            available = target["page_id"] in inspection.valid_pages
            if available and target["section_id"]:
                assert target["section_id"] in {s.id for s in inspection.valid_pages[target["page_id"]].sections}
            assert d.target_id == (target["section_id"] or target["page_id"])
            assert d.reference_status == ("RESOLVED" if available else "UNVERIFIABLE")
    for page_id in PAGES:
        expected = expected_links(page_id)
        actual = {d.selector: d for d in report.diagnostics
                  if d.document_id == f"page/{page_id}" and d.reference_status}
        assert actual.keys() == expected.keys()
        for selector, target in expected.items():
            d = actual[selector]
            assert target["page_id"] in routing.routes.pages
            assert d.target_document_id == f"page/{target['page_id']}"
            assert d.target_id == target.get("section_id", target["page_id"])
            assert d.reference_status == ("RESOLVED" if target["page_id"] in inspection.valid_pages else "UNVERIFIABLE")
    # Every incoming specialty reference from the existing pages is now available.
    incoming = [d for d in report.diagnostics if d.document_id in ("page/inicio", "page/capacidades")
                and d.target_document_id in {f"page/{id}" for id in PAGES}]
    assert incoming and all(d.reference_status == "RESOLVED" for d in incoming)
    expected_pending = Counter((f"page/{page.page_id}", p.field, p.reason_code)
                               for page in inspection.valid_pages.values() for p in page.pending)
    assert Counter((d.document_id, d.selector, d.reason_code) for d in inspection.diagnostics
                   if d.code == "EDITORIAL_PENDING") == expected_pending
    missing = [d for d in inspection.diagnostics if d.code == "DOCUMENT_MISSING"]
    assert len(missing) == len(inspection.missing_page_ids)
    assert {d.severity for d in missing} == {"error" if policy == "COMPLETE" else "warning"}
