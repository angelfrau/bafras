"""A2: real ES copy, the existing YAML loader, A1 models and WEB identities.

The Markdown extraction below is a test oracle only. Production loads the YAML;
it must never scrape D03 or a mockup to generate the site.
"""

from collections import Counter
from copy import deepcopy
from pathlib import Path
import re

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.yaml_files import load_yaml
from bafras_web.application.configuration import load_site_routing
from bafras_web.editorial import PageContent

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/project_v02/03_contenido_editorial_V1_22_baseline_G1.md"
CONTENT = ROOT / "content/es/pages/inicio.yaml"


@pytest.fixture(scope="module")
def routing():
    return load_site_routing(ProjectPaths(ROOT))


@pytest.fixture(scope="module")
def inicio(routing):
    raw = load_yaml(CONTENT)
    assert "locale" not in raw  # Supplied by the loading context, not duplicated.
    return PageContent.model_validate({**raw, "locale": routing.locales.default_locale})


@pytest.fixture(scope="module")
def source_blocks():
    source = SOURCE.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## (H0[1-7]) ·[^\n]*\n", source, re.M))
    assert len(matches) == 7
    result = {}
    for match in matches:
        following = re.search(r"^## ", source[match.end():], re.M)
        assert following
        result[match.group(1)] = source[match.end():match.end() + following.start()]
    return result


def field(block, name):
    match = re.search(r"^\*\*" + re.escape(name) + r":\*\* (.+)$", block, re.M)
    assert match, name
    return match.group(1)


def label(block, name):
    return field(block, name).split(" → ")[0]


