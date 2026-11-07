# CONTENT → WEB · Handoff del sistema editorial

Fecha: 07/11/2026 · Intervención CONTENT-I18N-02 · Rama `feat/contingut-v2`, HEAD `fca65e8`
(el trabajo CONTENT sigue sin commit). Verificación de esta entrega:
[CONTENT_I18N_02](../quality/CONTENT_I18N_02.md).

## 1. Propósito y alcance

CONTENT entrega contenido editorial tipado y validado de las nueve páginas en `es`, `ca`, `en` y `de`, y una
API Python para obtenerlo como un `EditorialBundle` por idioma. WEB lo usa para generar el HTML. **WEB no lee
los YAML directamente ni reimplementa su validación**: consume modelos Pydantic ya validados.

No forma parte de esta entrega: HTML, componentes, CSS, URLs, selector de idioma, SEO técnico, medios ni
publicación.

## 2. Estado de implementación

| Capacidad | Estado |
|---|---|
| Modelos editoriales (páginas, 9 tipos de sección, tarjetas, entidades, referencias, pendientes, revisión) | Implementado y probado |
| Carga por idioma con descubrimiento acotado y YAML estricto (sin claves duplicadas) | Implementado y probado |
| Inspección, integridad referencial y elegibilidad del bundle (INCREMENTAL / COMPLETE) | Implementado y probado |
| Contenido `es` (baseline A6) y `ca`/`en`/`de` (11 YAML cada uno) | Válido; todo en revisión **draft** |
| Paridad estructural de traducciones con `es` | Probado (`tests/integration/test_multilingual_content.py`) |
| `CommonContent` (menú, pie, mensajes de interfaz, acciones compartidas) | Modelo implementado; **sin datos**: no existe `common.yaml` |
| `Experience`, `DownloadableResource` | Modelos implementados; **sin datos** (sin experiencias verificadas ni catálogos PDF) |
| Referencias a medios | **No implementado**: todos los campos `media` y `portrait` son `None` hasta que WEB defina `MediaRef` |
| Seguimiento de vigencia de traducciones (huellas, `stale`) | No implementado (propuesta en ARCH-CONTENT-DISCOVERY-01) |
| Comandos CLI de contenido (`content validate/status`) | No implementados; el CLI solo tiene `doctor` |

## 3. Arquitectura editorial

| Módulo | Responsabilidad |
|---|---|
| `bafras_web.editorial` (`__init__`) | API pública de modelos: re-exporta páginas, secciones, entidades, referencias y primitivas |
| `editorial/primitives.py` | `EditorialModel` (estricto, `extra="forbid"`, congelado), `Paragraph`, `TextItem`, `EditorialReview`, `PendingField`, `Verification` |
| `editorial/sections.py` | Unión discriminada `Section` (9 tipos) y sus tarjetas e ítems |
| `editorial/references.py` | Destinos semánticos sin resolver: `InternalLink`, `ExternalLink`, `ContactLink`, `ResourceLink`; `CallToAction`, `SharedActionRef` |
| `editorial/entities.py` | `Person`, `Sector` (6 `SectorId` canónicos), `Experience`, `DownloadableResource` |
| `editorial/pages.py` | `PageContent`, `SeoMeta`, `CommonContent`, `EditorialBundle` |
| `editorial/inspection.py` | Inventario por idioma, diagnósticos y política de completitud |
| `editorial/integrity.py` | `assess_integrity`, `build_editorial_bundle` |
| `editorial/pending.py` | Validación de selectores de pendiente (sin aprobar ni publicar) |
| `adapters/yaml_files.py` | Único cargador YAML del proyecto (`SafeLoader` estricto) |
| `adapters/editorial_files.py` | Descubrimiento de archivos limitado a `content/<idioma>/` |
| `application/editorial.py` | Caso de uso `inspect_editorial` |
| `application/configuration.py` | `load_site_routing` (idiomas y rutas, propiedad de WEB) |

El dominio `editorial` no importa YAML, Jinja2 ni el sistema de archivos (lo comprueba
`tests/contracts/test_architecture.py`).

## 4. Inventario multilingüe

