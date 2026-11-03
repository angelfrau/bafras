# BAFRAS WEB — WEB-00 · Línea base
**Fecha:** 03/11/2026 · **Estado:** línea base **local** documentada y respaldada. **No existe todavía una línea base Git recuperable de todo el trabajo**: la documentación G1, la biblioteca de medios y los cambios de septiembre no están confirmados. Quedan protegidos por el respaldo externo de §3 hasta que se ejecuten los commits A–C de `WEB_00_PLAN_SANEAMIENTO.md`.

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
