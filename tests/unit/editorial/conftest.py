"""A1 contract fixtures, NOT publishable copy or a production content loader.

Headings and selected representative copy come from D03. Remaining strings are
explicitly synthetic; the fixture exercises structure, not migration parity.
The 51-row inventory is independent of the production section union.
"""

from copy import deepcopy
from pathlib import Path
import re

import pytest

from bafras_web.editorial import EditorialBundle

ROOT = Path(__file__).resolve().parents[3]
D03 = ROOT / "docs/project_v02/03_contenido_editorial_V1_22_baseline_G1.md"
SYNTHETIC = "Dato sintético de contrato A1; no publicable."
SECTOR_IDS = [
    "turismo-terciario", "industria-logistica-agroindustria", "infraestructuras-servicios-publicos",
    "salud-educacion-equipamientos", "edificacion-rehabilitacion-activos",
    "comunidades-energeticas-infraestructuras-tecnologicas",
]
# (WEB page identity, documentary prefix, section kinds in D03 order).
INVENTORY = [
    ("inicio", "H", ["hero", "cards", "item_list", "process", "cards", "text", "text"]),
    ("capacidades", "C", ["hero", "cards", "cards", "item_list", "text"]),
    ("infraestructuras", "INF-", ["hero", "item_list", "cards", "item_list", "text", "text", "text"]),
    ("sistemas_energeticos", "ENE-", ["hero", "item_list", "cards", "item_list", "text", "text", "text"]),
    ("automatizacion_control", "DIG-W", ["hero", "item_list", "cards", "item_list", "cards", "text", "text"]),
    ("sectores", "SEC-", ["hero", "sector_index", "text", "text", "text"]),
    ("proyectos_experiencia", "PE-", ["hero", "experience_index", "text", "text"]),
    ("sobre_bafras", "SB-", ["hero", "team", "process", "text", "text"]),
    ("contacto", "CO-", ["hero", "form", "text", "text"]),
]


def paragraph(id="description", text=SYNTHETIC):
    return {"id": id, "text": text}


def action(id="detail", page="contacto", label="Cuéntanos tu proyecto"):
    return {"id": id, "label": label, "target": {"kind": "internal", "page_id": page}}


def numbered(count):
    return [{"id": f"item-{i}", "text": SYNTHETIC} for i in range(1, count + 1)]


def cards(block, title):
    capability = block in ("H02", "C02")
    purpose = "capabilities" if capability else "technical_areas"
    count = 3 if capability else (4 if block == "INF-03" else 6)
    items = []
    for i in range(count):
        item = {"id": f"item-{i+1}", "kind": "capability" if capability else "technical_area",
                "title": SYNTHETIC, "paragraphs": [paragraph()]}
        if capability:
            item.update(examples=numbered(3 if block == "H02" else 4), actions=[action()])
        else:
            item.update(included=numbered(3) if block == "ENE-03" else [],
                        tags=numbered(4) if block == "DIG-W03" else [])
        items.append(item)
    result = {"purpose": purpose, "title": title, "introduction": [paragraph("introduction")], "items": items}
    if not capability:
        result["transversal"] = {"id": "transversal", "title": SYNTHETIC, "paragraphs": [paragraph()]}
    if block == "H02":
        result["actions"] = [action("all", "capacidades", "Todas nuestras capacidades")]
    return result


