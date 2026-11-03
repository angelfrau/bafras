# 01 · Baseline del repositorio

Auditoría: 2 de noviembre de 2026, Europe/Madrid. Alcance: copia local de `bafras/`, incluidos sus cambios pendientes. No representa una comprobación del sitio publicado. Documentación relacionada: [hallazgos](02-architecture-findings.md), [decisión](03-architecture-decision.md), [migración](07-incremental-migration-plan.md).

## Estado de Git antes de documentar

- Rama: `feat/contingut-v2`; no se cambió de rama.
- HEAD: `7dd275324ed1212662f099b69fa3cdd1a8930bff`.
- Mensaje literal: `Refactor Estructura Poryecto Web para mantenibiliad`.
- Autor y committer: Murti; fecha del commit: 30/09/2026 11:09:26 +0200.
- Referencias locales: `main` y `origin/main` en `04c92c8`; rama actual y su referencia `origin/feat/contingut-v2` en `7dd2753`. No se hizo fetch: esta coincidencia no acredita el estado remoto actual.
- Siete archivos rastreados modificados, ninguno preparado en el índice: `css/components.css`, `css/pages.css`, `index.html`, `js/router.js`, `js/site.js`, `tests/test_structure.py`, `tools/validate.py`.
- Diff inicial: 1.125 inserciones y 212 eliminaciones. El HTML aporta 675 líneas al diff; componentes CSS 146; páginas CSS 129; tests 316; validador 59; router 10; site 2. Son tamaños del diff, no tamaños finales.
- Once archivos sin rastrear: `docs/capabilities-architecture-implementation.md`, `docs/content-review-backlog.md`, `docs/content/capabilities.md`, `docs/content/home.md`, `docs/energy-systems-content-implementation.md`, `docs/energy-systems-visual-refinement-v1.1.md`, `docs/infrastructure-engineering-content-implementation.md`, `docs/infrastructure-visual-refinement-v1.1.md`, `docs/visual-component-inventory.md`, `docs/visual-evidence-map.md`, `docs/visual-system-v1.md`.

Git detectó propietario distinto al del proceso. Se usó exclusivamente `git -c safe.directory='<ruta absoluta de bafras>' …` por comando, sin cambiar configuración global. Git también avisó de falta de acceso al ignore global y de conversión LF/CRLF futura en dos archivos Python. No se normalizaron archivos. No se localizaron instrucciones `AGENTS.md` en el árbol del workspace inspeccionado.

## Árbol observado

```text
bafras/
  .git/                    referencias locales; sin cambios de esta auditoría
  .pytest_cache/           preexistente
  index.html               único documento HTML operativo
  CNAME                    bafras.com
  css/                     tokens.css, base.css, components.css, pages.css
  js/                      site.js, router.js, form.js
  assets/images/
    brand/                 favicon, logos, social, symbols
    home/                  hero, vision
    experience/mep/        seis JPG
    team/                  tres parejas PNG/JPG
    misc/                  archivo a, 2 bytes
  images/                  vacío; sin referencias operativas legacy
  tools/validate.py
  tests/test_structure.py
  pyproject.toml
  docs/                    contenido, diseño y arquitectura previos
  README.md
```

No hay `package.json`, lockfile JS, plantillas de generación, manifiesto de medios, colecciones de contenido, `sitemap.xml`, `robots.txt`, `404.html` ni workflow `.github/` en el árbol observado.

## Magnitudes reproducibles

| Archivo | Bytes en disco | Líneas |
|---|---:|---:|
| index.html | 110.026 | 1.208 |
| css/tokens.css | 958 | 21 |
| css/base.css | 1.191 | 22 |
| css/components.css | 36.398 | 378 |
| css/pages.css | 31.737 | 447 |
| js/site.js | 972 | 20 |
| js/router.js | 6.486 | 103 |
| js/form.js | 858 | 11 |

