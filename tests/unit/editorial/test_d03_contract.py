"""An explicit 51-block structural acceptance matrix, independent of the models.

Media is an acknowledged integration gap, not evidence of full visual coverage.
Fixtures preserve structure and selected literal copy; they are not ES migration.
"""

import ast
import re
from pathlib import Path

import pytest

import bafras_web.editorial as editorial
from bafras_web.editorial import EditorialBundle
from bafras_web.site.routes import PageId
from bafras_web.localization.locales import LocaleCode
from pydantic import TypeAdapter


# Block, kind, non-empty typed fields required by this documentary block.
COVERAGE = [
    ("H01", "hero", "eyebrow title subtitle paragraphs actions"),
    ("H02", "cards", "title introduction items actions"),
    ("H03", "item_list", "title introduction items"),
    ("H04", "process", "title introduction items closing actions"),
    ("H05", "cards", "title introduction items actions"),
    ("H06", "text", "title paragraphs actions"),
    ("H07", "text", "title paragraphs actions notes"),
    ("C01", "hero", "eyebrow title paragraphs actions"),
    ("C02", "cards", "title introduction items"),
    ("C03", "cards", "eyebrow title introduction items"),
    ("C04", "item_list", "title introduction items"),
    ("C05", "text", "title paragraphs actions"),
    ("INF-01", "hero", "eyebrow title subtitle paragraphs actions"),
    ("INF-02", "item_list", "title introduction items"),
    ("INF-03", "cards", "title introduction items transversal"),
    ("INF-04", "item_list", "title introduction items notes"),
    ("INF-05", "text", "title paragraphs actions"),
    ("INF-06", "text", "title paragraphs actions"),
    ("INF-07", "text", "title paragraphs actions"),
    ("ENE-01", "hero", "eyebrow title paragraphs actions"),
    ("ENE-02", "item_list", "title introduction items"),
    ("ENE-03", "cards", "title introduction items transversal"),
    ("ENE-04", "item_list", "title items notes"),
    ("ENE-05", "text", "title paragraphs actions"),
    ("ENE-06", "text", "title paragraphs actions"),
    ("ENE-07", "text", "title paragraphs actions"),
    ("DIG-W01", "hero", "eyebrow title paragraphs actions"),
    ("DIG-W02", "item_list", "title introduction items"),
    ("DIG-W03", "cards", "title introduction items transversal"),
    ("DIG-W04", "item_list", "title items notes"),
    ("DIG-W05", "cards", "title items closing"),
    ("DIG-W06", "text", "title paragraphs actions"),
    ("DIG-W07", "text", "title paragraphs actions"),
    ("SEC-01", "hero", "eyebrow title paragraphs actions"),
    ("SEC-02", "sector_index", "title introduction sector_refs"),
    ("SEC-03", "text", "title paragraphs actions"),
    ("SEC-04", "text", "title paragraphs actions"),
    ("SEC-05", "text", "title paragraphs actions"),
    ("PE-01", "hero", "eyebrow title paragraphs attribution"),
    ("PE-02", "experience_index", "title introduction groups"),
    ("PE-03", "text", "title paragraphs"),
    ("PE-04", "text", "title paragraphs actions"),
    ("SB-01", "hero", "eyebrow title paragraphs actions"),
    ("SB-02", "team", "title introduction corporate_presentation person_refs"),
    ("SB-03", "process", "title introduction items closing"),
    ("SB-04", "text", "title paragraphs actions"),
    ("SB-05", "text", "title paragraphs actions"),
    ("CO-01", "hero", "eyebrow title paragraphs"),
    ("CO-02", "form", "title fields submit_label messages"),
    ("CO-03", "text", "title paragraphs contact_channels"),
    ("CO-04", "text", "title paragraphs"),
]


