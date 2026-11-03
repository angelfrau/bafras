# Infrastructure & Engineering Public Content V1.0

Status: implemented
Date: 2026-09-30

## Source

Implemented from the pasted "BAFRAS Engineering - Area tecnica: Infraestructura e Ingenieria - Contenido publico v1.0" handoff.

The public route remains `#/capacidades/infrastructure`.

## B01-B12

- B01 Cabecera: final public hero copy and technical scope.
- B02 Mapa del area tecnica: 4 public area-map scopes.
- B03 Instalaciones: 5 visible disciplines with replaceable evidence slots.
- B04 Coordinacion: split editorial block with technical evidence slot.
- B05 Proyecto: documentation-focused split block with document slot.
- B06 Ejecucion: construction/assistance split block with photo slot.
- B07 Puesta en marcha y verificacion: verification split block with document slot.
- B08 Entregables: 5 flexible deliverable groups.
- B09 Integracion: compact integration map with Energy and Digital areas.
- B10 Experiencia aplicada: 1 featured reference plus 2 supporting references.
- B11 Equipo: team bridge without invented named owner.
- B12 Cierre: final CTA.

## Taxonomy

- Area: Infraestructura e Ingenieria.
- Disciplines: electricidad, climatizacion, ventilacion, instalaciones termicas, fontaneria y saneamiento, proteccion contra incendios.
- Engineering actions: diagnosticar, calcular, dimensionar, disenar, proyectar, coordinar, dirigir, supervisar, poner en marcha and verificar.
- Deliverables: informes, memorias, calculos, planos, esquemas, especificaciones, mediciones, presupuestos, proyectos, documentacion reglamentaria, protocolos and informes de prueba.

## Spanish Terminology

The Infrastructure page avoids public English labels from the previous scaffold:

- commissioning -> puesta en marcha y verificacion.
- MEP -> instalaciones / coordinacion de instalaciones.
- HVAC -> climatizacion y ventilacion.
- technical scope -> alcance tecnico in public language.
- workflow -> flujo / proceso only when conceptually needed.

Class names such as `technical-scope` remain internal implementation details.

## Components Reused

- `capability-hero`
- `area-map`
- `capability-module`
- `capability-split`
- `deliverables-group`
- `integration-examples`
- `experience-evidence`
- `supporting-evidence`
- `owner-strip`
- `related-capabilities`
- `capability-cta`

## Components / Styles Added

- `infrastructure-disciplines`
- `infrastructure-discipline-list`
- `infrastructure-strip`
- `compact-integration`
- `data-asset-kind="document"` slot treatment

## Evidence Slots

V1.1 visual refinement reduced the public placeholder set. Missing real assets now remain as prioritized placeholders:

- CAP-INF-HERO-01
- INFRA-INSTALL-PLAN-01
- INFRA-INSTALL-PHOTO-01
- INFRA-PROJECT-DOC-01
- INFRA-WORKS-PHOTO-01
- INFRA-VERIFY-01
- CAP-INF-EVID-01

No stock, fake plans or generated project evidence were added.

## Visual Refinement V1.1

The Infrastructure page was compacted after visual review:

- five discipline rows with five equal evidence slots became one discipline board with two shared evidence slots;
- coordination, project, execution and verification became one project-to-operation narrative;
- placeholders dropped from 11 to 7;
- Hotel Formentor remains the featured evidence item.

## Experience Attribution

Hotel Formentor, Colegio Montesion and Complejo residencial Ibiza are described as previous professional experience of the team. The page uses "Participacion como jefe de obra" and does not attribute those references to BAFRAS as company projects.

## Deferred

- Authorized real evidence images/documents.
- Human visual QA across desktop and mobile.
- Publication review for named references and image rights.
