# WEB-EXPERIENCE-04 V3 · Proyectos y experiencia: cartera BAFRAS, filas de experiencia, créditos e imagen de Automatización

**Fecha:** 21/11/2026. **Rama:** `feat/contingut-v2`, HEAD `9209efc`. Cambios sin commit (ni commit, ni push, ni despliegue).
**Estado:** desarrollo y preview. Publicación **NO-GO**; todos los estados editoriales siguen en `draft`.

## 1. Estado Git

| | Inicial | Final |
|---|---|---|
| Rama / HEAD | `feat/contingut-v2` / `9209efc` | sin cambios |
| Entradas en `git status` | 62 (WEB-EXPERIENCE-03 y trabajo editorial previo, sin commit) | 68 (incluye este informe) |
| Suite | 727 pruebas, todas correctas | 756 pruebas, todas correctas |

No se detectan cambios concurrentes de CONTENT-EXPERIENCE-04: ningún archivo de `content/`, `config/`,
`media-library/` ni `docs/` había cambiado desde el paquete VR04 (09/11) al empezar, ni al editar `common.yaml`.
Ninguna operación destructiva. Los originales multimedia no se han tocado (`assets/images` conserva el mismo estado Git
que al inicio).

## 2. Resumen ejecutivo

- El índice presenta **01 · Proyectos BAFRAS** inmediatamente tras la introducción y **02 · Experiencia profesional**
  con **siete filas uniformes en tres ámbitos**. El mosaico asimétrico de WEB-EXPERIENCE-03 desaparece.
- La cartera está vacía (no hay proyectos aprobados): solo un encabezado discreto, sin tarjetas, enlaces, imágenes,
  controles ni mensaje no aprobado. El carril reutilizable está probado con fixtures internos de 0, 1, 2, 4 y 6 proyectos.
- Las notas bajo las imágenes se corrigen en la causa raíz (MEDIA → presentación): se muestra un crédito breve y
  localizado solo donde la licencia lo exige.
- Automatización y control sustituye D02 («Flow measurement…») por D03 (operadora ante un sinóptico SCADA).
- Las fichas conservan su estructura y soportan el contenido ampliado representable por el contrato vigente.

## 3. Cambios por capa

| Capa | Cambio |
|---|---|
| MEDIA · `media/assets.py`, manifiesto | `ImageCredit` (autor, fuente, licencia, `adapted`) sustituye al volcado de `attribution_text`. D03: autorización declarada (§10.3 de este encargo), SHA-256 y alt ca/en/de |
| SITE · `config/composition.yaml` | `automatizacion_control/ambitos`: D02 → D03 (D02 sigue en Inicio h03) |
| APPLICATION · `presentation.py` | `experience_index_view`: bloques 01/02 por `Experience.kind`. Mensajes condicionales (controles, «adaptada»). El layout informa antes que los textos propios |
| PRESENTATION | `experience_index.html` reescrito (cartera + filas). Macro `credit_text` (también en `cards_capabilities` y en la ficha). CSS de filas y carril con los tokens D05. Carril en `site.js` (JS nativo mínimo) |
| CONTENT (solo interfaz) | `common.yaml` ×4: `experience-portfolio`, `experience-previous-work`, `image-adapted`. Ningún dato de páginas ni de experiencias cambia. Huella ES renovada en `ES_BASELINE_MANIFEST.md` |
| Pruebas | `test_web_experience_04.py` (28 casos) y `experience_fixtures.py` (fixtures en memoria). Adaptación justificada de 2 pruebas del mosaico (WE03) y de los recuentos que cambian con D03 y los enlaces de crédito |
| Docs | [arquitectura](../../architecture.md) (sección WEB-EXPERIENCE-04) y este informe |

## 4. Decisiones arquitectónicas

- **Sin arquitectura paralela.** Una sola fuente: las entradas de `experience_index`. La clasificación sale de
  `Experience.kind` (CONTENT). La selección y el orden se resuelven en APPLICATION/PRESENTATION. No hay condicionales por
  nombre, YAML duplicado ni cambios en modelos editoriales.
