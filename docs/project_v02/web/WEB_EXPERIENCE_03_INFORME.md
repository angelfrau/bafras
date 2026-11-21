# WEB-EXPERIENCE-03 V2 · Proyectos y experiencia, fichas y generación multilingüe

**Fecha:** 09/11/2026. **Rama:** `feat/contingut-v2`, HEAD `9209efc`. Cambios sin commit.
**Estado:** desarrollo y preview. Publicación no autorizada; todo el contenido sigue en `draft`.

## 1. Resumen ejecutivo

La vertical Proyectos y experiencia funciona en preview en los cuatro idiomas:
- un índice con siete experiencias reales en tres ámbitos, con jerarquía tomada de `emphasis` e imágenes reales;
- siete fichas generadas con una sola plantilla;
- rutas localizadas;
- el logotipo oficial en cabecera y pie.

Cada idioma se genera por separado y conserva los demás. Resultado: 64 páginas HTML y 24 recursos. Dos generaciones
completas en limpio producen los mismos 88 archivos, byte a byte.

La suite completa pasa. El QA de navegador no detecta errores de consola, imágenes rotas ni desbordamiento
horizontal, y la navegación índice → ficha → índice funciona en 7/7 casos.

**Dictamen: GO para revisión humana** (§8).

## 2. Cambios por capa

| Capa | Cambio |
|---|---|
| SITE · `site/routes.py`, `config/routes.yaml` | `entities.experience` (ficha = URL del índice + id estable). `for_preview()` resuelve idiomas no publicados solo en preview; release no cambia. Slugs ca/en/de propuestos. |
| SITE · `site/composition.py`, `config/composition.yaml` | `experiences.<id>: {main, gallery}`, validado contra el bundle. PE-03 en banda arena (C04-PE). |
| SITE · `site/publication.py`, `site/links.py` | Bloqueos de release para fichas (idioma publicado, `approved`). Resolución de enlaces de `Experience`. |
| MEDIA · `media/assets.py`, manifiesto | Texto alternativo por idioma (`alt_ca/en/de`), sin fallback. X01–X03 completados con material real; X04–X11 nuevos; alt ca/en/de para los 9 activos ya compuestos. |
| APPLICATION · `build.py`, `presentation.py` | Modo preview explícito, fichas (`render_experience`), imágenes de experiencias verificadas (tamaño y SHA-256), conservación de otros idiomas, contexto de ficha y selector de idioma. |
| ADAPTERS · `build_output.py`, `cli.py` | `preserve` traslada el HTML de otros idiomas al staging y valida el árbol completo. Nuevo `--build-root` (dentro de `build/`). |
| PRESENTATION | `experience_index.html` reescrito; nueva `pages/experience.html` (única plantilla de ficha); logotipo y favicon en cabecera y pie; CSS de la vertical con los tokens existentes. |
| CONTENT (solo interfaz y sincronización) | `common.yaml`: 17 textos de interfaz (maqueta C04-PE y addenda D05). Traducción de `common.yaml` a ca/en/de (draft). `contacto.yaml` ca/en/de sincronizado con CONTACT-R1, reutilizando los textos ya traducidos. Ningún dato de experiencias cambia. |
| Docs | [arquitectura](../../architecture.md) (sección WEB-EXPERIENCE-03), [manifiesto ES](../editorial/quality/ES_BASELINE_MANIFEST.md) (huella renovada, las anteriores quedan como históricas), [contrato de localización](../editorial/localization/LOCALIZATION_CONTRACT.md), [spec EXPERIENCE](../editorial/handoff/EXPERIENCE_WEB_SPEC.md) §10. |

**Escalabilidad.** Una experiencia nueva enlazada desde el índice obtiene ruta, tarjeta y ficha sin tocar código ni
plantilla. Lo demuestra una prueba que añade en memoria una entidad `kind: bafras_project`; no se añade contenido
público ficticio.

**Proyectos BAFRAS.** El modelo ya distingue `kind: bafras_project` y comparte índice, ruta y ficha. La activación
futura consiste en añadir la entidad en CONTENT y su entrada en PE-02 (o un ámbito nuevo, que genera su ancla
automáticamente). No se ha creado ningún acceso público: no existe contenido aprobado, y un enlace vacío prometería
algo inexistente (§8.5 del encargo).

## 3. Causas raíz corregidas

