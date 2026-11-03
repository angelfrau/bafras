# BAFRAS ENGINEERING — DOCUMENTO 04
## Arquitectura de producto y software · V2.4 (cuerpo V2.0 + adendas §11–§14) · 03/11/2026

**Estado:** especificación consolidada aprobada en sus decisiones principales; detalles de implementación sujetos a validación del repositorio. **Fuente editorial única:** Documento Maestro 03 Definitivo (vigente V1.22). **Documento complementario sin solapamientos:** Documento 05 (sistema visual y UX/UI; vigente V4.12; la redacción original de esta cabecera citaba V2.0). Ambos sustituyen las versiones previas 04/05 como documentación operativa; no se mantienen arquitecturas alternativas activas.

## 1. Propósito, alcance y decisiones vinculantes

La web de BAFRAS es un producto corporativo B2B, editorial y demostrador técnico, extensible hacia estudios, visualizaciones y herramientas de ingeniería. Debe ser rápida, accesible, multilingüe y mantenible por un equipo pequeño.

**Decisiones ratificadas:** (D01) reutilizar identidad visual real; (D02) **Python + Jinja2** como único generador principal de HTML estático, con CSS modular y JavaScript progresivo; (D03) separar web corporativa de motores Python; (D04) **diseño visual aprobado ANTES de refactorizar**; (D05) contenido editorial aprobado del Documento 03 sin reescrituras implícitas; (D06) incorporar en el futuro **dos estudios realizados por BAFRAS** que ya generan gráficos, informes HTML y tablas, previa preparación de sus exportadores y validación de publicación. Astro no forma parte del stack previsto. No introducir CMS, SPA, React, base de datos, API de simulación o framework CSS sin necesidad concreta.

**Orden obligatorio:** inspección de repositorio/identidad → diseño visual y contratos de componentes → aprobación de prototipos → refactorización incremental → publicación. Se permite trabajo de investigación, pruebas aisladas y prototipos desechables antes de aprobar diseño; **no** migrar el sitio productivo antes del gate de diseño.

## 2. Límites de responsabilidades

| Capa | Responsable | No debe hacer |
|---|---|---|
| Contenido | Archivos estructurados por idioma; referencia Documento 03 | Definir CSS o ejecutar simulaciones |
| Validación y build | Python 3 + Pydantic v2 + Jinja2 | Almacenar copy en plantillas o crear clases por tarjeta |
| Estructura HTML | Layouts y partials Jinja2 | Decidir autoría, atribución o autorización de publicación |
| Estilo | CSS/tokens existentes normalizados | Contener datos o lógica de negocio |
| Interactividad | JavaScript nativo, progressive enhancement | Ejecutar Python en el navegador o incluir secretos |
| Motores de estudios | Repositorios/software Python propios | Depender de rutas o CSS de la web |
| Exportación de estudios | Adaptador por estudio → paquete de publicación versionado | Forzar un esquema universal de resultados físicos |
| Cálculos online futuros | API independiente (FastAPI solo cuando se necesite) | Acoplar el build web al ciclo de vida del motor |

## 3. Arquitectura de información

Seis entradas de navegación: Inicio; Capacidades (índice y tres especialidades); Sectores; Proyectos y experiencia; Sobre BAFRAS; Contacto. Nueve páginas editoriales por idioma ES/CA/EN/DE, más legales y páginas de error. El Documento 03 define copy, jerarquías, alcance comercial y CTA. Las futuras **fichas individuales de proyectos BAFRAS** son rutas adicionales, no sustituyen ni alteran la arquitectura editorial de las nueve páginas. El índice de proyectos podrá combinar referencias verificadas de experiencia profesional previa y proyectos contratados/desarrollados por BAFRAS, siempre con etiquetas diferenciadas.

Rutas con prefijo `/es/`, `/ca/`, `/en/`, `/de/`, identificador de página estable y slugs localizados explícitos; enlaces equivalentes, canonical, hreflang, sitemap, robots y metadatos por idioma. No indexar páginas incompletas ni traducciones automáticas sin revisión. Si una ficha no existe en un idioma, no generar enlaces ficticios ni hreflang a una traducción inexistente.

## 4. Modelo editorial mínimo y extensible