- **Un ámbito sin experiencia previa** no se lista en el bloque 02. Sus proyectos BAFRAS aparecen en el bloque 01 con
  el ámbito como categoría.
- **`emphasis`** se conserva en el dato y no altera el tamaño de las filas: no hay regla visual aprobada para un
  tratamiento discreto.
- **Mensajes condicionales:** los controles del carril solo se exigen con dos o más proyectos. Si faltan, el build falla
  con el campo exacto: no hay fallback silencioso.

## 5. Contrato de proyectos BAFRAS y estado del carril

- **Activación:** una entidad `kind: bafras_project` en `content/<idioma>/entities/experiences.yaml`, más su entrada
  en PE-02 dentro del ámbito correspondiente. Ruta, ficha, tarjeta e imagen (por `composition.experiences`) se obtienen
  sin código.
- **Comportamiento:**
  - 0 proyectos: estado vacío.
  - 1 proyecto: tarjeta estática de 760 px, sin controles.
  - 2 proyectos: dos columnas en escritorio, sin controles; en móvil, tarjetas al 86 % con desplazamiento.
  - 3 o más: tres por vista (mínimo 280 px) y desplazamiento propio con `scroll-snap`.
- **Controles:**
  - Solo aparecen si hay desplazamiento efectivo; funcionan con puntero y teclado y tienen nombres accesibles.
  - En los extremos usan `aria-disabled`, de modo que el foco se conserva.
  - Respetan el movimiento reducido. Sin autoplay ni librerías.
  - Sin JS, el carril se desplaza de forma nativa (también con el teclado sobre el carril enfocable).
- **Verificado en navegador:** controles correctos en 7 configuraciones, extremos, puntero, Enter, flechas, foco,
  `scroll-behavior: auto` con movimiento reducido y 0 px de overflow global.

## 6. Notas bajo las imágenes

- **Causa:**
  - `resolve_image` copiaba `attribution_text` en `ResolvedImage.credit`, y la macro `figure` lo imprimía bajo cada
    imagen con licencia.
  - Ese texto es un registro de gestión (`attribution.md`): nombre del archivo original, URL de la licencia,
    «Obra derivada… Recortada y convertida a WebP…».
  - Estaba escrito solo en español y se mostraba en los cuatro idiomas.
- **Corrección:**
  - Crédito estructurado, por ejemplo «Steve Jurvetson from Los Altos, USA / Wikimedia Commons · CC BY 2.0 ·
    adaptada», con la fuente y la licencia enlazadas, tal como recomiendan `attribution.md` y DEC-10.
  - Solo aparece con `attribution_required` (CC BY/BY-SA).
  - «adaptada» es un texto de interfaz por idioma y solo se muestra si el derivado cambia las dimensiones del original.
  - El registro completo sigue en el manifiesto y en `attribution.md`.
- **Comprobado:**
  - En las 64 páginas no aparece ningún `attribution_text`.
  - Todas las atribuciones obligatorias se conservan, con autor y licencia.
  - Los textos alternativos están intactos.
  - Inicio, Sistemas energéticos y Automatización se acortan entre 42 y 215 px.
- **Pendiente DEC-10:** el título de la obra no se muestra (la fuente enlazada lo contiene) y la página «Créditos de
  imágenes» no está implementada. La decisión sobre ubicación de créditos sigue abierta.

## 7. Imagen de Automatización y control

| | Activo | Decisión |
|---|---|---|
| Sustituida | D02 `digital-industrial-instrumentation.webp` («Flow measurement with dP cell», CC BY-SA) | Retirada de `ambitos` |
| **Seleccionada** | **D03** `digital-scada-screen.webp`: operadora ante el sinóptico SCADA de una planta de agua (USDA, dominio público, 1600×1200, 110 KB) | Corresponde a «Del dato al control». Derivado WebP existente reutilizado; no requiere crédito |
| Descartada | D04: panel BMS | Válida, pero muestra el rostro de una persona identificable |
| Descartada | `instrumentación 1 valvula.HEIC` (propia) | Decodificada con libheif 1.23 en un entorno temporal: válvulas de mariposa manuales en un rack de tuberías. Es instalación hidráulica, no automatización |
| Descartada | D05 | Estado `NOT_FOUND` |

