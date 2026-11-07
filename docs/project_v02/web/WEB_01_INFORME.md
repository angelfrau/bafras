# WEB-01 R2 · Auditoría resolutiva de integración CONTENT → WEB

Fecha: 07/11/2026 · Plan resultante: [WEB_V01_A_PLAN](WEB_V01_A_PLAN.md).

## STATUS

**GO para WEB-V01-A.** No hay bloqueos externos para la vertical Inicio `es` en preview. Las dependencias
pendientes (`MediaRef`, `common.yaml`, SEO de DEC-05) solo afectan a la fidelidad visual completa y a release,
que quedan fuera de V01-A.

## BASELINE

- **Rama:** `feat/contingut-v2`.
- **HEAD:** `3927e5f` (commit CONTENT); `main` en `04c92c8`.
- **Árbol de trabajo:** limpio, sin trabajo ajeno pendiente.
- **Suite inicial:** 573 passed.
- **`bafras-web doctor`:** correcto (4 idiomas, publicado `es`, 9 páginas).

**Inventario WEB dirigido:**

| Elemento | Clasificación |
|---|---|
| API CONTENT (`inspect_editorial`, `build_editorial_bundle`, `EditorialBundle`, modelos) | Implementado y comprobado |
| `site/routes.py` (`RouteTable`, `SiteRouting.url/alternates`) y `config/{locales,routes}.yaml` | Implementado y comprobado |
| `adapters/yaml_files.py`, `adapters/filesystem.py`, `cli.py` (`doctor`) | Implementado y comprobado |
| Adaptador Jinja2, plantillas (`templates/` solo tiene README), CSS y JS (`assets/` solo tiene `images/`) | Ausente y necesario para V01-A |
| Resolución de enlaces, política de publicación, caso de uso de build, escritura de salida, comando `build` | Ausente y necesario para V01-A |
| `MediaRef` y adaptador del manifiesto de medios | Pendiente de contrato externo (WEB + CONTENT) |
| `common.yaml` (menú, pie, mensajes) | Pendiente de contrato externo (CONTENT) |
| `media/` (paquete vacío), SEO técnico, sitemap | No necesario todavía |

## VERIFIED CONTRACTS

| Contrato | Evidencia | Resultado | Acción |
|---|---|---|---|
| `inspect_editorial(paths: ProjectPaths, request: EditorialLoadRequest) -> EditorialInspection` | `inspect.signature` y ejecución `es`/`COMPLETE` | Correcto | — |
| `EditorialLoadRequest(locale, policy)` | `model_fields` = `['locale', 'policy']` | Correcto | — |
| `build_editorial_bundle(inspection) -> EditorialBundle` | Ejecución en 4 idiomas; `ValueError` si no es elegible (CONTENT-I18N-02) | Correcto | — |
| `EditorialBundle.get_page/get_sector/get_person(id: str)` | Firmas; `get_page("home")` → `KeyError` | Correcto. **La página es `inicio`, no `home`** | Plan usa `inicio` |
| Inicio H01–H07 | Ids `h01…h07`, `source_block` H01–H07, kinds/purposes reales (HOME MATRIX) | Correcto y en orden | — |
| `load_site_routing(paths) -> SiteRouting` | Ejecución; 9 URL `es` (`/`, `/capacidades/`, `/capacidades/infraestructuras-instalaciones/`…) | Correcto | — |
| Enlaces internos de todo el contenido → URL `es` y anclas existentes | Nueva `test_web_link_resolution.py` | Correcto (Inicio: 14 enlaces, 8 destinos) | Prueba añadida |
| Idiomas no publicados sin URL pública ni fallback | `url(..., "ca"/"en"/"de") is None`; `alternates("inicio") == {"es": "/"}` | Correcto | Prueba añadida |
| `ca`/`en`/`de`: carga e integridad de Inicio | `can_build_bundle=True`, mismos ids H01–H07, títulos traducidos | Correcto, sin contaminación | — |
| Negativos: referencia inexistente, documento inválido, archivo ausente, idioma no soportado | `test_multilingual_content.py`, `test_editorial_loading_b11.py`, `test_routing.py::test_unknown_page_is_an_error` (ya en verde) | Diagnósticos estructurados, sin fallback | NO ACTION |
| Diagnóstico estructurado | `EditorialDiagnostic(code, severity, document_id, source, selector, …)` | Correcto | — |

