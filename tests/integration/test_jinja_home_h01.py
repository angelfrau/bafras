"""WEB-V01-A.1: real editorial content (Inicio · H01) rendered through the Jinja2 adapter.

The test composes the context itself: the adapter never receives editorial objects.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from jinja2 import ChoiceLoader, FileSystemLoader

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.jinja import render_html, template_environment
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial import HeroSection
from bafras_web.editorial.integrity import build_editorial_bundle

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = Path(__file__).with_name("templates")


def test_inicio_h01_title_renders_into_preview_document():
    inspection = inspect_editorial(ProjectPaths(ROOT), EditorialLoadRequest(locale="es", policy="COMPLETE"))
    bundle = build_editorial_bundle(inspection)
    page = bundle.get_page("inicio")
    h01 = next(section for section in page.sections if section.id == "h01")
    assert isinstance(h01, HeroSection)
    before = page.model_dump()

    env = template_environment()
    env = env.overlay(loader=ChoiceLoader([FileSystemLoader(TEMPLATES), env.loader]))
    output = render_html("h01_preview.html", {
        "lang": bundle.locale,
        "title": f"PREVIEW · {page.page_id} · {bundle.locale}",
        "robots": "noindex, nofollow",
        "preview_notice": "Vista previa interna · no publicable",
        "heading": h01.title,
    }, environment=env)

    headings = re.findall(r"<h1>(.*?)</h1>", output, re.S)
    assert [html.unescape(text) for text in headings] == [h01.title]
    assert '<html lang="es">' in output
    assert '<meta name="robots" content="noindex, nofollow">' in output
    assert 'class="preview-notice"' in output
    assert "canonical" not in output and "hreflang" not in output
    assert page.model_dump() == before
