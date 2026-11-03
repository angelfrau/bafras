# BAFRAS Visual System V1.0

This document defines the shared visual grammar introduced in the Visual System & Composition Consolidation V1 pass.

It is not a separate design system or a redesign. It names the page compositions already used across Home, Infrastructure and Energy so future content can reuse the same structure without adding new card-heavy patterns.

## Design principles

- Evidence before decoration: visual spaces are reserved for real plans, diagrams, technical documents, project evidence or authorized data visuals.
- Editorial hierarchy over card grids: technical pages should read as structured rows, sections and evidence blocks.
- Sparse metrics: numbers are used only when attributable, contextualized and useful.
- Placeholders are temporary: missing evidence is shown as `MATERIAL PENDIENTE` and tracked in the evidence map.
- Mature pages keep Spanish public copy and avoid internal production labels in visible UI.

## Grid

The public pages use a small set of editorial grids:

- `layout-editorial` for conceptual intros.
- `layout-evidence` for text plus technical evidence.
- `layout-feature` for portfolio or proof rows.

All three collapse to one column below tablet width.

## Containers

Keep the existing `.envoltura` container as the page width reference. Text-heavy content should use local max-width rules instead of widening paragraphs to the full container.

## Typography

The public hierarchy should remain close to:

- H1: page proposition.
- H2: section idea.
- H3: technical concept.
- Body: explanation.
- Label / eyebrow: category, area, attribution or numbering.

Avoid stacked micro-headings unless they carry necessary technical meaning.

## Spacing

Use existing section rhythm from `.bloque` and local gaps from the layout classes. Avoid adding page-specific arbitrary gaps unless a section has a clear visual reason.

## Layout A - Editorial Intro

Class: `layout-editorial`

Use for an opening argument paired with a diagram, visual synthesis or other explanatory evidence.

Current use:

- Home system vision section.

Rules:

- Left side carries the editorial argument.
- Right side carries a system-level visual.
- Copy width remains controlled; visuals can be wider.
- On mobile it collapses to one column.

## Layout B - Text + Evidence

Class: `layout-evidence`

Use for technical body sections where explanatory content sits alongside evidence, steps, lists or visual slots.

Current use:

- Home technical area rows.
- Infrastructure discipline board.
- Infrastructure project-to-operation sequence.
- Energy narrative moments.

Rules:

- Text and evidence are peers, not nested cards.
- Use borders and whitespace for separation.
- Use `is-reverse` when evidence leads the section.
- Asset slots must keep `data-asset-id` and `data-asset-kind`.

## Layout C - Full Width Evidence

Class: `layout-feature`

Use for reference, portfolio or proof sections where one larger evidence block supports a public claim.

Current use:

- Home team experience rows.
- Infrastructure featured experience.
- Energy UIB featured experience.

Rules:

- The section should feel like a wide proof row rather than a card.
- Metrics may appear inside the copy side only when attribution is explicit.
- Evidence must be real or tracked as pending.

## Evidence Slots

Shared class: `asset-slot`

Required attributes:

- `data-asset-id`
- `data-asset-kind`
- `data-content-status="placeholder"` when no real asset exists yet

Visible placeholder text:

- Use `MATERIAL PENDIENTE` on mature public pages and Home.
- Do not use `ASSET REQUIRED`, `EVIDENCE REQUIRED` or `CONTENT PENDING` on mature public copy.

Supported kinds currently in use:

- `plan`
- `photo`
- `diagram`
- `dashboard`
- `data`
- `document`

## Evidence system

Evidence slots support both placeholder and real asset states. Real assets should replace placeholder contents directly without restructuring the section.

## Metrics

Shared class: `technical-metrics`

Use only for validated or explicitly contextualized numbers. Current Energy UIB metrics are shown as program magnitudes and include the disclaimer that they do not describe projects executed directly by BAFRAS Engineering.

## Portfolio

Use `layout-feature` for technical experience, important references and future project rows. Attribution must remain visible when an item is team experience rather than a BAFRAS project.

## Deliverables

Deliverables should remain sober text or document evidence, not decorative cards. When a deliverable has real visual proof, use an evidence slot with `data-asset-kind="document"` or the closest available kind.

## CTA

Use one primary CTA pattern and secondary text links. Avoid multiple competing buttons in the same viewport.

## Responsive

At tablet and mobile widths, move to one column before text becomes narrow. Reverse desktop layouts should collapse into logical reading order: heading, text, evidence, data, CTA.

## Content density rules

Preserve technical meaning while reducing repeated labels, nested headings and oversized card groups. If compression could change meaning, keep the copy and log it for content review.

## Placeholder behavior

Placeholders must preserve ratio and editorial space without looking like broken content. On mature pages and Home, visible placeholder labels use `MATERIAL PENDIENTE`.

## Usage examples

Home:

- Uses Layout A for the system vision.
- Uses Layout B for technical areas.
- Uses Layout C for team experience.

Infrastructure:

- Uses Layout B for disciplines and the project-to-operation section.
- Uses Layout C for featured experience.

Energy:

- Uses Layout B for the three narrative moments.
- Uses Layout C and `technical-metrics` for the UIB reference.

## Anti-patterns

- Using cards as the default answer for every section.
- Filling missing evidence with stock images or fake technical mockups.
- Displaying internal labels such as `ASSET REQUIRED` on mature public pages.
- Adding metrics without attribution or context.
- Re-expanding Energy into seven dense visual blocks.

## Deferred Work

- Replace placeholders with approved real assets from `docs/visual-evidence-map.md`.
- Extend the grammar to Digital only after the Digital public content pass.
- Revisit Projects, Sectors, About and Contact in later passes without pulling their patterns into this consolidation prematurely.