def public_strings(value):
    """All populated public fields; retain duplicate text to detect omissions/additions."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in public_strings(item)]
    if isinstance(value, dict):
        return [text for key, item in value.items()
                if key not in {"id", "source_block", "kind", "purpose", "target", "media"}
                for text in public_strings(item)]
    return []


def approved_strings(block_id, block):
    heading = field(block, "H1" if block_id == "H01" else "H2")
    if block_id == "H01":
        return [field(block, "Eyebrow"), heading, field(block, "Subtítulo destacado"), field(block, "Texto"),
                label(block, "CTA principal"), label(block, "CTA secundario")]
    if block_id == "H02":
        values = [heading, field(block, "Introducción")]
        cards = re.findall(r"\*\*Tarjeta \d — (.+?)\*\*\n(.+)\n\*\*Ejemplos:\*\* (.+)\n\*\*Enlace:\*\* (.+?) →", block)
        assert len(cards) == 3
        for title, description, examples, action in cards:
            values.extend([title, description, *examples.split("; "), action])
        return values + [label(block, "Enlace complementario")]
    if block_id == "H03":
        values = [heading, field(block, "Introducción")]
        needs = re.findall(r"\*\*Situación \d — (.+?)\*\*\n(.+)\n\*\*Enlace:\*\* (.+)", block)
        assert len(needs) == 4
        for title, description, action in needs:
            values.extend([title, description, action])
        return values
    if block_id == "H04":
        values = [heading, field(block, "Texto")]
        steps = re.findall(r"\*\*Paso \d — (.+?):\*\* (.+)", block)
        assert len(steps) == 4
        for title, description in steps:
            values.extend([title, description])
        return values + [field(block, "Cierre"), label(block, "Enlace")]
    if block_id == "H05":
        groups = re.findall(r"^- (.+)$", block, re.M)
        assert len(groups) == 4
        return [heading, field(block, "Texto"), *groups, label(block, "Enlace único")]
    if block_id == "H06":
        return [heading, field(block, "Texto"), label(block, "Enlace")]
    return [heading, field(block, "Texto"), label(block, "CTA"), field(block, "Microcopy")]


@pytest.mark.parametrize("block_id", [f"H0{i}" for i in range(1, 8)])
def test_every_public_string_matches_d03(block_id, inicio, source_blocks):
    section = next(s for s in inicio.sections if s.source_block == block_id)
    actual = Counter(public_strings(section.model_dump(mode="json")))
    expected = Counter(approved_strings(block_id, source_blocks[block_id]))
    assert actual == expected, {"missing": expected - actual, "unapproved": actual - expected}


def test_page_identity_locale_and_section_order(inicio, routing):
    assert inicio.page_id == CONTENT.stem == "inicio"
    assert inicio.locale == routing.locales.default_locale == "es"
    assert inicio.locale in routing.locales.codes
    assert routing.url(inicio.page_id, inicio.locale) == "/"
    assert [s.id for s in inicio.sections] == [f"h0{i}" for i in range(1, 8)]
    assert [s.kind for s in inicio.sections] == ["hero", "cards", "item_list", "process", "cards", "text", "text"]
    assert PageContent.model_validate_json(inicio.model_dump_json()) == inicio


def test_all_outgoing_links_use_existing_web_identities(inicio, routing):
    links = assert_configured_destinations(inicio, routing)
    assert len(links) == 14
    assert all(link["page_id"] in routing.routes.pages for link in links)
    # Configured routes do not certify editorial target pages as publishable.
    assert [item.actions[0].target.page_id for item in inicio.sections[1].items] == [
        "infraestructuras", "sistemas_energeticos", "automatizacion_control"]
    assert [item.actions[0].target.page_id for item in inicio.sections[2].items] == [
        "infraestructuras", "sistemas_energeticos", "automatizacion_control", "capacidades"]


def test_approval_gaps_are_explicit_and_not_public_copy(inicio):
    assert inicio.review.status == "draft"
    assert inicio.seo.title is None and inicio.seo.description is None
    pending = {entry.field: entry for entry in inicio.pending}
    assert len(pending) == len(inicio.pending) == 8
    assert pending["seo.title"].source_ref == pending["seo.description"].source_ref == "DEC-05"
    assert pending["sections/h05/items"].reason_code == "approval_required"
    media_paths = {
        "sections/h01/media", "sections/h02/items/infrastructure/media",
        "sections/h02/items/energy/media", "sections/h02/items/automation/media", "sections/h03/media",
    }
    assert {path for path in pending if path.endswith("/media")} == media_paths
    assert all(pending[path].reason_code == "integration_pending" for path in media_paths)
    assert inicio.sections[0].media is None and inicio.sections[2].media is None
    assert all(item.media is None for item in inicio.sections[1].items)
    assert not any("PENDIENTE" in text.upper() or "SINTÉTICO" in text.upper()
                   for s in inicio.sections for text in public_strings(s.model_dump()))


def test_collection_order_and_semantic_ids_survive_editing(inicio):
    expected = {
        "h02": ["infrastructure", "energy", "automation"],
        "h03": ["installation-performance", "energy-decision", "equipment-integration", "multidisciplinary-project"],
        "h04": ["understand", "evaluate", "develop", "verify"],
        "h05": ["hospitality", "industry", "tertiary", "public-facilities"],
    }
    for section in inicio.sections:
        if section.id in expected:
            assert [item.id for item in section.items] == expected[section.id]
    data = deepcopy(inicio.model_dump())
    original = {item["id"]: item for item in data["sections"][1]["items"]}
    data["sections"][1]["items"].reverse()
    edited = PageContent.model_validate(data)
    assert [item.id for item in edited.sections[1].items] == list(reversed(expected["h02"]))
    assert {item.id: item.model_dump() for item in edited.sections[1].items} == original


def test_no_synthetic_portfolio_or_extra_mockup_panels(inicio):
    assert not any(s.kind == "experience_index" for s in inicio.sections)
    assert inicio.sections[3].purpose == "workflow"
    assert len(inicio.sections[4].items) == 4  # Not the six-sector taxonomy.
    assert len(inicio.sections[5].paragraphs) == 1
    assert not inicio.sections[5].notes
    assert inicio.sections[6].actions[0].label == "Hablemos de tu proyecto"


def expected_semantics(source_blocks):
    """D03 relationships + explicitly assigned stable IDs, not a copy of the YAML.

    Text and ordering are extracted from D03's few known H01–H07 structures.
    Destinations map D03 names/codes to WEB IDs; no new route registry is created.
    """
    destinations = {
        "Contacto": "contacto", "Capacidades": "capacidades", "índice Capacidades": "capacidades", "Sectores": "sectores",
        "capacidad INF": "infraestructuras", "capacidad ENE": "sistemas_energeticos",
        "capacidad DIG": "automatizacion_control", "Infraestructuras e instalaciones": "infraestructuras",
        "Sistemas energéticos": "sistemas_energeticos", "Automatización y control": "automatizacion_control",
        "Sobre BAFRAS": "sobre_bafras", "Proyectos y experiencia": "proyectos_experiencia",
    }

    def paragraph(id, text):
        return {"id": id, "text": text}

    def action(id, text):
        parts = text.split(" → ")
        caption, destination = (parts[0], parts[1]) if len(parts) == 2 else (text, text)
        return {"id": id, "label": caption,
                "target": {"kind": "internal", "page_id": destinations[destination.removesuffix(".")]}}

    def section(block_id, kind, **values):
        return {"id": block_id.lower(), "source_block": block_id, "kind": kind, **values}

    h01, h02, h03, h04, h05, h06, h07 = [source_blocks[f"H0{i}"] for i in range(1, 8)]
    hero = section("H01", "hero", eyebrow=field(h01, "Eyebrow"), title=field(h01, "H1"),
                   subtitle=field(h01, "Subtítulo destacado"), paragraphs=[paragraph("introduction", field(h01, "Texto"))],
                   actions=[action("contact", field(h01, "CTA principal")), action("capabilities", field(h01, "CTA secundario"))])
    cards = re.findall(r"\*\*Tarjeta \d — (.+?)\*\*\n(.+)\n\*\*Ejemplos:\*\* (.+)\n\*\*Enlace:\*\* (.+)", h02)
    assert len(cards) == 3
    card_ids = ["infrastructure", "energy", "automation"]
    example_ids = [["electrical", "hvac", "coordination"], ["analysis", "renewables", "storage"],
                   ["automation", "supervision", "integration"]]
    capability_items = []
    for (title, description, examples, link), id, ids in zip(cards, card_ids, example_ids, strict=True):
        texts = examples.split("; ")
        capability_items.append({"id": id, "kind": "capability", "title": title,
                                 "paragraphs": [paragraph("description", description)],
                                 "examples": [paragraph(eid, text) for eid, text in zip(ids, texts, strict=True)],
                                 "actions": [action("detail", link)]})
    capabilities = section("H02", "cards", purpose="capabilities", title=field(h02, "H2"),
                           introduction=[paragraph("introduction", field(h02, "Introducción"))], items=capability_items,
                           actions=[action("all-capabilities", field(h02, "Enlace complementario"))])
    needs = re.findall(r"\*\*Situación \d — (.+?)\*\*\n(.+)\n\*\*Enlace:\*\* (.+)", h03)
    assert len(needs) == 4
    need_ids = ["installation-performance", "energy-decision", "equipment-integration", "multidisciplinary-project"]
    need_items = [{"id": id, "kind": "need", "title": title,
                   "paragraphs": [paragraph("description", description)], "actions": [action("detail", link)]}
                  for id, (title, description, link) in zip(need_ids, needs, strict=True)]
    situations = section("H03", "item_list", purpose="needs", title=field(h03, "H2"),
                         introduction=[paragraph("introduction", field(h03, "Introducción"))], items=need_items)
    steps = re.findall(r"\*\*Paso \d — (.+?):\*\* (.+)", h04)
    assert len(steps) == 4
    step_ids = ["understand", "evaluate", "develop", "verify"]
    workflow = section("H04", "process", purpose="workflow", title=field(h04, "H2"),
                       introduction=[paragraph("introduction", field(h04, "Texto"))],
                       items=[{"id": id, "title": title, "paragraphs": [paragraph("description", text)]}
                              for id, (title, text) in zip(step_ids, steps, strict=True)],
                       closing=[paragraph("contracted-scope", field(h04, "Cierre"))],
                       actions=[action("about", field(h04, "Enlace"))])
    groups = re.findall(r"^- (.+)$", h05, re.M)
    assert len(groups) == 4
    group_ids = ["hospitality", "industry", "tertiary", "public-facilities"]
    sectors = section("H05", "cards", purpose="sector_preview", title=field(h05, "H2"),
                      introduction=[paragraph("introduction", field(h05, "Texto"))],
                      items=[{"id": id, "kind": "sector_preview", "title": title}
                             for id, title in zip(group_ids, groups, strict=True)],
                      actions=[action("sectors", field(h05, "Enlace único"))])
    experience = section("H06", "text", title=field(h06, "H2"), paragraphs=[paragraph("introduction", field(h06, "Texto"))],
                         actions=[action("experience", field(h06, "Enlace"))])
    closing = section("H07", "text", title=field(h07, "H2"), paragraphs=[paragraph("introduction", field(h07, "Texto"))],
                      actions=[action("contact", field(h07, "CTA"))], notes=[paragraph("collaboration", field(h07, "Microcopy"))])
    return [hero, capabilities, situations, workflow, sectors, experience, closing]


def populated_fields(value):
    """Ignore unpopulated optional defaults, retain every populated field and ID."""
    if isinstance(value, dict):
        return {key: populated_fields(item) for key, item in value.items() if item is not None and item != []}
    if isinstance(value, list):
        return [populated_fields(item) for item in value]
    return value


def assert_semantic_parity(page, source_blocks):
    expected = expected_semantics(source_blocks)
    assert [s.id for s in page.sections] == [s["id"] for s in expected], "Orden e identidad de secciones D03"
    for section, approved in zip(page.sections, expected, strict=True):
        assert populated_fields(section.model_dump(mode="json")) == approved, section.source_block


def assert_configured_destinations(page, routing):
    links = []
    def visit(value):
        if isinstance(value, dict):
            if value.get("kind") == "internal":
                assert value["page_id"] in routing.routes.pages, value["page_id"]
                links.append(value)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(page.model_dump())
    return links


def test_structured_semantic_parity_h01_h07(inicio, source_blocks):
    assert_semantic_parity(inicio, source_blocks)


@pytest.mark.parametrize("mutation", [
    "swap_descriptions", "swap_examples", "swap_destinations", "move_text", "delete_text",
    "add_text", "reorder_sections", "reorder_steps", "wrong_document_id", "swap_section_text",
])
def test_semantic_mutations_are_detected(mutation, inicio, source_blocks):
    data = deepcopy(inicio.model_dump())
    cards = data["sections"][1]["items"]
    if mutation == "swap_descriptions":
        cards[0]["paragraphs"], cards[1]["paragraphs"] = cards[1]["paragraphs"], cards[0]["paragraphs"]
    elif mutation == "swap_examples":
        cards[0]["examples"], cards[1]["examples"] = cards[1]["examples"], cards[0]["examples"]
    elif mutation == "swap_destinations":
        actions = data["sections"][0]["actions"]  # Both configured; old card checks don't cover hero CTA.
        actions[0]["target"], actions[1]["target"] = actions[1]["target"], actions[0]["target"]
    elif mutation == "move_text":
        note = cards[0]["examples"].pop()
        note["id"] = "moved-example"
        cards[1]["examples"].append(note)
    elif mutation == "delete_text":
        cards[0]["examples"].pop()
    elif mutation == "add_text":
        data["sections"][5]["notes"].append({"id": "mockup", "text": "Texto adicional de maqueta"})
    elif mutation == "reorder_sections":
        data["sections"][1], data["sections"][2] = data["sections"][2], data["sections"][1]
    elif mutation == "reorder_steps":
        data["sections"][3]["items"].reverse()
    elif mutation == "wrong_document_id":
        data["sections"][1]["source_block"] = "H03"
    elif mutation == "swap_section_text":
        data["sections"][5]["paragraphs"], data["sections"][6]["paragraphs"] = data["sections"][6]["paragraphs"], data["sections"][5]["paragraphs"]
    edited = PageContent.model_validate(data)  # Structural validity is intentionally insufficient.
    if mutation in {"swap_descriptions", "swap_examples", "move_text", "swap_destinations", "reorder_steps"}:
        for original, changed in zip(inicio.sections, edited.sections, strict=True):
            assert Counter(public_strings(original.model_dump())) == Counter(public_strings(changed.model_dump()))
    with pytest.raises(AssertionError):
        assert_semantic_parity(edited, source_blocks)


def test_unknown_page_reference_is_detected(inicio, routing):
    data = deepcopy(inicio.model_dump())
    data["sections"][0]["actions"][0]["target"]["page_id"] = "not_configured"
    edited = PageContent.model_validate(data)
    with pytest.raises(AssertionError, match="not_configured"):
        assert_configured_destinations(edited, routing)


def test_configured_target_swap_is_not_publication_evidence(inicio, routing, source_blocks):
    data = deepcopy(inicio.model_dump())
    actions = data["sections"][0]["actions"]
    actions[0]["target"], actions[1]["target"] = actions[1]["target"], actions[0]["target"]
    edited = PageContent.model_validate(data)
    assert_configured_destinations(edited, routing)
    with pytest.raises(AssertionError):
        assert_semantic_parity(edited, source_blocks)
    # RouteTable has no section registry, copy-review or per-page release field.
    assert "section_id" not in type(next(iter(routing.routes.pages.values()))).model_fields
