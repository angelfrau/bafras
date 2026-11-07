# WEB-V01-A · Plan ejecutable: Inicio en español desde el `EditorialBundle` real

Fecha: 07/11/2026 · Base: `feat/contingut-v2` @ `3927e5f` · Auditoría previa: [WEB_01_INFORME](WEB_01_INFORME.md).
Este documento se puede usar tal cual como encargo de implementación.

> **Estado (WEB-V01-A R4, 07/11/2026): implementado.** `bafras-web build --locale es --page inicio --mode preview` genera `build/preview/es/inicio/index.html`. Diferencias con este plan: los enlaces se indexan por destino tipado (`dict[LinkTarget, str]`) en lugar de `(page_id, section_id)`; la escritura atómica es un solo archivo (`write_text_atomically`); release se bloquea siempre hasta WEB-V01-B; las familias soportadas se declaran en `application/build.py` (`SUPPORTED_SECTIONS`); no hay CSS (fidelidad D05 en V01-B).

## 1. Objetivo y alcance

Generar la página `inicio`, en `es` y en modo **preview**, como HTML estático a partir del bundle editorial
real, usando `SiteRouting` para los enlaces y Jinja2 con autoescape, con pruebas de integración.

**Incluido:**
- adaptador Jinja2;
- layout mínimo;
- componentes de los 5 `kind` que usa Inicio;
- resolución de enlaces internos;
- política preview/release;
- escritura atómica;
- comando `bafras-web build`.

**Excluido:**
- las otras 8 páginas;
- fidelidad visual D05 completa (tokens, cortes);
- imágenes (`MediaRef` pendiente);
- menú y pie (`common.yaml` pendiente);
- SEO técnico (canonical, hreflang, sitemap);
- `ca`, `en` y `de` como salida en disco;
- despliegue.

## 2. Contratos reales que se consumen (verificados en WEB-01)

| Pieza | Firma real |
|---|---|
| Rutas | `load_site_routing(paths: ProjectPaths) -> SiteRouting` (`ConfigurationError`) |
| URL | `SiteRouting.url(page_id: str, locale: str) -> str \| None`: `KeyError` si la página no existe; `None` si el idioma no está publicado o no tiene slug. `es`: `inicio → /`, `capacidades → /capacidades/`… |
| Carga | `inspect_editorial(paths, EditorialLoadRequest(locale=…, policy="COMPLETE")) -> EditorialInspection` |
| Bundle | `build_editorial_bundle(inspection) -> EditorialBundle` (`ValueError` si `not inspection.can_build_bundle`) |
| Página | `bundle.get_page("inicio") -> PageContent`. **El identificador es `inicio`, no `home`** |
| Secciones | `PageContent.sections`: `h01 hero`, `h02 cards/capabilities`, `h03 item_list/needs`, `h04 process/workflow`, `h05 cards/sector_preview`, `h06 text`, `h07 text` |
| Estado | `PageContent.review.status == "draft"`; 8 `pending` (SEO ×2, H05 items, media ×5) |
| Enlaces | En Inicio todas las acciones son `CallToAction` con `InternalLink(page_id, section_id=None)`. Hay 14 enlaces (8 destinos distintos) y todos resuelven en `es` |

**No se modifica ningún modelo de `bafras_web.editorial`.**

## 3. Arquitectura mínima

```
cli.py  build --mode preview|release --locale es --page inicio
  └─ application/build.py  build_page(paths, locale, page_id, mode) -> BuildResult
       ├─ load_site_routing + inspect_editorial + build_editorial_bundle   (API existente)
       ├─ site/publication.py  publication_blockers(page, locale, routing, mode) -> list[str]
       ├─ site/links.py        resolve_links(page, locale, routing) -> dict[LinkKey, str]   (falla si alguno no resuelve)
       ├─ adapters/jinja.py    render_html(template_name, context) -> str   (autoescape, StrictUndefined)
       └─ adapters/filesystem.py  write_files_atomically(target_dir, files: dict[Path, str])
```

**Decisiones cerradas para V01-A:**

1. **Contexto de plantilla:** no hay un segundo árbol de modelos. Las plantillas reciben `page: PageContent`,
   `locale: str`, `mode: str` y `links: dict[tuple[str, str | None], str]`, y usan un filtro `href(target)`
   que solo consulta `links`. La resolución se hace **antes** de renderizar, así que la plantilla nunca
   construye una URL.
2. **Selección de componente:** `components/{{ section.kind }}.html` (enumerado cerrado; un `kind` sin
   plantilla es error de build). Dentro de cada componente, el `purpose` elige la variante con `if`. Las
   variantes por identidad de sección que D05 exige (H05 banda verde pino, H06 respiro claro, H07 banda de
   cierre) se expresan con una **clase CSS** `section--{{ section.id }}` y no con plantillas distintas. No se
   crea `compositions.yaml`.