| Idioma | Páginas | Catálogos | Configurado | Publicado (`config/locales.yaml`) | Slugs (`config/routes.yaml`) |
|---|---:|---:|---|---|---|
| es | 9 | 2 | sí | **sí** | sí |
| ca | 9 | 2 | sí | no | no |
| en | 9 | 2 | sí | no | no |
| de | 9 | 2 | sí | no | no |

Cada idioma tiene `content/<idioma>/pages/{inicio, capacidades, infraestructuras, sistemas_energeticos,
automatizacion_control, sectores, proyectos_experiencia, sobre_bafras, contacto}.yaml` y
`entities/{sectors, people}.yaml`. El idioma **no** figura dentro de los YAML: lo aporta el contexto de carga.

## 5. Modelos y tipos de sección

Todas las secciones tienen `id` (estable e idéntico en los cuatro idiomas), `kind` (discriminador) y
`source_block` (procedencia D03, puede ser `None`). Los textos son `str` sin HTML ni Markdown: hay que
escaparlos al renderizar. Los párrafos son listas de `Paragraph(id, text)`.

| `kind` | Modelo | Campos de contenido | Referencias |
|---|---|---|---|
| `hero` | `HeroSection` | `title`; opcionales `eyebrow`, `subtitle`, `attribution`; `paragraphs`, `actions` | Acciones; `media` siempre `None` |
| `text` | `TextSection` | `title?`, `paragraphs`, `notes`, `actions`, `contact_channels` (`ContactChannel(id, label, target, value)`) | Acciones; `ContactLink` email/phone |
| `cards` | `CardsSection` | `purpose`, `eyebrow?`, `title`, `introduction`, `items`, `transversal?` (`EditorialAside`, solo `technical_areas`), `closing`, `actions` | Según tarjeta |
| `item_list` | `ItemListSection` | `purpose` (`needs` / `deliverables` / `modalities`), `title`, `introduction`, `items`, `notes` | `NeedItem.actions` |
| `process` | `ProcessSection` | `purpose` (`workflow` / `principles`), `title`, `introduction`, `items` (`ProcessItem`), `closing`, `actions` | Acciones |
| `sector_index` | `SectorIndexSection` | `title`, `introduction`, `sector_refs` | → `bundle.sectors` |
| `experience_index` | `ExperienceIndexSection` | `title`, `introduction`, `groups[].title/introduction/entries` | → `bundle.experiences` (hoy 0 entradas) |
| `team` | `TeamSection` | `title`, `introduction`, `corporate_presentation`, `person_refs` | → `bundle.people` |
| `form` | `ContactFormSection` | `title`, `fields` (`FormField(id, label, required, help, placeholder)`), `help`, `submit_label`, `messages.success/error`, `privacy_text?` | Ninguna |

Tarjetas de `cards`, con discriminador `kind` y `purpose` correspondiente:

| `purpose` | Tarjeta | Campos |
|---|---|---|
| `capabilities` | `CapabilityCard` | `title`, `paragraphs`, `examples`, `actions` (≥1) |
| `technical_areas` | `TechnicalAreaCard` | `title`, `paragraphs`, `included`, `tags` |
| `application_examples` | `ApplicationExampleCard` | `title`, `description`, `disciplines` (CTA internos). Ejemplos **hipotéticos** (D03, D05) |
| `sector_preview` | `SectorPreviewCard` | `title`, `paragraphs`, `action?` |
| `discipline_relations` | `DisciplineRelationCard` | `title`, `description`, `discipline` (`InternalLink`) |

Una acción (`Action`) es un `CallToAction(id, label, target)` o un `SharedActionRef(id, common_ref)`. El
contenido actual solo usa `CallToAction`. `target` es `InternalLink(page_id, section_id?)`,
`ContactLink(channel)`, `ExternalLink(url)` o `ResourceLink(catalog_id)`.

**Matriz de cobertura** (contenido real, idéntica en los cuatro idiomas):

| `kind` | Instancias | Páginas | Dependencias |
|---|---:|---|---|
| `text` | 20 | las nueve | 2 `ContactLink` en `contacto/co-03` |
| `hero` | 9 | una por página (invariante del modelo) | Medios pendientes en 5 páginas |
| `cards` | 8 | inicio (capabilities, sector_preview), capacidades (capabilities, application_examples), INF/ENE/DIG (technical_areas), DIG (discipline_relations) | — |
| `item_list` | 8 | needs ×4 (inicio, INF, ENE, DIG), deliverables ×3 (INF, ENE, DIG), modalities ×1 (capacidades) | — |
| `process` | 2 | inicio (`workflow`), sobre_bafras (`principles`) | — |
| `sector_index` | 1 | sectores | 6 sectores |
| `experience_index` | 1 | proyectos_experiencia | 3 grupos sin entradas |
| `team` | 1 | sobre_bafras | 3 personas |
| `form` | 1 | contacto | `privacy_text` pendiente |

