# CONTENT-ES-01 / A2.1 — Endurecimiento de contratos

Fecha: 05/11/2026. Alcance correctivo: paridad semántica de Inicio,
resolución local de pendientes y pruebas de estados. No inicia B1.

## A. Baseline

Rama `feat/contingut-v2`; HEAD inicial
`fca65e8ba7d75317be150e3f428be67d87825d34`.
La ejecución inicial reproduce las 232 pruebas aprobadas de A2.

Estado inicial completo de archivos modificados/sin seguimiento:

```text
 M src/bafras_web/editorial/__init__.py
?? content/es/pages/inicio.yaml
?? docs/project_v02/CONTENT_ES_01_A1.md
?? docs/project_v02/CONTENT_ES_01_A2_INICIO.md
?? src/bafras_web/editorial/entities.py
?? src/bafras_web/editorial/pages.py
?? src/bafras_web/editorial/primitives.py
?? src/bafras_web/editorial/references.py
?? src/bafras_web/editorial/sections.py
?? tests/integration/test_inicio_content.py
?? tests/unit/editorial/conftest.py
?? tests/unit/editorial/test_d03_contract.py
?? tests/unit/editorial/test_domain.py
```

Se leyeron los informes A1/A2, los contratos editoriales reales, sus pruebas,
Inicio YAML, D03 Parte A/adendas y el registro de rutas WEB. Ningún AGENTS.md
fue localizado en la raíz de trabajo inspeccionada. No se descartan ni restauran
los cambios anteriores. La comparación de huellas incluye archivos sin seguimiento.

## B. Hallazgos confirmados

| Caso | Cobertura previa | Debilidad confirmada |
|---|---|---|
| Descripciones o ejemplos intercambiados dentro de H02 | Mismos textos por bloque | El multiconjunto no conserva padre-hijo |
| Ejemplo movido entre capacidades | Multiconjunto conservado | No demuestra pertenencia al elemento correcto |
| CTA de hero intercambiados | Dos destinos configurados; mismo texto | No se vinculaban todas las etiquetas a su destino |
| Texto trasladado entre H06/H07 | Multiconjunto por bloque | Ya se detectaba; riesgo descartado para ese caso |
| Unidad eliminada o añadida | Diferencia de multiconjuntos | Ya se detectaba; se conserva esa comprobación |
| Orden de siete secciones o de IDs de colecciones | Tests de orden separados | Ya había cobertura; se integra también en la paridad semántica |
| Orden de textos/relación título-descripción-acción | Comparación no estructurada | Requería comprobación padre-hijo por identidad |
| Selector pendiente con errata | PendingField solo valida cadena/motivo | No existía resolución del selector contra la página |
| Validez/revisión/publicación | Contratos ya separados | Faltaba probar explícitamente su independencia |

No se encontró defecto del copy de Inicio que justificara modificar el YAML.
No se cambia el modelo de revisión ni se añade un estado de publicación.

## C. Implementación

| Archivo | Cambio A2.1 |
|---|---|
| `src/bafras_web/editorial/pending.py` | Nuevo resolver puro y validación explícita de pendientes |
| `src/bafras_web/editorial/primitives.py` | Solo docstring aclaratorio de EditorialReview; sin cambio de esquema |
| `tests/unit/editorial/test_pending.py` | 47 pruebas nuevas de selectores, diagnósticos y estados |
| `tests/integration/test_inicio_content.py` | Paridad estructurada, 10 mutaciones y negativos de referencias; reutiliza una comprobación de destinos |
| Este informe | Hallazgos, contrato, resultados y preparación B1 |

El código de producción nuevo solo depende de Pydantic, biblioteca estándar y
editorial. No importa filesystem, YAML, WEB ni templates. No existe otro loader,
MediaRef, servicio de publicación, máquina de estados ni validación multipágina.
El nuevo módulo se consume mediante `bafras_web.editorial.pending`.

## D. Paridad semántica