3. **Enlaces no internos:** `ContactLink`, `ExternalLink`, `ResourceLink` y `SharedActionRef` no aparecen en
   Inicio. En V01-A producen un error de build explícito ("tipo de enlace no soportado"), en lugar de un
   `href` vacío.
4. **Preview frente a release:**
   - *preview*: admite `draft`, escribe en `build/preview/<locale>/<page_id>/index.html` (ya ignorado por
     Git y **fuera de `dist/`**, para que nunca se despliegue), añade `<meta name="robots"
     content="noindex,nofollow">` y un aviso visible, y no genera canonical ni hreflang.
   - *release*: exige idioma publicado, URL pública y `review.status == "approved"`. Hoy Inicio es `draft`,
     así que **release debe fallar**, y eso es lo esperado.
5. **`<title>` en preview:** técnico y no editorial, `PREVIEW · inicio · es`, porque `seo.title` es `null`
   (DEC-05). En release, un `seo.title` nulo bloquea la publicación.
6. **Medios:** no se renderiza ninguna `<img>` (`media` es `None` en el modelo). La composición debe
   funcionar sin imagen. No hay huecos visibles ni marcadores.
7. **Cabecera y pie:** ningún texto de interfaz inventado. El layout V01-A no lleva menú, pie ni texto de marca hasta que
   exista `common.yaml`.

## 4. Plan de archivos

| Archivo | Existe | Acción | Responsabilidad | Prueba asociada |
|---|---|---|---|---|
| `src/bafras_web/adapters/jinja.py` | **Sí (V01-A.1)** | Hecho | `template_environment()` (compartido: `PackageLoader`, `select_autoescape`, `StrictUndefined`); `render_html(template_name, context, *, environment=None) -> str`. Plantillas adicionales mediante `Environment.overlay` | `tests/unit/test_jinja_adapter.py`, `tests/integration/test_jinja_home_h01.py` |
| `src/bafras_web/adapters/filesystem.py` | Sí | Ampliar | `write_files_atomically(target: Path, files: dict[Path, str])`: escribe en un directorio temporal hermano y lo sustituye con `os.replace`; sin salida parcial | `tests/unit/test_filesystem_write.py` |
| `src/bafras_web/site/links.py` | No | Crear | `resolve_links(page, locale, routing) -> dict[(page_id, section_id), str]`: URL + `#section_id`; error con selector si `url()` es `None` o el tipo no está soportado | `tests/unit/test_links.py` |
| `src/bafras_web/site/publication.py` | No | Crear | `PublicationMode = Literal["preview", "release"]`; `publication_blockers(page, locale, routing, mode) -> list[str]` | `tests/unit/test_publication.py` |
| `src/bafras_web/application/build.py` | No | Crear | `build_page(paths, locale, page_id, mode, out_root) -> BuildResult` (ruta escrita o diagnósticos); orquesta sin reglas editoriales | `tests/integration/test_build_home.py` |
| `src/bafras_web/cli.py` | Sí | Ampliar | `_register_build`: `build --mode {preview,release} --locale --page`; código 1 con diagnósticos | `tests/unit/test_cli.py` (ampliar) |
| `src/bafras_web/templates/layouts/base.html` | **Sí (V01-A.1)** | Hecho | `<html lang>`, `<head>` (charset, viewport, title, robots en preview), aviso de preview, `<main>` | Golden de estructura en `test_build_home.py` |
| `src/bafras_web/templates/components/{hero,cards,item_list,process,text}.html` | No | Crear | Un componente por `kind` usado en Inicio; `id="{{ section.id }}"` como ancla | `test_build_home.py` |
| `assets/css/base.css` | No | Crear (mínimo) | Tokens de color de D05 y tipografía; sin la composición completa | Prueba de existencia y enlace |
| `tests/contracts/test_architecture.py` | Sí | Sin cambios | Ya impide `jinja2` fuera de `adapters` | Ejecutar |
| `docs/architecture.md` | Sí | Actualizar §5 | Registrar `build` como implementado | — |

`site/` no importa Jinja2 ni YAML (regla vigente). `application/build.py` puede importar `adapters`.

## 5. Secuencia de implementación

