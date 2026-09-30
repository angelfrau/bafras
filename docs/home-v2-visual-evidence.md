# Home V2 â€” Visual & Evidence Layer

## Objective

Dar ritmo visual distinto a las secciones de Home, integrar el diagrama de visiÃ³n de sistema y preparar las capacidades y referencias para evidencia real, sin inventar activos ni alterar el routing o la arquitectura global.

## Baseline

- Rama: `feat/contingut-v2`.
- Estado inicial: `index.html` y `docs/` ya tenÃ­an cambios sin commit por las iteraciones previas de Home e idioma; se preservaron.
- El usuario habÃ­a aÃ±adido `assets/images/home/vision/bafras-system-vision-diagram.png` (1536 Ã— 1024; 1,906,658 bytes).
- No existÃ­a previamente el inventario visual ni el registro de esta iteraciÃ³n.

## Problems identified

- La visiÃ³n de sistema se comunicaba principalmente mediante texto y etiquetas.
- Problemas, capacidades, mÃ©todo, proyectos y sectores repetÃ­an el patrÃ³n de tarjetas blancas.
- Las referencias no exponÃ­an una estructura compacta de responsabilidad, sistemas y magnitudes.
- El footer mostraba un nÃºmero de versiÃ³n y una fecha/hora de desarrollo.
- Las imÃ¡genes disponibles para hotelerÃ­a y edificios no tenÃ­an correspondencia validada con los casos; no se asignaron.

## Decisions

- Integrar la visiÃ³n como composiciÃ³n editorial en fondo verde oscuro, con imagen conceptual a la derecha en escritorio y bajo el texto en mÃ³vil.
- AÃ±adir los nombres de las capacidades mediante HTML, no dentro del asset; imagen con texto alternativo descriptivo y carga diferida.
- Hacer de las cinco necesidades enlaces semÃ¡nticos hacia capacidades existentes, con indicador y hover/focus sobrios.
- Diferenciar capacidades como filas numeradas con slots opcionales de evidencia en vez de otra serie de cards.
- Mostrar metodologÃ­a como bloque editorial sencillo con secuencia, copy y CTA; retirar etapas detalladas de Home.
- Presentar los tres casos en filas homogÃ©neas con etiqueta, tÃ­tulo, contexto, descripciÃ³n, magnitudes/referencias, sistemas y enlace. Todos quedan como **EXPERIENCIA DEL EQUIPO**; no se resumen responsabilidades ni se aÃ±aden listas de capacidades BAFRAS.
- Mantener los slots visuales de casos y capacidades ocultos hasta disponer de material real aprobado; no mostrar placeholders.
- Retirar el bloque Sectores solo de Home y mantener su pÃ¡gina/navegaciÃ³n general. Situar colaboraciÃ³n en banda de contraste inmediatamente despuÃ©s de experiencia.
- Eliminar versiÃ³n/timestamp del footer sin tocar navegaciÃ³n ni enlaces legales existentes.

## Changes implemented

- **01 Hero:** sin reescritura; se conserva el contenido, la fotografÃ­a existente y la jerarquÃ­a de CTA.
- **02 VisiÃ³n:** imagen integrada desde `assets/images/home/vision/bafras-system-vision-diagram.webp`, labels en HTML y alt en espaÃ±ol.
- **03 Problemas:** cinco necesidades conservadas, convertidas en enlaces a pÃ¡ginas de capacidades existentes.
- **04 Capacidades:** tres filas editoriales numeradas con slots opcionales ocultos para imÃ¡genes futuras.
- **05 MÃ©todo:** bloque editorial con tÃ­tulo, secuencia, pÃ¡rrafo conciso y enlace a metodologÃ­a; sin workflow detallado.
- **06 Experiencia:** tres referencias actualizadas con el copy solicitado, sin campos de responsabilidad ni capacidades relacionadas. Todas se marcan como experiencia del equipo y conservan su enlace interior.
- **07 Sectores:** bloque eliminado de Home; permanecen la pÃ¡gina y navegaciÃ³n de sectores.
- **08 ColaboraciÃ³n/CTA:** banda de colaboraciÃ³n reubicada inmediatamente despuÃ©s de experiencia; CTA final mantenido.
- **09 Footer:** se quitÃ³ `v9 Â· 28/09 12:34`; se mantienen copyright, marca, navegaciÃ³n, contacto y enlaces legales actuales.

## Sections intentionally unchanged

- Arquitectura de pÃ¡ginas, hash routing `#/`, cabecera y vistas interiores.
- Copy principal del hero y fotografÃ­a existente.
- Narrativa comercial general, rutas de contacto y navegaciÃ³n de CTA.
- Contenido de colaboraciÃ³n y CTA final.
- No se alteraron versiones EN/DE ni se aÃ±adieron dependencias.

