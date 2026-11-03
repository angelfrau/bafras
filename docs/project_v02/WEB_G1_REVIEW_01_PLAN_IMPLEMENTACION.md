# WEB-G1-REVIEW-01 · Plan de implementación incremental

**Fecha:** 03/11/2026. **Naturaleza:** propuesta de secuencia para dirección y equipo técnico. **No inicia ninguna intervención productiva.** Cada intervención requiere autorización expresa; WEB-G2-01 y siguientes requieren además el acta G1 firmada (D04 §1 y §8).

**Marco fijo:** Python 3 + Pydantic v2 + Jinja2, generación estática en `dist/`, CSS modular y JavaScript nativo progresivo (D04 §1, §2). Sin React, Astro, SPA, CMS, base de datos ni backend propio. La única pieza de servidor prevista es el envío del formulario (D04 §7), mediante el proveedor que decida dirección (WGR-033).

## 0. Ajustes recomendados a la secuencia propuesta

1. **Paso previo de gobierno (G1-ACTA, no técnico):** firmar el acta G1 registrando las excepciones WGR-050 (diagramas), WGR-051 (normalización de tokens en G2-02), WGR-052 (regla de contraste) y WGR-063 (complemento del catálogo). Sin este paso solo puede ejecutarse WEB-G2-00.
2. **WEB-G2-00 puede empezar antes de G1:** es inspección y planificación sin cambios productivos, permitido por D04 §1 («investigación, pruebas aisladas»).
3. **Dividir WEB-G3-01 en G3-01a (renderizado) y G3-01b (formulario de extremo a extremo).** D04 §8 G3 exige un formulario probado de extremo a extremo, y eso depende de la elección de proveedor (WGR-033), que hoy D04 §9 considera no bloqueante. La división evita que una decisión operativa bloquee la vertical visual.
4. **Convivencia sin corte:** el sitio actual (`index.html` en la raíz) se mantiene publicado y sin cambios hasta el cambio de publicación de G4. El nuevo build genera solo `dist/`. El rollback consiste en no promover `dist/`. Esta estrategia satisface el requisito de rollback de D04 §8 G2 sin infraestructura adicional.

## 1. Dependencias de decisión por intervención

| Decisión (incidencia) | Necesaria antes de |
|---|---|
| Acta G1 firmada con excepciones (WGR-090, 050, 051, 052, 063, 072) | WEB-G2-01 |
| Trabajo previo del repositorio confirmado o archivado (WGR-036) | WEB-G2-01 |
| Registro de rutas ES ratificado (WGR-031) | WEB-G2-01 (cierre) |
| Logo maestro (WGR-060); pie único (WGR-054); cabecera (WGR-055); créditos de imagen (WGR-061); selector (WGR-062) | WEB-G2-02 (cierre) |
| Copy de Contacto (WGR-020, 021, 022); etiquetas H05 (WGR-025); SEO de cuatro páginas (WGR-040) | WEB-G3-01a |
| Estados del formulario (WGR-056); proveedor de envío y hosting (WGR-033) | WEB-G3-01b |
| Etiquetas de atribución (WGR-023); variante de PE sin referencias (WGR-026) | WEB-G3-02 |
| Idiomas de lanzamiento (WGR-032); dominio (WGR-039); P0 de publicación (WGR-080…084) | WEB-G4-01 |

## 2. Intervenciones

### WEB-G2-00 · Baseline técnico y plan de migración

- **Alcance:** inventario del repositorio actual (rama, cambios sin confirmar, assets sin seguimiento); registro de la evidencia G0 existente (B01 y las 86 capturas de `B02_Auditoria_Visual_BAFRAS/capturas/`); propuesta del registro de rutas ES, de la raíz `/`, del 404 y del tratamiento de los enlaces `#/…` heredados; ubicación productiva de assets; plan de ramas y rollback; esqueleto de contratos de G2-01 para revisión.
- **Dependencias:** ninguna. Puede ejecutarse antes de G1.
- **Archivos previstos:** solo documentación (`docs/project_v02/WEB_G2_00_BASELINE.md` o similar). Ningún cambio en `index.html`, `css/`, `js/`, `tests/` ni `tools/`.
- **Entregables:** baseline G0 con hashes; registro de rutas propuesto; plan de migración y rollback; lista de dependencias Python con versión.
- **Criterios de aceptación:** `git status` documentado y aprobado por el usuario; registro de rutas sin colisiones y alineado con D03 03.J §3.1; plan aprobado por arquitectura.
- **Pruebas:** `python -B tools/validate.py` y `pytest` actuales siguen pasando (no se tocan).
- **Cierra / avanza:** WGR-002 (localización de D01/D02), 003, 008, 031, 035, 036, 075.

### WEB-G2-01 · Modelos de contenido, validación y generador estático

