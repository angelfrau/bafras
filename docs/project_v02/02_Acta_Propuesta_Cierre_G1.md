# ACTA G1 — Propuesta de cierre y traspaso a desarrollo
**Fecha de la propuesta:** 03/11/2026 (actualizada en WEB-G1-CLOSE y WEB-00 FINAL, 03/11/2026)  
**Estado:** PROPUESTA PENDIENTE DE RATIFICACIÓN FORMAL. Incorpora las decisiones comunicadas por dirección en la instrucción WEB-00 FINAL (03/11/2026). Esta acta no lleva firma ni fecha de ratificación: el apartado 12 sigue sin completar.

## Decisión propuesta
Aceptar como línea base visual/editorial las nueve páginas aprobadas y los documentos D03 V1.22 (+ adenda 03.G1-02), D04 V2.4 y D05 V4.12. D02 V1.0-R (reconstruido) se acepta como contexto estratégico provisional. El catálogo AUD-G1-02 se consolidará durante la implementación. Se autoriza la implementación incremental una vez ratificado el gate.

## A. Decisiones comunicadas por dirección (instrucción WEB-00 FINAL, 03/11/2026)
Se registran literalmente como instrucción recibida. Su ratificación formal en el apartado 12 sigue pendiente.
1. Se mantiene el diseño aprobado de las nueve páginas.
2. Los diagramas técnicos no son obligatorios para el lanzamiento inicial; su incorporación futura debe seguir siendo posible (apartado 4).
3. Los componentes y tokens se consolidarán durante la implementación (apartados 3 y 5).
4. El contraste cumplirá WCAG AA en los usos aplicables, sin alterar innecesariamente la identidad corporativa (apartado 6).
5. Se mantiene la arquitectura Python + Pydantic v2 + Jinja2 de D04.
6. Se preservan los textos editoriales aprobados.
7. Las contradicciones de Contacto y las atribuciones pendientes se resuelven según la evidencia documental más reciente. Aplicado en la adenda 03.G1-02 de D03.
8. Las verificaciones legales, las licencias y las autorizaciones de publicación siguen pendientes hasta disponer de evidencia.
9. Git: `main` es producción y no se modifica; la única rama de desarrollo es `feat/contingut-v2`; sin `push` sin autorización.

## B. Pendiente de aprobación de dirección
| Materia | Referencia |
|---|---|
| Ratificación formal de esta acta | Apartado 12 |
| Ratificación de D02 V1.0-R (reconstruido) como autoridad estratégica | D02 §16–§17 |
| Title y meta de Inicio, Capacidades, Infraestructuras y Sistemas energéticos | DEC-05 |
| Etiquetas H05 de Inicio | DEC-15 |
| Adaptación opcional del copy CO-03 a la presencia del teléfono | Adenda 03.G1-02 |
| Logotipo maestro (`*_deep.svg` / `*_deep_corregido.svg`) y ubicación de créditos de imagen | DEC-10 |
| Proveedor del formulario, hosting y dominio canónico | DEC-11 |
| Idiomas de lanzamiento | DEC-14 |
| Registro de rutas ES | DEC-16 (WEB-G2-00) |
| Valor concreto de la regla de contraste (pino o tinta para texto pequeño sobre arena, o un token derivado) | Apartado 6 |

## 1. Documentos maestros y versiones
| Documento | Archivo | Versión | Autoridad |
|---|---|---|---|
| D02 — Posicionamiento | `02_posicionamiento.md` | V1.0-R, reconstruido | Provisional hasta ratificación; no es una recuperación literal del original perdido |
| D03 — Contenido editorial | `03_contenido_editorial_V1_22_baseline_G1.md` | V1.22 + adenda 03.G1-02 | Copy, orden y bloques |
| D04 — Arquitectura de software | `04_arquitectura_software_V2_4_handoff_G1.md` | V2.4 | Implementación, contratos y gates |
| D05 — Sistema visual | `05_sistema_visual_V4_12_baseline_G1.md` | V4.12 | Composición, medios, estilos y responsive |
| D01 — Taxonomía de servicios | — | — | No disponible; necesario antes de publicar (G4) |

## 2. Nueve maquetas aprobadas
Inicio V3 · Capacidades V1 · Infraestructuras e instalaciones V2 · Sistemas energéticos V2 · Automatización y control V1 · Sectores V3 · Proyectos y experiencia V1 · Sobre BAFRAS V1 · Contacto V2. Están en `maquetas_aprobadas/`, con hashes en `99_Manifest_SHA256.md`. Son referencia de composición; el texto vinculante es D03 (adendas 03.G1-01 y 03.G1-02).

