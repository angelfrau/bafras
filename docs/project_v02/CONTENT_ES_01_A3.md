# CONTENT-ES-01 / A3 — Auditoría y migración de Capacidades

Fecha: 06/11/2026. Intervención A3.0 + A3.1. Dictamen: **GO CON CONDICIONES**.
Capacidades conserva C01–C05 y valida con A1/B1.1. El YAML sigue en revisión
`draft`, con SEO pendiente. No acredita publicación ni completa el conjunto ES.

## A. Baseline y fuentes

Rama inicial: `feat/contingut-v2`. HEAD:
`fca65e8ba7d75317be150e3f428be67d87825d34`.
Se verificaron estado Git con todos los archivos sin seguimiento y existencia
de los destinos. Capacidades, sus pruebas y este informe no existían. No se
localizó AGENTS.md en el árbol inspeccionado. Se conservaron huellas SHA-256 en
memoria de 114 archivos preexistentes de src/tests/content/config/docs y
pyproject.toml, incluyendo archivos sin seguimiento, antes de editar.

Estado Git inicial completo:

```text
 M src/bafras_web/editorial/__init__.py
?? content/es/pages/inicio.yaml
?? docs/project_v02/CONTENT_ES_01_A1.md
?? docs/project_v02/CONTENT_ES_01_A2_1.md
?? docs/project_v02/CONTENT_ES_01_A2_INICIO.md
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
?? tests/integration/test_editorial_loading_b11.py
?? tests/integration/test_inicio_content.py
?? tests/unit/editorial/conftest.py
?? tests/unit/editorial/test_b11_inspection.py
?? tests/unit/editorial/test_d03_contract.py
?? tests/unit/editorial/test_domain.py
?? tests/unit/editorial/test_pending.py
```

La suite inicial confirma **400 passed**. La primera ejecución sin preparar el
entorno produjo errores de acceso al temporal compartido
`pytest-of-murti`; una ejecución focalizada reprodujo PermissionError en setup.
La repetición con `PYTEST_DEBUG_TEMPROOT` apuntando a un directorio nuevo dentro
del temporal permitido pasó íntegra. Git detectó propiedad distinta del checkout;
se usó `safe.directory` solo por comando/proceso, sin modificar configuración
persistente. No se alteró código para solucionar estas restricciones del entorno.

Fuentes consultadas y precedencia:

| Fuente | Autoridad y aplicación |
|---|---|
| D03 V1.22, `03_contenido_editorial_V1_22_baseline_G1.md`, C01–C05, líneas 160–286 | Copy, orden, alcance condicional, ámbitos, ejemplos, modalidades y acciones |
| Cabecera/registro D03 y adenda 03.G1-01 | Ratifican aprobación individual y prioridad del contenido D03 frente al prototipo; superan la leyenda local histórica «pendiente» |
| D03 03.G1-02 | Revisada: resuelve variantes de Contacto/atribución PE; no cambia C01–C05 |
| D04 V2.4, `04_arquitectura_software_V2_4_handoff_G1.md` | Separación de responsabilidades, nueve páginas e identidades; implementación real contrastada con configuración WEB |
| D05 V4.12, `05_sistema_visual_V4_12_baseline_G1.md`, §32–35 y notas de vigencia | §35 aprueba composición CAP V1: filas equivalentes, ejemplos, modalidades independientes y ausencia deliberada de fotografías |
| `maquetas_aprobadas/C04_CAP_V1_BAFRAS.zip`, HTML y README internos | Inspección sin extraer archivos persistentes; vínculos contextuales y orden. Cero imágenes HTML. No se ingiere copy del prototipo |
| `WEB_G1_CLOSE_DECISIONES.md`, DEC-05 | Propuestas SEO sin aprobación: no se convierten en metadatos definitivos |
| `WEB_G1_REVIEW_01_INCIDENCIAS.csv`, WGR-027/028; matriz de cierre | Excluir rótulos de maqueta e incluir «Ejemplos de aplicación» exigido por D03 |
| Informes A1, A2, A2.1, B1.0 y B1.1 | Modelos, persistencia, estrategia de paridad, pendientes y políticas de integridad existentes |

