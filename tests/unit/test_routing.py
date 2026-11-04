"""Contratos de idiomas (DEC-14) y rutas (DEC-16)."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from bafras_web.localization.locales import LocaleSettings
from bafras_web.site.routes import RouteTable, SiteRouting


def _locales(**published):
    states = {"es": True, "ca": False, "en": False, "de": False} | published
    return {
        "schema_version": 1,
        "default_locale": "es",
        "locales": [{"code": c, "name": c.upper(), "published": p} for c, p in states.items()],
    }


def _routes(**extra):
    pages = {
        "inicio": {"slugs": {"es": "", "ca": ""}},
        "capacidades": {"slugs": {"es": "capacidades", "ca": "capacitats"}},
        "infraestructuras": {"parent": "capacidades", "slugs": {"es": "infraestructuras-instalaciones"}},
        "contacto": {"slugs": {"es": "contacto", "ca": "contacte"}},
    }
    pages.update(extra)
    return {"schema_version": 1, "pages": pages}


def _routing(locales=None, routes=None):
    return SiteRouting(
        locales=LocaleSettings.model_validate(locales or _locales()),
        routes=RouteTable.model_validate(routes or _routes()),
    )


# --- idiomas -------------------------------------------------------------------------------


def test_default_locale_must_exist_and_be_published():
    with pytest.raises(ValidationError, match="no está en locales"):
        LocaleSettings.model_validate(_locales() | {"default_locale": "fr"})
    with pytest.raises(ValidationError, match="debe estar publicado"):
        LocaleSettings.model_validate(_locales(es=False))


def test_duplicate_locales_are_rejected():
    data = _locales()
    data["locales"].append({"code": "ca", "name": "Otra", "published": False})
    with pytest.raises(ValidationError, match="idiomas duplicados: ca"):
        LocaleSettings.model_validate(data)


@pytest.mark.parametrize("bad", [{"code": "ES", "name": "x", "published": True}, {"code": "es", "name": "x", "published": "yes"}])
def test_locale_fields_are_strict(bad):
    data = _locales()
    data["locales"][0] = bad
    with pytest.raises(ValidationError):
        LocaleSettings.model_validate(data)


def test_unknown_fields_are_rejected():
    with pytest.raises(ValidationError):
        LocaleSettings.model_validate(_locales() | {"fallback": "es"})


# --- tabla de rutas ------------------------------------------------------------------------


@pytest.mark.parametrize("slug", ["Capacidades", "con espacio", "a//b", "a/b", "-a", "a--b", "ñu", "a-"])
def test_invalid_slugs_are_rejected(slug):
    with pytest.raises(ValidationError):
        RouteTable.model_validate(_routes(otra={"slugs": {"es": slug}}))


def test_page_ids_are_stable_identifiers():
    with pytest.raises(ValidationError):
        RouteTable.model_validate(_routes(**{"Sobre-BAFRAS": {"slugs": {"es": "sobre-bafras"}}}))


def test_parent_must_exist_and_hierarchy_must_be_acyclic():
    with pytest.raises(ValidationError, match="página padre inexistente"):
        RouteTable.model_validate(_routes(hija={"parent": "nadie", "slugs": {"es": "hija"}}))
    with pytest.raises(ValidationError, match="ciclo"):
        RouteTable.model_validate(_routes(
            a={"parent": "b", "slugs": {"es": "a"}}, b={"parent": "a", "slugs": {"es": "b"}},
        ))


def test_only_one_root_page():
    with pytest.raises(ValidationError, match="más de una página raíz"):
        RouteTable.model_validate(_routes(portada={"slugs": {"es": ""}}))
    with pytest.raises(ValidationError, match="solo se admite en la página raíz"):
        RouteTable.model_validate(_routes(hija={"parent": "capacidades", "slugs": {"es": ""}}))


# --- combinación con idiomas ---------------------------------------------------------------


def test_spanish_urls_have_no_prefix_and_nest_under_parents():
    routing = _routing()
    assert routing.url("inicio", "es") == "/"
    assert routing.url("capacidades", "es") == "/capacidades/"
    assert routing.url("infraestructuras", "es") == "/capacidades/infraestructuras-instalaciones/"


def test_other_locales_use_prefix_only_when_published():
    assert _routing().url("contacto", "ca") is None
    routing = _routing(locales=_locales(ca=True))
    assert routing.url("inicio", "ca") == "/ca/"
    assert routing.url("contacto", "ca") == "/ca/contacte/"


def test_language_selector_only_offers_published_equivalents():
    routing = _routing(locales=_locales(ca=True, en=True))
    assert routing.alternates("contacto") == {"es": "/contacto/", "ca": "/ca/contacte/"}
    # Sin traducción publicada: no se inventa enlace ni se recurre al español.
    assert routing.alternates("infraestructuras") == {"es": "/capacidades/infraestructuras-instalaciones/"}
    assert routing.url("infraestructuras", "en") is None


def test_unknown_page_is_an_error():
    with pytest.raises(KeyError):
        _routing().url("inexistente", "es")


def test_every_page_needs_a_default_locale_slug():
    with pytest.raises(ValidationError, match="falta el slug del idioma por defecto"):
        _routing(routes=_routes(solo_ca={"slugs": {"ca": "nomes"}}))


def test_slugs_must_use_declared_locales():
    with pytest.raises(ValidationError, match="idiomas no declarados en locales.yaml: fr"):
        _routing(routes=_routes(otra={"slugs": {"es": "otra", "fr": "autre"}}))


def test_child_translation_requires_parent_translation():
    with pytest.raises(ValidationError, match="su padre no"):
        _routing(routes=_routes(hija={"parent": "infraestructuras", "slugs": {"es": "hija", "ca": "filla"}}))


def test_duplicate_paths_are_rejected():
    with pytest.raises(ValidationError, match="ruta duplicada /contacto/"):
        _routing(routes=_routes(otro_contacto={"slugs": {"es": "contacto"}}))


@pytest.mark.parametrize("segment", ["ca", "en", "de", "assets"])
def test_spanish_top_level_segments_cannot_shadow_prefixes(segment):
    with pytest.raises(ValidationError, match="está reservado"):
        _routing(routes=_routes(otra={"slugs": {"es": segment}}))
