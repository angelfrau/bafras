"""A5 documentary oracle, catalogs, attribution and complete ES integration.

Expectations read D03 directly. No migration utility is imported or retained.
"""

from collections import Counter
from copy import deepcopy
from pathlib import Path
import re

import pytest
from pydantic import TypeAdapter

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.yaml_files import load_yaml
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.entities import Person, Sector
from bafras_web.editorial.integrity import assess_integrity, build_editorial_bundle
from bafras_web.editorial.pages import PageContent
from bafras_web.editorial.pending import validate_pending_fields

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/project_v02/03_contenido_editorial_V1_22_baseline_G1.md"
PAGES = {"sectores": ("SEC", 5), "proyectos_experiencia": ("PE", 4),
         "sobre_bafras": ("SB", 5), "contacto": ("CO", 4)}
SECTORS = ("turismo-terciario", "industria-logistica-agroindustria", "infraestructuras-servicios-publicos",
           "salud-educacion-equipamientos", "edificacion-rehabilitacion-activos",
           "comunidades-energeticas-infraestructuras-tecnologicas")


def document():
    return SOURCE.read_text(encoding="utf-8")


def block(code):
    lines = document().splitlines()
    start = next(i for i, line in enumerate(lines) if re.match(r"^#{2,3} " + code + r" ·", line))
    level = len(lines[start].split(" ", 1)[0])
    end = next(i for i in range(start + 1, len(lines))
               if re.match(r"^#{1," + str(level) + r"} ", lines[i]))
    return [line for line in lines[start + 1:end] if line and line != "---"]


def marked(lines, label):
    prefix = f"**{label}:** "
    return next(line[len(prefix):] for line in lines if line.startswith(prefix))


def bare(lines):
    return [line for line in lines if not line.startswith(("#", "*", "-"))]


def p(text, id="description"):
    return [{"id": id, "text": text}]


def action(id, label, target, section=None):
    link = {"kind": "internal", "page_id": target}
    if section:
        link["section_id"] = section
    return {"id": id, "label": label.split(" → ")[0], "target": link}


def expected_sectors():
    lines = block("SEC-02")
    headings = [i for i, line in enumerate(lines) if line.startswith("### ")]
    assert len(headings) == 6
    targets = ("sistemas_energeticos", "automatizacion_control", "infraestructuras",
               "infraestructuras", "infraestructuras", "sistemas_energeticos")
    result = []
    for id, target, start in zip(SECTORS, targets, headings):
        rows = lines[start + 1:start + 4]
        examples = marked(rows, "Ejemplos breves").split(" · ")
        assert len(examples) == 3
        result.append({"id": id, "title": re.sub(r"^### \d+\. ", "", lines[start]),
                       "description": p(marked(rows, "Texto")),
                       "examples": [{"id": f"example-{i}", "text": text} for i, text in enumerate(examples, 1)],
                       "contextual_actions": [action("explore", marked(rows, "Enlace contextual"), target)]})
    return result


def expected_people():
    source = document().split("## 1. Identidad profesional — decisión cerrada", 1)[1].split("## 2.", 1)[0]
    result = []
    for id, name in (("murti", "Murti"), ("angel", "Àngel"), ("amin", "Amin")):
        line = next(line for line in source.splitlines() if line.startswith(f"- {name}:"))
        qualification = line.split("**")[1]
        specialty = line.split("Especialidad editorial: ", 1)[1]
        result.append({"id": id, "public_name": name, "qualification": qualification, "specialty": specialty,
                       "review": {"status": "draft", "source_ref": "D03 03.K §1"},
                       "verification": {"verified": False, "authorized": False}, "pending": [
                           {"field": "public_name", "reason_code": "verification_required",
                            "source_ref": "D03 03.K §1 · confirmar grafía pública y consentimiento"},
                           {"field": "biography", "reason_code": "verification_required",
                            "source_ref": "D03 03.K §1 · biografía contrastada no disponible"}]})
    return result


