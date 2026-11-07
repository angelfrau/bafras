# CONTENT-ES-01 / A4 — Tres páginas de especialización

Fecha: 06/11/2026. Dictamen: **GO CON CONDICIONES**.
Los 21 bloques de INF, ENE y DIG están migrados, validados y contrastados con
D03. La suite completa termina con **484 passed**. Los nuevos documentos
siguen en `draft`; los pendientes de SEO y medios permanecen explícitos.
No se modificó software de producción ni se inició A5.

## 1. Baseline real y protección del trabajo anterior

Rama inicial y final: `feat/contingut-v2`. HEAD inicial y final:
`fca65e8ba7d75317be150e3f428be67d87825d34`.

Se verificaron rama, HEAD, estado Git completo con archivos sin seguimiento,
fuentes y destinos. Los tres YAML, el archivo nuevo de pruebas y este informe
no existían. La búsqueda no localizó AGENTS.md en el árbol del proyecto.
Antes de editar se registraron en memoria SHA-256 de **117 archivos**
preexistentes de src/tests/content/config/docs y pyproject.toml, incluidos
los documentos y módulos sin seguimiento. No se revirtieron cambios anteriores.

Estado Git inicial completo:

```text
 M src/bafras_web/editorial/__init__.py
?? content/es/pages/capacidades.yaml
?? content/es/pages/inicio.yaml
?? docs/project_v02/CONTENT_ES_01_A1.md
?? docs/project_v02/CONTENT_ES_01_A2_1.md
?? docs/project_v02/CONTENT_ES_01_A2_INICIO.md
?? docs/project_v02/CONTENT_ES_01_A3.md
?? docs/project_v02/CONTENT_ES_01_B1_0.md
?? docs/project_v02/CONTENT_ES_01_B1_1.md
?? src/bafras_web/adapters/editorial_files.py
?? src/bafras_web/application/editorial.py
?? src/bafras_web/editorial/entities.py
?? src/bafras_web/editorial/inspection.py
?? src/bafras_web/editorial/integrity.py
?? src/bafras_web/editorial/pages.py
?? src/bafras_web/editorial/pending.py
?? src/bafras_web/editorial/primitives.py
?? src/bafras_web/editorial/references.py
?? src/bafras_web/editorial/sections.py
?? tests/contracts/test_editorial_b11_architecture.py
?? tests/integration/test_capacidades_content.py
?? tests/integration/test_editorial_loading_b11.py
?? tests/integration/test_inicio_content.py
?? tests/unit/editorial/conftest.py
?? tests/unit/editorial/test_b11_inspection.py
?? tests/unit/editorial/test_d03_contract.py
?? tests/unit/editorial/test_domain.py
?? tests/unit/editorial/test_pending.py
```

Baseline ejecutado: **422 passed**, con Inicio y Capacidades válidas. Se
mantuvieron las precauciones de ejecución de A3: temporal nuevo fuera del
repositorio mediante PYTEST_DEBUG_TEMPROOT y excepción safe.directory limitada
al comando/proceso por la propiedad distinta del checkout. No se cambió la
configuración Git persistente. No se realizó ninguna operación Git de escritura.

## 2. Fuentes consultadas y precedencia

