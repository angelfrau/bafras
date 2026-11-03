# 03 · Decisión arquitectónica propuesta

Estado: **recomendación pendiente de aprobación; no implementada**. Fecha: 02/11/2026. Decisión: introducir generación estática con **Python + Jinja2 + JSON estructurado**, conservando CSS y JavaScript nativo reutilizable. La web publicada seguirá siendo HTML/CSS/JS sin servidor Python. [Evidencia local](01-repository-baseline.md).

## Alternativas comparadas

A significa HTML/CSS/JS con archivos y convenciones manuales; si incorpora un compilador de plantillas propio deja de ser una alternativa realmente más sencilla y se aproxima a B.

| Criterio | A · Actual modularizado | B · Python + Jinja2 | C · Astro + contenido + Python |
|---|---|---|---|
| Complejidad inicial | Baja; deuda crece con páginas/idiomas | Baja-media; generador pequeño propio | Media; Node, dependencias y configuración adicionales |
| Aprendizaje | HTML/CSS/JS conocidos | Templates, contratos de datos y build | Astro, colecciones, routing y cadena Node |
| Esfuerzo de migración | Bajo por página, alto por duplicación | Medio; extracción cercana al HTML existente | Medio; extraer HTML a componentes Astro |
| Hosting estático | Directo | `dist/` con HTML ya generado | `dist/` con salida estática |
| Páginas independientes | Manuales | Registro derivado de contenido → `ruta/index.html` | Rutas/colecciones y generación estática |
| Componentes/layouts | Copia o composición manual | Herencia, includes y macros | Componentes y layouts nativos |
| Imágenes | Manual | Manifiesto + tarea Pillow por construir | Herramientas de imágenes integradas; distinguir `src/` y `public/` |
| i18n | Duplicación y enlaces manuales | Resolver por ID/locale y validaciones propias | Soporte routing i18n; contenido y revisión aún propios |
| SEO | Fácil omitir metadatos al copiar | Head compartido y contrato por página | Layout SEO compartido y datos por página |
| Tests | Pytest existente, muy ligado a fuente | Pytest de datos/build/HTML; navegador aparte | Validación colecciones + Python sobre dist + navegador |
| Mantenimiento | Sencillo al principio; multiplicación ES/CA/EN/DE | Un lenguaje de tooling; mantener pequeño generador | Ecosistema más amplio; mantener Node y Python |
| Velocidad al añadir contenido | Decrece al crecer el sitio | Alta tras piloto y plantillas | Alta tras formación y piloto |
| Integración Python | Existente | Directa: validación y build | Procesos auxiliares; no requiere Python en cliente |
| Colaboración con Codex | Fácil editar; difícil garantizar consistencia | Contratos explícitos y diffs de contenido pequeños | Buena con convenciones y herramientas instaladas |
| Dependencias nuevas | Ninguna | Jinja2 fijado como desarrollo | Node compatible y Astro fijado, lockfile; integraciones solo si necesarias |
| Principal coste oculto | Copia y divergencias | Inventar demasiadas funciones de un framework | Versiones/build y doble entorno para un sitio pequeño |

La generación estática y las plantillas de B cubren el requisito crítico de URLs HTML reales. A permite crear archivos HTML, pero no satisface bien «sin copiar estructuras» para 13 vistas y cuatro idiomas. Tampoco basta reemplazar hashes por History API si el host no sirve documentos independientes.

## Motivos para elegir B en este repositorio

Hay Python, pytest y validación propia operativos; no hay Node en PATH, backend, componentes interactivos complejos ni colecciones extensas. El HTML ya es principalmente estático. Jinja permite trasladar bloques a plantillas sin reinterpretar todo el frontend. JSON evita añadir un parser YAML y resulta suficiente para listas, relaciones y traducciones revisadas. El conocimiento técnico puede incorporarse posteriormente como Markdown con una dependencia explícita, si su volumen lo justifica.