def expected_sections(page_id):
    prefix, count = PAGES[page_id]
    blocks = [block(f"{prefix}-{i:02}") for i in range(1, count + 1)]

    def base(i, kind):
        return {"id": f"{prefix.lower()}-{i:02}", "source_block": f"{prefix}-{i:02}", "kind": kind,
                "title": marked(blocks[i - 1], "H1" if i == 1 else "H2")}

    def text(i, actions=()):
        body = ([marked(blocks[i - 1], "Texto")] if prefix in ("SEC", "PE") else bare(blocks[i - 1]))
        if prefix == "CO":
            body = body[:1]
        return {**base(i, "text"), "paragraphs": [{"id": "description" if j == 0 else "collaboration", "text": t}
                                                  for j, t in enumerate(body)],
                **({"actions": list(actions)} if actions else {})}

    hero = dict(base(1, "hero"), eyebrow=marked(blocks[0], "Eyebrow"),
                paragraphs=p(marked(blocks[0], "Texto") if prefix in ("SEC", "PE") else bare(blocks[0])[0]))
    if prefix == "SEC":
        hero["actions"] = [action("explore", marked(blocks[0], "CTA principal"), "sectores", "sectores"),
                           action("contact", marked(blocks[0], "CTA secundario"), "contacto")]
        index = dict(base(2, "sector_index"), id="sectores", sector_refs=list(SECTORS),
                     introduction=p(marked(blocks[1], "Introducción"), "introduction"))
        return [hero, index, text(3, [action("capabilities", marked(blocks[2], "Enlace"), "capacidades")]),
                text(4, [action("about", marked(blocks[3], "Enlace"), "sobre_bafras")]),
                text(5, [action("contact", marked(blocks[4], "CTA"), "contacto")])]
    if prefix == "PE":
        hero["attribution"] = marked(blocks[0], "Nota de atribución visible junto al índice")
        starts = [i for i, line in enumerate(blocks[1]) if line.startswith("#### ")]
        assert len(starts) == 3
        groups = [{"id": id, "title": blocks[1][i].removeprefix("#### "),
                   "introduction": p(marked([blocks[1][i + 1]], "Introducción"), "introduction")}
                  for id, i in zip(("infrastructure", "automation", "energy"), starts)]
        index = dict(base(2, "experience_index"), introduction=p(marked(blocks[1], "Intro"), "introduction"), groups=groups)
        return [hero, index, text(3), text(4, [
            action("contact", marked(blocks[3], "CTA principal"), "contacto"),
            action("capabilities", marked(blocks[3], "Enlace secundario"), "capacidades")])]
    if prefix == "SB":
        hero["actions"] = [action("experience", marked(blocks[0], "Enlace contextual"), "proyectos_experiencia")]
        corporate = next(line for line in document().splitlines() if line.startswith("**Texto publicable de presentación del equipo:"))
        team = dict(base(2, "team"), introduction=p(bare(blocks[1])[0], "introduction"),
                    corporate_presentation=p(corporate.split("«", 1)[1].split("»", 1)[0]),
                    person_refs=["murti", "angel", "amin"])
        entries = [line for line in blocks[2] if re.match(r"^\*\*[^*]+\.\*\* ", line)]
        assert len(entries) == 4
        process = dict(base(3, "process"), purpose="principles", introduction=p(bare(blocks[2])[0], "introduction"),
                       items=[{"id": id, "title": line.split("**")[1], "paragraphs": p(line.split("** ", 1)[1])}
                              for id, line in zip(("understand", "evaluate", "develop", "verify"), entries)],
                       closing=p(bare(blocks[2])[-1], "scope"))
        return [hero, team, process, text(4, [action("experience", marked(blocks[3], "Enlace"), "proyectos_experiencia")]),
                text(5, [action("contact", marked(blocks[4], "CTA principal"), "contacto"),
                         action("capabilities", marked(blocks[4], "CTA secundario"), "capacidades")])]
    labels = [marked(blocks[1], f"Campo {i}").split(" — ")[0] for i in range(1, 5)]
    fields = [{"id": id, "label": label, "required": "*" in label}
              for id, label in zip(("name", "company", "email", "message"), labels)]
    fields[-1]["help"] = marked(blocks[1], "Campo 4").split("«", 1)[1].split("»", 1)[0]
    k2 = document().split("# Decisión 03.K.2", 1)[1].split("## ADENDA", 1)[0]
    success = k2.split("Éxito: «", 1)[1].split("»", 1)[0]
    error = k2.split("Error: «", 1)[1].split("»", 1)[0]
    form = dict(base(2, "form"), fields=fields, submit_label=marked(blocks[1], "Botón"),
                messages={"success": success, "error": error})
    ad = document().split("## ADENDA 03.CO-02", 1)[1].split("## ADENDA", 1)[0]
    email = ad.split("**Correo público:** `", 1)[1].split("`", 1)[0]
    phone = ad.split("**Teléfono público autorizado:** **", 1)[1].split("**", 1)[0]
    direct = text(3)
    direct["contact_channels"] = [{"id": id, "label": label, "value": value,
                                   "target": {"kind": "contact", "channel": channel}}
                                  for id, label, value, channel in (("email", "Correo electrónico", email, "email"),
                                                                    ("phone", "Teléfono", phone, "phone"))]
    return [hero, form, direct, text(4)]


def compact(value):
    if isinstance(value, dict):
        return {k: compact(v) for k, v in value.items() if v is not None and v != []}
    if isinstance(value, list):
        return [compact(v) for v in value]
    return value


