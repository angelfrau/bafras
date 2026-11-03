from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import re

from tools.validate import ROOT, validate


class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.routes = set()
        self.classes_by_route = {}
        self.current_route = None
        self.asset_refs = []
        self.hashes = []

    def handle_starttag(self, tag, attrs):
        data = {key: value or "" for key, value in attrs}
        if data.get("data-pagina") is not None:
            self.current_route = data["data-pagina"]
            self.routes.add(self.current_route)
            self.classes_by_route.setdefault(self.current_route, set())
        class_attr = data.get("class", "")
        if self.current_route and class_attr:
            self.classes_by_route.setdefault(self.current_route, set()).update(class_attr.split())
        if tag in {"img", "source"}:
            src = data.get("src") or data.get("srcset", "")
            if src:
                self.asset_refs.append(src)
        if tag == "a":
            href = data.get("href", "")
            if href.startswith("#/"):
                self.hashes.append(href)


def parse_index():
    parser = StructureParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    return parser


def route_html(route):
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    marker = f'<div class="pagina" data-pagina="{route}">'
    start = html.index(marker)
    next_page = html.find('<div class="pagina"', start + len(marker))
    if next_page == -1:
        next_page = html.index("</main>", start)
    return html[start:next_page]


def visible_text(fragment):
    return unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()


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


def test_capability_routes_exist():
    parser = parse_index()
    for route in [
        "capacidades",
        "capacidades/infrastructure",
        "capacidades/energy-systems",
        "capacidades/digital-systems",
    ]:
        assert route in parser.routes


def test_capability_pages_use_shared_architecture():
    parser = parse_index()
    required = {
        "capability-hero",
        "area-map-section",
        "capability-areas",
        "capability-deliverables",
        "capability-integration",
        "capability-evidence",
        "capability-owner",
        "capability-related",
        "capability-cta",
    }
    for route in [
        "capacidades/infrastructure",
        "capacidades/energy-systems",
        "capacidades/digital-systems",
    ]:
        assert required <= parser.classes_by_route[route]


def test_capabilities_index_uses_required_sections():
    parser = parse_index()
    required = {
        "capability-hero",
        "capability-nav",
        "integrated-engineering",
        "integrated-workflow",
        "capability-cycle",
        "capability-cta",
    }
    assert required <= parser.classes_by_route["capacidades"]


def test_public_navigation_uses_technical_areas_name():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    start = html.index('<nav class="nav"')
    end = html.index("</nav>", start)
    nav = html[start:end]
    assert ">Áreas técnicas<" in nav
    assert ">Capacidades<" not in nav
    assert "#/capacidades" in nav
    assert '<h2 class="pie-t">Áreas técnicas</h2>' in html


def test_capabilities_public_copy_v10():
    html = route_html("capacidades")
    assert "ÁREAS TÉCNICAS" in html
    assert "Ingeniería para intervenir sobre el sistema completo." in html
    assert "Integramos capacidades en instalaciones e infraestructura, sistemas energéticos y sistemas digitales" in html
    assert "Tres áreas técnicas. Una visión integrada del activo." in html
    assert "Tres capacidades" not in html
    assert "Partimos del estado real del activo y de sus necesidades para identificar las actuaciones necesarias" in html
    assert "Evaluación técnico-económica" in html
    assert "Puesta en marcha y verificación" in html
    assert "Operación y seguimiento" in html
    assert "Podemos intervenir en una fase concreta o acompañar el proyecto a lo largo de todo su ciclo técnico." in html
    assert "No necesitas partir de una solución definida." in html
    assert html.count('<article class="capability-module') == 3
    assert html.count("workflow-number") == 8
    assert html.count("<li><strong>") == 5


def test_capability_area_maps_and_variable_deliverables():
    expected_counts = {
        "capacidades/infrastructure": 'data-map-count="4"',
        "capacidades/energy-systems": 'data-map-count="6"',
        "capacidades/digital-systems": 'data-map-count="6"',
    }
    for route, marker in expected_counts.items():
        html = route_html(route)
        assert marker in html
        assert "area-map" in html
        assert "deliverables-group" in html
        assert "experience-evidence is-featured" in html


def test_visual_system_v1_is_documented_and_applied():
    css = (ROOT / "css/components.css").read_text(encoding="utf-8")
    docs = (ROOT / "docs/visual-system-v1.md").read_text(encoding="utf-8")
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for selector in [
        ".layout-editorial",
        ".layout-evidence",
        ".layout-feature",
        ".technical-metrics",
    ]:
        assert selector in css
    for phrase in [
        "Layout A - Editorial Intro",
        "Layout B - Text + Evidence",
        "Layout C - Full Width Evidence",
    ]:
        assert phrase in docs
    assert "home-vision" in html and "layout-editorial" in html
    assert "infrastructure-discipline-board layout-evidence" in route_html("capacidades/infrastructure")
    assert "energy-narrative-moment layout-evidence" in route_html("capacidades/energy-systems")
    assert "energy-metrics technical-metrics" in route_html("capacidades/energy-systems")


