# CONTENT-ES-01 / A6 V2 — Consolidación editorial ES

Fecha: 06/11/2026. Dictamen: **GO CON CONDICIONES**.
El baseline ES conserva nueve páginas, 51 bloques, seis sectores y tres
personas. Pydantic, paridad D03 e integridad pasan; el bundle se construye con
ambas políticas. **No se modificaron los once YAML, producción ni pruebas.**
Se organizaron cinco informes históricos, se conservaron tres rutas externas
de entrega y se preparó la documentación para traducción posterior.

## Baseline real y preflight

Rama inicial/final: `feat/contingut-v2`. HEAD:
`fca65e8ba7d75317be150e3f428be67d87825d34`.
Se consultó git status con todos los archivos sin seguimiento antes de editar,
se inventariaron los nueve YAML y dos catálogos y se registraron SHA-256 de
**132 archivos** de src/tests/content/config/docs, pyproject.toml y README.md.
No existían las cinco altas documentales A6 ni sus destinos operativos.

Estado Git inicial: editorial/__init__.py ya figuraba modificado. Sin
seguimiento estaban los once YAML ES; los ocho informes CONTENT A1/A2/A2.1/
A3/A4/A5/B1.0/B1.1; los ocho módulos editoriales entities, inspection,
integrity, pages, pending, primitives, references y sections; adapters/editorial_files;
application/editorial; los tests editorial B1.1 de arquitectura; los cinco tests
de integración inicio, capacidades, specialty, es_completion y editorial_loading_b11;
y los seis archivos de tests/unit/editorial (conftest, a5_contract,
b11_inspection, d03_contract, domain, pending).
Todo ese trabajo anterior se preservó; no se hizo consolidación Git.

Inventario documental inicial: **57 archivos** en docs/project_v02: 28 en raíz,
dos en evidencias_B01, ocho en evidencias_B02_recursos, seis en
evidencias_WEB_G1_REVIEW_01, nueve ZIP en maquetas_aprobadas y cuatro en
soporte_auditoria. Se clasificaron los ocho informes CONTENT como operativos;
el resto corresponde a fuentes maestras, decisiones, WEB, diseño y evidencias.
No se asumió propiedad CONTENT de ese material.

Se buscaron consumidores en código, pruebas, scripts, README, content y docs.
Los consumidores ejecutables leen D03 en su ruta raíz estable, la carpeta
project_v02 o sus maestros; ninguno consume las cinco rutas movidas. Las
menciones entre informes anteriores son rutas en baselines, ejemplos o nombres
históricos en texto, sin enlaces Markdown que deban reescribirse. No se
localizó AGENTS.md en las búsquedas del proyecto de las intervenciones previas.

La suite inicial dio **544 passed**, sin errores ni omitidas. Antes de editar
se ejecutaron inspect_editorial y build_editorial_bundle con INCREMENTAL y
COMPLETE, además de assess_integrity(report_resolved=True); coinciden con A5.
Se capturaron en memoria los modelos completos, copy público, metadatos
protegidos y sus serializaciones deterministas antes de mover documentos.

## Fuentes y revisión transversal

Se mantiene la precedencia de [D03 V1.22](../../03_contenido_editorial_V1_22_baseline_G1.md),
03.K/03.K.2, 03.SEC.CAT-01/02, 03.CO-02 y 03.G1-01/02 según su ámbito.
[D04](../../04_arquitectura_software_V2_4_handoff_G1.md) gobierna contratos WEB;
[D05](../../05_sistema_visual_V4_12_baseline_G1.md) composición y medios.
Se contrastaron [DEC-05 y decisiones G1](../../WEB_G1_CLOSE_DECISIONES.md),
informes A1–A5/B1, modelos, loader único, pendientes, inspección, integridad,
constructor y registro WEB existentes. No se usaron propuestas como copy.

Las pruebas de paridad existentes cubren todos los campos poblados de los 51
bloques y catálogos, además de orden, jerarquía, relaciones padre/hijo, notas,
CTA, SEO, formularios, condiciones y atribución. Se reutilizaron; no se duplicó
su extracción documental. La inspección focalizada no detectó zonas concretas
que exigieran otra ampliación de contratos o pruebas.

Se conservan diferencias aprobadas: agrupaciones de Inicio frente a seis
sectores; cuatro ámbitos INF frente a seis ENE/DIG; modalidad frente a proceso;
diagnósticos y nota hídrica transversales; distinción entre monitorización,
supervisión y control; trayectoria del equipo frente a contratación BAFRAS.
No se deduce experiencia sectorial de ejemplos ni se promocionan candidatas PE.

Los catálogos son la fuente única de seis sectores y tres personas. SectorIndex
y TeamSection referencian sus identidades sin incrustar copias. Se preservan
grafías, titulaciones, especialidades y estados no verificados. No se crean
common, experiences o resources vacíos. No se encontró resto de maqueta,
texto añadido sin aprobación o duplicación funcional que requiriera corrección.

