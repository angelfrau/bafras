# config/ — configuración técnica del sitio (equipo WEB)

Datos neutros de idioma, validados por sus modelos (`bafras-web doctor` los comprueba). Cada archivo se incorpora junto con el modelo
que lo valida; no se crean archivos sin contrato.

| Archivo previsto | Contenido | Estado |
|---|---|---|
| `site.yaml` | URL base, contacto público (D04 §13), versión del esquema de contenido | Pendiente |
| `locales.yaml` | `es`, `ca`, `en`, `de`; publicado sí/no; idioma por defecto (`es`, sin prefijo) | **Vigente** (DEC-14) · modelo `bafras_web.localization.locales` |
| `routes.yaml` | Fuente única: `page_id` → página padre + slug por idioma | **Vigente** (DEC-16) · modelo `bafras_web.site.routes` |

Ver `docs/architecture.md`.
