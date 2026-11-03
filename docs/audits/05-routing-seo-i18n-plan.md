# 05 · Rutas, SEO e idiomas

Plan propuesto; ninguna URL pública se modifica con la auditoría. El objetivo es un documento HTML estático por página aprobada e idioma, accesible por petición directa y sin JavaScript. [Inventario actual](02-architecture-findings.md).

## Mapa de transición completo

Conservar `capacidades` como segmento técnico ES evita mezclar el cambio de etiqueta pública «Áreas técnicas» con una nueva reestructuración de URLs. Los slugs interiores se hacen españoles. Estas son rutas propuestas, no una lista de páginas que deban publicarse todas con el contenido pendiente actual.

| Origen histórico | Destino ES propuesto | Condición |
|---|---|---|
| `/` y `#/` | `/es/` para Home; `/` como entrada neutral | Decidir entrada de raíz antes del lanzamiento |
| `#/capacidades` | `/es/capacidades/` | Índice |
| `#/capacidades/infrastructure` | `/es/capacidades/infraestructura/` | Piloto sugerido |
| `#/capacidades/energy-systems` | `/es/capacidades/sistemas-energeticos/` | Tras validar cifras |
| `#/capacidades/digital-systems` | `/es/capacidades/sistemas-digitales/` | Contenido parcial: no publicarlo como completo |
| `#/sectores` | `/es/sectores/` | Conservar siete secciones actuales |
| `#/proyectos` | `/es/proyectos/` | Índice diferencia experiencia del equipo |
| `#/proyectos/experiencia-del-equipo/campus-universitario` | `/es/proyectos/experiencia-del-equipo/campus-universitario/` | Mantener atribución y validar datos |
| `#/proyectos/experiencia-del-equipo/mep-hoteles-colegios-residencial` | `/es/proyectos/experiencia-del-equipo/mep-hoteles-colegios-residencial/` | No separar en casos nuevos sin evidencia |
| `#/proyectos/experiencia-del-equipo/energia-offshore-internacional` | `/es/proyectos/experiencia-del-equipo/energia-offshore-internacional/` | Confirmar participación y nombres |
| `#/conocimiento` | `/es/conocimiento/` | Índice solo si ofrece contenido útil; no generar cinco artículos vacíos |
| `#/sobre-bafras` | `/es/sobre-bafras/` | Equipo y filosofía como secciones |
| `#/contacto` | `/es/contacto/` | Formulario y destinos legales revisados |

No acortar ahora las tres rutas de experiencia a slugs promocionales nuevos; se conserva su significado y se reduce el riesgo. Si se decide más adelante un nombre como transición energética UIB, mapear la entidad estable y conservar alias explícito.

## Página, sección y componente

- **Página:** intención y contenido independientes; URL `/es/servicios/instalaciones-electricas/` si existe suficiente alcance, entregables y evidencia propia.
- **Sección:** parte del relato de una página; `/es/capacidades/infraestructura/#instalaciones` mantiene el bloque actual. Crear `#instalaciones-electricas` solo al disponer de una sección realmente identificable; no prometer hoy ese ID existente.
- **Componente:** CTA, ficha, breadcrumb o métrica; se reutiliza y no necesita página ni aparecer en sitemap.

Preservar inicialmente los IDs editoriales enumerados en 02. Cambiar `#/sobre-bafras@equipo` por `/es/sobre-bafras/#equipo`; `#/capacidades@metodologia` por `/es/capacidades/#metodologia`; `#/sectores@hotelero` por `/es/sectores/#hotelero`; `#/contacto@colaboracion` por `/es/contacto/#colaboracion`. Cuando hoteles merezca ficha, mantener el ancla antigua en el índice con vínculo a la ficha; no perderla al extraer un bloque. Registrar alias si se renombra un ID. Los IDs técnicos de slots no son por defecto destinos públicos.

## Hash routing y compatibilidad

Un fragmento no forma parte de la petición HTTP. El servidor recibe `/` para todos los `/#/…`; por eso ni un 301 del servidor ni cambiar solo canonical distinguen los trece destinos históricos. Google recomienda no usar fragmentos para cambiar el contenido principal: [URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure). La Home puede indexarse; no se debe concluir que toda la web es invisible, sino que las vistas no tienen identidad documental independiente fiable.

