from __future__ import annotations

import os
import subprocess
import sys

import pytest
from jinja2 import ChoiceLoader, DictLoader, TemplateNotFound, TemplateSyntaxError, UndefinedError

from bafras_web.adapters.jinja import render_html, template_environment

BASE = {"lang": "es", "title": "Documento"}


def _with_templates(**templates: str):
    env = template_environment()
    return env.overlay(loader=ChoiceLoader([DictLoader(templates), env.loader]))


def test_package_templates_are_discoverable():
    assert "layouts/base.html" in template_environment().list_templates()


def test_environment_is_shared():
    assert template_environment() is template_environment()


def test_base_is_an_html5_document():
    html = render_html("layouts/base.html", BASE)
    assert html.startswith("<!doctype html>\n<html lang=\"es\">")
    assert '<meta charset="utf-8">' in html and 'name="viewport"' in html
    assert "<title>Documento</title>" in html and '<main id="contenido">' in html
    assert "robots" not in html and "preview-notice" not in html


def test_optional_preview_signals_come_only_from_context():
    html = render_html("layouts/base.html", {**BASE, "robots": "noindex, nofollow", "preview_notice": "Vista previa"})
    assert '<meta name="robots" content="noindex, nofollow">' in html
    assert '<p class="preview-notice" role="note">Vista previa</p>' in html


def test_child_template_extends_base():
    env = _with_templates(**{"child.html": '{% extends "layouts/base.html" %}{% block main %}<h1>{{ heading }}</h1>{% endblock %}'})
    html = render_html("child.html", {**BASE, "heading": "Hola"}, environment=env)
    assert "<main id=\"contenido\">\n<h1>Hola</h1>  </main>" in html


@pytest.mark.parametrize("value, escaped", [
    ("<script>alert(1)</script>", "&lt;script&gt;alert(1)&lt;/script&gt;"),
    ('"&\' onload=', "&#34;&amp;&#39; onload="),
])
def test_context_values_are_escaped(value, escaped):
    html = render_html("layouts/base.html", {"lang": value, "title": value})
    assert html.count(escaped) == 2 and value not in html


def test_context_is_data_not_template_code():
    html = render_html("layouts/base.html", {**BASE, "title": "{{ 7 * 7 }} {% raw %}"})
    assert "<title>{{ 7 * 7 }} {% raw %}</title>" in html


def test_utf8_text_is_preserved():
    title = "Ingeniería · Àngel · Ingenieurleistungen für Anlagen — «ç»"
    assert f"<title>{title}</title>" in render_html("layouts/base.html", {**BASE, "title": title})


def test_missing_variable_fails():
    with pytest.raises(UndefinedError, match="title"):
        render_html("layouts/base.html", {"lang": "es"})


def test_missing_template_fails():
    with pytest.raises(TemplateNotFound):
        render_html("layouts/no-existe.html", BASE)


def test_syntax_error_is_propagated_with_location():
    env = _with_templates(**{"broken.html": "line 1\n{% if %}"})
    with pytest.raises(TemplateSyntaxError) as info:
        render_html("broken.html", BASE, environment=env)
    assert info.value.lineno == 2 and info.value.name == "broken.html"


def test_rendering_does_not_depend_on_working_directory(tmp_path):
    code = (
        "from bafras_web.adapters.jinja import render_html;"
        "print(render_html('layouts/base.html', {'lang': 'es', 'title': 'x'}).splitlines()[1])"
    )
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    result = subprocess.run([sys.executable, "-I", "-c", code], cwd=tmp_path, env=env,
                            capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == '<html lang="es">'


def test_adapter_knows_no_editorial_routing_or_yaml_code():
    import ast
    import bafras_web.adapters.jinja as module

    tree = ast.parse(open(module.__file__, encoding="utf-8").read())
    imported = {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
    imported |= {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
    assert not {m for m in imported if m and (m.startswith("bafras_web") or m.startswith("yaml"))}