| Fuente | Aplicación y autoridad |
|---|---|
| D03 V1.22, `03_contenido_editorial_V1_22_baseline_G1.md` | Fuente textual vinculante: INF-01–07, ENE-01–07, DIG-W01–07, notas, relaciones, CTA y SEO de DIG |
| Registro 03.D.3 de D03 | Ratifica cuatro ámbitos INF más diagnóstico transversal y supera el estado histórico de propuesta 03.D.2 |
| Cabecera, registro de estados y 03.G1-01 de D03 | Confirman aprobación de las páginas; superan las menciones históricas «propuesta/no aprobada» de ENE y otras iteraciones |
| D03 03.G1-02 | Revisada; resuelve variantes de Contacto/atribución sin modificar los 21 bloques de A4 |
| D04 V2.4, `04_arquitectura_software_V2_4_handoff_G1.md` | Identidades, separación de responsabilidades y arquitectura; contrastado con el registro WEB y código real |
| D05 V4.12, `05_sistema_visual_V4_12_baseline_G1.md`, §24–31 | Composición de especialidades; §26 ratifica INF V2/R18, §29 ENE V2/R10+R08, §31 DIG V1/R01+R03 |
| `maquetas_aprobadas/C04_INF_V2_revision.zip` | HTML/estructura y selección R18, inspeccionados dentro del ZIP sin extracción persistente |
| `maquetas_aprobadas/C04_ENE_V2_BAFRAS.zip` | HTML/estructura, capítulos y R10/R08; subordinado al texto literal D03 |
| `maquetas_aprobadas/C04_DIG_V1_BAFRAS.zip` | HTML/estructura, seis ámbitos/etiquetas, transversal y R01/R03 |
| `WEB_G1_CLOSE_DECISIONES.md`, DEC-05 | SEO de INF/ENE sigue propuesto sin aprobación; confirma que DIG sí dispone de metadatos D03 |
| Registro de incidencias y matriz de cierre WEB-G1 | Divergencias de prototipos y límites de publicación: no trasladar marcas internas, enlaces demostrativos ni claims visuales |
| Informes A1, A2.1, B1.1 y A3 | Contratos, fidelidad estructural, pendientes, persistencia e integridad reutilizados |

Se contrastaron los modelos A1, resolver de pendientes, inspección e integridad,
application/editorial, loader único, adaptador editorial, configuración WEB y
pruebas reales. Los modelos existentes admiten el contenido completo; ningún
contrato se amplió por anticipación. El HTML de los prototipos se consultó para
composición y medios, sin usarlo para generar textos.

## 3. Los 21 bloques y su correspondencia A1

Cada fila remite al bloque homónimo de D03 y al source_block exacto del YAML.
Los H1/H2, párrafos, notas y elementos completos se comparan en las pruebas;
esta tabla resume estructura y cardinalidad sin duplicar todo el copy.

| Bloque | Contenido y cardinalidad preservados | Modelo A1 / propósito |
|---|---|---|
| INF-01 | Eyebrow, H1, subtítulo, apoyo, contacto y ancla ámbitos; R18 pendiente | HeroSection |
| INF-02 | Introducción y cinco necesidades: nueva instalación; funcionamiento deficiente; infraestructura específica; adecuación/seguridad; decisiones de inversión | ItemListSection / needs, NeedItem |
| INF-03 | Introducción; electricidad; climatización/ventilación/refrigeración; agua/hidráulica/auxiliares; protección/condiciones técnicas; diagnóstico transversal separado | CardsSection / technical_areas, cuatro TechnicalAreaCard y EditorialAside |
| INF-04 | Introducción; diagnóstico/estudios, diseño/proyecto, asistencia/coordinación, pruebas/verificación; nota de precisión completa | ItemListSection / deliverables, cuatro DeliveryItem y TextItem |
| INF-05 | Párrafo condicional de instalaciones/energía/control; enlaces ENE y DIG | TextSection |
| INF-06 | Experiencia profesional del equipo y atribución/contexto, sin referencias concretas; enlace al índice de experiencia | TextSection |
| INF-07 | Pregunta, párrafo y CTA Contacto | TextSection |
| ENE-01 | Eyebrow, H1, texto principal y apoyo, contacto y ancla ámbitos; R10 pendiente | HeroSection |
| ENE-02 | Introducción y seis necesidades: consumo; generación/almacenamiento; electrificación; recarga/activos; costes/seguimiento; descarbonización | ItemListSection / needs, seis NeedItem |
| ENE-03 | Seis ámbitos completos, 30 entradas Incluye y nota hídrica separada; R08 pendiente | CardsSection / technical_areas, seis TechnicalAreaCard y EditorialAside |
| ENE-04 | Diagnóstico/auditoría; viabilidad/alternativas; ingeniería/proyecto; integración/seguimiento; criterio de alcance completo | ItemListSection / deliverables, cuatro DeliveryItem y TextItem |
| ENE-05 | Párrafo de coordinación con límites por disciplina; enlaces INF y DIG | TextSection |
| ENE-06 | Experiencia del equipo, diferenciando trayectoria previa y encargos BAFRAS; enlace al índice | TextSection |
| ENE-07 | Pregunta, párrafo y CTA Contacto | TextSection |
| DIG-W01 | Eyebrow, H1, texto principal y apoyo, contacto y ancla ámbitos; R01 pendiente | HeroSection |
| DIG-W02 | Introducción y cinco necesidades: datos; control; intercambio de información; modernización; decisiones con datos | ItemListSection / needs, cinco NeedItem |
| DIG-W03 | Seis ámbitos completos, 25 etiquetas y diagnóstico/pruebas/evolución transversal; R03 pendiente | CardsSection / technical_areas, seis TechnicalAreaCard y EditorialAside |
| DIG-W04 | Diagnóstico/definición; diseño; desarrollo/integración; pruebas/documentación; nota literal de alcance | ItemListSection / deliverables, cuatro DeliveryItem y TextItem |
| DIG-W05 | Dos relaciones INF/ENE con descripción y destino propios; texto de cierre literal | CardsSection / discipline_relations, dos DisciplineRelationCard |
| DIG-W06 | Párrafo de actuaciones documentadas y atribución profesional frente a corporativa; enlace al índice | TextSection |
| DIG-W07 | Pregunta, párrafo y CTA Contacto | TextSection |