Consecuencias actuales: un solo recurso y head inicial; previews sociales sin metadatos propios por ficha; enlaces compartibles dependientes de JS y de la sintaxis `@`; analítica por pathname no distingue vistas sin instrumentación; foco y anuncios de navegación requieren código; las anclas no son nativas. Sustituir por archivos reales permite metadatos en la respuesta, navegación nativa y medición por URL. No basta convertirlo en SPA con History API.

Compatibilidad propuesta, solo al habilitar cada destino:

1. Generar `legacy-routes.json` con las trece claves conocidas y los alias necesarios; el build produce un mapa público seguro que solo incluye destinos disponibles.
2. En `/` y su documento equivalente `index.html`, un adaptador pequeño detecta exclusivamente hashes `#/…`, captura errores de decodificación y normaliza una barra final. Separar ruta/ancla una vez; no usar el fragmento en un selector CSS.
3. Resolver ruta en allowlist, validar el ancla dentro del documento de destino (índice de IDs del build) y realizar `location.replace(destino + '#ancla')`. Destinos siempre internos y generados; no aceptar URLs o protocolos del fragmento. Conservar parámetros de campañas permitidos, como `utm_*`, en el destino; no propagar parámetros arbitrarios con datos de consulta.
4. Para ruta desconocida, mostrar entrada con explicación y enlaces útiles; para ancla desconocida de ruta conocida, abrir la página sin el fragmento y registrar incidencia de revisión. No enviar todas las rutas desconocidas a una Home que aparente éxito.
5. Sin JS, la raíz ofrece enlaces reales a ES y a idiomas disponibles; explicar acceso por navegación si el usuario trae enlace antiguo. No prometer un salto automático de hash sin JavaScript.

Este reemplazo es navegación cliente, **no un 301**. Mantener el adaptador ligero mientras puedan circular enlaces antiguos y comprobarlo con la lista completa, incluyendo `@`, codificación inválida, consultas UTM y barras finales. Durante piloto, la raíz antigua continúa operativa: no instalar todavía el adaptador ni apuntar a rutas no publicadas.

Para futuras URLs de pathname retiradas sí preferir 301/308 en hosting que permita reglas de servidor/CDN. El repositorio solo evidencia compatibilidad con hosting estático y CNAME. GitHub Pages se documenta como servicio de archivos estáticos: [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages). Por esa naturaleza, no asumir soporte de reglas arbitrarias tipo `.htaccess` o configuración de Nginx en este proyecto; confirmar posibilidades reales en los ajustes del proveedor. Si se conserva Pages sin reglas, un archivo antiguo con canonical, enlace y reemplazo cliente es compatibilidad limitada, no HTTP 301. Evitar un `404.html` que convierta cualquier ruta inexistente en SPA con 200 aparente.

## Enlaces internos y páginas comerciales

Home enlaza a capacidades y evidencia; capacidad a servicios aprobados, sectores y fichas relacionadas; cada servicio a su capacidad, sectores, evidencia y contacto; sector a servicios aplicables y casos; proyecto a capacidades/servicios y sector; conocimiento a temas comerciales relacionados y CTA pertinente. Cada nueva página debe tener enlace entrante desde índice y al menos un contexto editorial real, migas y enlace de vuelta. Validar el grafo, no solo la existencia de href.

| Tema solicitado | Tratamiento inicial | Umbral para página independiente |
|---|---|---|
| Ingeniería de instalaciones en Mallorca | Página de infraestructura | Ya tiene disciplinas, proceso y entregables; reforzar evidencia aprobada |
| Proyectos de instalaciones eléctricas | Sección de infraestructura; candidata a servicio | Problema, alcance y entregables propios y evidencia diferenciada |
| Ingeniería de climatización | Sección MEP; candidata a servicio | Casos, condicionantes y alcance térmico específicos |
| Ingeniería energética | Página de sistemas energéticos | Relato técnico ya amplio; confirmar datos |
| Fotovoltaica industrial | Sección energética; candidata posterior | Alcance industrial verificable, integración y caso útil |
| Estudios de almacenamiento energético | Sección energética; candidata posterior | Metodología, hipótesis/entregables y evidencia publicable |
| Automatización industrial | Sección digital primero | Completar contenido digital y diferenciar del BMS de edificios |
| Monitorización energética | Relación energía/digital; un propietario editorial | Evitar dos servicios duplicados; definir problema y entregables |
| SCADA | Sección digital | Proyecto y alcance SCADA validados; no glosario comercial vacío |
| Ingeniería para hoteles | Mantener ancla sector hotelero; primera ficha sectorial candidata | Necesidades de operación hotelera, servicios y evidencia autorizada |
| Instalaciones para terciario | Mantener ancla terciario | Diferenciación respecto de hoteles y contenido útil propio |