- `Page`: `id`, `locale`, `slug`, `status`, `seo`, `hero`, `sections`, `related_pages`.
- `Section`: `id`, `kind`, `content`, `media_refs` con variantes de presentación limitadas y documentadas. No inventar una clase por tipo de tarjeta.
- `Media`: `id`, `path`, `alt_by_locale`, `rights`, `publication_status`, `caption`.
- `Experience`: `id`, `kind` (`bafras_project` o `founder_previous`), `attribution`, `scope_verified`, `client_permission`, `media_permission`, `status`.
- `StudyPublication`: `id`, `project_id`, `title_by_locale`, `summary_by_locale`, `version`, `published_at`, `methodology`, `limitations`, `assets`, `visibility`, `permission_status`.

Los modelos Pydantic v2 validan archivos YAML/JSON/Markdown con metadatos, no diccionarios sueltos en lógica de dominio. El build falla si faltan campos públicos, existen referencias a archivos ausentes, enlaces internos inválidos, duplicidad de rutas o contenidos `draft` publicados. **No crear un CMS universal ni imponer a todos los estudios un modelo físico único.** Las plantillas no contienen textos editoriales, salvo etiquetas de interfaz internacionalizadas.

## 5. Estructura objetivo (adaptable tras inspección del código)

```text
bafras-web/
  pyproject.toml
  src/bafras_web/
    build.py                 # compilación reproducible
    models.py                # contratos editoriales mínimos
    content.py               # lectura/validación
    routes.py                # rutas e i18n
    seo.py                   # metadata, sitemap, hreflang
    templates/
      layouts/base.html
      components/            # partials y macros compartidos
      pages/                 # composiciones por tipo de página
  content/{es,ca,en,de}/
  content/projects/          # referencias y atribuciones
  content/studies/           # manifiestos de publicación
  assets/{css,js,images,diagrams}/
  public/studies/            # salidas publicables generadas, no fuentes privadas
  tests/
  dist/                      # artefacto generado; no editar a mano
```

Los nombres y carpetas son **objetivo lógico**, no una orden de reestructuración masiva. Priorizar cambios pequeños, revisables, tests y paridad con el diseño aprobado. Extraer componentes solo cuando se repitan o resuelvan un problema real.

## 6. Contrato de publicación para los dos estudios BAFRAS existentes

**Hecho comunicado:** hay dos softwares de estudios desarrollados por BAFRAS que ya producen gráficos, informes HTML y tablas. **No se dispone aquí de sus repositorios ni esquemas**, por lo que NO se presupone tecnología concreta de gráficos, estructura interna, temática o permiso de difusión.

**Objetivo:** modificar cada software para producir un **paquete de publicación desacoplado** de la web. No modificar sus motores de cálculo para ajustarse al frontend. Incorporar un adaptador/exportador por software y, si procede, una pequeña librería compartida de manifiestos, sin acoplamiento bidireccional.

**Paquete mínimo por estudio:**

```text
study-export/<study-id>/<release>/
  manifest.json              # identidad, versión, proyecto, procedencia, derechos
  summary.es.md              # resumen editorial público revisado
  assets/                    # SVG/PNG/WebP, HTML sanitizado o fragmentos, CSS aislado
  tables/                    # CSV o JSON con unidades, columnas y semántica
  reports/                   # PDF o HTML autocontenido, si autorizado
  data/                      # series agregadas/anonimizadas opcionales
```

`manifest.json` debe contener `schema_version`, `study_id`, `project_id`, `release`, `generated_at`, `title`, `description`, `source_tool`, `artifacts[]` (tipo, ruta, título, idioma, MIME, dimensiones/unidades si procede), `data_classification`, `permissions`, `publication_status` y `methodology_reference` cuando aplique. **Los resultados técnicos mantienen esquemas específicos por estudio**; el manifiesto solo describe y permite publicar artefactos.

**Flujo:** motor de estudio → exportador específico → paquete inmutable → validación de permisos/datos/rutas/HTML → revisión editorial → incorporación al repositorio de web → build estático → página de proyecto con visualizaciones. Para gráficos interactivos, preferir JSON/CSV + visualizador JS independiente del motor. Para informes HTML, preferir exportar fragmentos semánticos controlados o mostrar documento autocontenido en contexto aislado; no inyectar HTML arbitrario sin sanitización ni confiar en scripts externos. Para tablas, usar HTML accesible y ofrecer CSV cuando tenga sentido. Gráficos raster/SVG deben disponer de alt, descripción, unidades y fuente.