Referencias resueltas por idioma: 73 (58 enlaces internos de página, 6 `sector_refs`, 3 `person_refs` y
6 acciones contextuales de sector).

## 6. Interfaces públicas

Estas son las firmas verificadas en el código. Cualquier otra función es interna.

| Interfaz | Firma / uso |
|---|---|
| `bafras_web.adapters.filesystem.ProjectPaths` | `ProjectPaths(root: Path)`; `.content`, `.config`, `.locales_file`, `.routes_file` |
| `bafras_web.adapters.filesystem.find_project_root` | `(start: Path) -> Path \| None` |
| `bafras_web.application.configuration.load_site_routing` | `(paths) -> SiteRouting`; lanza `ConfigurationError(problems: list[str])` |
| `SiteRouting` (WEB) | `.locales` (`LocaleSettings`: `codes`, `published_codes`, `default_locale`), `.routes`, `.url(page_id, locale) -> str \| None`, `.alternates(page_id) -> dict[str, str]` |
| `bafras_web.application.editorial.EditorialLoadRequest` | `EditorialLoadRequest(locale: str, policy: "INCREMENTAL" \| "COMPLETE")` |
| `bafras_web.application.editorial.inspect_editorial` | `(paths, request) -> EditorialInspection`. No lanza errores por contenido: los devuelve como diagnósticos. Propaga `ConfigurationError` |
| `EditorialInspection` | `.locale`, `.policy`, `.documents`, `.diagnostics`, `.valid_pages`, `.missing_page_ids`, `.invalid_page_ids`, `.documents_complete`, `.has_errors`, `.can_build_bundle` |
| `EditorialDiagnostic` | `.code`, `.severity` (`error` / `warning` / `info`), `.message`, `.document_id`, `.source` (relativa a `content/`), `.selector`, `.target_id`, `.reference_status`, `.reason_code` |
| `bafras_web.editorial.integrity.build_editorial_bundle` | `(inspection) -> EditorialBundle`; `ValueError` si `can_build_bundle` es falso |
| `bafras_web.editorial.integrity.assess_integrity` | `(documents, expected_page_ids, *, report_resolved=False) -> IntegrityResult`. Diagnóstico; WEB no lo necesita para construir |
| `EditorialBundle` | `.locale`, `.pages`, `.common`, `.people`, `.sectors`, `.experiences`, `.resources`; `get_page`, `get_common`, `get_person`, `get_sector`, `get_experience`, `get_resource` (lanzan `KeyError`) |
| Modelos | `from bafras_web.editorial import …`: ver `__all__` en `editorial/__init__.py` |

**Políticas:**
- `COMPLETE`: un documento requerido ausente es error.
- `INCREMENTAL`: un documento requerido ausente es aviso.
- En ambas, `can_build_bundle` exige las nueve páginas válidas, los catálogos requeridos válidos y ningún
  error. Por tanto, **INCREMENTAL sirve para diagnosticar, pero no permite construir un bundle parcial**.

**Selección de idioma:**
- El idioma debe estar en `config/locales.yaml`. Si no lo está: diagnóstico `LOCALE_UNKNOWN` y ningún
  archivo leído.
- No hay idioma por defecto implícito ni fallback: un archivo ausente en `ca` no se sustituye por `es`.
- `inspect_editorial` **no** comprueba `published`: eso corresponde a la publicación (WEB).

## 7. Ejemplo de integración

Ejecutado literalmente desde la raíz del checkout (`.venv/Scripts/python`), con resultado correcto: hero y
seis sectores en catalán, y `'/contacto/' None`.

