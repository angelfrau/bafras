# Contrato de localización editorial

Fecha: 06/11/2026. Origen: baseline ES de A6, revisión **draft**.
Este documento prepara una futura traducción por IA externa a catalán (ca),
inglés (en) y alemán (de). No aprueba traducciones, no crea un pipeline y no
modifica el loader, el registro de idiomas ni las rutas WEB.

## Fuentes y paquete de entrega

La autoridad textual es [D03 V1.22 y sus addenda aprobadas](../../03_contenido_editorial_V1_22_baseline_G1.md).
Los datos fuente exactos se identifican por sus once SHA-256 en el
[manifiesto ES](../quality/ES_BASELINE_MANIFEST.md). Deben entregarse juntos:

- Nueve archivos de `content/es/pages/`: inicio.yaml, capacidades.yaml,
  infraestructuras.yaml, sistemas_energeticos.yaml, automatizacion_control.yaml,
  sectores.yaml, proyectos_experiencia.yaml, sobre_bafras.yaml y contacto.yaml.
- Dos secuencias de entidades: `content/es/entities/sectors.yaml` y people.yaml.
- Este contrato y el [glosario de contexto](TERMINOLOGY_ES.md).

Una entrega futura preservará los once nombres de archivo y las carpetas
pages/entities bajo el idioma solicitado. No se sobrescribirá ES. La IA no debe
añadir locale a los YAML: el contexto de carga aporta el código de idioma.
No debe renombrar archivos, traducir nombres de claves ni fabricar archivos
common, experiences, resources, fichas o documentos legales.

## Campos traducibles de los contratos reales

Las rutas siguientes describen campos Pydantic, no rutas nuevas de archivos.
La autorización se aplica solo a valores de texto **ya poblados**. Los null,
listas vacías, campos ausentes y discriminadores se conservan. Las colecciones
mantienen orden, pertenencia y cardinalidad. `*` indica cada miembro existente.

| Modelo / campo | Valores traducibles | Restricción |
|---|---|---|
| Paragraph.text, TextItem.text | Párrafos, notas, ejemplos, listas y ayudas | Cada texto conserva su id, padre y posición; no combinar ni resumir |
| SeoMeta.title / description | Metadatos que ya tienen texto aprobado ES | Los null pendientes siguen null; no crear SEO desde títulos o propuestas DEC-05 |
| HeroSection | eyebrow, title, subtitle, attribution; paragraphs[*].text; acciones locales | No convertir subtítulo en párrafo ni atribución en claim de proyecto propio |
| TextSection | title; paragraphs[*].text; notes[*].text; actions[*].label; contact_channels[*].label | ContactChannel.value y target no se traducen |
| CardsSection | eyebrow, title; introduction[*].text; closing[*].text; acciones locales | purpose, items y transversal conservan su tipo y relación |
| CapabilityCard | title; paragraphs[*].text; examples[*].text; actions[*].label | Los ámbitos ilustrativos no pasan a servicios exhaustivos |
| TechnicalAreaCard | title; paragraphs[*].text; included[*].text; tags[*].text | Acrónimos y tokens técnicos protegidos; no mover etiquetas a otra área |
| ApplicationExampleCard | title; description[*].text; disciplines[*].label | Mantener carácter hipotético y cada destino de disciplina |
| DisciplineRelationCard | title; description[*].text | discipline es una referencia inmutable |
| SectorPreviewCard | title; paragraphs[*].text; action.label si existe | Las agrupaciones de Inicio no se sustituyen por la taxonomía de seis sectores |
| EditorialAside | title; paragraphs[*].text | Sigue siendo transversal, no tarjeta de ámbito adicional |
| ItemListSection | title; introduction[*].text; notes[*].text | purpose needs/deliverables/modalities no se traduce |
| NeedItem, DeliveryItem | title; paragraphs[*].text; NeedItem.actions[*].label | No convertir modalidades independientes en secuencia contractual |
| ProcessSection, ProcessItem | title; introduction/closing[*].text; items[*].title y paragraphs[*].text; actions[*].label | purpose workflow/principles y orden permanecen; preservar notas de alcance |
| SectorIndexSection | title; introduction[*].text | sector_refs conserva las seis identidades y el orden |
| ExperienceIndexSection, ExperienceGroup | title; introduction[*].text de sección y grupos | entries permanece vacío en este baseline; no traducir fichas provisionales de D03 como hechos |
| TeamSection | title; introduction[*].text; corporate_presentation[*].text | person_refs inmutable; no atribuir a la empresa habilitaciones individuales |
| ContactFormSection | title; help[*].text; submit_label; messages.success/error; privacy_text solo si ya tiene texto | No activar ni implementar formulario; privacidad null sigue pendiente |
| FormField | label, help, placeholder si existen | id y required son inmutables; conservar indicadores de obligatorio |
| ContactChannel | label | id, target.kind/channel y value son inmutables |
| CallToAction | label | id y target completo son inmutables, incluidos destinos externos |
| Sector | title; description[*].text; examples[*].text; contextual_actions[*].label | id y catalog_refs no cambian; no crear PDF ni nuevas actividades |
| Person | qualification, specialty; biography[*].text si existiese | public_name es nombre propio protegido; no homologar títulos ni inventar biografía |