def make_section(block, kind, title):
    value = {"id": block.lower(), "source_block": block, "kind": kind, "title": title}
    if kind == "hero":
        value.update(eyebrow=SYNTHETIC, paragraphs=[paragraph("main"), paragraph("support")])
        if block not in ("CO-01", "PE-01"):
            value["actions"] = [action(), action("explore", "capacidades", "Explorar capacidades")]
        if block == "PE-01":
            value["attribution"] = "Las referencias de experiencia profesional previa se distinguen de los encargos desarrollados directamente por BAFRAS."
    elif kind == "text":
        value.update(paragraphs=[paragraph("main")], actions=[action()])
        if block in ("C05", "PE-04", "SB-05"):
            value["actions"].append(action("explore", "capacidades", "Explorar capacidades"))
        if block == "H07":
            value["notes"] = [{"id": "collaboration", "text": "También colaboramos con otras ingenierías, instaladores y equipos técnicos."}]
        if block == "SB-04":
            value["paragraphs"].append(paragraph("collaboration"))
        if block in ("INF-05", "ENE-05"):
            value["actions"] = [action("infrastructure", "infraestructuras"), action("energy", "sistemas_energeticos")]
        if block == "CO-03":
            value["actions"] = []
            value["contact_channels"] = [
                {"id": "email", "label": "Correo electrónico", "target": {"kind": "contact", "channel": "email"}},
                {"id": "phone", "label": "Teléfono", "target": {"kind": "contact", "channel": "phone"}},
            ]
    elif kind == "cards":
        if block == "H05":
            value.update(purpose="sector_preview", introduction=[paragraph("introduction")],
                         items=[{"kind": "sector_preview", "id": f"group-{i}", "title": text} for i, text in enumerate([
                             "Hoteles y alojamientos turísticos.", "Industria y procesos.",
                             "Edificios terciarios y comerciales.", "Equipamientos e instalaciones públicas.",
                         ], 1)], actions=[action("sectors", "sectores", "Explorar sectores")])
        elif block == "C03":
            value.update(purpose="application_examples", eyebrow="Ejemplos de aplicación", introduction=[paragraph("introduction")], items=[
                {"kind": "application_example", "id": f"example-{i}", "title": SYNTHETIC,
                 "description": [paragraph()], "disciplines": [action("energy", "sistemas_energeticos")]} for i in range(1, 4)])
        elif block == "DIG-W05":
            value.update(purpose="discipline_relations", items=[
                {"kind": "discipline_relation", "id": id, "title": SYNTHETIC,
                 "description": [paragraph()], "discipline": {"kind": "internal", "page_id": page}}
                for id, page in [("infrastructure", "infraestructuras"), ("energy", "sistemas_energeticos")]
            ], closing=[paragraph("closing")])
        else:
            value.update(cards(block, title))
    elif kind == "item_list":
        needs = block in ("H03", "INF-02", "ENE-02", "DIG-W02")
        count = {"H03": 4, "INF-02": 5, "ENE-02": 6, "DIG-W02": 5}.get(block, 4)
        value.update(purpose="needs" if needs else ("modalities" if block == "C04" else "deliverables"),
                     introduction=[paragraph("introduction")], items=[
                         {"kind": "need" if needs else "delivery", "id": f"item-{i}", "title": SYNTHETIC,
                          "paragraphs": [paragraph()], **({"actions": [action()]} if needs else {})} for i in range(1, count + 1)])
        if not needs:
            value["notes"] = [{"id": "scope", "text": SYNTHETIC}]
    elif kind == "process":
        value.update(purpose="workflow" if block == "H04" else "principles", introduction=[paragraph("introduction")],
                     items=[{"id": f"step-{i}", "title": SYNTHETIC, "paragraphs": [paragraph()]} for i in range(1, 5)],
                     closing=[paragraph("scope")], actions=[action("about", "sobre_bafras")])
    elif kind == "sector_index":
        value.update(introduction=[paragraph("introduction")], sector_refs=SECTOR_IDS.copy())
    elif kind == "experience_index":
        value.update(introduction=[paragraph("introduction")], groups=[
            {"id": id, "title": SYNTHETIC, "introduction": [paragraph("introduction")], "entries": [
                {"id": ref, "experience_ref": ref, "emphasis": "featured" if j == 0 else "complementary"}
                for j, ref in enumerate(refs)]}
            for id, refs in [("infrastructure", ["formentor", "school", "ibiza"]),
                             ("automation", ["wind", "hvac-uib"]), ("energy", ["energy-uib"])]] )
    elif kind == "team":
        value.update(introduction=[paragraph("introduction")], corporate_presentation=[paragraph("presentation",
            "BAFRAS Engineering reúne a dos ingenieros industriales y un ingeniero técnico electrónico, con perfiles complementarios en infraestructuras e instalaciones, sistemas energéticos y automatización y control. Combinamos estas perspectivas para estudiar cada proyecto y desarrollar el alcance de ingeniería que necesita.")],
            person_refs=["murti", "angel", "amin"])
    elif kind == "form":
        value.update(fields=[{"id": id, "label": label} for id, label in [
            ("name", "Nombre"), ("organization", "Empresa u organización"),
            ("email", "Correo electrónico"), ("message", "Cuéntanos qué necesitas")]],
            submit_label="Enviar consulta", messages={"success": "Tu consulta se ha enviado correctamente.",
            "error": "No hemos podido enviar tu consulta. Escríbenos a info@bafras.com."})
        value["fields"][-1]["help"] = "Puedes indicar el tipo de instalación o actividad, el problema o actuación prevista, la ubicación y la fase del proyecto. No necesitas tener todos los datos."
    return value


@pytest.fixture(scope="session")
def source_document():
    return D03.read_text(encoding="utf-8")


