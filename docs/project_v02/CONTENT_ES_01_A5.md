# CONTENT-ES-01 / A5 — Cierre de migración editorial ES

Fecha: 06/11/2026. Dictamen: **GO CON CONDICIONES**.
Se migraron los 18 bloques restantes. Las nueve páginas y los catálogos
necesarios validan; **EditorialBundle se construye con ambas políticas**.
Suite completa: **544 passed**. El conjunto conserva revisión draft y pendientes
editoriales; no se autoriza publicación ni funcionamiento WEB.

## 1. Baseline real

Rama inicial/final: `feat/contingut-v2`. HEAD inicial/final:
`fca65e8ba7d75317be150e3f428be67d87825d34`.
Se consultó git status con todos los archivos sin seguimiento antes de editar.
Los seis YAML A5, las dos pruebas nuevas y este informe no existían.
La búsqueda no localizó AGENTS.md en el árbol del proyecto.

Estado inicial completo:

```text
 M src/bafras_web/editorial/__init__.py
?? content/es/pages/automatizacion_control.yaml
?? content/es/pages/capacidades.yaml
?? content/es/pages/infraestructuras.yaml
?? content/es/pages/inicio.yaml
?? content/es/pages/sistemas_energeticos.yaml
?? docs/project_v02/CONTENT_ES_01_A1.md
?? docs/project_v02/CONTENT_ES_01_A2_1.md
?? docs/project_v02/CONTENT_ES_01_A2_INICIO.md
?? docs/project_v02/CONTENT_ES_01_A3.md
?? docs/project_v02/CONTENT_ES_01_A4.md
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
?? tests/integration/test_specialty_content.py
?? tests/unit/editorial/conftest.py
?? tests/unit/editorial/test_b11_inspection.py
?? tests/unit/editorial/test_d03_contract.py
?? tests/unit/editorial/test_domain.py
?? tests/unit/editorial/test_pending.py
```

Se registraron SHA-256 en memoria de **122 archivos preexistentes** de
src/tests/content/config/docs y pyproject.toml, incluidos los archivos sin
seguimiento. Baseline reejecutado: **484 passed**. Se usaron temporales nuevos
fuera del repositorio mediante PYTEST_DEBUG_TEMPROOT y safe.directory limitado
al proceso/comando por la propiedad distinta del checkout; no se cambió
configuración Git persistente. No se descartó trabajo previo.

## 2. Fuentes y precedencia aplicada

| Fuente | Aplicación |
|---|---|
| D03 V1.22, `03_contenido_editorial_V1_22_baseline_G1.md` | Texto literal de SEC-01–05, PE-01–04, SB-01–05 y CO-01–04; 18 bloques |
| D03 03.K §1 | Titulaciones exactas, especialidades editoriales y presentación corporativa del equipo; supera perfiles propuestos anteriores |
| D03 03.K §2 y 03.G1-02 | Experiencia del equipo frente a encargos BAFRAS; sin referencias confirmadas no se muestran tarjetas ni fichas vacías |
| D03 03.SEC.CAT-01/02 | Seis identidades sectoriales estables; PDF opcionales, sin presumir existencia ni publicar controles sin documentos |
| D03 03.K.2, 03.CO-02 y 03.G1-02 | Mensajes cortos de estado, correo y teléfono aprobados; introducción/ayuda de CO V1.1 y H2/párrafo de CO-03 prevalecen sobre variantes del prototipo |
| D03 03.G1-01 | Prioridad del contenido aprobado sobre HTML y estados históricos; nueve páginas individualmente aprobadas no equivalen a publicación |
| D04 V2.4 | Registro WEB, nueve identidades, separación de capas y responsabilidades |
| D05 V4.12, §36–47 | Composiciones aprobadas SEC V3, PE V1, SB V1 y CO V2, estados documentales y alternativas sin fotografías |
| Cuatro ZIP de `maquetas_aprobadas/`: C04_SEC_V3_aprobado_BAFRAS, C04_PE_V1_BAFRAS, C04_SB_V1_BAFRAS y C04_CO_V2_BAFRAS | Inspección de HTML interno, jerarquía, imágenes y canales; sin extraer artefactos persistentes ni generar copy desde HTML |
| WEB-G1 y DEC-05 | Se mantienen pendientes SEO de las cuatro páginas anteriores; ninguna propuesta se convierte en aprobada |
| Informes A1, A2.1, B1.1, A3 y A4 y código real | Modelos, formato de catálogos, loader único, políticas, pendientes y oráculos reutilizados |