`expected_semantics(source_blocks)` extrae de D03 los textos, su orden y sus
relaciones en las estructuras conocidas H01–H07. Los IDs asignados por A2 y el
mapeo de nombres documentales a IDs WEB son expectativas explícitas y trazables;
no se obtiene ninguna expectativa del YAML ni se mantiene otro copy completo.

La comparación conserva todos los campos poblados, identidades, discriminadores,
orden, párrafos, ejemplos, acciones y destinos. Solo omite defaults opcionales
vacíos/None; cualquier texto público añadido queda dentro de la comparación.

| Bloque | Correspondencia comprobada |
|---|---|
| H01 | ID/documento/kind; eyebrow-H1-subtítulo-párrafo; CTA principal y secundario ordenados con destino |
| H02 | Tres capacidades con ID, título, descripción, ejemplos identificados y ordenados, acción propia; enlace al índice |
| H03 | Cuatro necesidades con identidad, título, descripción y destino asociado |
| H04 | Cuatro pasos con ID, título y explicación; introducción, cierre y enlace |
| H05 | Cuatro agrupaciones de portada y su orden; introducción y enlace único; no equivalen a seis sectores |
| H06 | Párrafo de experiencia y acción; ausencia de paneles públicos adicionales |
| H07 | Título, párrafo, CTA específico y microcopy de colaboración |

Se conserva el test de multiconjuntos por bloque como verificación complementaria.
Las mutaciones se aplican a copias en memoria que siguen validando con Pydantic:
intercambiar descripciones, ejemplos o destinos; mover un ejemplo a otra tarjeta;
eliminar texto; añadir texto; reordenar secciones; reordenar pasos; cambiar el ID
documental; intercambiar párrafos entre secciones. Todas fallan la nueva paridad.
En cinco casos se demuestra además que el multiconjunto permanece idéntico.

## E. Selectores de pendientes

API:

```python
resolve_pending_selector(page: PageContent, selector: str) -> SelectorResolution
validate_pending_fields(page: PageContent) -> list[PendingDiagnostic]
```

Gramática admitida:

```text
seo.<field>
sections/<section_id>/<field>
sections/<section_id>/items
sections/<section_id>/items/<item_id>/<field>
```

IDs validados con EditorialId, nunca posiciones. Campos con nombre textual
simple, sujetos a la lista explícita siguiente. Sin eval, getattr dinámico,
recursión arbitraria ni acceso a atributos internos de Pydantic.

| Objetivo | Campos admitidos |
|---|---|
| SEO | title, description |
| Cualquier sección | title |
| Hero | eyebrow, subtitle, media |
| Cards | eyebrow, media, items |
| ItemList | media, items |
| Process | items |
| Elemento de cards/list/process | title |
| CapabilityCard | media |

Otros campos requieren una ampliación explícita de contrato. La gramática no
convierte todas las propiedades presentes en propiedades consultables.

| status | Significado |
|---|---|
| value | Campo permitido con valor textual |
| none | Campo permitido existente con None |
| collection | Colección permitida existente |
| invalid_syntax | No pertenece a la gramática acotada |
| section_not_found | ID de sección inexistente |
| item_not_found | ID de elemento inexistente |
| field_not_allowed | Campo no expuesto o incompatible con ese tipo |

SelectorResolution contiene status, valor tipado y mensaje para los errores.
PendingDiagnostic identifica página, selector, reason_code, código y contexto.
La validación acumula errores en orden de declaración. No borra pendientes ni
devuelve una decisión de publicación. Los modelos anteriores siguen rechazando
identificadores duplicados antes de resolver.

Los ocho selectores de Inicio son compatibles: dos SEO devuelven none, H05/items
devuelve collection con sus cuatro elementos y los cinco medios devuelven none.
No hay errores de integridad de selectores en Inicio. Reordenar tarjetas y
secciones no cambia el objetivo seleccionado por ID.

PendingField permanece compatible: no se impone esta gramática a campos de
entidades ni se cambia su construcción. La función explícita valida los
selectores de una PageContent; no es una búsqueda universal en todo el dominio.

## F. Estados e invariantes