**Regla de seguridad:** nada de datos confidenciales de clientes, CUPS, consumos individualizados, información personal, credenciales o detalles protegidos sin revisión y permiso. Distinguir proyecto propio BAFRAS de experiencia anterior de fundadores; las dos nuevas fichas se etiquetarán `bafras_project` **tras verificar atribución y autorizaciones**. No prometer resultados, ahorro o precisión que los estudios no documenten.

**Integración incremental:** V1 mostrar imagen/figura + interpretación + informe descargable; V2 tablas y gráficos interactivos precalculados; V3, solo con caso de uso real, API FastAPI separada para cálculo bajo demanda, con autenticación/cuotas/validación y aislamiento de procesos.

## 7. Contacto, seguridad y despliegue

Formulario de nombre, empresa opcional, email y mensaje. Entrega segura a `info@bafras.com` por función serverless/endpoint mínimo; credenciales solo en servidor, validación doble, antispam, límites, manejo de errores, SPF/DKIM/DMARC cuando proceda. Sin CRM ni base de datos de consultas V1. La política de privacidad debe identificar titular jurídico real. Hosting estático con HTTPS y despliegue reproducible; proveedor concreto pendiente. Auditoría de dependencias, cabeceras y CSP compatibles con los informes embebidos.

## 8. Calidad, pruebas y gates

**Gate G0 — Baseline:** repositorio real inventariado, rutas, CSS, paleta, fuentes, assets, JS y comportamiento actuales; captura de escritorio/móvil.

**Gate G1 — Diseño aprobado (OBLIGATORIO ANTES DEL REFACTOR):** conforme a la decisión de dirección B02-PREP-01, requiere nueve wireframes completos, uno por página, en escritorio y móvil y con trazabilidad de todos los bloques editoriales del Documento 03; tres maquetas completas de alta fidelidad de **Inicio, Infraestructuras e instalaciones y Contacto**; y maquetas detalladas de los módulos visuales singulares de las otras seis páginas. Requiere además catálogo aprobado de componentes y sus variantes/estados, especificación del sistema visual, revisión visual global de las nueve páginas sin decisiones estéticas fundamentales pendientes y aprobación expresa de dirección registrada documentalmente. El Documento 05, §8, concreta los entregables y criterios visuales de este mismo contrato.

No se exigen nueve prototipos completos e independientes de alta fidelidad cuando las páginas puedan reconstruirse inequívocamente mediante los patrones y variantes aprobados. La aprobación G1 autoriza planificar la implementación; cualquier intervención productiva requiere su autorización correspondiente y sigue sujeta a los gates posteriores. G1 no acredita por sí mismo recursos gráficos, referencias profesionales, datos técnicos, formulario ni requisitos legales preparados para publicación. Esta consolidación documental no inicia G1 ni lo declara completado.

**Gate G2 — Arquitectura lista:** contratos de contenido y rutas, build de prueba, tests de validación, plan de migración incremental y estrategia de rollback.

**Gate G3 — Vertical funcional:** Inicio, capacidad y Contacto en Jinja2, paridad de copy y diseño, formulario probado extremo a extremo.

**Gate G4 — Publicación:** nueve páginas ES, traducciones revisadas, derechos, legales, SEO, WCAG 2.2 AA como objetivo, móvil y rendimiento validados, sin referencias no verificadas.

**Gate G5 — Estudios:** exportador de cada uno de los dos softwares validado con un paquete real, sin datos privados, y fichas públicas aprobadas. Este gate puede ejecutarse después del lanzamiento; no bloquear el sitio corporativo.

## 9. Decisiones abiertas, explícitamente no bloqueantes

Proveedor de hosting, proveedor transaccional, dominio canónico, estrategia de analítica respetuosa, tecnología JS de gráficos y detalles de los dos estudios. La publicación sí requiere resolver permisos, privacidad, licencias y correo. No definir de antemano FastAPI, base de datos ni sistema de colas para estudios estáticos.

## 10. Responsabilidades y próximos entregables