CSS total: 70.284 bytes; JS total: 8.316 bytes. No son tamaños transferidos comprimidos. `assets/` contiene 34 archivos y 5.816.707 bytes: 33 recursos gráficos y un archivo sin formato gráfico reconocido. No se infiere de ello el peso de una visita: numerosos recursos no están referenciados.

## Dependencias y operación actual

`pyproject.toml` declara `bafras-site` 0.5.0 y Python >=3.10. No fija dependencias de desarrollo ni versiones de pytest. El runtime es HTML/CSS/JS nativo; no hay build ni backend propio. Dependencias externas observadas: Google Fonts (Inter), FormSubmit para POST nativo y AJAX. No se identificó instrumentación analítica en los archivos operativos.

Desarrollo documentado: `python -m http.server 8000` desde la raíz y edición directa de HTML/CSS/JS. README y `docs/architecture.md` describen compatibilidad con GitHub Pages desde la raíz; `CNAME` declara `bafras.com`. No hay workflow ni configuración local que pruebe qué rama publica, si hay Actions o despliegue desde rama, DNS efectivo o HTTPS activo. Verificar esos ajustes antes de implementar publicación; no deducirlos del nombre de rama.

Entorno examinado: Python 3.12.10; pytest y Pillow importables; Jinja2, Playwright, BeautifulSoup y tinycss2 no importables; `node` no disponible en PATH. Chrome y Edge sí existen en sus rutas habituales de Program Files. No se instaló ninguna herramienta.

## Validaciones ejecutadas

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -B tools/validate.py
python -B -m pytest -p no:cacheprovider -q
```

Resultados: validador con exit code 0 y `Validation passed.`; advertencias `placeholders: 33 item(s)` y `verify flags: 10 item(s)`. Pytest: **18 passed in 0.12s**. Se deshabilitaron bytecode y caché de pytest para evitar escrituras de las pruebas. Las advertencias cuentan coincidencias de regex, no entidades únicas ni errores bloqueantes; véase 02.

Se midió HTML con `html.parser`, CSS mediante lectura y recorrido de llaves/contextos, e imágenes con Pillow, sin editar fuentes. Este análisis no sustituye un validador HTML completo, CSSOM, auditoría WCAG o medición de Core Web Vitals.

Se intentó Chrome con `--headless --disable-gpu --no-first-run --no-default-browser-check --user-data-dir=<perfil temporal> --dump-dom` contra el archivo local y `#/capacidades/infrastructure`. Resultado: exit code **2147483651**, salida DOM de 0 bytes. Stderr: procesos GPU terminan con `-1073741790`, fallos de acceso/caché (`0x20`, `0x80070005`) y `GPU process isn't usable. Goodbye.` Es un fallo del entorno al arrancar el navegador; no acredita un fallo de la web. No hubo captura visual válida, test de navegación runtime ni prueba de envío de formulario.

Alternativa: servir por HTTP con el comando del README y revisar en Chrome/Edge interactivo; para automatizar, usar un entorno CI compatible con Playwright tras aprobar su incorporación. Matriz concreta en 07. No se envían consultas comerciales de prueba durante la auditoría.

## Integridad y límites

Se tomó una huella SHA-256 de los 65 archivos preexistentes fuera de `.git`, caché de pytest y bytecode antes de crear entregables. La comparación final confirmó cero archivos preexistentes alterados y únicamente siete documentos añadidos bajo `docs/audits/`. Los siete documentos se pudieron leer como UTF-8 y sus enlaces relativos Markdown resolvieron correctamente. El diff de los siete archivos rastreados pendientes conserva sus magnitudes iniciales. No se hicieron commits, push, limpieza, cambios de rama ni modificaciones de páginas, estilos, scripts, tests o imágenes.

La auditoría no verifica rankings, búsquedas/volumen comercial, permisos reales de imágenes, ajustes remotos del hosting, entrega efectiva de correo ni cifras de proyectos. El documento exacto «BAFRAS Website — Plan Maestro de Material Gráfico V1.0» no se localizó entre los archivos disponibles; 06 propone compatibilidad con los requisitos facilitados y con los inventarios locales, pendiente de cotejo con el original.
