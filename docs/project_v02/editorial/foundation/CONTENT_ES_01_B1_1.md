# CONTENT-ES-01 / B1.1 — Carga editorial e integridad transversal

Fecha: 05/11/2026. Dictamen: **GO** para el alcance B1.1 implementado.
La falta de ocho páginas reales impide construir el bundle íntegro actual;
no impide aceptar la infraestructura ni autoriza publicación.

## A. Baseline y protección Git

Rama inicial: `feat/contingut-v2`.
HEAD inicial: `fca65e8ba7d75317be150e3f428be67d87825d34`.
WEB-G2-00 conserva sus commits `762e196` y `fca65e8`.
Se leyó B1.0 y se contrastaron los contratos reales, Inicio, configuración y
loader. Las condiciones C1–C3 fueron autorizadas expresamente por el encargo B1.1.
Su exigencia de Pydantic v2 sustituye los ejemplos dataclass de la auditoría.

Estado inicial completo, preservado:

```text
 M src/bafras_web/editorial/__init__.py
?? content/es/pages/inicio.yaml
?? docs/project_v02/CONTENT_ES_01_A1.md
?? docs/project_v02/CONTENT_ES_01_A2_1.md
?? docs/project_v02/CONTENT_ES_01_A2_INICIO.md
?? docs/project_v02/CONTENT_ES_01_B1_0.md
?? src/bafras_web/editorial/entities.py
?? src/bafras_web/editorial/pages.py
?? src/bafras_web/editorial/pending.py
?? src/bafras_web/editorial/primitives.py
?? src/bafras_web/editorial/references.py
?? src/bafras_web/editorial/sections.py
?? tests/integration/test_inicio_content.py
?? tests/unit/editorial/conftest.py
?? tests/unit/editorial/test_d03_contract.py
?? tests/unit/editorial/test_domain.py
?? tests/unit/editorial/test_pending.py
```

Los cuatro módulos nuevos y el informe no existían al comenzar. No se localizó
AGENTS.md en la búsqueda realizada. Se tomaron SHA-256 de los 106 archivos
preexistentes inspeccionados en src/tests/content/config/docs y pyproject.toml.
La suite inicial fue reejecutada: **292 passed**, no solo recogida.

No se cambia de rama ni se realizan commits, push, merge, add, reset, clean,
stash o reversión de archivos previos. Safe.directory se limita al comando o
entorno del proceso; no se modifica configuración Git persistente.

## B. Implementación

Únicos archivos de producción creados:

| Archivo | Responsabilidad / símbolos |
|---|---|
| `editorial/inspection.py` | Contratos Pydantic de diagnóstico, documento, inspección y resultado de integridad; aliases cerrados y orden/deduplicación |
| `editorial/integrity.py` | Recorridos tipados, índices, dependencias, resolución y regla única de elegibilidad/construcción |
| `adapters/editorial_files.py` | Discovery acotado; EditorialSource Pydantic; ruta comprobada inmediatamente antes de leer |
| `application/editorial.py` | EditorialLoadRequest Pydantic e inspect_editorial; configuración WEB y orquestación documental |

Los seis modelos nuevos heredan EditorialModel: EditorialDiagnostic,
EditorialDocument, EditorialInspection, IntegrityResult, EditorialSource y
EditorialLoadRequest. Se reutilizan strict=True, extra=forbid, frozen=True y
validate_default=True. No se introducen dataclasses, attrs, NamedTuple,
servicios, repositorios abstractos, plugins o contenedores de dependencias.

Invariantes de EditorialDocument:

- VALID requiere valor del tipo de su kind e identidad de página compatible.
- ABSENT/INVALID requieren None.
- unexpected es INVALID, no obligatorio e identificado por su source.
- Catálogos contienen tuplas homogéneas y no admiten IDs duplicados.
- Sources relativos POSIX, sin raíz absoluta, unidad Windows ni traversal.

EditorialInspection valida unicidad de documentos/orígenes, inventario exacto
de páginas esperadas, ubicación documental, locale y contexto inválido. Guarda
tuplas, no contadores paralelos ni un bundle opcional. valid_pages devuelve un
MappingProxyType derivado; missing/invalid IDs, completitud y errores son
propiedades derivadas. No tiene success, approved, published ni publishable.

Los modelos editoriales A1 contenidos conservan listas: frozen no implica
inmutabilidad profunda. Los resultados son de lectura; una edición debe
reconstruirse y validarse, no mutar listas internas.

