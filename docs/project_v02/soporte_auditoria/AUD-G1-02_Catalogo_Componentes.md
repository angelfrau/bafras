# AUD-G1-02 · Catálogo consolidado de componentes (especificación para G2)

**Base:** D04 V2.3, D05 V4.11 y HTML aprobados. **Naturaleza:** inventario de contratos, no una biblioteca de componentes implementada ni cambio de diseño. La fuente editorial continúa siendo D03.

| Componente | Variantes / estados | Reglas de aceptación | Fuente |
|---|---|---|---|
| Cabecera global | 6 entradas principales; Capacidades + 3 especialidades; activo; escritorio/móvil | Todas las rutas de página existen, navegación teclado, menú móvil desplegable, foco visible | D03 §3.1–3.2; D04 navegación |
| Pie global | enlaces principales, legal publicado, contacto verificado | No enlaces ficticios ni datos legales no aprobados | D03; D05 |
| Hero | título, entradilla, CTA primario/secundario opcional | H1 único; jerarquía y copy exactos; sin salto de línea impuesto | D05 Inicio/INF/CO |
| CTA | primario, secundario, texto, ancla, tel, mailto | Enlace semántico, foco visible, destino real; no botón inerte | D03 §3.2 |
| Tarjeta de capacidad | INF, ENE, DIG | Texto y destino especializado correctos | D03 Capacidades; D05 CAP |
| Tarjeta sectorial | seis sectores; 0/1/N catálogos | 0: sin descarga; 1: enlace directo; N≥2: selector `<details>`; PDF solo real y autorizado | D03 03.SEC.CAT-02; D04 §12; D05 SEC |
| Tarjeta de experiencia | destacada, secundaria, ficha futura | Atribución correcta; no ficha sin evidencia y permiso | D03 PE; D05 §41 |
| Perfil fundador | tres perfiles, igual jerarquía | Nombre, especialidad, titulación y referencias verificadas | D03 SB; D05 §44 |
| Bloque editorial | intro, listado, columnas, banda de cierre | Tipografía/espaciado consistentes; contenido literal D03 | D05 aprobaciones |
| Formulario de contacto | vacío, requerido, inválido, enviando, éxito, error, deshabilitado | 4 campos, 3 requeridos, envío deshabilitado en prototipo; éxito solo con servidor | D03 CO; D04 §13; D05 §47 |
| Contacto directo | teléfono y email; estados verificado/no operativo | `tel:+34610903179`, `mailto:info@bafras.com`; verificar recepción antes de publicar | D03 03.CO-02 |
| Selector de idioma | ES/CA/EN/DE; página disponible/no disponible | No enlazar traducciones inexistentes; preservar página equivalente | D04 i18n |
| Medios | imagen, pie, alternativa textual, no disponible | Asset autorizado, sin imagen rota ni licencia presumida | D04 Media; D05 |

## Precedencia

1. Aprobaciones posteriores de D05 prevalecen sobre borradores históricos de la misma página. 2. D03 gobierna el copy. 3. D04 gobierna rutas y contratos. 4. No normalizar CSS a costa de modificar composición aprobada. 5. Los componentes deben quedar implementados una sola vez en G2 y validados en dist.

## Estados todavía no verificables

Foco real, teclado, validación y envío, PDFs reales, imágenes finales, traducciones y metadatos requieren navegador y/o implementación; no se certifican aquí.
