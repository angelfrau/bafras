"""Rutas localizadas (DEC-16), validadas desde config/routes.yaml.

URL de una página en un idioma: prefijo del idioma ("" para el idioma por defecto, "/<código>" para el
resto) + segmentos de la cadena de páginas padre + "/". La página raíz tiene segmento vacío.
"""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

from bafras_web.localization.locales import LocaleCode, LocaleSettings

PageId = Annotated[str, StringConstraints(pattern=r"^[a-z][a-z0-9_]*$")]
# Un segmento de URL: minúsculas ASCII, dígitos y guiones simples; vacío solo para la raíz.
Slug = Annotated[str, StringConstraints(pattern=r"^([a-z0-9]+(-[a-z0-9]+)*)?$")]

# Primeros segmentos que el idioma por defecto (sin prefijo) no puede usar: los ocupan los
# prefijos de idioma y los recursos publicados.
_RESERVED_ROOT_SEGMENTS = frozenset({"assets"})


class Route(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    parent: PageId | None = None
    slugs: dict[LocaleCode, Slug] = Field(min_length=1)


class RouteTable(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    schema_version: Literal[1]
    pages: dict[PageId, Route] = Field(min_length=1)

    @model_validator(mode="after")
    def _check_hierarchy(self) -> RouteTable:
        for page_id, route in self.pages.items():
            if route.parent is not None and route.parent not in self.pages:
                raise ValueError(f"{page_id}: página padre inexistente {route.parent!r}")
            seen = {page_id}
            ancestor = route.parent
            while ancestor is not None:
                if ancestor in seen:
                    raise ValueError(f"{page_id}: ciclo en la jerarquía de páginas")
                seen.add(ancestor)
                ancestor = self.pages[ancestor].parent
            for locale, slug in route.slugs.items():
                if slug == "" and route.parent is not None:
                    raise ValueError(f"{page_id}: slug vacío ({locale}) solo se admite en la página raíz")
        roots = sorted({pid for pid, r in self.pages.items() for slug in r.slugs.values() if slug == ""})
        if len(roots) > 1:
            raise ValueError(f"más de una página raíz con slug vacío: {', '.join(roots)}")
        return self

    def segments(self, page_id: str, locale: str) -> list[str] | None:
        """Segmentos de la página y sus padres, o None si alguno no tiene slug en el idioma."""
        chain: list[str] = []
        current: str | None = page_id
        while current is not None:
            route = self.pages[current]
            if locale not in route.slugs:
                return None
            if route.slugs[locale]:
                chain.append(route.slugs[locale])
            current = route.parent
        return list(reversed(chain))


class SiteRouting(BaseModel):
    """Combina idiomas y rutas; fuente única de URL internas y alternativas de idioma."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    locales: LocaleSettings
    routes: RouteTable

    @model_validator(mode="after")
    def _check_against_locales(self) -> SiteRouting:
        declared = set(self.locales.codes)
        default = self.locales.default_locale
        for page_id, route in self.routes.pages.items():
            unknown = sorted(set(route.slugs) - declared)
            if unknown:
                raise ValueError(f"{page_id}: idiomas no declarados en locales.yaml: {', '.join(unknown)}")
            if default not in route.slugs:
                raise ValueError(f"{page_id}: falta el slug del idioma por defecto {default!r}")
            if route.parent is not None:
                missing = sorted(set(route.slugs) - set(self.routes.pages[route.parent].slugs))
                if missing:
                    raise ValueError(f"{page_id}: tiene slug en {', '.join(missing)} pero su padre no")

        reserved = _RESERVED_ROOT_SEGMENTS | declared
        for code in self.locales.codes:
            paths: dict[str, str] = {}
            for page_id in self.routes.pages:
                segments = self.routes.segments(page_id, code)
                if segments is None:
                    continue
                if code == default and segments and segments[0] in reserved:
                    raise ValueError(f"{page_id}: el segmento {segments[0]!r} está reservado")
                path = self._path(code, segments)
                if path in paths:
                    raise ValueError(f"ruta duplicada {path} ({paths[path]} y {page_id})")
                paths[path] = page_id
        return self

    def _path(self, locale: str, segments: list[str]) -> str:
        prefix = "" if locale == self.locales.default_locale else f"/{locale}"
        return prefix + "/" + "".join(f"{segment}/" for segment in segments)

    def url(self, page_id: str, locale: str) -> str | None:
        """URL publicada de la página en el idioma, o None si el idioma no está publicado o no hay slug."""
        if page_id not in self.routes.pages:
            raise KeyError(f"página desconocida: {page_id!r}")
        if locale not in self.locales.published_codes:
            return None
        segments = self.routes.segments(page_id, locale)
        return None if segments is None else self._path(locale, segments)

    def alternates(self, page_id: str) -> dict[str, str]:
        """Páginas equivalentes publicadas por idioma (selector de idioma y hreflang)."""
        found = {code: self.url(page_id, code) for code in self.locales.published_codes}
        return {code: url for code, url in found.items() if url is not None}
