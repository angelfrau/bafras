# BAFRAS WEB — WEB-00 · Auditoría del repositorio
**Fecha:** 03/11/2026 · **Ámbito:** repositorio `bafras/` (raíz Git real) · **Naturaleza:** inspección de solo lectura. No se ha cambiado de rama, ni hecho commits, ni descartado o borrado nada.

Comandos usados: `git rev-parse`, `branch -vv -a`, `remote -v`, `status --porcelain -uall [--ignored]`, `log --graph --all`, `diff --stat`, `diff HEAD`, `ls-files [--eol]`, `tag`, `stash list`, `ls-remote origin` y `fetch --dry-run`. Este último consulta el remoto sin actualizar referencias. Las cifras siguientes se pueden reproducir con esos comandos.

## 1. Estado Git

| Aspecto | Resultado |
|---|---|
| Raíz | `C:/Murti_Personal/PROJ - Laborals/Murti_Python/Web BAFRAS/bafras` |
| Rama activa | `feat/contingut-v2` @ `7dd2753` («Refactor Estructura Poryecto Web para mantenibiliad», 30/09/2026), sincronizada con `origin/feat/contingut-v2` |
| `main` local | `04c92c8` («Update index.html», 28/09/2026). `feat/contingut-v2` = `main` + 1 commit |
| Remoto | `origin` → `https://github.com/angelfrau/bafras.git` (único) |
| Remoto real (`ls-remote`) | `main` = **`4af79e0`** (local conoce `04c92c8`); ramas **`contratos-menores`** (`92754ba`) y **`presupuesto-pdf`** (`415f738`), no presentes localmente; `feat/contingut-v2` = `7dd2753` |
| Tags / stash | Ninguno / vacío |
| Staged | Nada |
| Commits locales sin publicar | Ninguno |
| Producción | `CNAME` = `bafras.com` → GitHub Pages; la rama publicada probablemente sea `main`, pero no se ha verificado en la configuración de Pages. **El contenido actual de `origin/main` (`4af79e0`) no se ha inspeccionado**: requiere `git fetch` (WEB_00_BASELINE §6) |
| Finales de línea | `core.autocrlf=true`, sin `.gitattributes`. Avisos LF→CRLF en `tests/test_structure.py` y `tools/validate.py`. `index.html` está en LF en el índice y en CRLF en el árbol |

## 2. Cambios preexistentes no confirmados (no atribuibles a esta intervención)

`git diff --stat` respecto a HEAD: 7 archivos, +1125/−212. Ninguno está staged.

| Archivo | Δ | Función del cambio | Clasificación |
|---|---|---|---|
| `index.html` | +487/−188 | Contenido público V1.0/V1.1 de «Áreas técnicas», Infraestructura y Sistemas energéticos sobre la SPA heredada | Trabajo **válido pero anterior** a la línea base G1: usa terminología («Áreas técnicas») que D03 V1.22 sustituye por «Capacidades». REVIEW |
| `css/components.css`, `css/pages.css` | +146/−0 · +111/−18 | Patrones `layout-*`, `capability-*`, diagramas CSS, ciclos de intervención | Igual que el anterior. REVIEW |
| `js/router.js` | 5 líneas | Títulos y metas SEO de Capacidades, INF y ENE | Igual. Útil como antecedente SEO, no como copy aprobado |
| `js/site.js` | 1 línea | Ruta de fotos de equipo de absoluta a relativa (`/assets/…` → `assets/…`) | Corrección funcional probable. REVIEW |
| `tests/test_structure.py` | +316 | 14 pruebas nuevas que fijan el contenido V1.0/V1.1 | Válido para el sitio heredado; contradice D03 V1.22 (WGR-038) |
| `tools/validate.py` | +59 | Detección de mojibake, terminología y avisos de publicación | Detección de mojibake reutilizable; reglas terminológicas obsoletas |

Interpretación: es un bloque coherente de trabajo de septiembre (fechas 30/09/2026), documentado en los `.md` no rastreados de `docs/`. Pasa sus propias pruebas (18/18). No es experimental, pero **es incompatible con la línea base G1** en terminología y no forma parte de V2. Recomendación: preservarlo en una rama propia, sin integrarlo en V2 ni descartarlo (WEB_00_PLAN_SANEAMIENTO §3).

## 3. Archivos no rastreados (151 archivos en 13 entradas de primer nivel)

