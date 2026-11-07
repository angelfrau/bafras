# CONTENT-ES-01 / A1 — Dominio editorial

Fecha: 05/11/2026. Implementación de dominio y contratos de prueba; no migración de contenido.

## A. Baseline y decisiones vigentes

- Raíz Git: `bafras/`; rama `feat/contingut-v2`.
- HEAD inicial: `fca65e8ba7d75317be150e3f428be67d87825d34`; árbol inicialmente limpio.
- WEB-G2-00 tiene sus dos commits locales: `762e196` (retirada del legacy) y
  `fca65e8` (arquitectura, idiomas y rutas).
- DEC-14 implementada en `config/locales.yaml` y `localization/locales.py`:
  fuente/default ES; ES/CA/EN/DE previstos; solo ES publicado; sin fallback.
- DEC-16 implementada en `config/routes.yaml` y `site/routes.py`: ES sin prefijo;
  CA/EN/DE con prefijo al publicarse. No se añaden rutas desde CONTENT.
- Los IDs WEB reales son `inicio`, `capacidades`, `infraestructuras`,
  `sistemas_energeticos`, `automatizacion_control`, `sectores`,
  `proyectos_experiencia`, `sobre_bafras`, `contacto`.
  Sustituyen los IDs ingleses propuestos en la auditoría de Fase 1.

Fuentes: D03 V1.22 y adendas 03.K, 03.K.2, 03.SEC.CAT-01/02,
03.CO-02, 03.G1-01/02; D04 V2.4; D05 V4.12 §48; nueve ZIP de maquetas
en `maquetas_aprobadas/`; `docs/architecture.md`; auditoría Fase 1 A–M
entregada en la conversación. Las maquetas no autorizan copy adicional.

## B. Arquitectura implementada

Solo `src/bafras_web/editorial/` contiene código de producción nuevo.

| Módulo | Contratos |
|---|---|
| `primitives.py` | Base estricta y frozen, IDs, texto conservado, párrafos, elementos, revisión, pendientes y evidencia de verificación/autorización |
| `references.py` | Destinos internos/externos/contacto/recurso; unión discriminada; acciones locales o compartidas excluyentes |
| `sections.py` | Nueve familias de sección; cinco tipos de tarjeta; necesidades y entregables diferenciados; principios/pasos; grupos de experiencia; campos y mensajes de formulario |
| `entities.py` | Personas, seis sectores canónicos, experiencias previas/proyectos BAFRAS, resultados documentados e identidad editorial de catálogo |
| `pages.py` | SEO editorial, página, contenido común y bundle de un idioma con acceso por identidad |
| `__init__.py` | API pública del dominio |

Todas las clases heredan configuración única `extra='forbid'`, `strict=True`,
`frozen=True`, `validate_default=True`. Las listas conservan el orden de entrada.
`frozen` impide reasignar campos, pero no hace profundamente inmutables las listas:
el consumidor debe reconstruir y validar el documento editado, no mutar un modelo.
No se prometen objetos hashables ni una caché.

Invariantes locales: texto no vacío ni marcador `[PENDIENTE]`; IDs únicos por
colección; un hero por página; contenido de sección no vacío; propósitos de
tarjetas/listas compatibles; referencias de disciplinas internas; catálogos sin
duplicar; páginas/catálogos únicos en bundle; locale coherente dentro del bundle.
Una aprobación editorial no concede autorización. Afirmar verificación o
autorización requiere una referencia de evidencia. Un resultado requiere respaldo.
El dominio exige la referencia, no certifica la veracidad del documento citado.

No se fijan universalmente las cantidades actuales de D03. Las cantidades
3/4/5/6 y el orden de los 51 bloques se verifican en aceptación independiente.
No se implementan existencia de referencias, permisos de release ni membresía
en el registro WEB: son validación transversal/integración posterior.

