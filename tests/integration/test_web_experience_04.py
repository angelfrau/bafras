"""WEB-EXPERIENCE-04 V3: cartera BAFRAS (bloque 01), filas de experiencia (bloque 02), créditos de imagen,
imagen de Automatización y fichas con contenido técnico ampliado.

Los proyectos BAFRAS y el contenido ampliado son fixtures en memoria (experience_fixtures.py), nunca CONTENT.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application import build
from bafras_web.application.build import BuildError, BuildRequest, build_site, render_experience, render_page
from bafras_web.application.configuration import load_media_manifest, load_site_composition
from bafras_web.application.presentation import PORTFOLIO_KIND

sys.path.insert(0, str(Path(__file__).parent))  # --import-mode=importlib: módulos de apoyo de este directorio
import experience_fixtures as fx  # noqa: E402
from test_web_experience_03 import Doc  # noqa: E402

PATHS = ProjectPaths(Path(__file__).resolve().parents[2])
LOCALES = ("es", "ca", "en", "de")
LOGOS = {"brand__logo", "site-footer__logo"}


@pytest.fixture(scope="module")
def inputs():
    return {locale: build._load_inputs(PATHS, locale) for locale in LOCALES}


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    out = tmp_path_factory.mktemp("we04")
    for locale in LOCALES:
        build_site(PATHS, locale, "preview", out)
    return out / "preview"


def _index(inputs_, locale="es") -> Doc:
    return Doc(render_page(PATHS, BuildRequest(locale, fx.INDEX_PAGE, "preview"), inputs=inputs_).html)


def _messages(data) -> dict[str, str]:
    return {m.id: m.text for m in data.bundle.common.interface_messages}


def _cards(doc: Doc) -> list[dict]:
    return doc.all("li", "portfolio-card")


# ---------- Bloque 01 · Proyectos BAFRAS ----------

@pytest.mark.parametrize("locale", LOCALES)
def test_real_content_shows_empty_portfolio_before_professional_experience(site, inputs, locale):
    data = inputs[locale]
    assert not [e for e in data.bundle.experiences if e.kind == PORTFOLIO_KIND]  # hoy no hay proyectos aprobados
    html = (site / data.routing.url(fx.INDEX_PAGE, locale).lstrip("/") / "index.html").read_text(encoding="utf-8")
    doc = Doc(html)
    messages = _messages(data)
    blocks = doc.all("section", "experience-block")
    assert [b["id"] for b in blocks] == ["pe-02-portfolio", "pe-02-previous"]  # 01 antes que 02
    assert "portfolio--empty" in blocks[0]["class"]
    assert not _cards(doc) and not doc.all("button", "portfolio__control") and "data-portfolio" not in html
    assert messages["experience-portfolio"] in doc.texts and messages["experience-previous-work"] in " ".join(doc.texts)
    assert not doc.by_class.get("portfolio__empty")  # sin mensaje aprobado no se redacta ninguno
    # Sin fotografías de experiencia previa en el bloque de cartera
    assert html.index('id="pe-02-portfolio"') < html.index('id="pe-02-previous"')
    portfolio_html = html[html.index('id="pe-02-portfolio"'):html.index('id="pe-02-previous"')]
    assert "<img" not in portfolio_html and "<a " not in portfolio_html


def test_empty_message_is_shown_only_when_content_provides_it(inputs):
    doc = _index(fx.with_index(inputs["es"], messages={"experience-portfolio-empty": "Fixture mensaje vacío"}))
    assert doc.by_class["portfolio__empty"] == ["Fixture mensaje vacío"]


def test_one_project_is_a_static_card_without_controls(inputs):
    data = fx.portfolio_inputs(inputs["es"], 1, controls=False)  # con uno, los controles no son necesarios
    doc = _index(data)
    html = render_page(PATHS, BuildRequest("es", fx.INDEX_PAGE, "preview"), inputs=data).html
    assert len(_cards(doc)) == 1 and not doc.all("button", "portfolio__control") and "data-portfolio" not in html
    track = doc.all("ul", "portfolio__track")[0]
    assert "portfolio__track--1" in track["class"] and "tabindex" not in track


@pytest.mark.parametrize("count", [2, 4])
def test_several_projects_get_a_scrollable_track_with_accessible_controls(inputs, count):
    data = fx.portfolio_inputs(inputs["es"], count)
    html = render_page(PATHS, BuildRequest("es", fx.INDEX_PAGE, "preview"), inputs=data).html
    doc = Doc(html)
    cards = _cards(doc)
    assert len(cards) == count and html.count("data-portfolio ") + html.count("data-portfolio>") == 1
    track = doc.all("ul", "portfolio__track")[0]
    assert track["tabindex"] == "0" and track["aria-labelledby"] == "pe-02-portfolio-title"
    buttons = doc.all("button", "portfolio__control")
    assert len(buttons) == 2 and all(b["type"] == "button" and b["aria-controls"] == track["id"] for b in buttons)
    assert fx.CONTROL_MESSAGES["experience-portfolio-previous"] in doc.texts
    assert fx.CONTROL_MESSAGES["experience-portfolio-next"] in doc.texts
    assert doc.all("div", "portfolio__controls")[0].get("hidden") is not None  # JS los muestra solo si hay desplazamiento


def test_controls_require_localized_labels_instead_of_falling_back(inputs):
    with pytest.raises(BuildError) as info:
        render_page(PATHS, BuildRequest("es", fx.INDEX_PAGE, "preview"), inputs=fx.portfolio_inputs(inputs["es"], 3, controls=False))
    assert any("experience-portfolio-next" in p for p in info.value.problems)


def test_portfolio_order_classification_links_and_fichas(inputs):
    data = fx.portfolio_inputs(inputs["es"], 4)
    doc = _index(data)
    page = data.bundle.get_page(fx.INDEX_PAGE)
    index = next(s for s in page.sections if s.kind == "experience_index")
    ordered = [e.experience_ref for g in index.groups for e in g.entries
               if data.bundle.get_experience(e.experience_ref).kind == PORTFOLIO_KIND]
    titles = [t for t in doc.by_class["portfolio-card"] if t.startswith("Fixture proyecto")]
    assert titles == [data.bundle.get_experience(ref).title for ref in ordered]  # orden editorial
    hrefs = [a["href"] for a in doc.all("a") if a.get("aria-describedby", "").startswith("pe-02-fixture")]
    assert hrefs == [data.routing.entity_url("experience", ref, "es") for ref in ordered]
    groups = {e.experience_ref: g.title for g in index.groups for e in g.entries}
    assert doc.by_class["portfolio-card__category"] == [groups[ref] for ref in ordered]
    assert len(doc.all("li", "experience-row")) == 7  # la experiencia previa no cambia
    for ref in ordered:  # la misma entidad tiene ficha con la plantilla estándar
        ficha = Doc(render_experience(PATHS, "es", ref, "preview", inputs=data).html)
        assert data.bundle.get_experience(ref).title in ficha.texts


def test_classification_comes_from_kind_not_from_names(inputs):
    data = inputs["es"]
    first = data.bundle.experiences[0]
    flipped = fx.with_index(data, replace={first.id: first.model_copy(update={"kind": PORTFOLIO_KIND})})
    doc = _index(flipped)
    assert len(_cards(doc)) == 1 and first.title in doc.by_class["portfolio-card"]
    assert len(doc.all("li", "experience-row")) == 6 and first.title not in doc.by_class["experience-row"]


def test_scope_with_only_bafras_projects_is_not_listed_in_block_02(inputs):
    data = inputs["es"]
    page = data.bundle.get_page(fx.INDEX_PAGE)
    index = next(s for s in page.sections if s.kind == "experience_index")
    last = index.groups[-1]
    replace = {e.experience_ref: data.bundle.get_experience(e.experience_ref).model_copy(update={"kind": PORTFOLIO_KIND})
               for e in last.entries}
    doc = _index(fx.with_index(data, replace=replace, messages=fx.CONTROL_MESSAGES))
    assert len(doc.all("section", "experience-group")) == len(index.groups) - 1
    assert f"#{index.id}-{last.id}" not in [a["href"] for a in doc.all("a")]
    assert len(_cards(doc)) == len(last.entries)


# ---------- Bloque 02 · Experiencia profesional ----------

@pytest.mark.parametrize("locale", LOCALES)
def test_rows_put_image_first_and_text_only_rows_have_no_placeholder(site, inputs, locale):
    data = inputs[locale]
    composition = load_site_composition(PATHS)
    html = (site / data.routing.url(fx.INDEX_PAGE, locale).lstrip("/") / "index.html").read_text(encoding="utf-8")
    chunks = html.split('<li class="experience-row')[1:]
    # cada fila termina en su enlace a la ficha (el último trozo seguiría hasta el pie)
    rows = [c[:c.index("</a></p>", c.index("experience-row__action"))] for c in chunks]
    assert len(rows) == 7
    entries = [e for g in next(s for s in data.bundle.get_page(fx.INDEX_PAGE).sections if s.kind == "experience_index").groups
               for e in g.entries]
    for entry, row in zip(entries, rows):
        has_media = entry.experience_ref in composition.experiences
        assert ("<img" in row) == has_media and ("experience-row__media" in row) == has_media
        if has_media:  # DOM: imagen → título → profesional y rol → resumen → magnitudes → enlace
            order = [row.index(k) for k in ("<img", "<h4", "experience-row__attribution", "experience-row__summary",
                                            "experience-row__action")]
            assert order == sorted(order)
    text_rows = re.findall(r'<li class="experience-row experience-row--text">', html)
    assert len(text_rows) == 7 - len(composition.experiences)


def test_missing_key_figures_leave_no_empty_block(inputs):
    data = inputs["es"]
    target = next(e for e in data.bundle.experiences if e.key_figures)
    doc = _index(fx.with_index(data, replace={target.id: target.model_copy(update={"key_figures": []})}))
    figures_lists = doc.all("ul", "experience-figures")
    expected = sum(1 for e in data.bundle.experiences if e.key_figures and e.id != target.id)
    assert len(figures_lists) == expected


# ---------- Fichas: contenido ampliado ----------

@pytest.mark.parametrize("locale", LOCALES)
def test_fichas_represent_extended_content_without_empty_or_duplicated_blocks(inputs, locale):
    data = inputs[locale]
    messages = _messages(data)
    for base in data.bundle.experiences:
        extended = fx.extended_experience(base, locale=locale)
        html = render_experience(PATHS, locale, base.id, "preview",
                                 inputs=fx.with_index(data, replace={base.id: extended})).html
        doc = Doc(html)
        for field in ("systems", "phases", "deliverables", "key_figures"):
            for item in getattr(extended, field):
                assert doc.text.count(" ".join(item.text.split())) >= 1
        for item in extended.systems:  # sin duplicados: cada elemento de módulo aparece una vez
            assert doc.texts.count(" ".join(item.text.split())) == 1
        assert len(doc.all("a", "link--external")) == len(extended.links)
        assert len(re.findall(r"<h2[^>]*>\s*</h2>", html)) == 0
        assert len(doc.all("h1")) == 1
        for key in ("experience-systems", "experience-phases", "experience-intervention", "experience-deliverables",
                    "experience-results", "experience-links"):
            assert doc.texts.count(messages[key]) == 1


def test_fichas_omit_absent_modules(inputs):
    data = inputs["es"]
    messages = _messages(data)
    base = data.bundle.experiences[0]
    bare = base.model_copy(update={"context": [], "systems": [], "phases": [], "intervention": [], "deliverables": [],
                                   "results": [], "links": [], "key_figures": []})
    doc = Doc(render_experience(PATHS, "es", base.id, "preview", inputs=fx.with_index(data, replace={base.id: bare})).html)
    for key in ("experience-context", "experience-systems", "experience-phases", "experience-intervention",
                "experience-deliverables", "experience-results", "experience-links", "experience-figures"):
        assert messages[key] not in doc.texts


# ---------- Créditos de imagen y Automatización ----------

def test_credits_are_compact_localized_and_keep_alt_text(site, inputs):
    manifest = load_media_manifest(PATHS)
    management = [a.attribution_text for a in manifest.assets if a.attribution_text]
    for locale, data in inputs.items():
        adapted = _messages(data)["image-adapted"]
        for pid in data.routing.routes.pages:
            html = (site / data.routing.url(pid, locale).lstrip("/") / "index.html").read_text(encoding="utf-8")
            doc = Doc(html)
            assert not any(text in html for text in management)  # el registro de gestión no se publica
            assert "Recortada y convertida" not in html and "Obra derivada" not in html
            for caption in doc.by_class.get("credit", []):
                assert len(caption) < 120
            if doc.by_class.get("credit"):
                assert any(adapted in c for c in doc.by_class["credit"])
            for img in doc.all("img"):
                assert img.get("alt")


def test_credits_keep_every_mandatory_attribution(site, inputs):
    data = inputs["es"]
    manifest = load_media_manifest(PATHS)
    composition = load_site_composition(PATHS)
    for pid, config in composition.pages.items():
        if not config.media:
            continue
        html = (site / data.routing.url(pid, "es").lstrip("/") / "index.html").read_text(encoding="utf-8")
        for asset_id in config.media.values():
            asset = manifest.get(asset_id)
            if asset.attribution_required:
                assert asset.author in html and asset.license_url in html, f"{pid}/{asset_id}"


@pytest.mark.parametrize("locale", LOCALES)
def test_automation_page_uses_d03_instead_of_d02(site, inputs, locale):
    data = inputs[locale]
    manifest = load_media_manifest(PATHS)
    doc = Doc((site / data.routing.url("automatizacion_control", locale).lstrip("/") / "index.html").read_text(encoding="utf-8"))
    srcs = {img["src"]: img["alt"] for img in doc.all("img") if img.get("class") not in LOGOS}
    d02, d03 = manifest.get("D02"), manifest.get("D03")
    assert "/" + d02.relative_path not in srcs
    assert srcs["/" + d03.relative_path] == getattr(d03, f"alt_{locale}")
