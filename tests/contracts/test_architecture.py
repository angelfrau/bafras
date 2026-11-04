"""Reglas de dependencia entre subpaquetes de bafras_web (docs/architecture.md, «Reglas de dependencia»)."""

from __future__ import annotations

import ast
from pathlib import Path

import bafras_web

PACKAGE_DIR = Path(bafras_web.__file__).parent
LAYERS = ("editorial", "localization", "site", "media", "application", "adapters")

# Subpaquetes internos que cada capa puede importar.
ALLOWED_INTERNAL = {
    "media": set(),
    "editorial": {"media"},
    "localization": {"editorial", "media"},
    "site": {"editorial", "localization", "media"},
    "adapters": {"editorial", "localization", "site", "media"},
    "application": {"editorial", "localization", "site", "media", "adapters"},
}

# Bibliotecas externas o de sistema de archivos prohibidas por capa.
FORBIDDEN_EXTERNAL = {
    "editorial": {"yaml", "jinja2", "os", "pathlib", "shutil", "io"},
    "localization": {"yaml", "jinja2"},
    "site": {"yaml", "jinja2"},
    "media": {"yaml", "jinja2"},
}


def _layer_of(path: Path) -> str:
    rel = path.relative_to(PACKAGE_DIR)
    return rel.parts[0] if len(rel.parts) > 1 else rel.stem


def _imports_in_source(source: str, package: list[str]) -> set[str]:
    """Módulos importados por `source`, con los imports relativos resueltos desde `package`."""
    found: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = package[: len(package) - (node.level - 1)]
                found.add(".".join([*base, node.module] if node.module else base))
            elif node.module:
                found.add(node.module)
    return found


def _imports(path: Path) -> set[str]:
    # Paquete que contiene el módulo; para un __init__.py, el propio paquete.
    package = ["bafras_web", *path.relative_to(PACKAGE_DIR).parent.parts]
    return _imports_in_source(path.read_text(encoding="utf-8"), package)


def _python_files() -> list[Path]:
    return sorted(PACKAGE_DIR.rglob("*.py"))


def _internal_layer(module: str) -> str | None:
    parts = module.split(".")
    if parts[0] != "bafras_web" or len(parts) < 2:
        return None
    return parts[1]


def _layer_graph() -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for path in _python_files():
        layer = _layer_of(path)
        for module in _imports(path):
            target = _internal_layer(module)
            if target and target != layer:
                graph.setdefault(layer, set()).add(target)
    return graph


def test_every_layer_exists_as_a_package():
    for layer in LAYERS:
        assert (PACKAGE_DIR / layer / "__init__.py").is_file(), layer


def test_internal_dependencies_follow_the_rules():
    violations = []
    for path in _python_files():
        layer = _layer_of(path)
        if layer not in ALLOWED_INTERNAL:
            continue  # cli, __init__ y __main__ componen y pueden importar cualquier capa
        for module in _imports(path):
            target = _internal_layer(module)
            if target and target != layer and target not in ALLOWED_INTERNAL[layer]:
                violations.append(f"{path.relative_to(PACKAGE_DIR)} -> {module}")
    assert not violations, violations


def test_forbidden_external_imports():
    violations = []
    for path in _python_files():
        forbidden = FORBIDDEN_EXTERNAL.get(_layer_of(path), set())
        for module in _imports(path):
            if module.split(".")[0] in forbidden:
                violations.append(f"{path.relative_to(PACKAGE_DIR)} -> {module}")
    assert not violations, violations


def test_no_dependency_cycles_between_layers():
    graph = _layer_graph()
    visiting: set[str] = set()
    done: set[str] = set()

    def visit(node: str, trail: list[str]) -> None:
        if node in done:
            return
        assert node not in visiting, " -> ".join([*trail, node])
        visiting.add(node)
        for nxt in sorted(graph.get(node, ())):
            visit(nxt, [*trail, node])
        visiting.discard(node)
        done.add(node)

    for node in sorted(graph):
        visit(node, [])


def test_no_layer_imports_the_cli():
    offenders = [
        str(path.relative_to(PACKAGE_DIR))
        for path in _python_files()
        if _layer_of(path) in LAYERS and "bafras_web.cli" in _imports(path)
    ]
    assert not offenders, offenders


def test_relative_imports_are_resolved():
    """Autoprueba del analizador: un import relativo se evalúa como su módulo absoluto."""
    package = ["bafras_web", "editorial"]
    assert _imports_in_source("from ..adapters import filesystem\n", package) == {"bafras_web.adapters"}
    assert _imports_in_source("from . import pages\n", package) == {"bafras_web.editorial"}
    assert _imports_in_source("from .pages import Page\n", package) == {"bafras_web.editorial.pages"}
