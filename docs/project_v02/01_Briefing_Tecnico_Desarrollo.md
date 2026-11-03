# BAFRAS Engineering — Briefing técnico para el equipo de desarrollo
**Versión:** DEV-HANDOFF-01 · 03/11/2026  
**Estado:** línea base de diseño aprobada individualmente (9/9); **cierre formal G1 pendiente de ratificación expresa**.

## 1. Objetivo del producto
Web corporativa B2B de ingeniería, con tres especialidades (infraestructuras e instalaciones, sistemas energéticos, automatización y control), sectores, experiencia, equipo y contacto. Debe comunicar capacidades reales y facilitar conversaciones comerciales, sin presentar referencias no verificadas. A futuro podrá publicar estudios de ingeniería generados por software externo, sin ejecutar sus motores en el servidor web.

## 2. Qué existe y qué no
**Existe:** contenido editorial y decisiones de publicación D03; arquitectura de software D04; sistema visual acumulativo D05; nueve composiciones visuales aprobadas; prototipos HTML/ZIP; contrato de navegación de ensayo; catálogo de componentes (13 familias); informes de auditoría AUD-G1-02/03 (el informe AUD-G1-01, sus CSV, el script de QA y los prototipos de integración citados no están incluidos en este paquete; ver `WEB_G1_REVIEW_01_INFORME.md`).

**No existe como producto validado:** un sitio productivo completo que implemente las nueve páginas con navegación, formulario y traducciones operativos; pruebas browser certificadas a 320/375/390/768/1024/1440 px y zoom 200 %; verificación WCAG y SEO del build final; paridad editorial completa de salida compilada. La aprobación de las maquetas no certifica estas funciones.

## 3. Jerarquía de documentación
- **D03 V1.22:** fuente vinculante del copy, estructura editorial, CTA, especialidades, referencias, catálogos y condiciones de publicación. Ante discrepancias, no tomar el texto del prototipo como fuente.
- **D04 V2.4:** arquitectura y contratos de modelos, rutas, build, integración de estudios, calidad y gates.
- **D05 V4.12:** tokens, composición, patrones, decisiones visuales y versiones de las nueve maquetas.
- **AUD-G1-02:** contrato de navegación y catálogo de componentes, material de soporte para implementación; **AUD-G1-03:** limitaciones y pendientes de QA.
- **Maquetas aprobadas:** evidencia visual de referencia, no templates ni código final obligatorio.

Las nuevas versiones D03/D04/D05 reproducen íntegramente las versiones previas y añaden una adenda de traspaso. No se han reescrito secciones anteriores. Las anotaciones históricas que digan «G1 pendiente» deben interpretarse con el acta de estado vigente; el gate sigue pendiente de ratificación.

## 4. Mapa del sitio
Nueve páginas por idioma: Inicio; Capacidades; Infraestructuras e instalaciones; Sistemas energéticos; Automatización y control; Sectores; Proyectos y experiencia; Sobre BAFRAS; Contacto. Menú principal de seis destinos: Inicio, Capacidades, Sectores, Proyectos y experiencia, Sobre BAFRAS y Contacto; las tres especialidades son subrutas de Capacidades. Prefijos de idioma `/es/`, `/ca/`, `/en/`, `/de/` y slugs explícitos. La primera salida puede implementarse en ES, pero G4 requiere traducciones revisadas conforme al alcance del D04.

## 5. Arquitectura obligatoria
Python 3 + Pydantic v2 + Jinja2 para generación estática; CSS modular y JavaScript nativo progresivo. Contenido estructurado por idioma, validado antes de renderizar; layouts y componentes compartidos; rutas y metadatos explícitos; salida `dist/` reproducible. No adoptar React, Astro, CMS, SPA, base de datos ni API de simulación por defecto. No acoplar el build a motores de cálculo.

Modelos conceptuales: `Page`, `Section`, `Media`, `Experience`, `StudyPublication`, `DownloadableResource`; los catálogos 0/1/N deben resolverse desde datos publicados válidos. `Experience` distingue proyecto BAFRAS y experiencia previa de fundador.

## 6. Sistema visual
Paleta: pino `#0E2B25`, acento `#1A7A5A`, papel `#F7F5F0`, arena `#ECE8DD`, línea `#D8D2C3`; tipografía Inter. Reconstruir las composiciones aprobadas de forma responsive. Unificar shell (header/footer), CTA, tarjetas y navegación sin arrastrar duplicidades de los prototipos de ensayo.

## 7. Contacto y recursos
Contacto V2: `info@bafras.com` (operatividad pendiente de verificar), `+34 610 903 179` (`tel:+34610903179`), formulario con nombre, empresa opcional, correo y consulta. No habilitar envío hasta integrar endpoint/servicio, privacidad y antispam con pruebas de extremo a extremo. Sin PDFs ficticios ni estudios sin permisos. En sectores, cero catálogos: sin CTA; uno: descarga directa; dos o más: selector accesible.

## 8. Hallazgos de auditoría y asignación correcta
- **G1-001 navegación:** contrato documental disponible; implementar shell único y probar enlaces/menú en G2/G3. Las copias integradas de ensayo conservan duplicidades.
- **G1-002 responsive:** 0/36 pruebas de navegador certificadas por bloqueo del entorno en AUD-G1-03. WEB-G1-REVIEW-01 midió desbordamiento horizontal de las maquetas a 320/375/390/768/1024/1440 px (59/60 sin desbordamiento; Sobre BAFRAS V1 desborda a 320 px); no equivale a revisión visual, teclado, zoom ni WCAG. Ejecutar la matriz completa sobre la implementación en G3/G4, no asumir éxito.
- **G1-003 componentes:** 13 familias documentadas; ratificar catálogo en acta G1 y construir componentes en G2/G3.
- **G1-004 editorial:** 212 fragmentos candidatos; 134 coincidencias normalizadas y 78 por clasificar (no equivalen a 78 errores). Verificar bloques D03↔salida final y corregir divergencias reales.

## 9. Plan de trabajo inicial
1. Inventariar repositorio y crear baseline de tests (G0/G2).
2. Ratificar formalmente G1 y el catálogo, con verificaciones de implementación diferidas explícitamente.
3. Implementar modelos Pydantic v2, rutas, build Jinja2 y estructura de contenido.
4. Implementar header/footer y tokens; construir una vertical funcional Inicio + una capacidad + Contacto (G3).
5. Integrar nueve páginas, catálogo de recursos, atribuciones, SEO/i18n y formulario.
6. Ejecutar pruebas responsive 320/375/390/768/1024/1440 y zoom 200 % (D05 §12.5, CA-C02-10), teclado, WCAG, enlaces, copy, seguridad, derechos, traducciones y despliegue (G4).

## 10. Criterios de aceptación del desarrollo
Build determinista, sin rutas rotas ni contenido draft publicado; copia editorial conforme a D03; composición conforme a D05; navegación funcional sin duplicados; sin overflow ni errores de interacción en los seis anchos de D05 §12.5 (320/375/390/768/1024/1440) y con zoom 200 %; accesibilidad WCAG 2.2 AA como objetivo validado; idiomas revisados; privacidad, derechos y contacto operativo antes de publicar. No marcar una prueba como aprobada si no se ha ejecutado.

## 11. Gobierno y límites
El diseño está congelado como referencia; los cambios visuales requieren incidencia con evidencia y aprobación. Las comprobaciones diferidas son deuda de verificación, no deuda de diseño. La dirección debe aprobar expresamente el cierre G1 antes del refactor productivo, como exige D04 §8. El presente paquete **no suplanta esa decisión**.