## FINDINGS

| # | Hallazgo | Clase | Propietario |
|---|---|---|---|
| F1 | `docs/architecture.md` §2 y §8 asignaban todo `application/` y `adapters/` a WEB y no listaban `application/editorial.py` ni `adapters/editorial_files.py` (CONTENT) | **FIXED** | WEB |
| F2 | Ninguna prueba garantizaba que los `InternalLink` editoriales tuvieran URL pública en `SiteRouting` (la integridad solo comprueba el destino editorial) | **FIXED** (prueba de contrato) | WEB |
| F3 | Identificador `inicio` frente a "home" del encargo | NO ACTION | — |
| F4 | `SiteRouting.url()` devuelve `None` para idiomas no publicados: no sirve para enlazar un preview de ca/en/de | WEB-V01-A (solo `es`); decisión D-W2 para después | WEB |
| F5 | No existen adaptador Jinja2, plantillas, CSS, resolución de enlaces, política preview/release, build ni escritura | WEB-V01-A | WEB |
| F6 | `media: None` en todo el modelo; Inicio tiene 5 medios aprobados en D05 sin vía de referencia | **BLOCKER** solo para la fidelidad visual (no para V01-A) | WEB propone `MediaRef`; CONTENT acepta el cambio de modelo |
| F7 | `common.yaml` ausente: sin etiquetas de menú, pie ni mensajes de interfaz | **BLOCKER** para el layout global (V01-B), no para V01-A | CONTENT (desde D03 L50 y 03.K) |
| F8 | `seo.title` / `description` de Inicio nulos (DEC-05) | DEFERRED (bloquea release, no preview) | Dirección / Editorial |
| F9 | H05: tarjetas `sector_preview` solo con `title` (`sections/h05/items` `approval_required`) | NO ACTION técnica; se renderizan tal cual | Editorial |
| F10 | Sin violaciones de frontera: ningún módulo WEB parsea YAML aparte, duplica modelos, resuelve URL fuera de `SiteRouting` ni accede a medios desde `editorial` (`test_architecture` y búsqueda manual) | NO ACTION | — |

## FIXES APPLIED

1. **`docs/architecture.md`, §2 y §8.**
   - *Causa raíz:* la documentación de WEB-G2-00 no se actualizó cuando CONTENT añadió sus módulos en
     `application/` y `adapters/`.
   - *Cambio:* propiedad y responsabilidad de `application/editorial.py` y `adapters/editorial_files.py`, con
     enlace al handoff. No cambia ninguna regla de dependencia.
2. **`tests/integration/test_web_link_resolution.py`** (5 pruebas).
   - Cada página configurada tiene página en el bundle.
   - Todo `InternalLink` de páginas y sectores en idiomas publicados tiene URL y su ancla existe.
   - En idiomas no publicados no hay URL pública y `alternates` solo devuelve idiomas publicados.

No se ha modificado ningún archivo de CONTENT (`editorial/`, `content/`, `application/editorial.py`,
`adapters/editorial_files.py`).

## HOME MATRIX

D05 §23 aprueba la composición Inicio V3 (`maquetas_aprobadas/C04_Inicio_V3_BAFRAS.zip`, `inicio_v3.html`).
Los tokens de la maqueta son `--ink #2A2A2A`, `--muted #4A5550`, `--line #D8D2C3`, `--paper #F7F5F0`,
`--soft #ECE8DD`, `--dark #0E2B25`, `--accent #1A7A5A` y `--max 1180px`. Cortes: 1000, 850, 760, 560 y
360 px. No existe CSS en el repositorio.