```python
from pathlib import Path

from bafras_web.adapters.filesystem import ProjectPaths, find_project_root
from bafras_web.application.configuration import load_site_routing
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial import CardsSection, HeroSection, InternalLink, SectorIndexSection
from bafras_web.editorial.integrity import build_editorial_bundle

paths = ProjectPaths(find_project_root(Path.cwd()))
routing = load_site_routing(paths)                       # ConfigurationError si config/ es inválida

locale = "ca"                                            # idioma explícito; sin fallback
inspection = inspect_editorial(paths, EditorialLoadRequest(locale=locale, policy="COMPLETE"))
if not inspection.can_build_bundle:
    for d in inspection.diagnostics:
        if d.severity == "error":
            print(d.code, d.source, d.selector, d.message)
    raise SystemExit(1)
bundle = build_editorial_bundle(inspection)              # EditorialBundle(locale="ca")

page = bundle.get_page("sectores")                       # KeyError si el page_id no existe
for section in page.sections:                            # orden editorial
    match section:                                       # el discriminador es section.kind
        case HeroSection():
            print("hero:", section.title)
        case SectorIndexSection():
            for sector_id in section.sector_refs:        # referencia → catálogo del mismo bundle
                print("  sector:", bundle.get_sector(sector_id).title)
        case CardsSection():
            print("cards:", section.purpose, len(section.items))
        case _:
            print(section.kind, section.id)

# Un enlace interno es una identidad editorial; la URL la resuelve WEB con config/routes.yaml.
target = InternalLink(page_id="contacto")
print(routing.url(target.page_id, "es"), routing.url(target.page_id, locale))  # '/contacto/' y None (ca sin publicar ni slug)
print("review:", page.review.status, "| pending:", [p.field for p in page.pending])
```

## 8. Bundles

`build_editorial_bundle` agrupa, para **un** idioma:
- las nueve `PageContent`, en orden alfabético de `page_id`; el orden de navegación es el de `config/routes.yaml`;
- `common`: vacío, porque no existe `common.yaml`;
- `people` (3: Murti, Àngel, Amin, en ese orden);
- `sectors` (6, en orden canónico);
- `experiences` y `resources`: 0.

Cada llamada crea objetos nuevos. Los modelos son congelados, pero sus listas no son inmutables en
profundidad: WEB no debe mutarlas.

La serialización `model_dump(mode="json")` con claves ordenadas es determinista. Huellas observadas:

| Idioma | SHA-256 del bundle (`COMPLETE` = `INCREMENTAL`) |
|---|---|
| es | `725e0f2326f9e723…` (igual al [manifiesto ES](../quality/ES_BASELINE_MANIFEST.md)) |
| ca | `9d2c0f86c93e772f…` |
| en | `d7959a95c75dce24…` |
| de | `538ffc5eb055c998…` |

## 9. Navegación y referencias

**Identidades de página** (`page_id` = nombre de archivo = clave de `config/routes.yaml`):

| `page_id` | Secciones (orden) | Destinos internos | Pendientes |
|---|---|---|---|
| inicio | h01 hero · h02 cards/capabilities · h03 item_list/needs · h04 process/workflow · h05 cards/sector_preview · h06 text · h07 text | capacidades, 3 especialidades, sobre_bafras, sectores, proyectos_experiencia, contacto | SEO ×2, H05, medios ×5 |
| capacidades | c01 hero · especialidades cards/capabilities · c03 cards/application_examples · c04 item_list/modalities · c05 text | `capacidades#especialidades`, 3 especialidades, contacto, proyectos_experiencia | SEO ×2 |
| infraestructuras | inf-01 hero · necesidades · ambitos cards/technical_areas · entregables · integracion text · inf-06 · inf-07 | `#ambitos`, ENE, DIG, proyectos_experiencia, contacto | SEO ×2, medio |
| sistemas_energeticos | ene-01 hero · necesidades · ambitos · entregables · integracion text · ene-06 · ene-07 | `#ambitos`, INF, DIG, proyectos_experiencia, contacto | SEO ×2, medios ×2 |
| automatizacion_control | dig-w01 hero · necesidades · ambitos · entregables · integracion cards/discipline_relations · dig-w06 · dig-w07 | `#ambitos`, INF, ENE, proyectos_experiencia, contacto | medios ×2 |
| sectores | sec-01 hero · sectores sector_index · sec-03 · sec-04 · sec-05 | `sectores#sectores`, capacidades, sobre_bafras, contacto | — |
| proyectos_experiencia | pe-01 hero · pe-02 experience_index · pe-03 · pe-04 | capacidades, contacto | SEO description, entradas PE |
| sobre_bafras | sb-01 hero · sb-02 team · sb-03 process/principles · sb-04 · sb-05 | proyectos_experiencia, capacidades, contacto | — |
| contacto | co-01 hero · co-02 form · co-03 text (email, teléfono) · co-04 | — | `privacy_text` |