Esta elección es una inferencia sobre el coste local y los requisitos, no una afirmación de superioridad universal. Jinja no aporta routing, SEO, traducciones ni imágenes por sí mismo: B exige construir esas tareas acotadas. Astro es la segunda opción razonable si el responsable prefiere su ecosistema o prevé muchas publicaciones y transformaciones de imagen. La ausencia local de Node es fricción de implantación, no una incompatibilidad de hosting.

Límites del generador B: lectura/validación JSON, resolución de rutas por ID y locale, render de unas pocas plantillas, copia de estáticos, generación de metadatos/sitemap/robots y manifiesto de salida; imágenes como tarea separada. Sin plugins arbitrarios, editor web, sistema de bloques genérico, base de datos ni servidor. Un solo comando de build documentado; tests específicos para las reglas comerciales críticas. Si el generador empieza a necesitar extensiones, dependencias de plantillas complejas o un ecosistema de Markdown/imágenes significativo, reevaluar C antes de ampliar infraestructura propia.

## Implementación prevista, todavía no autorizada

- Jinja con `StrictUndefined` y `select_autoescape` para HTML/XML; no habilitar contenido editorial como HTML seguro por defecto.
- JSON UTF-8 con validadores Python pequeños y errores con archivo/campo; los campos ricos iniciales serán párrafos/listas, no HTML arbitrario.
- Construcción determinista, rutas bajo `dist/`, rechazo de slugs absolutos, `..`, colisiones y referencias desconocidas. Nunca limpiar la raíz del repositorio.
- Bloqueo de publicación cuando una página marcada para publicar use evidencia o medios no aprobados. Los borradores se pueden previsualizar en un modo separado, fuera del artefacto público.
- Dependencias de desarrollo fijadas tras seleccionar versiones compatibles y probadas. No se propone un número de versión sin probarlo.

No introducir React, Next.js, CMS, backend ni base de datos: no resuelven una necesidad actual demostrada. El formulario puede conservar su proveedor externo y su POST nativo; verificar entrega y privacidad en una tarea de publicación.

## Coste y umbrales

Estimación orientativa para una persona familiarizada con Python/HTML, sin traducción, producción gráfica ni aprobación de referencias: B, **8–14 jornadas** para base, migración de las vistas actuales y comprobaciones; C, **10–17 jornadas** bajo el supuesto de aprendizaje/configuración local; A, **4–7 jornadas** de refactor parcial sin resolver de forma durable el coste de cuatro idiomas. No son presupuestos ni resultados medidos. Desglose y contingencias en 07.

Aceptar B si el piloto produce HTML accesible sin JS, conserva la composición y permite una segunda página mediante contenido/plantilla sin copia estructural. Reevaluar Astro si el piloto necesita mecanismos propios amplios o si el equipo ya mantiene Node y prefiere adoptar una herramienta completa. No mantener dos generadores en producción.

## Fundamento documental oficial

Fuentes consultadas el 02/11/2026; las decisiones de estructura de este informe son propuestas propias:

- Jinja ofrece herencia e inclusión de plantillas y autoescape configurable: [plantillas](https://jinja.palletsprojects.com/en/stable/templates/), [API y configuración](https://jinja.palletsprojects.com/en/stable/api/).
- Astro permite definir colecciones y validar sus datos: [Content collections](https://docs.astro.build/en/guides/content-collections/). La gestión de imágenes incluye componentes y tratamiento de recursos locales: [Images](https://docs.astro.build/en/guides/images/).
- Astro dispone de herramientas para rutas localizadas, pero estas no sustituyen la traducción editorial: [Internationalization](https://docs.astro.build/en/guides/internationalization/).
- Ambos pueden publicar artefactos estáticos; GitHub documenta el mecanismo de workflows personalizados: [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages). Para C existe [guía oficial Astro/GitHub Pages](https://docs.astro.build/en/guides/deploy/github/).