D02 sigue en Inicio h03, que está fuera del alcance de §11. Si la objeción es al activo en sí, se requiere una decisión
visual.

## 8. Edge AI

- No existe en el repositorio la primera página auténtica del artículo (DOI 10.1016/j.asoc.2025.114175).
- Se mantiene la fila sin imagen: el texto se reparte en dos columnas, con filete verde y sin marcador.
- La ficha no tiene imagen principal. El enlace DOI editorial ya existía.
- **Integración científica no completada:** depende de CONTENT. Cuando llegue el recurso, basta con un activo MEDIA y
  `experiences.edge-ai-investigacion: {main: …}`; no hay lógica específica de Edge AI.

## 9. Fichas y compatibilidad con CONTENT-EXPERIENCE-04

- La estructura no cambia: hero, imagen, contexto, ficha técnica, módulos, enlaces, galería y retorno.
- Solo se añade el crédito de imagen cuando la licencia lo exige. Ninguna imagen de experiencia actual lo requiere.
- **Contrato vigente:**
  - `context` e `intervention`: párrafos.
  - `systems`, `phases` y `deliverables`: listas.
  - `results`: resultados con evidencias internas.
  - `key_figures`: magnitudes.
  - `links`: enlaces externos.
- **Fixtures probados en es/ca/en/de:**
  - Contenido: 3 párrafos de contexto, 9 sistemas, 7 fases, 6 entregables, 8 magnitudes, 2 resultados y 4 enlaces.
  - Casos: alemán con compuestos largos y módulos ausentes.
  - Resultado: sin encabezados vacíos ni duplicados, sin solapamientos y sin texto recortado.

| Necesidad (encargo §8.1) | Campo existente | Limitación | Cambio mínimo propuesto | Responsable |
|---|---|---|---|---|
| Tecnologías | — (`systems` como aproximación) | No hay lista diferenciada | `technologies: list[TextItem]` y módulo opcional | CONTENT (modelo) + WEB (módulo) |
| Retos | — | No representable | `challenges: list[Paragraph]` y módulo opcional | CONTENT + WEB |
| Evidencias públicas | `evidence_refs` (internas) | No se publican | Enlaces en `links` o un campo público de evidencias | CONTENT |
| Módulos con subtítulo y párrafos | — | Las listas son de texto plano | Solo si CONTENT lo define | CONTENT + WEB |

## 10. Builds, suite y QA

- **Builds:**
  - `python -m bafras_web build --locale <es|ca|en|de> --all --mode preview --build-root build/we04r`
  - 16 páginas por idioma, 64 HTML y 25 recursos (24 + D03).
  - El árbol completo valida sin destinos ausentes.
- **Suite:** 756 pruebas, todas correctas (`build/visual-review-we04/pytest-full.txt`).
  - Pruebas nuevas en `tests/integration/test_web_experience_04.py` (28) y `tests/unit/test_media_layout.py` (1).
  - Ninguna prueba se ha relajado. Las adaptaciones siguen al cambio de diseño o de recuento (§3).
- **Release:** sin cambios. Los estados `draft`, los gates y la política SEO están intactos, y ca/en/de siguen sin
  publicar.