Se inspeccionaron los ocho módulos editoriales indicados, entidades y páginas,
application/editorial, adapters/editorial_files y yaml_files, rutas/localización,
Inicio y pruebas editoriales, de integración y arquitectura. El código describe
el comportamiento real; su validez estructural no sustituye autoridad editorial.

## B. Auditoría editorial C01–C05

Matriz de trazabilidad; todos los textos completos se preservan en el YAML y se
contrastan directamente con D03 mediante el oráculo de pruebas independiente.

| Bloque → fuente | Elementos y jerarquía | Modelo A1 | Referencias | Pendientes | Compatibilidad |
|---|---|---|---|---|---|
| C01 → D03 C01; D05 §35 | Antetítulo NUESTRAS CAPACIDADES; H1 «Tres especialidades de ingeniería. Soluciones ajustadas a cada proyecto.»; introducción; orientación | HeroSection, Paragraph, CallToAction | Capacidades → especialidades (C02) | Ninguno propio | COMPATIBLE |
| C02 → D03 C02; D05 §35 | H2 «Encuentra la especialidad que necesita tu proyecto.»; introducción; tres áreas de igual jerarquía, cada una con descripción, cuatro ámbitos y enlace | CardsSection(capabilities), CapabilityCard, TextItem | INF, ENE, DIG | Ninguno propio | COMPATIBLE |
| C03 → D03 C03 y jerarquía visual; D05 §33–35; CAP V1 | Etiqueta «Ejemplos de aplicación»; H2 «Cuando las instalaciones, la energía y el control están relacionados.»; introducción; tres ejemplos condicionales con disciplinas enlazadas | CardsSection(application_examples), ApplicationExampleCard | Nueve enlaces contextuales ordenados | Ninguno propio | COMPATIBLE |
| C04 → D03 C04; D05 §35 | H2 «Ingeniería en distintas fases de un proyecto.»; introducción; cuatro modalidades independientes | ItemListSection(modalities), DeliveryItem | Ninguna | Ninguno propio | COMPATIBLE |
| C05 → D03 C05; D05 §35 | H2 «¿Qué necesitas resolver o desarrollar?»; párrafo; CTA principal y enlace secundario | TextSection, Paragraph, CallToAction | Contacto; Proyectos y experiencia | Ninguno propio | COMPATIBLE |
| Página → DEC-05; A1/A2/B1.1 | Identidad capacidades, idioma es aportado por contexto, revisión draft; metadatos null | PageContent, SeoMeta, EditorialReview, PendingField | Registro WEB | seo.title y seo.description: approval_required | COMPATIBLE CON PENDIENTES |

Inventario interno, en orden documental:

1. **C02 / infrastructure — Infraestructuras e instalaciones.** Descripción de
   diseño, análisis y mejora de instalaciones y alcance definido por encargo.
   Ámbitos: Instalaciones eléctricas de baja y media tensión; Climatización,
   ventilación y sistemas térmicos; Instalaciones hidráulicas y saneamiento;
   Coordinación y asistencia técnica. CTA: «Ver infraestructuras e instalaciones».
2. **C02 / energy — Sistemas energéticos.** Descripción de demanda, operación,
   alternativas y viabilidad con datos disponibles. Ámbitos: Análisis y auditoría
   energética; Eficiencia y optimización; Fotovoltaica y autoconsumo;
   Almacenamiento y gestión energética. CTA: «Ver sistemas energéticos».
3. **C02 / automation — Automatización y control.** Descripción de instrumentación,
   control, supervisión, integración, datos y comunicación. Ámbitos:
   Instrumentación y adquisición de datos; PLC y controladores DDC; BMS y SCADA;
   Comunicaciones, integración y software técnico. CTA: «Ver automatización y control».
