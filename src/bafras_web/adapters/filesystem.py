"""Ubicación del proyecto en disco y comprobación de su estructura."""

from __future__ import annotations

import os
import tempfile
import shutil
from contextlib import contextmanager
from collections.abc import Iterator
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
    def site_file(self) -> Path:
        return self.config / "site.yaml"

    @property
    def composition_file(self) -> Path:
        return self.config / "composition.yaml"

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

    @property
    def build(self) -> Path:
        """Salidas locales no publicables (p. ej. `build/preview/`); ignorado por Git."""
        return self.root / "build"

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


def _replace_atomically(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False)
    temporary = Path(handle.name)
    try:
        with handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def write_text_atomically(path: Path, text: str) -> None:
    """Escribe `text` (UTF-8, LF) en `path` sin dejar nunca un archivo a medias.

    El temporal se crea en el mismo directorio y sustituye al destino con `os.replace`; si algo
    falla, se borra el temporal y el archivo anterior queda intacto.
    """
    _replace_atomically(path, text.replace("\r\n", "\n").encode("utf-8"))


def copy_file_atomically(source: Path, target: Path) -> None:
    """Copia byte a byte con la misma garantía; no reescribe un destino ya idéntico. El origen no se toca."""
    data = source.read_bytes()
    if target.is_file() and target.read_bytes() == data:
        return
    _replace_atomically(target, data)


@contextmanager
def staged_directory(output: Path) -> Iterator[Path]:
    """Preparar en un hermano temporal y promover con recuperación del directorio anterior.

    No garantiza atomicidad absoluta de directorios: hay dos renombrados si ya existe salida.
    Solo elimina temporales creados por esta llamada; si la recuperación falla conserva el backup.
    """
    output = output.absolute()
    if output.is_symlink() or (output.exists() and not output.is_dir()):
        raise OSError(f"salida no admitida: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}-stage-", dir=output.parent))
    backup: Path | None = None
    try:
        yield staging
        if output.exists():
            backup = Path(tempfile.mkdtemp(prefix=f".{output.name}-previous-", dir=output.parent))
            backup.rmdir()
            output.rename(backup)
        try:
            staging.rename(output)
        except OSError:
            if backup is not None:
                try:
                    backup.rename(output)
                except OSError as recovery:
                    raise OSError(f"recuperación fallida; salida anterior conservada en {backup}: {recovery}") from recovery
                backup = None
            raise
        if backup is not None:
            shutil.rmtree(backup)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