## Hallazgos clasificados T1–T5

| Tipo | Revisión y evidencia | Decisión |
|---|---|---|
| T1 — defecto técnico | Once YAML legibles UTF-8, sin claves duplicadas por el loader estricto; cero documentos inválidos, referencias incorrectas o selectores de página defectuosos | Ninguna corrección de datos o código necesaria |
| T2 — desviación D03 | Paridad literal y estructural existente satisfactoria; condiciones y atribuciones conservadas | Cero cambios editoriales |
| T3 — normalización equivalente | Conviven listas YAML con distinta indentación y defaults explícitos como null SEO o entries vacío PE; validan y expresan pendientes/ausencia deliberada | No reformatear ni eliminar: beneficio insuficiente frente al diff y la trazabilidad |
| T3 — organización documental | Informes CONTENT mezclados con maestros y material WEB; se identifican consumidores y responsabilidad | Organizar cinco informes por flujo, indexar todos y conservar tres rutas de entrega externas |
| T4 — mejora editorial | CTA y vocabulario se repiten en contextos aprobados; ello no demuestra duplicación accidental | No proponer ni aplicar abreviación, cambio de tono o uniformidad artificial; cualquier nueva redacción requiere revisión humana |
| T5 — pendientes legítimos | 22 pendientes de página, seis avisos de persona y dos contactos no verificados; draft en las nueve páginas | Conservar valores, motivos, selectores y fuentes |

No se forzó una normalización para producir cambios. La estabilidad de los
once archivos es el resultado de la revisión, no una omisión del alcance.

## Correcciones, normalizaciones y dominio

**Cero cambios de producción, pruebas o YAML.** Se mantienen los contratos
Pydantic v2, configuración estricta, loader único, APIs, políticas de integridad
y construcción del bundle. No se añaden dataclasses, capas, servicios,
adaptadores, fallback, lenguajes, snapshots permanentes o herramientas de IA.

La normalización se limita al acceso documental: índice por responsabilidad,
cinco movimientos de informes inalterados, contrato de campos, glosario y
manifiesto. No se cambian comentarios, formato, orden de claves, null o listas
vacías por preferencias estéticas. El cuerpo histórico de cada informe se
preserva byte a byte, incluido su estado Git y sus rutas originales citadas.

## Comparación semántica antes/después

Aunque no se modificaron YAML, se ejecutó la comparación solicitada. Los modelos
se cargaron mediante APIs reales y se serializaron con model_dump(mode="json"),
JSON con claves ordenadas, ensure_ascii=False y separadores compactos. Las
listas conservan su orden editorial. Las capturas quedaron en memoria, no en
un nuevo sistema de fixtures o snapshots del repositorio.

Se compararon:

- Bundle completo: todos los campos, defaults y colecciones.
- Proyección de copy: textos visibles, nombres, valores de contacto y
  obligatoriedad, conservando sus contenedores y orden; se separan identidad,
  discriminadores, referencias, fuentes, revisión, pendientes y medios.
- Metadatos protegidos: IDs, estructura tipada, relaciones, fuentes, estados,
  selectores, Rxx, contactos, nombres y booleanos. Nombres/contactos/required
  se protegen también aunque sean datos visibles.
- Cardinalidades y once hashes de bytes originales.

| Huella SHA-256 | Antes = después |
|---|---|
| Bundle completo | `725e0f2326f9e723253c698fac34afe70ea49bb9b659edad1c8fbc4e55ab0df8` |
| Proyección pública | `c968c3ca008e1d25f6e01da504b5da27446705eed6dd1f382cf1b1985b7340bc` |
| Metadatos protegidos | `d8ced6a5ef24e31da4f08857bab4ef59d7c2ffa2e6d09ec92de1b2b9bb0d7612` |

Resultado: **cero diferencias** en objetos, serializaciones, copy, relaciones,
cardinalidades o metadatos. Los once YAML conservan además bytes idénticos.
Esta comparación complementa la paridad D03; no la sustituye.

## Integridad y pendientes

| Resultado real | INCREMENTAL | COMPLETE |
|---|---:|---:|
| Páginas configuradas / válidas | 9 / 9 | 9 / 9 |
| Bloques / sectores / personas | 51 / 6 / 3 | 51 / 6 / 3 |
| Páginas ausentes / documentos inválidos | 0 / 0 | 0 / 0 |
| Referencias internas y de catálogo resueltas | 73 | 73 |
| Referencias incorrectas | 0 | 0 |
| EXTERNAL_CONTACT_UNCHECKED | 2 info | 2 info |
| EDITORIAL_PENDING | 22 info | 22 info |
| ENTITY_PENDING_UNCHECKED | 6 warning | 6 warning |
| PENDING_SELECTOR_INVALID | 0 | 0 |
| Errores | 0 | 0 |
| documents_complete / can_build_bundle | true / true | true / true |

