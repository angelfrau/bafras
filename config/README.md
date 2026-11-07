# config/ — configuración técnica del sitio (equipo WEB)

Datos neutros de idioma, validados por sus modelos (`bafras-web doctor` los comprueba). Cada archivo se incorpora junto con el modelo
que lo valida; no se crean archivos sin contrato.

| Archivo previsto | Contenido | Estado |
|---|---|---|
| `site.yaml` | Contacto público (D04 §13): `email`, `phone_display`, `phone_e164` (validados entre sí). URL base: pendiente (DEC-11) | Implementado (WEB-V01-B) |
| `composition.yaml` | Por página: imagen del manifiesto asignada a cada hueco `media` (mismo selector que el pendiente de CONTENT) y variantes de sección; autoridad D05 | Implementado (WEB-V01-B) |
| `locales.yaml` | `es`, `ca`, `en`, `de`; publicado sí/no; idioma por defecto (`es`, sin prefijo) | **Vigente** (DEC-14) · modelo `bafras_web.localization.locales` |
| `routes.yaml` | Fuente única: `page_id` → página padre + slug por idioma | **Vigente** (DEC-16) · modelo `bafras_web.site.routes` |

Ver `docs/architecture.md`.


WEB-V02 R2: `composition.yaml` incorpora INF/ENE/DIG (D05 §26/29/31) y variantes compartidas
para interiores. Se validan páginas, secciones, huecos media, activos y compatibilidad de variantes.
Las URL públicas continúan procediendo únicamente de `routes.yaml` / `SiteRouting`.

CONTACT-R1 / WEB-V03 R2: datos operativos exclusivamente en site.yaml; composición de canales
mediante direct_contact, sin formulario. Detalle de autoridad editorial: ../docs/project_v02/web/CONTACT_R1.md.
