"""Renderizado Jinja2 de las plantillas del paquete.

Solo conoce nombres de plantilla y contextos explícitos: no lee contenido, rutas ni
políticas de publicación. Los errores de Jinja2 (`TemplateNotFound`, `UndefinedError`,
`TemplateSyntaxError`) se propagan sin transformar.
"""

from __future__ import annotations

from collections.abc import Mapping
from functools import cache

from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape


@cache
def template_environment() -> Environment:
    """Entorno compartido: plantillas de `bafras_web/templates`, autoescape HTML y variables estrictas.

    Para añadir plantillas (p. ej. en pruebas) sin perder esta configuración, usar
    `template_environment().overlay(loader=...)`.
    """
    return Environment(
        loader=PackageLoader("bafras_web", "templates"),
        autoescape=select_autoescape(enabled_extensions=("html",), default_for_string=True),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_html(
    template_name: str,
    context: Mapping[str, object],
    *,
    environment: Environment | None = None,
) -> str:
    """Renderiza `template_name` con exactamente las variables de `context`."""
    env = environment if environment is not None else template_environment()
    return env.get_template(template_name).render(dict(context))
