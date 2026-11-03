# 02 · Hallazgos de arquitectura

Estado observado el 02/11/2026; evidencia sobre el working tree, no solo HEAD. [Baseline y pruebas](01-repository-baseline.md). Las prioridades P1 bloquean una publicación profesional completa; P2 reducen coste y riesgo de mantenimiento.

## Arquitectura actual y acoplamiento

Un único `index.html` contiene 13 contenedores `.pagina[data-pagina]`. `router.js` escucha `hashchange`, activa un contenedor, cambia title/description y desplaza al ancla con la sintaxis `#/ruta@id`. `pages.css:437` oculta las páginas salvo `.activa`; con JS desactivado un `<noscript>` muestra todos los contenedores, pero los enlaces hash siguen sin ser anclas HTML nativas. No hay páginas HTML independientes de capacidades, sectores o proyectos.

El CSS está separado en cuatro archivos y el JS en tres; esto es una modularización útil que conservar. El contenido no está separado: textos, métricas, relaciones y slots de medios se editan dentro del mismo HTML; títulos SEO se mantienen además en un mapa JS. Los Markdown de `docs/content/` sirven de documentación, no alimentan el sitio. Añadir una nueva capacidad exige hoy HTML, enlaces, CSS potencialmente y metadatos JS coordinados.

## Inventario de páginas y enlaces

Todas las filas son **virtuales**, idioma principal ES y dependencias comunes **D**: `index.html`, cuatro CSS, `router.js` (visibilidad/metadatos), `site.js` (menú/año/fotos). Google Fonts es común. Las referencias de líneas pertenecen al working tree auditado. Entrantes/salientes indican enlaces presentes en código, no tráfico ni backlinks externos.

Códigos: G = cabecera/pie; H = Home; C = índice de capacidades; I/E/Dg = infraestructura/energía/digital; S = sectores; P = proyectos; U/M/O = fichas campus/MEP/offshore; K = conocimiento; A = sobre BAFRAS; F = contacto. Las repeticiones hacia la misma ruta se agrupan. Home recibe el enlace de marca a `/` (fuera de los 99 enlaces `#/…`).

| Ruta actual | Página, función y contenido | Componentes principales | Idioma / dependencia extra | Entrantes | Salientes | Implementación |
|---|---|---|---|---|---|---|
| `/` (`data-pagina=""`, L121) | H: presentación comercial, necesidades, tres áreas, método, experiencia, colaboración | Hero, diagrama, filas de capacidad, casos, CTA | ES / JPG hero CSS, WebP visión | G (marca) | C,I,E,Dg,P,U,M,O,F | Amplia; cifras y evidencias por aprobar |
| `#/capacidades` (L272) | C: áreas técnicas y metodología integrada | Hero, tres áreas, fases, CTA | ES / D | G,H,I,E,Dg,A | I,E,Dg,F | Texto desarrollado; medios pendientes |
| `#/capacidades/infrastructure` (L379) | I: disciplinas MEP, proyecto/obra/verificación, entregables, experiencia | Mapa, módulos técnicos, workflow, evidencia, responsable, CTA | ES / D | G,H,C,E,Dg,U,M,A | C,E,Dg,A#equipo,F | Desarrollada; faltan medios/autorizaciones |
| `#/capacidades/energy-systems` (L512) | E: diagnóstico, FV/BESS, recarga, operación, UIB | Ejes, módulos, métricas, evidencia, responsable, CTA | ES / D | G,H,C,I,Dg,U,O,A | C,I,Dg,A#equipo,F | Desarrollada; cifras y recursos por validar |
| `#/capacidades/digital-systems` (L642) | Dg: instrumentación, BMS/SCADA, integración y datos | Mapa, entregables, evidencia, responsable, CTA | ES con pendientes EN / D | G,H,C,I,E,U,O,A | C,I,E,A#equipo,F#colaboracion,F | Parcial; `EVIDENCE PENDING` visible en fuente |
| `#/sectores` (L734) | S: siete bloques de sectores, necesidades y chips | Bloques dos columnas, chips, CTA | ES / D | G (incluye siete anclas) | F | Índice existente; sin fichas sectoriales |
| `#/proyectos` (L810) | P: tres referencias de experiencia del equipo | Tarjetas, slots, CTA | ES / D | G,H,U,M,O | U,M,O,F | Índice; atribución y recursos pendientes |
| `#/proyectos/experiencia-del-equipo/campus-universitario` (L858) | U: programa campus, alcance, magnitudes, participación | Migas, ficha, slot, lista técnica, relaciones, CTA | ES / D | H,P | P,E,Dg,I,A#equipo,F | Parcial; contexto pendiente y cifras divergentes |
| `#/proyectos/experiencia-del-equipo/mep-hoteles-colegios-residencial` (L906) | M: experiencia MEP Mallorca/Ibiza | Migas, ficha, slot, lista técnica, relaciones, CTA | ES / D | H,P | P,I,A#equipo,F | Parcial; resultados/contexto por confirmar |
| `#/proyectos/experiencia-del-equipo/energia-offshore-internacional` (L954) | O: experiencia energética internacional | Migas, ficha, slot, lista técnica, relaciones, CTA | ES / D | H,P | P,E,Dg,A#equipo,F | Parcial; responsabilidades y permisos pendientes |
| `#/conocimiento` (L1002) | K: artículos, casos, guías, innovación previstos | Bloques, etiquetas «En preparación», CTA | ES / D | G | F | Esqueleto; cinco piezas sin páginas propias |
| `#/sobre-bafras` (L1036) | A: compañía, equipo, filosofía | Biografías, retratos, chips, enlaces, CTA | ES / cuatro slots `data-foto` en el conjunto del HTML | G,I,E,Dg,U,M,O | I,E,Dg,C#metodologia,F; tres LinkedIn | Contenido existente; fotos dependen de JS |
| `#/contacto` (L1106) | F: correo, consulta, colaboración | Formulario, correo, tarjetas de colaboración | ES / `form.js`, FormSubmit | G,H,C,I,E,Dg,S,P,U,M,O,K,A,F | mailto; F#cuentanos-tu-proyecto | Funcionalidad en código; envío no comprobado; privacidad pendiente |

