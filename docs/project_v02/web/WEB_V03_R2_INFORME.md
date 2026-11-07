# WEB-V03 R2 · Consolidación y Contacto R1

07/11/2026 · **STATUS: COMPLETED**, incluido dossier Fase K. No autoriza publicación.

## BASELINE

Rama `feat/contingut-v2`; HEAD inicial `3927e5f73fcfca7e9eeed7eb37858bfe168c4df4`.
Baseline ejecutada: **683 passed**, nueve páginas/51 secciones/16 combinaciones, 20 archivos de preview.
Índice inicial vacío; trabajo WEB-V01/02 heredado: 12 archivos versionados modificados y 27 entradas
sin seguimiento, varias correspondientes a directorios. Ningún cambio ajeno identificado.
Estados/huellas iniciales y build anterior: `build/web-v03-evidence/` y `build/web-v03-baseline/preview/`.

## AUDIT FINDINGS / REFACTORING

Sin pérdida de datos ni bloqueos P0 detectados.

| Prioridad / módulo original | Problema demostrado | Intervención / resultado |
|---|---|---|
| P1 · application/build.py | Coordinación mezclada con contexto visual, reglas de composición y operaciones físicas | Contexto en application/presentation.py; materialización/verificación física en adapters/build_output.py; composición en SITE. Un único motor y una carga por ejecución |
| P2 · application/configuration.py | Genéricos devolvían BaseModel o un tipo implícito, perdiendo el contrato concreto | TypeVar y retornos explícitos, estrechamiento de errores; consumidores reciben el modelo preciso |
| P2 · adapters/site_integrity.py | Esquemas no permitidos se aceptaban si la URL tenía host | Rechazo de esquema independiente del host; pruebas FTP/javascript con host. No modifica destinos válidos |
| P2 · contexto/plantillas | Datos de contacto duplicados; plantillas de páginas idénticas y dispatcher cards sin uso | Valores visibles de SITE, PageContext tipado, composición general única; retirados form/cards e inicio/contacto redundantes |
| P2 · QA heredado | Dependencia de rutas locales y controles de formulario retirados; capturas parciales del inventario | scripts/capture_site.py independiente, rutas SITE, comprobación HTTP y 18 capturas con manifest/huellas |

Se conservaron `filesystem.staged_directory`, recuperación y políticas de publicación.
CSS sigue en un archivo; JS sin cambios. No se introducen framework, capa de dominio nueva ni dependencias
de ejecución. Las dos extracciones productivas separan responsabilidades reales, sin wrappers de delegación.
Inventario técnico con funciones, imports y control de flujo: `build/web-v03-evidence/technical-inventory.json`.

## ARCHITECTURE

Se preservan `BuildRequest`, `BuildError`, `render_page`, `build_page`, `build_site` y el alias individual.
`BuildInputs` sigue perteneciendo a una ejecución; se rechaza reutilizarlo con un locale distinto.
`PageContext` es TypedDict, no otro modelo editorial. CONTENT y los modelos originales no se duplican.
SITE mantiene routing/enlaces/selección de composición; MEDIA, manifiesto/metadatos/autorización.
Los adaptadores realizan I/O; Jinja recibe referencias resueltas y no carga YAML ni MEDIA.
Pruebas de dependencia y ciclos superadas. La incorporación de un componente se concentra en el mapeo
kind/purpose; una página con componentes existentes continúa seleccionándose desde el catálogo SITE.

## CONTACT

[CONTACT-R1](CONTACT_R1.md) registra la decisión aprobada: Release 1.0 solo correo/teléfono,
sin formulario ni proveedor pendiente. Datos de `config/site.yaml`, validación E.164 conservada.
CO-02 pasa explícitamente de form a text y conserva título/ayuda aprobados; CO-01/03/04 conservan
su texto. Se retiran exclusivamente campos, estados de envío, valores duplicados y el pendiente de
privacidad del formulario eliminado. El resto de requisitos legales no cambia.

Resultado: nueve páginas y **51 secciones/15 combinaciones**; Contacto con enlaces mailto/tel, sin
controles activos/desactivados ni avisos técnicos. CA/EN/DE permanecen byte a byte intactos y pendientes
de adaptación revisada de Contacto; los tests delimitan exactamente esa diferencia, sin omisiones ni fallback.
D03/D04/D05 y las nueve maquetas no cambian; la nueva decisión funcional posterior queda trazada.
DEC-10 se conserva sin reabrir autorización de imágenes.

## FRONTEND / BUILD

Mismos tokens y patrones D05. Contacto usa la variante direct_contact, dos columnas en escritorio y una en
móvil; no quedan espacios de controles retirados. Se eliminan estilos exclusivos del formulario.
Las otras ocho páginas conservan HTML idéntico y capturas desktop/mobile idénticas al baseline.

```powershell
python -m bafras_web build --locale es --all --mode preview
python -m bafras_web build --locale es --page inicio --mode preview
```