4. **C03 / thermal-modernization — Modernización de una instalación térmica.**
   Conserva literalmente la posibilidad de estudiar equipos/circuitos, demanda
   y regulación. Disciplinas: INF → ENE → DIG.
5. **C03 / self-consumption-storage — Autoconsumo y almacenamiento.** Conserva
   literalmente generación/baterías, perfil energético, instalación eléctrica,
   medida y control como necesidades posibles. Disciplinas: ENE → INF → DIG.
6. **C03 / installation-performance — Problemas de funcionamiento en una instalación.**
   Conserva literalmente la comprobación previa de operación, equipos y
   señales/secuencias antes de decidir una reforma. Disciplinas: INF → DIG → ENE.
7. **C04 / diagnosis-studies — Diagnóstico y estudios.** «Inspección técnica dentro
   del alcance contratado, análisis de datos, mediciones y evaluación de alternativas.»
8. **C04 / design-project — Diseño y proyecto.** «Definición de soluciones,
   cálculos, planos, especificaciones y documentación técnica.»
9. **C04 / assistance-coordination — Asistencia y coordinación.** «Apoyo a la
   planificación, revisión de interfaces, seguimiento técnico y coordinación
   con los agentes del proyecto.»
10. **C04 / programming-integration-verification — Programación, integración y
    verificación.** «Configuración de sistemas, pruebas y documentación de
    resultados cuando estas actuaciones formen parte del encargo.»

Los ámbitos conservan su puntuación original, incluido el punto terminal del
cuarto elemento; los títulos de ejemplo/modalidad conservan el punto de D03.
No se añaden subtítulos, servicios, resultados, certificaciones ni referencias
de proyectos. C03 mantiene «Puede», «puede requerir» y «puede ser conveniente»;
no se transforma en cartera BAFRAS ni en experiencia de fundadores. C04 no es
ProcessSection: su orden editorial no implica cronología contractual.

## C. Compatibilidad Pydantic

Validación real con PageContent Pydantic v2 y reconstrucción JSON satisfactoria.
Familias ordenadas: hero, cards/capabilities, cards/application_examples,
item_list/modalities, text. Cinco source_block: C01–C05. IDs de sección:
`c01`, `especialidades`, `c03`, `c04`, `c05`. La identidad `especialidades`
preserva el contrato de ancla D03 sin añadir una propiedad WEB al dominio.

CapabilityCard.examples representa los cuatro ámbitos ilustrativos de cada
área; no son un catálogo exhaustivo de servicios. La familia semántica cards
admite la composición en filas aprobada: no impone layout. ApplicationExampleCard
conserva la relación descripción/disciplina sin crear entidades Experience.

Los medios existentes solo admiten None. Esta limitación no impide Capacidades,
pues D05 §35 aprueba explícitamente ausencia de fotografías. No corresponde
crear un pendiente de integración visual sin una necesidad editorial real.
No se detectó limitación del dominio ni defecto Pydantic que exigiera corregir
los ocho archivos con autorización condicional.

## D. Incoherencias detectadas

| Hallazgo | Clasificación, causa raíz y evidencia | Resolución |
|---|---|---|
| Leyenda local D03 «pendiente de validación» | Estado documental histórico; cabecera, registro y 03.G1-01 son posteriores y confirman aprobación | Aplicar precedencia documentada, sin editar D03 ni trasladar automáticamente aprobación al YAML |
| Rótulos CAP V1 «C02 /», «C03 /»; falta etiqueta de ejemplos | Divergencia de representación ya registrada WGR-027/028; maqueta no gobierna copy | Usar H2 D03 y eyebrow «Ejemplos de aplicación» exigido por D03; omitir controles internos |
| href HTML físicos | Destinos de prototipo, no contrato editorial A1 | Mapear identidades WEB; ancla semántica especialidades |
| Test B1.1 fija solo Inicio en checkout real | Expectativa de inventario obsoleta tras migración autorizada; antes pasa con 400 pruebas, después valid_pages incluye capacidades e inicio, no solo inicio | Aislar escenario histórico en temporal con Inicio real y mantener todas sus aserciones; A3 verifica inventario real nuevo |
| Temporales/Git sin preparar | Restricciones del entorno de ejecución, no defectos del producto | Temporal nuevo y safe.directory de proceso; sin cambios persistentes de configuración |