Inventario global: 108 enlaces `<a>`: 99 hash de ruta, tres LinkedIn, dos mailto, tres `href="#"` legales y uno `/` de marca. No se detectan rutas huérfanas en el grafo actual. Sí hay vínculos comerciales insuficientes: sectores solo lleva a contacto; capacidad → ficha de proyecto relacionada no está resuelta por enlaces en todas las áreas, aunque aparecen evidencias textuales. Cada ficha enlaza de vuelta a capacidades. Se propone completar relaciones bidireccionales, no crear bloques de enlaces genéricos.

Anclas editoriales existentes: Home `vision-de-sistema`, `tres-capacidades`, `como-trabajamos`; C `areas-tecnicas`, `intervencion-integrada`, `metodologia`; I `infraestructura-cabecera`, `mapa-area-infraestructura`, `instalaciones`, `definicion-sistema-funcionando`, `coordinacion-instalaciones`, `proyecto-documentacion`, `direccion-asistencia`, `puesta-marcha-verificacion`, `entregables-infraestructura`, `integracion-infraestructura`, `experiencia-infraestructura`, `equipo-infraestructura`, `rel-inf`, `cierre-infraestructura`; E `energia-cabecera`, `mapa-sistemas-energeticos`, `ambitos-energeticos`, `entregables-energia`, `integracion-energia`, `experiencia-energia-uib`, `equipo-energia`, `cierre-energia`; Dg `rel-dig`; S `hotelero`, `industria`, `deportivos`, `terciario`, `infraestructura`, `publico`, `otros`; K `articulos-tecnicos`, `casos-de-estudio`, `guias-tecnicas`, `innovacion`; P `experiencia-del-equipo`; A `quienes-somos`, `equipo`, `filosofia`; F `contacto-directo`, `cuentanos-tu-proyecto`, `colaboracion`. Además existen IDs técnicos de formulario, marca y slots gráficos; no convertirlos automáticamente en rutas comerciales.

## HTML, componentes y accesibilidad

