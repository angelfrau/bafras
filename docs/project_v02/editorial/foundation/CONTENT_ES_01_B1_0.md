# CONTENT-ES-01 / B1.0 — Auditoría contractual y especificación B1.1

Fecha: 05/11/2026. Dictamen: **GO CON CONDICIONES** (véase K).
Este archivo es el único entregable escrito en B1.0. Ninguna interfaz propuesta
en los ejemplos está implementada por esta auditoría.

Convenciones: **H** = hecho comprobado en código; **A** = decisión arquitectónica
ya documentada; **P** = propuesta definitiva recomendada para B1.1;
**D** = decisión que requiere ratificación/autorización en B1.1.
Las rutas y líneas de evidencia son relativas a la raíz Git `bafras/` y a la
fotografía inicial de esta auditoría, incluidos archivos sin seguimiento.

## A. Baseline y estado Git

**H.** Rama `feat/contingut-v2`; HEAD inicial
`fca65e8ba7d75317be150e3f428be67d87825d34`.
WEB-G2-00 tiene los commits locales `762e196` (retirada legacy) y `fca65e8`
(arquitectura, idiomas y rutas); ambos posteriores a `efa5b6f`.

Estado inicial completo:

```text
 M src/bafras_web/editorial/__init__.py
?? content/es/pages/inicio.yaml
?? docs/project_v02/CONTENT_ES_01_A1.md
?? docs/project_v02/CONTENT_ES_01_A2_1.md
?? docs/project_v02/CONTENT_ES_01_A2_INICIO.md
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

**H.** A1/A2/A2.1 siguen sin consolidar. `git diff` contra HEAD no representa por
sí solo este baseline: casi todo el dominio está sin seguimiento. Se registraron
huellas SHA-256 de código, configuración, contenido, pruebas, documentación y
pyproject.toml para detectar modificaciones concurrentes o accidentales.
No se localizó AGENTS.md en la búsqueda realizada en el workspace.

**H.** `CONTENT_ES_01_A2_1.md:177` documenta 292 pruebas aprobadas. La colección
actual con `.venv/Scripts/python.exe -B -m pytest --collect-only -q` devuelve
**292 tests collected**. No se reejecutó la suite: la colección no demuestra que
las 292 sigan pasando. El resultado de aprobación es la evidencia previa de
A2.1, coherente con el código inspeccionado; no una ejecución nueva de B1.0.

Se ejecutaron únicamente lecturas, introspección con Python `-B` y sondas en
memoria del loader mediante `unittest.mock`; sin crear fixtures en disco,
instalar dependencias o ejecutar herramientas que reescriban código.
Git utilizó safe.directory por comando y --no-optional-locks; no se alteró
configuración persistente.

## B. Inventario de contratos existentes

### B.1. Valores e invariantes ya garantizados

| Evidencia | Contrato real y garantía |
|---|---|
| `editorial/primitives.py:19` | EditorialId: cadena estricta con guiones; PageIdentity admite guiones bajos como WEB; LanguageCode solo forma de dos letras |
| `editorial/primitives.py:30` | EditorialModel: strict, extra=forbid, frozen, validate_default; unicidad por colección de hijos con id y listas de referencias |
| `editorial/primitives.py:11` | PublicText rechaza blanco y marcadores de pendiente; conserva el texto |
| `editorial/primitives.py:59` | EditorialReview: draft/reviewed/approved y source_ref opcional; no permiso de publicación |
| `editorial/primitives.py:70` | PendingField: cadena, cinco motivos cerrados y source_ref; la construcción no resuelve el selector |
| `editorial/primitives.py:81` | Verification: verified/authorized falsos por defecto; declaraciones afirmativas requieren evidencia; no certifica esa evidencia |
| `editorial/references.py:31` | LinkRef: unión discriminada internal/external/contact/resource |
| `editorial/references.py:34` | Acción local con label/target o SharedActionRef con common_ref; formas excluyentes por extra=forbid |
| `editorial/sections.py:257` | Section: nueve familias discriminadas por kind |
| `editorial/sections.py:100` | Card: cinco tipos; propósito de CardsSection comprobado contra sus elementos |
| `editorial/sections.py:160` | ItemListSection separa necesidades de entregables/modalidades |
| `editorial/pages.py:21` | PageContent: identidad, locale, review, seo, secciones no vacías; exactamente un hero e IDs de sección únicos |

**H.** Campos obligatorios de PageContent: page_id, locale, review, seo, sections.
pending tiene lista vacía por defecto; SeoMeta.title/description permiten None.
Cada sección tiene id y source_block opcional. Orden editorial = orden de listas;
el modelo no impone el orden D03 ni el número de bloques de una página.
Los tests de aceptación se ocupan de esa paridad (A2.1).

**H.** frozen impide reasignación, no mutación profunda de listas. Los modelos no
son snapshots profundamente inmutables. No se debe construir una caché ni prometer
inmutabilidad profunda basándose en esa opción.

**P.** B1.1 reutiliza todas estas garantías. No repite el conteo de heroes,
discriminadores, forma de IDs, campos desconocidos o unicidad de hijos ya validada.
Sí añade identidad archivo/modelo, pertenencia de idioma y resolución entre
documentos, que los modelos actuales no garantizan.

### B.2. Secciones y lugares reales de referencia

| Familia | Estructura relevante | Evidencia |
|---|---|---|
| Hero | actions; media exclusivamente None | `sections.py:18` |
| Text | actions; contact_channels con ContactLink | `sections.py:30,36` |
| Cards | actions de sección; CapabilityCard.actions; ApplicationExampleCard.disciplines; SectorPreviewCard.action; DisciplineRelationCard.discipline | `sections.py:51,70,84,92,114` |
| ItemList | NeedItem.actions; DeliveryItem no tiene acciones | `sections.py:140,148,160` |
| Process | actions de sección; elementos sin enlaces | `sections.py:177,183` |
| SectorIndex | sector_refs | `sections.py:193` |
| ExperienceIndex | groups[].entries[].experience_ref; entry.id es identidad local, no referencia | `sections.py:200,206,220` |
| Team | person_refs | `sections.py:227` |
| ContactForm | copy de campos/estados/privacidad; sin endpoint ni enlace a política modelado | `sections.py:235,242,247` |

**H.** `ApplicationExampleCard` exige destinos internos; no comprueba que el
page_id referido exista. `source_block` y títulos no son enlaces a documentos.

### B.3. Entidades y contenido común

| Modelo | Identidad, relaciones y restricciones reales |
|---|---|
| Person (`entities.py:23`) | id, public_name y review obligatorios; qualification/specialty/biography opcionales; experience_refs; verification; pending; portrait solo None |
| Sector (`entities.py:36`) | id pertenece a los seis SectorId aprobados; title y description obligatorios; examples; contextual_actions; catalog_refs sin duplicados |
| Experience (`entities.py:58`) | id, kind, title, review obligatorios; founder_previous/bafras_project; person_refs; contexto/intervención/sistemas/fases/entregables; resultados/evidencias; verification; pending |
| DocumentedResult (`entities.py:52`) | id, text y al menos una SourceRef; no registro de evidencias resolubles |
| DownloadableResource (`entities.py:77`) | catalog_id, sector_id canónico, title; description opcional. Es identidad editorial de catálogo, no PDF/versionado físico |
| CommonContent (`pages.py:36`) | navigation_labels/footer_texts/actions/interface_messages, todo por defecto vacío; actions solo CallToAction, nunca SharedActionRef recursivo |

**H.** No existen documentos persistidos de estas entidades ni common.yaml.
Solo existe `content/es/pages/inicio.yaml`. No hay MediaRef, config/site.yaml,
catálogo físico de PDF implementado ni declaración content/schema.yaml.

**P.** Ningún catálogo se exige por tener una clase Python. Su necesidad se deriva
de relaciones reales presentes. No se inventan personas, experiencias, recursos
o archivos vacíos para completar una estructura visual.

## C. Auditoría de EditorialBundle

Evidencia principal: `src/bafras_web/editorial/pages.py:43`.

| Campo | Tipo | Obligatorio / defecto |
|---|---|---|
| locale | LanguageCode | Obligatorio |
| pages | list[PageContent] | [] |
| common | CommonContent | CommonContent() |
| people | list[Person] | [] |
| sectors | list[Sector] | [] |
| experiences | list[Experience] | [] |
| resources | list[DownloadableResource] | [] |

**H.** `_local_identity` (L53) comprueba page_id y catalog_id únicos y locale de
las páginas igual al bundle. La base comprueba IDs de personas, sectores y
experiencias. No exige nueve páginas, no consulta WEB, no resuelve referencias,
no comprueba aprobación ni publicación. get_page/get_person/get_sector/
get_experience/get_resource recorren su colección y lanzan KeyError si falta el ID.

**H.** Sonda real sin escritura: `EditorialBundle(locale='es')` es válido con cero
páginas. También es válido con únicamente Inicio, CommonContent vacío y cuatro
colecciones de entidades vacías. Inicio conserva sus ocho pendientes y ninguno
produce error de selector A2.1. Estas construcciones son legítimas según A1;
no garantizan que los enlaces de Inicio tengan contenido disponible.

**Dictamen sobre la separación propuesta.** Es compatible y necesaria como
convención de aplicación, pero todavía no está implementada: hoy solo existe
el modelo y las pruebas. No se endurece el constructor para exigir nueve páginas.

**P.** La inspección produce inventario, modelos válidos parciales y diagnósticos,
sin construir un bundle como certificado. Una operación explícita adicional
construye EditorialBundle cuando cumple las precondiciones de G.4. Un consumidor
puede seguir construyendo bundles parciales directamente, como permite A1; no
debe interpretarlos como salida del proceso de inspección íntegra.

Los defaults vacíos del modelo se reutilizan únicamente para colecciones no
necesarias y ausentes, dejando constancia en el inventario. No se representan
documentos ausentes como presentes/válidos ni se crean entidades ficticias.

## D. Contratos WEB verificados

### D.1. Identidades y rutas

**H.** `RouteTable.pages` (`site/routes.py:31`) es el diccionario autoritativo.
Tras `load_site_routing(paths)`, B1.1 obtiene:

```python
expected_page_ids = tuple(sorted(routing.routes.pages))
```

Hoy contiene exactamente:

```text
automatizacion_control, capacidades, contacto, infraestructuras, inicio,
proyectos_experiencia, sectores, sistemas_energeticos, sobre_bafras
```

**A/P.** El alcance B1.1 es todo ese catálogo del idioma solicitado, sin carga de
subconjuntos arbitrarios y sin mantener una segunda lista de nueve IDs. Si WEB
añade páginas posteriormente, el conjunto esperado crecerá con su registro.
No se filtra por `url()` o por slug del idioma: una traducción puede inspeccionarse
antes de que WEB habilite sus rutas o su publicación.

**H.** Route contiene parent/slugs; no tiene estado editorial, contenido,
section_id ni disponibilidad del YAML. `SiteRouting.url` (L113) comprueba idioma
publicado y cadena de slugs; `alternates` (L122) reutiliza esa comprobación.
Ninguno verifica el estado por página. La documentación que habla de versiones
realmente publicadas expresa una intención arquitectónica más amplia que el
contrato ejecutable actual. B1.1 no debe certificar publicación usando url().

### D.2. Idiomas e inyección de locale

**H.** `LocaleSettings` (`localization/locales.py:20`) valida unicidad, catálogo y
default publicado. get (L42), codes (L46) y published_codes (L50) son las APIs.
La configuración actual declara es/ca/en/de, default es y solo es publicado.
LanguageCode editorial no comprueba pertenencia al catálogo.

**P.** Mantener la convención de Inicio: ruta global `ProjectPaths.content`,
después `<request.locale>/pages/<page_id>.yaml`; locale omitido en YAML se inyecta
desde la solicitud ya contrastada con LocaleSettings.codes. Si el YAML declara
locale, se acepta solo si coincide exactamente con la solicitud y directorio;
nunca se sobreescribe silenciosamente un valor divergente. Se verifica además
page_id == nombre de archivo esperado. No se recoloca un documento bajo el ID
que declare si su archivo tiene otro nombre.

Idiomas configurados no publicados pueden inspeccionarse. Un idioma desconocido
produce LOCALE_UNKNOWN antes de construir rutas físicas o leer contenido. No
se consulta es como alternativa. Miembros del catálogo, no cadenas aportadas
libremente, determinan los directorios admitidos.

### D.3. Loader YAML y límites demostrados

**H.** `adapters/yaml_files.py:43`: `load_yaml(path: Path) -> Any`.
Lee UTF-8, usa su SafeLoader y rechaza claves duplicadas (L24). Envuelve OSError
y yaml.YAMLError en YamlFileError; este expone path/message y su texto incluye
la ruta recibida. Un archivo ausente produce esa excepción, no None.

Sondas con Path.read_text sustituido solo en memoria, reutilizando load_yaml:

| Entrada | Resultado real |
|---|---|
| Documento vacío | None |
| Raíz secuencia | list |
| Raíz escalar 42 | int |
| Mapping duplicado / sintaxis rota | YamlFileError |
| `value: yes` / fecha sin comillas | bool True / datetime.date |
| Clave YAML secuencia no hashable | TypeError no envuelto |
| Lectura con UTF-8 inválido | UnicodeDecodeError no envuelto |

**P.** Reutilizar sin modificarlo. El límite documental comprueba la forma de
raíz y llama al modelo adecuado. No convierte bool/fechas/números a PublicText.
En la llamada aislada al loader se contienen YamlFileError y esos errores de
entrada conocidos (UnicodeError/TypeError); no se añade un except Exception
global que oculte errores de programación. Discovery/lectura por documento
continúan ante fallos independientes. No se exige en B1.1 un perfil YAML nuevo
de aliases/merges o booleanos: cualquier cambio al parser requiere tarea WEB.

### D.4. Application, propiedad y punto de integración

**H.** `application/configuration.py:40` ofrece una función, no un servicio:
`load_site_routing(paths: ProjectPaths) -> SiteRouting`. Acumula errores de
ambos archivos y usa ConfigurationError.problems (L15). `ProjectPaths.content`
está en `adapters/filesystem.py:32`. No existe un caso de uso editorial de carga.

**A.** architecture.md §8 atribuye application/ y adapters/ a WEB. Las reglas
ejecutables están en `tests/contracts/test_architecture.py:14,24`.

**P/D.** Añadir `application/editorial.py` para la orquestación y
`adapters/editorial_files.py` exclusivamente para discovery acotado del filesystem;
ninguno modifica configuration.py o yaml_files.py. La siguiente tarea debe
autorizar expresamente esos nuevos archivos de propiedad WEB. No se elude
esa coordinación llevando Path/I/O a editorial/ o creando otro paquete.

## E. Políticas de completitud

### E.1. Definiciones definitivas propuestas

- **Esperado:** página registrada para el alcance completo, o catálogo requerido
  por una relación tipada; distinto de lo encontrado por glob.
- **Presente:** existe el origen persistido; no implica que sea archivo regular,
  legible, YAML válido o conforme a su modelo.
- **Válido:** cumple contrato documental local, Pydantic, identidad archivo/locale
  y unicidad de la raíz de catálogo; no implica referencias resueltas.
- **Inválido:** documento presente que falla esas condiciones. Nunca se omite.
- **Ausente:** no existe el origen esperado en el inventario de esta ejecución.
- **Completo documentalmente:** todas las páginas del registro y los catálogos
  requeridos tienen documento válido. No cambia entre políticas.
- **Aprobado:** estado declarado de revisión; independiente de completitud.
- **Publicable:** decisión WEB posterior; B1.1 no calcula este atributo.

**INCREMENTAL:** ausencias obligatorias = warning; conserva inventario de todo el
catálogo y continúa. **COMPLETE:** las mismas ausencias = error; continúa para
acumular problemas. Documentos presentes inválidos, adicionales desconocidos y
referencias definitivamente erróneas = error en ambos modos. No se interrumpe
al primer fallo editorial. Solo falla el contexto global si la configuración WEB
no puede cargarse (ConfigurationError existente).

Una fuente descubierta que desaparece antes de la lectura produce error de
lectura sobre ese inventario, no contenido inventado. No se promete snapshot
atómico del filesystem; debe repetirse la inspección si hay edición concurrente.

### E.2. Persistencia mínima: propuesta, no estructura existente

La necesidad se ha derivado de C y F. Se recomienda un documento por catálogo
homogéneo para localizar errores sin invalidar entidades de otros tipos:

| Origen propuesto bajo `content/<locale>/` | Raíz / validación | Cuándo es obligatorio |
|---|---|---|
| `pages/<page_id>.yaml` | Mapping -> PageContent; inyectar locale | Todas las identidades WEB |
| `common.yaml` | Mapping -> CommonContent | Cuando hay SharedActionRef |
| `entities/people.yaml` | Secuencia -> TypeAdapter(list[Person]), strict | Cuando hay person_refs |
| `entities/sectors.yaml` | Secuencia -> TypeAdapter(list[Sector]), strict | Cuando hay sector_refs o DownloadableResource.sector_id |
| `entities/experiences.yaml` | Secuencia -> TypeAdapter(list[Experience]), strict | Cuando hay experience_ref/experience_refs |
| `entities/resources.yaml` | Secuencia -> TypeAdapter(list[DownloadableResource]), strict | Cuando hay ResourceLink/catalog_refs |

**D.** Ratificar nombres y raíces de esta tabla en B1.1. No son hechos ni formatos
aprobados previamente. La raíz secuencia evita cuatro wrappers Pydantic nuevos.
La unicidad de IDs de esas secuencias debe comprobarse al construir sus índices:
TypeAdapter(list[T]) no detecta duplicados entre entidades distintas. Es una
garantía de raíz nueva, no repetición de validadores internos del modelo.
Si hay duplicados se invalida el documento; no se selecciona la primera entidad.

Discovery solo en la raíz del locale, pages/ y entities/, con contratos de nombre
explícitos; no busca documentos recursivamente por todo content/. Todo documento
YAML encontrado fuera de los nombres contratados en ese alcance se informa como
DOCUMENT_UNEXPECTED; .yml no se trata como alias silencioso de .yaml. No se
recorre un enlace simbólico que escape del content_root del idioma.

Todos los documentos conocidos presentes se validan aunque nadie los referencie.
Las dependencias se obtienen de documentos válidos, incluyendo common/entidades
presentes; por tanto un catálogo puede requerir otro. Se usa un conjunto finito
de tipos/documentos para calcular esa necesidad, sin recursión de contenido.
Una ausencia no requerida se registra, pero no genera un archivo ni warning.
Catálogo válido vacío con referencia a un ID produce referencia UNRESOLVED.
Una página inválida no permite descubrir de forma fiable sus dependencias;
ya impide declarar completo el conjunto.

No es requisito B1.1 crear content/schema.yaml ni migrar datos. Los modelos
actuales no tienen ese campo; su ubicación/versionado se difiere a acuerdo WEB
sin duplicar config/site.yaml. Tampoco se crean otros idiomas ficticios.

### E.3. Matriz de comportamiento

En todas las filas se continúa inspeccionando. «Bundle» significa la operación
controlada de G.4, no la posibilidad técnica de llamar al constructor A1.
Los casos de nueve páginas suponen satisfechas las otras dependencias indicadas.

| Escenario | Clasificación / código | INCREMENTAL | COMPLETE | Bundle controlado / completitud |
|---|---|---|---|---|
| Solo Inicio válido | 1 válida, 8 ausentes; DOCUMENT_MISSING | 8 warnings | 8 errores | No; incompleto |
| Dos páginas válidas | 2 válidas, 7 ausentes | 7 warnings | 7 errores | No; incompleto |
| Nueve válidas + catálogos requeridos válidos + referencias resueltas | Inventario completo | Sin errores documentales | Igual | Sí; completo, incluso draft |
| Página esperada ausente | ABSENT / DOCUMENT_MISSING | warning | error | No; incompleto |
| Página presente inválida | INVALID / DOCUMENT_INVALID o YAML_ERROR | error | error | No; incompleto |
| Adicional desconocida | INVALID/unexpected / DOCUMENT_UNEXPECTED | error | error | No; las nueve pueden estar completas, pero existe error adicional |
| Catálogo requerido ausente | ABSENT / DOCUMENT_MISSING; referencias no verificables | warning | error | No; incompleto |
| Catálogo no requerido ausente | Ausencia opcional registrada | Sin diagnóstico | Igual | No afecta |
| Catálogo opcional presente inválido | INVALID | error | error | No; no afecta cobertura obligatoria, sí validez de inspección |
| Página destino configurada sin YAML | UNVERIFIABLE / REFERENCE_TARGET_UNAVAILABLE | warning | warning + ausencia error | No; incompleto |
| Página destino desconocida | UNRESOLVED / REFERENCE_UNKNOWN | error | error | No; error de integridad aunque inventario esté completo |
| Sección inexistente en página válida disponible | UNRESOLVED / REFERENCE_SECTION_UNKNOWN | error | error | No; inventario puede estar completo |
| Sección de página ausente/inválida | UNVERIFIABLE / REFERENCE_TARGET_UNAVAILABLE | warning | warning; ausencia/invalidez ya tiene su severidad | No; no inventar sección inexistente |
| Catálogo válido sin entidad referida | UNRESOLVED / REFERENCE_UNKNOWN | error | error | No; documentos pueden estar completos |
| Selector de pendiente inválido | PENDING_SELECTOR_INVALID | error | error | No; documentos pueden estar completos |
| approved con pendientes técnicos válidos | EDITORIAL_PENDING | info | info | Sí si lo demás íntegro; no acredita publicación |
| Completo con SEO None y pendiente válido | EDITORIAL_PENDING | info | info | Sí si lo demás íntegro; no acredita publicación |
| Completo, todo draft | Estado declarado | No error por draft | Igual | Sí; aprobación no requerida para inspección/bundle |

Fotografía de hoy: Inicio válido, ocho páginas ausentes, catorce enlaces a esas
páginas configuradas pero sin contenido y ocho pendientes legítimos. INCREMENTAL
deberá conservar Inicio y reportar todo lo anterior; no entregar un bundle íntegro.
No hay catálogos requeridos por referencias de Inicio. No se transforma cada
destino sin contenido en «página desconocida».

## F. Referencias transversales

### F.1. Clasificación mínima suficiente

**P.** RESOLVED: identidad editorial única y destino accesible en documento válido.
UNRESOLVED: evidencia suficiente de destino incorrecto/inexistente/incompatible.
UNVERIFIABLE: documento esperado no disponible o inválido, o comprobación externa
que B1 no posee. Se distingue el motivo mediante código y target_document_id;
no hace falta un cuarto estado ni una excepción por cada variante.

No se confunde «resuelto» con publicado. Un enlace hacia una página draft
disponible puede estar RESOLVED. Una ruta configurada sin YAML no lo está.

### F.2. Matriz tipada de resolución

| Variante / origen real | Destino y autoridad | Resolución B1.1 / ausencia / error |
|---|---|---|
| InternalLink sin section_id en cualquier acción o discipline | page_id; registro WEB + PageContent disponible | Desconocido en WEB: UNRESOLVED; conocido pero YAML ausente/inválido: UNVERIFIABLE; válido: RESOLVED |
| InternalLink con section_id | page_id y sections[].id | Mismas reglas de página; solo buscar sección si la página es válida; ausencia entonces UNRESOLVED |
| SharedActionRef en listas Action | common_ref -> CommonContent.actions[].id | common ausente/inválido: UNVERIFIABLE; ID ausente en common válido: UNRESOLVED; presente: RESOLVED, y se valida el target de esa acción |
| ExternalLink | URL HTTP/HTTPS | Forma validada por Pydantic; identidad simbólica RESOLVED para B1; no se comprueba red, accesibilidad o permisos |
| ContactLink y TextSection.contact_channels | email/phone; valores reales propiedad WEB | Canal tipado válido; valores/operatividad externa UNVERIFIABLE con EXTERNAL_CONTACT_UNCHECKED, no error de identidad editorial |
| ResourceLink en acción o Sector.catalog_refs | catalog_id -> DownloadableResource | resources ausente/inválido: UNVERIFIABLE; ID ausente: UNRESOLVED; presente: RESOLVED solo identidad editorial |
| SectorIndexSection.sector_refs | Sector.id; seis IDs canónicos de entities.py:15 | ID fuera de SectorId: UNRESOLVED aunque falte catálogo; ID canónico con catálogo ausente/inválido: UNVERIFIABLE; catálogo válido decide existencia |
| TeamSection.person_refs / Experience.person_refs | Person.id | Catálogo ausente/inválido: UNVERIFIABLE; válido sin ID: UNRESOLVED; con ID: RESOLVED |
| ExperienceGroup.entries[].experience_ref / Person.experience_refs | Experience.id | Misma regla de catálogo; verificar borradores también |
| DownloadableResource.sector_id | Sector.id | Forma canónica ya validada por Pydantic; comprobar presencia de la entidad sectorial |
| Sector.catalog_refs vs DownloadableResource.sector_id | Pertenencia al mismo sector | Ambos destinos válidos pero sector distinto: RESOURCE_SECTOR_MISMATCH, error |
| DocumentedResult.evidence_refs / Verification.evidence_refs / SourceRef | Cadenas documentales; no registro de evidencias implementado | No tratarlas como IDs ni abrir archivos; EXTERNAL_EVIDENCE_UNCHECKED cuando se informa de evidencias, sin certificar veracidad |
| media/portrait | Actualmente solo None | Sin MediaRef resoluble; conservar metadatos PendingField; fuera de validación de medios B1 |

**P.** La ausencia de datos externos de contacto, PDF o evidencia NO bloquea por
sí sola el bundle editorial: se distingue con códigos EXTERNAL_* y no se incluye
en el cierre de referencias editoriales. La identidad de ResourceLink sí debe
resolverse. El archivo PDF, idioma físico, versión y derechos siguen siendo WEB.

La implementación usa recorridos explícitos por las variantes de B.2, CommonContent
y entidades de B.3. No infiere relaciones por sufijo _id, no recorre arbitrariamente
atributos ni interpreta strings documentales como rutas. Una fuente inválida no
se recorre: REFERENCES_SKIPPED_INVALID_SOURCE, sin cascada de falsos IDs ausentes.

**P.** No se prohíben ciclos de navegación A↔B, persona↔experiencia o
sector↔catálogo: son referencias de identidad, no inclusión recursiva. CommonContent
ya impide acciones compartidas recursivas por su tipo. No se necesita DFS de
ciclos editoriales ni duplicar el control de padres de RouteTable.

### F.3. Reutilización de pendientes A2.1

Evidencia: `pending.py:32` SelectorResolution; L39 PendingDiagnostic;
L85 resolve_pending_selector; L132 validate_pending_fields.

**P.** Para cada PageContent válido, llamar a validate_pending_fields exactamente
como está y adaptar sus fallos a PENDING_SELECTOR_INVALID con page_id, selector,
motivo y fuente. Los ocho pendientes legítimos se informan como EDITORIAL_PENDING
info, no como errores ni como campos automáticamente resueltos.

Person y Experience también tienen pending; CommonContent no tiene ese campo.
La gramática A2.1 está ligada a PageContent y no debe aplicarse a entidades ni
duplicarse. Para pending de entidades se conserva el dato y se emite
ENTITY_PENDING_UNCHECKED warning, sin afirmar resolución. No bloquea el cierre
de identidades de B1 por sí mismo: el alcance del bundle controlado es inventario,
referencias tipadas y selectores de página, no certificación de todo pendiente
de entidad. Una ampliación de ese alcance requiere tarea posterior explícita.

## G. Interfaces definitivas propuestas para B1.1

### G.1. Solicitud y entrada de aplicación

Reutilizar ProjectPaths evita otra raíz ambigua en la solicitud:

```python
# application/editorial.py — propuesta, no implementada
@dataclass(frozen=True)
class EditorialLoadRequest:
    locale: str
    policy: CompletenessPolicy  # Literal['INCREMENTAL', 'COMPLETE']