## Assets integrated

- Original: `assets/images/home/vision/bafras-system-vision-diagram.png`, conservado sin modificaciÃ³n.
- Web derivado: `assets/images/home/vision/bafras-system-vision-diagram.webp`, 1400 Ã— 933, 113,786 bytes (aprox. 94% menos que el PNG original). Compuesto sobre `#0E2B25` y aplanado para evitar artefactos alfa; creado localmente con ImageMagick, sin nueva dependencia.
- Uso: solo en VisiÃ³n de Sistema; `loading="lazy"`, `decoding="async"`, dimensiones intrÃ­nsecas declaradas.
- Las fotos de renders/edificios existentes no se asignaron a capacidades ni casos porque no se pudo verificar su relaciÃ³n con el contenido.

## Assets pending

- Infraestructura e IngenierÃ­a: plano MEP/unifilar, instalaciÃ³n, sala tÃ©cnica, obra, detalle tÃ©cnico o BIM aprobado.
- Sistemas EnergÃ©ticos: FV/BESS, diagrama de integraciÃ³n o curva de consumo autorizada.
- Sistemas Digitales y AutomatizaciÃ³n: captura SCADA/HMI/BMS, arquitectura de control, armario o datos operativos autorizados.
- Campus universitario: fotografÃ­a o diagrama verificable de FV/BESS, SCADA, monitorizaciÃ³n, esquema o plano. Validar los datos solicitados de 7,6 MWp y 10 MWh: el contenido previo de la ficha interior indica ~7,4 MWp FV y +10 MWh BESS.
- Proyecto hotelero: plano MEP, HVAC, instalaciÃ³n elÃ©ctrica, sala tÃ©cnica, obra o instalaciÃ³n terminada; verificar Hotel Formentor y las referencias temporales a centros educativos y residencial en Ibiza.
- Sistemas energÃ©ticos internacionales: infraestructura eÃ³lica marina, sistemas elÃ©ctricos, automatizaciÃ³n/control, arquitectura tÃ©cnica o puesta en marcha; confirmar la publicaciÃ³n de las referencias y magnitudes indicadas.
- Validar permisos de publicaciÃ³n, NDA, atribuciones y contexto de responsabilidad antes de emplear cualquier material. Ver `docs/website-visual-assets.md`.

## Responsive decisions

- VisiÃ³n: columnas en escritorio, pila texto-primero en pantallas estrechas; labels pasan a lista vertical.
- Necesidades: rejilla existente colapsa y enlaces conservan foco visible.
- Capacidades y casos: filas con slots opcionales; si se incorpora visual, pasa a la fila siguiente en mÃ³vil.
- MÃ©todo: secuencia en lÃ­nea con wrap natural en mÃ³vil.
- Experiencia: tres filas en escritorio; una columna en mÃ³vil.
- ColaboraciÃ³n: banda de contraste inmediatamente posterior a experiencia; apilada en mÃ³vil.
- Se ajustÃ³ el ancho del logo y el espacio del header en mÃ³vil estrecho, y se limita el logo del footer por debajo de 280 px. La comprobaciÃ³n final no detectÃ³ overflow horizontal entre 256 y 390 px CSS.

## Accessibility decisions

- Las etiquetas se proporcionan como HTML, independientes del idioma del bitmap.
- El diagrama tiene alt descriptivo: â€œRepresentaciÃ³n conceptual de edificios, instalaciones, sistemas energÃ©ticos y control digital interconectados.â€ No repite el texto completo de la secciÃ³n.
- Necesidades enlazables usan `<a>` nativo y conservan `:focus-visible`.
- Se respetan preferencias de movimiento reducido para transiciones aÃ±adidas.
- Slots vacÃ­os se marcan `hidden`, no se exponen como placeholders.

## Technical notes

- WebP generado con herramienta ya instalada (`magick`); PNG original conservado.
- No se aÃ±adieron scripts, frameworks ni librerÃ­as.
- El footer no muestra versiÃ³n ni timestamp.
- Los enlaces de necesidad apuntan solo a rutas de capacidades que ya existen.
- Los elementos de evidencia no se atribuyen a Proyecto BAFRAS; siguen identificados como Experiencia del Equipo.

## Remaining work

- Recibir, aprobar y anonimizar evidencia visual para las tres capacidades y tres casos.
- Validar las cifras UIB solicitadas frente a los valores de la ficha interior, referencias concretas hoteleras/educativas/residenciales, y los derechos/contexto de las tres experiencias.
- Si se habilita un slot, proporcionar archivo real con dimensiones/peso adecuados, alt contextual y autorizaciÃ³n.
- Revisar el menÃº mÃ³vil en dispositivos reales; el viewport automatizado de 256â€“390 px CSS no muestra overflow tras el ajuste localizado.