def assert_parity(page):
    assert compact([s.model_dump() for s in page.sections]) == expected_sections(page.page_id)


@pytest.fixture(params=PAGES)
def page(request):
    path = ROOT / f"content/es/pages/{request.param}.yaml"
    raw = load_yaml(path)
    assert raw["page_id"] == path.stem == request.param and "locale" not in raw
    return PageContent.model_validate({**raw, "locale": "es"})


def test_all_approved_copy_parent_child_order_and_identity(page):
    assert_parity(page)
    assert len(page.sections) == PAGES[page.page_id][1]
    assert page.locale == "es" and page.review.status == "draft"
    assert PageContent.model_validate_json(page.model_dump_json()) == page
    assert validate_pending_fields(page) == []


def test_exact_seo_review_and_pending_metadata(page):
    source = document()
    if page.page_id == "sectores":
        lines = source.split("# UX y publicación (interno)", 1)[1].split("## Matriz", 1)[0].splitlines()
        expected_seo = {"title": next(line.removeprefix("- SEO title: ") for line in lines if line.startswith("- SEO title: ")),
                        "description": next(line.removeprefix("- Meta description: ") for line in lines if line.startswith("- Meta description: "))}
        pending = []
    elif page.page_id == "proyectos_experiencia":
        line = next(line for line in source.splitlines() if line.startswith("- SEO: título «"))
        expected_seo = {"title": line.split("«", 1)[1].split("»", 1)[0], "description": None}
        pending = [{"field": "seo.description", "reason_code": "source_missing",
                    "source_ref": "D03 PE · UX y SEO: intención sin descripción literal"},
                   {"field": "sections/pe-02/groups", "reason_code": "verification_required",
                    "source_ref": "D03 PE-02 · 03.K §2 · 03.G1-02 · seis referencias candidatas sin confirmación ni autorización"}]
    else:
        start = "## UX y SEO Sobre BAFRAS" if page.page_id == "sobre_bafras" else "## Conversión, accesibilidad y tecnología"
        lines = source.split(start, 1)[1].splitlines()
        expected_seo = {"title": marked(lines, "Title"), "description": marked(lines, "Meta description")}
        pending = [] if page.page_id == "sobre_bafras" else [
            {"field": "sections/co-02/privacy_text", "reason_code": "source_missing",
             "source_ref": "D03 CO-02 · 03.K §4 · política real pendiente de revisión legal"}]
    assert page.seo.model_dump() == expected_seo
    assert [p.model_dump() for p in page.pending] == pending
    prefix, count = PAGES[page.page_id]
    assert page.review.source_ref == f"D03 V1.22 · {prefix}-01–{prefix}-{count:02} · 03.K/03.G1-01/02"
    assert page.sections[0].media is None


@pytest.mark.parametrize("name,cls,expected", [("sectors", Sector, expected_sectors), ("people", Person, expected_people)])
def test_real_catalogs_exactly_match_d03(name, cls, expected):
    raw = load_yaml(ROOT / f"content/es/entities/{name}.yaml")
    values = TypeAdapter(list[cls]).validate_python(raw)
    actual = [compact(v.model_dump()) for v in values]
    assert actual == expected()
    if cls is Person:
        assert all(pending.field in Person.model_fields for person in values for pending in person.pending)


@pytest.mark.parametrize("case", ("omit", "text", "order", "cta", "destination", "claim", "condition", "addition"))
def test_valid_mutations_fail_independent_parity(page, case):
    data = deepcopy(page.model_dump())
    sections = data["sections"]
    if case == "omit": sections.pop()
    elif case == "text": sections[0]["paragraphs"][0]["text"] += " Cambio."
    elif case == "order": sections[1], sections[2] = sections[2], sections[1]
    elif case in ("cta", "destination"):
        if page.page_id == "contacto":
            if case == "cta": sections[1]["submit_label"] = "Solicitar presupuesto"
            else: sections[2]["contact_channels"][0]["target"]["channel"] = "phone"
        else:
            section = next(s for s in reversed(sections) if s.get("actions"))
            if case == "cta": section["actions"][0]["label"] = "Solicitar presupuesto"
            else: section["actions"][0]["target"]["page_id"] = "inicio"
    elif case == "claim": sections[0]["paragraphs"][0]["text"] = "Todos estos proyectos fueron contratados por BAFRAS."
    elif case == "condition": sections[-1]["paragraphs"][0]["text"] = "Garantizamos resultados y respuesta inmediata."
    elif case == "addition": sections[0]["subtitle"] = "Empresa certificada con más de cien proyectos."
    edited = PageContent.model_validate(data)
    with pytest.raises(AssertionError): assert_parity(edited)