def inspect_editorial(
    paths: ProjectPaths,
    request: EditorialLoadRequest,
) -> EditorialInspection: ...
```

**P.** content_root es siempre `paths.content`, raíz GLOBAL, nunca content/es.
No se añade otro Path al request. Validar que policy sea uno de los dos valores
al construir/recibir la solicitud; dataclass por sí sola no valida Literal.
La configuración se carga con load_site_routing. ConfigurationError se mantiene
como fallo de prerrequisito WEB; no se interpreta como documento editorial ausente.

LOCALE_UNKNOWN produce inspección con error, expected_page_ids y documentos
vacíos y sin lecturas editoriales. La completitud es falsa en contexto inválido;
no se usa all([]) para declarar completo un resultado sin alcance.

### G.2. Tipos de resultado y diagnóstico

Nuevos contratos puros en `editorial/inspection.py`, sin Path ni imports WEB:

```python
CompletenessPolicy = Literal['INCREMENTAL', 'COMPLETE']
DiagnosticSeverity = Literal['error', 'warning', 'info']
ReferenceStatus = Literal['RESOLVED', 'UNRESOLVED', 'UNVERIFIABLE']
DocumentState = Literal['ABSENT', 'VALID', 'INVALID']
DocumentKind = Literal[
    'page', 'common', 'people', 'sectors', 'experiences', 'resources', 'unexpected'
]
DocumentValue = (
    PageContent | CommonContent | tuple[Person, ...] | tuple[Sector, ...]
    | tuple[Experience, ...] | tuple[DownloadableResource, ...]
)

