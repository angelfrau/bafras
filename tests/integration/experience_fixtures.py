"""Fixtures internos de WEB-EXPERIENCE-04 (no publicables): se construyen en memoria sobre los BuildInputs reales.

Nunca escriben en content/ ni en config/: los builds editoriales normales no los ven. Los textos son marcadores de
prueba evidentes («Fixture …»), no afirmaciones sobre BAFRAS.
"""
from __future__ import annotations

from bafras_web.application import build
from bafras_web.editorial.entities import Experience
from bafras_web.editorial.primitives import TextItem
from bafras_web.editorial.sections import ExperienceEntry

INDEX_PAGE = "proyectos_experiencia"
CONTROL_MESSAGES = {"experience-portfolio-previous": "Fixture anterior", "experience-portfolio-next": "Fixture siguiente"}


def fixture_project(n: int, *, figures: int = 2, long: bool = False) -> Experience:
    summary = "Resumen fixture de proyecto BAFRAS número %d." % n
    if long:
        summary += " Texto de prueba extenso para comprobar que la tarjeta crece sin recortes ni solapamientos." * 4
    return Experience.model_validate({
        "id": f"fixture-proyecto-{n}", "kind": "bafras_project", "title": f"Fixture proyecto BAFRAS {n}",
        "attribution": "Fixture", "role": "Rol fixture", "summary": [{"id": "summary", "text": summary}],
        "key_figures": [{"id": f"f{i}", "text": f"Magnitud fixture {i}"} for i in range(1, figures + 1)],
        "review": {"status": "draft"},
    })


def _index(bundle):
    page = bundle.get_page(INDEX_PAGE)
    return page, next(s for s in page.sections if s.kind == "experience_index")


def with_index(inputs: build.BuildInputs, *, add: dict[int, list[Experience]] | None = None,
               replace: dict[str, Experience] | None = None, messages: dict[str, str] | None = None) -> build.BuildInputs:
    """Copia de los inputs con experiencias añadidas a los ámbitos indicados (por posición), entidades sustituidas
    y mensajes de interfaz adicionales. El resto (rutas, MEDIA, composición) es el real."""
    bundle = inputs.bundle
    page, index = _index(bundle)
    groups = list(index.groups)
    added: list[Experience] = []
    for position, experiences in (add or {}).items():
        group = groups[position]
        entries = [*group.entries, *(ExperienceEntry(id=e.id, experience_ref=e.id, emphasis="complementary") for e in experiences)]
        groups[position] = group.model_copy(update={"entries": entries})
        added.extend(experiences)
    index = index.model_copy(update={"groups": groups})
    page = page.model_copy(update={"sections": [index if s.id == index.id else s for s in page.sections]})
    experiences = [(replace or {}).get(e.id, e) for e in bundle.experiences] + added
    common = bundle.common
    if messages:
        extra = [TextItem(id=k, text=v) for k, v in messages.items()]
        common = common.model_copy(update={"interface_messages": [*common.interface_messages, *extra]})
    bundle = bundle.model_copy(update={
        "experiences": experiences, "common": common,
        "pages": [page if p.page_id == page.page_id else p for p in bundle.pages]})
    return build.BuildInputs(inputs.routing, bundle, inputs.manifest, inputs.composition, inputs.contact)


def portfolio_inputs(inputs: build.BuildInputs, count: int, *, controls: bool = True) -> build.BuildInputs:
    """`count` proyectos BAFRAS repartidos entre ámbitos (orden editorial: ámbito 0, 1, 2, 0, …)."""
    add: dict[int, list[Experience]] = {}
    groups = len(_index(inputs.bundle)[1].groups)
    for n in range(1, count + 1):
        add.setdefault((n - 1) % groups, []).append(fixture_project(n, long=(n == 2)))
    return with_index(inputs, add=add, messages=CONTROL_MESSAGES if controls else None)


def extended_experience(base: Experience, *, locale: str) -> Experience:
    """Contenido técnico ampliado representable por el contrato vigente: párrafos largos, listas extensas,
    varios enlaces y muchas magnitudes. Textos alemanes más largos en `de`."""
    word = "Gebäudeautomationssystemintegrationsprüfung" if locale == "de" else "integración"
    para = (f"Fixture párrafo ampliado con {word} y contenido técnico extenso. " * 9).strip()
    item = lambda prefix, n: [{"id": f"{prefix}{i}", "text": f"Fixture {prefix} {i}: {word} " * (1 + i % 3)} for i in range(n)]
    data = base.model_dump(mode="json")
    data.update({
        "context": [{"id": f"c{i}", "text": para} for i in range(3)],
        "intervention": [{"id": f"i{i}", "text": para} for i in range(2)],
        "systems": item("sistema", 9), "phases": item("fase", 7), "deliverables": item("entregable", 6),
        "key_figures": item("magnitud", 8),
        "results": [{"id": f"r{i}", "text": para, "evidence_refs": ["fixture"]} for i in range(2)],
        "links": [{"id": f"l{i}", "label": f"Fixture enlace externo {i} {word}",
                   "target": {"kind": "external", "url": f"https://example.org/fixture/{i}"}} for i in range(4)],
    })
    return Experience.model_validate(data)
