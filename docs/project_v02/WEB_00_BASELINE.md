# BAFRAS WEB — WEB-00 · Línea base
**Fecha:** 03/11/2026 · **Estado (WEB-00 FINAL):** **existe línea base Git** en `feat/contingut-v2` (§8). Los apartados 1–7 describen el estado inicial anterior al saneamiento. Texto original: línea base **local** documentada y respaldada. **No existe todavía una línea base Git recuperable de todo el trabajo**: la documentación G1, la biblioteca de medios y los cambios de septiembre no están confirmados. Quedan protegidos por el respaldo externo de §3 hasta que se ejecuten los commits A–C de `WEB_00_PLAN_SANEAMIENTO.md`.

## 1. Referencia Git
| Elemento | Valor |
|---|---|
| HEAD | `7dd275324ed1212662f099b69fa3cdd1a8930bff` (`feat/contingut-v2`) |
| `main` local / `origin/main` real | `04c92c8` / `4af79e0` (sin inspeccionar; requiere `fetch`) |
| Cambios rastreados sin confirmar | 7 archivos (+1125/−212) antes de WEB-00; `.gitignore` (+10) en WEB-00 |
| No rastreados | 151 archivos antes de WEB-00 (`lista_no_rastreados.txt` del respaldo) |
| Staged / stash / tags | ninguno |

## 2. Pruebas de referencia

| Ejecución | Resultado |
|---|---|
| Árbol de trabajo · `python -B -m pytest -q -p no:cacheprovider` | **18 passed** |
| Árbol de trabajo · `python -B tools/validate.py` | **Validation passed**; avisos heredados: 33 placeholders y 10 «verify» |
| HEAD `7dd2753` exportado con `git archive` a un directorio temporal · pytest | **4 passed** |
| HEAD exportado · `validate.py` | **Validation passed**, sin avisos |
| Entorno | Python 3.12.10; pydantic 2.12.5 instalado; **jinja2 no instalado**; `pyproject.toml` sin dependencias (WGR-037) |

Fallos heredados: ninguno. Los 43 avisos de publicación corresponden al contenido del sitio heredado y no son regresiones.

## 3. Respaldo y protección (ejecutado, no destructivo)
Ubicación: `Web BAFRAS/_respaldo_WEB-00_20261103/`, fuera del repositorio, por lo que no altera `git status`.

| Archivo | Contenido | Verificación |
|---|---|---|
| `bafras_refs_locales.bundle` | `git bundle --all`: ramas locales y remotas conocidas | `git bundle verify` → *is okay* |
| `cambios_rastreados_vs_HEAD_7dd2753.patch` | `git diff HEAD --binary` | `git apply --check` sobre HEAD exportado: OK. Al aplicarlo, 5/7 archivos son idénticos byte a byte y 2 coinciden salvo finales de línea (`autocrlf`) |
| `rastreados_modificados.tar` | Los 7 archivos modificados, byte a byte | Extraído y comparado con `cmp`: idénticos |
| `no_rastreados.tar` (112 MB) | Los 151 archivos no rastreados | Extraído y comparado con `cmp`: **158/158 idénticos, 0 diferencias** (7 + 151) |
| `estado_git.txt`, `lista_no_rastreados.txt`, `cambios_rastreados_stat.txt` | Estado de referencia | — |
| `SHA256SUMS.txt` | Hashes de todo lo anterior | `sha256sum -c SHA256SUMS.txt` |

El respaldo se hizo **antes** de las ediciones documentales de WEB-G1-CLOSE. Los archivos editados después (acta, D04, D05, briefing, informe REVIEW-01, manifiesto, `.gitignore`) tienen su versión anterior en el tar.

## 4. Procedimiento de recuperación
```bash
B="../_respaldo_WEB-00_20261103"; cd "$B" && sha256sum -c SHA256SUMS.txt     # 1. integridad
git clone bafras_refs_locales.bundle bafras_recuperado                        # 2. historial local
cd bafras_recuperado && git checkout feat/contingut-v2
tar -xf "../rastreados_modificados.tar"                                       # 3. cambios exactos (bytes)
tar -xf "../no_rastreados.tar"                                                # 4. no rastreados
git status --porcelain -uall | diff - <(tail -n +2 ../estado_git.txt)         # 5. comparar con el estado de referencia
python -B -m pytest -q && python -B tools/validate.py                         # 6. 18 passed / Validation passed
```
Para restaurar el contenido de los archivos rastreados, usar el tar, no el parche: el tar conserva los finales de línea exactos.

## 5. Archivos protegidos (no modificar sin autorización)
`index.html`, `css/*`, `js/*`, `tests/*`, `tools/*`, `CNAME`, `assets/images/{brand,team,experience,home}`, la biblioteca `BAFRAS_Website_Visual_Assets_V1/` y `docs/project_v02/maquetas_aprobadas/*.zip` (hashes en `99_Manifest_SHA256.md`).

## 6. Estrategia de ramas
Resumen de `WEB_00_PLAN_SANEAMIENTO.md` §4: `main` = producción intacta, con etiqueta `prod-pre-v2`; `feat/contingut-v2` = trabajo heredado congelado; `v2/desarrollo` = única rama de integración de V2, creada desde `origin/main` actualizado. Primera operación pendiente de autorización: `git fetch origin`, sin efecto en el árbol de trabajo.