| Incidencia | Causa raíz | Corrección |
|---|---|---|
| ca/en/de no generaban (PE-04 → capacidades «sin URL pública») | `url()` devolvía `None` para idiomas no publicados y `routes.yaml` solo tenía slugs es | Modo preview explícito y slugs ca/en/de; release sigue bloqueado |
| Faltaba layout en ca/en/de | `common.yaml` solo existía en es | Traducción draft con los mismos ids |
| Las imágenes fallaban en ca/en/de | El manifiesto solo tenía `alt_es` | `alt_<idioma>` en MEDIA |
| `contacto` ca/en/de sin componente (`form`) | CONTACT-R1 (9209efc) se aplicó solo a es | Sincronización estructural con el texto `help` ya traducido |
| Generar un idioma borraba los demás | `staged_directory` sustituía toda la preview | El HTML de otros idiomas se traslada al staging y se valida el árbol completo |
| `build/preview` inaccesible | ACL de Windows denegada desde el 07/11: no se puede leer el ACL ni renombrar la carpeta. Ajeno al código | Aislado con `--build-root`. No se han tocado permisos (ver §6) |

## 4. Evidencias funcionales

- **Pruebas:** suite completa satisfactoria (`build/we03-evidence/pytest-full.txt`).
  - Pruebas nuevas en `tests/integration/test_web_experience_03.py` y `tests/unit/test_routing.py`, además de las
    adaptaciones justificadas en build, multilingüe y MEDIA.
  - Ninguna prueba omitida ni relajada. Se retiraron dos excepciones de paridad (common y CONTACT-R1) porque las
    divergencias se resolvieron.
- **Builds:** `bafras-web build --locale <es|ca|en|de> --all --mode preview --build-root build/we03`, 16 páginas por
  idioma. El árbol completo valida sin admitir destinos ausentes.
- **Reproducibilidad:** `build/we03` y `build/we03-repro` son idénticos: 88 archivos inventariados uno a uno
  (`inventory.txt`), huella del inventario `f985e3b4…9fd3`. Regenerar un idioma deja el resto byte a byte igual
  (prueba automatizada). No hay exclusiones.

**Mapa de rutas** (preview; solo es está publicado):

| Página | es | ca | en | de |
|---|---|---|---|---|
| Índice | `/proyectos-experiencia/` | `/ca/projectes-experiencia/` | `/en/projects-experience/` | `/de/projekte-erfahrung/` |
| Ficha | `…/<id>/` | `…/<id>/` | `…/<id>/` | `…/<id>/` |
| Capacidades | `/capacidades/` | `/ca/capacitats/` | `/en/capabilities/` | `/de/kompetenzen/` |
| Sectores · Sobre · Contacto | `/sectores/` `/sobre-bafras/` `/contacto/` | `/ca/sectors/` `/ca/sobre-bafras/` `/ca/contacte/` | `/en/sectors/` `/en/about-bafras/` `/en/contact/` | `/de/branchen/` `/de/ueber-bafras/` `/de/kontakt/` |

Las especialidades cuelgan de Capacidades (`/ca/capacitats/infraestructures-installacions/`, etc.). El `<id>` de la
ficha es el identificador estable de la experiencia.

**Imágenes utilizadas.**
- Derivados WebP en `assets/images/experience/web/`: calidad 82, sin metadatos, orientación EXIF aplicada. Los
  originales no se han modificado (SHA-256 comprobado antes y después).
- Cada activo tiene en el manifiesto su original, la experiencia, el uso, la naturaleza y el alt en cuatro idiomas.

| Id | Experiencia | Uso | Original | Naturaleza |
|---|---|---|---|---|
| X02 / X04 | four-seasons-formentor | principal / galería | `formentor_1.jpg` / `formentor_2.jpg` | sin determinar (foto o render) |
| X05 / X06 | montesion | principal / galería | `montesion_1.jpg` / `montesion_2.jpg` | render |
| X07 / X08 | the-n-residences-ibiza | principal / galería | `ibiza_2.jpg` / `ibiza_1.jpg` | sin determinar |
| X03 / X09 | dogger-bank-a | principal / galería | `dogger bank 2.jpg` / `amin dogger bank.jpg` | fotografía |
| X10 / X11 | vineyard-wind-1 | principal / galería | `vinneyatrd turbina.jpg` / `amin vineayrd.jpg` | fotografía |
| X01 | uib-transicion-energetica | principal | `CAMPUS-UIB-2026.webp` | fotografía |
| — | edge-ai-investigacion | — | sin imagen adecuada | composición tipográfica |

Descartadas:
- `Dogger Bank 1.jpg`: 640 px, insuficiente.
- `8de8083c-….JPG`: cubierta fotovoltaica sin correspondencia verificable.
- Las 29 HEIC: no se convierten porque no se usan.

**Logotipo.** Se usa `BAFRAS_logo_horizontal_deep.svg` (maestro deep, fondos claros) en cabecera y pie, con favicon.
- Discrepancia: DEC-10 recomendaba `*_deep_corregido.svg` «si Diseño confirma». Ese archivo contiene un manifiesto
  C2PA que lo declara generado o modificado con IA, y no consta la confirmación de Diseño. Se aplica el maestro sin
  modificar.
