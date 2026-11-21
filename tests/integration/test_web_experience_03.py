"""WEB-EXPERIENCE-03 V2: vertical Proyectos y experiencia, fichas estándar y generación multilingüe.

Las expectativas salen de los datos (CONTENT, SITE, composición), no de identificadores escritos en el código.
"""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
from pathlib import Path

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.site_integrity import validate_site_tree
from bafras_web.application import build
from bafras_web.application.build import BuildError, BuildRequest, build_site, render_experience, render_page
from bafras_web.application.configuration import load_site_composition, load_site_routing
from bafras_web.editorial.entities import Experience
from bafras_web.editorial.sections import ExperienceEntry
from bafras_web.site.composition import SiteComposition

PATHS = ProjectPaths(Path(__file__).resolve().parents[2])
LOCALES = ("es", "ca", "en", "de")
LOGOS = {"brand__logo", "site-footer__logo"}


class Doc(HTMLParser):
    """Árbol mínimo: etiquetas con atributos, texto visible y texto por clase CSS de su contenedor."""

    def __init__(self, source: str) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.texts: list[str] = []
        self.stack: list[str] = []
        self.by_class: dict[str, list[str]] = {}
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        data = {k: v or "" for k, v in attrs}
        self.tags.append((tag, data))
        if tag not in ("img", "br", "meta", "link", "input"):
            self.stack.append(data.get("class", ""))

    def handle_endtag(self, tag):
        if tag not in ("img", "br", "meta", "link", "input") and self.stack:
            self.stack.pop()

    def handle_data(self, data):
        text = " ".join(data.split())
        if text:
            self.texts.append(text)
            for classes in self.stack:
                for name in classes.split():
                    self.by_class.setdefault(name, []).append(text)

    def all(self, tag, cls=None):
        return [a for t, a in self.tags if t == tag and (cls is None or cls in a.get("class", "").split())]

    @property
    def text(self) -> str:
        return " ".join(self.texts)