Detalle de los ámbitos ENE, en orden: Diagnóstico y eficiencia energética;
Generación renovable y almacenamiento; Electrificación y sistemas térmicos;
Movilidad eléctrica y sistemas energéticos integrados; Gestión, monitorización
y costes energéticos; Descarbonización y sostenibilidad energética. Sus líneas
Incluye conservan respectivamente **5/5/4/5/6/5** entradas y su puntuación.

Detalle de los ámbitos DIG, en orden: Instrumentación, adquisición de datos y
telemetría; Ingeniería de automatización y programación de control; Supervisión
y control técnico de instalaciones; Integración de equipos, comunicaciones y
arquitectura OT; Software técnico, datos y aplicaciones de ingeniería; Control
e integración de activos energéticos. Sus etiquetas conservan respectivamente
**4/4/4/4/5/4** entradas y su puntuación.

No se convirtió la nota hídrica en un séptimo ámbito, ni el diagnóstico INF en
una quinta tarjeta equivalente, ni el transversal DIG en una séptima tarjeta.
Las modalidades de entrega son listas independientes, nunca ProcessSection.

## 4. Decisiones editoriales y de representación

- Se crearon secuencialmente INF, ENE y DIG, validando siete bloques y ejecutando
  sus pruebas focalizadas antes de pasar a la siguiente página.
- Los page_id son los del registro WEB. El loader aporta `locale="es"`; no se
  duplica locale en YAML. Cada sección conserva su source_block documental.
- IDs de sección por página: hero `inf-01`/`ene-01`/`dig-w01`; `necesidades`,
  `ambitos`, `entregables`, `integracion`; cierres `inf-06/07`, `ene-06/07`,
  `dig-w06/07`. El CTA de exploración apunta a la propia página / ambitos.
- Los IDs de necesidades, áreas y entregables son estables y descriptivos.
  El oráculo declara esas decisiones explícitamente, sin deducirlas del YAML.
- Las enumeraciones Markdown de necesidades/ámbitos son orden de colección;
  no se anteponen números de presentación al título. Se conservan íntegros los
  títulos y su puntuación textual, incluidos los puntos de las necesidades.
- INF conserva Subtítulo en HeroSection.subtitle y apoyo como párrafo. ENE/DIG
  conservan dos párrafos principal/apoyo, sin inventar un subtítulo equivalente.
- Los códigos, referencias de catálogo, exclusiones y reglas de tratamiento de
  INF-03 son metadatos internos según su regla de presentación y no se publican.
  El párrafo transversal sí se conserva íntegro. Las notas de precisión de
  INF-04, criterio de ENE-04 y alcance de DIG-W04 sí son contenido visible.
- La nota hídrica ENE-03 conserva su título y párrafo completos de D03, aunque
  el prototipo pueda resumirla. D03 prevalece sobre divergencias del HTML.
- DIG-W05 utiliza la relación tipada disciplina/descripción. Las descripciones
  permanecen bajo su capacidad y se conserva el cierre; no se transforman en
  acciones genéricas perdiendo su relación editorial.
- Las necesidades no reciben nuevos CTA con etiquetas inventadas ni una falsa
  correspondencia uno a uno con una disciplina. Índices auxiliares, migas y
  navegación de presentación pertenecen a WEB; no se agregan como copy.
