"""Punto de entrada `bafras-web`.

Cada grupo de comandos se declara con una función `_register_<grupo>(subparsers)` que
añade sus subcomandos y asigna `handler`, y se incorpora a `_REGISTRARS`. El CLI solo
compone: las reglas viven en los subpaquetes de dominio y los casos de uso en
`bafras_web.application`.
"""

from __future__ import annotations

import argparse
import platform
import sys
from collections.abc import Callable, Sequence
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from bafras_web import __version__
from bafras_web.adapters.filesystem import ProjectPaths, find_project_root, templates_dir
from bafras_web.application.configuration import ConfigurationError, load_site_routing

# Distribuciones de ejecución declaradas en pyproject.toml.
_RUNTIME_DISTRIBUTIONS = ("pydantic", "PyYAML", "Jinja2")


def _doctor(args: argparse.Namespace) -> int:
    """Diagnóstico del entorno y de la estructura del proyecto. Devuelve 1 si falta algo."""
    problems = 0
    print(f"bafras-web {__version__}")
    print(f"Python {platform.python_version()} ({sys.executable})")

    for dist in _RUNTIME_DISTRIBUTIONS:
        try:
            print(f"  [ok] {dist} {version(dist)}")
        except PackageNotFoundError:
            print(f"  [falta] {dist}")
            problems += 1

    templates = templates_dir()
    if templates.is_dir():
        print(f"  [ok] plantillas del paquete: {templates}")
    else:
        print(f"  [falta] plantillas del paquete: {templates}")
        problems += 1

    root = find_project_root(args.project.resolve())
    if root is None:
        print(f"Proyecto: no se encuentra una raíz BAFRAS WEB desde {args.project.resolve()}")
        return 1

    paths = ProjectPaths(root)
    print(f"Proyecto: {root}")
    for label, path in paths.required_entries():
        if path.exists():
            print(f"  [ok] {label}")
        else:
            print(f"  [falta] {label}")
            problems += 1

    if paths.locales_file.exists() and paths.routes_file.exists():
        try:
            routing = load_site_routing(paths)
        except ConfigurationError as exc:
            for problem in exc.problems:
                print(f"  [error] {problem}")
            problems += len(exc.problems)
        else:
            published = ", ".join(routing.locales.published_codes)
            print(
                f"  [ok] configuración: {len(routing.locales.locales)} idiomas (publicados: {published}),"
                f" {len(routing.routes.pages)} páginas"
            )

    print("Resultado: correcto" if problems == 0 else f"Resultado: {problems} problema(s)")
    return 0 if problems == 0 else 1


def _register_diagnostics(subparsers: argparse._SubParsersAction) -> None:
    doctor = subparsers.add_parser(
        "doctor", help="comprueba dependencias instaladas y estructura del proyecto"
    )
    doctor.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
        help="directorio desde el que buscar la raíz del proyecto (por defecto, el actual)",
    )
    doctor.set_defaults(handler=_doctor)


_REGISTRARS: tuple[Callable[[argparse._SubParsersAction], None], ...] = (
    _register_diagnostics,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bafras-web", description="Herramientas de BAFRAS WEB V2."
    )
    parser.add_argument("--version", action="version", version=f"bafras-web {__version__}")
    subparsers = parser.add_subparsers(dest="command", metavar="COMANDO")
    for register in _REGISTRARS:
        register(subparsers)
    return parser


def _ensure_utf8_output() -> None:
    """Salida en UTF-8 aunque se redirija en Windows (cp1252 por defecto)."""
    for stream in (sys.stdout, sys.stderr):
        encoding = (getattr(stream, "encoding", None) or "").lower().replace("-", "")
        if encoding != "utf8" and hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    _ensure_utf8_output()
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 2
    return handler(args)