## 3. Catálogo de componentes
`soporte_auditoria/AUD-G1-02_Catalogo_Componentes.md` (13 familias), con el complemento de `WEB_G1_CLOSE_INFORME.md` §6.3. **Decisión A.3:** se consolida durante la implementación (WEB-G2-02), con criterios de aceptación por componente.

## 4. Diagramas técnicos (WGR-050)
**Decisión A.2.** D05 §8.5 y C03-EV-03/04/05 exigían diagramas conceptuales de INF, ENE y DIG como entregable G1; las composiciones aprobadas los excluyen. Los diagramas **no son requisito de G1 ni del lanzamiento inicial** y no bloquean la implementación. Solo podrán incorporarse más adelante con relaciones técnicas revisadas por ingeniería, versión móvil y alternativa textual (D05 CA-C03-D02/D03), mediante una nueva aprobación de diseño y sin alterar el copy de D03. La implementación debe permitir añadir una sección de diagrama sin cambiar la arquitectura.

## 5. Tokens (WGR-051)
**Decisión A.3.** Contenedor, cortes, escala tipográfica y espaciado se consolidan en WEB-G2-02 a partir de las maquetas aprobadas, sin cambio estético. La paleta corporativa no cambia.

## 6. Contraste (WGR-052)
**Decisión A.4:** WCAG AA en los usos aplicables sin alterar innecesariamente la identidad. **Aplicación propuesta, pendiente de validación de Diseño en WEB-G2-02:** verde `#1A7A5A` sobre arena (4,31:1) solo para texto grande y elementos no textuales; texto pequeño sobre arena en pino `#0E2B25` (12,33:1) o tinta `#2A2A2A` (11,72:1); verde sobre papel (4,85:1) y blanco (5,28:1) sin restricción. No introduce colores nuevos.

## 7. Componentes o estados pendientes de concretar
Pie global único (WGR-054), estados del formulario (WGR-056), migas (WGR-057), créditos de imagen (WGR-061), selector con un solo idioma (WGR-062) y homogeneización del menú (WGR-055). Se concretan en WEB-G2-02 o WEB-G3-01b dentro de los patrones aprobados.

## 8. Verificaciones diferidas, sin declararlas superadas
- Navegación final, menú, teclado y enlaces: G2/G3.
- Responsive a 320, 375, 390, 768, 1024 y 1440 px, zoom 200 % (D05 §12.5, CA-C02-10) y accesibilidad: G3/G4. Hallazgo conocido: Sobre BAFRAS desborda 27 px a 320 px en la maqueta (WGR-059); se corrige en la implementación.
- Cotejo literal de D03 con el HTML generado: G3/G4.
- Formularios, privacidad, correo, referencias, catálogos, traducciones y permisos: G4 antes de publicar.

## 9. Bloqueantes de publicación (no bloquean el desarrollo)
Referencias verificadas y autorizadas; perfiles autorizados; canales de contacto probados; aviso legal y privacidad con titular real; licencias y créditos de imagen; proveedor del formulario; hosting y dominio; idiomas de lanzamiento; D01. Detalle en `WEB_G1_CLOSE_INFORME.md` §8.

## 10. Responsabilidades de implementación y QA
- **Dirección:** ratificar esta acta y resolver el apartado B.
- **Editorial:** SEO, H05 y CO-03 opcional.
- **Diseño:** tokens, regla de contraste y estados del apartado 7.
- **Arquitectura y desarrollo:** contratos Pydantic v2, rutas, build Jinja2 y tests en `feat/contingut-v2`.
- **QA:** la matriz del apartado 8, con evidencia reproducible.

## 11. Criterios de apertura de G2
1. Esta acta ratificada formalmente (apartado 12).
2. Repositorio saneado y documentación confirmada en `feat/contingut-v2`. **Cumplido en WEB-00 FINAL:** ver `WEB_00_BASELINE.md`.
3. Registro de rutas ES ratificado antes de cerrar WEB-G2-00 (DEC-16).

## Condición de aceptación
Dirección confirma que no quedan decisiones estéticas fundamentales abiertas y traslada las verificaciones enumeradas a gates posteriores. Esta acta no constituye aprobación formal hasta esa confirmación.

## 12. Ratificación de dirección
**Decisión dirección:** [ ] Aprobado conforme a los apartados A y 1–11 [ ] Requiere cambios  
**Responsable / fecha:** pendiente.
