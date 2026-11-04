"""Integridad del repositorio V2: legacy retirado, documentación y recursos preservados."""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECT_DOCS = REPO_ROOT / "docs" / "project_v02"

LEGACY_PATHS = ("index.html", "css", "js", "tools", "tests/test_structure.py", "docs/visual-system-v1.md")


@pytest.mark.parametrize("relative", LEGACY_PATHS)
def test_legacy_code_is_retired(relative):
    assert not (REPO_ROOT / relative).exists()


def test_approved_documents_are_present():
    for pattern in (
        "02_posicionamiento.md",
        "03_contenido_editorial_V1_22_*.md",
        "04_arquitectura_software_V2_4_*.md",
        "05_sistema_visual_V4_12_*.md",
        "02_Acta_Propuesta_Cierre_G1.md",
    ):
        assert list(PROJECT_DOCS.glob(pattern)), pattern


def test_nine_approved_mockups_are_present():
    assert len(list((PROJECT_DOCS / "maquetas_aprobadas").glob("C04_*.zip"))) == 9


def test_project_package_manifest_hashes():
    manifest = (PROJECT_DOCS / "99_Manifest_SHA256.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \|$", manifest, flags=re.M)
    assert rows
    mismatches = [
        name for name, digest in rows
        if hashlib.sha256((PROJECT_DOCS / name).read_bytes()).hexdigest() != digest
    ]
    assert not mismatches, mismatches


def test_publishable_media_paths_exist():
    manifest = yaml.safe_load((REPO_ROOT / "media-library/manifests/media-manifest.yaml").read_text(encoding="utf-8"))
    ready = [asset for asset in manifest["assets"] if asset.get("status") == "READY"]
    assert ready
    missing = [a["relative_path"] for a in ready if not (REPO_ROOT / a["relative_path"]).is_file()]
    assert not missing, missing


def test_provenance_records_are_preserved():
    sources = list((REPO_ROOT / "media-library" / "originals").glob("*/source.json"))
    assert len(sources) == 26
    assert (REPO_ROOT / "media-library/manifests/attribution.md").is_file()


def test_publishable_assets_contain_no_originals():
    assert not list((REPO_ROOT / "assets").rglob("*_original.*"))


def test_domain_configuration_is_kept():
    assert (REPO_ROOT / "CNAME").read_text(encoding="utf-8").strip() == "bafras.com"


@pytest.mark.skipif(shutil.which("git") is None, reason="git no disponible")
@pytest.mark.parametrize("relative", ["dist/index.html", "build/lib/x.py", "src/bafras_web.egg-info/PKG-INFO"])
def test_generated_paths_are_ignored(relative):
    result = subprocess.run(["git", "check-ignore", "-q", relative], cwd=REPO_ROOT, check=False)
    assert result.returncode == 0, relative
