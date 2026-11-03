# BAFRAS WEB — WEB-00 · Plan de saneamiento
**Fecha:** 03/11/2026 · **Base:** `WEB_00_AUDITORIA_REPOSITORIO.md` · **Regla:** nada de esta tabla se ha ejecutado salvo lo marcado «HECHO». Todas las demás acciones requieren autorización expresa.

Clases: `KEEP` conservar · `REORGANIZE` reorganizar · `ARCHIVE` preservar como histórico · `REMOVE` residuo prescindible · `REVIEW` decisión humana.

## 1. Clasificación

| Ruta | Clase | Motivo | Dependencias | Riesgo | Acción propuesta | Autorización |
|---|---|---|---|---|---|---|
| `index.html`, `css/*`, `js/*` (HEAD) | KEEP | Sitio productivo heredado; referencia de G0 y de rollback | GitHub Pages, `CNAME` | Alto si se toca | No modificar hasta WEB-01 | — |
| Cambios no confirmados en esos 7 archivos | REVIEW | Trabajo válido de septiembre, incompatible con la terminología G1 | `docs/*.md` de septiembre | Pérdida si se descartan; regresión si se integran en V2 | Commit A en `feat/contingut-v2` (§3) | **Sí** |
| `tests/test_structure.py`, `tools/validate.py` | KEEP (+ REVIEW de los cambios) | Red de seguridad del sitio heredado | `pytest`, `index.html` | Fijan el copy antiguo (WGR-038) | Mantener para el sitio heredado; V2 tendrá sus propias pruebas (WEB-02) | Sí (commit A) |
| `docs/project_v02/` (núcleo: 00–05, 99, B01, B02_PREP, WEB_*) | KEEP | Línea base documental G1 vigente | Todo V2 | **P0: única copia** | Commit B (§3) | **Sí** |
| `docs/project_v02/maquetas_aprobadas/*.zip` (7,2 MB) | KEEP | Las nueve maquetas aprobadas: autoridad de composición | D05, acta | No excluir por tamaño | Commit B, tal cual (sin descomprimir) | Sí |
| `docs/project_v02/soporte_auditoria/`, `evidencias_*` | KEEP | Trazabilidad de auditorías | INFORME, CSV | Bajo | Commit B | Sí |
| `docs/audits/01…07` | ARCHIVE | Auditoría de arquitectura (02/11/2026) que fundamenta la elección B (Jinja2); superada por D04 V2.4 | D04 | Bajo | Commit B en `docs/audits/` sin mover | Sí |
| `docs/*.md` de septiembre (9) y `docs/content/*.md` (2) | ARCHIVE | Documentación del trabajo heredado | Commit A | Bajo | Commit A, junto al código que describen | Sí |
| `docs/*.md` rastreados (6) | KEEP | Histórico ya versionado | — | — | Sin cambios | — |
| `assets/images/BAFRAS_Website_Visual_Assets_V1/assets/` (29 WebP, 5 MB) | KEEP | Derivados candidatos para V2 | `media-manifest.yaml`, B02_PREP | Licencias CC BY-SA no verificadas | Commit C | Sí |
| `…/manifests/`, `README.md`, `reports/` (1,7 MB) | KEEP | Procedencia, licencia y atribución | Contrato de medios | — | Commit C | Sí |
| `…/originals/` (96 MB; JPG/TIFF ≤ 13 MB + `source.json`) | REVIEW | Necesarios para rederivar y acreditar procedencia; costosos en historial | `source.json` con SHA1 | Inflado permanente del repositorio | Opción recomendada: versionar solo `source.json` y conservar los binarios fuera de Git (almacén con SHA1 ya registrado). Alternativas: Git LFS o commit directo | **Sí (DEC-12)** |
| `…/originals/{D06,E01,E07}/demo_graphics.py` | REVIEW | Tres copias idénticas (mismo MD5) del generador de gráficos sintéticos propios | E01/E07/D06 | Duplicidad | Conservar una sola copia en `tools/` en WEB-02; mientras, no tocar | Sí |
| `assets/images/brand/logos/*` (variantes `_corregido`, `logo_h_*`) | REVIEW | Varias versiones del logo sin maestro declarado (WGR-060) | `index.html`, `css` | Elegir mal el maestro | Decisión DEC-10; no borrar | Sí |
| `assets/images/team/*.{jpg,png}` | REVIEW | Retratos sin consentimiento documentado para V2 (WGR-081) | `js/site.js` | Publicación | Mantener; no usar en V2 sin autorización | — |
| `assets/images/misc/a` | REMOVE | Archivo rastreado de 2 bytes (`\r\n`), sin referencias en código ni pruebas; marcador de carpeta | Ninguna (grep) | Nulo | `git rm` en un commit de limpieza | **Sí (archivo rastreado)** |
| `tests/__pycache__/`, `tools/__pycache__/`, `.pytest_cache/` | REMOVE | Cachés ya ignoradas | — | Nulo | Pueden borrarse localmente en cualquier momento; no afectan a Git | No (no se ha hecho) |
| `.gitignore` | KEEP | — | — | — | **HECHO**: entornos, compilados y `.env` | — |
| `dist/` (futuro) | REVIEW | Salida del build Jinja2 | Despliegue | Versionar artefactos, o no | Decidir en WEB-01 junto con el método de despliegue (Pages desde Actions vs rama) | Sí |
| `../_respaldo_WEB-00_20261103/` (fuera del repo) | KEEP | Respaldo verificable de esta intervención | — | — | Conservar hasta confirmar los commits A–C | — |