## C. Persistencia y carga

API pública, sin nuevo CLI:

```python
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import build_editorial_bundle

inspection = inspect_editorial(
    paths,
    EditorialLoadRequest(locale="es", policy="INCREMENTAL"),
)
# Construir solo cuando inspection.can_build_bundle sea verdadero.
```

ProjectPaths.content es la raíz GLOBAL. load_site_routing conserva su mecanismo
ConfigurationError; una configuración inválida no se convierte en registro vacío.
Las páginas esperadas son tuple(sorted(routing.routes.pages)); no hay una segunda
lista de nueve IDs. Los idiomas se contrastan con LocaleSettings.codes.

Un idioma desconocido devuelve LOCALE_UNKNOWN, sin discovery/lectura editorial.
Se puede inspeccionar en/ca/de aunque no estén publicados. No existe fallback.
Si locale falta en YAML se inyecta el solicitado; si está declarado debe coincidir.
page_id debe corresponder al archivo esperado; nunca se recoloca el documento.

Formatos ratificados implementados:

| Origen relativo al locale | Forma/modelo |
|---|---|
| pages/<id>.yaml | Mapping -> PageContent |
| common.yaml | Mapping -> CommonContent |
| entities/people.yaml | Secuencia -> list[Person] |
| entities/sectors.yaml | Secuencia -> list[Sector] |
| entities/experiences.yaml | Secuencia -> list[Experience] |
| entities/resources.yaml | Secuencia -> list[DownloadableResource] |

Las colecciones se validan con TypeAdapter y se conservan como tuplas tipadas.
Un catálogo válido vacío no prueba existencia de una entidad referida.
No se crean archivos ni entidades vacíos para completar el inventario.

Discovery examina solo la raíz del idioma, pages/ y entities/, además de los
orígenes esperados. No recorre todo el repositorio; ignora auxiliares no YAML.
.yml se informa como inesperado, no alias. Directorios en lugar de documentos,
errores de acceso y symlinks fuera del locale producen errores explícitos.
Un error al examinar un directorio no se inventa como documento YAML adicional.
La contención y regularidad se comprueban otra vez antes de leer; no se promete
snapshot atómico ni ausencia total de carreras de filesystem.

La única interpretación YAML es adapters/yaml_files.load_yaml. El módulo nuevo
de filesystem devuelve rutas tipadas, no un contrato de diccionarios sin tipar.
La aplicación comprueba raíz mapping/secuencia, no convierte tipos editoriales
silenciosamente y contiene errores por documento:

- YamlFileError: error YAML o lectura, según su contexto de excepción.
- UnicodeError: entrada no interpretable.
- TypeError conocido de claves YAML no hashables: error de entrada.
- OSError recuperable y errores de resolución de ruta: error de lectura.
- Otros RuntimeError/TypeError del loader se propagan como errores inesperados;
  no se usa except Exception ni se ocultan bugs como contenido inválido.

INCREMENTAL convierte ausencias requeridas en warnings; COMPLETE en errores.
Ambos conservan documentos válidos y continúan ante errores independientes.
Presentes inválidos o adicionales desconocidos son errores en las dos políticas.

Diagnósticos tipados: identidad separada del mensaje, source relativo, selector,
destino, estado de referencia y motivo cuando corresponden. Orden estable y
deduplicación por identidad, conservando fuentes diferentes. No se vuelcan
inputs, trazas, mensajes OS o excepciones con rutas absolutas.

## D. Integridad transversal

assess_integrity recibe documentos validados y las identidades esperadas;
devuelve IntegrityResult tipado, con catálogos requeridos y diagnósticos.
Los índices de páginas, secciones, entidades y acciones comunes utilizan las
garantías de unicidad de los modelos; la unicidad de raíz de catálogo se valida
en EditorialDocument, sin seleccionar silenciosamente la primera entidad.

Recorridos explícitos cubiertos por pruebas:

- Hero/Text/Cards/Process.actions.
- CapabilityCard.actions, ApplicationExampleCard.disciplines,
  SectorPreviewCard.action y DisciplineRelationCard.discipline.
- NeedItem.actions y TextSection.contact_channels.
- SectorIndexSection.sector_refs, TeamSection.person_refs,
  ExperienceIndexSection.groups.entries.experience_ref.
- CommonContent.actions, Person.experience_refs, Experience.person_refs.
- Sector.contextual_actions/catalog_refs y DownloadableResource.sector_id.
- Referencias con y sin sección y pertenencia catálogo-sector.

