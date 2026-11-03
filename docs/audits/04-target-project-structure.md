# 04 · Estructura objetivo y operación editorial

Propuesta para Python/Jinja2, no árbol creado durante esta auditoría. Principio: fuentes editoriales, plantillas, diseño y artefacto de publicación diferenciados; una sola fuente de verdad por dato. [Decisión](03-architecture-decision.md), [contratos](06-content-assets-model.md).

## Árbol objetivo

```text
bafras/
  src/
    content/
      entities/
        capabilities/infraestructura.json
        services/instalaciones-electricas.json
        sectors/hoteles.json
        projects/campus-uib.json
      locales/
        es/
          pages/home.json           también contacto, sobre, índices
          capabilities/infraestructura.json
          services/instalaciones-electricas.json
          sectors/hoteles.json
          projects/campus-uib.json
        ca/                         solo traducciones existentes/revisadas
        en/
        de/
      i18n/es.json                   etiquetas de interfaz; equivalentes revisados
      navigation.json               IDs, no copias de URLs y títulos
      legacy-routes.json            alias de hashes históricos
    media/
      manifest.json                 fuente de verdad de recursos
      originals/
        brand/
        home/
        capabilities/
        projects/
        team/
    templates/
      layouts/base.html             documento, lang y head
      layouts/detail.html           extensión opcional si evita repetición real
      pages/home.html
      pages/capability.html
      pages/service.html
      pages/sector.html
      pages/project.html
      pages/listing.html
      pages/about.html
      pages/contact.html
      partials/head.html
      partials/header.html
      partials/footer.html
      partials/brand-symbols.html
      partials/breadcrumbs.html
      components/cta.html
      components/media.html
      components/technical-metrics.html
      components/evidence.html
      components/related-links.html
    styles/
      tokens.css
      base.css
      layouts.css
      components.css
      pages.css
    scripts/menu.js
    scripts/form.js
    scripts/legacy-links.js
  public/
    CNAME                           dominio verificado; sin alteración accidental
    favicon.ico
    .nojekyll                       si lo requiere la publicación elegida
  tools/
    build.py                        orquestación, sin render duplicado en validación
    content.py                      lectura/contratos y estados
    routes.py                       resolver IDs/locale, alias, colisiones
    media.py                        variantes y manifiesto derivado
    validate.py                     ampliar sin perder controles útiles
  tests/
    test_content.py
    test_routes.py
    test_output.py
    test_media.py
    test_structure.py               adaptar contratos ligados al HTML antiguo
    browser/                        solo si se aprueba herramienta de navegador
  docs/
    audits/                         decisión y plan presentes
    architecture.md                 actualizar al ejecutar, no en esta auditoría
    content-authoring.md            receta editorial, sin duplicar modelos
    website-visual-assets.md         conservar procedencia histórica
  pyproject.toml
  requirements-dev.txt              Jinja2, pytest y Pillow fijados tras validación
  .github/workflows/pages.yml        solo al preparar despliegue autorizado
  dist/                             salida generada, no fuente editable
    index.html                      entrada/selector + compatibilidad de hashes
    404.html
    es/index.html
    es/capacidades/infraestructura/index.html
    assets/css/…
    assets/js/…
    assets/images/…                  variantes; originales no copiados por defecto
    sitemap.xml
    robots.txt
    CNAME
```

Los archivos de entidades contienen hechos compartidos, IDs y relaciones; los de locale contienen texto, slug, SEO y aprobación de cada idioma. No repetir magnitudes en Home, capacidad y proyecto: resolver una misma entidad. Las páginas genéricas usan `pages/`; las páginas de entidad se derivan de su tipo/estado, sin otro listado manual de rutas públicas. No crear directorios de contenido vacíos ni stubs publicables para aparentar cuatro idiomas completos.

En el piloto se añade una zona aislada sin mover los archivos operativos actuales. El árbol anterior es el destino final, no una orden de reorganizar todo al iniciar. El CSS puede copiarse en su orden actual a la salida antes de consolidarlo en otra fase.

## Responsabilidades del build

