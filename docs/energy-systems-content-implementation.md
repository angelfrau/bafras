# Energy Systems Public Content V1.0

Status: implemented
Date: 2026-09-30

## Baseline

The previous `#/capacidades/energy-systems` route was a scaffold with placeholder map text, incomplete deliverables and provisional evidence. Baseline validation passed before implementation.

## Architecture Implemented

- E01 Hero: Spanish public hero for Sistemas Energeticos, with no CTA.
- E02 Area map: six technical scopes plus the narrative axis.
- E03-E09 Technical body: seven-domain editorial system.
- E10 Deliverables: five compact deliverable families.
- E11 Integration: compact bridge to Infrastructure and Digital.
- E12-E13 UIB experience: one featured reference with magnitudes and cycle layer.
- E14 Team bridge: short team link, no invented area owner.
- E15 CTA: final contact CTA.

## Narrative Axis

Implemented as a technical rail:

Conocer -> Optimizar -> Generar -> Almacenar -> Electrificar -> Gestionar -> Decidir

## Visual Decisions

- Avoided seven large repeated cards.
- Used a single domain list with a sticky evidence rail.
- Kept evidence slots limited and narrative-led.
- Presented UIB as experience evidence, not as a BAFRAS company project.
- Replaced prohibited public terms in this route: BESS, CAPEX/OPEX, KPIs and English placeholder labels.

## Components Reused

- `capability-hero`
- `area-map`
- `deliverables-group`
- `capability-integration`
- `integration-examples`
- `experience-evidence`
- `owner-strip`
- `capability-cta`

## Components Added

- `energy-axis`
- `energy-area-map`
- `energy-domain-layout`
- `energy-domain-list`
- `energy-evidence-rail`
- `technical-actions`
- `energy-metrics`
- `energy-experience-cycle`

## Evidence Slots

- ENERGY-HERO-01: curva de carga / balance energetico / esquema de sistema.
- ENERGY-KNOW-01: curva de carga / balance energetico.
- ENERGY-GEN-STORAGE-01: esquema red, generacion, almacenamiento y consumo.
- ENERGY-MANAGE-01: seguimiento energetico / analisis operativo.
- ENERGY-UIB-01: campus, esquema energetico, generacion, almacenamiento or monitoring evidence.

## UIB Experience Treatment

The page states that UIB magnitudes belong to the program, not projects executed directly by BAFRAS Engineering. It uses "Participacion del equipo" framing and avoids derived metrics.

Program magnitudes shown:

- 7,576 MWp generacion fotovoltaica.
- 2 x 5,016 MWh almacenamiento energetico.
- 19 infraestructuras de recarga.

## Validation

- `python tools/validate.py`
- `python -m pytest`
- `git diff --check`

## Deferred

- Real authorized energy evidence assets.
- Visual QA with final assets.
- Publication review for UIB evidence and exact responsibility wording.

## Visual Refinement V1.1

The seven-domain body was consolidated into three visual moments while preserving all V1.0 content:

- Entender y optimizar: Conocer + Optimizar.
- Transformar el sistema energetico: Generar + Almacenar + Electrificar.
- Gestionar y decidir: Gestionar + Decidir.

UIB metrics and evidence were given greater visual hierarchy. See `docs/energy-systems-visual-refinement-v1.1.md`.
