"""CONTENT-EXPERIENCE-02 + LOCALIZATION-EXPERIENCE-01: contrato de Experience y siete referencias.

Las expectativas críticas son literales e independientes de la addenda D03 que alimenta otras pruebas.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from pydantic import ValidationError

from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial import Experience
from bafras_web.editorial.integrity import build_editorial_bundle

ROOT = Path(__file__).resolve().parents[3]
LOCALES = ("es", "ca", "en", "de")
BASE = {"id": "ref", "kind": "founder_previous", "title": "Referencia", "review": {"status": "draft"}}
UIB_URL = "https://diari.uib.cat/w/la-uib-formalitza-un-dels-projectes-d-autoconsum-energetic-mes-grans-de-l-ambit-universitari-de-l-estat"
DOI = "https://doi.org/10.1016/j.asoc.2025.114175"
# Ámbito → [(referencia, profesional)], en el orden aprobado; la primera de cada ámbito es la destacada.
EXPECTED = {
    "infrastructure": [("four-seasons-formentor", "angel"), ("montesion", "angel"), ("the-n-residences-ibiza", "angel")],
    "automation": [("dogger-bank-a", "amin"), ("vineyard-wind-1", "amin")],
    "energy": [("uib-transicion-energetica", "murti"), ("edge-ai-investigacion", "murti")],
}
FEATURED = {"four-seasons-formentor", "dogger-bank-a", "uib-transicion-energetica"}
FULL_NAMES = {"angel": "Àngel Frau Salom", "amin": "Amin", "murti": "Murti Bär"}


@pytest.fixture(scope="module")
def bundles():
    paths = ProjectPaths(ROOT)
    return {loc: build_editorial_bundle(inspect_editorial(paths, EditorialLoadRequest(locale=loc, policy="COMPLETE")))
            for loc in LOCALES}


def _index(bundle):
    return next(s for s in bundle.get_page("proyectos_experiencia").sections if s.kind == "experience_index")


def _numbers(texts):
    """Valores numéricos con independencia del separador decimal o de miles del idioma (1,2 = 1.2; 7.500 = 7,500)."""
    return sorted(re.sub(r"[.,\s]", "", n) for text in texts for n in re.findall(r"\d[\d.,\s]*\d|\d", text))


# ---------- Contrato del modelo ----------

def test_new_fields_are_optional_and_backward_compatible():
    experience = Experience.model_validate(BASE)
    assert experience.role is None and experience.key_figures == [] and experience.links == []


def test_links_must_be_external():
    external = {"id": "doi", "label": "DOI", "target": {"kind": "external", "url": DOI}}
    assert Experience.model_validate({**BASE, "links": [external]}).links[0].id == "doi"
    internal = {"id": "page", "label": "Página", "target": {"kind": "internal", "page_id": "contacto"}}
    with pytest.raises(ValidationError, match="external"):
        Experience.model_validate({**BASE, "links": [internal]})


def test_unknown_fields_are_still_rejected():
    with pytest.raises(ValidationError):
        Experience.model_validate({**BASE, "organization": "Inventada"})


# ---------- Siete referencias (literales) ----------

@pytest.mark.parametrize("locale", LOCALES)
def test_groups_order_professionals_and_featured(bundles, locale):
    bundle = bundles[locale]
    index = _index(bundle)
    assert [g.id for g in index.groups] == list(EXPECTED)
    for group in index.groups:
        assert [(e.experience_ref, bundle.get_experience(e.experience_ref).person_refs[0]) for e in group.entries] \
            == EXPECTED[group.id]
        assert {e.experience_ref for e in group.entries if e.emphasis == "featured"} == FEATURED & {r for r, _ in EXPECTED[group.id]}
    assert [e.id for e in bundle.experiences] == [r for refs in EXPECTED.values() for r, _ in refs]


@pytest.mark.parametrize("locale", LOCALES)
def test_public_attribution_is_affirmative(bundles, locale):
    """CONTENT-EXPERIENCE-03: atribución pública «Profesional · Rol» (attribution · role), sin descargos ni nota general."""
    bundle = bundles[locale]
    assert bundle.get_page("proyectos_experiencia").sections[0].attribution is None
    for experience in bundle.experiences:
        assert experience.kind == "founder_previous" and experience.review.status == "draft"
        assert experience.attribution == FULL_NAMES[experience.person_refs[0]]
        assert experience.role and experience.summary
        assert experience.verification.verified and experience.verification.authorized and experience.verification.evidence_refs
        assert "scope" not in {p.id for p in experience.intervention}, f"{locale}/{experience.id}: nota de alcance pública"


def test_spanish_facts(bundles):
    bundle = bundles["es"]
    get = bundle.get_experience
    assert get("four-seasons-formentor").role == "Técnico de instalaciones"
    assert [f.text for f in get("dogger-bank-a").key_figures] == ["Capacidad nominal del parque: 1,2 GW"]
    assert [f.text for f in get("vineyard-wind-1").key_figures] == ["Capacidad nominal del parque: 806 MW"]
    assert [f.text for f in get("uib-transicion-energetica").key_figures][0] == "7,6 MWp de generación fotovoltaica en el programa"
    assert [(l.label, str(l.target.url)) for l in get("uib-transicion-energetica").links] == [("Ver noticia institucional", UIB_URL)]
    assert [(l.label, str(l.target.url)) for l in get("edge-ai-investigacion").links] == [("Consultar publicación científica", DOI)]
    assert [r.evidence_refs for r in get("edge-ai-investigacion").results] == [[DOI]]
    for wind in ("dogger-bank-a", "vineyard-wind-1"):
        assert len(get(wind).phases) == 10 and get(wind).intervention == []
        assert {"pitch-control", "yaw-control", "anomaly-detection"} <= {p.id for p in get(wind).phases}
    assert [p.id for p in get("uib-transicion-energetica").intervention] == ["work"]
    residences = get("the-n-residences-ibiza")
    assert residences.summary[0].text.startswith("Ejerció") and residences.intervention == []


# ---------- Invariantes entre idiomas ----------

@pytest.mark.parametrize("locale", ("ca", "en", "de"))
def test_translations_keep_values_links_and_names(bundles, locale):
    for es, tr in zip(bundles["es"].experiences, bundles[locale].experiences):
        assert tr.id == es.id and tr.person_refs == es.person_refs and tr.kind == es.kind
        assert _numbers(f.text for f in tr.key_figures) == _numbers(f.text for f in es.key_figures), f"{locale}/{tr.id}"
        assert [str(l.target.url) for l in tr.links] == [str(l.target.url) for l in es.links]
        assert [r.evidence_refs for r in tr.results] == [r.evidence_refs for r in es.results]
        assert [len(getattr(tr, f)) for f in ("phases", "systems", "intervention", "key_figures")] == \
               [len(getattr(es, f)) for f in ("phases", "systems", "intervention", "key_figures")]
        assert tr.summary[0].text != es.summary[0].text
    official = ("Four Seasons Formentor", "Colegio Nuestra Señora de Montesión", "The N Residences Ibiza",
                "Dogger Bank A", "Vineyard Wind 1")
    assert [e.title for e in bundles[locale].experiences][:5] == list(official)