Dependencias: biblioteca estándar y Pydantic; imports internos únicamente dentro
de `editorial/`. Sin filesystem, YAML, Jinja2, templates, rutas, HTML ni servicios.

## C. Archivos y alcance

Nuevos: los cinco módulos de dominio anteriores; `tests/unit/editorial/conftest.py`,
`test_domain.py`, `test_d03_contract.py`; este informe.
Modificado: únicamente `editorial/__init__.py`, para exportar la API pública.

No se modifican módulos WEB, configuración, dependencias, manifiestos, pruebas
WEB ni documentos maestros. No se crean YAML editoriales, traducciones,
adaptadores, comandos CLI, huellas, vistas o generador HTML.

## D. Matriz verificable de los 51 bloques

La matriz ejecutable está en `tests/unit/editorial/test_d03_contract.py`.
Su inventario se compara con los 51 encabezados reales de D03 y comprueba
campos tipados poblados y serialización/reconstrucción de cada bloque.

Abreviaturas de modelos: H=HeroSection; T=TextSection; C=CardsSection;
L=ItemListSection; P=ProcessSection; S=SectorIndexSection;
E=ExperienceIndexSection; G=TeamSection; F=ContactFormSection.
Cada letra corresponde a un discriminador único: hero/text/cards/item_list/
process/sector_index/experience_index/team/form.

Estado R: estructura editorial representada y probada. Estado R/M: lo mismo,
con medio pendiente. No significa aprobación, publicación ni migración literal.