1. Diseño/branding: inventario de identidad real y maquetas; propietario del Documento 05.
2. Editorial/comercial: trazabilidad exacta de Documento 03 y revisión de fichas de los dos estudios.
3. Arquitectura/software: contratos mínimos Pydantic/Jinja2, plan de migración y tests; sin cambios productivos antes de G1.
4. Responsables de estudios: entregar estructura de exportación y muestras anonimizadas; implementar adaptadores posteriormente.
5. Dirección BAFRAS: aprobar G1 y publicación de cada proyecto.

**Criterio rector:** diseño definido antes de refactorizar; una única fuente de copy; una única arquitectura web; una interfaz de publicación independiente para cada motor de ingeniería; crecimiento sin abstracciones anticipadas.


---
## 11. SEC-CAT-01 — Contrato de catálogos PDF sectoriales · 03/11/2026
**Estado:** especificación de diseño/arquitectura, no implementación productiva; sometida a G1/G2. Compatible con Python + Pydantic v2 + Jinja2 y generación estática. No añade CMS, BD, API ni backend de descargas.

### 11.1 Datos y límites
Introducir `DownloadableResource` como modelo Pydantic v2 mínimo reutilizable, **solo si no existe contrato equivalente al inspeccionar el repositorio**. Campos propuestos: `id` (estable y único), `sector_id` (referencia válida a uno de los seis IDs D03), `title` (título editorial), `language` (`es|ca|en|de`), `file_path` (ruta relativa de origen), `version` (identificador documental), `publication_status` (`draft|published|archived`), `updated_at` (fecha opcional ISO). No duplicar `Media` si el modelo existente ya cubre documentos con los metadatos y reglas necesarias; preferir extensión mínima o composición. No introducir entidades por tarjeta.

**Invariantes:** IDs únicos; cada PDF pertenece a un sector existente; como máximo una versión `published` por pareja `(catalog_id, language)`; un `sector_id` puede agrupar varios `catalog_id`; idioma real obligatorio; rutas relativas bajo raíz de documentos autorizada, sin `..`, sin esquemas URL ni escape por symlinks; extensión `.pdf`, fichero regular existente y PDF verificable por firma o parser en gate de publicación; ningún recurso `draft/archived` entra en `dist`. Evitar exponer rutas de origen, información privada o documentos sin autorización. Comprobar también licencias y vigencia editorial.

### 11.2 Resolución y build
1. Cargar manifiesto YAML/JSON de recursos en modelos Pydantic v2, sin diccionarios sueltos en dominio.
2. Validar esquema, unicidad, sector, idioma, estado y rutas. Los errores estructurales de recursos declarados publicables **fallan el build**; los borradores se ignoran en publicación, aunque deben pasar validación básica de esquema.
3. Para cada sector y locale, seleccionar `published` del mismo idioma. Si no existe, aplicar **solo** una política de fallback explícita definida editorialmente; por defecto, no mostrar enlace.
4. Comprobar existencia, tipo PDF y permiso de publicación del seleccionado. No publicar enlaces rotos; una entrada marcada `published` con archivo inexistente debe producir fallo de build, no desaparición silenciosa.
5. Copiar PDF a ruta pública determinista y estable, por ejemplo `dist/downloads/sectors/<sector_id>/<language>/<filename-versionado>.pdf`, con URL relativa al prefijo de despliegue, sin rutas absolutas del equipo de desarrollo. La versión en nombre permite caché segura; mantener enlaces estables mediante manifiesto y regeneración del sitio.
6. Renderizar macro Jinja2 reutilizable con `href` URL-encoded, etiqueta localizada, idioma explícito y atributo `download` opcional; el navegador puede abrir PDF según configuración. No JS necesario. Validar enlaces de `dist` tras copiar y en pruebas de despliegue/base path.
7. Tests: recursos 0/1/varios, idioma coincidente/no coincidente, fallback permitido/no permitido, archivo ausente, borrador, duplicados, traversal/symlink, PDF corrupto, título largo, enlaces relativos en despliegue y cambio de versión.

### 11.3 Manifiesto ilustrativo (NO recursos existentes)
```yaml
resources:
  - id: catalogo-turismo-es
    sector_id: turismo-terciario
    title: Catálogo de servicios de ingeniería para turismo y terciario
    language: es
    file_path: content/downloads/turismo-es-v1.pdf
    version: '1.0'
    publication_status: draft
    updated_at: null
```
Este ejemplo **no se debe cargar como catálogo publicable ni enlazar** hasta disponer del archivo real y de autorización.