- Los enlaces de contacto van a page_id contacto, no a los anclajes de
  demostración de las maquetas. No se trasladan rótulos de control de prototipo.
- No se publican proyectos ni entidades Experience. El copy preserva diferencia
  entre oferta, ejemplo, experiencia previa del equipo y encargos BAFRAS.
- Se mantienen los límites sobre encargos, habilitaciones, verificación,
  mantenimiento continuo, disponibilidad 24/7, ciberseguridad e IA. No se añaden
  servicios, resultados, clientes, certificaciones ni cifras comerciales.

## 5. Defectos reproducidos y correcciones

**No se necesitó modificar ningún módulo de producción**, incluidos los ocho
archivos editoriales con autorización condicional. Los contratos de Pydantic,
pendientes e integridad permiten las tres migraciones completas.

Único defecto preexistente directamente afectado: el test A3
`test_real_b11_inventory_and_every_reference` de
`tests/integration/test_capacidades_content.py` seguía inspeccionando el checkout
real y afirmando exactamente Inicio/Capacidades válidas y siete ausentes.

Evidencia reproducible después de crear las tres páginas: la ejecución conjunta
de pruebas nuevas y A3 dio **76 passed, 2 failed**; ambos fallos ocurrieron en
la aserción del conjunto válido, con las tres nuevas especialidades como
elementos adicionales. No eran errores editoriales ni regresiones del loader.
La huella SHA-256 de ese archivo se contrastó con el baseline inmediatamente
antes de editar y coincidía.

Causa raíz: el escenario histórico A3 estaba acoplado a un inventario mutable.
Cambiar dos/siete por cinco/cuatro mantendría el defecto para otra migración.
Corrección mínima autorizada por etapas 3 y 9 del encargo: recibir tmp_path,
copiar configuración e Inicio/Capacidades reales al temporal e inspeccionar ese
escenario. Se añadió únicamente shutil y la preparación del temporal. Se
mantienen todas las aserciones previas de páginas, enlaces, pendientes,
catálogos, políticas y rechazo del bundle. No se cambian los YAML protegidos.

Las nuevas pruebas A4 inspeccionan por separado el checkout con las cinco
páginas y comparan **cada referencia**, no solo contadores. El escenario B1.1
aislado en A3 permanece intacto. Regresión posterior: A1–A3 233 passed;
B1.1 108 passed. No hay skips, xfail ni relajación de validadores.

Las menciones históricas de propuesta/aprobación en D03/D05 se resolvieron
mediante la precedencia inequívoca de sus registros posteriores. No se
reescribieron documentos maestros ni se interpretó una propuesta SEO como
aprobación. No se encontró contradicción editorial bloqueante.

## 6. SEO, medios, referencias y pendientes

Los tres YAML conservan `review.status: draft`, aunque sus fuentes estén
aprobadas. La revisión de la migración no se presume completada.

| Página | SEO | Medios aprobados no integrables | Pendientes nuevos |
|---|---|---|---:|
| Infraestructuras | title/description null, DEC-05 | Hero R18, D05 §26 | 3 |
| Sistemas energéticos | title/description null, DEC-05 | Hero R10 y ámbitos R08, D05 §29 | 4 |
| Automatización y control | Title y meta literales de D03 «Navegación, diseño y SEO» | Hero R01 y ámbitos R03, D05 §31 | 2 |

SEO DIG conservado:

- Title: `Automatización y control de instalaciones y procesos | BAFRAS Engineering`
- Description: `Ingeniería de instrumentación, PLC/DDC, SCADA, BMS, integración OT y software técnico para instalaciones y procesos.`

Los cuatro pendientes SEO nuevos usan approval_required y fuente DEC-05.
Los cinco medios usan integration_pending, selector estable
`sections/<id>/media` y source_ref documental con Rxx/acta aplicable. Media
permanece None según el contrato actual. No se inventan MediaRef, IDs de
manifiesto, rutas de archivos, alt o créditos. Las fotografías son contextuales;
no se convierten en evidencias de trabajos BAFRAS. Las reservas INF R15/R20 no
son selecciones aprobadas para integrar y no generan pendientes artificiales.