Las cuatro maquetas nuevas no contienen imágenes HTML. SB admite expresamente
la alternativa tipográfica sin retratos; no se inventan pendientes MediaRef
para una fotografía todavía inexistente. No se modificó ningún documento
maestro, maqueta o informe anterior.

## 3. Estabilización focalizada de A4

### Inventario histórico

Se revisaron los escenarios B1.1/A3 ya aislados y se conservaron intactos.
El escenario A4 de cinco páginas seguía usando el checkout real. Tras completar
las páginas, su ejecución focalizada reprodujo **dos fallos**, uno por política,
al encontrar cuatro páginas adicionales en la aserción del conjunto válido.

Causa raíz: escenario histórico unido a inventario mutable. Se añadió únicamente
preparación temporal a `test_real_five_page_integrity_and_each_outgoing_reference`:
copiar configuración y las cinco páginas reales de A4 al temporal. No se
sustituyeron contadores por nueve ni se cambiaron sus invariantes. La nueva
prueba A5 inspecciona por separado el checkout completo y cada referencia.

### Independencia y omisiones del oráculo

Se conservó el oráculo A4: lee D03, no YAML ni objetos validados para formar
expectativas; la utilidad puntual de migración no se importó ni se guardó en
pruebas. Mantiene cardinalidad 7 bloques, 5/6/5 necesidades, 4/6/6 ámbitos,
cuatro entregables, notas, transversales y relación padre/hijo. Las exclusiones
de códigos de catálogo/reglas internas INF están justificadas por D03.

Se añadieron **tres comprobaciones negativas documentales** al mismo archivo:
para cada especialidad se elimina en memoria la primera necesidad de D03 y se
exige que el oráculo falle por cardinalidad antes de comparar con YAML.
Las tres pasan. No se reescribió el extractor ni se añadió un framework.

### Cinco medios A4

| Medio | Fuente | Selector existente | Resultado |
|---|---|---|---|
| R18 | D05 §26 | INF: sections/inf-01/media | válido / integration_pending |
| R10 | D05 §29 | ENE: sections/ene-01/media | válido / integration_pending |
| R08 | D05 §29 | ENE: sections/ambitos/media | válido / integration_pending |
| R01 | D05 §31 | DIG: sections/dig-w01/media | válido / integration_pending |
| R03 | D05 §31 | DIG: sections/ambitos/media | válido / integration_pending |

Las pruebas exactas A4 contrastan identificador, fuente, selector y motivo.
No se encontró defecto ni se modificó ningún YAML A1–A4. No se implementó MediaRef.

## 4. Inventario de los 18 bloques y modelos

| Bloque | Contenido preservado | Modelo existente |
|---|---|---|
| SEC-01 | Eyebrow, H1, párrafo, ancla sectores y Contacto | HeroSection |
| SEC-02 | H2, introducción, seis sectores canónicos en orden | SectorIndexSection, seis Sector en catálogo |
| SEC-03 | Problemas transversales, párrafo y Capacidades | TextSection |
| SEC-04 | Colaboración con equipos de proyecto y Sobre BAFRAS | TextSection |
| SEC-05 | Pregunta/contexto, párrafo y Contacto | TextSection |
| PE-01 | Eyebrow, H1, párrafo y nota visible de atribución | HeroSection con attribution |
| PE-02 | H2/intro, tres agrupaciones con título e introducción; referencias pendientes | ExperienceIndexSection, tres ExperienceGroup sin entradas |
| PE-03 | Cómo se documentará la intervención, sin afirmar evidencias inexistentes | TextSection |
| PE-04 | Pregunta/párrafo, Contacto y Capacidades | TextSection |
| SB-01 | Eyebrow, H1, párrafo y enlace a experiencia | HeroSection |
| SB-02 | H2, introducción, presentación corporativa 03.K y Murti/Àngel/Amin | TeamSection, tres Person en catálogo |
| SB-03 | Introducción, cuatro principios y condición contractual de cierre | ProcessSection / principles |
| SB-04 | Dos párrafos de experiencia/colaboración y enlace al índice | TextSection |
| SB-05 | Pregunta/párrafo, Contacto y Capacidades | TextSection |
| CO-01 | Eyebrow, H1 e introducción CO V1.1 ratificada | HeroSection |
| CO-02 | Cuatro campos, opcionalidad, ayuda íntegra, botón, mensajes 03.K.2; privacidad pendiente | ContactFormSection, FormField, FormMessages |
| CO-03 | H2/párrafo D03; correo y teléfono 03.CO-02 con sus canales | TextSection, ContactChannel/ContactLink |
| CO-04 | H2 y párrafo de orientación sin exigir definición completa | TextSection |

