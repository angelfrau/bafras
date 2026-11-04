"""Idiomas admitidos y publicados (DEC-14), validados desde config/locales.yaml."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

LocaleCode = Annotated[str, StringConstraints(pattern=r"^[a-z]{2}$")]


class Locale(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    code: LocaleCode
    name: Annotated[str, StringConstraints(min_length=1, strip_whitespace=True)]
    published: bool


class LocaleSettings(BaseModel):
    """El idioma por defecto es también el idioma fuente del contenido y no lleva prefijo de URL."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    schema_version: Literal[1]
    default_locale: LocaleCode
    locales: list[Locale] = Field(min_length=1)

    @model_validator(mode="after")
    def _check(self) -> LocaleSettings:
        codes = [locale.code for locale in self.locales]
        duplicated = sorted({code for code in codes if codes.count(code) > 1})
        if duplicated:
            raise ValueError(f"idiomas duplicados: {', '.join(duplicated)}")
        default = self.get(self.default_locale)
        if default is None:
            raise ValueError(f"default_locale {self.default_locale!r} no está en locales")
        if not default.published:
            raise ValueError(f"el idioma por defecto {self.default_locale!r} debe estar publicado")
        return self

    def get(self, code: str) -> Locale | None:
        return next((locale for locale in self.locales if locale.code == code), None)

    @property
    def codes(self) -> list[str]:
        return [locale.code for locale in self.locales]

    @property
    def published_codes(self) -> list[str]:
        return [locale.code for locale in self.locales if locale.published]
