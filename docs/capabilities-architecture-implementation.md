# Technical Areas Public Copy Implementation V1.0

Status: implemented
Date: 2026-09-30

## Source Architecture

The pasted "BAFRAS WEBSITE # TECHNICAL AREAS - PUBLIC COPY V1.0 IMPLEMENTATION" handoff was used as the source of truth for this pass.

Public naming changes from "Capacidades" to "Areas tecnicas". The route remains `#/capacidades`, and internal vertical routes remain under `#/capacidades/...`.

## Public /capacidades

- A01: public name "AREAS TECNICAS", approved hero and explanatory copy.
- A02: approved heading "Tres areas tecnicas. Una vision integrada del activo." with Infrastructure, Energy and Digital area cards.
- A03: integrated intervention narrative and stages 01-08 from analysis through operation and follow-up.
- A04: compact intervention cycle with the required distinction that BAFRAS can intervene in one phase or across the complete technical cycle.
- A05: final CTA with approved "No necesitas partir de una solucion definida" copy.

## Navigation And Taxonomy

- Global public navigation label: "Areas tecnicas".
- Public subnavigation labels: Infrastructure, Energy, Digital, Ingenieria integrada and Ciclo de intervencion.
- Footer public area heading: "Areas tecnicas".
- The old public framing "Tres capacidades" is removed from operative HTML.
- The term "Capacidades" may still appear in project-detail or documentation contexts where it means applied competencies, not the public page name.

## Internal Page Architecture

The vertical architecture remains reusable, with Infrastructure now advanced to Public Content V1.0 and Energy/Digital still scaffolded:

- B01: technical hero.
- B02: area map.
- B03: technical capabilities.
- B04: variable deliverables groups.
- B05: integration with other areas.
- B06: experience and evidence with featured + supporting references.
- B07: owner and related capabilities.
- B08: CTA.

Infrastructure has since received its closed public copy handoff. Energy and Digital still require future public technical copy handoffs.

## Area Maps

- Infrastructure: 4 groups.
- Energy: 6 groups.
- Digital: 6-stage flow, Medir -> Controlar -> Supervisar -> Integrar -> Explotar -> Verificar.

## Component / Pattern System

- `capability-hero`
- `capability-module`
- `integrated-workflow`
- `intervention-cycle`
- `area-map`
- `capability-area`
- `deliverables-group`
- `technical-flow`
- `experience-evidence`
- `supporting-evidence`
- `owner-strip`
- `related-capabilities`
- `capability-cta`

## Legacy Migration

- KEEP: route slugs, internal page scaffold, area identities and verified project contexts.
- MODIFY: public page and navigation terminology from "Capacidades" to "Areas tecnicas".
- REMOVE: obsolete public "Tres capacidades" concept from operative HTML.
- DEFER: final copy for Energy and Digital, validated responsibility wording, deliverables finalization and real assets.

## Placeholders

Placeholders remain only where the handoff says future technical copy or evidence is pending:

- `data-content-status="placeholder"`
- `data-content-status="verify"`
- `ASSET REQUIRED`
- `EVIDENCE REQUIRED`
- `CONTENT PENDING`
- `DELIVERABLES TO DEFINE`

## Production Safety

`tools/validate.py` fails broken assets, legacy operative `/images/`, obvious mojibake in operative files, obsolete "Tres capacidades" terminology in operative HTML, and obsolete "Capacidades" as the global public nav label. Placeholder and verify markers remain warnings.

## Deferred Work

- Public Technical Copy for Energy and Digital.
- Final deliverable families per vertical.
- Real evidence assets and alt text.
- Verification of public reference names, responsibilities, magnitudes and publication rights.
- Human visual QA across desktop and mobile.