Todas las páginas conservan `page_id` oficial, source_block, orden y revisión
draft. El loader aporta locale es, que no se duplica en YAML. SEC-02 usa
`id: sectores` para preservar el ancla aprobada; los demás IDs de bloque siguen
sec/pe/sb/co-XX. No se crean bloques adicionales ni se fusionan los existentes.

## 5. Catálogos y atribución

Se crearon únicamente dos catálogos necesarios, con raíz secuencia conforme a
B1.1 y validación TypeAdapter sobre modelos A1:

- `entities/sectors.yaml`: seis Sector, títulos y descripciones exactos,
  tres ejemplos por sector y un enlace contextual propio. Orden: turismo y
  terciario; industria/logística/agroindustria; servicios públicos;
  salud/educación/equipamientos; edificación/rehabilitación/activos;
  comunidades energéticas e infraestructuras tecnológicas. Se conservan las
  seis identidades canónicas de 03.SEC.CAT-01, sin subpáginas adicionales.
- `entities/people.yaml`: Murti, Àngel y Amin, en ese orden. Titulaciones:
  ingeniero industrial; ingeniero industrial; ingeniero técnico electrónico.
  Especialidades literales 03.K §1, sin años, cargos, habilitaciones, proyectos
  o biografías inventadas. Cada persona sigue en draft y verification conserva
  verified/authorized false. Se registran pendientes de grafía pública y
  biografía contrastada, sin afirmar que estas estén verificadas.

Estos catálogos son necesarios porque SectorIndexSection y TeamSection
referencian entidades; incrustar copias perdería la relación prevista por A1.
No se creó common.yaml: no hay consumidores de acciones compartidas que lo
exijan. Tampoco experiences.yaml ni resources.yaml vacíos para completar cifras.

PE conserva Infraestructuras, Automatización y Sistemas energéticos con sus
introducciones aprobadas. Las seis candidatas —Formentor, centro educativo de
Mallorca, residencia de Ibiza, sistemas eólicos, HVAC UIB y transformación
energética UIB— siguen sin fichas/autorizaciones. Conforme a 03.K §2/03.G1-02
no se persisten como hechos o tarjetas públicas, no se crean enlaces vacíos ni
un catálogo Experience por anticipación. El pendiente sobre groups hace
explícita esa dependencia. Los textos provisionales y listas de sistemas son
inventario interno, no copy publicable omitido. No se transforma trayectoria
previa del equipo en cartera contratada por BAFRAS.

## 6. Correcciones mínimas de dominio

Se añadieron primero pruebas que reproducen los límites reales de A5; después
se aplicaron cuatro ampliaciones aditivas, sin relajar invariantes:

| Caso reproducido | Causa y solución mínima | Archivo |
|---|---|---|
| ContactChannel rechaza value con extra_forbidden | No podía conservar etiqueta de canal y dato aprobado unidos. Se añade value: PublicText opcional, default None compatible con A1 | editorial/sections.py |
| FormField rechaza required con extra_forbidden | No había campo tipado para distinguir tres obligatorios y empresa opcional. Se añade required: bool opcional; None preserva datos antiguos sin asumir obligatoriedad | editorial/sections.py |
| sections/co-02/privacy_text devuelve field_not_allowed | El formulario ya admite privacidad opcional, pero el resolver no permitía declarar su fuente ausente. Se habilita solo ese campo en ContactFormSection | editorial/pending.py |
| sections/pe-02/groups devuelve field_not_allowed | Los grupos existentes podían quedar sin referencias confirmadas, pero no seleccionarse como colección pendiente. Se habilita groups solo en ExperienceIndexSection y se amplía el tipo de resultado | editorial/pending.py |

Las cuatro regresiones nuevas pasan. Se comprobó también que los selectores
siguen rechazándose en hero y que los consumidores anteriores admiten campos
no declarados con defaults None. No se cambió integridad, elegibilidad del
bundle, políticas, rutas, idiomas, aplicación ni adaptadores.

Se eligió ampliar los contratos existentes frente a concatenar datos nuevos
en etiquetas, guardar obligatoriedad en texto informal o inventar selectores
provisionales. Son datos editoriales, no lógica de validación de navegador,
envío de correo, telefonía o presentación.

## 7. Contacto, SEO y pendientes