| # | Objetivo | Cambios | Pruebas | Resultado observable | Aceptación |
|---|---|---|---|---|---|
| 1 | Adaptador Jinja2 seguro | `adapters/jinja.py` y `layouts/base.html` | Autoescape (`<script>` → `&lt;script&gt;`); variable no definida → error; plantilla inexistente → error | `render("layouts/base.html", …)` devuelve HTML | 3 pruebas en verde; `test_architecture` en verde |
| 2 | Resolución de enlaces | `site/links.py` | Los 14 enlaces de Inicio dan las URL esperadas; ancla con `section_id`; idioma no publicado → error con selector; tipo no soportado → error | Diccionario de enlaces de Inicio | Ningún `href` se construye fuera de `links.py` |
| 3 | Política de publicación | `site/publication.py` | preview + draft → sin bloqueos; release + draft → bloqueo `review`; release + idioma no publicado → bloqueo; release + `seo.title` nulo → bloqueo | Lista de bloqueos | Ninguna prueba altera estados editoriales |
| 4 | Componentes de Inicio | `components/*.html` (5) | H01–H07 en orden (`id`); cada texto del `PageContent` aparece una vez y escapado; `purpose` correcto; 0 `<img>`; `href` de cada acción = URL resuelta | HTML de Inicio en memoria | Prueba de preservación: todos los `str` del modelo están en la salida |
| 5 | Orquestación y escritura | `application/build.py` y `write_files_atomically` | build preview `es/inicio` escribe `build/preview/es/inicio/index.html` con `noindex`; release falla con diagnóstico y **sin** escribir; error de render a mitad → directorio destino intacto | Archivo HTML abrible | Fallo = sin salida parcial |
| 6 | CLI | `_register_build` | `build --mode preview` → 0; `--mode release` → 1 con mensaje; `--page desconocida` → 1; `--locale fr` → 1 (`LOCALE_UNKNOWN`) | `bafras-web build …` | Mensajes con código y selector |
| 7 | Separación de idiomas (en memoria) | Prueba sin salida en disco | Para `ca`, `en`, `de`: la carga y el bundle funcionan, y `resolve_links` falla explícitamente (sin URL pública ni fallback a `es`) | Diagnóstico por idioma | Ningún HTML de ca/en/de reutiliza URL de `es` |

## 6. Pruebas previstas

| Prueba | V01-A | Posterior |
|---|---|---|
| Bundle real de Inicio y H01–H07 en orden | ✔ | |
| Preservación de todos los textos y del orden de colecciones | ✔ | |
| Escape HTML (texto con `<`, `&`, comillas en fixture) | ✔ | |
| Enlaces internos resueltos con `SiteRouting` (+ anclas) | ✔ | |
| Referencia inválida (fixture en `tmp_path`) → build falla antes de renderizar | ✔ | |
| Separación de idiomas sin fallback (ca/en/de) | ✔ (en memoria) | Salida preview multilingüe (decisión D-W2) |
| Renderizado sin imágenes | ✔ | Con `MediaRef` |
| Preview de `draft` con `noindex` y aviso | ✔ | |
| Release bloqueado para `draft` | ✔ | |
| Fallo de build sin salida parcial | ✔ | |
| Determinismo (dos builds → bytes idénticos) | ✔ | |
| Fidelidad visual frente a la maqueta Inicio V3 (6 anchos, zoom) | | V01-B / G3 |
| Menú, pie, canonical, hreflang, sitemap | | Tras `common.yaml` y SEO |

## 7. Criterios de aceptación

1. `bafras-web build --mode preview --locale es --page inicio` genera `build/preview/es/inicio/index.html`
   desde el contenido real.
2. Usa solo `inspect_editorial`, `build_editorial_bundle` y `SiteRouting`; no lee YAML ni duplica modelos.
3. Las secciones H01–H07 y todos sus textos aparecen en orden y sin alteraciones (prueba de preservación).
4. Todos los `href` internos proceden de `SiteRouting`.
5. Jinja2 con `autoescape=True` y `StrictUndefined`.
6. El HTML es verificable: sin `<img>`, con `lang="es"` y `noindex` en preview.
7. `--mode release` falla para Inicio (`draft`) sin escribir nada.
8. Los errores salen con código, selector e idioma; un fallo no deja salida parcial.
9. Sin cambios en `src/bafras_web/editorial/` ni en `content/`.
10. Suite completa en verde (base: 578) más las pruebas nuevas.

## 8. Riesgos y dependencias

| Elemento | Impacto en V01-A | Propietario |
|---|---|---|
| `MediaRef` sin definir (5 imágenes de Inicio: R24, R23, R22, R21, R03) | Ninguno: render sin imágenes | WEB propone y CONTENT acepta el cambio de modelo |
| `common.yaml` ausente (menú, pie, mensajes) | Ninguno: layout sin menú ni pie | CONTENT, a partir de D03 |
| `seo.title` / `description` nulos (DEC-05) | Solo release | Dirección / Editorial |
| H05: tarjetas solo con título (`approval_required`) | Se renderizan tal cual | Editorial |
| Salida preview de idiomas no publicados (D-W2) | No es necesaria en V01-A | WEB |
| Política de pendientes en release (D-W3) | No es necesaria (release falla ya por `draft`) | WEB + dirección |