No hay contradicción editorial bloqueante en C01–C05. SEO sigue pendiente de
decisión humana y se representa legítimamente con campos opcionales vacíos.

## E. Correcciones implementadas

**No se necesitó corregir software de producción.** Ningún módulo editorial,
WEB o adaptador fue modificado.

Única modificación preexistente: `tests/integration/test_editorial_loading_b11.py`,
función `test_real_inicio_acceptance`. Se añade fixture project, se copia
únicamente el Inicio real al temporal configurado y se inspecciona allí.
La huella del archivo se contrastó contra el baseline inmediatamente antes de
editar: coincidía. Se mantienen las aserciones de nueve páginas esperadas,
una válida, ocho ausentes, catorce referencias no verificables, ocho pendientes
y políticas/bundle. No se usa skip, xfail ni se relajan validadores.

Causa raíz: el test mezclaba escenario de aceptación histórica B1.1 con el
inventario mutable del repositorio. Cambiar únicamente contadores a dos/siete
pospondría el mismo problema a otra migración. Se eligió separar ese escenario
con datos reales en temporal y añadir en A3 comprobación real de las dos páginas,
cada referencia y sus estados. La autorización procede de §§C.1, H y 13 del
encargo para expectativas demostrablemente obsoletas. Regresión B1.1: 108 passed.

## F. Migración de Capacidades

Alta: `content/es/pages/capacidades.yaml`. Convenciones de Inicio preservadas:
locale no duplicado, page_id del registro, source_block trazable, IDs estables,
acciones tipadas, review/source_ref, SEO null y PendingField explícitos.
Los textos se migraron de D03 sin reescritura; el loader productivo sigue siendo
adapters/yaml_files.load_yaml. No se incorpora extracción Markdown a producción.

`review.status: draft` expresa integración pendiente de revisión humana; la
aprobación de D03 no certifica revisión del YAML. `seo.title` y `seo.description`
conservan `approval_required`, fuente DEC-05. No se adopta el title del HTML ni
las propuestas SEO del acta. No hay rutas físicas, PDFs, MediaRef ni manifiestos
ficticios. No se necesitan common.yaml, people.yaml, sectors.yaml,
experiences.yaml ni resources.yaml: todas las acciones son locales e internas.
Las seis identidades sectoriales canónicas quedan intactas.

## G. Integridad B1.1

Carga real ejecutada para ambas políticas con
`inspect_editorial(ProjectPaths(ROOT), EditorialLoadRequest(locale="es", policy=...))`.
Auditoría adicional con assess_integrity(report_resolved=True).

| Resultado real | INCREMENTAL | COMPLETE |
|---|---:|---:|
| Páginas configuradas | 9 | 9 |
| Válidas | capacidades, inicio | capacidades, inicio |
| Ausentes | 7 | 7 |
| Inválidas | 0 | 0 |
| DOCUMENT_MISSING | 7 warning | 7 error |
| REFERENCE_TARGET_UNAVAILABLE / UNVERIFIABLE | 25 warning | 25 warning |
| EDITORIAL_PENDING | 10 info | 10 info |
| Referencias RESOLVED en auditoría explícita | 4 | 4 |
| Referencias UNRESOLVED | 0 | 0 |
| PENDING_SELECTOR_INVALID | 0 | 0 |
| Catálogos requeridos | ninguno | ninguno |
| documents_complete / can_build_bundle | false / false | false / false |