@pytest.fixture
def bundle_data(source_document):
    pages = []
    for page, prefix, kinds in INVENTORY:
        sections = []
        for i, kind in enumerate(kinds, 1):
            block = f"{prefix}{i:02}"
            match = re.search(r"^#{2,3} " + re.escape(block) + r" ·[^\n]*\n(.*?)(?=^## |^### PE-|\Z)", source_document, re.M | re.S)
            assert match, block
            title = re.search(r"\*\*H[12]:\*\* (.+)", match.group(1)).group(1)
            section = make_section(block, kind, title)
            if block == "INF-01":
                section["subtitle"] = re.search(r"\*\*Subtítulo:\*\* (.+)", match.group(1)).group(1)
            sections.append(section)
        pending = [{"field": f"seo.{field}", "reason_code": "approval_required"} for field in ("title", "description")]
        if page == "contacto":
            pending.append({"field": "sections/co-02/privacy_text", "reason_code": "source_missing", "source_ref": "D03 CO-02"})
        if page == "inicio":
            pending += [{"field": "sections/h01/media", "reason_code": "integration_pending"},
                        {"field": "sections/h05/items", "reason_code": "approval_required", "source_ref": "DEC-15"}]
        pages.append({"page_id": page, "locale": "es", "review": {"status": "draft"},
                      "seo": {"title": None, "description": None}, "sections": sections, "pending": pending})
    home = pages[0]["sections"][0]
    home.update(eyebrow="BAFRAS ENGINEERING · INGENIERÍA MULTIDISCIPLINAR",
                subtitle="Comprender cada reto. Desarrollar la solución adecuada.",
                paragraphs=[paragraph("introduction", "Analizamos necesidades, evaluamos alternativas y desarrollamos soluciones de ingeniería adaptadas a cada proyecto. Integramos distintas especialidades cuando el reto lo requiere.")])
    # D03 H03 has four distinct destinations, not four copies of contact.
    for item, page in zip(pages[0]["sections"][2]["items"],
                          ["infraestructuras", "sistemas_energeticos", "automatizacion_control", "capacidades"]):
        item["actions"][0]["target"]["page_id"] = page
    # Exercise real, differently sized include/tag lists from the technical copy.
    for page, block, label, target, separator in [
        ("sistemas_energeticos", "ENE-03", "Incluye", "included", ";"),
        ("automatizacion_control", "DIG-W03", "Etiquetas", "tags", "·"),
    ]:
        section = next(p for p in pages if p["page_id"] == page)["sections"][2]
        start = source_document.index(f"## {block} ·")
        end = source_document.index("\n## ", start + 1)
        body = source_document[start:end]
        chunks = re.split(r"^### (?:\d+\. )?", body, flags=re.M)[1:7]
        for item, chunk in zip(section["items"], chunks):
            item["title"] = chunk.splitlines()[0]
            copy = re.search(rf"\*\*{label}:\*\* (.+)", chunk).group(1)
            item[target] = [{"id": f"item-{i}", "text": text.strip()} for i, text in enumerate(copy.split(separator), 1)]
        if block == "ENE-03":
            note = re.search(r"### Nota de alcance[^\n]*\n(.+)", body).group(1)
            section["transversal"] = {"id": "water-efficiency", "title": "Nota de alcance — eficiencia hídrica", "paragraphs": [paragraph("scope", note)]}
    sectors = [{"id": id, "title": SYNTHETIC, "description": [paragraph()], "examples": numbered(3),
                "contextual_actions": [action()], "catalog_refs": []} for id in SECTOR_IDS]
    people = [{"id": id, "public_name": name, "qualification": qualification, "specialty": specialty,
               "review": {"status": "draft"}, "pending": [{"field": "profile", "reason_code": "verification_required"}]}
              for id, name, qualification, specialty in [
                  ("murti", "Murti", "ingeniero industrial", "sistemas energéticos, análisis e integración energética"),
                  ("angel", "Àngel", "ingeniero industrial", "infraestructuras e instalaciones"),
                  ("amin", "Amin", "ingeniero técnico electrónico", "automatización, control y software técnico")]]
    experiences = [{"id": id, "kind": "founder_previous", "title": SYNTHETIC,
                    "review": {"status": "draft"}, "person_refs": [person],
                    "pending": [{"field": "intervention", "reason_code": "verification_required"}]}
                   for id, person in [("formentor", "angel"), ("school", "angel"), ("ibiza", "angel"),
                                      ("wind", "amin"), ("hvac-uib", "murti"), ("energy-uib", "murti")]]
    return {"locale": "es", "pages": pages, "sectors": sectors, "people": people, "experiences": experiences,
            "common": {"actions": [action("project-contact")]}}


@pytest.fixture
def editorial_bundle(bundle_data):
    return EditorialBundle.model_validate(deepcopy(bundle_data))