Contacto aplica la precedencia 03.G1-02: introducción CO-01 y ayuda del campo
consulta de CO V1.1; éxito «Tu consulta se ha enviado correctamente.» y error
«No hemos podido enviar tu consulta. Escríbenos a info@bafras.com.» de 03.K.2.
Se conserva el H2 «¿Prefieres escribirnos directamente?» y su párrafo, frente
al H2 alternativo del prototipo. Canal email: info@bafras.com; teléfono:
+34 610 903 179. Ambos son datos aprobados, no operatividad comprobada.

El formulario sigue siendo representación editorial: Nombre, correo y consulta
son obligatorios; empresa opcional. Se preservan los indicadores de sus
etiquetas, la ayuda y la puntuación D03. No se implementan envío, validación
WEB, consentimiento, backend ni mensaje de éxito automático. La privacidad
queda None con source_missing, sin fabricar texto legal o enlace fuera del
registro WEB. La adaptación opcional del H2 de contacto al teléfono no se
ejecuta: requeriría aprobar otro copy.

SEO: Sectores, Sobre BAFRAS y Contacto usan sus title/description literales de
D03. PE usa su título aprobado; la descripción tiene intención temática pero
no literal aprobado y queda None/source_missing. Los pendientes DEC-05 de
Inicio/Capacidades/INF/ENE se preservan intactos.

Pendientes nuevos de página: descripción SEO PE; grupos PE pendientes de
verificación; privacidad CO-02. **19 anteriores + 3 = 22**. Se añaden seis
pendientes de personas, dos por persona. Los cinco medios A4 y los de Inicio
permanecen intactos. No se generan referencias ficticias a fotografías o PDF.

## 8. Inspección de las nueve páginas y EditorialBundle

Se ejecutaron inspect_editorial para ambas políticas, auditoría con
assess_integrity(report_resolved=True) y build_editorial_bundle real:

| Resultado observado | INCREMENTAL | COMPLETE |
|---|---:|---:|
| Páginas configuradas / válidas | 9 / 9 | 9 / 9 |
| Páginas ausentes | 0 | 0 |
| Documentos inválidos | 0 | 0 |
| Referencias internas y de catálogo RESOLVED | 73 | 73 |
| Referencias UNRESOLVED | 0 | 0 |
| EXTERNAL_CONTACT_UNCHECKED / UNVERIFIABLE | 2 info | 2 info |
| EDITORIAL_PENDING | 22 info | 22 info |
| ENTITY_PENDING_UNCHECKED | 6 warning | 6 warning |
| PENDING_SELECTOR_INVALID | 0 | 0 |
| Errores | 0 | 0 |
| Catálogos requeridos | people, sectors | people, sectors |
| documents_complete / can_build_bundle | true / true | true / true |

Ambas políticas producen seis warnings y 24 info. Las dos referencias externas
son los canales de contacto, no destinos editoriales rotos. Los seis avisos de
persona conservan el límite explícito B1.1: el resolver de páginas no se aplica
a entidades. Las pruebas de catálogo verifican que sus campos pendientes
existen y los datos siguen sin acreditación; no se presentan estos avisos como
errores de selector ni se cambia la política para ocultarlos.

Bundle construido: nueve páginas / **51 bloques**, seis sectores, tres personas,
cero experiencias y cero recursos. Los 16 destinos no verificables A4 pasan a
estar disponibles. Se comprueba cada selector y destino de todas las páginas
y sectores, no solo los totales; el recuento 73 procede de los datos reales.
No se fijan artificialmente cantidades de warnings para conseguir completitud.

El constructor se ejecuta con sus precondiciones existentes. Que el conjunto
sea íntegro no significa que el contenido draft, las personas, los canales,
privacidad o materiales estén aprobados para publicar.

## 9. Pruebas y regresión

`tests/integration/test_es_completion_content.py` concentra las cuatro páginas
y sus dos catálogos para compartir mecanismos sin duplicar oráculos. Lee D03
y decisiones aprobadas mediante extracción de pruebas independiente; no
utiliza el YAML ni objetos validados para obtener expectativas y no comparte
la transformación de la migración puntual.

La comparación incluye todos los campos poblados de cada sección, relaciones
padre/hijo, orden, puntuación, condiciones, formularios, canales, atribución,
catálogos y sus enlaces. SEO, review/source_ref y pendientes se verifican por
separado. Solo se omiten defaults None/listas vacías; texto o entidades añadidos
y omisiones respecto a D03 producen diferencias. Se comprueban cardinalidades
de seis sectores, tres ejemplos por sector, tres personas, tres grupos PE y
cuatro principios SB, además del inventario exacto de bloques.