## 2. Hallazgos de duplicidad y residuos
- Duplicados exactos rastreados: ninguno en `brand/` ni `team/` (hash SHA-256). Sí hay variantes funcionalmente redundantes de logo y de foto (`.jpg` y `.png` del mismo retrato).
- Estructura anidada `BAFRAS_Website_Visual_Assets_V1/assets/images/…` dentro de `assets/images/`: la ruta final prevista por el manifiesto (`assets/images/home/hero/…`) no coincide con la ubicación real. Reorganizar **solo** en WEB-02, cuando el contrato de medios fije la ruta publicada (REORGANIZE diferido).
- Colisión de identificadores: las imágenes `D01…D07` de la biblioteca comparten nombre con los documentos D01–D05, y una de ellas se llama `D02_original.jpg`. Ver WGR-008 y WGR-096.

## 3. Commits propuestos (ninguno ejecutado)

Selección explícita, sin `git add .`. Cada commit es independiente y revisable.

**Commit A — preservar el trabajo heredado** · rama `feat/contingut-v2`
```
git add css/components.css css/pages.css index.html js/router.js js/site.js \
        tests/test_structure.py tools/validate.py \
        docs/capabilities-architecture-implementation.md docs/content-review-backlog.md \
        docs/energy-systems-content-implementation.md docs/energy-systems-visual-refinement-v1.1.md \
        docs/infrastructure-engineering-content-implementation.md docs/infrastructure-visual-refinement-v1.1.md \
        docs/visual-component-inventory.md docs/visual-evidence-map.md docs/visual-system-v1.md \
        docs/content/capabilities.md docs/content/home.md
git commit -m "WIP: contenido V1.0/V1.1 Áreas técnicas (preservado; no integrado en V2)"
```
Antes, confirmar que `pytest` y `tools/validate.py` pasan (hoy: 18 pasadas). No publicar (`push`) sin decisión.

**Commit B — documentación G1** · rama `v2/desarrollo` (§4), **no en `main`**
```
git add .gitignore docs/project_v02/ docs/audits/
git commit -m "docs: paquete G1 (D03 V1.22, D04 V2.4, D05 V4.12, maquetas, auditorías, WEB-00/G1-CLOSE)"
```
Motivo para no usar `main`: si GitHub Pages sirve la raíz de `main` (indicio: `CNAME`), todo `docs/` se publicaría en `bafras.com/docs/…`. Los `docs/*.md` ya rastreados probablemente son públicos hoy. Verificar en *Settings → Pages* (DEC-13).

**Commit C — biblioteca de medios (sin originales)** · rama `v2/desarrollo`
```
git add assets/images/BAFRAS_Website_Visual_Assets_V1/README.md \
        assets/images/BAFRAS_Website_Visual_Assets_V1/assets/ \
        assets/images/BAFRAS_Website_Visual_Assets_V1/manifests/ \
        assets/images/BAFRAS_Website_Visual_Assets_V1/reports/ \
        assets/images/BAFRAS_Website_Visual_Assets_V1/originals/*/source.json
```
Los binarios de `originals/` quedan según DEC-12.

**Commit D — limpieza** (opcional): `git rm assets/images/misc/a`.

## 4. Estrategia de ramas (proporcionada)

| Rama | Papel | Regla |
|---|---|---|
| `main` | Producción publicada (bafras.com) | Solo recibe la integración final de V2 o correcciones urgentes del sitio heredado. Antes de V2: etiqueta anotada `prod-pre-v2` sobre `origin/main` actualizado |
| `feat/contingut-v2` | Trabajo heredado de septiembre | Se congela tras el commit A. No se fusiona en V2 |
| `v2/desarrollo` | Integración de V2 (docs + build Jinja2) | Se crea desde `origin/main` **actualizado**. Cada intervención WEB-01…WEB-0n entra como commit o rama corta `v2/web-0n-…` fusionada sin reescribir historial |
| `contratos-menores`, `presupuesto-pdf` (remotas) | Desconocidas | Inspeccionar tras `fetch`; no tocar |

Sin GitFlow ni ramas permanentes adicionales. Rollback de producción: `main` no cambia hasta el lanzamiento; después, `git revert` del merge de V2 o redeploy de `prod-pre-v2`. La documentación y el código de V2 conviven en `v2/desarrollo`, lo que evita conflictos entre ramas de documentación y de código.

## 5. Orden de ejecución propuesto (requiere autorización)
1. `git fetch origin` (solo actualiza referencias remotas) e inspeccionar `origin/main`, `contratos-menores` y `presupuesto-pdf`.
2. Commit A en `feat/contingut-v2`, en el árbol actual.
3. `git switch -c v2/desarrollo origin/main`. Los archivos no rastreados viajan con el árbol, y los modificados ya estarán confirmados en A. Si `origin/main` contiene cambios en los mismos archivos, Git lo detectará y no sobrescribirá nada.
4. Commits B y C en `v2/desarrollo`; luego commit D.
5. Comprobar: `git status` limpio salvo ignorados; `git ls-files docs/project_v02 | wc -l` = número esperado; `sha256sum` frente a `99_Manifest_SHA256.md`.
6. `git tag -a prod-pre-v2 origin/main`; `push` de ramas y etiqueta solo con autorización.