Los modelos también definen CommonContent (navigation_labels/footer_texts/
interface_messages[*].text y actions[*].label), Experience (title, summary,
attribution, context, intervention, systems, phases, deliverables y
results[*].text) y DownloadableResource (title/description). **No hay archivos
ni entradas de esos catálogos en el baseline entregado**: la IA no debe crearlos.
Una futura incorporación necesitará su revisión propia antes de autorizar
traducción. DocumentedResult.evidence_refs siempre queda protegido.

La lista se basa en los módulos existentes
`src/bafras_web/editorial/{primitives,references,sections,entities,pages}.py`.
No amplía el dominio ni autoriza a rellenar campos porque el modelo los permita.

## Campos protegidos

| Contrato | Campos que se conservan literalmente |
|---|---|
| PageContent / EditorialBundle | page_id, idioma aportado por contexto, estructura de sections/pages y orden |
| SectionBase y todos los items | id, source_block, kind, purpose y pertenencia a colecciones |
| Referencias | InternalLink.page_id/section_id; ExternalLink.url; ContactLink.channel; ResourceLink.catalog_id; SharedActionRef.id/common_ref; todos los kind |
| Índices y entidades | sector_refs, person_refs, experience_refs, experience_ref, catalog_refs, catalog_id, sector_id, Experience.kind y ExperienceEntry.emphasis |
| EditorialReview | status y source_ref completos; draft no cambia tras traducir |
| PendingField | field, reason_code y source_ref completos, incluso cuando la explicación de source_ref esté escrita en español |
| Verification | verified, authorized y evidence_refs; nunca aprobar por traducción |
| Medios | media/portrait null; códigos Rxx y sus fuentes documentales |
| FormField | id, required true/false/null y estructura de campos |
| Contactos / nombres | info@bafras.com, +34 610 903 179; Murti, Àngel, Amin, BAFRAS y BAFRAS Engineering |

No traducir valores que parezcan texto si son identificadores. Por ejemplo,
sectores y ambitos como section_id son claves protegidas, aunque coincidan con
palabras españolas. Las rutas localizadas pertenecen a config/routes.yaml,
no a la traducción de valores. Los selectores de pendiente se conservan
exactamente; no renombrarlos para seguir la traducción de un título.

## Reglas lingüísticas y semánticas

Preservar la diferencia entre capacidad, ejemplo, experiencia del equipo y
proyecto contratado por BAFRAS. No introducir ahorros, plazos, resultados,
certificaciones o intervenciones no acreditadas. Mantener las condiciones
«cuando proceda», «según el alcance», «puede» y equivalentes semánticos: no
convertirlas en compromisos absolutos. Las titulaciones se traducen como datos
de origen, sin afirmar equivalencias profesionales o habilitaciones locales.

