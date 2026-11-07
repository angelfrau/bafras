"""WEB-01: contract between editorial InternalLink identities and SiteRouting URLs.

CONTENT integrity only proves that a target page/section exists. WEB renders links with
SiteRouting, so every editorial link must also resolve to a public URL in published
locales, and to nothing (never to another locale's URL) where the locale is unpublished.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import build_editorial_bundle
from bafras_web.editorial.references import InternalLink

ROOT = Path(__file__).resolve().parents[2]
PATHS = ProjectPaths(ROOT)
ROUTING = load_site_routing(PATHS)


def _bundle(locale: str):
    return build_editorial_bundle(inspect_editorial(PATHS, EditorialLoadRequest(locale=locale, policy="COMPLETE")))


def _internal_links(value, found=None):
    found = [] if found is None else found
    if isinstance(value, InternalLink):
        found.append(value)
    elif hasattr(type(value), "model_fields"):
        for name in type(value).model_fields:
            _internal_links(getattr(value, name), found)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _internal_links(item, found)
    return found


def test_every_configured_page_has_a_bundle_page_and_vice_versa():
    assert {p.page_id for p in _bundle(ROUTING.locales.default_locale).pages} == set(ROUTING.routes.pages)


@pytest.mark.parametrize("locale", ROUTING.locales.published_codes)
def test_published_links_resolve_to_urls_and_existing_anchors(locale):
    bundle = _bundle(locale)
    sources = [*bundle.pages, *bundle.sectors]
    links = [link for source in sources for link in _internal_links(source)]
    assert links
    for link in links:
        assert ROUTING.url(link.page_id, locale), f"{locale}: sin URL para {link.page_id}"
        if link.section_id is not None:
            anchors = {s.id for s in bundle.get_page(link.page_id).sections}
            assert link.section_id in anchors, f"{locale}: ancla {link.page_id}#{link.section_id} inexistente"


@pytest.mark.parametrize("locale", sorted(set(ROUTING.locales.codes) - set(ROUTING.locales.published_codes)))
def test_unpublished_locales_get_no_public_url(locale):
    """No fallback: an unpublished locale never borrows the default locale's URL."""
    page_ids = {link.page_id for page in _bundle(locale).pages for link in _internal_links(page)}
    assert page_ids
    assert all(ROUTING.url(page_id, locale) is None for page_id in page_ids)
    assert all(code in ROUTING.locales.published_codes for code in ROUTING.alternates("inicio"))
