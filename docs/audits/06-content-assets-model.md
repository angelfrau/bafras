# 06 · Modelo de contenido y recursos gráficos

Propuesta mínima para B: JSON UTF-8, IDs estables, referencias verificables y textos por idioma. No se han creado modelos ejecutables, manifiestos ni traducciones. [Estructura de archivos](04-target-project-structure.md).

## Contrato común

Entidad compartida: `id`, `type`, `status`, relaciones y hechos no lingüísticos. Versión localizada: `entity_id`, `locale`, `slug`, `name`, `summary`, cuerpo de alcance apropiado, `seo.title`, `seo.description`, `status`, `reviewed_by`, `reviewed_at`. Estados editoriales `draft`, `review`, `approved`; permiso de publicación separado `pending`, `approved`, `restricted`. No confundir «texto revisado» con «derecho de publicación autorizado».

Un servicio puede tener `presentation: section|page`: el primero participa en su capacidad con `section_id`; el segundo requiere contenido/SEO y genera documento propio. Las capacidades y sectores no heredan una ficha vacía por existir su ID. `publish` requiere contenido suficiente y revisión, no únicamente `status` válido. Texto como párrafos/listas y campos concretos por tipo; no una taxonomía infinita de bloques abstractos.

Los hechos compartidos se guardan una vez. Cada métrica: `id`, `value` numérico, `unit`, `qualifier`, `scope`, `source_ref`, `verified_at`, `publication_status`; label por idioma. Distinguir valor exacto de aproximación y capacidad del programa de responsabilidad del participante. Home y fichas referencian la misma métrica y su regla de formato. No convertir en datos aprobados las cifras UIB divergentes observadas.

## Modelos por entidad

| Modelo | Campos específicos | Validación útil |
|---|---|---|
| Capability | ID, slug/nombre/descripcion localizados, `disciplines`, `service_ids`, `deliverables`, `media_refs`, `project_ids`, `sector_ids`, `cta` | Disciplinas/entregables no vacíos para página; todas las relaciones existen; CTA resuelve destino aprobado |
| Service | ID, `capability_id`, problema, alcance, actividades, entregables, `evidence_ids`, `sector_ids`, CTA, presentación/section_id | Una capacidad principal; no repetir un servicio distinto por idioma o sector; alcance diferenciado para página |
| Sector | ID, nombre, necesidades, `capability_ids`, `service_ids`, `evidence_ids`, CTA | Necesidades específicas, vínculos reales; no página independiente solo con nombre y chips |
| Project | ID, nombre, `project_type`, organización, `attribution_type`, alcance, responsabilidades, `metrics`, `media_refs`, `authorization`, `sector_ids`, `capability_ids`, opcional `service_ids` | `attribution_type: team_experience|bafras_project`; responsabilidades y autorización explícitas; no inferir autoría BAFRAS de una referencia previa |
| MediaAsset | ID, ruta fuente, tipo, licencia, autor, procedencia, alt por idioma, estado, dimensiones, aprobación, focal point opcional | Fuente existe; permiso y alt adecuados; formato/dimensiones reales; uso compatible con licencia |

Tipos y valores editoriales de Project no son sinónimos: `project_type` describe ingeniería/instalación/estudio; `attribution_type` describe quién realizó el trabajo. La organización puede ser cliente, empleador o institución de referencia: añadir `organization_role` para no confundirlos. `authorization` registra responsable, fecha, alcance y referencia documental, sin incorporar contratos privados al repositorio público.

`cta` es un destino por ID y sección opcional más label localizado; no un HTML embebido. Los proyectos/capacidades/sectores relacionados se resuelven por ID. El grafo puede derivar enlaces inversos para evitar mantener listas contradictorias; establecer una relación como fuente y comprobar las que se declaren explícitamente en ambos extremos.

## Ejemplo de servicio, solo ilustrativo y no aprobado

Entidad `entities/services/instalaciones-electricas.json`:

```json
{
  "id": "svc.electrical-installations",
  "type": "service",
  "status": "draft",
  "capability_id": "cap.infrastructure",
  "presentation": "section",
  "section_id": "instalaciones-electricas",
  "sector_ids": ["sector.hotels"],
  "evidence_ids": [],
  "media_refs": {}
}
```

Versión localizada `locales/es/services/instalaciones-electricas.json`:

```json
{
  "entity_id": "svc.electrical-installations",
  "locale": "es",
  "slug": "instalaciones-electricas",
  "name": "Instalaciones eléctricas",
  "summary": "Texto pendiente de revisión técnica.",
  "problem": [],
  "scope": [],
  "activities": [],
  "deliverables": [],
  "cta": {"page_id": "page.contact", "section_id": "cuentanos-tu-proyecto", "label": "Consultar"},
  "seo": {"title": "", "description": ""},
  "status": "draft",
  "reviewed_by": null,
  "reviewed_at": null
}
```

No generar página de este ejemplo: sus campos pendientes son deliberados. Al promover a `page`, completar datos, revisión, enlaces y evidencia; cambiar la presentación, sin duplicar el servicio. Las disciplinas existentes pueden seguir siendo secciones sencillas hasta tener contenido propio suficiente.

## Assets: estado real y aprovechamiento

Inventario: 34 archivos en `assets/images/`, con 33 gráficos: marca 18, equipo 6, experiencia MEP 6, Home 3; más `misc/a` de 2 bytes. Total 5.816.707 bytes. No hay manifiesto ni licencias/autores estructurados. `images/` está vacío. No se eliminaron variantes ni el archivo sin formato.