- **Alcance:** paquete `src/bafras_web/` con `models.py`, `content.py`, `routes.py`, `seo.py` y `build.py` (D04 §5). Contratos mínimos: `Page`, `Section`, `Media` (con author, license, license_url, source_url, attribution_text, modifications), `Experience`, `DownloadableResource` (D04 §11–§12), y los que faltan para las nueve páginas: `SiteSettings` (correo, teléfono mostrado/E.164, datos legales opcionales), `NavItem`, `Sector`, `Person`, `UiStrings`, SEO por página. Contenido ES de las nueve páginas en `content/es/` con un fichero por página y bloques identificados con los IDs de D03 (H01…CO-04).
- **Formato de contenido:** YAML por mantenibilidad editorial. Es la única dependencia nueva (PyYAML) y está justificada. La alternativa sin dependencias es JSON.
- **Dependencias:** acta G1; WGR-036; registro de rutas de G2-00.
- **Archivos previstos:** `pyproject.toml` (dependencias fijadas y extra `dev`), `src/bafras_web/**`, `content/es/**`, `content/projects/`, `tests/test_models.py`, `tests/test_build.py`. Las pruebas heredadas que fijan el editorial antiguo se sustituyen; se conservan sus comprobaciones de recursos y enlaces (WGR-038).
- **Entregables:** `python -m bafras_web.build` genera `dist/` con las nueve rutas ES y una plantilla mínima (sin diseño todavía).
- **Criterios de aceptación:**
  - El build falla si falta un campo público, una referencia apunta a un archivo inexistente, hay rutas duplicadas, enlaces internos inválidos, contenido `draft` publicable o una imagen sin crédito exigible.
  - Ningún texto editorial está en las plantillas (D04 §4).
  - Dos builds consecutivos producen `dist/` idéntico (hash).
  - Con cero referencias o catálogos publicados no se renderiza ningún contenedor vacío.
- **Pruebas:** unitarias de modelos (válidos e inválidos); catálogos 0/1/2/10, idioma coincidente y no coincidente, archivo ausente, traversal (D04 §11.2 y §12); prueba de paridad D03 → contenido para los bloques cargados.
- **Cierra / avanza:** WGR-010, 030, 034, 037, 038, 073 (parcial).

### WEB-G2-02 · Shell, navegación y componentes compartidos

- **Alcance:** hoja de tokens derivada de las maquetas aprobadas y de `css/tokens.css` (colores, tipografía, contenedor, cortes, espaciado), **aprobada por Diseño antes de usarse** (WGR-051), con la regla de contraste WGR-052. Layout base, `SiteHeader` (C01, CA-01…CA-07), menú móvil, selector según WGR-062, migas (WGR-057), enlace de salto (WGR-058), `SiteFooter` único con correo y teléfono (WGR-054), logo maestro (WGR-060), y las macros comunes: `PageHero` (home/specialty/interior), `SectionHeading`, `ContentCard` (capability/technical-area/sector), `NeedList`, `DeliverableList`, `ContactBand`, `MediaFigure` con crédito, `ExperienceCard` y `FounderProfile`.
- **Complemento del catálogo AUD-G1-02 (WGR-063):** SectionHeading, NeedList, DeliverableList, rejilla de ámbitos con banda transversal, migas, enlace de salto y ficha VIS-PE-02.
- **Dependencias:** G2-01 y las decisiones de diseño de la tabla §1.
- **Archivos previstos:** `src/bafras_web/templates/layouts/base.html`, `templates/components/*.html`, `assets/css/{tokens,base,components,layout}.css`, `assets/js/nav.js` (mejora progresiva: menú y Escape). No se modifica el sitio actual.
- **Criterios de aceptación:**
  - Un solo shell para las nueve rutas, sin navegación duplicada.
  - El menú funciona sin JS (mejora progresiva) y con teclado (Tab, Shift+Tab, Enter, Espacio, Escape).
  - No hay valores de color ni tamaño fuera de tokens.
  - No hay desbordamiento a 320/375/390/768/1024/1440 px en una página de prueba con todos los componentes.
- **Pruebas:** HTML válido por parser; enlaces internos; desbordamiento y contraste con los scripts de `evidencias_WEB_G1_REVIEW_01/` adaptados a `dist/`; teclado manual registrado.
- **Cierra / avanza:** WGR-051…055, 057, 058, 060…063, 070 (parcial).

### WEB-G3-01a · Vertical funcional: Inicio, Infraestructuras e instalaciones y Contacto (renderizado)

- **Alcance:** las tres páginas de alta fidelidad (D05 §8.4) con contenido D03 íntegro y composición de D05 §23/§26 (Inicio V3, INF V2) y §47 (Contacto V2). El formulario se renderiza desactivado, con el correo y el teléfono como alternativa real (03.K §3 y D05 §47.1).
- **Dependencias:** G2-02; WGR-020, 021, 022, 025, 040.
- **Archivos previstos:** `content/es/{inicio,infraestructuras-instalaciones,contacto}.yaml`, `templates/pages/{home,specialty,contact}.html`, CSS de página si un patrón no es reutilizable.
- **Criterios de aceptación:**
  - Paridad literal con D03 sin cadenas ajenas a D03, salvo las etiquetas de interfaz aprobadas (WGR-027).
  - Las imágenes R24, R23, R22, R21, R03 y R18 llevan alt y crédito.
  - Inicio H06 sin tarjetas.
  - H1 único y title/meta por página.
  - Comparación visual con las maquetas aprobadas revisada y firmada por Diseño.