@dataclass(frozen=True)
class EditorialDiagnostic:
    code: DiagnosticCode
    severity: DiagnosticSeverity
    message: str
    document_id: str | None = None
    source: str | None = None
    selector: str | None = None
    target_id: str | None = None
    target_document_id: str | None = None
    reference_status: ReferenceStatus | None = None
    reason_code: str | None = None

@dataclass(frozen=True)
class EditorialDocument:
    document_id: str
    kind: DocumentKind
    source: str
    required: bool
    state: DocumentState
    value: DocumentValue | None = None

@dataclass(frozen=True)
class EditorialInspection:
    locale: str
    policy: CompletenessPolicy
    expected_page_ids: tuple[str, ...]
    documents: tuple[EditorialDocument, ...]
    diagnostics: tuple[EditorialDiagnostic, ...]
```

Justificación: un registro de documento es necesario para representar ausencia,
presencia inválida y catálogo no requerido sin inventar modelos. Un diagnóstico
sirve para todas las variantes y evita una clase por error. No hace falta otra
clase para resultados de referencia: status/código/origen/destino bastan.

Reglas de construcción: VALID exige valor del tipo asociado a kind; ABSENT/INVALID
exigen value=None; unexpected nunca es VALID ni required. document_id único,
por ejemplo page/inicio, catalog/people, common o unexpected/es/pages/extra.yaml.
source es relativo a content_root: es/pages/inicio.yaml. Estado, required y tipo
se fijan al terminar la inspección, después de calcular dependencias. No se
mantienen contadores mutables paralelos. Los índices de consulta se derivan.

Propiedades derivadas, no campos editables:

- valid_pages: Mapping[str, PageContent], vista de los registros VALID/page.
- missing_page_ids, invalid_page_ids: tuplas ordenadas desde el inventario.
- common: CommonContent | None y catálogos válidos: consultas tipadas a documents.
- documents_complete: contexto válido y todos los documentos requeridos VALID.
- has_errors: existe diagnostic.severity == error.
- can_build_bundle: las condiciones de G.4, no permiso de publicación.

Tuplas y dataclasses frozen dan estabilidad superficial. Los modelos Pydantic
contenidos conservan listas mutables; documentar que son snapshots de lectura.
No se promete inmutabilidad profunda. Mapping de páginas debe devolverse como
vista de solo lectura o copia derivada, no como diccionario mutable autoritativo.

DiagnosticCode mínimo, como Literal o enum cerrado:

```text
LOCALE_UNKNOWN, DOCUMENT_MISSING, DOCUMENT_UNEXPECTED, DOCUMENT_READ_ERROR,
YAML_ERROR, DOCUMENT_ROOT_INVALID, DOCUMENT_INVALID, DOCUMENT_ID_MISMATCH,
DOCUMENT_LOCALE_MISMATCH, DUPLICATE_ENTITY_ID, REFERENCE_RESOLVED,
REFERENCE_UNKNOWN, REFERENCE_SECTION_UNKNOWN, REFERENCE_TARGET_UNAVAILABLE,
RESOURCE_SECTOR_MISMATCH, REFERENCES_SKIPPED_INVALID_SOURCE,
PENDING_SELECTOR_INVALID, EDITORIAL_PENDING, ENTITY_PENDING_UNCHECKED,
EXTERNAL_CONTACT_UNCHECKED, EXTERNAL_RESOURCE_UNCHECKED, EXTERNAL_EVIDENCE_UNCHECKED
```

REFERENCE_RESOLVED es info y permite consultar los resultados por origen; si se
emite una vez para una acción común, sus usos SharedActionRef conservan su propio
resultado de identidad. Los diagnósticos son deterministas, no logs de eventos.

**P.** Identidad estable del diagnóstico: tupla
(code, document_id, selector, target_document_id, target_id, reason_code).
No depende de message, hora, ruta absoluta ni orden de discovery. Duplicados con
esa misma identidad se eliminan. Orden final por source/document_id/selector/code/
target_document_id/target_id/reason_code, usando cadena vacía para None; el orden
de contenido nunca se ordena para satisfacer diagnósticos.

Ubicación Pydantic: conservar loc como selector de campo con sus posiciones de
error si las hay; esas posiciones son ubicaciones de diagnóstico, no selectores
PendingField. No pasarlas al resolver de A2.1. Los selectores de relaciones usan
IDs estables al recorrer objetos válidos.

No volcar str(YamlFileError), ValidationError, input ni ctx completos: pueden
incluir rutas absolutas o contenido innecesario. Producir mensajes acotados desde
código, tipo de error y campo. Para YAML, no extraer líneas parseando cadenas
localizadas; el contrato público actual no ofrece una ubicación estructurada
uniforme. Línea/columna quedan fuera del mínimo B1.1, sin perder archivo/campo.

### G.3. Orquestación mínima y separación de I/O

`adapters/editorial_files.py` propone una función de discovery sobre las carpetas
fijas del locale: devuelve orígenes existentes ordenados y errores de acceso,
comprueba contención y archivos regulares. No valida Pydantic ni importa
application. No necesita clase de repositorio o servicio. La lectura sigue siendo
load_yaml; el nuevo módulo no incluye parser.

`application/editorial.py` obtiene contexto WEB, deriva las rutas esperadas,
compara discovery, llama al loader/modelos por documento, valida raíz/identidad
y ensambla el inventario. Un archivo inválido no impide cargar los otros.
No se captura un error de configuración para sustituirla por listas vacías.

`editorial/integrity.py` recibe inventario tipado y expected_page_ids en valores
simples. Construye índices sin ambigüedad, calcula catálogos requeridos, recorre
las relaciones explícitas de F, reutiliza pendientes A2.1 y devuelve resultados
de integridad mediante diagnósticos. No conoce rutas físicas o LocaleSettings.
No lee Markdown maestro en producción.

### G.4. Construcción explícita del bundle

```python
# editorial/integrity.py — propuesta
def build_editorial_bundle(inspection: EditorialInspection) -> EditorialBundle: ...
```

Precondiciones acumulativas, idénticas para las dos políticas:

1. Contexto de idioma/alcance válido y al menos una página esperada.
2. documents_complete verdadero: páginas y catálogos requeridos válidos.
3. Ningún error, incluidos documentos adicionales o catálogos opcionales inválidos.
4. Ninguna referencia EDITORIAL UNRESOLVED/UNVERIFIABLE ni selector de página
   inválido. EXTERNAL_* y ENTITY_PENDING_UNCHECKED tienen el alcance limitado de F.

Si no se cumplen, lanzar ValueError con mensaje estable indicando que la
inspección no permite construir el bundle; los detalles ya están en diagnostics.
No devolver un bundle parcial ni None con significado ambiguo. No hace falta una
jerarquía nueva de excepciones. B1.1 puede comprobar can_build_bundle antes.

Si se cumplen, usar los modelos válidos y defaults legítimos del constructor
actual. Ese constructor conserva su validación defensiva; no se modifica A1.
Un resultado INCREMENTAL que ya esté completo puede construir bundle: el modo
solo cambia severidad de ausencias, no el requisito de integridad.

Esta operación garantiza el alcance B1 (inventario, referencias editoriales y
selectores de página), no publicación, derechos, revisión humana, ni verificación
de toda evidencia o pendiente de entidad. El modelo devuelto no contiene un
campo publicable, y su existencia sigue sin constituir autorización.

### G.5. Dependencias

```text
application/editorial -> application/configuration -> site/routes -> localization/locales
application/editorial -> adapters/editorial_files + adapters/yaml_files + ProjectPaths
application/editorial -> editorial/inspection + editorial/integrity
editorial/integrity -> editorial/inspection + modelos + editorial/pending
editorial/pending -> modelos editoriales existentes
adapters/editorial_files -> biblioteca estándar (filesystem)
```

Prohibido: editorial -> application/adapters/site/localization/templates/YAML/
filesystem; adapters -> application/CLI; site -> application; cualquier ciclo
de capas. Se conservan las pruebas de arquitectura actuales. Las nuevas funciones
son necesarias por inventario/contexto y reglas entre documentos, no para
anticipar caches, publicación, CMS o motores de estudios.

## H. Matriz ejecutable de pruebas B1.1

U=unitaria; I=integración; C=contrato. Fixtures sintéticos pequeños y claramente
no publicables, o Inicio real para aceptación; ningún test exige migrar copy real
de las ocho páginas. «Nueve mínimas» significa nueve documentos válidos de prueba,
no páginas ficticias persistidas en content/.

| Caso | Nivel / fixture mínimo | Expectativa | Riesgo |
|---|---|---|---|
| Solo Inicio incremental | I / Inicio real + config actual | 1 válida, 8 ausentes warning; enlaces UNVERIFIABLE; sin bundle | Parcial presentado como completo |
| Solo Inicio complete | I / mismo fixture | Mismas colecciones; ausencias error | Modo estricto ignorado |
| Dos páginas | I / dos YAML mínimos | Siete ausencias; ambas válidas conservadas | Descartar documentos válidos |
| YAML roto y duplicado | I / un YAML malo + otro válido | YAML_ERROR por origen; continuar | Fail-fast o duplicados silenciosos |
| Raíz vacía/escalar/lista en página | I / tres variantes | DOCUMENT_ROOT_INVALID | Confundir None con ausencia |
| page_id incorrecto | I / archivo inicio con otro id | DOCUMENT_ID_MISMATCH; no reindexar | Suplantar archivo esperado |
| Locale divergente en YAML | I / locale en != solicitud es | DOCUMENT_LOCALE_MISMATCH | Sobrescribir datos silenciosamente |
| Locale desconocido | I / request zz o traversal | LOCALE_UNKNOWN; sin lecturas | Fallback o escape de raíz |
| Locale en configurado no publicado | I / carpeta en ausente | Nueve ausencias en en, sin leer es | Confundir habilitación y edición |
| Documento extra | I / extra.yaml y opcional .yml | DOCUMENT_UNEXPECTED; error en ambos modos | Ignorar contenido desconocido |
| Presente inválido | I / campos desconocidos/tipos erróneos | INVALID; no omitir | Tolerancia incremental excesiva |
| Errores independientes | I / dos archivos malos + Inicio | Dos grupos diagnósticos y Inicio válido | Cascadas o aborto global |
| UTF-8 malo / clave no hashable | I / archivos temporales | Error documental contenido; resto continúa | Excepciones no cubiertas del loader |
| Origen desaparece / directorio .yaml / symlink escape | I / filesystem temporal | Error de lectura/contrato; no leer fuera del locale | Inventario inconsistente |
| Referencia a página válida | U / dos PageContent mínimos | RESOLVED sin exigir approved | Confundir existencia con revisión |
| Página desconocida | U / target fuera del registro | UNRESOLVED + error | Clasificación demasiado permisiva |
| Página configurada sin YAML | I / registro y archivo ausente | UNVERIFIABLE, no REFERENCE_UNKNOWN | Falso destino inexistente |
| Página configurada inválida | I / target YAML roto | UNVERIFIABLE + error raíz, sin cascada de secciones | Diagnósticos engañosos |
| Sección existente/inexistente | U / target PageContent válido | RESOLVED / REFERENCE_SECTION_UNKNOWN | Comprobar solo página |
| Enlaces recíprocos | U / A↔B | Ambos resueltos, sin error de ciclo | DFS indebido |
| Cada ubicación de B.2 | U / un caso por lugar de acción/ref | Se encuentra la referencia exacta con selector por ID | Walker incompleto |
| Catálogo requerido ausente | I / Team con person_refs, sin catálogo | Requerido; ausencia + UNVERIFIABLE | Inventar personas |
| Catálogo válido sin entidad | I / lista con otra persona | REFERENCE_UNKNOWN | Confundir catálogo con entidad |
| Catálogo presente no requerido inválido | I / resources roto sin referencias | Error; no ocultar archivo presente | Ignorar errores opcionales |
| Catálogo no requerido ausente | I / Inicio sin refs de entidad | Ausencia opcional no bloquea por sí misma | Exigir archivos vacíos |
| IDs duplicados en catálogo | I / dos personas con mismo id | Documento inválido; no elegir primera | Índices ambiguos |
| SharedActionRef inexistente | U/I / common válido sin acción | UNRESOLVED; common ausente sería UNVERIFIABLE | Recursión/duplicación de CTA |
| Catálogo-sector incompatible | U / dos sectores y recurso | RESOURCE_SECTOR_MISMATCH | Relaciones incoherentes |
| Persona↔experiencia, sector↔catálogo | U / identidades recíprocas | Relaciones válidas, sin falso ciclo | Confundir identidad e inclusión |
| Resultado con evidencia | U / DocumentedResult existente | Forma Pydantic reutilizada; sin leer evidencia | Certificación ficticia |
| Pendiente página inválido | U / selector A2.1 erróneo | Adaptar PendingDiagnostic; error | Duplicar gramática |
| Ocho pendientes reales | I / Inicio real | Ocho info y cero errores de selector | Resolver valor implica aprobar |
| Pendiente entidad | U / Person.pending no vacío | ENTITY_PENDING_UNCHECKED; conservarlo | Aplicar gramática equivocada |
| Draft válido / approved con pendientes | U/I / ambas variantes | Validez/completitud independientes de revisión | Estado igual a publicación |
| Nueve completas con SEO pendiente | I / nueve mínimas | Bundle B1 construible si refs íntegras; no publicable calculado | Confundir completo con release |
| Construcción prematura | U / inspección con ausentes/error | ValueError estable, nunca bundle parcial | Usar bundle no-None como éxito |
| Dos inspecciones equivalentes | I / mismo árbol | Inventario/diagnósticos iguales | Dependencia de hora/azar |
| Orden de discovery distinto | U/I / fuentes permutadas | Diagnósticos y mapas iguales; orden editorial conservado | Orden accidental |
| Temporales diferentes | I / mismo fixture bajo raíces distintas | source relativo, sin rutas absolutas en message | Dependencia del equipo local |
| Duplicación de diagnóstico | U / mismo uso recolectado dos veces | Identidad deduplicada; otros selectores conservados | Contadores inflados |
| Reutilización loader | C / spy de load_yaml | Todas las lecturas YAML pasan por esa función | Segundo parser |
| Arquitectura | C / tests existentes + nuevos módulos | Sin imports prohibidos, D03 ni HTML en producción | Acoplamiento circular |
| Regresión | C/I / suite A1/A2/A2.1 intacta | 292 previas siguen pasando + casos B1 | Romper contratos previos |

No se implementó ninguno de estos tests durante B1.0.

## I. Riesgos y decisiones pendientes

| Prioridad | Hallazgo / evidencia | Resolución mínima |
|---|---|---|
| P0, condición de arranque | application/adapters son WEB (architecture.md §8) | Autorizar los dos archivos nuevos exactos en la tarea B1.1; sin modificar archivos WEB existentes |
| P0, decisión de contrato | No hay formatos de catálogo persistidos | Ratificar E.2: nombres, raíces secuencia y obligatoriedad por dependencias |
| P1 | Bundle parcial permitido (`pages.py:43`) | Reutilizar intacto y añadir inspección/constructor controlado |
| P1 | Loader permite raíces diferentes y propaga dos errores de entrada | Contención acotada por documento y tests; no otro parser |
| P1 | Clasificación missing/invalid/unknown ausente hoy | Inventario único por documento y políticas E; acumular errores |
| P1 | Fuente de locale actualmente inyectada solo por tests | Contexto validado, inyección sin sobrescribir discrepancias |
| P1 | SiteRouting no acredita publicación real por página | Usar solo identidades/contexto; disponibilidad desde inventario |
| P1 | Diagnósticos actuales no son generales ni uniformes | Contrato único propuesto; adaptar A2.1 sin reemplazarlo |
| P1 | Catálogo-lista necesita unicidad de raíz | Índices explícitos que invalidan ambigüedad |
| P1 | Archivos A1/A2/A2.1 sin seguimiento | Comparar baseline de contenido, no solo git diff; no consolidar sin autorización |
| P2 | frozen superficial | Snapshot de lectura, tuplas externas; no deep-freeze/caché |
| P2 | architecture.md aún llama vacío al dominio | Anotación documental obsoleta; código real prevalece; tarea documental posterior |
| P2 | Pendientes de entidades fuera del resolver | Informar limitación con alcance explícito; no ampliar A2.1 en B1 |
| P2 | Versión global de contenido no definida | Acordar fuera del mínimo B1; no crear dos declaraciones |
| Fuera de alcance | MediaRef, derechos/PDF, contacto operativo | WEB; no bloquear la carga textual inventando contratos |
| Fuera de alcance | Traducción, huellas, release, CLI y HTML | Fases propias; no anticiparlas en infraestructura B1 |

Simplificación aplicada: sin registro alternativo de páginas/idiomas; sin service
class, repositorio abstracto, plugins de documentos, parser nuevo, snapshots
históricos, motor de consultas o detección de ciclos de navegación. No se
duplican modelos de página, garantías Pydantic ni políticas de publicación.

## J. Plan mínimo B1.1

1. Ratificar condiciones de K y permisos de propiedad. Registrar baseline de
   A1/A2/A2.1 sin reset/stash/commits automáticos.
2. Añadir `editorial/inspection.py`: contratos de inventario/diagnóstico y
   propiedades derivadas; tests unitarios de estados coherentes/determinismo.
3. Añadir `adapters/editorial_files.py`: discovery acotado; reutilizar load_yaml
   sin modificar yaml_files.py ni filesystem.py.
4. Añadir `application/editorial.py`: función inspect_editorial y request;
   usar load_site_routing/ProjectPaths; validar por documento; sin CLI.
5. Añadir `editorial/integrity.py`: recorrido tipado, índices, catálogos requeridos,
   referencias, pendientes existentes y build_editorial_bundle con precondiciones.
6. Implementar la matriz H en pruebas propias unit/integration/contracts, con
   fixtures temporales. Verificar Inicio real sin editarlo ni migrar otras páginas.
7. Ejecutar suite previa y nueva; revisar diffs/hashes de archivos propietarios;
   entregar informe B1.1 con inventario, diagnósticos y limitaciones externas.

No cambiar A1/A2/A2.1 salvo defecto demostrado. No crear documentos persistidos
de entidades para ejecutar infraestructura: los tests usan fixtures temporales.
No añadir dependencias o modificar site/media/localization/config/templates/CLI.
La creación de common/catálogos reales corresponde a la migración editorial.

## K. Dictamen final

**GO CON CONDICIONES.** Los modelos y contratos WEB existentes son suficientes
para implementar carga incremental e integridad editorial sin refactorizar A1.
El baseline actual de datos no es completo: solo Inicio puede validarse hoy.

Condiciones concretas que debe incorporar la autorización de B1.1:

- **C1:** permitir los nuevos `application/editorial.py` y
  `adapters/editorial_files.py`, sujetos a propiedad WEB; sin tocar los existentes.
- **C2:** aceptar la persistencia y política E.2 (catálogos condicionales, raíces
  secuencia) y el alcance de todo el registro de páginas del idioma.
- **C3:** aceptar que bundle controlado significa integridad dentro del alcance
  B1; no publicación ni verificación de evidencias/medios/pendientes de entidades.

No hay una incompatibilidad que requiera cambiar de stack o endurecer el
constructor de EditorialBundle. Si no se autorizan C1/C2, no debe improvisarse
otra capa de I/O ni un formato distinto durante la implementación.

B1.0 se detiene en este informe. B1.1 no se ha iniciado.

### Verificación de cierre

Rama y HEAD finales coinciden con el inicio. La comparación SHA-256 de los
105 archivos preexistentes inspeccionados no detecta modificaciones ni bajas.
La única alta es `docs/project_v02/CONTENT_ES_01_B1_0.md`; el estado Git previo
se conserva íntegro y solo añade ese informe sin seguimiento. No se observaron
cambios concurrentes ajenos ni se realizaron commits, push u operaciones de
reescritura del repositorio. La suite no se reejecutó: se verificó su colección
de 292 casos y se conservó la evidencia de aprobación previa de A2.1.
