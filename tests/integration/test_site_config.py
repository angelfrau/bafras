"""La configuración real de config/ cumple DEC-14 y DEC-16 y coincide con D03 V1.22 §3.1."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application.configuration import ConfigurationError, load_site_routing

REPO_ROOT = Path(__file__).resolve().parents[2]
D03 = next((REPO_ROOT / "docs" / "project_v02").glob("03_contenido_editorial_V1_22_*.md"))

# Nombre de página en D03 §3.1 → identificador estable.
D03_PAGE_IDS = {
    "Inicio": "inicio",
    "Capacidades": "capacidades",
    "Infraestructuras e instalaciones": "infraestructuras",
    "Sistemas energéticos": "sistemas_energeticos",
    "Automatización y control": "automatizacion_control",
    "Sectores": "sectores",
    "Proyectos y experiencia": "proyectos_experiencia",
    "Sobre BAFRAS": "sobre_bafras",
    "Contacto": "contacto",
}


@pytest.fixture(scope="module")
def routing():
    return load_site_routing(ProjectPaths(REPO_ROOT))


def _d03_spanish_paths() -> dict[str, str]:
    """Tabla «Rutas canónicas propuestas» de D03 §3.1, sin el prefijo /es/ (DEC-16)."""
    text = D03.read_text(encoding="utf-8")
    section = text.split("### 3.1 Rutas canónicas propuestas", 1)[1].split("###", 1)[0]
    rows = re.findall(r"^\| ([^|]+?) \| `/es/([^`]*)` \|", section, flags=re.M)
    return {D03_PAGE_IDS[name]: "/" + path for name, path in rows}


def test_locales_dec14(routing):
    assert routing.locales.default_locale == "es"
    assert routing.locales.codes == ["es", "ca", "en", "de"]
    assert routing.locales.published_codes == ["es"]


def test_nine_pages_with_stable_ids(routing):
    assert list(routing.routes.pages) == list(D03_PAGE_IDS.values())


def test_spanish_urls_match_d03_without_prefix(routing):
    expected = _d03_spanish_paths()
    assert len(expected) == 9
    assert {page_id: routing.url(page_id, "es") for page_id in routing.routes.pages} == expected


def test_spanish_urls_are_unique(routing):
    urls = [routing.url(page_id, "es") for page_id in routing.routes.pages]
    assert len(urls) == len(set(urls))


def test_unpublished_locales_produce_no_links(routing):
    for page_id in routing.routes.pages:
        assert routing.alternates(page_id) == {"es": routing.url(page_id, "es")}
        assert all(routing.url(page_id, code) is None for code in ("ca", "en", "de"))


def test_invalid_files_report_their_origin(tmp_path):
    (tmp_path / "config").mkdir()
    (tmp_path / "config/locales.yaml").write_text("schema_version: 1\ndefault_locale: es\nlocales: []\n", encoding="utf-8")
    (tmp_path / "config/routes.yaml").write_text("pages:\n  a: {slugs: {es: x}}\n  a: {slugs: {es: y}}\n", encoding="utf-8")
    with pytest.raises(ConfigurationError) as exc_info:
        load_site_routing(ProjectPaths(tmp_path))
    problems = exc_info.value.problems
    assert any(p.startswith("config/locales.yaml: locales:") for p in problems)
    assert any(p.startswith("config/routes.yaml:") and "clave duplicada 'a'" in p for p in problems)
