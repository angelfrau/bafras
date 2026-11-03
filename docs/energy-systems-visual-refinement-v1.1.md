# Energy Systems Visual Refinement V1.1

Status: implemented
Date: 2026-09-30

## Baseline

Energy Systems Public Content V1.0 was implemented and validated before this pass. The page had the correct content, route, Spanish public terminology, UIB attribution and five evidence placeholders.

## Problems Identified

- The seven technical domains were visually parallel and created a long central body.
- The evidence rail helped structure the page, but did not create strong narrative moments.
- UIB experience had correct content but needed stronger visual hierarchy.

## Design Decisions

- Preserved all seven domains and their V1.0 copy.
- Consolidated the central body into three narrative moments.
- Kept the energy axis visible as the conceptual spine.
- Gave the transformation moment a larger evidence-first layout.
- Increased UIB visual weight through larger evidence and stronger metrics.

## Seven-Domain Consolidation

- Entender y optimizar: Conocer + Optimizar.
- Transformar el sistema energetico: Generar + Almacenar + Electrificar.
- Gestionar y decidir: Gestionar + Decidir.

## Narrative Moments

- `energy-narrative-moment`
- `energy-domain-pair`
- `energy-domain-pair.is-three`

The route now exposes `data-moment-count="3"` and preserves `data-domain-count="7"`.

## Asset Strategy

No new real assets were added. Existing slots remain:

- ENERGY-HERO-01
- ENERGY-KNOW-01
- ENERGY-GEN-STORAGE-01
- ENERGY-MANAGE-01
- ENERGY-UIB-01

The main body slots are now attached to the three narrative moments rather than a generic rail.

## UIB Visual Treatment

The UIB reference remains explicitly framed as previous professional experience of the team. The magnitudes remain unchanged:

- 7,576 MWp.
- 2 x 5,016 MWh.
- 19 infraestructuras de recarga.

Metrics now have stronger type scale and the evidence slot has more visual weight.

## Responsive Decisions

- Desktop: asymmetric moment layouts, with the transformation moment reversed and larger.
- Tablet: moments collapse to one column without losing order.
- Mobile: each moment reads as title, text, technical detail and evidence.

## Components Modified

- `energy-axis`
- `energy-metrics`
- `energy-experience-cycle`
- Energy-specific responsive rules.

## Components Added

- `energy-moment-list`
- `energy-narrative-moment`
- `energy-domain-pair`

## Validation

- `python tools/validate.py`
- `python -m pytest`
- `git diff --check`

## Deferred Work

- Replace placeholders with authorized real technical evidence.
- Full visual QA at 1440, 1024, 820, 700 and 430.
- Publication rights review for UIB visual evidence.