1. Cargar contenido y validar datos, estados, referencias, rutas y medios.
2. Derivar un índice interno `(entity_id, locale) → URL`, navegación y relaciones. La URL incluye slug localizado y `/` final; se genera su `index.html` real.
3. Resolver recursos por ID, preparar variantes y renderizar templates con errores estrictos.
4. Copiar solo recursos públicos necesarios; generar head SEO, sitemap, robots, 404 y mapa de compatibilidad.
5. Validar `dist/`: enlaces, anclas en el documento correcto, assets, dimensiones, traducciones y metadatos. Publicar solamente el artefacto que pasó validación.

Los nombres `build.py`, flags y archivos futuros son una interfaz propuesta, no comandos que funcionen hoy. Contrato esperado tras implementación: `python tools/build.py --output dist` y `python tools/validate.py --root dist`; `python -m http.server 8000 --directory dist` para revisar la salida. Un directorio de salida alternativo permitirá el piloto sin sustituir la raíz existente. Rechazar destino igual a raíz, `.git` o fuentes; no borrar contenido fuera de un directorio generado validado.

## Seis operaciones editoriales concretas

| Operación | Cambios de fuente previstos | Resultado y validación |
|---|---|---|
| Servicio nuevo | Añadir `entities/services/instalaciones-electricas.json`, traducción ES con alcance y entregables y relaciones con infraestructura; decidir `presentation: section` o `page` | Como sección obtiene ID en capacidad; como página genera `/es/servicios/instalaciones-electricas/`. Build comprueba evidencia, SEO y enlaces; no copiar el HTML de otra página |
| Proyecto nuevo | Añadir entidad `projects/campus-uib.json` y texto ES, con tipo de atribución, responsabilidad, métricas y permiso | Si está aprobado, ficha e índice se derivan del mismo registro; capacidades/sectores resuelven su ID. Hasta confirmar hechos, borrador excluido del artefacto público |
| Traducción nueva | Añadir `locales/ca/projects/campus-uib.json` con mismo ID, slug catalán, texto/SEO revisados; completar etiquetas UI necesarias | Generar solo esa versión aprobada; selector y hreflang recíprocos se derivan automáticamente. Faltan campos → error, no español encubierto como catalán |
| Imagen nueva o sustitución | Guardar original autorizado y registrar ID/ruta, dimensiones, procedencia, alt localizado y aprobación en `media/manifest.json` | Componente `media` emite variantes/dimensiones. Sustituir la ruta del mismo ID actualiza todas sus referencias tras build; verificar encuadre/alt cuando cambia significado |
| Página sectorial | Añadir entidad y ES de hoteles con problemas concretos, capacidades/servicios y evidencia diferenciada | `/es/sectores/hoteles/` solo tras cumplir criterio editorial; el índice y vínculos usan ID. No extraer cada chip del listado a una página vacía |
| Componente visual | Crear macro `components/technical-metrics.html` y estilos de componente; usar datos de métricas del proyecto | Mismo patrón en capacidad/ficha sin copiar cifras ni estructura; preservar semántica `dl`, contraste y composición responsive |

Para un caso nuevo no siempre hace falta un componente nuevo: usar los existentes con datos. No introducir un constructor genérico de bloques ni un DSL de páginas. Texto narrativo singular puede permanecer en un template específico mientras se estabiliza el modelo, documentando esa excepción; evitar duplicarlo en JSON y template.

## Desarrollo, revisión y despliegue

El build ocurre localmente o en CI; el hosting recibe únicamente `dist/`. No necesita Python ni Jinja en runtime. Fijar herramientas y reconstruir desde instalación limpia. No guardar credenciales ni datos privados en fuentes públicas ni artefacto. Mantener dominio/base URL como configuración única y distinguir preview de producción para que canonical/sitemap no apunten a localhost.

Para GitHub Pages, confirmar primero ajustes reales y permisos. Propuesta: workflow con instalación de dependencias, tests, build, validación del artefacto y carga/despliegue con herramientas oficiales de Pages, con publicación como paso final autorizado. Evitar publicar `src/`, originales y borradores por desplegar la raíz entera. No cambiar DNS/CNAME ni rama de publicación como efecto secundario del piloto.

La vuelta atrás recupera el artefacto anterior ya revisado y la configuración de publicación documentada, sin resetear cambios de trabajo del usuario. Véase la secuencia y aceptación por fase en 07.