@pytest.mark.parametrize("name", ("sectors", "people"))
@pytest.mark.parametrize("case", ("omission", "order", "grouping", "claim"))
def test_catalog_mutations_keep_validation_but_lose_fidelity(name, case):
    cls, expected = (Sector, expected_sectors) if name == "sectors" else (Person, expected_people)
    raw = load_yaml(ROOT / f"content/es/entities/{name}.yaml")
    if case == "omission": raw.pop()
    elif case == "order": raw.reverse()
    elif case == "grouping":
        key = "examples" if name == "sectors" else "specialty"
        raw[0][key], raw[1][key] = raw[1][key], raw[0][key]
    else:
        if name == "sectors": raw[0]["description"][0]["text"] = "Clientes corporativos acreditados."
        else: raw[0]["qualification"] = "Empresa certificada"
    values = TypeAdapter(list[cls]).validate_python(raw)
    assert [compact(v.model_dump()) for v in values] != expected()


def test_no_unverified_experience_or_optional_pdf_catalogs_are_fabricated():
    page = PageContent.model_validate({**load_yaml(ROOT / "content/es/pages/proyectos_experiencia.yaml"), "locale": "es"})
    assert [len(g.entries) for g in page.sections[1].groups] == [0, 0, 0]
    assert not (ROOT / "content/es/entities/experiences.yaml").exists()
    assert not (ROOT / "content/es/entities/resources.yaml").exists()
    assert all(not s.catalog_refs for s in TypeAdapter(list[Sector]).validate_python(load_yaml(ROOT / "content/es/entities/sectors.yaml")))
    assert any(p.field == "sections/pe-02/groups" and p.reason_code == "verification_required" for p in page.pending)


def reference_inventory(value, path=""):
    """Inventory serialized links and entity identities independently of B1.1."""
    if isinstance(value, dict):
        if value.get("kind") == "internal":
            yield path, (f"page/{value['page_id']}", value.get("section_id") or value["page_id"])
        elif value.get("kind") == "contact":
            yield path, (None, None)
        else:
            for key, child in value.items():
                current = f"{path}/{key}".lstrip("/")
                if key in ("sector_refs", "person_refs"):
                    catalog = "sectors" if key == "sector_refs" else "people"
                    for id in child:
                        yield f"{current}/{id}", (f"catalog/{catalog}", id)
                else:
                    yield from reference_inventory(child, current)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            if isinstance(child, dict):
                yield from reference_inventory(child, f"{path}/{child.get('id', i)}")


@pytest.mark.parametrize("policy", ("INCREMENTAL", "COMPLETE"))
def test_real_nine_page_bundle_and_all_reference_states(policy):
    result = inspect_editorial(ProjectPaths(ROOT), EditorialLoadRequest(locale="es", policy=policy))
    assert len(result.valid_pages) == len(result.expected_page_ids) == 9
    assert not result.missing_page_ids and not result.invalid_page_ids
    assert result.documents_complete and result.can_build_bundle and not result.has_errors
    report = assess_integrity(result.documents, result.expected_page_ids, report_resolved=True)
    assert set(report.required_catalogs) == {"sectors", "people"}
    assert not any(d.reference_status == "UNRESOLVED" for d in report.diagnostics)
    assert all(d.reference_status == "RESOLVED" for d in report.diagnostics
               if d.target_document_id is not None)
    for doc in result.documents:
        if isinstance(doc.value, PageContent):
            expected = dict(reference_inventory(doc.value.model_dump()))
        elif isinstance(doc.value, tuple) and doc.kind == "sectors":
            expected = dict(reference_inventory([s.model_dump() for s in doc.value], "sectors"))
        else:
            continue
        actual = {d.selector: d for d in report.diagnostics if d.document_id == doc.document_id and d.reference_status}
        assert actual.keys() == expected.keys()
        for selector, (target_doc, id) in expected.items():
            assert actual[selector].target_document_id == target_doc
            assert actual[selector].target_id == id
            assert actual[selector].reference_status == ("RESOLVED" if target_doc else "UNVERIFIABLE")
    assert not any(d.code == "PENDING_SELECTOR_INVALID" for d in result.diagnostics)
    assert Counter((d.document_id, d.selector) for d in result.diagnostics if d.code == "EDITORIAL_PENDING") == Counter(
        (f"page/{page.page_id}", pending.field) for page in result.valid_pages.values() for pending in page.pending)
    bundle = build_editorial_bundle(result)
    assert {p.page_id for p in bundle.pages} == set(result.expected_page_ids)
    assert sum(len(p.sections) for p in bundle.pages) == 51
    assert len(bundle.sectors) == 6 and len(bundle.people) == 3
    assert bundle.experiences == bundle.resources == []
    assert all(p.review.status == "draft" for p in bundle.pages)