No se crea ni exige catálogo alguno: common, people, sectors, experiences y
resources siguen opcionales para estos consumidores. Las referencias a
experiencia son a la página índice, no a entidades ficticias. No se cambia
ninguna identidad sectorial canónica.

Inventario tipado de referencias nuevas (idéntico bajo ambas políticas):

| Origen | Texto / relación | Destino | Estado real |
|---|---|---|---|
| INF-01 / contact | Cuéntanos tu proyecto | contacto | UNVERIFIABLE |
| INF-01 / explore | Ver ámbitos de ingeniería | infraestructuras / ambitos | RESOLVED |
| INF-05 / energy | Sistemas energéticos | sistemas_energeticos | RESOLVED |
| INF-05 / automation | Automatización y control | automatizacion_control | RESOLVED |
| INF-06 / experience | Conocer proyectos y experiencia | proyectos_experiencia | UNVERIFIABLE |
| INF-07 / contact | Cuéntanos tu proyecto | contacto | UNVERIFIABLE |
| ENE-01 / contact | Cuéntanos tu proyecto | contacto | UNVERIFIABLE |
| ENE-01 / explore | Explorar ámbitos de actuación | sistemas_energeticos / ambitos | RESOLVED |
| ENE-05 / infrastructure | Infraestructuras e instalaciones | infraestructuras | RESOLVED |
| ENE-05 / automation | Automatización y control | automatizacion_control | RESOLVED |
| ENE-06 / experience | Conocer proyectos y experiencia | proyectos_experiencia | UNVERIFIABLE |
| ENE-07 / contact | Cuéntanos tu proyecto | contacto | UNVERIFIABLE |
| DIG-W01 / contact | Cuéntanos tu proyecto | contacto | UNVERIFIABLE |
| DIG-W01 / explore | Explorar ámbitos de actuación | automatizacion_control / ambitos | RESOLVED |
| DIG-W05 / infrastructure / discipline | Infraestructuras e instalaciones, con descripción propia | infraestructuras | RESOLVED |
| DIG-W05 / energy / discipline | Sistemas energéticos, con descripción propia | sistemas_energeticos | RESOLVED |
| DIG-W06 / experience | Conocer proyectos y experiencia | proyectos_experiencia | UNVERIFIABLE |
| DIG-W07 / contact | Cuéntanos tu proyecto | contacto | UNVERIFIABLE |

Todos los destinos están registrados en WEB. UNVERIFIABLE significa contenido
destino ausente; no se informa como página desconocida. No hay UNRESOLVED.

## 7. Inspección transversal real INCREMENTAL / COMPLETE

Ejecutada con `inspect_editorial(ProjectPaths(ROOT), EditorialLoadRequest(...))`
y `assess_integrity(..., report_resolved=True)` para auditar también los éxitos.

| Resultado | INCREMENTAL | COMPLETE |
|---|---:|---:|
| Páginas registradas | 9 | 9 |
| Páginas válidas | 5 | 5 |
| Ausentes | 4 | 4 |
| Documentos inválidos | 0 | 0 |
| DOCUMENT_MISSING | 4 warning | 4 error |
| REFERENCE_TARGET_UNAVAILABLE | 16 warning | 16 warning |
| Referencias RESOLVED en auditoría explícita | 31 | 31 |
| Referencias UNVERIFIABLE | 16 | 16 |
| Referencias UNRESOLVED | 0 | 0 |
| EDITORIAL_PENDING | 19 info | 19 info |
| PENDING_SELECTOR_INVALID | 0 | 0 |
| Catálogos requeridos | ninguno | ninguno |
| documents_complete | false | false |
| can_build_bundle | false | false |

Válidas: automatizacion_control, capacidades, infraestructuras, inicio,
sistemas_energeticos. Ausentes: contacto, proyectos_experiencia, sectores,
sobre_bafras. INCREMENTAL suma 20 warnings y 19 info, sin errores;
COMPLETE suma 4 errores, 16 warnings y 19 info. build_editorial_bundle rechaza
ambas inspecciones: no se construye un bundle parcial ni se relaja COMPLETE.

Recuento derivado de cada enlace del contenido real:

| Origen | RESOLVED | UNVERIFIABLE |
|---|---:|---:|
| Inicio | 9 | 5 |
| Capacidades | 13 | 2 |
| Infraestructuras | 3 | 3 |
| Sistemas energéticos | 3 | 3 |
| Automatización y control | 3 | 3 |

Se resuelven los seis enlaces desde Inicio a las especialidades y los doce
desde Capacidades (tres áreas y nueve enlaces contextuales). También se
resuelven los seis enlaces cruzados entre especialidades y las tres anclas
propias. Los cuatro éxitos ya existentes de A3 se conservan: 18 + 6 + 3 + 4 = 31.
De los 25 no verificables A3 se resuelven 18 y se añaden nueve de las nuevas
páginas: 25 − 18 + 9 = 16. Pendientes: diez preservados + nueve nuevos = 19.
Estas cifras son evidencia observada; las pruebas verifican inventarios y
destinos individuales y derivan los contadores de los datos.

## 8. Pruebas de fidelidad, mutación e integración

Nuevo archivo único `tests/integration/test_specialty_content.py`, con
parametrización por página. Se eligió esta distribución, permitida por la
preferencia de nombres del encargo, para compartir el mismo oráculo documental
y los mecanismos de mutación/integridad sin tres copias de código o wrappers
redundantes. No se añade código de pruebas al producto.

El oráculo lee D03 directamente, reconoce sus campos y enumeraciones y forma
la expectativa de jerarquía por bloque. No lee expectativas de los YAML,
no copia el YAML como fixture y no usa salidas validadas como patrón. Los YAML
se construyeron mediante una operación de migración puntual separada; el
oráculo de pruebas no se invoca para generarlos. El loader productivo sigue
siendo exclusivamente adapters/yaml_files.load_yaml.

Se compara la totalidad de campos poblados de secciones, conservando
identidades, discriminadores, propósitos, orden, relaciones padre/hijo,
subtítulos, descripciones, notas, campos included/tags, CTA y destinos. Solo se
omiten defaults vacíos/None, no contenido poblado. Identidad archivo/page_id,
locale, revisión, source_ref, SEO, medios y pendientes se comprueban aparte.
La inspección transversal inventaría de forma independiente todos los enlaces
internos serializados de las cinco páginas y exige correspondencia exacta con
los diagnósticos B1.1, además del contraste documental de las nuevas páginas.

Los **62 casos nuevos** incluyen:

- Tres pruebas de paridad completa y reconstrucción JSON, una por página.
- Tres pruebas de SEO y pendientes exactos, una por página.
- Cuarenta y ocho mutaciones: 16 por página, todas válidas para Pydantic y
  rechazadas por paridad: texto; orden de bloques; bloque omitido; tarjeta
  omitida; CTA; destino; agrupación de descripciones; afirmación absoluta;
  contenido adicional; transversal omitido; nota omitida; orden de tarjetas;
  orden de necesidades; jerarquía alterada; puntuación; ancla alterada.
- Seis mutaciones específicas de included ENE y tags DIG: orden, omisión y
  cambio de padre. Conservan validación Pydantic y fallan fidelidad.
- Dos inspecciones reales del conjunto: INCREMENTAL y COMPLETE, referencias
  individuales de todas las páginas, pendientes, dependencias y bundle.

No se duplican los validadores genéricos A1 ni se añaden modelos nuevos.

## 9. Resultados de QA y regresión

Ejecuciones con `.venv/Scripts/python.exe -B -m pytest -q`, temporales nuevos
y safe.directory de proceso para las comprobaciones Git ya existentes:

| Grupo | Resultado |
|---|---:|
| Suite baseline, antes de editar | 422 passed |
| INF focalizada antes de continuar con ENE | 18 passed |
| ENE focalizada antes de continuar con DIG | 18 passed |
| DIG focalizada antes de inspección conjunta | 18 passed |
| Nuevas pruebas A4, ejecución final | 62 passed |
| A1–A3: domain, d03_contract, pending, inicio_content, capacidades_content | 233 passed |
| B1.1: b11_inspection, editorial_loading_b11, editorial_b11_architecture | 108 passed |
| Contratos de arquitectura completos | 17 passed |
| Suite completa final | **484 passed** |

