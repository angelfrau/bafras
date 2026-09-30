from pathlib import Path

from tools.validate import ROOT, validate


def test_foundation_files_exist():
    for relative in [
        "index.html",
        "css/tokens.css",
        "css/base.css",
        "css/components.css",
        "css/pages.css",
        "js/site.js",
        "js/router.js",
        "js/form.js",
        "assets/images/brand/favicon/favicon.ico",
        "tools/validate.py",
        "docs/architecture.md",
    ]:
        assert (ROOT / relative).is_file(), relative


def test_static_structure_validation_passes():
    assert validate() == []


def test_no_unconsumed_data_directory():
    assert not (ROOT / "data").exists()


def test_cname_is_preserved():
    assert (ROOT / "CNAME").read_text(encoding="utf-8").strip() == "bafras.com"