| ID | `kind` / `purpose` | Modelo y campos usados | D05 (§20.2 / §23) | Maqueta | Componente Jinja (V01-A) | Medios | Enlaces internos | Pendientes |
|---|---|---|---|---|---|---|---|---|
| h01 | `hero` | `HeroSection`: eyebrow, title, subtitle, paragraphs[1], actions[2] | Hero asimétrico, texto a la izquierda y foto a la derecha | `section.hero` | `components/hero.html` | **R24** → manifiesto `H01`, `assets/images/home/hero/home-hero-engineering.webp`, CC BY 2.0, crédito obligatorio | contacto, capacidades | `sections/h01/media` |
| h02 | `cards` / `capabilities` | `CardsSection`: title, introduction[1], items[3] `CapabilityCard` (title, paragraphs, examples[3], actions[1]), actions[1] | Tres tarjetas iguales con imagen superior | `section#capacidades` | `components/cards.html` (variante `capabilities`) | **R23** `H03` home-cap-infrastructure (CC BY-SA 4.0), **R22** `H04` home-cap-energy (dominio público), **R21** `H05` home-cap-digital (CC BY-SA 4.0) | 3 especialidades, capacidades | 3 × `items/*/media` |
| h03 | `item_list` / `needs` | `ItemListSection`: title, introduction[1], items[4] `NeedItem` (title, paragraphs, actions[1]) | Apertura asimétrica con foto y matriz 2×2 de filas | `section#necesidades` | `components/item_list.html` (variante `needs`) | **R03** → `D02`, `capabilities/digital/instrumentation/digital-industrial-instrumentation.webp`, CC BY-SA 4.0 | 3 especialidades, capacidades | `sections/h03/media` |
| h04 | `process` / `workflow` | `ProcessSection`: title, introduction[1], items[4] `ProcessItem`, closing[1], actions[1] | Cuatro pasos numerados, introducción a dos columnas, sin imagen | `section#filosofia` | `components/process.html` | — | sobre_bafras | — |
| h05 | `cards` / `sector_preview` | `CardsSection`: title, introduction[1], items[4] `SectorPreviewCard` (solo title), actions[1] | Banda verde pino, matriz 2×2, sin imagen | `section#sectores` | `components/cards.html` (variante `sector_preview`) + clase `section--h05` | — | sectores | `sections/h05/items` (approval) |
| h06 | `text` | `TextSection`: title, paragraphs[1], actions[1] | Respiro editorial claro, sin proyectos | `section#experiencia` | `components/text.html` + `section--h06` | — | proyectos_experiencia | — |
| h07 | `text` | `TextSection`: title, paragraphs[1], notes[1] (microcopy), actions[1] | Banda de cierre con CTA prominente | `section#contacto.contactband` | `components/text.html` + `section--h07` | — | contacto | — |

- **Evidencia de la correspondencia R→ID:** tabla de B02_PREP_01 (L62, L80–L83, L290, L308–L311). Los cinco
  archivos de la maqueta son idénticos byte a byte a los de `assets/images/`. Los cinco tienen `alt_es` en
  `media-library/manifests/media-manifest.yaml`.
- **Reutilización:** `hero`, `cards` y `item_list` se usan en INF/ENE/DIG/Capacidades (matriz del handoff §5),
  y `text` en las nueve páginas. Las variantes de Inicio se resuelven con `purpose` o con la clase por
  `section.id`, no con plantillas exclusivas.

### MEDIA: contrato mínimo `MediaRef` (propuesta, no aplicada)

| Campo | Propiedad | Uso |
|---|---|---|
| `asset_id` (p. ej. `H01`) | Referencia editorial (CONTENT, en el YAML) | Clave en el manifiesto |
| `role` (`hero`, `card`, `context`) | Referencia editorial | Selección de variante y recorte |
| `alt` / `decorative` | Editorial (localizable); `alt_es` del manifiesto como origen | Accesibilidad |
| `path`, dimensiones, licencia, autor, `attribution_text`, `status` | Manifiesto (MEDIA, WEB), **no** en el YAML | Resolución, crédito y bloqueo de release si falta autorización |

Para incorporarlo hay que sustituir `media: None` en `HeroSection`, `CapabilityCard`, `CardsSection` e
`ItemListSection`: es un cambio de modelo **de CONTENT**. Release debe fallar si `status != READY` o si falta
el crédito obligatorio. Las imágenes son necesarias para la fidelidad D05 y obligatorias, con crédito, para
publicar (7 de las 9 asignadas son CC BY / BY-SA). En V01-A son opcionales.

