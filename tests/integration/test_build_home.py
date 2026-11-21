"""WEB-V01-A E2E: real editorial content → build_page → HTML file, checked with an HTML parser."""

from __future__ import annotations

import html
from html.parser import HTMLParser
from pathlib import Path

import pytest
from pydantic import BaseModel

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application import build as build_module
from bafras_web.application.build import BuildError, BuildRequest, build_page, preview_path
from bafras_web.application.configuration import load_media_manifest, load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import build_editorial_bundle
from bafras_web.site.links import iter_link_targets, resolve_links

ROOT = Path(__file__).resolve().parents[2]
PATHS = ProjectPaths(ROOT)
PREVIEW = BuildRequest(locale="es", page_id="inicio", mode="preview")
VISIBLE_FIELDS = frozenset({"text", "title", "eyebrow", "subtitle", "label", "attribution"})


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.doctype: str | None = None
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.texts: list[str] = []
        self.h1: list[str] = []
        self.anchors: list[tuple[str, dict[str, str]]] = []  # (región: header/main/footer/otro, atributos)
        self._in_h1 = False
        self._region = "otro"

    def handle_decl(self, decl):
        self.doctype = decl

    def handle_starttag(self, tag, attrs):
        attributes = {k: v or "" for k, v in attrs}
        self.tags.append((tag, attributes))
        self._in_h1 = tag == "h1"
        if tag in ("header", "main", "footer"):
            self._region = tag
        elif tag == "a":
            self.anchors.append((self._region, attributes))

    def handle_endtag(self, tag):
        if tag == "h1":
            self._in_h1 = False
        if tag in ("header", "main", "footer"):
            self._region = "otro"

    def hrefs(self, region):
        """Destinos editoriales; los enlaces de crédito de imagen (fuente y licencia, WEB-EXPERIENCE-04) van aparte."""
        return [attrs["href"] for where, attrs in self.anchors
                if where == region and "credit__link" not in attrs.get("class", "").split()]

    def credit_hrefs(self, region):
        return [attrs["href"] for where, attrs in self.anchors
                if where == region and "credit__link" in attrs.get("class", "").split()]

    def handle_data(self, data):
        text = " ".join(data.split())
        if text:
            self.texts.append(text)
            if self._in_h1:
                self.h1.append(text)

    def all(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]


def _visible_strings(value, key=None):
    if isinstance(value, BaseModel):
        for name in type(value).model_fields:
            yield from _visible_strings(getattr(value, name), name)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _visible_strings(item, key)
    elif isinstance(value, str) and key in VISIBLE_FIELDS:
        yield value


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    out = tmp_path_factory.mktemp("build")
    target = build_page(PATHS, PREVIEW, build_root=out)
    bundle = build_editorial_bundle(inspect_editorial(PATHS, EditorialLoadRequest(locale="es", policy="COMPLETE")))
    page = bundle.get_page("inicio")
    parser = DocumentParser()
    parser.feed(target.read_text(encoding="utf-8"))
    return out, target, page, resolve_links(bundle, page, load_site_routing(PATHS)), parser


def test_output_path_and_document(built):
    out, target, _, _, doc = built
    assert target == (out / "preview" / "es" / "inicio" / "index.html").resolve() and target.stat().st_size > 0
    assert doc.doctype == "doctype html"
    assert doc.all("html")[0]["lang"] == "es"
    assert len(doc.all("main")) == 1


def test_preview_signals_without_public_seo(built):
    *_, doc = built
    assert {"name": "robots", "content": "noindex, nofollow"} in doc.all("meta")
    assert any(attrs.get("class") == "preview-notice" for _, attrs in doc.tags)
    assert [link["rel"] for link in doc.all("link")] == ["icon", "stylesheet"]  # favicon de marca (WEB-EXPERIENCE-03)
    assert not any("hreflang" in attrs for _, attrs in doc.tags)