- 110.026 bytes, 1.208 líneas, 1.605 etiquetas de apertura, 76 `<section>`, 13 H1, 68 H2, 77 H3 y 40 H4. No se encontraron IDs duplicados. Trece H1 corresponden a trece vistas; no se debe diagnosticar automáticamente trece H1 visibles a la vez con JS activo.
- Treinta y tres H4 usan `role="heading" aria-level="3"`: existe intención accesible, pero el HTML nativo y el nivel ARIA divergen. Al extraer componentes, usar H3 reales y una clase visual independiente. No penalizar automáticamente todos como saltos accesibles sin considerar ARIA.
- Doce bandas finales `bloque oscuro banda`, tres detalles con una estructura casi idéntica y tres páginas de capacidad con nueve familias de secciones compartidas: candidatos claros a plantillas/componentes. La repetición del HTML generado es normal; debe desaparecer la copia en las fuentes editoriales.
- Veintiocho atributos `style`; SVG de marca embebido compartido por `<use>`, que conviene conservar en un partial. El favicon está embebido como data URI aunque también existe un ICO local.
- Puntos positivos: `header`, `nav`, `main`, `footer`, listas, fichas `dl`, etiquetas de formulario envolventes, estados de menú `aria-expanded`/`aria-controls`, foco visible y tratamiento de movimiento reducido.
- Falta enlace de salto a contenido. El router no lleva el foco al H1 ni anuncia explícitamente el cambio de vista. El menú no maneja Escape ni devolución de foco; comprobar comportamiento con teclado y lector en navegador. El selector de idioma se oculta bajo 1.100px y no hay alternativa móvil en el código actual.
- Los tres destinos legales son `#`. La privacidad del formulario sigue siendo texto pendiente. Cerrar destinos y revisión editorial antes de declarar el contacto listo para publicación; no se emite una conclusión jurídica en esta auditoría.

## CSS: deuda medible y consolidación

70.284 bytes en cuatro archivos. El recorrido de bloques tras retirar comentarios detecta aproximadamente 823 bloques de reglas (incluye pasos de keyframes), 62 `@media` (25 en components y 37 en pages) y once declaraciones `!important` (5 y 6). La cifra de reglas es una métrica textual, no un parser CSS completo.

En igualdad de contexto de at-rules y selector de grupo literal hay **54 grupos repetidos en pages.css** y dos en components.css (`.capa h3`, `.pilar`). Esto excluye repeticiones legítimas entre media queries distintas, aunque una repetición puede añadir propiedades complementarias. No equivale a 56 bugs ni a 56 reglas idénticas eliminables.

Evidencias concretas: `pages.css:143–210` vuelve a fijar tipografía, line-height, ritmo y tarjetas definidos antes; `:root` y tokens de espaciado aparecen también en pages; desde L394 hay un pase «Visual direction refinement V1.1»; `.asset-slot`, `.home .hero`, `.home-caso-magnitudes` y `.caso-caps` acumulan declaraciones; el último par añade más `!important`. `.pagina:not(.home) .bloque.cab`, combinaciones con `:is()`/`:has()` y selectores descendientes elevan el coste de razonar sobre cascada frente a clases simples. No se realizó un cálculo exhaustivo de especificidad ni cobertura runtime.

Clases presentes en CSS pero no como clases literales en HTML: `metodo`, `pilares`, `capability-diagram`, `diagram-node`, `version`, `socios`, `socios-mini`. Son candidatas a revisión, no prueba de código muerto: comprobar selectores compuestos, JS y variantes antes de retirarlas. Hay estilos de componentes generales en pages que afectan otras páginas y se cargarán todos en cada visita mientras el HTML sea único.

Consolidación futura: conservar primero orden y resultado visual; mover valores de diseño a tokens; agrupar declaración efectiva y breakpoints junto a su componente; separar utilidades/layout/componentes/páginas; sustituir estilos inline por clases con propósito; eliminar solamente selectores acreditados sin uso. No introducir `@layer` y cambiar precedencias a la vez que se migra HTML. Revisar contraste y capturas antes/después. La identidad verde/piedra, tipografías, ritmos y composiciones existentes son reutilizables.

## JavaScript: responsabilidades y riesgos