- No se usa variante blanca porque no hay ninguna superficie oscura con logotipo.

## 5. Evidencias visuales

Las capturas están en `build/we03-evidence/` (fuera de Git):
- índice a 1440, 390 y 320 px (es, ca, de);
- fichas de los tres ámbitos (Formentor, Dogger Bank A, UIB), Edge AI sin imagen y Montesión en;
- regresión de las ocho páginas restantes a 1440 y 390 px.

QA de navegador (Chrome, servidor HTTP local, `build/qa-tools/we03_browser_qa.py`):
- 1440, 768, 390 y 320 px: 0 errores de JS, 0 imágenes rotas, 0 desbordamiento;
- un h1 por página y logotipo cargado;
- teclado: enlace de salto, logotipo, navegación, idiomas y anclas en orden lógico;
- el zoom 200 % se aproxima con el ancho de 768 px; no hay auditoría WCAG completa.

**Contraste con `proyectos-experiencia.html`.** Coinciden:
- hero editorial;
- cabecera de sección en dos columnas;
- anclas en «chips»;
- ámbitos «01 / ÁMBITO» en dos columnas;
- rejilla asimétrica 1,22/0,78 con la destacada a dos filas y filete verde;
- PE-03 en arena y PE-04 en banda pino.

| Diferencia | Causa |
|---|---|
| Sin aviso general ni etiquetas «Referencia destacada / Experiencia profesional previa» | Política sin descargos (addenda D03 §8) y §7.3 del encargo |
| Sin enlace «Explorar referencias ↓» en el hero | PE-01 no tiene esa acción en CONTENT; no se inventa |
| Imágenes reales en lugar de marcadores; miniatura en complementarias | Addenda D05 §1.5 (miniatura si hay material) |
| Magnitudes como etiquetas y línea «Profesional · Rol» | Addenda D05 §2 |
| «Inicio» por el logotipo y pie claro con logotipo | Cabecera y pie compartidos existentes (D05 VIS-020); no se rediseñan |

**Contraste con `plantilla-ficha-proyecto.html`.** Coinciden:
- hero pino con migas, ámbito, título y resumen;
- «Ficha técnica» lateral en arena;
- módulos numerados en dos columnas;
- retorno y cierre CTA.

| Diferencia | Causa |
|---|---|
| Imagen principal entre el hero y el contenido; galería como módulo | §8.2 del encargo |
| Sin «flag» de tipo; ficha técnica sin período, organización ni permisos | Sin datos publicables (P-EXP-04); los módulos vacíos se omiten |
| Eyebrow de módulo solo con número | Un único texto por módulo en CommonContent |
| Sin módulo «Estudio técnico» | No existen datos |

## 6. Pendientes y riesgos

- **Publicación:** revisión nativa de ca/en/de (common, experiencias), aprobación de los slugs ca/en/de (D04), SEO y
  release (sin implementar), y aprobación visual humana.
- **`build/preview`:** el propietario debe restaurar los permisos (p. ej. `takeown /F build\preview /R` +
  `icacls build\preview /grant <usuario>:F /T`) o borrarla. Mientras tanto, usar `--build-root build/we03`.
- **Imágenes:**
  - naturaleza sin determinar en Formentor e Ibiza, que conviene confirmar (render o fotografía);
  - las fotos de Amin muestran a una persona (autorización operativa §6.1);
  - la góndola de Vineyard lleva una marca de fabricante visible.
- **Logotipo maestro:** pendiente de la decisión DEC-10 (`deep` o `deep_corregido`).
- **Ficha sin contexto:** la ficha técnica queda sola en la primera fila; es aceptable, pero conviene validarlo
  visualmente.
- **Git:** los cambios WEB conviven con trabajo editorial previo sin commit (experiencias, addenda, fotos del
  usuario, `mep/` reorganizada). Un commit futuro debería separar los commits CONTENT y WEB por procedencia.

## 7. Criterios de aceptación

| Criterio | Estado |
|---|---|
| A · cuatro builds completos y conservados; PE-04; salida aislada; estados intactos | Cumplido |
| B · imágenes reales asociadas, derivados, originales intactos, logotipo oficial, sin rutas rotas | Cumplido (decisión DEC-10 pendiente) |
| C · siete referencias, tres ámbitos, jerarquía por datos, imágenes, enlaces a fichas, contraste con maqueta | Cumplido |
| D · siete fichas, una plantilla, módulos opcionales, rutas localizadas, retorno, extensibilidad probada | Cumplido |
| E · suite, navegador, capturas, comparación, regresión, reproducibilidad | Cumplido; sin auditoría WCAG completa |

## 8. Dictamen

**GO para revisión humana** de la composición y del contenido en preview. Publicación: **NO-GO** hasta cerrar los
pendientes de §6.