| Página WEB | D03 | Modelo | Ubicaciones tipadas y particularidades | Estado / límite |
|---|---|---|---|---|
| inicio | H01 | H | eyebrow, title, subtitle, paragraphs, actions | R/M: hero media |
| inicio | H02 | C | capabilities; 3 items con paragraphs/examples/actions; acción global | R/M: fotos de tarjetas |
| inicio | H03 | L | needs; introduction; 4 items con paragraphs/actions y destinos distintos | R/M: figura contextual |
| inicio | H04 | P | workflow; introduction; 4 items; closing; actions | R |
| inicio | H05 | C | sector_preview; introduction; 4 títulos; acción única | R; etiquetas DEC-15 pendientes |
| inicio | H06 | T | title, paragraphs, actions | R; no copiar panel adicional de maqueta |
| inicio | H07 | T | title, paragraphs, actions, notes para microcopy | R |
| capacidades | C01 | H | eyebrow, title, paragraphs, actions con sección destino | R |
| capacidades | C02 | C | capabilities; 3 items con 4 examples cada uno y actions | R; sin variantes de layout |
| capacidades | C03 | C | application_examples; eyebrow; 3 descriptions y disciplines | R; ejemplos hipotéticos |
| capacidades | C04 | L | modalities; introduction; 4 delivery items | R; no cronología |
| capacidades | C05 | T | title, paragraphs, 2 actions | R |
| infraestructuras | INF-01 | H | eyebrow, title, subtitle, paragraphs, actions | R/M: hero media |
| infraestructuras | INF-02 | L | needs; introduction; 5 items | R |
| infraestructuras | INF-03 | C | technical_areas; 4 items; transversal con título/párrafos | R; códigos y exclusiones internos fuera del copy |
| infraestructuras | INF-04 | L | deliverables; introduction; 4 items; notes de alcance | R |
| infraestructuras | INF-05 | T | title, paragraphs, 2 actions | R |
| infraestructuras | INF-06 | T | title, paragraphs, actions | R |
| infraestructuras | INF-07 | T | title, paragraphs, actions | R |
| sistemas_energeticos | ENE-01 | H | eyebrow, title, paragraphs principal/apoyo, actions | R/M: hero media |
| sistemas_energeticos | ENE-02 | L | needs; introduction; 6 items | R |
| sistemas_energeticos | ENE-03 | C | technical_areas; 6 items/included; transversal hídrica separada | R/M: imagen de sección |
| sistemas_energeticos | ENE-04 | L | deliverables; 4 items; notes de criterio | R |
| sistemas_energeticos | ENE-05 | T | title, paragraphs, 2 actions | R |
| sistemas_energeticos | ENE-06 | T | title, paragraphs, actions | R |
| sistemas_energeticos | ENE-07 | T | title, paragraphs, actions | R |
| automatizacion_control | DIG-W01 | H | eyebrow, title, paragraphs principal/apoyo, actions | R/M: hero media |
| automatizacion_control | DIG-W02 | L | needs; introduction; 5 items | R |
| automatizacion_control | DIG-W03 | C | technical_areas; 6 items/tags; transversal | R/M: imagen de sección |
| automatizacion_control | DIG-W04 | L | deliverables; 4 items; notes | R |
| automatizacion_control | DIG-W05 | C | discipline_relations; 2 descriptions/discipline; closing | R |
| automatizacion_control | DIG-W06 | T | title, paragraphs, actions | R |
| automatizacion_control | DIG-W07 | T | title, paragraphs, actions | R |
| sectores | SEC-01 | H | eyebrow, title, paragraphs, actions | R |
| sectores | SEC-02 | S | introduction; 6 sector_refs → description/examples/contextual_actions/catalog_refs | R; cero catálogos reales |
| sectores | SEC-03 | T | title, paragraphs, actions | R |
| sectores | SEC-04 | T | title, paragraphs, actions | R |
| sectores | SEC-05 | T | title, paragraphs, actions | R |
| proyectos_experiencia | PE-01 | H | eyebrow, title, paragraphs, attribution | R |
| proyectos_experiencia | PE-02 | E | 3 groups/introduction; entries con experience_ref y énfasis; 6 entidades borrador | R; medios y fichas futuras pendientes |
| proyectos_experiencia | PE-03 | T | title, paragraphs | R |
| proyectos_experiencia | PE-04 | T | title, paragraphs, 2 actions | R |
| sobre_bafras | SB-01 | H | eyebrow, title, paragraphs, actions | R |
| sobre_bafras | SB-02 | G | introduction, corporate_presentation íntegra de 03.K, 3 person_refs | R; portrait pendiente de MediaRef |
| sobre_bafras | SB-03 | P | principles; introduction; 4 items; closing | R |
| sobre_bafras | SB-04 | T | 2 paragraphs identificados, title, actions | R |
| sobre_bafras | SB-05 | T | title, paragraphs, 2 actions | R |
| contacto | CO-01 | H | eyebrow, title, paragraphs | R; introducción V1.1 vigente |
| contacto | CO-02 | F | fields (4), help por campo, submit_label, messages, privacy_text | R; privacidad pendiente explícita |
| contacto | CO-03 | T | title, paragraphs, contact_channels con etiqueta y canal | R; valores reales en WEB |
| contacto | CO-04 | T | title, paragraphs | R |

Los fixtures contienen títulos reales, hero de Inicio, listas técnicas ENE/DIG,
nota hídrica, presentación de equipo, titulaciones, ayuda y estados de Contacto
trazados a D03. El resto incluye texto explícitamente sintético de contrato,
no publicable. No se presenta el fixture como contenido ES migrado ni como
certificación de paridad literal. La validación JSON no pierde los datos presentes.

No hay cobertura completa de medios: WEB todavía no ofrece MediaRef. Los campos
media/portrait aceptan exclusivamente None; rechazan un ID o diccionario inventado.
La ausencia se documenta como `integration_pending` al construir una página real.
Así se implementa lo independiente sin convertir R24/H01 en una identidad paralela.

## E. Pruebas y reproducibilidad

Comandos de verificación:

```powershell
.venv/Scripts/python.exe -B -m pytest tests/unit/editorial -q
.venv/Scripts/python.exe -B -m pytest tests/contracts/test_architecture.py -q
.venv/Scripts/python.exe -B -m pytest -q --tb=short --basetemp <TEMPORAL-NUEVO>
```