Sin fallos, skips o xfail en las ejecuciones finales. La diferencia contra
baseline es exactamente 62 pruebas. Las focalizadas iniciales precedieron las
seis mutaciones específicas de detalles y las dos inspecciones finales.
La única prueba histórica corregida preserva sus invariantes; los dos fallos
reproducidos antes de corregirla se explican en §5 y no se ocultaron.

## 10. Archivos creados, modificados y arquitectura preservada

Altas A4, exclusivamente:

1. `content/es/pages/infraestructuras.yaml`.
2. `content/es/pages/sistemas_energeticos.yaml`.
3. `content/es/pages/automatizacion_control.yaml`.
4. `tests/integration/test_specialty_content.py`.
5. `docs/project_v02/CONTENT_ES_01_A4.md`.

Único archivo preexistente modificado:
`tests/integration/test_capacidades_content.py`, preparación del escenario
histórico A3 descrita en §5. Como ya estaba sin seguimiento, esa edición no
aparece en git diff; se contrastaron su hash inicial y la edición puntual.

Comparación final de las 117 huellas: **116 archivos idénticos**, incluida
la totalidad de producción, Inicio, Capacidades e informes anteriores; una
modificación autorizada de pruebas y cero bajas. No se detectaron cambios
concurrentes. Estado Git final: conserva la lista inicial y añade las cinco
altas A4. Rama y HEAD se mantienen. Verificación de whitespace de las altas y
del archivo editado sin incidencias.

No se modificaron application, adapters, site, localization, rutas, idiomas,
templates, media, dependencias, pyproject, D03/D04/D05, mockups ni otras páginas.
No se introdujeron contratos alternativos, dataclasses, servicios, parser
productivo, rendering, publicación o despliegue. Editorial mantiene su
independencia del filesystem/YAML/WEB. Se reutilizan Pydantic v2, loader único,
resolver de pendientes y reglas de integridad B1.1 sin cambiar sus políticas.

No se ejecutaron add, commit, push, merge, reset, clean, stash ni cambio de rama.
Los temporales de pruebas permanecen fuera del repositorio; no se guardaron
scripts de migración ni artefactos auxiliares persistentes en el proyecto.

## 11. Bloqueos y riesgos residuales

No hay bloqueos de representación ni contradicciones editoriales que impidan
entregar las tres páginas completas. Se conservan estas limitaciones legítimas:

- Revisión humana de los tres YAML antes de cambiar draft. Aprobar el contenido
  fuente no equivale a aprobar su migración o publicar.
- SEO INF/ENE requiere decisión DEC-05; no se usan propuestas no aprobadas.
- Cinco medios aprobados esperan contrato MediaRef y la posterior integración
  WEB de procedencia, licencias, alt, recorte y correspondencia de manifiesto.
- Contacto y Proyectos y experiencia todavía no tienen contenido migrado.
  Sectores y Sobre BAFRAS también faltan para la completitud. El bundle íntegro
  continúa rechazándose por diseño.
- El texto de experiencia no acredita proyectos, permisos, habilitaciones o
  actividad contratada. Las comprobaciones de evidencias/publicación quedan
  pendientes en sus fases propias; no se crean catálogos para simularlas.
- La paridad de datos no certifica rendering, títulos HTML, migas, responsive,
  accesibilidad, traducciones o navegación productiva. No se ejecutó QA visual
  de una salida web inexistente en el alcance de esta intervención.
- Frozen de A1 es superficial y B1.1 no garantiza snapshot atómico; cambios
  posteriores requieren nueva inspección. Todo el trabajo sigue sin commit.

## 12. Dictamen final

**GO CON CONDICIONES.** INF-01–INF-07, ENE-01–ENE-07 y DIG-W01–DIG-W07 están
completos, fieles y válidos. Referencias y pendientes son coherentes; cinco
páginas válidas y cuatro ausentes; cero documentos inválidos y cero errores de
selectores. Las 484 pruebas aprobadas respaldan la paridad y regresión. Inicio
y Capacidades permanecen intactos. No fue necesario cambiar el dominio.

Las condiciones son revisión editorial del YAML, decisión SEO INF/ENE,
integración posterior de los medios aprobados y migración de destinos para
completar el conjunto. Ninguna implica pérdida del contenido entregado.

Se entrega este informe único y se detiene A4. **No se inicia A5 ni se realizan
commits.**
