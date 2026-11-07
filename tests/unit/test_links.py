from __future__ import annotations

from pathlib import Path

import pytest

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial import EditorialBundle, PageContent
from bafras_web.editorial.integrity import build_editorial_bundle
from bafras_web.editorial.references import ContactLink, ExternalLink, InternalLink
from bafras_web.site.links import LinkResolutionError, iter_link_targets, resolve_links

ROOT = Path(__file__).resolve().parents[2]
PATHS = ProjectPaths(ROOT)
ROUTING = load_site_routing(PATHS)


def _bundle(locale="es"):
    return build_editorial_bundle(inspect_editorial(PATHS, EditorialLoadRequest(locale=locale, policy="COMPLETE")))


def _page(page_id, *targets):
    actions = [{"id": f"a{i}", "label": "Etiqueta", "target": t} for i, t in enumerate(targets)]
    return PageContent.model_validate({
        "page_id": page_id, "locale": "es", "review": {"status": "draft"}, "seo": {},
        "sections": [{"id": "hero", "kind": "hero", "title": "Título", "actions": actions}],
    })


def _problems(page, bundle=None):
    bundle = bundle or EditorialBundle(locale="es", pages=[page])
    with pytest.raises(LinkResolutionError) as info:
        resolve_links(bundle, page, ROUTING)
    return info.value.problems


def test_real_inicio_links_resolve_through_site_routing():
    bundle = _bundle()
    page = bundle.get_page("inicio")
    found = list(iter_link_targets(page))
    resolved = resolve_links(bundle, page, ROUTING)
    assert len(found) == 14 and len({selector for selector, _ in found}) == 14
    assert set(resolved) == {target for _, target in found}
    for _, target in found:
        assert resolved[target] == ROUTING.url(target.page_id, "es")


def test_fragment_is_appended_to_the_routed_url():
    bundle = _bundle()
    resolved = resolve_links(bundle, bundle.get_page("capacidades"), ROUTING)
    assert resolved[InternalLink(page_id="capacidades", section_id="especialidades")] == "/capacidades/#especialidades"


def test_repeated_targets_share_one_resolution_and_keep_distinct_selectors():
    target = {"kind": "internal", "page_id": "contacto"}
    page = _page("inicio", target, target)
    resolved = resolve_links(EditorialBundle(locale="es", pages=[page]), page, ROUTING)
    assert resolved == {InternalLink(page_id="contacto"): "/contacto/"}
    assert [s for s, _ in iter_link_targets(page)] == ["sections/hero/actions/a0/target", "sections/hero/actions/a1/target"]


def test_unknown_page_is_an_integrity_problem_with_its_selector():
    (problem,) = _problems(_page("inicio", {"kind": "internal", "page_id": "noexiste"}))
    assert (problem.kind, problem.selector, problem.target) == ("integrity", "sections/hero/actions/a0/target", "noexiste")
    assert problem.page_id == "inicio" and problem.locale == "es"


def test_unknown_section_is_an_integrity_problem():
    (problem,) = _problems(_page("inicio", {"kind": "internal", "page_id": "inicio", "section_id": "falta"}))
    assert problem.kind == "integrity" and problem.target == "inicio#falta"


def test_unpublished_locale_has_no_public_route_and_no_fallback():
    bundle = _bundle("ca")
    with pytest.raises(LinkResolutionError) as info:
        resolve_links(bundle, bundle.get_page("inicio"), ROUTING)
    assert len(info.value.problems) == 14
    assert {p.kind for p in info.value.problems} == {"availability"} and {p.locale for p in info.value.problems} == {"ca"}


def test_unsupported_link_types_are_explicit():
    (problem,) = _problems(_page("inicio", {"kind": "contact", "channel": "email"}))
    assert problem.kind == "unsupported" and "ContactLink" in problem.reason


def test_external_links_require_https():
    ok = _page("inicio", {"kind": "external", "url": "https://example.org/x"})
    assert resolve_links(EditorialBundle(locale="es", pages=[ok]), ok, ROUTING) == {
        ExternalLink(url="https://example.org/x"): "https://example.org/x"}
    (problem,) = _problems(_page("inicio", {"kind": "external", "url": "http://example.org/x"}))
    assert problem.kind == "integrity"


def test_all_problems_are_reported_together():
    page = _page("inicio", {"kind": "internal", "page_id": "noexiste"}, {"kind": "contact", "channel": "phone"})
    assert [p.kind for p in _problems(page)] == ["integrity", "unsupported"]


def test_editorial_models_are_not_modified():
    bundle = _bundle()
    page = bundle.get_page("inicio")
    before = page.model_dump()
    resolve_links(bundle, page, ROUTING)
    assert page.model_dump() == before and isinstance(ContactLink(channel="email"), ContactLink)