En el usuario aislado de ejecución, la primera suite encontró acceso denegado al
temporal pytest previo y tres consultas Git rechazadas por propietario distinto.
Se usa una carpeta temporal nueva fuera del repositorio y una excepción
safe.directory mediante GIT_CONFIG_COUNT/KEY/VALUE solo en el entorno del proceso.
No se modifica la configuración Git persistente ni las pruebas para acomodarlo.

Las pruebas cubren negativos de primitivas/referencias, nueve secciones,
discriminadores, propósitos, duplicados anidados, cardinalidad mínima, orden,
reconstrucción JSON, entidades borrador, pruebas de arquitectura y la matriz D03.
Resultado final: 139 pruebas editoriales, 6 pruebas arquitectónicas y suite
completa de 220 pruebas aprobadas. Sin fallos en la ejecución con el entorno
de proceso corregido. No se relajan contratos ni se modifican pruebas WEB.

## F. Integración WEB y desviaciones justificadas

1. PageIdentity respeta la gramática de PageId WEB, incluidos guiones bajos.
   EditorialId conserva la gramática con guiones para bloques y entidades. No hay
   registro alternativo, slug o mapeo inglés-español dentro del dominio.
2. WEB Locale es un objeto de configuración (code/name/published), no el valor
   editorial. Además editorial→localization está prohibido. LanguageCode valida
   solo forma textual compatible con LocaleCode; aplicación comprobará membresía.
   No se duplica la lista es/ca/en/de ni la política de publicación.
3. No existe MediaRef ni contrato físico de PDF. Se pospone el primero; el
   catálogo editorial contiene solo catalog_id/sector_id/title/description.
   No contiene disponibilidad, idioma físico, versión, ruta ni derechos.
4. Las referencias Rxx pertenecen a documentación visual; el manifiesto tiene
   otros IDs. WEB debe confirmar su correspondencia, no se infiere R24=H01.
5. El cargador único YA existe en adapters/yaml_files.py y es propiedad WEB.
   A2 debe reutilizarlo, conforme a arquitectura actual, sin implementar otro.

## G. Estado final

Sin cambio de rama, commits o push. HEAD final idéntico al inicial:
`fca65e8ba7d75317be150e3f428be67d87825d34`. Estado final: nueve archivos
nuevos y un archivo modificado (`editorial/__init__.py`). La comparación SHA-256
de archivos preexistentes en src/config/content/tests/docs y pyproject.toml
detecta únicamente esa modificación autorizada; ninguna eliminación ni cambio
ajeno observado. `git diff --check` sin errores de whitespace.
Las únicas modificaciones son dominio, pruebas propias e informe.

## H. Preparación de A2

- Usar `inicio.yaml` (nombre determinado por routes.yaml), no `home.yaml`.
- Cargar con adapters/yaml_files.load_yaml y validar con PageContent.
- Inyectar locale desde contexto y contrastarlo con LocaleSettings.
- H01–H07 y IDs internos estables; los textos definitivos se migrarán de D03,
  nunca desde los strings sintéticos del fixture.
- Resolver antes el contrato MediaRef con WEB para hero, tarjetas y figura H03.
  Ampliar únicamente los campos None con ese contrato, sin tocar manifiestos
  desde CONTENT. Añadir pruebas específicas para alt, captions y referencias.
- Registrar SEO y H05 pendientes donde aún no exista aprobación.
- Acordar versión/envelope del conjunto, API de carga y validación transversal
  con application; no están implementados en A1.
- Validar referencias compartidas, página/sección/entidades y pertenencia a
  idiomas en A2. No hay fallback ni permiso de publicación implícito.
- El loader WEB actual deberá evaluarse contra el perfil editorial requerido
  (además del rechazo ya existente de claves duplicadas); no se cambia en A1.

A1 termina aquí. No se inicia A2 ni se crean YAML definitivos.