### 11.4 Internacionalización, seguridad y accesibilidad
La interfaz admite ES/CA/EN/DE; la disponibilidad de PDF es independiente por idioma. Nunca fabricar traducciones. Si se ofrece PDF en idioma alternativo, mostrar idioma real y, si procede, `hreflang` del recurso; `hreflang` de páginas no debe apuntar a PDF. Título del enlace comprensible con contexto de sector, foco visible y tamaño táctil adecuado. PDF final revisado en accesibilidad, metadatos, permisos y ausencia de información sensible. No incluir descargas en sitemap de páginas por defecto; decidir indexación documental según política SEO. No hay tracking obligatorio.

### 11.5 Gates y trazabilidad
**G1:** aprobar wireframe SEC desktop/móvil y estados de componente `VIS-SEC-01`. **G2:** validar contrato y tests de generación. **G4:** solo PDF autorizados y verificables. Los seis sectores pueden publicarse sin ningún catálogo; los documentos futuros no alteran las nueve páginas. No iniciar refactor productivo por esta adenda.


---
## 12. SEC-CAT-02 — Varios catálogos por sector y selector accesible · 03/11/2026
**Estado:** contrato actualizado, pendiente de G1/G2. **Precedencia:** corrige el cardinal de §11.1 sin alterar el stack estático.

### Modelo y resolución
- Añadir `catalog_id` (identidad estable de la línea documental o actividad) al recurso descargable. Conservar `id` como identidad del archivo/versionado, `sector_id` como agrupación y `language` como idioma del PDF. `title` será el título específico del catálogo, no necesariamente el título del sector. Puede añadirse `display_order` solo si se necesita un orden editorial explícito.
- **Cardinalidad:** sector 0..N catálogos; catálogo 0..N traducciones, **a lo sumo una versión publicada por `(catalog_id, language)`**. Validar que cada `catalog_id` pertenezca a un único sector y que las combinaciones no sean ambiguas. No restringir Industria a una lista fija de subsectores.
- Por locale, resolver documentos elegibles: versión del mismo idioma primero; alternativa lingüística solo con autorización editorial explícita, sin duplicar dos idiomas del mismo `catalog_id` salvo decisión expresa. Validar existencia y firma PDF, permisos, rutas y unicidad como en §11.
- Presentación: `0` elegibles → no CTA; `1` → enlace directo; `2+` → control desplegable nativo `<details><summary>` y enlaces `<a>` reales a cada PDF, **sin JavaScript**. La lista no se renderiza a partir de borradores.
- Jinja2 recibe una colección tipada y resuelta por sector/locale, nunca lee manifiestos ni hace `if` sobre rutas locales. No modificar HTML para añadir un catálogo.
- URL pública estable por recurso: `downloads/sectors/<sector_id>/<catalog_id>/<language>/<version>.pdf` (nombre de archivo sanitizado y URL relativa a base path). Las rutas y versiones se validan antes de copiar a `dist`.
- Pruebas adicionales: 0/1/2/10 catálogos, cambio de cardinalidad, mismo catálogo con ES/EN, fallback, títulos largos, teclas Enter/Espacio en `<summary>`, foco en enlaces, 320 px, PDF inexistente y enlaces post-build. No introducir CMS, backend ni base de datos.

### Ejemplo conceptual, sin PDF existente
```yaml
resources:
  - id: madera-es-v1
    catalog_id: industria-madera-muebles
    sector_id: industria-logistica-agroindustria
    title: Ingeniería para fabricación de muebles y madera
    language: es
    file_path: content/downloads/industria/madera-es-v1.pdf
    version: '1.0'
    publication_status: draft
  - id: lavanderias-es-v1
    catalog_id: industria-lavanderias
    sector_id: industria-logistica-agroindustria
    title: Ingeniería para lavanderías industriales
    language: es
    file_path: content/downloads/industria/lavanderias-es-v1.pdf
    version: '1.0'
    publication_status: draft
```
**Nota:** ejemplos de estructura, no archivos existentes.


---
## 13. CO-V2 — Contrato técnico de Contacto aprobado · 03/11/2026
**Estado:** diseño C04-CO-V2 aprobado por dirección; implementación, pruebas y publicación pendientes. No cambia el stack Python 3 + Pydantic v2 + Jinja2 ni la generación estática.