def test_infrastructure_public_content_v10_structure():
    html = route_html("capacidades/infrastructure")
    text = visible_text(html)
    for anchor in [
        "infraestructura-cabecera",
        "mapa-area-infraestructura",
        "instalaciones",
        "coordinacion-instalaciones",
        "proyecto-documentacion",
        "direccion-asistencia",
        "puesta-marcha-verificacion",
        "entregables-infraestructura",
        "integracion-infraestructura",
        "experiencia-infraestructura",
        "equipo-infraestructura",
        "cierre-infraestructura",
    ]:
        assert f'id="{anchor}"' in html
    assert "Instalaciones diseñadas para funcionar, integrarse y construirse." in text
    assert 'data-map-count="4"' in html
    assert 'data-discipline-count="5"' in html
    assert 'data-deliverables-count="5"' in html
    assert 'data-integration-count="4"' in html
    assert "¿Tienes una instalación que diseñar, reformar o ejecutar?" in text


def test_infrastructure_visual_refinement_v11_compression():
    html = route_html("capacidades/infrastructure")
    assert "infrastructure-discipline-board" in html
    assert "discipline-list" in html
    assert "project-operation" in html
    assert "project-operation-steps" in html
    assert html.count('data-content-status="placeholder"') <= 8
    assert "INFRA-INSTALL-PLAN-01" in html
    assert "INFRA-INSTALL-PHOTO-01" in html
    assert "INFRA-PROJECT-DOC-01" in html
    assert "INFRA-WORKS-PHOTO-01" in html
    assert "INFRA-VERIFY-01" in html
    for removed_slot in [
        "CAP-INF-ELEC-01",
        "CAP-INF-CLIMA-01",
        "CAP-INF-VENT-01",
        "CAP-INF-WATER-01",
        "CAP-INF-PCI-01",
        "CAP-INF-COORD-01",
        "CAP-INF-PROJ-01",
        "CAP-INF-OBRA-01",
        "CAP-INF-VERIF-01",
    ]:
        assert removed_slot not in html


def test_infrastructure_language_and_attribution_v10():
    text = visible_text(route_html("capacidades/infrastructure"))
    forbidden = [
        "commissioning",
        "technical scope",
        "workflow",
        "punch list",
        "MEP",
        "HVAC",
        "BESS",
        "KPIs",
        "ASSET REQUIRED",
        "EVIDENCE REQUIRED",
        "CONTENT PENDING",
        "DELIVERABLES TO DEFINE",
    ]
    for term in forbidden:
        assert term not in text
    assert not re.search(r"\bEnergy\b|\bDigital\b", text)
    assert "experiencia profesional previa del equipo" in text.lower()
    assert text.count("Participación como jefe de obra") == 3
    assert not re.search(r"BAFRAS[^.]{0,80}(Hotel Formentor|Colegio Montesion|Complejo residencial)", text)


def test_energy_systems_public_content_v10():
    html = route_html("capacidades/energy-systems")
    text = visible_text(html)
    assert "Ingeniería para conocer, transformar y gestionar la energía de un activo." in text
    for axis in ["Conocer", "Optimizar", "Generar", "Almacenar", "Electrificar", "Gestionar", "Decidir"]:
        assert axis in text
    assert 'data-map-count="6"' in html
    assert 'data-domain-count="7"' in html
    assert 'data-energy-deliverables-count="5"' in html
    assert 'data-energy-integration-count="4"' in html
    assert "7,576 MWp" in text
    assert "2 × 5,016 MWh" in text
    assert "19" in text
    assert "Participación del equipo" in text
    assert "no a proyectos ejecutados directamente por BAFRAS Engineering" in text
    assert "ENERGY-KNOW-01" in html
    assert "ENERGY-GEN-STORAGE-01" in html
    assert "ENERGY-MANAGE-01" in html
    assert "ENERGY-UIB-01" in html


def test_energy_systems_visual_refinement_v11():
    html = route_html("capacidades/energy-systems")
    text = visible_text(html)
    assert 'data-moment-count="3"' in html
    assert html.count("energy-narrative-moment") == 3
    assert html.count("<section><span>") == 7
    assert "01 · ENTENDER Y OPTIMIZAR" in text
    assert "02 · TRANSFORMAR EL SISTEMA ENERGÉTICO" in text
    assert "03 · GESTIONAR Y DECIDIR" in text
    assert "Del dato energético a las oportunidades de mejora." in text
    assert "Generación, almacenamiento y electrificación como arquitectura integrada." in text
    assert "Seguimiento, operación y planificación para tomar mejores decisiones." in text


def test_energy_systems_language_and_attribution_v10():
    text = visible_text(route_html("capacidades/energy-systems"))
    forbidden = [
        "BESS",
        "commissioning",
        "KPIs",
        "CAPEX",
        "OPEX",
        "technical scope",
        "Energy Management",
        "Smart Energy",
        "ASSET REQUIRED",
        "EVIDENCE REQUIRED",
        "CONTENT PENDING",
        "DELIVERABLES TO DEFINE",
    ]
    for term in forbidden:
        assert term not in text
    assert not re.search(r"BAFRAS[^.]{0,100}(7,576|5,016|infraestructuras de recarga|Universitat)", text)


def test_no_legacy_images_or_mojibake_in_operational_files():
    patterns = [
        "\u00c3\u00a2",
        "\u00e2",
        "\u00c3",
        "\u00c3\u0192",
        "\u00c3\u201a",
        "\u00c2",
        "\u00c3\u00b0",
        "\u00ef\u00bf\u00bd",
        "\u00e2\u2020",
        "\u00e2\u20ac\u201d",
        "\u00e2\u20ac\u2122",
        "\u00e2\u20ac\u0153",
    ]
    for relative in ["index.html", "css/components.css", "css/pages.css", "js/router.js"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert not re.search(r"(?<!assets)/images/", text)
        for pattern in patterns:
            assert pattern not in text, f"{pattern!r} in {relative}"