### CommonContent: inventario para Inicio y layout

`CommonContent` existe (`navigation_labels`, `footer_texts`, `actions`, `interface_messages`) pero no hay
`common.yaml` en ningún idioma.

| Campo requerido | Uso | Idiomas | Existe | Propietario |
|---|---|---|---|---|
| `navigation_labels`: 6 entradas principales + 3 especialidades | Cabecera y menú móvil | es, ca, en, de | No (texto fuente en D03 L50) | CONTENT |
| `interface_messages`: «Saltar al contenido» y apertura/cierre del menú | Accesibilidad del layout | 4 | No | CONTENT (texto); WEB (uso) |
| `footer_texts`: nombre, contacto y enlaces legales | Pie global | 4 | No (contacto en adenda 03.CO-02; legales pendientes) | CONTENT |
| `actions`: CTA compartido «Contacto» de la cabecera | Botón de cabecera (D05 VIS-020) | 4 | No | CONTENT |
| Etiquetas de preview | Aviso de borrador | Solo interno | No necesarias como copy: texto técnico de WEB | WEB |

Nada de esto bloquea V01-A, cuyo layout no lleva menú ni pie.

## INTEGRATION DECISIONS

**Cerradas** (WEB, aplicables en V01-A; ver plan §3):
1. Contexto de plantilla: `PageContent` + mapa de enlaces resuelto; sin un segundo árbol de modelos.
2. Componente por `kind` con variante por `purpose`; identidad de sección solo como clase CSS; sin
   `compositions.yaml`.
3. Salida de preview en `build/preview/<locale>/<page_id>/`, fuera de `dist/`, con `noindex`, aviso y sin
   canonical ni hreflang.
4. Release exige idioma publicado, URL, `approved` y `seo.title`.
5. Los tipos de enlace no internos fallan explícitamente en V01-A.

**Pendientes:**

| Id | Decisión | Propietario | Necesaria para |
|---|---|---|---|
| D-W1 | Contrato `MediaRef` (propuesta arriba) y cambio de modelo | WEB + CONTENT | Fidelidad visual / V01-B |
| D-W2 | Ruta y enlaces de preview para idiomas no publicados (recomendación: `build/preview/<locale>/<page_id>/` con enlaces por `page_id`, nunca slugs inventados) | WEB | Preview ca/en/de |
| D-W3 | Qué `reason_code` de pendiente bloquea release (recomendación: todos salvo los `integration_pending` que WEB resuelva) | WEB + dirección | Release |
| D-W4 | Creación de `common.yaml` a partir de D03 | CONTENT | Layout global |
| DEC-05 | SEO de Inicio, Capacidades, INF y ENE | Dirección / Editorial | Release |

## VALIDATION

| Comando | Resultado |
|---|---|
| `.venv/Scripts/python -m pytest -q` (inicial) | 573 passed |
| `.venv/Scripts/python -m pytest -q tests/integration/test_web_link_resolution.py` | 5 passed |
| `.venv/Scripts/python -m pytest -q` (final) | **578 passed**, 0 skip |
| `.venv/Scripts/bafras-web doctor` | Resultado: correcto |
| Script de integración en el scratchpad (firmas, Inicio es, 4 idiomas, URL) | Ver VERIFIED CONTRACTS |
| `cmp` de los activos de la maqueta frente a `assets/images/` | 5/5 idénticos |

**Limitaciones:** no he renderizado HTML ni probado en navegador, porque no existe el renderer. Las
licencias de imagen son las que declara el proveedor.

**Diff final:**
- `docs/architecture.md` (modificado);
- `tests/integration/test_web_link_resolution.py`, `docs/project_v02/web/WEB_01_INFORME.md` y
  `docs/project_v02/web/WEB_V01_A_PLAN.md` (nuevos);
- índice `docs/project_v02/README.md`.

Sin commits, sin push y sin dependencias nuevas.

## NEXT ACTION

Implementar el **incremento 1 de WEB-V01-A**: `adapters/jinja.py` + `templates/layouts/base.html`, con
pruebas de autoescape, `StrictUndefined` y plantilla inexistente. Después, los incrementos 2–7 del
[plan](WEB_V01_A_PLAN.md) en orden.
