# WEB-V02 R2 · Cierre del sitio español en preview

Fecha: 07/11/2026. **STATUS: COMPLETED** para WEB-V02; publicación no autorizada.

## BASELINE

Rama inicial/final `feat/contingut-v2`; HEAD `3927e5f73fcfca7e9eeed7eb37858bfe168c4df4`.
Sin ramas nuevas, commits, push ni operaciones destructivas Git. Baseline reproducida: **660 passed**.
Python del proyecto: `.venv/Scripts/python.exe` (3.12.10). El Python global carece de las dependencias.
Se usaron temporales en `../.web-v02-tmp/` y `safe.directory` por proceso para superar las diferencias
de cuenta de Windows; ninguna configuración Git global se modificó.

Trabajo heredado: 8 archivos versionados modificados y 25 entradas sin seguimiento (varias son directorios),
incluidos build individual, Jinja, componentes Inicio, CSS/JS, composición, MEDIA y pruebas de WEB-V01.
Se conserva: inventario inicial y huellas en `build/web-v02-evidence/git-initial.txt` e `initial-hashes.json`.
Las autoridades D03 V1.22, D04 V2.4 y D05 V4.12, contratos y nueve ZIP aprobados se consultaron;
no se modificaron D03/D04/D05, modelos CONTENT, datos editoriales ni estados `draft`.

## DEC-10

Registrada la declaración expresa BAFRAS en `WEB_G1_CLOSE_DECISIONES.md` y `attribution.md`.
Alcance: **H01, H03, H04, H05, D02, I03, E02, E06 y D01**, nueve derivados únicos seleccionados por D05.
El manifiesto registra autorización declarada, referencia documental y SHA-256 del derivado.
Autores, créditos, licencias originales, URLs y demás trazabilidad permanecen intactos.
Los restantes activos conservan autorización pendiente por defecto. No se afirma auditoría jurídica externa.
Se actualizó únicamente el hash documental de DEC-10 en `99_Manifest_SHA256.md`.

## PAGES

Todas las páginas están generadas y comprobadas. **9 HTML, 51 secciones, 16 combinaciones kind/purpose**.
En la tabla, los componentes comunes incluyen hero y text donde corresponde.

| Página | URL | Secciones | Componentes y particularidades | Estado |
|---|---|---:|---|---|
| Inicio | `/` | 7 | hero, capabilities, needs, workflow, sector_preview, text; 5 imágenes | OK |
| Capacidades | `/capacidades/` | 5 | capabilities en filas, application_examples, modalities, text | OK |
| Infraestructuras | `/capacidades/infraestructuras-instalaciones/` | 7 | needs, technical_areas, deliverables, text; I03 | OK |
| Sistemas energéticos | `/capacidades/sistemas-energeticos/` | 7 | needs 3/2/1, technical_areas en capítulos, deliverables pino; E02/E06 | OK |
| Automatización y control | `/capacidades/automatizacion-control/` | 7 | needs, technical_areas, deliverables, discipline_relations; D01/D02 | OK |
| Sectores | `/sectores/` | 5 | sector_index con seis entidades y enlaces contextualizados | OK |
| Proyectos y experiencia | `/proyectos-experiencia/` | 4 | experience_index, grupos editoriales sin fichas vacías ni referencias inventadas | OK |
| Sobre BAFRAS | `/sobre-bafras/` | 5 | team con tres personas, principles, text | OK |
| Contacto | `/contacto/` | 4 | form desactivado, text con canales reales; composición a dos columnas | OK |

Inventario detallado con cada sección, plantilla, medio, enlace y dependencia:
`build/web-v02-evidence/page-matrix.json`. Lectura de las nueve maquetas: `mockups-review.json`.

## IMPLEMENTATION / ARCHITECTURE

- `application/build.py`: motor único para página y sitio; `BuildInputs` comparte dependencias de una ejecución.
  Mapeo explícito de componentes, resolución de entidades, imágenes y enlaces mediante contratos existentes.
- `adapters/site_integrity.py`: inspección del árbol físico y fragmentos; no decide contenido ni routing.
- `adapters/filesystem.py`: staging hermano, promoción con backup y recuperación; escritura/copia reutilizadas.
- `site/links.py`: también resuelve enlaces de entidades Sector. `site/composition.py`: variantes compartidas D05.
- `media/assets.py`: autorización independiente de licencia y huella opcional del derivado; sin excepciones por ID.
- Plantillas: layout/header/footer heredados, composición general por secciones y composición específica de Contacto;
  siete componentes nuevos para familias distintas, reutilización de listas para deliverables/modalities.
- CSS: tokens y patrones heredados, variantes semánticas sin reglas por identificador de página o sección.

No hay segunda CLI, segundo catálogo, routing alternativo, modelos editoriales duplicados, backend,
proveedor externo ni cachés globales de bundles. Jinja no lee YAML ni archivos MEDIA.
La dataclass de dependencias evita repetir carga; no reproduce `PageContent` ni sus secciones.

## BUILD

Con el entorno del proyecto activado:

```powershell
python -m bafras_web build --locale es --all --mode preview
python -m bafras_web build --locale es --page inicio --mode preview
```

Salida completa: `build/preview/`, con **20 archivos: 9 HTML, 9 WebP, 1 CSS y 1 JS**.
Inicio corresponde a `index.html`. El build individual conserva además el alias histórico
`es/inicio/index.html` y devuelve esa ruta. Cada ejecución sustituye preview por su selección validada;
para disponer del sitio navegable completo debe usarse `--all` como último build.