- **QA de navegador** (`build/qa-tools/we04_browser_qa.py`, Chrome 157, servidor HTTP local):
  - 280 comprobaciones de página: las 16 páginas es, más el índice y las 7 fichas en ca, en y de, en 7 anchos (1440,
    1280, 1024, 768, 390, 375 y 320 px).
  - 56 comprobaciones de fixtures.
  - Resultado: 0 errores JS, 0 imágenes rotas, 0 overflow global, un h1 por página, sin enlaces anidados ni ids
    duplicados, sin solapamientos y sin texto recortado.
  - Las imágenes de las filas quedan a la izquierda en escritorio y arriba en móvil.
  - Teclado: 12 enlaces de fila con foco visible.
- **Incidencia preexistente, fuera de alcance:**
  - Entre unos 761 y 800 px, el logotipo de cabecera se estrecha a 148×34 en lugar de 158×34.
  - Es idéntico en la preview VR04 anterior. La cabecera compartida no se ha modificado.
  - Corrección propuesta: `flex-shrink: 0` en `.brand__logo`.
- **No hay auditoría WCAG completa.**

## 11. Evidencias visuales

En `build/visual-review-we04/` (fuera de Git) y en `BAFRAS_WEB_EXPERIENCE_04_REVISION_VISUAL.zip`:
- **32 capturas completas ES** (1440×900 y 390×844, 32/32 correctas), con `manifest.json` y `qa-summary.md`.
- **19 capturas específicas:**
  - bloque 01 vacío y los tres ámbitos, a 1440 y 390 px;
  - carril con 1, 2 y 4 proyectos;
  - índice con 4 proyectos;
  - fichas ampliadas (de/Dogger Bank A y es/Edge AI).
- Los archivos `fixture-*` contienen datos de prueba, no contenido editorial.
- La ficha Edge AI y la página de Automatización figuran en las 32 capturas (`16-edge-ai`, `05-automatizacion-control`).

**Comparación con VR04:** el mosaico ha desaparecido y el índice pasa de 5151 a 5065 px en escritorio y de 6822 a
7113 px en móvil. Las siete fichas, Capacidades, Infraestructuras, Sectores, Sobre BAFRAS y Contacto conservan la misma
altura. Inicio, Sistemas energéticos y Automatización solo se acortan por los créditos.

## 12. Dependencias editoriales (CONTENT / LOCALIZATION)

| Dependencia | Estado |
|---|---|
| Mensaje del estado vacío `experience-portfolio-empty` (propuesta V2 provisional, no aprobada) | No implementado como texto. Se mostrará automáticamente en cada idioma en que CONTENT lo aporte |
| Etiquetas `experience-portfolio-previous/next` del carril | Necesarias con el primer par de proyectos reales; el build lo indica |
| Validación nativa ca/en/de de las 3 claves nuevas y del alt de D03 | Propuestas draft |
| Literal de los encabezados de bloque | «Proyectos BAFRAS» y «Experiencia profesional» (estructura V2, a partir de las etiquetas canónicas D03 «Proyecto BAFRAS» / «Experiencia profesional del equipo»). Confirmación editorial |
| Primera página del artículo Edge AI | Recurso ausente |
| Campos de tecnologías, retos y evidencias públicas | §9 |

## 13. Desviaciones y riesgos

- `common.yaml` (CONTENT) recibe 3 textos de interfaz, siguiendo el precedente de WEB-EXPERIENCE-03. No había cambios
  concurrentes. Si CONTENT-EXPERIENCE-04 modifica el archivo, debe conservar estas claves.
- La autorización de D03 se registra con la referencia de este encargo (§10.3: recursos del repositorio autorizados).
- La biblioteca `pillow-heif` solo se usó en un directorio temporal para inspeccionar el HEIC. No es una dependencia
  del proyecto.
- Riesgos heredados (WE03 §6): permisos de `build/preview`, DEC-10 (logotipo), separación futura de commits CONTENT/WEB.

## 14. Dictamen

- **GO técnico:** implementación verificable, cuatro idiomas generados, suite y QA de navegador sin regresiones y sin
  bloqueos críticos.
- **GO para revisión humana:** paquete visual completo.
- **GO de publicación:** **no autorizado** por esta intervención (estados `draft`, dependencias de §12, DEC-10, release).
