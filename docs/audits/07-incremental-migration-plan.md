# 07 · Migración incremental, aceptación y primer encargo

Estado: **plan preparado; auditoría finalizada sin implementación**. La aprobación de la arquitectura y del primer alcance debe preceder cualquier cambio de código. El trabajo actual solo crea los siete documentos de `docs/audits/`.

## Secuencia ejecutable tras aprobación

| Fase | Trabajo | Criterio de salida | Riesgo y vuelta atrás |
|---|---|---|---|
| 0 · Preservar | Repetir Git status/diff y validaciones; registrar cambios del usuario, dominio y configuración real de publicación. Guardar copia/artefacto fuera de cambios de código; acordar rama de trabajo, sin cambiarla automáticamente | Baseline reproducible, responsables y método de recuperación conocidos | No usar reset/clean/stash automático ni commits que incluyan cambios ajenos |
| 1 · Base aislada | Crear esqueleto Python/Jinja/JSON, dependencias fijadas, resolver de rutas, estados y salida separada. No conectar aún despliegue | Build determinista de una página mínima, errores útiles, salida bajo directorio permitido | Si crece un framework propio, revisar decisión antes de seguir |
| 2 · Piloto | Extraer Infraestructura con texto, IDs, diseño y componentes actuales; contrato de contenido y medios. Generar `/es/capacidades/infraestructura/index.html` en artefacto de preview | HTML útil sin JS, title/description propios, enlaces y assets resueltos, contenido sin pérdidas, comparación visual revisada | No sustituir `index.html` operativo; descartar salida piloto sin tocar fuentes actuales |
| 3 · Rutas y medios | Validar acceso HTTP directo/recarga, anclas y mayúsculas; resolver IDs de medios, dimensiones/variantes; comparar responsive | Ningún enlace nuevo roto ni imágenes faltantes; encuadre/ritmo aceptados en matriz visual | Usar originales/derivados actuales como fallback; no reorganizar archivos globalmente de golpe |
| 4 · Compartidos | Extraer cabecera, pie, marca, CTA, migas, evidencia y responsable. Mantener orden CSS; consolidar estilos en cambio separado | Segunda página usa componentes sin copiar estructura; navegación teclado y móvil revisada | Evitar mezclar rediseño con extracción; volver a versión previa del artefacto |
| 5 · Resto ES | Migrar Home, índices, Energía, Digital, equipo/contacto y fichas con sus estados editoriales. Digital/proyectos pendientes siguen fuera de publicación definitiva o requieren revisión | Paridad de contenido; grafo completo; resolución de discrepancias antes de marcar páginas publicables | No completar placeholders con invenciones; conservar raíz antigua durante transición |
| 6 · Idiomas | Probar resolver y contratos con una traducción piloto humana revisada; habilitar versiones completas progresivamente | Selector correcto, etiquetas UI completas, hreflang recíproco y sin fallback silencioso | Una versión incompleta no se genera; ES puede publicarse sin esperar todos los idiomas |
| 7 · SEO y publicación preparada | Head, sitemap, robots, Schema apropiado, 404, compatibilidad hash; revisar dominio, formulario y privacidad; producir artefacto candidato y rollback | Checklist de aceptación y preview revisados; cambios de publicación concretos listos para aprobación final | No desplegar, hacer push ni cambiar DNS hasta la autorización correspondiente |

La fase piloto puede incluir slots existentes pendientes en preview interno, claramente separados del artefacto publicable. Que una página se haya migrado técnicamente no la convierte en aprobada editorialmente. No bloquear la extracción por falta de una fotografía opcional, pero tampoco publicar un hueco de evidencia presentado como caso real.

## Estimación y complejidad

Complejidad global **media**: HTML y visuales reutilizables, sin backend, pero con 13 vistas, contratos nuevos y cuatro idiomas previstos. Para la opción B: aproximadamente 8–14 jornadas técnicas de una persona familiarizada con Python/HTML, incluyendo extracción y validación de las vistas actuales. Orientación: base/preservación 2–3; piloto y rutas/medios 2–3; compartidos y resto ES 3–5; contratos i18n, SEO y preparación de publicación 1–3. Las tareas pueden solaparse y estas cifras no son un compromiso de plazo.

