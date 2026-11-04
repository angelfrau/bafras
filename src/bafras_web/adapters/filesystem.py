"""Ubicación del proyecto en disco y comprobación de su estructura."""

from __future__ import annotations

from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path

# Marcadores de la raíz de un checkout de BAFRAS WEB V2.
_ROOT_MARKERS = ("pyproject.toml", "config", "content")


@dataclass(frozen=True)
class ProjectPaths:
    """Rutas de trabajo de un checkout. `dist/` es salida generada y puede no existir."""

    root: Path

    @property
    def config(self) -> Path:
        return self.root / "config"

    @property
    def locales_file(self) -> Path:
        return self.config / "locales.yaml"

    @property
    def routes_file(self) -> Path:
        return self.config / "routes.yaml"

    @property
    def content(self) -> Path:
        return self.root / "content"

    @property
    def assets(self) -> Path:
        return self.root / "assets"

    @property
    def media_manifest(self) -> Path:
        return self.root / "media-library" / "manifests" / "media-manifest.yaml"

    @property
    def project_docs(self) -> Path:
        return self.root / "docs" / "project_v02"

    @property
    def dist(self) -> Path:
        return self.root / "dist"

    def required_entries(self) -> list[tuple[str, Path]]:
        """Entradas que deben existir en cualquier checkout válido."""
        return [
            ("config/locales.yaml", self.locales_file),
            ("config/routes.yaml", self.routes_file),
            ("content/", self.content),
            ("assets/images/", self.assets / "images"),
            ("media-library/manifests/media-manifest.yaml", self.media_manifest),
            ("docs/project_v02/", self.project_docs),
        ]


def find_project_root(start: Path) -> Path | None:
    """Primer directorio, desde `start` hacia arriba, que contiene todos los marcadores."""
    for candidate in (start, *start.parents):
        if all((candidate / marker).exists() for marker in _ROOT_MARKERS):
            return candidate
    return None


def templates_dir() -> Path:
    """Directorio de plantillas Jinja2 incluido en el paquete instalado."""
    return Path(str(files("bafras_web") / "templates"))