- **Configuración tipada:** representar los datos públicos de contacto como valores de contenido/configuración validados, no duplicar literales en plantillas: `email = info@bafras.com`, `phone_display = +34 610 903 179`, `phone_e164 = +34610903179`. Validar que el número normalizado y el mostrado correspondan; no exponer estos datos como secretos.
- **Renderizado:** `mailto:info@bafras.com` y `tel:+34610903179` mediante enlaces semánticos accesibles en CO-03; repetir contacto directo en el pie común conforme a D05. Evitar enlaces `tel:` vacíos y datos de contacto ficticios en otros idiomas.
- **Formulario:** mantener cuatro campos (nombre, organización opcional, correo, consulta), validación cliente/servidor, protección antispam, límites y notificación a `info@bafras.com`. Mientras no exista servicio probado y política legal real, no permitir envío ni mostrar confirmaciones ficticias. El teléfono publicado **no** se añade como campo requerido.
- **i18n:** mismos datos públicos en ES/CA/EN/DE; localizar etiquetas, ayuda, errores y textos legales, no traducir ni alterar email o teléfono.
- **Pruebas de aceptación:** enlace telefónico correcto, enlace mailto correcto, presencia en bloque de contacto y footer, foco de teclado, responsive 320/390/768/1440 px (matriz completa en §14: más 375 y 1024 px y zoom 200 %), comprobación de no desbordamiento, ausencia de submit operativo en maqueta, y pruebas E2E de entrega antes de producción.
- **Gobernanza:** D03 controla el contenido, D04 este contrato, D05 el diseño visual. Aprobación de Contacto completa las **nueve aprobaciones visuales**, pero no implica cierre automático del gate G1: faltan verificaciones transversales y entregables exigidos por la arquitectura.

---
## 14. G1-HANDOFF-01 — Traspaso de diseño a implementación · 03/11/2026
**Precedencia:** esta sección concreta la distribución de verificaciones entre gates sin eliminar requisitos de diseño del §8. Las nueve páginas tienen composición aprobada. Se propone a dirección formalizar el cierre G1 tras aceptar el catálogo de componentes y la documentación de excepciones. Hasta su aprobación expresa, el gate se registra como **pendiente de ratificación**, no como aprobado automáticamente.

**Evidencias disponibles:** D03 V1.22, D05 V4.12, nueve prototipos aprobados, contrato de navegación AUD-G1-02 y catálogo de 13 familias de componentes; auditorías AUD-G1-01/02/03. Los prototipos de integración de AUD-G1-02/03 son material de ensayo, no código a migrar literalmente.

**Criterios diferidos a G2–G4:** navegación final sin duplicados, pruebas de menú y teclado, viewport 320/390/768/1440 (más 375 y 1024 px y zoom 200 %, exigidos por los criterios aprobados de D05 §12.5 y CA-C02-10), ausencia de overflow, WCAG 2.2 AA, verificación literal D03↔salida compilada, enlaces internos, SEO/i18n y pruebas de formulario. Estos controles no se dan por superados; deben figurar como tests o criterios de aceptación del desarrollo.

**Arranque controlado:** inspeccionar repositorio existente; crear baseline y tests; implementar rutas, modelos Pydantic v2, build Jinja2, layout compartido y una vertical inicial; extender a las nueve páginas con paridad visual/editorial; no publicar recursos no verificados. No cambiar el stack ni crear backend propio por conveniencia.

**Decisión de autorización:** la aceptación de este documento como especificación no sustituye el acta expresa de cierre G1 exigida por §8.

**Nota de control documental WEB-G1-REVIEW-01 (03/11/2026):** de las evidencias citadas en este apartado, el paquete `docs/project_v02/` no contiene el informe AUD-G1-01, los prototipos de integración de AUD-G1-02/03, los CSV `AUD-G1-03_Auditoria_Estatica.csv` y `AUD-G1-03_Cotejo_Editorial.csv` ni el script `ejecutar_qa_browser_local.py`. Constan AUD-G1-02 (contrato de navegación y catálogo) y AUD-G1-03 (informe y plan de cierre). Esta nota no altera ninguna decisión; véase `WEB_G1_REVIEW_01_INFORME.md`.