Ausentes: automatizacion_control, contacto, infraestructuras,
proyectos_experiencia, sectores, sistemas_energeticos, sobre_bafras.
INCREMENTAL: 32 warnings y 10 info, sin errores. COMPLETE: 7 errores,
25 warnings y 10 info. El constructor de bundle rechaza ambas inspecciones.

Inventario de enlaces de Capacidades; todos son InternalLink y sus páginas
están configuradas. Solo el ancla dispone ya de contenido destino válido.

| Origen | Texto | Destino (orden cuando múltiple) | Disponibilidad / estado |
|---|---|---|---|
| C01 / explore | Explorar las especialidades | capacidades / especialidades | disponible / RESOLVED |
| C02 / infrastructure | Ver infraestructuras e instalaciones | infraestructuras | ausente / UNVERIFIABLE |
| C02 / energy | Ver sistemas energéticos | sistemas_energeticos | ausente / UNVERIFIABLE |
| C02 / automation | Ver automatización y control | automatizacion_control | ausente / UNVERIFIABLE |
| C03 / thermal-modernization | Infraestructuras e instalaciones; Sistemas energéticos; Automatización y control | infraestructuras; sistemas_energeticos; automatizacion_control | tres ausentes / UNVERIFIABLE |
| C03 / self-consumption-storage | Sistemas energéticos; Infraestructuras e instalaciones; Automatización y control | sistemas_energeticos; infraestructuras; automatizacion_control | tres ausentes / UNVERIFIABLE |
| C03 / installation-performance | Infraestructuras e instalaciones; Automatización y control; Sistemas energéticos | infraestructuras; automatizacion_control; sistemas_energeticos | tres ausentes / UNVERIFIABLE |
| C05 / contact | Cuéntanos tu proyecto | contacto | ausente / UNVERIFIABLE |
| C05 / experience | Conoce nuestros proyectos y experiencia | proyectos_experiencia | ausente / UNVERIFIABLE |

Quince enlaces nuevos: uno resuelto y catorce no verificables. Los tres enlaces
Inicio → Capacidades pasan a RESOLVED (hero, cierre de capacidades, necesidad
multidisciplinar). De los catorce no verificables previos de Inicio quedan once;
11 + 14 = 25. Estas cifras se calcularon del contenido real; las pruebas nuevas
comparan cada selector/destino contra el oráculo documental y su disponibilidad,
sin fijar artificialmente el total de warnings. Los diez pendientes son los
ocho de Inicio preservados y los dos SEO de Capacidades.

## H. Pruebas

Nuevo `tests/integration/test_capacidades_content.py`: 22 casos. Se concentraron
en integración para evitar duplicar en un archivo unitario las reglas genéricas
de modelos que no se modificaron.

El oráculo interpreta D03 en pruebas y conserva estructura padre/hijo, campos
poblados, identidades, familias, orden, puntuación, descripciones, ámbitos,
modalidades, etiquetas de CTA y destinos. No lee expectativas del YAML ni copia
el YAML completo como fixture. Las decisiones de IDs se declaran expresamente;
el orden contextual de C03 procede del HTML CAP V1 aprobado, subordinado al
contrato de orientación de D03. La comparación incluye cualquier campo público
añadido y solo omite defaults None/listas vacías. SEO, revisión y pendientes se
comprueban separadamente con expectativas exactas.

Dieciocho mutaciones en memoria siguen validando con Pydantic y fallan paridad:
texto; orden de bloques; omisión de bloque; omisión de tarjeta; etiqueta CTA;
destino CTA; texto movido a subtítulo; sustitución por proyecto ejecutado;
texto añadido; orden de tarjetas; orden de ámbitos; ámbitos bajo otra capacidad;
descripción bajo otro ejemplo; orden de disciplinas; destino de disciplina;
ancla; orden de modalidades; source_block alterado. Se prueban asimismo
identidad/idioma, reconstrucción JSON, revisión/pendientes/medios y las dos
políticas reales con todos los enlaces y ausencia de dependencias espurias.