No incluye redactar/traducir todo CA/EN/DE, producir material gráfico, obtener permisos, resolver datos técnicos con terceros ni tiempos de aprobación. Si esos insumos faltan, puede estar terminado el trabajo técnico sin estar listo el lanzamiento. El piloto debe recalibrar la estimación antes de migrar todas las vistas. Consolidación CSS profunda y nuevos servicios/sectores no son requisitos previos para extraer las páginas existentes.

## Matriz de calidad propuesta

| Área | Prueba automática futura | Revisión humana necesaria |
|---|---|---|
| Estructura/build | Instalación limpia, build reproducible, salida permitida, archivos esperados, errores `StrictUndefined`, HTML parseable | Correspondencia con arquitectura y ausencia de complejidad innecesaria |
| Contenido | Campos requeridos, estados, IDs únicos, relaciones existentes, métricas en una sola fuente; bloquear pendientes en release | Exactitud técnica, alcance, responsabilidad y atribución equipo/BAFRAS |
| Rutas | Colisiones, acceso por URL directa y recarga, slash, locale, 404; mapa de 13 rutas históricas | Claridad y estabilidad de slugs |
| Enlaces/anclas | Href internos, destinos y anclas en el documento correcto, enlaces desde índices y contexto; codificación malformada segura | Utilidad de enlaces relacionados y navegación comercial |
| Imágenes | Existencia, formato, dimensiones, variantes, `srcset`, case-sensitive, aprobación y alt por idioma | Calidad, derechos confirmados, recorte, color, significado y fidelidad de diagramas |
| Traducciones | Integridad de versión publicada, etiquetas UI, IDs equivalentes, selector y hreflang recíproco; rechazar cuerpo de fallback silencioso | Revisión lingüística y técnica; no basta comparar claves |
| Metadatos | Titles/descriptions no vacíos ni duplicados, canonical propio, OG, JSON-LD válido, sitemap de publicados | Relevancia comercial y veracidad de datos estructurados |
| Formulario | Labels/required/POST; navegador con red simulada para éxito/error/desconexión/doble clic; comprobar recuperación del botón | Envío controlado solo con autorización, recepción real, texto de privacidad y destino legal |
| Navegación | Menú, teclado, foco, back/forward, enlaces hash heredados, JS desactivado | Lector de pantalla, Escape/foco y comprensión de estados |
| Responsive | Navegador para overflow, elementos visibles y carga de medios a varios tamaños | Capturas antes/después, ritmo, alineación, tipografía, contraste y encuadre |
| Accesibilidad | Herramienta de reglas automatizadas si se incorpora; landmarks, nombres, headings nativos y IDs | Teclado completo, lector, ampliación y contraste contextual |
| Rendimiento | Medir recursos, duplicaciones de descarga, tamaño y pruebas de laboratorio cuando el navegador funcione | Experiencia real móvil; Core Web Vitals de campo cuando haya datos |

Pruebas de navegador con respuestas simuladas no deben enviar datos al proveedor real. Los enlaces externos pueden comprobarse por separado con límites y tolerancia a indisponibilidad temporal; no convertir cada fallo externo transitorio en rotura del build.

Los tests actuales afirman estructura literal: marcadores `div.pagina`, clases compartidas, rutas hash y texto. Además `test_no_unconsumed_data_directory` prohíbe `data/`, y el validador rechaza scripts inline, incluido un futuro JSON-LD sin excepción de tipo. Adaptarlos por fases a contratos de salida, sin conservar restricciones del monolito que impedirían la arquitectura aprobada. Mantener controles de codificación, dominio, referencias y contenido. No borrar tests simplemente para obtener verde.

El validador actual comprueba el ID de ancla en el conjunto del HTML, no necesariamente en la vista de destino; el nuevo debe usar el documento correcto. Su lectura de `srcset` no constituye una validación completa de múltiples candidatos, y sus advertencias de publicación no fallan el comando. Añadir pruebas de estos riesgos reales, sin duplicar la implementación con asserts de cada clase visual.

## Revisión visual y alternativa al navegador fallido

En esta auditoría Chrome headless falló al arrancar: exit 2147483651, procesos GPU `-1073741790`, errores de acceso/caché y `GPU process isn't usable`. No existe comparación visual aprobada ni medición Lighthouse. Pytest y parsing no sustituyen esa revisión.