## 7. Condición para declarar la línea base Git
Commits A–C ejecutados, `git fetch` realizado, `origin/main` inspeccionado, etiqueta `prod-pre-v2` creada y estas pruebas repetidas con el mismo resultado. Hasta entonces, la línea base es **local y respaldada**, no versionada.

## 8. Resultado WEB-00 FINAL (03/11/2026)

**Estrategia (decisión de dirección):** `main` (`04c92c8` local) es producción y no se ha modificado. La única rama de desarrollo es `feat/contingut-v2`. No se ha hecho `push`, `fetch` ni reescritura de historial, y no se han creado ramas.

| Commit | Contenido | Pruebas |
|---|---|---|
| `601eec4` A | Trabajo de septiembre: 7 archivos productivos y 11 documentos | 18 passed |
| `88b17af` B | D02 V1.0-R, D03 + adenda 03.G1-02, D04, D05, acta, maquetas, auditorías, evidencias, `docs/audits` | — (solo documentación) |
| `c5156ec` C | `misc/a`, 5 logos duplicados y 15 documentos heredados superados eliminados; `.gitignore`; `.gitattributes` | 18 passed |
| `bf56666` D | Biblioteca reorganizada en `assets/images/` + `media-library/`; rutas actualizadas | 18 passed; 107 enlaces OK |
| E | Informes WEB-00/G1-CLOSE actualizados y manifiesto | ver §9 |

**Eliminados y por qué** (todos recuperables desde el historial o el respaldo):

| Elemento | Motivo | Comprobación previa |
|---|---|---|
| `assets/images/misc/a` | Residuo de 2 bytes | Sin referencias |
| `brand/logos/logo_h_blanco.png`, `logo_h_deep.png`, `logo_v_blanco.png`; `brand/symbols/simbolo_blanco.png`, `simbolo_deep.png` | Copias a media resolución de los maestros `BAFRAS_*` | Diferencia media < 1 tras reescalar; sin referencias |
| `docs/home-v2-1-structure-closeout.md`, `home-v2-visual-evidence.md`, `language-audit-es.md`, `terminology-es.md`, `website-visual-assets.md` | Documentación del sitio heredado superada por D03/D05 (`terminology-es` contradice la nomenclatura de D03) | Sin referencias desde código, pruebas ni enlaces |
| 10 documentos de septiembre (`capabilities-*`, `content-review-backlog`, `energy-*`, `infrastructure-*`, `visual-component-inventory`, `visual-evidence-map`, `content/*`) | Superados por D03 V1.22/D05 V4.12; preservados en el commit A | Igual |
| 2 copias de `demo_graphics.py` | Idénticas (mismo MD5) | Se conserva una en `media-library/generators/` |
| `tests/__pycache__`, `tools/__pycache__` | Cachés | Ignoradas |

**Conservados a propósito:**
- `docs/architecture.md` y `docs/visual-system-v1.md`, que las pruebas del sitio heredado leen.
- `docs/audits/`, antecedente de la decisión de arquitectura.
- `experience/mep/*`, fotografías propias pendientes de autorización.
- Los dos logotipos SVG `*_deep` / `*_deep_corregido`, hasta decidir el maestro (DEC-10).

**Estructura final de recursos visuales:**
```
assets/images/                 publicables (versionados, 8 MB)
  brand/{logos,symbols,favicon,social}   logos maestros y exportaciones
  team/*.png                     retratos usados por el sitio
  home/{hero,capabilities,vision}  ·  capabilities/{infrastructure,energy,digital}/…  ·  sectors/…
  experience/mep/                fotografías propias (pendientes de autorización)
media-library/                 fuentes no publicables
  README.md                      integración, recuperación y verificación de originales
  manifests/                     media-manifest.yaml (fuente de verdad), assets-inventory.csv, attribution.md
  reports/                       acquisition-report, missing-assets, contact-sheet.pdf
  generators/demo_graphics.py    gráficos sintéticos E01/E07/D06
  originals/<ID>/source.json     procedencia + SHA-1 (versionado)
  originals/<ID>/<ID>_original.* Commons, ≈95 MB: SOLO LOCAL (.gitignore), SHA-1 26/26 OK
  originals/team/, originals/diagrams/  originales propios (versionados)
assets/downloads/              (previsto para catálogos PDF; aún no existe)
```

**Residuo local no eliminable:** `.pytest_cache/` (permisos del sistema; ignorado por Git).

**Riesgos residuales:**
1. Los originales de Commons dependen de la copia local, Wikimedia Commons y el respaldo. No están en Git.
2. `origin/main` (`4af79e0`) y las ramas remotas `contratos-menores` y `presupuesto-pdf` no se han inspeccionado; habrá que hacerlo antes de cualquier integración futura.
3. El resto del repositorio sigue con `autocrlf` sin normalizar.
4. D02 es una reconstrucción pendiente de ratificar.
5. El sitio heredado y sus pruebas siguen en la rama hasta que WEB-01/02 los sustituyan.

## 9. Validación final
Ver el resumen del commit E: pruebas, validador, enlaces, manifiesto, maquetas, originales y estado Git.