| Concepto | Contrato |
|---|---|
| Validez estructural | Pydantic valida forma, tipos e identidades locales |
| Integridad local de pendientes | La función explícita comprueba que sus selectores tengan objetivos admitidos |
| Revisión | Declaración draft/reviewed/approved; resolver no la modifica |
| Publicabilidad | WEB integrará contenido disponible, revisión, pendientes, permisos, medios y demás requisitos |

Las pruebas verifican draft/reviewed/approved estructuralmente válidos, incluidos
approved con SEO ausente y medios pendientes. Una colección con contenido o un
SEO con texto puede conservar approval_required. Resolver o validar pendientes
no altera revisión ni contenido. Un selector inexistente puede ser una cadena
estructuralmente válida y producir después un diagnóstico de integridad local.

Una referencia documental registra procedencia. No concede autorización:
Verification(evidence_refs=["D03"]) sigue sin authorized. Se mantiene el contrato
anterior que exige evidencia si alguien declara verificación/autorización, sin
atribuir al dominio la certificación de esa evidencia. No se introducen estados
nuevos ni funciones que deduzcan permiso de publicación.

## G. QA

Baseline: 232 pruebas aprobadas. Resultado final:

| Comando pytest | Resultado |
|---|---:|
| `tests/unit/editorial -q` | 186 passed |
| `tests/integration/test_inicio_content.py -q` | 25 passed |
| `tests/contracts/test_architecture.py -q` | 6 passed |
| `-q --tb=short` (suite completa) | 292 passed |

Se usa `.venv/Scripts/python.exe -B -m pytest`, temporal nuevo fuera del repositorio
y safe.directory solo mediante variables de entorno del proceso. Sin cambios de
configuración persistente. Incremento neto: 60 pruebas respecto de A2.
Durante el desarrollo se corrigió una entrada omitida (Sectores) en el mapeo
documental del nuevo oráculo; no se modificó el contenido ni se relajaron tests.

Los negativos de referencias diferencian un page_id desconocido de un destino
configurado pero intercambiado. El segundo pasa existencia de ruta y falla
paridad semántica. WEB RouteTable no contiene registro de section_id, estado
editorial o contenido; se pospone la comprobación de anclas de otras páginas.
No se inventan páginas ni se considera SiteRouting.url prueba de publicación.

## H. Git y concurrencia

HEAD se conserva en `fca65e8ba7d75317be150e3f428be67d87825d34`.
Las modificaciones A2.1 son únicamente los cinco archivos enumerados en C.
Inicio YAML, documentos maestros, informes anteriores, configuración, módulos
WEB y demás archivos preexistentes permanecen intactos, comprobado por SHA-256.
No se observan cambios concurrentes ajenos. Sin cambio de rama, commits, push,
reset, clean o stash. No se eliminan archivos.

El estado Git mantiene todos los archivos A1/A2 sin commit; A2.1 añade pending.py,
test_pending.py y este informe, y actualiza primitives.py y el test de Inicio,
que ya eran archivos sin seguimiento desde A1/A2. El estado abreviado por sí
solo no describe esas modificaciones: la comparación de huellas las distingue.

## I. Preparación B1

Antes de ampliar infraestructura editorial deben acordarse con WEB:

1. API de carga/diagnósticos y propiedad de su integración en application.
2. Declaración única de versión/envelope del conjunto de contenido.
3. MediaRef y correspondencias Rxx/manifiesto; aún no implementados.
4. Cómo conocer contenido disponible y revisión por página/idioma, además del
   registro técnico de rutas; sin fallback ni publicación deducida del routing.
5. Política release que consuma los pendientes y demás evidencias, sin convertir
   una resolución correcta del selector en aprobación editorial.
6. Qué campos adicionales necesitarán selectores al migrar otras páginas; se
   ampliará la lista explícita con pruebas, sin crear un lenguaje de consultas.

Siguen pendientes SEO de Inicio y aprobación de las etiquetas H05. La siguiente
fase puede consumir estos contratos locales, pero A2.1 no inicia B1.
