"""Verificación física y materialización de una selección ya resuelta por APPLICATION/SITE."""
from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path

from bafras_web.media.assets import ResolvedImage

from .filesystem import ProjectPaths, copy_file_atomically, staged_directory, write_text_atomically
from .site_integrity import SiteIntegrityError, validate_site_tree


class OutputError(ValueError):
    def __init__(self, problems: list[str]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


def image_file_problems(root: Path, image: ResolvedImage, expected_sha256: str | None) -> list[str]:
    """Comparar archivo con metadatos MEDIA; no decide composición ni elegibilidad."""
    source = (root / image.source_path).resolve()
    if not source.is_relative_to((root / "assets/images").resolve()):
        return [f"{image.asset_id}: archivo fuera de assets/images"]
    if not source.is_file():
        return [f"{image.asset_id} sin archivo en {image.source_path}"]
    try:
        data = source.read_bytes()
    except OSError as error:
        return [f"{image.asset_id}: no se puede leer {image.source_path}: {error}"]
    if len(data) != image.size_bytes:
        return [f"{image.asset_id} no coincide con el tamaño del manifiesto ({image.size_bytes} bytes)"]
    if expected_sha256 and hashlib.sha256(data).hexdigest() != expected_sha256:
        return [f"{image.asset_id} no coincide con SHA-256 del manifiesto"]
    return []


def _asset_copies(paths: ProjectPaths, output: Path, assets: tuple[str, ...]) -> list[tuple[Path, Path]]:
    source_root, target_root = (paths.root / "assets").resolve(), output.resolve()
    copies, problems = [], []
    for relative in assets:
        source, target = (paths.root / relative).resolve(), (output / relative).resolve()
        if not source.is_relative_to(source_root) or not target.is_relative_to(target_root):
            problems.append(f"recurso fuera de los directorios permitidos: {relative}")
        elif not source.is_file():
            problems.append(f"recurso inexistente: {relative}")
        else:
            copies.append((source, target))
    if problems:
        raise OutputError(problems)
    return copies


def materialize_preview(paths: ProjectPaths, output: Path, html_by_url: Mapping[str, str], assets: tuple[str, ...],
                        *, allowed_missing_pages: set[str], legacy_alias: Path | None = None) -> tuple[Path, ...]:
    """URL públicas explícitas → HTML físico, assets e integridad antes de promover.

    Esta traducción física no es un segundo routing: solo acepta las URL recibidas de SITE.
    El staging y su recuperación permanecen en filesystem.staged_directory.
    """
    if output.is_symlink():
        raise OutputError([f"salida no admitida: enlace simbólico {output}"])
    targets: dict[str, Path] = {}
    for url in html_by_url:
        if re.fullmatch(r"/(?:[a-z0-9-]+/)*", url) is None:
            raise OutputError([f"URL no admitida para salida física: {url!r}"])
        relative = Path(url.lstrip("/")) / "index.html"
        if relative.as_posix().casefold() in {p.as_posix().casefold() for p in targets.values()}:
            raise OutputError([f"colisión de ruta: {url}"])
        targets[url] = relative
    if legacy_alias is not None and (legacy_alias.is_absolute() or ".." in legacy_alias.parts or len(html_by_url) != 1):
        raise OutputError([f"alias individual no admitido: {legacy_alias}"])
    _asset_copies(paths, output, assets)  # validar antes de crear temporales
    try:
        with staged_directory(output) as staging:
            for source, target in _asset_copies(paths, staging, assets):
                copy_file_atomically(source, target)
            for url, html in html_by_url.items():
                write_text_atomically(staging / targets[url], html)
            if legacy_alias is not None:
                write_text_atomically(staging / legacy_alias, next(iter(html_by_url.values())))
            validate_site_tree(staging, allowed_missing_pages=allowed_missing_pages)
    except SiteIntegrityError as error:
        raise OutputError(error.problems) from error
    return tuple(output / relative for relative in targets.values())
