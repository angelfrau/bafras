from __future__ import annotations

from pathlib import Path

import pytest

import bafras_web
from bafras_web.adapters.filesystem import ProjectPaths, find_project_root
from bafras_web.cli import main

REPO_ROOT = Path(__file__).resolve().parents[2]


LOCALES_YAML = """
schema_version: 1
default_locale: es
locales:
  - {code: es, name: Español, published: true}
"""
ROUTES_YAML = """
schema_version: 1
pages:
  inicio: {slugs: {es: ""}}
  contacto: {slugs: {es: contacto}}
"""


def _make_project(root: Path) -> None:
    (root / "pyproject.toml").write_text("", encoding="utf-8")
    for entry in ("config", "content", "assets/images", "media-library/manifests", "docs/project_v02"):
        (root / entry).mkdir(parents=True)
    (root / "media-library/manifests/media-manifest.yaml").write_text("", encoding="utf-8")
    (root / "config/locales.yaml").write_text(LOCALES_YAML, encoding="utf-8")
    (root / "config/routes.yaml").write_text(ROUTES_YAML, encoding="utf-8")


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out.strip() == f"bafras-web {bafras_web.__version__}"


def test_without_command_prints_help_and_fails(capsys):
    assert main([]) == 2
    assert "doctor" in capsys.readouterr().out


def test_doctor_on_repository_succeeds(capsys):
    assert main(["doctor", "--project", str(REPO_ROOT)]) == 0
    out = capsys.readouterr().out
    assert "Resultado: correcto" in out
    assert "[falta]" not in out


def test_doctor_finds_root_from_subdirectory(tmp_path, capsys):
    _make_project(tmp_path)
    assert main(["doctor", "--project", str(tmp_path / "content")]) == 0
    assert f"Proyecto: {tmp_path}" in capsys.readouterr().out


def test_doctor_reports_missing_entries(tmp_path, capsys):
    _make_project(tmp_path)
    (tmp_path / "media-library/manifests/media-manifest.yaml").unlink()
    assert main(["doctor", "--project", str(tmp_path)]) == 1
    out = capsys.readouterr().out
    assert "[falta] media-library/manifests/media-manifest.yaml" in out
    assert "Resultado: 1 problema(s)" in out


def test_doctor_outside_a_project_fails(tmp_path, capsys):
    assert main(["doctor", "--project", str(tmp_path)]) == 1
    assert "no se encuentra una raíz" in capsys.readouterr().out


def test_find_project_root_requires_all_markers(tmp_path):
    (tmp_path / "pyproject.toml").write_text("", encoding="utf-8")
    (tmp_path / "config").mkdir()
    assert find_project_root(tmp_path) is None
    (tmp_path / "content").mkdir()
    assert find_project_root(tmp_path) == tmp_path


def test_project_paths_are_relative_to_root(tmp_path):
    paths = ProjectPaths(tmp_path)
    assert paths.dist == tmp_path / "dist"
    assert paths.media_manifest == tmp_path / "media-library" / "manifests" / "media-manifest.yaml"
    assert paths.routes_file == tmp_path / "config" / "routes.yaml"
    assert [label for label, _ in paths.required_entries()] == [
        "config/locales.yaml",
        "config/routes.yaml",
        "content/",
        "assets/images/",
        "media-library/manifests/media-manifest.yaml",
        "docs/project_v02/",
    ]


def test_doctor_reports_configuration(tmp_path, capsys):
    _make_project(tmp_path)
    assert main(["doctor", "--project", str(tmp_path)]) == 0
    assert "[ok] configuración: 1 idiomas (publicados: es), 2 páginas" in capsys.readouterr().out


def test_doctor_reports_invalid_configuration(tmp_path, capsys):
    _make_project(tmp_path)
    (tmp_path / "config/routes.yaml").write_text(ROUTES_YAML.replace("contacto}", "''}"), encoding="utf-8")
    assert main(["doctor", "--project", str(tmp_path)]) == 1
    out = capsys.readouterr().out
    assert "[error] config/routes.yaml" in out
    assert "más de una página raíz con slug vacío: contacto, inicio" in out