Las mutaciones válidas Pydantic cubren bloque omitido, texto, orden, CTA,
destino, experiencia convertida en contratación corporativa, condiciones de
alcance sustituidas por garantías y claims añadidos: ocho por cada página.
Otras ocho mutaciones de catálogos comprueban omisión, orden, cambio de padre
y claims de sectores/personas. Las expectativas permanecen independientes.
Las tres omisiones documentales negativas A4 comprueban cobertura del oráculo.

Ejecuciones finales con `.venv/Scripts/python.exe -B -m pytest -q`:

| Grupo | Resultado |
|---|---:|
| Suite baseline A4 | 484 passed |
| Sectores focalizada al migrar | 9 passed |
| PE focalizada al migrar | 9 passed |
| Sobre BAFRAS focalizada al migrar | 9 passed |
| A5 + A4 focalizadas finales, incluidas regresiones de dominio | 122 passed |
| Regresión editorial e integración A1–A5/B1.1 explícita | 452 passed |
| Contratos de arquitectura | 17 passed |
| Suite completa final | **544 passed** |

Incremento de 60 casos: 53 de migración/catálogos/integridad A5, cuatro de
contrato y tres omisiones documentales negativas A4. Cero fallos, skips y xfail
en las ejecuciones finales. Los fallos previos de reproducción se corrigieron
por causa raíz; no se relajaron tests para obtener verde.

## 10. Archivos creados, modificados y protección

Altas A5:

1. content/es/pages/sectores.yaml.
2. content/es/pages/proyectos_experiencia.yaml.
3. content/es/pages/sobre_bafras.yaml.
4. content/es/pages/contacto.yaml.
5. content/es/entities/sectors.yaml.
6. content/es/entities/people.yaml.
7. tests/integration/test_es_completion_content.py.
8. tests/unit/editorial/test_a5_contract.py.
9. docs/project_v02/CONTENT_ES_01_A5.md.

Modificaciones preexistentes: editorial/sections.py, editorial/pending.py y
tests/integration/test_specialty_content.py, exclusivamente las correcciones y
pruebas descritas. Las huellas originales de los tres se contrastaron antes
de intervenir. Al ser archivos previamente sin seguimiento, git diff no basta
para detectarlos; se usó comparación SHA-256 del inventario inicial.

Comparación final de los 122 archivos preexistentes: **119 idénticos**, tres
modificaciones autorizadas y cero bajas. Inicio, Capacidades, INF/ENE/DIG y
todos los informes anteriores permanecen idénticos. No se detectaron cambios
concurrentes. Estado Git final: lista inicial más las nueve altas A5, rama/HEAD
intactos. Whitespace revisado en los doce archivos de la intervención.

No se modificaron configuración, dependencias, pyproject, D03/D04/D05, mockups,
application, adapters, site, localization, templates o media. No se añadieron
dataclasses ni contratos informales entre capas. Los campos nuevos heredan los
contratos estrictos Pydantic v2 existentes. El dominio permanece independiente
de YAML/filesystem/WEB. Los temporales quedan fuera del repositorio y no se
guardaron generadores o artefactos auxiliares de migración.

No se ejecutaron git add, commit, push, merge, reset, clean, stash, cambios de
rama ni modificaciones de configuración Git persistente.

## 11. Riesgos residuales y dictamen

**GO CON CONDICIONES**: migración española completa y fiel en su contenido
aprobado, 51 bloques, referencias íntegras, catálogos válidos y bundle
construible con ambas políticas, sin regresiones. No hay bloqueo técnico para
continuar con la revisión conjunta e integración posterior autorizada por WEB.

Condiciones pendientes: revisión humana de los nueve documentos draft; SEO
DEC-05 y descripción PE; privacidad e identidad jurídica reales; verificación
de nombres/biografías y autorización de referencias; operatividad de correo y
teléfono; contrato e integración de medios; permisos y eventual disponibilidad
de PDF. Las seis candidatas PE no se publican ni se consideran cartera BAFRAS.

B1.1 sigue sin resolver selectores de entidades ni verificar hechos o canales
externos: se conserva ese límite y sus avisos. La validación superficial frozen
y la lectura no atómica requieren reinspección tras cambios posteriores.
La representación del formulario no implica que exista una funcionalidad de
envío. No se ejecutó rendering, HTML, CSS, JavaScript, responsive, backend,
despliegue o traducciones, que quedan fuera de A5.

Se entrega este informe único. No se creó A4.1, no se inició presentación WEB
y no se realizaron commits ni se solicitó revisión humana intermedia.
