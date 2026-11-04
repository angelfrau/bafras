"""Caso de uso: cargar y validar la configuración de idiomas y rutas del sitio."""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ValidationError

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.yaml_files import YamlFileError, load_yaml
from bafras_web.localization.locales import LocaleSettings
from bafras_web.site.routes import RouteTable, SiteRouting


class ConfigurationError(Exception):
    """Configuración inválida; `problems` contiene un mensaje por error, con su origen."""

    def __init__(self, problems: list[str]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


def _messages(source: str, error: ValidationError) -> list[str]:
    problems = []
    for item in error.errors():
        location = ".".join(str(part) for part in item["loc"])
        problems.append(f"{source}: {location + ': ' if location else ''}{item['msg']}")
    return problems


def _validate(model: type[BaseModel], path: Path, label: str) -> BaseModel | list[str]:
    try:
        return model.model_validate(load_yaml(path))
    except YamlFileError as exc:
        return [f"{label}: {exc.message}"]
    except ValidationError as exc:
        return _messages(label, exc)


def load_site_routing(paths: ProjectPaths) -> SiteRouting:
    """Valida config/locales.yaml y config/routes.yaml por separado y después en conjunto."""
    locales = _validate(LocaleSettings, paths.locales_file, "config/locales.yaml")
    routes = _validate(RouteTable, paths.routes_file, "config/routes.yaml")
    problems = [*(locales if isinstance(locales, list) else []), *(routes if isinstance(routes, list) else [])]
    if problems:
        raise ConfigurationError(problems)
    try:
        return SiteRouting(locales=locales, routes=routes)
    except ValidationError as exc:
        raise ConfigurationError(_messages("config/locales.yaml + config/routes.yaml", exc)) from exc
