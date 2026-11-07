"""Atomic writing, publication policy, component coverage and the `build` CLI."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest

from bafras_web.adapters import filesystem
from bafras_web.adapters.filesystem import ProjectPaths, write_text_atomically
from bafras_web.adapters.jinja import template_environment
from bafras_web.application.build import SUPPORTED_SECTIONS, SECTION_COMPONENTS
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.cli import main
from bafras_web.editorial.integrity import build_editorial_bundle
from bafras_web.site.publication import RELEASE_NOT_AVAILABLE, publication_blockers

ROOT = Path(__file__).resolve().parents[2]
PATHS = ProjectPaths(ROOT)


def test_atomic_write_creates_directories_and_uses_utf8_lf(tmp_path):
    target = tmp_path / "a" / "b" / "index.html"
    write_text_atomically(target, "Àngel\nfür\n")
    assert target.read_bytes() == "Àngel\nfür\n".encode("utf-8")
    assert [p.name for p in target.parent.iterdir()] == ["index.html"]


def test_atomic_write_failure_keeps_previous_file_and_cleans_temporary(tmp_path, monkeypatch):
    target = tmp_path / "index.html"
    write_text_atomically(target, "anterior")

    def failing_replace(src, dst):
        raise OSError("disco lleno")

    monkeypatch.setattr(filesystem.os, "replace", failing_replace)
    with pytest.raises(OSError):
        write_text_atomically(target, "nuevo")
    assert target.read_text(encoding="utf-8") == "anterior"
    assert [p.name for p in tmp_path.iterdir()] == ["index.html"]


def _inicio(locale="es"):
    return build_editorial_bundle(inspect_editorial(PATHS, EditorialLoadRequest(locale=locale, policy="COMPLETE"))).get_page("inicio")


def test_preview_admits_drafts_and_release_reports_every_reason():
    page, routing = _inicio(), load_site_routing(PATHS)
    assert page.review.status == "draft"
    assert publication_blockers(page, "es", routing, "preview") == []
    blockers = publication_blockers(page, "es", routing, "release")
    assert blockers[0] == RELEASE_NOT_AVAILABLE
    assert any("'draft'" in b for b in blockers) and any("SEO" in b for b in blockers)
    assert sum(b.startswith("pendiente ") for b in blockers) == len(page.pending)
    assert page.review.status == "draft"


def test_release_for_unpublished_locale_is_blocked():
    blockers = publication_blockers(_inicio("ca"), "ca", load_site_routing(PATHS), "release")
    assert any("no publicado" in b for b in blockers)


def test_every_supported_section_family_has_a_component():
    templates = set(template_environment().list_templates())
    assert {f"components/{name}" for name in SECTION_COMPONENTS.values()} <= templates


def test_inicio_uses_only_supported_section_families():
    assert {(s.kind, getattr(s, "purpose", None)) for s in _inicio().sections} <= SUPPORTED_SECTIONS


@pytest.fixture
def project_copy(tmp_path):
    (tmp_path / "pyproject.toml").write_text("", encoding="utf-8")
    shutil.copytree(ROOT / "config", tmp_path / "config")
    shutil.copytree(ROOT / "content", tmp_path / "content")
    shutil.copytree(ROOT / "assets", tmp_path / "assets")
    (tmp_path / "media-library" / "manifests").mkdir(parents=True)
    shutil.copyfile(ROOT / "media-library/manifests/media-manifest.yaml", tmp_path / "media-library/manifests/media-manifest.yaml")
    return tmp_path


def test_cli_build_preview_writes_and_prints_the_file(project_copy, capsys):
    assert main(["build", "--locale", "es", "--page", "inicio", "--mode", "preview", "--project", str(project_copy)]) == 0
    target = Path(capsys.readouterr().out.strip())
    assert target == (project_copy / "build" / "preview" / "es" / "inicio" / "index.html").resolve()
    assert target.read_text(encoding="utf-8").startswith("<!doctype html>")


def test_cli_build_release_fails_without_output(project_copy, capsys):
    assert main(["build", "--locale", "es", "--page", "inicio", "--mode", "release", "--project", str(project_copy)]) == 1
    err = capsys.readouterr().err
    assert "no generado" in err and RELEASE_NOT_AVAILABLE in err
    assert not (project_copy / "build").exists() and not (project_copy / "dist").exists()


def test_cli_build_rejects_invalid_mode(project_copy):
    with pytest.raises(SystemExit) as info:
        main(["build", "--locale", "es", "--page", "inicio", "--mode", "publish", "--project", str(project_copy)])
    assert info.value.code == 2


def test_cli_build_outside_a_project_fails(tmp_path, capsys):
    assert main(["build", "--locale", "es", "--page", "inicio", "--mode", "preview", "--project", str(tmp_path)]) == 1
    assert "raíz" in capsys.readouterr().err
    assert os.listdir(tmp_path) == []