Alternativa inmediata: `python -m http.server 8000` para el original y otro puerto/directorio para el piloto cuando exista; abrir Chrome/Edge interactivo, sin instalar nada ahora. Matriz mínima: 1440×900, 1024×768, 768×1024, 390×844 y 320×568; comprobar ambos lados de 1100px para menú/idiomas, zoom 200%, teclado y movimiento reducido. Revisar Home, las tres capacidades, sectores, una ficha y contacto; extender al resto antes de lanzamiento. Registrar navegador/versión, viewport, fecha, capturas y diferencias aceptadas en la documentación de la implementación.

Con entorno compatible, incorporar Playwright y herramienta de accesibilidad solo tras aprobar esa dependencia y sus binarios; ejecutarlos en CI o equipo sin el fallo del sandbox. No pedir elevación ni deshabilitar protecciones del navegador para declarar una validación conseguida.

## Riesgos y decisiones abiertas

| Riesgo | Mitigación / decisión |
|---|---|
| Cambios locales amplios que no coinciden con HEAD | Migrar desde working tree acordado; comparar huellas y diffs; nunca sobrescribir cambios del usuario |
| Hosting real y rama de publicación desconocidos | Inspeccionar ajustes antes de configurar Actions; no suponer que la rama actual está publicada |
| Hashes históricos sin redirección de servidor | Adaptador allowlist solo para destinos disponibles; mantener navegación sin JS y probar mapa completo |
| Datos y atribución de referencias | Resolver divergencias UIB; confirmar nombres, magnitudes y alcance offshore/MEP con responsables |
| Derechos de fotos/planos y material pendiente | Manifiesto con autorización y exclusión de recursos no aprobados; cotejar Plan Maestro original |
| Falta de versiones lingüísticas | Publicar únicamente traducciones revisadas; decidir orden CA/EN/DE por necesidad comercial |
| Cambios visuales involuntarios por cascada | Mantener CSS inicial, separar consolidación y extracción, capturas comparables |
| Generador propio que crece demasiado | Acotar funciones; reevaluar Astro con evidencia del piloto |
| Formulario no probado y privacidad pendiente | Pruebas simuladas primero; entrega real y política/destinos revisados antes de lanzamiento |

Decisiones que requieren definición antes de implementación o lanzamiento, según fase: aceptar B o C; aprobar alcance de piloto y dependencias; mantener `/` como selector neutral o elegir otra entrada explícita; confirmar dominio/origen y hosting; validar datos/permisos; priorizar idiomas y servicios realmente diferenciados; aportar Plan Maestro original para cotejo. Ninguna requiere alterar el sitio para completar esta auditoría.

## Propuesta de primer prompt de implementación

> Implementa únicamente las fases 0–2 del plan aprobado en `docs/audits/`, usando Python + Jinja2 y JSON. Verifica primero rama, Git status y cambios pendientes; no cambies de rama ni sobrescribas trabajo existente. Crea una base aislada con salida separada y migra como piloto solo Infraestructura e Ingeniería a `/es/capacidades/infraestructura/index.html`. Conserva contenido, IDs, CSS efectivo y composición actuales; extrae los componentes mínimos necesarios y añade contratos simples de contenido, rutas y medios. Usa Jinja con autoescape y StrictUndefined, dependencias de desarrollo fijadas y un comando de build documentado. El original debe seguir funcionando. No inventes imágenes, cifras, traducciones ni permisos; los pendientes solo podrán estar en preview y nunca en un artefacto release. Valida build, enlaces, anclas y assets del piloto, acceso HTTP directo, metadatos y navegación sin JS; compara visualmente con el original y documenta cualquier limitación real del navegador. No migres otras páginas, consolides todos los estilos, reorganices todos los assets, publiques, hagas commits/push ni cambies DNS/CNAME. Entrega diff revisable, resultados, limitaciones y estimación recalibrada antes de continuar.

## Resultado de esta auditoría

Validador existente: pasa con avisos 33/10; pytest: 18/18 pasan. Navegador: bloqueado por arranque del entorno, sin validación visual. Documentación entregada: 01 baseline, 02 hallazgos, 03 decisión, 04 estructura, 05 rutas/SEO/i18n, 06 contenido/assets, 07 migración. El próximo paso es aprobar una arquitectura y el piloto; no se ejecuta la migración durante esta solicitud.