No se hizo investigación de demanda/competencia ni se prometen posiciones. Mallorca/Baleares pueden aparecer donde sean reales y útiles; no multiplicar páginas por localidad con el mismo contenido. `Service` o `BreadcrumbList` no garantizan resultados enriquecidos.

## Contrato SEO del HTML generado

- Documento con `lang`, un H1 principal y jerarquía nativa coherente; contenido de la página disponible sin scripts.
- Title y description propios, derivados de datos aprobados. Ejemplo orientativo, no reescritura aplicada: «Ingeniería de instalaciones en Mallorca | BAFRAS Engineering» para infraestructura. Detectar duplicados entre documentos publicados.
- Canonical absoluto a la propia versión y ruta normalizada con `/`; no canonicalizar las traducciones a español. Configurar origen de producción una sola vez y verificar host preferido antes del despliegue.
- OpenGraph por página: title, description, URL, tipo apropiado e imagen social aprobada con alt; datos de tarjetas sociales si se usan. No asumir que crawlers sociales ejecutan router.js.
- Sitemap con URLs publicadas y canonicales, sin hashes, borradores ni páginas duplicadas. `lastmod` solo con fechas reales. Robots permite recursos necesarios e incluye sitemap; ausencia actual de robots no significa bloqueo. Para previews, control de acceso o noindex verificable; robots por sí solo no evita indexación.
- Schema.org: `Organization` en contexto corporativo con datos confirmados; `WebSite`; `BreadcrumbList` en detalles; `Service` donde describa un servicio real. No inventar reseñas, direcciones, certificaciones o proyectos BAFRAS. JSON-LD serializado de forma segura y compatible con el control de scripts inline, que hoy prohíbe cualquier bloque sin src.
- Migas como `<nav aria-label="Ruta de navegación"><ol>…`; estado actual desde el build. Páginas inexistentes entregan 404 real del hosting y una página útil.
- Dimensiones/variantes de imágenes, recursos por página y JS mínimo; medir LCP/CLS/INP tras publicar o con laboratorio apropiado, sin confundir HTML pequeño con rendimiento demostrado.

## Idiomas y slugs traducidos

Prefijos propuestos: `/es/`, `/ca/`, `/en/`, `/de/`. Cada entidad conserva ID independiente del nombre y slug. Ejemplo: ID `cap.infrastructure` → ES `/es/capacidades/infraestructura/`, CA `/ca/capacitats/infraestructura/`, EN `/en/capabilities/infrastructure/`, DE `/de/kompetenzen/infrastruktur/`. Los slugs no españoles son propuestas a revisar por traductores; no se crean esas páginas durante la auditoría.

El resolver enlaza por `(ID, locale)`, nunca sustituyendo strings dentro de una URL. El slug publicado se considera estable: si cambia, registrar alias y su estrategia de redirección según hosting. El build rechaza colisiones, rutas reservadas y slugs inseguros. Las traducciones mantienen relación por ID aunque el texto o estructura editorial no sea idéntico.

Cada traducción tiene `draft/review/approved`, fecha y revisor; solo `approved` y completa publica. Campos requeridos y etiquetas UI deben existir; su ausencia es error de build para una versión solicitada. No generar una página CA con cuerpo ES como fallback. Si falta traducción, el selector indica «Disponible en español» con enlace explícito a esa versión; no anuncia un idioma que no existe. En móvil el selector también debe ser accesible. No forzar idioma por IP/navegador.

Emitir hreflang recíproco, autorreferente y con URLs absolutas **solo entre equivalentes publicados**; usar `es`, `ca`, `en`, `de` salvo necesidad regional acreditada. En raíz se propone selector neutral con canonical propio; puede ser `x-default` en el grupo Home. No enlazar todos los servicios a la Home como si fuera su equivalente traducido, ni usar raíz como sustituto universal. Para grupos sin selector neutral específico se puede omitir `x-default`.

Google documenta idiomas alternativos y reciprocidad en [Localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions), y recomienda URLs distintas para versiones lingüísticas en [Managing multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites). Estas reglas no equivalen a disponibilidad editorial: no publicar idiomas sin revisión para completar el selector.