| Ruta | Archivos | Tamaño | Contenido |
|---|---|---|---|
| `assets/images/BAFRAS_Website_Visual_Assets_V1/` | 91 | 102 MB | Biblioteca de imágenes V2: 29 WebP derivados, originales JPG/TIFF (hasta 13 MB), `source.json`, manifiestos (`assets-inventory.csv`, `media-manifest.yaml`, `attribution.md`), `reports/` y 3 scripts `demo_graphics.py`. **No referenciada por el código productivo** |
| `docs/project_v02/` | 42 (antes de los entregables WEB-00/G1-CLOSE) | 9,8 MB | Paquete documental G1 vigente (D03/D04/D05, acta, briefing, maquetas ZIP, auditorías, evidencias) |
| `docs/audits/01…07-*.md` | 7 | — | Auditoría de arquitectura del 02/11/2026: comparación A/B/C y elección de Python + Jinja2 |
| `docs/*.md`, `docs/content/*.md` | 11 | — | Documentación del trabajo de septiembre (sección 2) |

## 4. Archivos ignorados y sensibles
- Ignorados presentes: `tests/__pycache__/`, `tools/__pycache__/` y `.pytest_cache/` (este último con permisos que impiden listarlo; residuo local).
- Búsqueda de secretos (`*.env`, `*secret*`, `*.key`, `*.pem`, `*credential*`, `*token*`, `id_rsa*`): **ninguno**. Único resultado, falso positivo: `css/tokens.css`.
- `.gitignore` no cubría `.venv/`, `.env` ni compilados `*.pyc` fuera de `__pycache__`: corregido en esta intervención (sección 7).
- Datos personales en el paquete: nombres de pila de los fundadores, `info@bafras.com` y el teléfono autorizado por adenda 03.CO-02. Son datos públicos por decisión documentada. Las hojas de contactos de `evidencias_B02_recursos/` muestran personas identificables en dos imágenes de Commons (R04, R05); es una consideración de publicación, no de versionado.

## 5. Estructura actual (resumen)
```
bafras/                      (54 archivos rastreados)
  index.html                 SPA heredada (#/rutas), 110 KB
  css/ {tokens,base,components,pages}.css
  js/  {router,site,form}.js
  assets/images/{brand,team,experience,home,misc}   (34 rastreados)
  assets/images/BAFRAS_Website_Visual_Assets_V1/    (no rastreada)
  tests/test_structure.py · tools/validate.py · pyproject.toml (sin dependencias)
  docs/ (6 rastreados + 62 no rastreados, incluida project_v02/)
  CNAME · README.md · .gitignore
```

## 6. Riesgos

| # | Riesgo | Severidad | Evidencia |
|---|---|---|---|
| R1 | **Pérdida documental ya materializada:** D02 (`02_posicionamiento.md`, 2347 líneas) existía el 02/11/2026 (B01 L5, L36) y hoy no está en el paquete, en el repositorio ni en el árbol de proyecto. Al no estar en Git, no es recuperable desde el repositorio | **P0** | `find` sin resultados; B01 L5/L36 |
| R2 | 9,8 MB de documentación G1, 102 MB de biblioteca y el trabajo de septiembre dependen de una sola copia local | P0 | sección 3 |
| R3 | `origin/main` ha avanzado (`4af79e0`) y hay dos ramas remotas desconocidas: el estado publicado no coincide con el que se conoce localmente | P1 | `ls-remote` |
| R4 | `feat/contingut-v2` es una rama publicada en el remoto: cualquier reescritura afectaría a terceros | P1 | `branch -vv` |
| R5 | Finales de línea sin normalizar (`autocrlf` sin `.gitattributes`): diffs de archivo completo y falsos cambios | P2 | sección 1 |
| R6 | Biblioteca de 102 MB con originales de hasta 13 MB: versionarla tal cual infla el historial para siempre | P2 | sección 3 |
| R7 | Las pruebas actuales fijan la terminología antigua: cualquier implementación conforme a D03 las rompe | P2 | WGR-038 |

## 7. Acciones ejecutadas en WEB-00 (no destructivas)
1. **Respaldo verificable** fuera del repositorio, en `../_respaldo_WEB-00_20261103/`: bundle de todas las referencias locales (verificado con `git bundle verify`), parche `git diff HEAD --binary`, tar byte a byte de los 7 archivos modificados y de los 151 no rastreados, lista de archivos, estado Git y `SHA256SUMS.txt`. Verificación en WEB_00_BASELINE §3.
2. **`.gitignore`**: añadidos `.venv/`, `venv/`, `*.py[cod]`, `.mypy_cache/`, `.ruff_cache/`, `.env`, `.env.*` y `!.env.example`. Comprobado que ningún archivo existente cambia de estado de seguimiento.
3. Ningún borrado, traslado, `stash`, cambio de rama, `fetch` real ni commit.