Catálogos requeridos: people y sectors, ambos válidos. Bundle construido en
ambas políticas con cero experiencias y cero recursos. No se relajan reglas
para conseguir completitud. Los 22 pendientes de página se distribuyen en
diez integration_pending, nueve approval_required, dos source_missing y uno
verification_required. Seis pendientes de persona conservan el límite B1.1 de
resolución no implementada para entidades. Dos contactos son externos no
comprobados, no referencias editoriales rotas. Todas las páginas siguen draft.

## Reorganización documental

Se adaptó el árbol al inventario real: editorial/foundation,
editorial/migration-es, editorial/quality y editorial/localization. No hay
carpetas vacías architecture/web/decisions: el índice enlaza sus documentos
maestros y de otros equipos en sus rutas estables.

Mapa de rutas, relativo a docs/project_v02:

| Ruta anterior | Ruta final | Motivo |
|---|---|---|
| CONTENT_ES_01_A1.md | [editorial/foundation/CONTENT_ES_01_A1.md](../foundation/CONTENT_ES_01_A1.md) | Contrato de dominio |
| CONTENT_ES_01_B1_0.md | [editorial/foundation/CONTENT_ES_01_B1_0.md](../foundation/CONTENT_ES_01_B1_0.md) | Contrato de carga/integridad |
| CONTENT_ES_01_B1_1.md | [editorial/foundation/CONTENT_ES_01_B1_1.md](../foundation/CONTENT_ES_01_B1_1.md) | Infraestructura editorial |
| CONTENT_ES_01_A2_INICIO.md | [editorial/migration-es/CONTENT_ES_01_A2_INICIO.md](../migration-es/CONTENT_ES_01_A2_INICIO.md) | Migración española |
| CONTENT_ES_01_A2_1.md | [editorial/quality/CONTENT_ES_01_A2_1.md](CONTENT_ES_01_A2_1.md) | Paridad y pendientes |
| CONTENT_ES_01_A3.md | [CONTENT_ES_01_A3.md](../../CONTENT_ES_01_A3.md), sin movimiento | Enlace absoluto de entrega anterior fuera del repositorio |
| CONTENT_ES_01_A4.md | [CONTENT_ES_01_A4.md](../../CONTENT_ES_01_A4.md), sin movimiento | Mismo criterio de compatibilidad externa |
| CONTENT_ES_01_A5.md | [CONTENT_ES_01_A5.md](../../CONTENT_ES_01_A5.md), sin movimiento | Mismo criterio de compatibilidad externa |

Los tres informes de entrega se mantienen en raíz conforme a §12.3/12.4 del
encargo: no es seguro actualizar sus enlaces previos en la conversación. Se
indexan sin duplicarlos. Al comprobar este consumidor externo se conservaron
sus rutas originales antes de cerrar la intervención; sus hashes no cambian.

Cada movimiento se realizó por filesystem con rutas absolutas comprobadas
dentro del proyecto, origen existente, destino sin colisión y hash coincidente
con preflight. Se verificó el mismo hash al llegar. No hay pérdida de informes,
copias redundantes, alias o archivos de redirección. Las menciones históricas
de rutas en sus cuerpos no se reescribieron. No había enlaces operativos ni
consumidores ejecutables de las cinco rutas movidas que actualizar; el nuevo
índice y este mapa son la referencia navegable actual.

El [índice documental](../../README.md) incluye fuentes, arquitectura, WEB,
decisiones, historial A1–A6 y localización. Define la convención de crear nuevos
informes directamente en su carpeta de flujo, preservar los maestros y usar
enlaces relativos. Los 49 archivos documentales iniciales ajenos a los ocho
informes CONTENT permanecen en su ubicación, igual que los tres informes
retenidos. Todos conservan su contenido.

## Contrato de localización y glosario

Se entregan [LOCALIZATION_CONTRACT.md](../localization/LOCALIZATION_CONTRACT.md)
y [TERMINOLOGY_ES.md](../localization/TERMINOLOGY_ES.md). El contrato inventaría
los campos reales de los modelos, distinguiendo copy traducible de identidad,
referencias, selectores, revisión, contactos, booleanos y estructura protegidos.
Explicita Hero/Text/Cards/List/Process/índices/Team/Form, tarjetas, acciones,
canales, campos, SEO, Person y Sector; los catálogos inexistentes no se crean.

Se fijan nombres de archivo, carpetas, tratamiento de null, orden, cardinalidad,
nombres propios, títulos profesionales, pendientes, ausencia de fallback,
variables y validación con las APIs actuales. No se detectaron variables de
interpolación en los valores actuales; el contrato explica cómo preservarlas
si apareciesen después, sin añadirlas al contenido.

