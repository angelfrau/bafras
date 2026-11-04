"""Lectura de archivos YAML del proyecto: único cargador de config/ y content/."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class YamlFileError(Exception):
    """Archivo YAML ilegible, sintácticamente inválido o con claves duplicadas."""

    def __init__(self, path: Path, message: str) -> None:
        super().__init__(f"{path}: {message}")
        self.path = path
        self.message = message


class _StrictSafeLoader(yaml.SafeLoader):
    """SafeLoader que rechaza claves duplicadas (PyYAML conserva la última en silencio)."""


def _mapping_without_duplicates(loader: _StrictSafeLoader, node: yaml.MappingNode) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    seen: set[Any] = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=True)
        if key in seen:
            mark = key_node.start_mark
            raise yaml.constructor.ConstructorError(
                None, None, f"clave duplicada {key!r} (línea {mark.line + 1})", mark
            )
        seen.add(key)
    return loader.construct_mapping(node, deep=True)


_StrictSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping_without_duplicates
)


def load_yaml(path: Path) -> Any:
    """Devuelve el contenido de un único documento YAML en estructuras Python básicas."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise YamlFileError(path, f"no se puede leer ({exc.strerror})") from exc
    try:
        return yaml.load(text, Loader=_StrictSafeLoader)  # noqa: S506 - SafeLoader estricto
    except yaml.YAMLError as exc:
        raise YamlFileError(path, str(exc)) from exc