- `InternalLink.section_id` es el `id` de una sección de la página destino. Sirve de **ancla** estable (p. ej.
  `ambitos`), y la integridad comprueba que exista.
- La URL y el fragmento HTML los construye WEB. Ningún `page_id`, nombre de archivo ni `id` es una URL.
- No hay contrato de navegación global en CONTENT: la estructura del menú es configuración WEB
  (`config/routes.yaml` con `parent`), y las etiquetas del menú (`CommonContent.navigation_labels`) no
  existen todavía.

## 10. Estados y pendientes

- **`review.status`:** las nueve páginas y las tres personas, en los cuatro idiomas, están en `draft`. Draft
  permite desarrollar y previsualizar, **no** publicar. Que una traducción exista no la aprueba.
- **`PendingField(field, reason_code, source_ref)`:** 22 por idioma, con selectores estables idénticos entre
  idiomas:
  - `approval_required`: SEO de Inicio, Capacidades, INF y ENE, y selección H05;
  - `integration_pending`: medios;
  - `source_missing`: SEO description de PE y privacidad de Contacto;
  - `verification_required`: entradas PE.
- **Personas:** 6 pendientes (grafía pública y consentimiento, biografía). Se informan como aviso
  `ENTITY_PENDING_UNCHECKED`, porque el sistema no resuelve todavía selectores de entidad.
- **Valores `null`:** un campo `null` con pendiente declarado significa "dato no aprobado". WEB no lo
  rellena ni lo deduce de otro campo. Por ejemplo, un `seo.title` nulo no se sustituye por el `title` del hero
  sin decisión de DEC-05.
- **Medios:** el texto no cambia hasta que WEB y CONTENT acuerden `MediaRef` y se sustituya `media: None` en
  el dominio. La composición sin imagen debe funcionar.
- **Severidades:**
  - `error` impide el bundle;
  - `warning` informa sin bloquear el bundle;
  - `info` registra hechos (pendientes, contactos no comprobados).

## 11. Matriz de responsabilidades

| Materia | CONTENT | WEB | Revisión humana / dirección |
|---|---|---|---|
| YAML, modelos, validación, integridad, bundle | Responsable | Consumidor; no duplica validación | — |
| Tipos de sección | Define datos | Implementa un componente por `kind`/`purpose` | D05 para composición |
| Textos y traducciones | Mantiene fuente | Renderiza sin alterar; escapa HTML | Revisión lingüística y técnica por idioma |
| Idioma | Carga explícita por código | `published`, selector, `lang`, hreflang | DEC-14 |
| Rutas, slugs, URLs, anclas HTML | Identidades `page_id` / `section_id` | `config/routes.yaml`, `SiteRouting` | DEC-16; slugs ca/en/de |
| Menú y pie | Etiquetas (pendientes) | Estructura y presentación | — |
| Medios | Referencia editorial (pendiente) | `MediaRef`, manifiesto, derechos, alt técnico | Licencias |
| SEO | `title` / `description` | canonical, hreflang, sitemap, OG | DEC-05 |
| Formulario | Etiquetas y mensajes | Estados, envío desactivado, accesibilidad | DEC-11, privacidad |
| Accesibilidad | Semántica disponible (jerarquía, `required`) | Implementación WCAG | — |
| Publicación | Estados `review` y pendientes | No publica `draft` ni idiomas no publicados | Aprobación expresa |

## 12. Dependencias de WEB

1. Un componente Jinja2 por `kind` y por `purpose` de `cards`, `item_list` y `process` (§5).
2. Resolución de `InternalLink` → URL y ancla mediante `SiteRouting`; `ContactLink` → `mailto:` / `tel:` con
   los datos de `ContactChannel.value` o de la configuración del sitio (D04 §13).