def snapshot(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    """Los cuatro idiomas generados por separado en la misma salida, en orden es → ca → en → de."""
    out = tmp_path_factory.mktemp("we03")
    targets = {locale: build_site(PATHS, locale, "preview", out) for locale in LOCALES}
    inputs = {locale: build._load_inputs(PATHS, locale) for locale in LOCALES}
    return out / "preview", targets, inputs


def _page(root: Path, url: str) -> Doc:
    return Doc((root / url.lstrip("/") / "index.html").read_text(encoding="utf-8"))


# ---------- A. Multilingüe, rutas y conservación ----------

def test_four_locales_coexist_and_validate_without_missing_destinations(site):
    root, targets, inputs = site
    assert {locale: len(found) for locale, found in targets.items()} == {locale: 16 for locale in LOCALES}
    assert all(target.is_file() for found in targets.values() for target in found)  # es sigue tras generar de
    assert len(list(root.rglob("*.html"))) == 64
    validate_site_tree(root)  # árbol completo: ningún destino ausente admitido


def test_routes_are_localized_unique_and_derived_from_identities(site):
    _, _, inputs = site
    urls = []
    for locale, data in inputs.items():
        routing = data.routing
        for page_id in routing.routes.pages:
            url = routing.url(page_id, locale)
            assert url and (locale == "es" or url.startswith(f"/{locale}/"))
            urls.append(url)
        for experience_id in build.entity_ids(data):
            url = routing.entity_url("experience", experience_id, locale)
            assert url == routing.url("proyectos_experiencia", locale) + experience_id + "/"
            urls.append(url)
    assert len(urls) == len(set(urls)) == 64


def test_full_four_locale_build_is_reproducible_and_regenerating_one_locale_keeps_the_others(site, tmp_path):
    root, *_ = site
    for locale in LOCALES:
        build_site(PATHS, locale, "preview", tmp_path)
    first = snapshot(tmp_path / "preview")
    # HTML + recursos, inventariados archivo a archivo (25 recursos: + D03, WEB-EXPERIENCE-04 §11)
    assert first == snapshot(root) and len(first) == 64 + 25
    build_site(PATHS, "de", "preview", tmp_path)  # regenerar un idioma no altera ni elimina los demás
    assert snapshot(tmp_path / "preview") == first


def test_pe04_capabilities_link_resolves_in_every_locale(site):
    root, _, inputs = site
    for locale, data in inputs.items():
        doc = _page(root, data.routing.url("proyectos_experiencia", locale))
        hrefs = [a["href"] for a in doc.all("a", "btn")]
        assert data.routing.url("capacidades", locale) in hrefs and data.routing.url("contacto", locale) in hrefs


def test_release_stays_blocked_and_publication_unchanged():
    routing = load_site_routing(PATHS)
    assert routing.locales.published_codes == ["es"] and routing.url("inicio", "ca") is None
    assert routing.entity_url("experience", "montesion", "ca") is None
    with pytest.raises(BuildError) as info:
        render_experience(PATHS, "es", "montesion", "release")
    assert any("release aún no implementado" in p for p in info.value.problems)
    assert any("'draft'" in p for p in info.value.problems)


# ---------- C. Índice ----------

@pytest.mark.parametrize("locale", LOCALES)
def test_index_rows_follow_editorial_order_and_link_to_fichas(site, locale):
    """WEB-EXPERIENCE-04 V3 sustituye el mosaico por filas uniformes: una fila por entrada, sin variantes de tamaño."""
    root, _, inputs = site
    data = inputs[locale]
    page = data.bundle.get_page("proyectos_experiencia")
    index = next(s for s in page.sections if s.kind == "experience_index")
    doc = _page(root, data.routing.url("proyectos_experiencia", locale))
    rows = doc.all("li", "experience-row")
    entries = [entry for group in index.groups for entry in group.entries]
    assert len(rows) == len(entries) == 7 and len(doc.all("section", "experience-group")) == len(index.groups) == 3
    assert not doc.all("li", "experience-card") and not any("--featured" in r["class"] for r in rows)
    links = [a["href"] for a in doc.all("a") if a.get("aria-describedby", "").endswith("-title") and "link" in a.get("class", "")]
    assert links == [data.routing.entity_url("experience", e.experience_ref, locale) for e in entries]
    anchors = [a["href"] for a in doc.all("a") if a["href"].startswith(f"#{index.id}-") and a["href"] != f"#{index.id}-portfolio"]
    assert anchors == [f"#{index.id}-{g.id}" for g in index.groups]
    attributions = doc.by_class["experience-row__attribution"]
    for entry, shown in zip(entries, attributions):
        experience = data.bundle.get_experience(entry.experience_ref)
        assert shown == f"{experience.attribution} · {experience.role}"
        assert experience.review.status == "draft"
    shown_figures = doc.by_class.get("experience-figures", [])
    expected_figures = [f.text for e in entries for f in data.bundle.get_experience(e.experience_ref).key_figures[:3]]
    assert shown_figures == expected_figures


def test_rows_show_summary_but_not_technical_modules(site):
    root, _, inputs = site
    data = inputs["es"]
    doc = _page(root, data.routing.url("proyectos_experiencia", "es"))
    rows = doc.by_class["experience-row"]  # textos dentro de las filas
    for experience in data.bundle.experiences:
        assert experience.summary[0].text in doc.by_class["experience-row__summary"]
        for item in (*experience.phases, *experience.systems, *experience.context, *experience.intervention):
            assert " ".join(item.text.split()) not in rows, f"{experience.id}: módulo de ficha volcado en la fila"
        assert experience.kind not in doc.text  # valores internos no se muestran como etiqueta
    assert not {"featured", "complementary"} & set(" ".join(rows).split())


def test_card_images_come_from_composition_main_asset(site):
    root, _, inputs = site
    data = inputs["es"]
    composition = load_site_composition(PATHS)
    doc = _page(root, data.routing.url("proyectos_experiencia", "es"))
    shown = [img["src"] for img in doc.all("img") if img.get("class") not in LOGOS]
    expected = ["/" + data.manifest.get(composition.experiences[e.id].main).relative_path
                for e in data.bundle.experiences if e.id in composition.experiences]
    assert shown == expected and len(shown) == 6
    assert all((root / src.lstrip("/")).is_file() for src in shown)


# ---------- D. Fichas ----------

MODULES = (("systems", "experience-systems"), ("phases", "experience-phases"), ("intervention", "experience-intervention"),
           ("deliverables", "experience-deliverables"), ("results", "experience-results"))


@pytest.mark.parametrize("locale", LOCALES)
def test_each_ficha_renders_only_modules_with_content(site, locale):
    root, _, inputs = site
    data = inputs[locale]
    messages = {m.id: m.text for m in data.bundle.common.interface_messages}
    composition = load_site_composition(PATHS)
    index_url = data.routing.url("proyectos_experiencia", locale)
    for experience in data.bundle.experiences:
        doc = _page(root, data.routing.entity_url("experience", experience.id, locale))
        headings = [t for t in doc.texts if t in messages.values()]
        assert doc.all("h1") and experience.title in doc.texts
        for field, message in MODULES:
            assert (messages[message] in headings) == bool(getattr(experience, field)), f"{locale}/{experience.id}/{field}"
            for item in getattr(experience, field):
                assert " ".join(item.text.split()) in doc.text
        assert (messages["experience-context"] in headings) == bool(experience.context)
        assert (messages["experience-links"] in headings) == bool(experience.links)
        for link in experience.links:
            assert str(link.target.url) in [a["href"] for a in doc.all("a", "link--external")]
        assert f"{experience.attribution} · {experience.role}" in doc.text
        returns = [a["href"] for a in doc.all("a", "return")]
        assert returns == [index_url]
        media = composition.experiences.get(experience.id)
        images = [img["src"] for img in doc.all("img") if img.get("class") not in LOGOS]
        expected = ["/" + data.manifest.get(asset).relative_path for asset in media.assets] if media else []
        assert images == expected
        assert (messages["experience-gallery"] in headings) == bool(media and media.gallery)


def test_translated_pages_do_not_fall_back_to_spanish(site):
    root, _, inputs = site
    spanish = inputs["es"].bundle
    for locale in ("ca", "en", "de"):
        data = inputs[locale]
        for experience, es_experience in zip(data.bundle.experiences, spanish.experiences):
            doc = _page(root, data.routing.entity_url("experience", experience.id, locale))
            assert doc.all("html")[0]["lang"] == locale
            assert experience.summary[0].text in doc.text and es_experience.summary[0].text not in doc.text
            alts = [img["alt"] for img in doc.all("img") if img.get("class") not in LOGOS]
            assert all(getattr(data.manifest.get(a), f"alt_{locale}") in alts for a in
                       (load_site_composition(PATHS).experiences[experience.id].assets
                        if experience.id in load_site_composition(PATHS).experiences else ()))


# ---------- Extensibilidad (sin contenido público ficticio) ----------

def test_new_experience_needs_no_code_only_data():
    """Una experiencia nueva (p. ej. un futuro proyecto BAFRAS) obtiene ruta, tarjeta y ficha solo con datos."""
    inputs = build._load_inputs(PATHS, "es")
    new = Experience.model_validate({
        "id": "prueba-extension", "kind": "bafras_project", "title": "Prueba de extensión", "attribution": "Equipo",
        "role": "Rol de prueba", "summary": [{"id": "summary", "text": "Resumen de prueba."}],
        "review": {"status": "draft"},
    })
    page = inputs.bundle.get_page("proyectos_experiencia")
    index = next(s for s in page.sections if s.kind == "experience_index")
    group = index.groups[0].model_copy(update={"entries": [*index.groups[0].entries,
                                                         ExperienceEntry(id=new.id, experience_ref=new.id, emphasis="complementary")]})
    index = index.model_copy(update={"groups": [group, *index.groups[1:]]})
    page = page.model_copy(update={"sections": [index if s.id == index.id else s for s in page.sections]})
    bundle = inputs.bundle.model_copy(update={
        "experiences": [*inputs.bundle.experiences, new],
        "pages": [page if p.page_id == page.page_id else p for p in inputs.bundle.pages]})
    extended = build.BuildInputs(inputs.routing, bundle, inputs.manifest, inputs.composition, inputs.contact)
    assert new.id in build.entity_ids(extended)
    index_html = render_page(PATHS, BuildRequest("es", "proyectos_experiencia", "preview"), inputs=extended).html
    assert "/proyectos-experiencia/prueba-extension/" in index_html and "Prueba de extensión" in index_html
    ficha = Doc(render_experience(PATHS, "es", new.id, "preview", inputs=extended).html)
    assert "Prueba de extensión" in ficha.texts and "Equipo · Rol de prueba" in ficha.text
    assert not [img for img in ficha.all("img") if img.get("class") not in LOGOS]  # sin imagen: tipográfica


def test_composition_rejects_unknown_experiences_and_repeated_images():
    inputs = build._load_inputs(PATHS, "es")
    data = {"schema_version": 1, "experiences": {"no-existe": {"main": "X01"}, "montesion": {"main": "X05", "gallery": ["X05"]}}}
    problems = build.composition_problems(SiteComposition.model_validate(data), inputs.bundle)
    assert any("experiencia desconocida 'no-existe'" in p for p in problems)
    assert any("montesion: imagen repetida" in p for p in problems)