Ejecución en orden, mediante `.venv/Scripts/python.exe -B -m pytest -q`:

| Grupo | Resultado |
|---|---:|
| Baseline completo anterior a cambios | 400 passed |
| Capacidades focalizadas | 22 passed |
| Modelos modificados | no aplica: cero cambios de producción |
| A1/A2/A2.1: test_domain, test_d03_contract, test_pending, test_inicio_content | 211 passed |
| B1.1: test_b11_inspection, test_editorial_loading_b11, test_editorial_b11_architecture | 108 passed |
| Contratos de arquitectura completos | 17 passed |
| Suite completa final | 422 passed |

Sin fallos, skips ni xfail en las ejecuciones finales. Los temporales de pytest
quedan fuera del repositorio. No se añaden dependencias ni se modifica pyproject.

## I. Arquitectura y protección Git

Altas A3, exclusivamente:

- content/es/pages/capacidades.yaml.
- tests/integration/test_capacidades_content.py.
- docs/project_v02/CONTENT_ES_01_A3.md.

Modificación A3 preexistente: solo el escenario de aceptación histórica indicado
en tests/integration/test_editorial_loading_b11.py, archivo que ya estaba sin
seguimiento al inicio. Por ello `git diff` no muestra su diferencia: se verificó
su hash inicial y se revisó la edición puntual de la función.

Comparación final de las 114 huellas preexistentes: únicamente cambia ese
archivo de pruebas; cero bajas. Inicio y los 113 restantes permanecen idénticos.
No se observaron cambios concurrentes. Estado Git final conserva íntegra la
lista inicial y añade las tres altas anteriores. Rama y HEAD finales coinciden
con el inicio. No se realizaron cambios de rama, add, commit, push, merge, reset,
clean, stash ni reversiones.

No hay nuevos contratos entre capas. Se usan los modelos Pydantic existentes,
el loader único y los recorridos de integridad B1.1. Editorial conserva su
independencia de filesystem/YAML/WEB. application, adapters, site, localization,
config, templates, media, documentos maestros, mockups e informes anteriores
quedan preservados. No hay rendering, publicación ni modificación de rutas.

## J. Riesgos residuales

- El YAML requiere revisión humana antes de cambiar su estado draft. La suite
  comprueba fidelidad documental, no concede aprobación ni publicación.
- DEC-05 sigue abierto: title y description SEO no se inventan.
- Siete páginas todavía ausentes: sus destinos son conocidos pero no están
  disponibles editorialmente; el bundle completo sigue bloqueado correctamente.
- La ausencia de fotos es una decisión aprobada de esta página. El contrato
  MediaRef sigue pendiente globalmente y no se amplía durante A3.
- Layout en filas, encabezados HTML, accesibilidad, responsive, navegación real,
  logotipo oficial, traducciones y publicación pertenecen a integración WEB/QA.
  El YAML preserva jerarquía semántica, pero no demuestra un render final.
- Enlaces de C03 son orientación contextual; el futuro render no debe convertir
  esa asociación en afirmación de tres disciplinas obligatorias o trabajo real.
- Frozen en A1 no implica inmutabilidad profunda; B1.1 tampoco promete snapshot
  atómico. Reinspeccionar después de cambios externos.
- Todo el trabajo anterior y A3 permanece sin consolidar, conforme al encargo.

## K. Dictamen

**GO CON CONDICIONES** para la migración editorial A3: cinco bloques íntegros,
paridad independiente, referencias tipadas y clasificadas, pendientes válidos y
regresión satisfactoria. No se necesitó corregir el dominio. Las condiciones
son revisión humana del YAML, decisión SEO y migración posterior de destinos
para completar el conjunto; no invalidan la fidelidad de C01–C05 entregados.

Se entrega este informe y se detiene A3. No se inicia A4 ni se realizan commits.