No se deducen relaciones por sufijos de campos ni reflexión recursiva genérica.
No se rechazan ciclos de navegación A↔B, persona↔experiencia o sector↔catálogo:
no son relaciones de inclusión recursiva.

RESOLVED significa identidad disponible en documento válido. UNRESOLVED indica
un destino conocido como incorrecto/inexistente. UNVERIFIABLE distingue documento
requerido ausente/inválido de destino desconocido. Solo se busca una sección
si su página está disponible y validada. Los éxitos no generan un diagnóstico
por referencia por defecto; report_resolved=True permite obtenerlos al auditar.

Un catálogo se exige solo cuando una relación lo requiere. Los catálogos
presentes se validan aunque no tengan consumidores y sus relaciones pueden
requerir otros catálogos. El conjunto es finito y se calcula sin motor recursivo.

Se llama a validate_pending_fields por cada página válida. Los errores se
adaptan a PENDING_SELECTOR_INVALID; los pendientes legítimos permanecen como
EDITORIAL_PENDING. No cambia gramática, contenido ni estado de revisión.
Person.pending/Experience.pending se conservan con ENTITY_PENDING_UNCHECKED,
sin aplicarles el resolver de páginas ni bloquear únicamente por esa limitación.

URLs, contactos, PDF y evidencias no se verifican mediante red o filesystem.
Los diagnósticos EXTERNAL_* distinguen esas limitaciones de una referencia
editorial rota. No bloquean por sí solos el bundle. SourceRef no es un permiso,
una ruta física ni un registro de evidencia acreditada.

## E. Construcción controlada del bundle

bundle_is_eligible es la única regla que usa can_build_bundle. El constructor
build_editorial_bundle consulta esa propiedad y falla con ValueError estable
si no se cumplen sus precondiciones. No devuelve None o un bundle parcial.

Exige alcance no vacío, completitud requerida, ningún documento inválido ni
error, catálogos requeridos válidos, referencias editoriales resueltas y
selectores de página íntegros. La regla se aplica igual a ambas políticas.
Vuelve a evaluar integridad para impedir que una inspección construida a mano
omita diagnósticos y eluda referencias o dependencias. No hay caché.

La propiedad importa la función localmente para evitar un ciclo de importación
en la inicialización de módulos: los modelos de resultado están en inspection
y las reglas puras en integrity. No hay recursión de elegibilidad ni ciclos de
capas. La misma función sirve a consulta y construcción.

Se conserva el constructor A1 de EditorialBundle y sus defaults legítimos para
colecciones opcionales ausentes. Se reutilizan modelos y orden editorial.
Un conjunto completo draft o approved con pendientes técnicos puede construir
bundle; esto no acredita revisión completa ni publicación.

## F. Pruebas

Archivos nuevos:

- tests/unit/editorial/test_b11_inspection.py.
- tests/integration/test_editorial_loading_b11.py.
- tests/contracts/test_editorial_b11_architecture.py.

Resultados ejecutados con `.venv/Scripts/python.exe -B -m pytest`:

| Grupo | Resultado |
|---|---:|
| Baseline completo anterior a B1.1 | 292 passed |
| Nuevas pruebas B1.1 focalizadas, ejecución final | 108 passed |
| Regresión explícita A1/A2/A2.1 | 211 passed |
| Contratos de arquitectura, existentes y nuevos | 17 passed |
| Suite completa final | **400 passed** |

Resultado final: 0 fallos, 0 omitidas. El aumento es de 108 pruebas frente al
baseline. El total completo incluye las 292 anteriores: no se afirma regresión
superada sin ejecución. La prueba de symlink usa enlace real si el token Windows
lo permite; si no, simula su resolución fuera de raíz sin omitir la comprobación.

Se prueban invariantes Pydantic, coerciones, fuentes relativas, estados,
orden/deduplicación, YAML roto/duplicado, raíz errónea, UTF-8, claves no hashables,
errores de lectura, desaparición de archivo, directorio en lugar de YAML,
locales, fuentes adicionales, catálogos opcionales inválidos, duplicados,
referencias en todas sus ubicaciones, ciclos válidos, recursos incompatibles,
pendientes, inspección manual sin diagnósticos, bundle draft completo,
determinismo entre temporales/órdenes y reutilización del parser.

Los fixtures sintéticos solo se escriben en temporales de pytest fuera del
repositorio. No se migran ni crean páginas ficticias en content/.
Se utiliza un temporal nuevo y la excepción safe.directory solo en el entorno
del proceso para las pruebas Git existentes. No se cambian tests protegidos.

