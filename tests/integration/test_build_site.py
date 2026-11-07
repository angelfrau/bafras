"""WEB-V02: cadena real completa, contratos de salida y fallos antes/durante promoción."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
from pathlib import Path

import pytest
from pydantic import BaseModel

from bafras_web.adapters.filesystem import ProjectPaths, staged_directory
from bafras_web.adapters.site_integrity import HtmlDocument, SiteIntegrityError, validate_site_tree
from bafras_web.application import build, presentation
from bafras_web.adapters import build_output
from bafras_web.application.build import BuildError, BuildRequest, build_page, build_site
from bafras_web.application.configuration import load_site_routing, load_media_manifest, load_site_composition
from bafras_web.cli import main
from bafras_web.media.assets import MediaAsset, media_publication_blockers

PATHS = ProjectPaths(Path(__file__).resolve().parents[2])


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    out = tmp_path_factory.mktemp("full-site")
    targets = build_site(PATHS, "es", "preview", out)
    return out, targets, build._load_inputs(PATHS, "es")


class VisibleText(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.feed(source)

    def handle_data(self, data):
        self.parts.append(data)


def visible_strings(value, key=None):
    if isinstance(value, BaseModel):
        for name in type(value).model_fields:
            yield from visible_strings(getattr(value, name), name)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from visible_strings(item, key)
    elif isinstance(value, str) and key in {
        "title", "text", "label", "eyebrow", "subtitle", "attribution", "value", "help",
        "public_name", "qualification", "specialty", "submit_label", "privacy_text",
    }:
        yield value


def test_full_site_matches_routing_and_assets(site):
    out, targets, inputs = site
    root = out / "preview"
    assert len(targets) == len(list(root.rglob("*.html"))) == 9
    assert targets[0] == root / "index.html"
    assert {p.relative_to(root).as_posix() for p in targets} == {
        (url.lstrip("/") + "index.html") for pid in inputs.routing.routes.pages
        if (url := inputs.routing.url(pid, "es")) is not None
    }
    assert len([p for p in (root / "assets").rglob("*") if p.is_file()]) == 11
    validate_site_tree(root)
    assert not (out / "dist").exists()


def test_real_content_order_and_all_visible_fields_including_entities(site):
    _, targets, inputs = site
    for target, page_id in zip(targets, inputs.routing.routes.pages):
        page = inputs.bundle.get_page(page_id)
        source = target.read_text(encoding="utf-8")
        doc = HtmlDocument(source)
        assert doc.h1_count == 1
        assert all(source.index(f'<section id="{a.id}"') < source.index(f'<section id="{b.id}"')
                   for a, b in zip(page.sections, page.sections[1:]))
        assert 'content="noindex, nofollow"' in source and 'rel="canonical"' not in source and 'hreflang=' not in source
        texts = " ".join(" ".join(VisibleText(source).parts).split())
        expected = list(visible_strings(page.sections))
        for section in page.sections:
            if section.kind == "sector_index":
                for ref in section.sector_refs:
                    expected.extend(visible_strings(inputs.bundle.get_sector(ref)))
            if section.kind == "team":
                for ref in section.person_refs:
                    expected.extend(visible_strings(inputs.bundle.get_person(ref)))
        assert not [s for s in expected if " ".join(s.split()) not in texts], page_id


def test_contact_has_real_channels_and_no_active_submission(site):
    source = next(p for p in site[1] if p.parent.name == "contacto").read_text(encoding="utf-8")
    assert "Formulario no disponible" not in source
    assert all(tag not in source for tag in ("<form", "<fieldset", "<input", "<textarea", "<button disabled"))
    assert "Enviar consulta." not in source
    assert 'href="mailto:info@bafras.com"' in source and 'href="tel:+34610903179"' in source
    assert "Tu consulta se ha enviado correctamente" not in source


def test_full_build_is_deterministic_and_loads_bundle_once(site, tmp_path, monkeypatch):
    original = build.inspect_editorial
    calls = []
    def counted(*args, **kwargs):
        calls.append(1)
        return original(*args, **kwargs)
    monkeypatch.setattr(build, "inspect_editorial", counted)
    build_site(PATHS, "es", "preview", tmp_path)
    assert len(calls) == 1
    assert snapshot(site[0] / "preview") == snapshot(tmp_path / "preview")


@pytest.mark.parametrize("failure", ["render", "copy", "write", "integrity", "promotion"])
def test_failed_build_preserves_every_previous_file(site, tmp_path, monkeypatch, failure):
    build_site(PATHS, "es", "preview", tmp_path)
    root = tmp_path / "preview"
    before = snapshot(root)
    def broken(*args, **kwargs):
        raise OSError("fallo inyectado")
    if failure in {"render", "copy", "write"}:
        monkeypatch.setattr(build if failure == "render" else build_output, {"render": "render_html", "copy": "copy_file_atomically", "write": "write_text_atomically"}[failure], broken)
    elif failure == "integrity":
        original = build.render_html
        monkeypatch.setattr(build, "render_html", lambda *a, **kw: original(*a, **kw) + '<a href="/ausente/">Fallo</a>')
    else:
        original = Path.rename
        def fail_promotion(self, target):
            if self.name.startswith(".preview-stage-"):
                raise OSError("fallo de promoción")
            return original(self, target)
        monkeypatch.setattr(Path, "rename", fail_promotion)
    with pytest.raises(BuildError):
        build_site(PATHS, "es", "preview", tmp_path)
    assert snapshot(root) == before
    assert sorted(p.name for p in tmp_path.iterdir()) == ["preview"]


def test_success_removes_obsolete_files(tmp_path):
    root = tmp_path / "preview"
    root.mkdir()
    (root / "obsolete.webp").write_bytes(b"old")
    build_site(PATHS, "es", "preview", tmp_path)
    assert not (root / "obsolete.webp").exists()


def test_rollback_failure_preserves_backup(tmp_path, monkeypatch):
    root = tmp_path / "preview"
    root.mkdir()
    (root / "old.txt").write_text("previous")
    original = Path.rename
    def failed(self, target):
        if self.name.startswith((".preview-stage-", ".preview-previous-")):
            raise OSError("rename failed")
        return original(self, target)
    monkeypatch.setattr(Path, "rename", failed)
    with pytest.raises(OSError, match="conservada"):
        with staged_directory(root) as staging:
            (staging / "new.txt").write_text("new")
    backups = list(tmp_path.glob(".preview-previous-*"))
    assert len(backups) == 1 and (backups[0] / "old.txt").read_text() == "previous"
    assert not list(tmp_path.glob(".preview-stage-*"))


@pytest.mark.parametrize("href", ["/absent/", "#absent", "/#absent", "/assets/absent.webp"])
def test_tree_rejects_missing_destinations_and_fragments(tmp_path, href):
    (tmp_path / "index.html").write_text(f'<h1>Page</h1><a href="{href}">Link</a>', encoding="utf-8")
    with pytest.raises(SiteIntegrityError):
        validate_site_tree(tmp_path)


def test_tree_distinguishes_remote_and_contact_links(tmp_path):
    (tmp_path / "index.html").write_text('<h1>Page</h1><a href="https://example.org/">External</a><a href="mailto:x@y.org">Mail</a><a href="tel:+34123456789">Phone</a>', encoding="utf-8")
    validate_site_tree(tmp_path)


@pytest.mark.parametrize("href", ["ftp://example.org/file", "javascript://example.org/"])
def test_tree_rejects_unapproved_schemes_even_with_host(tmp_path, href):
    (tmp_path / "index.html").write_text(f'<h1>Page</h1><a href="{href}">Link</a>', encoding="utf-8")
    with pytest.raises(SiteIntegrityError, match="esquema no admitido"):
        validate_site_tree(tmp_path)


def test_render_does_not_mix_locales_when_reusing_inputs(site):
    with pytest.raises(BuildError, match="incompatible con locale"):
        build.render_page(PATHS, BuildRequest("ca", "inicio", "preview"), inputs=site[2])


def test_unknown_component_is_contextual_and_never_silently_omitted(monkeypatch):
    monkeypatch.setattr(presentation, "SECTION_COMPONENTS", {k: v for k, v in presentation.SECTION_COMPONENTS.items() if k != ("cards", "technical_areas")})
    with pytest.raises(BuildError, match="página infraestructuras, sección ambitos.*sin componente"):
        build.render_page(PATHS, BuildRequest("es", "infraestructuras", "preview"))


def test_dec10_scope_and_original_licenses():
    manifest, composition = load_media_manifest(PATHS), load_site_composition(PATHS)
    selected = {asset for config in composition.pages.values() for asset in config.media.values()}
    assert len(selected) == 9
    for asset in manifest.assets:
        assert bool(media_publication_blockers(asset)) == (asset.id not in selected)
        if asset.id in selected:
            assert asset.license and asset.author and asset.authorization_ref and asset.output_sha256
    fresh = MediaAsset(id="Z99", status="READY", relative_path="assets/images/new.webp")
    assert media_publication_blockers(fresh)


def test_cli_all_selection_and_release_preserve_output(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(build.ProjectPaths, "build", property(lambda self: tmp_path))
    assert main(["build", "--locale", "es", "--all", "--mode", "preview", "--project", str(PATHS.root)]) == 0
    assert len(capsys.readouterr().out.strip().splitlines()) == 9
    before = snapshot(tmp_path)
    assert main(["build", "--locale", "es", "--all", "--mode", "release", "--project", str(PATHS.root)]) == 1
    assert snapshot(tmp_path) == before
    with pytest.raises(SystemExit) as error:
        main(["build", "--locale", "es", "--all", "--page", "inicio", "--mode", "preview"])
    assert error.value.code == 2


def test_single_page_preserves_legacy_path_and_adds_site_route(tmp_path):
    target = build_page(PATHS, BuildRequest("es", "inicio", "preview"), tmp_path)
    assert target == (tmp_path / "preview/es/inicio/index.html").resolve()
    assert target.read_bytes() == (tmp_path / "preview/index.html").read_bytes()