- **Pruebas:** paridad automática; desbordamiento a seis anchos; contraste; enlaces; teclado; capturas archivadas a 390 y 1440 px.

### WEB-G3-01b · Formulario de extremo a extremo

- **Alcance:** integración con el proveedor elegido (WGR-033); validación en cliente y servidor; antispam; límites; `From` del dominio y `Reply-To` del usuario; estados aprobados (WGR-056); copy de éxito y error decidido (WGR-020).
- **Dependencias:** G3-01a; WGR-033, WGR-056; texto de privacidad provisional aprobado por legal para entorno de pruebas.
- **Criterios de aceptación:** los criterios de 03.K.2 (L1241): recepción en `info@bafras.com`, respuesta posible mediante Reply-To, errores sin pérdida silenciosa y sin secretos en el cliente. Además, la prueba E2E mínima de D03 03.J §6.
- **Pruebas:** envío válido, campos obligatorios, correo inválido, fallo de red, error del servidor, doble clic, antispam, recepción real y anuncio accesible de estados.
- **Cierre del gate G3** (D04 §8): G3-01a + G3-01b.

### WEB-G3-02 · Integración de las seis páginas restantes

- **Alcance:**
  - Capacidades (V1, con etiqueta «Ejemplos de aplicación», WGR-028).
  - Sistemas energéticos (V2).
  - Automatización y control (V1).
  - Sectores (V3, con `DownloadableResource` y VIS-SEC-01/02, cero catálogos por defecto).
  - Proyectos y experiencia (V1, en la variante decidida en WGR-026 y con las etiquetas de WGR-023; plantilla de ficha sin generar fichas).
  - Sobre BAFRAS (V1, con texto y fichas de 03.K, WGR-024, y sin desbordamiento a 320 px, WGR-059).
- **Dependencias:** G3-01a; WGR-023, WGR-026.
- **Criterios de aceptación:** los de G3-01a aplicados a cada página; ninguna referencia, cifra, retrato ni PDF sin autorización en `dist`; build con 0, 1 y 2 catálogos de prueba fuera de `dist` publicable.
- **Pruebas:** paridad, seis anchos, contraste, enlaces, teclado y `<details>` con Enter/Espacio.

### WEB-G4-01 · QA, accesibilidad, paridad, recursos y preparación de publicación

- **Alcance:** matriz completa de D05 §12.5 y CA-C02-10 sobre `dist` (seis anchos, zoom 200 %, teclado, lector de pantalla); checklist WCAG 2.2 AA; paridad final; derechos y créditos por imagen; textos legales reales; SEO (canonical, sitemap con URLs publicables, robots, hreflang solo si hay más de un idioma); despliegue en staging con HTTPS y dominio decidido; plan de cambio desde el sitio actual.
- **Dependencias:** G3 cerrado; WGR-032, 039, 080…085.
- **Criterios de aceptación:** D04 §8 G4 y briefing §10; ninguna P0 abierta (D03 03.J §8, regla de salida); aprobación expresa de publicación por dirección.
- **Pruebas:** todas las anteriores, más respuestas HTTP 200/301/404 en staging, entregabilidad del correo y medición de rendimiento.

## 3. Pruebas transversales reutilizables

- **Desbordamiento y contraste:** `evidencias_WEB_G1_REVIEW_01/medir_desbordamiento.py` y `medir_contraste.py` usan solo Python estándar y el Chrome instalado. Deben adaptarse para leer `dist/` en lugar de las maquetas. No sustituyen la revisión humana.
- **Paridad editorial:** extraer el texto visible de `dist` y compararlo con los ficheros de contenido; compararlos a su vez con D03 por ID de bloque.
- **Enlaces:** parser estándar sobre `dist`, que falla ante cualquier destino interno inexistente o ancla ausente.

## 4. Riesgos de migración

| Riesgo | Mitigación |
|---|---|
| Perder trabajo sin confirmar del repositorio actual (WGR-036) | Confirmar o crear rama antes de G2-01 |
| Hosting estático (GitHub Pages) sirve la raíz y no `dist/` | Despliegue mediante workflow que publique `dist/` solo en G4, tras decidir WGR-039 |
| Enlaces externos a rutas `#/…` del sitio actual | Script mínimo en la nueva raíz que redirija los hashes conocidos a las nuevas URLs (G2-00 lo especifica) |
| Copiar CSS o JS de las maquetas con duplicidades | Prohibido por D05 §26.2 y AUD-G1-02; todo se implementa contra tokens y componentes de G2-02 |
| Imágenes CC BY-SA modificadas (recortes, WebP) sin aviso | Campo `modifications` y crédito obligatorio en `Media` (WGR-034) |