El glosario contextualiza veinte términos o grupos reales de D03 con riesgo de
ambigüedad, incluidos especialidades, diagnóstico, verificación, asistencia,
control/supervisión, siglas, titulaciones y atribución. No propone traducciones
definitivas, no amplía la oferta y no pretende ser un glosario enciclopédico.

La entrega futura a una IA se define como procedimiento documental: paquete
fuente identificado por hash, un idioma destino, once archivos con estructura
protegida, comparación de invariantes, validación Pydantic, inspección/bundle
y revisión lingüística/técnica posterior. No se generan traducciones, scripts
de exportación/importación, servicios o cambios al loader.

## Manifiesto y QA final

El [ES_BASELINE_MANIFEST.md](ES_BASELINE_MANIFEST.md) registra fecha, rama/HEAD,
nueve páginas, dos catálogos, cardinalidades, once SHA-256 de bytes, autoridades,
pendientes, revisión draft, integridad, bundle, pruebas, límites y condiciones
de obsolescencia. No es una aprobación, release ni tag.

Se verificaron los destinos y hashes de los cinco movimientos, la permanencia
de los otros documentos y los enlaces locales del conjunto Markdown de
docs/project_v02, incluidos los documentos nuevos y el ancla del mapa. Se
comprobaron las once huellas del manifiesto contra los archivos reales.
No se confundieron rutas citadas dentro de bloques históricos con enlaces
operativos. No se validó disponibilidad de sitios web externos.

| Ejecución | Resultado |
|---|---:|
| Suite completa preflight | 544 passed |
| Paridad e integración editorial A1–A5/B1.1, ejecución final | 452 passed |
| Contratos de arquitectura, ejecución final | 17 passed |
| Suite completa final | 544 passed |
| YAML/catálogos, integridad, selectores de página, bundle | válidos en ambas políticas |
| Diferencias semánticas / once YAML | 0 / 0 |
| Informes perdidos / movimientos alterados | 0 / 0 |

Se reutilizó la suite existente: no se añadieron pruebas que duplicasen reglas
o verificasen solo formato documental. Los controles de hashes, enlaces y
comparación se ejecutaron de forma puntual, sin dejar scripts persistentes.
Sin fallos, skips o xfail en las ejecuciones finales. Se usaron temporales
nuevos fuera del repositorio y safe.directory solo de proceso cuando las
comprobaciones Git existentes lo requieren por la propiedad del checkout.

## Control de alcance y cierre

Altas nuevas, cinco documentos: README.md de project_v02, contrato de
localización, glosario, manifiesto y este informe. Movimientos finales: cinco
informes. Los tres informes A3–A5 mantienen ruta y bytes; no existen duplicados.
De los 132 archivos registrados al inicio, 127 permanecen idénticos en la
misma ruta y los otros cinco mantienen bytes idénticos en sus destinos nuevos.
No hay modificación de contenido de ningún archivo preexistente ni pérdida.

No se observaron cambios concurrentes. La comparación incluye producción,
pruebas, once YAML, maestros y evidencias. Rama y HEAD no cambian. El estado
Git mantiene el trabajo previo y refleja solo las altas y reubicaciones A6;
al estar los informes sin seguimiento, git status no identifica renombrados,
por lo que el mapa y la comparación SHA-256 proporcionan esa evidencia.

No se ejecutaron add, commit, push, merge, reset, clean, stash ni cambio de rama.
No se modificó configuración Git persistente, pyproject, dependencias, rutas,
idiomas, aplicación, adaptadores, modelos, políticas o presentación WEB.

## Pendientes, riesgos y dictamen

**GO CON CONDICIONES**: baseline español completo, fiel e íntegro, equivalencia
demostrada, documentación organizada con compatibilidad de rutas y contrato
de localización preparado. No se encontraron defectos que requirieran cambios
editoriales o técnicos de producto.

Se mantienen la revisión humana conjunta, SEO pendiente, privacidad y titular
legal, nombres/biografías, permisos de referencias, contrato MediaRef, licencias
y comprobación de canales. Las seis candidatas PE no se convierten en cartera
corporativa. El bundle técnicamente válido y las páginas draft no autorizan
publicación. Los avisos de entidad reflejan el límite explícito de B1.1.

Las futuras traducciones deben conservar la fuente exacta por hash y pasar su
propia revisión; la paridad literal española no certifica otra lengua. Los
movimientos de los cinco informes requieren usar el índice actualizado; las
rutas antiguas solo sobreviven como historia, sin duplicados. A3–A5 conservan
sus enlaces de entrega existentes. El baseline se renueva si cambian datos,
contratos, registro WEB o decisiones fuente, conforme al manifiesto.

Se cierra A6 V2. No se traduce contenido, no se inicia presentación WEB, no se
solicita revisión humana intermedia y no se realizan commits.