def test_images_come_from_composition_and_manifest(built):
    out, *_, doc = built
    logos = [img for img in doc.all("img") if img.get("class") in {"brand__logo", "site-footer__logo"}]
    images = [img for img in doc.all("img") if img.get("class") not in {"brand__logo", "site-footer__logo"}]
    # Logotipo oficial en cabecera y pie (WEB-EXPERIENCE-03), con la marca de CommonContent como alternativa.
    assert [img["src"] for img in logos] == ["/assets/images/brand/logos/BAFRAS_logo_horizontal_deep.svg"] * 2
    assert all(img["alt"] == "BAFRAS Engineering" and (out / "preview" / img["src"].lstrip("/")).is_file() for img in logos)
    assert len(images) == 5
    for img in images:
        assert img["src"].startswith("/assets/images/") and img["alt"] and img["width"] and img["height"]
        assert (out / "preview" / img["src"].lstrip("/")).is_file()
    assert sum(attrs.get("class") == "credit" for _, attrs in doc.tags) == 2  # H01, H03: figcaption
    assert len([1 for name, attrs in doc.tags if name == "ul" and attrs.get("class") == "credits"]) == 1


def test_static_assets_are_copied_next_to_the_html(built):
    out, *_, doc = built
    for url in [doc.all("link")[0]["href"], doc.all("script")[0]["src"]]:
        assert (out / "preview" / url.lstrip("/")).is_file()


def test_sections_follow_the_editorial_order_with_one_h1(built):
    _, _, page, _, doc = built
    assert [s["id"] for s in doc.all("section")] == [s.id for s in page.sections]
    assert doc.h1 == [page.sections[0].title] and len(doc.all("h1")) == 1
    for section in page.sections:
        if section.kind != "hero":
            assert {"id": f"{section.id}-title"} in doc.all("h2")


def test_every_visible_editorial_text_is_rendered(built):
    _, _, page, _, doc = built
    rendered = "\n".join(doc.texts)
    expected = list(_visible_strings(page))
    assert len(expected) > 40
    missing = [text for text in expected if " ".join(text.split()) not in rendered]
    assert not missing, missing


def test_links_are_the_resolved_destinations_in_order(built):
    _, _, page, links, doc = built
    hrefs = doc.hrefs("main")
    assert hrefs == [links[target] for _, target in iter_link_targets(page)]
    assert all(href.startswith("/") and href.count("#") <= 1 for href in hrefs)
    # Créditos CC (WEB-EXPERIENCE-04): fuente y licencia enlazadas, solo hacia destinos externos registrados en MEDIA.
    credits = doc.credit_hrefs("main")
    assert credits and all(href.startswith("https://") for href in credits)


def test_header_and_footer_use_common_content_routing_and_site_contact(built):
    *_, doc = built
    routing = load_site_routing(PATHS)
    top_level = [routing.url(pid, "es") for pid, r in routing.routes.pages.items() if r.parent is None and pid != "inicio"]
    nav = [url for url in top_level if url != "/contacto/"] + ["/contacto/"]
    assert doc.anchors[0] == ("otro", {"class": "skip-link", "href": "#contenido"})  # primer elemento enfocable
    # Preview: selector con los cuatro idiomas (sin hreflang ni publicación); release solo mostrará los publicados.
    assert doc.hrefs("header") == ["/", *nav, "/", "/ca/", "/en/", "/de/"]
    assert doc.hrefs("footer") == ["mailto:info@bafras.com", "tel:+34610903179", *nav]
    assert {"id": "site-nav", "class": "site-nav", "aria-label": "Navegación principal"} in doc.all("nav")
    toggle = next(attrs for name, attrs in doc.tags if name == "button")
    assert toggle["aria-controls"] == "site-nav" and toggle["aria-expanded"] == "false" and "hidden" in toggle


def test_build_is_deterministic(built, tmp_path):
    _, target, *_ = built
    second = build_page(PATHS, PREVIEW, build_root=tmp_path)
    assert second.read_bytes() == target.read_bytes()