3. Slugs ca/en/de en `config/routes.yaml` antes de publicar esos idiomas (hoy `url()` devuelve `None`).
4. Contrato `MediaRef` acordado con CONTENT, y adaptador del manifiesto de medios.
5. Menú y pie: mientras no exista `common.yaml`, WEB **no** inventa etiquetas. Se acuerda con CONTENT la
   creación de `common.yaml` (CONTENT) a partir de D03.
6. Gating de publicación: modo preview con draft visible; modo release solo con idioma publicado,
   `review.status` aprobado y sin pendientes bloqueantes.
7. SEO técnico, selector de idioma, responsive, estados del formulario y accesibilidad (D05, acta G1).

## 13. Pruebas y garantías

**Comprobado (573 pruebas, 0 skip):**
- validación Pydantic y estricta de los 44 YAML;
- paridad estructural ca/en/de con es (IDs, discriminadores, orden, cardinalidad, referencias, estados,
  pendientes, contactos, booleanos);
- perfil de diagnósticos idéntico a es en cada idioma y política;
- bundle que procede de los archivos del idioma pedido;
- carga intercalada sin contaminación y con huellas estables;
- huella ES igual al manifiesto;
- archivo ausente, documento inválido, referencia rota e idioma no soportado, sin fallback;
- reglas de dependencia de la arquitectura.

**No comprobado:**
- calidad, fidelidad o terminología de las traducciones: no hay registro de revisión humana ni informe
  I18N-01 en el repositorio;
- literalidad de ca/en/de frente a D03 (solo existe para es);
- operatividad de email y teléfono;
- derechos de medios;
- HTML.

## 14. Riesgos y condiciones

- **El trabajo CONTENT no está confirmado en Git** (código, 44 YAML y documentación sin seguimiento). Hay que
  hacer commit antes de que WEB construya encima.
- Las traducciones son válidas técnicamente, pero no están revisadas. Su procedencia (traducción por IA
  externa, según el contrato de localización) no está documentada en el repositorio.
- No hay detección de vigencia: un cambio en es no marca las traducciones como desactualizadas. La paridad
  estructural sí se rompe ante cambios de estructura, porque la prueba falla.
- `common.yaml` ausente: no hay textos aprobados para el menú, el pie ni los mensajes de interfaz.
- `PageIdentity` admite `_`, pero `EditorialId` no: los `page_id` y los `id` de sección siguen convenciones
  distintas.

## 15. Fuentes documentales

[D03 V1.22 y addenda](../../03_contenido_editorial_V1_22_baseline_G1.md) ·
[D04 V2.4](../../04_arquitectura_software_V2_4_handoff_G1.md) ·
[D05 V4.12](../../05_sistema_visual_V4_12_baseline_G1.md) ·
[Decisiones WEB-G1 / DEC-05](../../WEB_G1_CLOSE_DECISIONES.md) ·
[Arquitectura del repositorio](../../../architecture.md) ·
[Contrato de localización](../localization/LOCALIZATION_CONTRACT.md) ·
[Terminología ES](../localization/TERMINOLOGY_ES.md) ·
[Manifiesto ES](../quality/ES_BASELINE_MANIFEST.md) ·
[A6](../quality/CONTENT_ES_01_A6.md) ·
[B1.1: inspección e integridad](../foundation/CONTENT_ES_01_B1_1.md) ·
[Informe CONTENT-I18N-02](../quality/CONTENT_I18N_02.md)

## 16. Criterios de aceptación WEB

1. Consume el contenido solo a través de `inspect_editorial` + `build_editorial_bundle`. No lee YAML ni
   duplica modelos.
2. Construye únicamente cuando `can_build_bundle` es verdadero y muestra los diagnósticos `error` en otro caso.
3. Pide el idioma de forma explícita y no implementa fallback entre idiomas.
4. Respeta el orden de `sections` y de las colecciones. Selecciona el componente por `kind`/`purpose`; un
   `kind` desconocido es error de build, no se omite.
5. Escapa todos los textos. No altera, resume ni completa copy, y deja intactos `null` y listas vacías.
6. Resuelve URLs y anclas solo con `SiteRouting` y las identidades editoriales.
7. No publica `draft`, idiomas con `published: false` ni contenido con pendientes que bloqueen la publicación.
8. Renderiza `application_examples` como hipotéticos y las experiencias con su etiqueta de atribución
   (adenda 03.G1-02).
9. Sus pruebas cubren al menos un idioma traducido además de `es`.