Tres IIFE, sin librerías cliente. `site.js` controla menú, año y búsqueda de retratos por combinaciones de nombres/extensiones; cuatro slots pueden repetir búsquedas y no aportan `loading` ni dimensiones al `<img>` insertado (el contenedor CSS sí reserva espacio). Los PNG son los primeros candidatos; los JPG disponibles no implican que se muestren. Resolver fotos en build permite retirar el mecanismo de ensayo/error y su dependencia de JS.

`router.js` mezcla ruta, historial hash, scroll, estados de menú, navegación activa, transiciones y SEO. Problemas derivados de lectura de código:

1. `decodeURIComponent` sin captura puede lanzar `URIError` con fragmentos malformados; `querySelector('.pagina.activa #' + id)` puede lanzar `SyntaxError` ante anclas no válidas como selector. Usar mapa permitido y búsqueda por ID en la compatibilidad futura.
2. Ruta desconocida se convierte silenciosamente en Home; no hay 404 de recurso independiente. El estado activo no se aplica a Home y solo a enlaces principales, no a todos los subniveles.
3. Las transiciones alternativas usan timers sin cancelación; navegación rápida puede intercalar cambios. Riesgo pendiente de reproducción runtime, no fallo demostrado en navegador.
4. Dependencia del DOM exacto de cabecera/main; carece de validación de entradas. El title y description cambiantes no crean documentos HTTP nuevos.

`form.js` mantiene POST nativo en HTML y mejora con fetch. Usa `response.ok`, no examina el cuerpo del proveedor: confirmar semántica de éxito antes de mostrar confirmación comercial. Deshabilita botón, restablece formulario en éxito y ofrece mailto al fallar; `role="status"` ya existe. Probar errores, desconexión, doble envío, validación y navegación fuera de contacto durante petición; no afirmar entrega de email a partir de un HTTP 2xx. No se envió ningún formulario.

Con HTML generado se eliminan routing de vistas, mapa cliente de SEO, scroll `@`, fotos por adivinación y navegación activa calculada en cliente. Conservar un menú pequeño y mejora progresiva del formulario; año en build o script mínimo. El adaptador de hashes se limita a compatibilidad de entrada, no es un nuevo router. No hay evidencia suficiente para señalar funciones concretas JS como muertas en el estado actual.

## Contenido, SEO y preparación

Treinta slots con `data-asset-id` distintos permiten empezar un manifiesto estable. Hay 21 atributos `data-content-status="placeholder"` y seis `verify`; las regex del validador suman además mensajes, y por eso devuelven 33/10. No hay gobernanza ejecutable que impida publicarlos. El contenido digital incluye mensajes EN de pendiente dentro del sitio ES; CA/EN/DE son botones deshabilitados, no traducciones implementadas.

La ficha UIB indica `~7,4 MWp FV`, `+10 MWh BESS` y financiación; Energía especifica `7,576 MWp`, `2 × 5,016 MWh`, `19` recargas. No resolver por redondeo sin confirmar alcance y fuente. La clasificación «experiencia profesional previa del equipo» debe mantenerse tanto en datos como en UI: no convertir estas referencias en proyectos BAFRAS.

Hay title y description iniciales y 13 entradas de metadatos JS, pero no canonical, hreflang, OpenGraph, sitemap, robots ni JSON-LD. Migas visuales existen como párrafos, no como navegación estructurada. El documento tiene una sola lengua `es`. El favicon y las fuentes no resuelven la ausencia de SEO por página.

Solo hay un `<img>` estático: el WebP de visión, con alt, 1400×933, lazy y decoding async. El hero es un JPG CSS de 504.536 bytes; no tiene variantes responsive ni prioridad explícita de recurso. La visión WebP pesa 113.786 frente a 1.906.658 bytes del PNG original: conservar ese trabajo. No se midieron LCP, CLS, INP ni tráfico de red; no adjudicar una puntuación de rendimiento.

**Conclusión operativa:** base visual y técnica reutilizable; preparada para una extracción controlada, todavía sin sistema de contenido o páginas independientes. P1: rutas reales/SEO, estados editoriales y atribución, contacto y política, traducciones reales. P2: consolidación CSS, medios centralizados y pruebas de navegador. [Plan de rutas](05-routing-seo-i18n-plan.md) y [modelos](06-content-assets-model.md) concretan las soluciones sin modificar el sitio.