Dos builds independientes del sitio final producen las mismas rutas, bytes y SHA-256 de los 20 archivos.
Evidencia: `build/web-v02-evidence/build-hashes.json`; segunda salida en `build/repro-web-v02/preview/`.
No hay timestamps variables en los artefactos, archivos antiguos mezclados ni escritura en `dist/`.

Staging probado en Windows: render/copia/escritura/enlaces fallidos conservan todos los archivos previos;
fallo de promoción restaura el directorio anterior; fallo adicional de recuperación conserva el backup y
comunica su ubicación. Se limpian los temporales propios. Dos renombrados no garantizan atomicidad absoluta.

## NAVIGATION / CONTACTO

**220 referencias HTML** comprobadas sobre destinos físicos, incluidos header/footer, referencias entre
páginas, anclas, CSS, JS e imágenes. Los enlaces externos, `mailto:` y `tel:` se distinguen sin hacer
peticiones a terceros. El build completo rechaza destinos inexistentes y fragmentos rotos.
El build individual permite expresamente los destinos SITE conocidos fuera de su selección.

Contacto usa `info@bafras.com` y `+34 610 903 179` desde las fuentes existentes.
No hay integración de envío aprobada: campos y botón están desactivados, sin elemento form ni envío,
con aviso técnico explícito. No se muestra confirmación de éxito ni se capturan consultas.
Privacidad y proveedor siguen pendientes; la recepción real de correo/llamadas no ha sido acreditada.

## VISUAL / ACCESIBILIDAD

Chrome **157.0.8103.38**, servido mediante HTTP loopback con cierre del servidor propio al finalizar.
**54 comprobaciones**: las nueve páginas a **320/375/390/768/1024/1440 px**.
Sin errores HTTP/JS, overflow horizontal detectado, imágenes rotas, IDs repetidos ni saltos de encabezado;
un h1 y landmarks principales por página. Medición de contraste de texto renderizado con composición alfa
de fondos; controles desactivados excluidos. No constituye una auditoría WCAG completa.

Probados con teclado: skip-link, foco visible, menú mediante Enter/Escape, devolución de foco y navegación
real hacia Capacidades/INF. Contacto comprobado sin capacidad de envío. Diez capturas completas revisadas:
Inicio escritorio/móvil, las tres especialidades, Capacidades, Sectores, Equipo, Experiencia y Contacto móvil.
Evidencia: `build/web-v02-evidence/browser-qa.json` y los PNG del mismo directorio.

Corrección detectada: eyebrow verde pequeño sobre arena en ejemplos de aplicación daba 4,31:1;
ahora usa pino conforme a D05. Se preservó la composición de Inicio y se verificó visualmente.
**Zoom real al 200 % pendiente de revisión manual**: Chrome headless no confirmó cambio de DPR/ancho CSS
con el atajo de zoom. No se presenta viewport reducido ni emulación de escala como zoom real.

## TESTS

Baseline: **660 passed**. Pruebas focalizadas de integración/arquitectura: **90 passed** antes de añadir
cuatro casos de composición/SHA. Suite completa final: **683 passed**.
Cobertura: YAML reales → modelos → bundle → routing → MEDIA → Jinja → HTML/assets, contenido visible
incluidas entidades, CLI, selección, referencias, composición, staging, fallos y preview/release.
Dos expectativas antiguas se actualizaron porque Sectores ya renderiza y DEC-10 ya autoriza medios;
se mantienen las comprobaciones de fallo y protección editorial de release.
Logs: `build/baseline-r2.txt`, `build/focused-r2.txt`, `build/full-r2.txt`.

## ISSUES / RELEASE READINESS

No hay bloqueos técnicos conocidos para el preview completo. Release sigue rechazado sin producir salida.
Inventario exacto por página: `build/web-v02-evidence/release-blockers.json`.

Pendientes priorizados para publicación:

1. Aprobar estados editoriales, servicios D01 y gates; resolver los pendientes CONTENT mediante su propietario.
   Los huecos media ya integrados conservan sus marcadores editoriales originales por instrucción del encargo.
2. Aprobar SEO de Inicio/Capacidades/INF/ENE y descripción de Experiencia; decidir H05 y tratamiento público
   de Experiencia sin referencias, confirmar datos profesionales y consentimientos del equipo.
3. Confirmar identidad jurídica/legales/privacidad y operatividad de correo/teléfono; decidir proveedor de formulario
   si se habilita envío, con antispam y E2E real. No se eligió ninguno en WEB-V02.
4. Confirmar logo maestro y presentación definitiva de créditos, manteniendo los créditos visibles actuales.
   DEC-10 ha resuelto la autorización declarada de los nueve archivos, no la ratificación de marca.
5. Comprobar zoom real 200 %, completar auditoría de accesibilidad/rendimiento y aceptación visual final.
6. Decidir hosting/dominio canónico/idiomas y completar salida release, canonical/hreflang/robots/sitemap,
   legales, 404 y configuración de despliegue. Sin habilitar release mediante excepciones artificiales.

## DIFF / NEXT ACTION

Cambios de sesión: 23 archivos existentes modificados y 13 nuevos (incluido este informe); ninguno eliminado.
El diff de sesión se distingue del trabajo heredado mediante `session-diff.json`, huellas y estados Git.
Se conservaron los cambios heredados de `configuration.py`, pruebas multilingües y baseline editorial.
`git diff --check` sin errores; D03/D04/D05 y los nueve ZIP aprobados permanecen íntegros.

Siguiente encargo mínimo propuesto, **no ejecutado**: WEB-RC-01, resolver decisiones de publicación anteriores,
aprobar contenido/legales/configuración y generar una release candidate reproducible con el mismo motor,
QA final y paquete de despliegue revisable para el hosting elegido. Despliegue sujeto a autorización separada.