## G. Aceptación real de Inicio

Inspección ejecutada sobre el checkout real, sin modificar inicio.yaml:

| Dato | INCREMENTAL | COMPLETE |
|---|---:|---:|
| Idioma | es | es |
| Páginas esperadas | 9 | 9 |
| Páginas válidas | inicio | inicio |
| Ausentes | 8 | 8 |
| Inválidas | 0 | 0 |
| DOCUMENT_MISSING | 8 warning | 8 error |
| REFERENCE_TARGET_UNAVAILABLE | 14 warning / UNVERIFIABLE | 14 warning / UNVERIFIABLE |
| EDITORIAL_PENDING | 8 info | 8 info |
| PENDING_SELECTOR_INVALID | 0 | 0 |
| documents_complete | false | false |
| can_build_bundle | false | false |

Ausentes: automatizacion_control, capacidades, contacto, infraestructuras,
proyectos_experiencia, sectores, sistemas_energeticos y sobre_bafras.
INCREMENTAL suma 22 warnings y 8 info; COMPLETE suma 8 errores, 14 warnings y
8 info. No se ocultan ausencias ni se declara desconocida una página configurada.
Los cinco documentos de common/entidades están ausentes pero no son requeridos
por Inicio, por lo que no generan ausencias obligatorias adicionales.

El resultado coincide con B1.0; no fue necesario modificar contenido o expectativas.

## H. Arquitectura y compatibilidad

Producción nueva: solo los cuatro módulos autorizados. Los símbolos se importan
desde sus módulos; editorial/__init__.py no se cambia. Nuevos contratos usan
EditorialModel; no se duplica su ConfigDict.

Application reutiliza ProjectPaths/load_site_routing/load_yaml. Adapters no
importa application. Editorial no importa WEB, YAML, filesystem, templates o
generación HTML. Las pruebas existentes de arquitectura siguen aprobadas.
No se añaden dependencias; Pydantic y su core ya están en el entorno existente.

No se modifican site/, media/, localization/, módulos WEB existentes,
configuración, manifiestos, pyproject.toml, documentos maestros, maquetas,
Inicio o pruebas/informes anteriores. Tampoco se introduce CLI, esquema de
versionado, MediaRef, publicación, traducción, huellas o HTML.

## I. Riesgos residuales

- Solo Inicio tiene YAML real: el bundle completo actual seguirá rechazándose
  hasta migrar las otras páginas y las entidades que sus relaciones requieran.
- SEO y etiquetas H05 siguen pendientes; los cinco medios esperan MediaRef.
- Los pendientes de entidad y la veracidad/autorización de evidencias permanecen
  fuera del resolver de páginas. Sus límites se expresan en diagnósticos.
- SiteRouting continúa siendo un registro técnico, no prueba de publicación
  por página/idioma. No se usa como permiso de release.
- frozen es superficial para modelos A1 contenidos. No editar sus listas en una
  inspección ya construida; reconstruir y validar los datos editados.
- No hay snapshot atómico del filesystem; la doble comprobación reduce carreras,
  pero debe repetirse una inspección si hay cambios concurrentes.
- El TypeError de claves no hashables se reconoce de forma acotada al contrato
  observado del loader existente. Cambios futuros a ese loader exigirán revisar
  su prueba de compatibilidad, sin capturar todos los TypeError indiscriminadamente.
- Los cambios anteriores y B1.1 siguen sin commit, por instrucción expresa.

## J. Dictamen y cierre

**GO.** B1.1 implementa los contratos autorizados con Pydantic v2, carga única,
inventario completo del idioma, políticas de ausencias, integridad referencial,
catálogos condicionales y construcción controlada. Las pruebas y la aceptación
real respaldan el alcance, sin confundirlo con publicación.

El estado Git final mantiene el baseline y añade exactamente ocho archivos:
cuatro módulos, tres archivos de pruebas y este informe. La comparación SHA-256
de los 106 archivos preexistentes confirma cero modificaciones y cero bajas;
no se observaron cambios concurrentes ajenos. La revisión de whitespace de los
ocho archivos nuevos no detectó errores. HEAD final:
`fca65e8ba7d75317be150e3f428be67d87825d34`, en `feat/contingut-v2`;
sin commits, push, operaciones destructivas o migración de las ocho páginas.

La intervención se detiene aquí. No se inicia ninguna fase posterior.