Build completo en `build/preview/`: **9 HTML + 9 WebP + CSS + JS = 20 archivos**. Las mismas nueve rutas SITE,
Inicio en `/`. Solo cambian CSS y contacto/index.html respecto al baseline; las otras 18 huellas coinciden.
Dos builds independientes finales idénticos por SHA-256. Build individual verificado en salida separada.
Cada ejecución reemplaza preview por su selección; para navegación completa debe finalizarse con --all.
Referencia final: `build/web-v03-evidence/final-build-hashes.json`.

Staging probado: errores de render/copia/escritura/integridad/promoción conservan la salida previa;
fallo adicional de recuperación conserva el backup. No se promete atomicidad absoluta de directorios.
Preview mantiene aviso/noindex, sin canonical/hreflang públicos; release sigue bloqueado, sin escribir dist/.

## TESTS

**Baseline: 683 passed. Suite completa final: 687 passed**, sin skips ni xfail.
Incluye contratos de arquitectura, caracterización, CLI, modelos reales, integración y E2E físico.
Las cuatro nuevas comprobaciones cubren esquemas con host, mezcla de locales y dato de Contacto desde SITE.
Las pruebas de contenido preservan la comparación independiente D03 y aplican únicamente CONTACT-R1.
Los fallos se inyectan ahora en el adaptador extraído; las garantías verificadas no se han debilitado.
Logs locales: `build/web-v03-evidence/baseline-tests.txt`, `focused-tests.txt`, `full-tests.txt` y `staged-tests.txt`.

## VISUAL REVIEW ARTIFACTS

Directorio exacto desde la raíz del checkout: **`artifacts/web-v03/visual-review/es/`**.
Herramienta: Playwright con Chrome real **157.0.8103.38**, HTTP loopback, DPR 1.
**18 PNG completos generados correctamente:** 9 en desktop/ y 9 en mobile/, más manifest.json.
Viewport desktop **1440×900**, mobile **390×844**; fullPage, menú cerrado, fuentes/imágenes cargadas,
animaciones/transiciones anuladas solo durante captura. No hay archivos faltantes, capturas vacías,
documentos erróneos, errores HTTP/JS ni imágenes rotas detectadas.

El manifest registra cada page_id, URL local, ruta pública, rutas y dimensiones de ambos PNG, estado,
errores, huellas de archivos/build/fuentes y comparación anterior. Los PNG abarcan cabecera–footer;
las alturas van de 1780 a 6154 px en desktop y de 1944 a 9526 px en mobile.
Las **16 comparaciones fuera de Contacto son idénticas**; sus dos capturas cambian intencionadamente.

QA adicional: **54 comprobaciones** (nueve páginas × 320/375/390/768/1024/1440), sin overflow horizontal
detectado, con encabezados/landmarks/alt/contraste básico correctos. Teclado: skip-link, foco visible,
Enter/Escape, menú y navegación, foco en ambos canales de Contacto. Servidores propios cerrados al finalizar.
Zoom real al 200 % pendiente manual: Chrome headless no confirmó cambio de zoom; no se sustituye por viewport.

El dossier se prepara para revisión del responsable BAFRAS. **No se declara realizada revisión visual humana**
ni auditoría WCAG completa. Script versionado; imágenes/manifest ignorados y excluidos del commit.

## GIT

Un único commit local autorizado: `refactor(web): consolidate site architecture and finalize contact`.
Consolida WEB-V01, WEB-V02 y WEB-V03, fuente/configuración/tests/documentación revisados.
Índice preparado por lista explícita de 66 archivos, sin git add indiscriminado. Comprobaciones de diff/staged,
fuentes nuevas, eliminaciones, credenciales y artefactos, suite completa con índice preparado y build final.
No se incluyen .venv, builds, temporales, cachés, PNG ni manifest del dossier.
Se registra el hash efectivo y el estado posterior en la entrega y en `build/web-v03-evidence/git-post-commit.json`.
Sin ramas nuevas, push ni modificación de main. Los artefactos ignorados permanecen disponibles localmente.

## RESIDUAL ISSUES / RELEASE READINESS

Sin defectos bloqueantes conocidos para el alcance WEB-V03. Para release siguen pendientes:

1. Estados editoriales aprobados, SEO incompleto, H05, habilitación de servicios D01 y gates.
2. Identidad jurídica/legales/privacidad general, confirmación de datos profesionales y operatividad
   del correo/teléfono. No se enviaron mensajes ni llamadas de prueba.
3. Logo maestro y aceptación de presentación de créditos; autorización DEC-10 ya adoptada.
4. Zoom 200 % real, revisión visual humana, accesibilidad/rendimiento finales.
5. Hosting/dominio/idiomas y salida release (canonical/hreflang/robots/sitemap/404/despliegue).

No queda pendiente decidir proveedor de formularios para R1. CA/EN/DE requieren adaptar Contacto y revisión
antes de habilitarse. Siguiente encargo: resolver decisiones de publicación y producir release candidate
reproducible usando el motor actual, sin desplegar hasta autorización. No ejecutado en esta intervención.