def test_release_is_rejected_without_writing(tmp_path):
    with pytest.raises(BuildError) as info:
        build_page(PATHS, BuildRequest(locale="es", page_id="inicio", mode="release"), build_root=tmp_path)
    assert any("'draft'" in problem for problem in info.value.problems)
    assert not any(tmp_path.iterdir())


def test_failed_render_keeps_previous_output(tmp_path, monkeypatch):
    target = build_page(PATHS, PREVIEW, build_root=tmp_path)
    before = target.read_bytes()

    def broken(*args, **kwargs):
        raise RuntimeError("render roto")

    monkeypatch.setattr(build_module, "render_html", broken)
    with pytest.raises(RuntimeError):
        build_page(PATHS, PREVIEW, build_root=tmp_path)
    assert target.read_bytes() == before
    assert [p.name for p in target.parent.iterdir()] == ["index.html"]


@pytest.mark.parametrize("request_, expected", [
    (BuildRequest(locale="es", page_id="noexiste", mode="preview"), "página no configurada"),
    (BuildRequest(locale="fr", page_id="inicio", mode="preview"), "LOCALE_UNKNOWN"),
])
def test_unbuildable_requests_fail_explicitly(tmp_path, request_, expected):
    with pytest.raises(BuildError) as info:
        build_page(PATHS, request_, build_root=tmp_path)
    assert any(expected in problem for problem in info.value.problems)
    assert not any(tmp_path.iterdir())


@pytest.mark.parametrize("locale, page_id", [("es", "../x"), ("es", "Inicio"), ("../", "inicio"), ("es", "a/b")])
def test_output_path_rejects_uncontrolled_identifiers(tmp_path, locale, page_id):
    with pytest.raises(BuildError):
        preview_path(tmp_path, locale, page_id)


def test_escaped_text_round_trips(built):
    _, target, page, _, _ = built
    source = target.read_text(encoding="utf-8")
    for text in _visible_strings(page):
        if any(ch in text for ch in "<>&\"'"):
            assert html.escape(text, quote=False) in source


def test_translated_preview_uses_its_own_alt_text_and_urls(tmp_path):
    """WEB-EXPERIENCE-03: ca se genera en preview con alt y URL propios; nunca toma el texto español."""
    target = build_page(PATHS, BuildRequest(locale="ca", page_id="inicio", mode="preview"), build_root=tmp_path)
    doc = DocumentParser()
    doc.feed(target.read_text(encoding="utf-8"))
    assert doc.all("html")[0]["lang"] == "ca"
    manifest = load_media_manifest(PATHS)
    content = [img for img in doc.all("img") if img.get("class") not in {"brand__logo", "site-footer__logo"}]
    assert content and all(img["alt"] in {a.alt_ca for a in manifest.assets} for img in content)
    assert not {img["alt"] for img in content} & {a.alt_es for a in manifest.assets}
    internal = [href for href in doc.hrefs("main") + doc.hrefs("header") if href.startswith("/") and not href.startswith("/assets/")]
    assert internal and all(href.startswith("/ca/") or href in ("/", "/en/", "/de/") for href in internal)


def test_missing_alt_text_for_a_locale_still_blocks_the_build(tmp_path, monkeypatch):
    """Sin texto alternativo en el idioma pedido no hay fallback: el build falla de forma explícita."""
    from bafras_web.media import assets as media_assets

    original = media_assets.resolve_image

    def without_catalan(asset, locale):
        return original(asset.model_copy(update={"alt_ca": None}), locale)

    monkeypatch.setattr(build_module, "resolve_image", without_catalan)
    with pytest.raises(BuildError) as info:
        build_page(PATHS, BuildRequest(locale="ca", page_id="inicio", mode="preview"), build_root=tmp_path)
    assert any("sin texto alternativo para 'ca'" in problem for problem in info.value.problems)
    assert not any(tmp_path.iterdir())
