# Home V2.1 — Structure Closeout

## Objective

Cerrar la estructura comercial de Home: simplificar metodología, concretar la evidencia de experiencia, retirar el bloque de sectores de esta página y situar colaboración inmediatamente después de experiencia. Se conservan el routing y las páginas interiores.

## Baseline

- Rama: `feat/contingut-v2`.
- Working tree ya contenía cambios previos de Home/idioma, el diagrama de visión y documentos V2; se preservaron.
- Home está implementada en `index.html`, dentro de `.pagina.home`; no se cambió la arquitectura global.

## Changes

- Metodología: se retiró la lista detallada con círculos, columnas y resultados individuales. Quedó título, secuencia horizontal, párrafo editorial exacto y enlace a `#/capacidades@metodologia`.
- Experiencia: introducción y tres referencias sustituidas por el copy V2.1. Se eliminaron los campos explícitos de responsabilidad y las listas de capacidades BAFRAS. Las referencias se presentan bajo `EXPERIENCIA DEL EQUIPO` y conservan sus enlaces interiores.
- Campus UIB: título “Programa de transición energética del campus de la UIB”; Universitat de les Illes Balears · Mallorca; integración fotovoltaica, almacenamiento, movilidad eléctrica y medida/control/gestión; cifras solicitadas: 7,6 MWp y 10 MWh; sistemas FV, BESS, V2G, AMI, SCADA y VPP.
- MEP/edificación: “Instalaciones en hoteles, centros educativos y residencial”; Mallorca e Ibiza; referencias Hotel Formentor, centros educativos y proyectos residenciales en Ibiza; sistemas de electricidad, climatización, fontanería, PCI y MEP.
- Eólica marina: “Grandes proyectos de energía eólica marina”; Dogger Bank A (1,2 GW) y Vineyard Wind 1 (806 MW); sistemas eléctricos, automatización, control y commissioning.
- Sectores: se retiró solo el bloque de Home; rutas, navegación general y página `#/sectores` permanecen.
- Colaboración: bloque oscuro trasladado a continuación de experiencia, con copy y CTA “Trabaja con BAFRAS”.
- CTA final: se conserva sin ampliación.
- Hero, visión, problemas y capacidades: no se reescribieron en este pase.

## Final Home Architecture

01 Hero
02 Visión
03 Problemas
04 Capacidades
05 Cómo trabajamos
06 Experiencia
07 Colaboración
08 CTA final
09 Footer

El footer es global y se conserva tras el CTA. El bloque de sectores ya no forma parte del DOM de Home.

## Pending Content

- Confirmar los valores UIB del copy solicitado para Home: `7,6 MWp` y `10 MWh`. Las fichas interiores existentes al iniciar este pase dicen `~7,4 MWp FV` y `+10 MWh BESS`; Home sigue el nuevo copy solicitado, pero verificar la fuente antes de publicación.
- Validar el nombre Hotel Formentor y los derechos de publicación de la referencia; el copy temporal también menciona “Centros educativos” y “Proyectos residenciales en Ibiza” hasta disponer de nombres concretos.
- Validar atribución, contexto y publicación de Dogger Bank A (1,2 GW) y Vineyard Wind 1 (806 MW); los nombres y magnitudes ya constan en las fichas existentes.
- Material visual real autorizado para UIB, MEP/edificación y eólica marina; los slots siguen ocultos.
- Material visual real para las tres capacidades; sus slots siguen ocultos.
- Rights/NDA, clientes, logos, datos personales y sensibilidad técnica deben revisarse antes de incorporar imágenes o documentos.

## Validation Notes

- Enlaces de Home previstos: metodología, tres experiencias, proyectos y colaboración conservan slugs existentes.
- Navegación, páginas interiores y rutas de sectores quedan intactas.
- No se añadieron dependencias; no se tocó `CNAME`, despliegue, dominio ni idiomas.
- Sin commit ni push.