| Dominio | Recursos observados | Decisión propuesta |
|---|---|---|
| Marca | PNG/SVG de símbolos/logos, versiones `corregido`, favicon y avatar | Identificar variantes canónicas y usos autorizados; no borrar por parecido de nombre |
| Home hero | JPG 1248×832, 504.536 bytes, fondo CSS | Derivar WebP/AVIF y tamaños adecuados; mantener original; comprobar recorte y contraste |
| Home visión | PNG 1536×1024 de 1.906.658 bytes y WebP 1400×933 de 113.786 bytes | Conservar derivación útil; ilustración conceptual, no evidencia de obra |
| Equipo | PNG 400×400, 520×520, 476×520; tres JPG 912×1136 | Selección explícita por persona, crop acordado y salida HTML con dimensiones |
| Experiencia MEP | Seis JPG 1200×800, aproximadamente 100–304 KB cada uno | Candidatos disponibles en disco; aprobación de derechos/atribución todavía no demostrada |
| Slots de evidencia | 30 IDs en HTML, muchos sin archivo vinculado | Preservar identidad de slot y enlazar solo recursos aprobados |

Los recursos más pesados existentes no se transfieren necesariamente a visitantes: no están todos enlazados. Ni un JPG disponible ni un slot `data-asset-id` implican autorización o integración terminada. Los documentos locales `website-visual-assets.md`, `visual-evidence-map.md` y `visual-component-inventory.md` aportan requisitos útiles; algunos textos documentales contienen mojibake y datos históricos que deben revisarse al reutilizarse. No se ha corregido su contenido.

El Plan Maestro de Material Gráfico V1.0 citado en la solicitud no está disponible con ese título en el repositorio inspeccionado. Compatibilidad propuesta con sus requisitos facilitados: mantener dominios, identificadores, procedencia, estado, centralización, variantes y control de publicación; cotejar nombres y campos con el documento original cuando esté disponible. No afirmar conformidad completa con un documento no leído.

## Manifiesto mínimo y resolución de slots

Separar ID del **recurso** de ID del **slot**: `CAP-INF-HERO-01` identifica una posición editorial, no necesariamente la fotografía misma. Un recurso puede servir a varios slots; cambiarlo no debe exigir editar múltiples secciones.

Ejemplo de recurso existente, con derechos aún pendientes:

```json
{
  "assets": {
    "media.home.system-vision": {
      "id": "media.home.system-vision",
      "source_path": "home/vision/bafras-system-vision-diagram.png",
      "kind": "conceptual-illustration",
      "width": 1536,
      "height": 1024,
      "author": null,
      "provenance": "Inventario local docs/website-visual-assets.md",
      "license": null,
      "publication_status": "pending",
      "alt": {"es": "Representación conceptual de sistemas físicos y digitales interconectados."},
      "status": "available",
      "related_page_ids": ["page.home"]
    }
  }
}
```

`source_path` será relativa a `src/media/originals/` tras una migración aprobada; el ejemplo no cambia rutas actuales. El contenido tiene `media_refs`, por ejemplo `{"CAP-INF-HERO-01": "media.infrastructure.authorized-overview"}` cuando ese recurso exista y esté autorizado. Slot opcional sin recurso: `null`, sin placeholder público. Slot imprescindible para una evidencia que se quiera publicar: error o página en borrador; no inventar un asset para satisfacer el build.

`related_page_ids` es índice derivado de usos, para no mantener a mano dos listas de relaciones. Autor/licencia `null` expresan desconocido y bloquean uso público nuevo hasta revisión. No inferir propiedad a partir de estar en Git. La sustitución se hace cambiando el recurso asociado en un solo registro o actualizando su fuente; si el significado visual cambia, volver a revisar alt y usos vinculados.

## Pipeline gráfico propuesto

1. Conservar original con nombre consistente `dominio-tema-variante.ext`; no renombrar el inventario actual hasta mapear cada uso. Organizar por marca, home, capacidades, proyectos y equipo. Licencia/procedencia en manifiesto, documentos privados fuera del artefacto.
2. Validar extensión contra formato real, dimensiones y aprobación; no publicar originales grandes automáticamente. Derivar con Pillow y soporte de codecs comprobado; si AVIF no está disponible, WebP/JPEG es un fallback válido, no una instalación silenciosa.
3. Generar anchuras útiles según uso (p. ej. 480, 800, 1200 y 1600, sin ampliar por encima del original), parámetros de calidad probados visualmente y nombres deterministas con huella de contenido. Evitar regenerar si fuente/parámetros no cambiaron.
4. El componente emite `<picture>`/`srcset`/`sizes`, fallback, `width`/`height`, `decoding="async"` y alt localizado. Lazy para medios fuera de primera pantalla; la imagen principal candidata a LCP no debe ser lazy. Si se cambia el hero de fondo a imagen HTML, comprobar superposición/encuadre antes de publicar.
5. Reservar proporción para evitar saltos; respetar focal point y recorte según breakpoint. Medios decorativos tienen alt vacío explícito y no repiten texto; diagramas requieren explicación textual, no solo alt extenso. Vídeos/PDF, si aparecen, requieren tipo y presentación accesible apropiados.
6. Validador inspecciona cada documento generado, variantes, dimensiones, `srcset`, URLs en CSS, referencias por ID y estado de aprobación. Comprobar rutas case-sensitive para evitar que Windows oculte errores del host Linux. Señalar archivos sin uso como revisión, nunca borrarlos automáticamente.

La tarea de imágenes y su resultado derivado alimentan el build; no necesitan una segunda aplicación ni una CDN externa. El propósito es sustituir una imagen mediante un ID y reconstrucción, manteniendo coherencia y pruebas de todos sus usos.