@pytest.mark.parametrize("block,kind,fields", COVERAGE, ids=[row[0] for row in COVERAGE])
def test_documentary_block_has_typed_locations(block, kind, fields, editorial_bundle, source_document):
    sections = [s for p in editorial_bundle.pages for s in p.sections if s.source_block == block]
    assert len(sections) == 1
    section = sections[0]
    assert section.kind == kind
    assert section.title in source_document
    for field in fields.split():
        assert getattr(section, field), (block, field)
    # Reconstruction must preserve all the populated fields, order and identities.
    rebuilt = EditorialBundle.model_validate_json(editorial_bundle.model_dump_json())
    other = next(s for p in rebuilt.pages for s in p.sections if s.source_block == block)
    assert other.model_dump(mode="json") == section.model_dump(mode="json")


def test_inventory_is_exactly_d03_and_web_pages(editorial_bundle, source_document):
    blocks = re.findall(r"^#{2,3} ((?:H\d{2}|C\d{2}|INF-\d{2}|ENE-\d{2}|DIG-W\d{2}|SEC-\d{2}|PE-\d{2}|SB-\d{2}|CO-\d{2})) ·", source_document, re.M)
    assert len(blocks) == len(COVERAGE) == 51
    assert blocks == [row[0] for row in COVERAGE]
    assert [s.source_block for p in editorial_bundle.pages for s in p.sections] == blocks
    # Reuse WEB's existing acceptance boundary without importing it into domain.
    for page in editorial_bundle.pages:
        assert TypeAdapter(PageId).validate_python(page.page_id) == page.page_id
        assert TypeAdapter(LocaleCode).validate_python(page.locale) == page.locale


def test_real_structural_particularities(editorial_bundle, source_document):
    sections = {s.source_block: s for p in editorial_bundle.pages for s in p.sections}
    assert len(sections["H02"].items) == len(sections["C02"].items) == 3
    assert all(len(i.examples) == 3 and i.actions for i in sections["H02"].items)
    assert all(len(i.examples) == 4 for i in sections["C02"].items)
    assert [i.actions[0].target.page_id for i in sections["H03"].items] == [
        "infraestructuras", "sistemas_energeticos", "automatizacion_control", "capacidades"]
    assert len(sections["H04"].items) == len(sections["H05"].items) == 4
    assert len(sections["INF-03"].items) == 4
    assert sections["INF-03"].transversal.paragraphs
    assert len(sections["ENE-03"].items) == len(sections["DIG-W03"].items) == 6
    for item in sections["ENE-03"].items:
        assert item.included
        assert all(value.text in source_document for value in item.included)
    assert sections["ENE-03"].transversal.id == "water-efficiency"
    for item in sections["DIG-W03"].items:
        assert item.tags and all(tag.text in source_document for tag in item.tags)
    assert len(sections["SEC-02"].sector_refs) == 6
    assert [len(g.entries) for g in sections["PE-02"].groups] == [3, 2, 1]
    assert sum(e.emphasis == "featured" for g in sections["PE-02"].groups for e in g.entries) == 3
    assert all(e.review.status == "draft" and not e.verification.authorized for e in editorial_bundle.experiences)
    assert len(sections["SB-02"].person_refs) == 3
    assert sections["SB-02"].corporate_presentation[0].text in source_document
    assert len(sections["SB-04"].paragraphs) == 2
    form = sections["CO-02"]
    assert [f.id for f in form.fields] == ["name", "organization", "email", "message"]
    assert form.fields[-1].help in source_document
    assert form.messages.success == "Tu consulta se ha enviado correctamente."
    assert form.messages.error == "No hemos podido enviar tu consulta. Escríbenos a info@bafras.com."
    assert form.privacy_text is None
    assert any(p.field == "sections/co-02/privacy_text" for p in editorial_bundle.get_page("contacto").pending)


def test_domain_has_no_io_templates_or_routing_dependencies():
    package = Path(editorial.__file__).parent
    forbidden = {"yaml", "jinja2", "os", "pathlib", "shutil", "io", "importlib", "subprocess"}
    forbidden_calls = {"open", "eval", "exec", "__import__"}
    for path in package.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                assert not any(alias.name.split(".")[0] in forbidden for alias in node.names)
            if isinstance(node, ast.ImportFrom) and node.module:
                assert node.module.split(".")[0] not in forbidden
                assert not node.module.startswith(("bafras_web.site", "bafras_web.localization", "bafras_web.templates"))
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                assert node.func.id not in forbidden_calls