Los nombres propios, marcas, siglas y códigos se conservan, incluidos acentos
de Àngel. Los términos técnicos se interpretan con el glosario y el contexto
de cada párrafo; no imponer una traducción mecánica idéntica cuando cambie la
función técnica. El glosario no contiene traducciones definitivas aprobadas.

La extracción de los once YAML no muestra variables de interpolación en el
copy actual. Si en una versión posterior aparecen tokens como `{name}`,
`{{ value }}`, `%s` o enlaces embebidos, preservarlos íntegros y consultar su
contrato antes de traducirlos. Estos ejemplos **no son campos que deban
añadirse**. El asterisco de las etiquetas de formulario es un indicador de
obligatoriedad, no una variable; required y su valor deben permanecer intactos.

Conservar puntos, listas y separación entre unidades de contenido. Las reglas
tipográficas del idioma destino pueden adaptarse solo dentro del valor
traducible, sin alterar números, acrónimos, condiciones o estructura. No
convertir nombres de campos a sintaxis Markdown ni introducir etiquetas HTML.
Usar UTF-8 y YAML compatible con el loader único; no duplicar claves.

## Pendientes, ambigüedades y SEO

Los 22 pendientes de página y seis de persona se conservan, sin traducir sus
selectores, motivos o fuentes. Las dos comprobaciones externas de canales
siguen pendientes de operatividad. No inventar SEO, privacidad, fotografías,
biografías, nombres completos o tarjetas de experiencia para que la traducción
parezca terminada. Las listas vacías PE no representan instrucciones para
completar referencias candidatas.

Ante ambigüedad técnica o profesional, conservar la estructura y devolver una
nota separada que identifique archivo, id y campo, con la decisión requerida.
No incrustar «[PENDIENTE]», comentarios de la IA o alternativas de traducción
en copy público. No resolver cambios de significado mediante fluidez estilística.

El SEO poblado se traduce conservando intención y atribución; no añadir
localidades, nuevos mercados, claims o keywords. El título traducido puede
necesitar revisión SEO posterior, pero esa revisión no autoriza a rellenar los
metadatos que en ES siguen null. Mantener los estados draft y las fuentes ES.

## Procedimiento recomendado de entrega y aceptación

1. Congelar el paquete ES por los hashes del manifiesto e indicar un único
   idioma destino por entrega. Facilitar los once archivos en su árbol original,
   este contrato y el glosario; no enviar el HTML como autoridad textual.
2. Pedir los once YAML completos, con nombres intactos, traduciendo únicamente
   los valores autorizados. Prohibir cambios de estructura, IDs, relaciones,
   estados, contactos o booleanos y la introducción de nuevas entidades.
3. Recibir los archivos fuera de ES y comparar recursivamente claves, tipos,
   orden, cardinalidades, IDs y todos los campos protegidos contra el paquete
   fuente. Cualquier cambio debe resolverse antes de integrar.
4. Usar el loader YAML existente y validar PageContent, list[Sector] y
   list[Person] con Pydantic v2, aportando el idioma por contexto. Comprobar
   que el idioma ya está configurado; no editar rutas o loader para aceptar
   una entrega defectuosa.
5. Ejecutar inspect_editorial para el idioma destino con INCREMENTAL y COMPLETE,
   examinar referencias/pendientes y construir EditorialBundle solo cuando
   can_build_bundle sea verdadero. No hay fallback implícito entre idiomas.
6. Revisar semántica y terminología con una persona competente en el idioma y
   el ámbito técnico, incluidos condiciones, atribución y titulaciones. Las
   pruebas españolas de literalidad contra D03 no se aplican sin adaptación a
   texto extranjero; no deben relajarse ni utilizarse como falsa aprobación.
7. Aceptar la entrega técnica solo si conserva nueve páginas, 51 bloques, seis
   sectores, tres personas, todos los destinos y pendientes, sin contenido
   inventado ni errores de integridad. Mantener draft hasta la revisión
   editorial explícita. La aceptación lingüística no equivale a publicación.

Este es un procedimiento documental: A6 no incorpora exportadores,
importadores, validadores nuevos, traducciones ni herramientas de IA.
