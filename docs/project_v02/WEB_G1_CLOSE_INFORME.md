# BAFRAS WEB — WEB-G1-CLOSE · Informe de consolidación y cierre documental G1
**Fecha:** 03/11/2026 · **Estado:** COMPLETADO CON DECISIONES PENDIENTES. G1 **no** está cerrado: el acta queda preparada y pendiente de ratificación.
**Documentos asociados:** `WEB_G1_CLOSE_MATRIZ.md` (estado vigente de las 71 incidencias) · `WEB_G1_CLOSE_DECISIONES.md` (16 decisiones) · `02_Acta_Propuesta_Cierre_G1.md` · `WEB_00_*` (repositorio).

## 1. Resumen
- El contrato de diseño es coherente en alcance, stack y contenido. Las contradicciones que quedan están localizadas, tienen autoridad identificada y una propuesta concreta.
- **Correcciones objetivas aplicadas:** la matriz responsive seguía reducida en D04 §13, en D05 §48 y en el briefing. El acta se ha reestructurado con los 12 apartados requeridos y sigue sin firmar.
- **Hallazgo nuevo grave:** D02 se ha perdido entre el 02/11 y hoy (WGR-091). El resto del paquete corre el mismo riesgo mientras no esté en Git (WGR-092). Se ha creado un respaldo externo verificado (WEB_00_BASELINE §3).
- **Revisión de una recomendación anterior:** para la introducción y la ayuda de Contacto, la autoridad respalda CO-01/CO-02 V1.1, no 03.K (DEC-04).
- **Bloquean el inicio de G2:** ratificar el acta (con la excepción de diagramas, la regla de contraste y el catálogo) y versionar el repositorio. Ninguno es técnico.

## 2. Estado documental

| Documento | Estado | Observación |
|---|---|---|
| D03 V1.22 | Vigente | Contradicciones internas en Contacto (DEC-04), atribución (DEC-06) y H05 (DEC-15); falta SEO en 4 páginas (DEC-05) |
| D04 V2.4 | Vigente | §13 corregido; contratos de modelo incompletos (§5) |
| D05 V4.12 | Vigente | §8.5 en conflicto con las composiciones aprobadas (§4); §48 corregido |
| Acta G1 | Propuesta actualizada | Pendiente de ratificación |
| D02 | **Ausente; existía el 02/11** | No recuperable desde Git (DEC-03) |
| D01, AUD-G1-01, CSV y script de AUD-G1-03, prototipos de integración | Ausentes | Siguen sin aparecer (WGR-003) |
| Briefing, catálogo AUD-G1-02, contrato de navegación, AUD-G1-03, REVIEW-01 (informe, CSV, trazabilidad, plan), evidencias | Presentes | Manifiesto actualizado |

No se ha reconstruido ningún documento ausente.

## 3. Revisión de las incidencias de REVIEW-01
Se han releído el informe, las 61 filas del CSV y la matriz de trazabilidad. Para cada incidencia se han revisado la evidencia (contrastada con las líneas actuales de D03/D05 y con las maquetas extraídas), la autoridad, la vigencia, las dependencias, la fase y el criterio de cierre. Resultado en `WEB_G1_CLOSE_MATRIZ.md`:

- **9 RESOLVED · 5 PARTIAL · 19 OPEN · 15 DEFERRED · 23 BLOCKED_DECISION · 0 ACCEPTED_EXCEPTION.**
- Ninguna excepción se da por aceptada sin firma. Las cuatro «ACEPTADA» de REVIEW-01 se han recalificado: dos como RESOLVED, porque ya existía una regla documental explícita, y dos como DEFERRED.
- Severidades confirmadas. Las P0 de publicación (WGR-080…084) se mantienen como P0, pero de tipo `PUBL`: no bloquean el desarrollo.
- **Recomendación corregida (WGR-021):** ver §4.2.

## 4. Contradicciones G1

### 4.1 Diagramas técnicos (WGR-050, P0 de gobierno)
- **Cláusulas que lo exigen:** D05 §8.5 (L66), «Diagramas conceptuales: INF, ENE y DIG con lenguaje visual común y versiones móviles», dentro de los «Entregables obligatorios del diseño ANTES del refactor», a los que remiten D04 §8 G1 y D05 L576 (C03-EV-03/04/05).
- **Decisiones visuales aprobadas que los excluyen:** D05 L1049 (INF-05 «Sin diagrama ficticio de integración»), L1218 (ENE-05 «sin gráfico inventado»), L1250 (DIG «sin flujogramas inventados»); además, L605–608 y L693/L795 los declaran «sin diagrama obligatorio».
- **Alcance:** tres páginas. No afecta al copy, porque D03 no contiene texto de diagramas, ni a la arquitectura, porque `Section` admite añadir un tipo más adelante.
- **Autoridad:** la exigencia procede de D05 §8, que es posterior y específico; las exclusiones proceden de aprobaciones de página posteriores, también de D05. Ninguna de las dos prevalece de forma inequívoca. Por eso **la excepción la decide dirección** y no se ha corregido en el documento.
- **Propuesta:** texto literal en el acta, apartado 4 (DEC-02). Mantiene la posibilidad futura con las garantías de CA-C03-D02/D03 y no modifica las maquetas.

### 4.2 Contacto (WGR-020/021/022)
Las variantes y su análisis de autoridad están en DEC-04. Conclusión: ninguna variante de los mensajes de estado es inequívocamente la aprobada. Para la introducción y la ayuda, la adenda 03.CO-02 (la aprobación más reciente) y la maqueta aprobada respaldan CO-01/CO-02 V1.1. La recomendación de REVIEW-01 §10.4 («03.K/03.K.2 en todo») se **corrige** y queda anotada allí. CO-03 con teléfono necesita texto aprobado. **No se ha modificado ningún texto de D03.**

### 4.3 Proyectos y experiencia (WGR-023, 026, 080)
- La diferenciación está bien protegida: D03 L6–12 («no se presentarán como encargos de BAFRAS»), L868–874, 03.K §2 y D04 §4 (`Experience.kind`: `bafras_project` / `founder_previous`).
- Lo que falta es la forma canónica de las etiquetas (DEC-06) y la variante sin referencias publicables (DEC-07).
- **Riesgo comercial residual:** Sobre BAFRAS SB-04 (D03 L958) titula «Experiencia profesional aplicada a proyectos reales». Ese texto está aprobado y no atribuye proyectos a BAFRAS, pero la implementación no debe enlazar desde ahí a fichas inexistentes.
- No se ha inventado ningún proyecto, cliente ni cifra.

### 4.4 Sobre BAFRAS (WGR-024, 081)
03.K §1 fija la titulación de cada fundador y el texto publicable del equipo. La maqueta SB V1 usa otro texto de equipo y omite las titulaciones. Por la adenda 03.G1-01 («prevalece D03»), la implementación usará 03.K §1: no es una decisión, sino una incidencia OPEN de G3-02. Los nombres completos, biografías y retratos siguen pendientes de autorización (G4). No se han modificado biografías. La coherencia con D02 no puede verificarse porque D02 está ausente.

### 4.5 SEO editorial (WGR-040)
Faltan title y meta en Inicio, Capacidades, INF y ENE. Las propuestas, derivadas de los H1 aprobados y del mapa de intención de D03 §4, están en DEC-05. **No se han incorporado a D03.**

## 5. Contratos de arquitectura (D04)
Flujo obligatorio: **contenido declarativo → Pydantic v2 → aplicación Python → Jinja2 → HTML estático**. Las plantillas no reciben diccionarios sin validar. Esta tabla delimita los contratos; **no** los implementa ni fija tipos definitivos, que corresponden a WEB-02.

| Contrato | En D04 | Responsabilidad | Campos esenciales | Validaciones y reglas de publicación | Estado |
|---|---|---|---|---|---|
| Configuración del sitio | Parcial (§13) | Datos globales | `site_name`, `base_url`, `email`, `phone_display`, `phone_e164`, `default_locale`, `locales_published` | Coherencia entre el teléfono mostrado y E.164; email válido; solo idiomas publicados | Falta el modelo (WGR-030) |
| Página (`Page`) | Sí (§4) | Unidad editorial por idioma | `id`, `locale`, `slug`, `status`, `seo`, `hero`, `sections`, `related_pages` | `id` estable; `slug` único por idioma; `draft` nunca en `dist` | Suficiente |
| Sección (`Section`) | Sí (§4) | Bloque D03 | `id` (= ID D03), `kind` (enumerado cerrado), `content`, `media_refs` | `kind` limitado a variantes de D05; `id` trazable al bloque D03 | Falta el enumerado de `kind` (WGR-010) |
| Navegación | No | Seis entradas, Capacidades con 3 hijas | `items[]`: `page_id`, `label_by_locale`, `children`, `order` | Destino existente; sin duplicados; estado activo | Falta (WGR-030) |
| Sector | No (claves en 03.SEC.CAT-01) | Seis sectores | `sector_id`, `order`, `title`, `catalogs[]` | `sector_id` del enumerado de D03; orden fijo | Falta |
| Capacidad | No | INF/ENE/DIG | `capability_id`, `page_id`, `card` | Tres valores cerrados | Falta |
| Proyecto (`Experience`) | Sí (§4) | Referencias | `id`, `kind`, `attribution`, `scope_verified`, `client_permission`, `media_permission`, `status` | Publicable solo si `scope_verified` y los permisos son verdaderos; etiqueta según `kind` (DEC-06) | Suficiente; falta la etiqueta localizada |
| Persona | No | Fundadores | `person_id`, `display_name`, `degree`, `specialty`, `role`, `portrait_ref`, `consent` | Sin retrato ni nombre completo si `consent` es falso; titulación literal de 03.K §1 | Falta |
| SEO | Parcial (`Page.seo`) | Metadatos | `title`, `description`, `canonical`, `og_image_ref`, `noindex` | `title` y `description` únicos por idioma; canónica absoluta; `hreflang` solo hacia versiones existentes | Falta la estructura interna |
| Recurso visual (`Media`) | Parcial (§4) | Imágenes | ver §7 | ver §7 | Insuficiente (WGR-034) |
| Documento descargable | Sí (§11–12) | Catálogos PDF | `catalog_id`, `sector_id`, `title`, `file`, `language`, `status` | 0/1/N; archivo existente; idioma real | Suficiente |
| Localización | Parcial (§3) | Idiomas y slugs | `locale`, `published`, `fallback_policy` | Sin enlaces a traducciones inexistentes | Depende de DEC-14 |
| Estado de publicación | Parcial (`status`) | Ciclo de vida | Enumerado común: `draft` · `internal` · `approved` · `published` | El build falla si una entidad pública referencia otra no publicable | Falta el enumerado común |

**Criterios de aceptación de WEB-02:** cada contrato tiene un modelo Pydantic v2 con `extra="forbid"`; hay pruebas de rechazo para los casos inválidos de la columna de validaciones; las plantillas solo reciben instancias de modelo; el build falla ante referencias rotas, rutas duplicadas o `draft` público (D04 §4). No se fijan aquí tipos, rutas de archivo ni formato (YAML/JSON/MD).

## 6. Sistema visual y accesibilidad

### 6.1 Contraste
Valores medidos con la fórmula WCAG 2.x:

| Primer plano / fondo | Arena `#ECE8DD` | Papel `#F7F5F0` | Blanco | Línea `#D8D2C3` |
|---|---|---|---|---|
| Verde `#1A7A5A` | **4,31** | 4,85 | 5,28 | 3,50 |
| Pino `#0E2B25` | 12,33 | 13,86 | 15,10 | 10,01 |
| Tinta `#2A2A2A` | 11,72 | 13,17 | 14,35 | 9,52 |

Blanco sobre verde: 5,28. Usos afectados sobre arena, en las nueve maquetas: eyebrows (11 px), numerales (12–13 px), enlace `info@bafras.com` (22 px, peso 600, que no cuenta como texto grande). Además, hay grises locales fuera de tokens por debajo de 4,5:1 (WGR-053). Los estados hover y focus no se han medido porque requieren interacción (WGR-074).

**Regla propuesta (DEC-08, acta §6):** verde sobre arena solo para texto ≥ 24 px (o ≥ 18,66 px con peso ≥ 700) y para elementos no textuales (≥ 3:1). El texto pequeño sobre arena usa pino o tinta. Los enlaces sobre arena se distinguen también por subrayado. El indicador de foco debe tener ≥ 3:1 frente a ambos fondos: verde da 4,31 sobre arena y 4,85 sobre papel, así que cumple. Alternativa que exige modificar D05: un token `verde-texto` `#187154`, con 4,86:1 sobre arena. No se ha aprobado ningún token.

### 6.2 Responsive: Sobre BAFRAS a 320 px (WGR-059)
- **Elemento:** `h1` del hero («Ingeniería con visión técnica y disciplinas complementarias.»).
- **Causa raíz:** en el corte móvil, la maqueta fija `.hero h1{font-size:42px}`, por debajo del mínimo de `clamp(42px,5vw,70px)`, y define `.hero{grid-template-columns:1fr}`. Una pista `1fr` equivale a `minmax(auto,1fr)`, de modo que su mínimo es el ancho mínimo del contenido. La palabra más larga, «complementarias», a 42 px impone ese mínimo y desborda 27 px a 320 px.
- **Corrección mínima propuesta:** en la implementación, no en la maqueta aprobada, que se conserva intacta: pistas `minmax(0,1fr)` y un límite inferior de H1 en el token tipográfico móvil, por ejemplo `clamp(2rem, 10vw, 2.625rem)`, para mantener 42 px desde unos 420 px. Se completa con `overflow-wrap:break-word` como salvaguarda.
- **Fidelidad:** idéntica a partir de unos 420 px; a 320–419 px el H1 se reduce proporcionalmente. Se resuelve con DEC-09 (tokens) en WEB-G2-02 y se verifica en la matriz de seis anchos.

### 6.3 Componentes
El catálogo AUD-G1-02 (13 familias) está **completamente especificado** en: CTA, tarjeta de capacidad, tarjeta sectorial (0/1/N), contacto directo y bloque editorial.

**Variantes o estados que faltan:**

| Componente | Falta | Criterio de aceptación propuesto |
|---|---|---|
| Cabecera | Composición única (WGR-055): el logo enlaza a Inicio; cinco destinos más el botón Contacto | Una sola plantilla; `aria-current`; menú móvil con `aria-expanded`, cierre con Esc, foco devuelto al botón; utilizable sin hover |
| Pie | Diseño único (WGR-054) | Enlaces principales, `mailto`/`tel` reales, enlaces legales solo si las páginas existen, enlace a créditos (DEC-10) |
| Formulario | Estados de error, carga, éxito y fallo del servidor sin diseño (WGR-056) | Etiquetas persistentes; error asociado con `aria-describedby`; resumen enfocable; envío anunciado (`aria-live`); doble envío bloqueado; éxito solo con respuesta del servidor; formulario desactivado y correo visible mientras no haya proveedor |
| Navegación móvil | Homogeneizar | Igual que la cabecera; sin desbordamiento a 320 px; objetivos ≥ 24×24 px |
| Recursos ausentes | Regla general | Si `Media` no es publicable, no se muestra imagen rota ni hueco, y la composición alternativa queda definida por página |
| Complemento al catálogo (WGR-063) | `SectionHeading`, `NeedList`, `DeliverableList`, rejilla de ámbitos con banda transversal, `Breadcrumbs`, `SkipLink`, ficha de proyecto | Cada uno con variantes tomadas de las maquetas y una sola implementación |

**D04 ↔ D05:** coherentes. D04 §13 exige contacto en CO-03 y en el pie, y D05 lo representa en las maquetas. La única divergencia, la matriz de anchos, ya está corregida.

## 7. Recursos visuales y licencias
- **Inventario:** biblioteca `BAFRAS_Website_Visual_Assets_V1` con 36 entradas: 29 READY, 4 PENDING_ORIGINAL, 2 NEEDS_CREATION y 1 NOT_FOUND. Licencias: CC BY-SA 4.0 (12), CC BY-SA 3.0 (3), CC BY 2.0 (3), CC BY 3.0 (1), CC BY 4.0 (1), dominio público (5), CC0 (1), propias (3) y sin licencia (7, no READY). En las maquetas hay 10 imágenes, byte a byte iguales a la biblioteca; 7 de las 9 asignadas son CC BY/BY-SA.
- **Evidencia disponible:** `source.json` con URL, autor, licencia y SHA1 del original; `attribution.md` con el texto de crédito y las obligaciones ShareAlike. Las licencias **declaradas por el proveedor** no se han verificado de forma independiente. El campo `commercial_use_verified: true` del manifiesto es una afirmación del proveedor, no una autorización de BAFRAS.
- **Obligaciones:** CC BY/BY-SA exigen crédito visible, enlace a la licencia e indicación de la modificación (recorte y WebP). Los derivados de CC BY-SA se ofrecen con la misma licencia. Las imágenes con personas identificables (WGR-098) requieren además valorar el derecho de imagen.
- **Contrato de asset propuesto (amplía `Media` de D04 §4):**

| Campo | Regla |
|---|---|
| `asset_id` | Estable, con prefijo inequívoco (p. ej. `img-inf-01`). Nunca `D0x`, para no confundir con documentos (WGR-096) |
| `kind` | `photo` · `diagram` · `chart_synthetic` · `logo` · `portrait` · `pdf` |
| `source_path` / `published_path` | Original (puede estar fuera de Git, con SHA) y derivado en `assets/` |
| `provenance` | `source_url`, `provider`, `retrieved`, `original_sha1` |
| `license` | Identificador SPDX (`CC-BY-SA-4.0`…), `license_url`, `attribution_required`, `share_alike` |
| `author`, `attribution_text_by_locale`, `modifications` | Obligatorios si `attribution_required` |
| `alt_by_locale`, `caption_by_locale` | `alt` vacío solo si es decorativa |
| `rights_status` | `declared` · `verified` · `authorized` · `rejected`; solo `verified` o `authorized` son publicables |
| `publication_status` | Enumerado común (§5) |
| `variants` | Anchos y formatos generados |
| `used_by` | `page_id`/`section_id`/componente; el build genera desde aquí la página de créditos |

El build falla si una imagen publicada carece de licencia, de crédito exigido o de `rights_status` publicable.

## 8. Condiciones de publicación clasificadas

| Pendiente | Bloqueante de implementación | Bloqueante de integración | Bloqueante de publicación |
|---|---|---|---|
| Referencias profesionales verificadas | — | — (DEC-07 define la variante sin tarjetas) | Sí (WGR-080) |
| Perfiles autorizados | — | — | Sí (WGR-081) |
| Canales de contacto probados | — | E2E del formulario en G3-01b | Sí (WGR-082) |
| Textos legales y privacidad | — | Activación del formulario | Sí (WGR-083) |
| Licencias de recursos | — | — | Sí (WGR-084, 098) |
| Hosting | — | — | Sí (WGR-039) |
| Servicio de formulario | — | Sí, cierre de G3-01b (WGR-033) | Sí |
| Idiomas de lanzamiento | — (la arquitectura ya es multilingüe) | Selector (WGR-062) | Sí (WGR-032) |
| Copy de Contacto, SEO, H05 y etiquetas | — | Sí, paridad de G3 (DEC-04/05/06/15) | Sí |
| Acta G1, tokens, contraste, catálogo | **Sí** (DEC-01/02/08/09) | — | — |
| Control de versiones y estado de `origin/main` | **Sí** (DEC-13) | — | — |
| Rutas ES | **Sí**, cierre de G2-00 (DEC-16) | — | — |

## 9. Correcciones ejecutadas en WEB-G1-CLOSE
1. **D04 §13:** la matriz responsive remite a la matriz completa de §14.
2. **D05 §48 (L1691):** «QA posterior obligatorio» incluye 375/1024 px y zoom 200 % según §12.5.
3. **Briefing L11:** la matriz dice «320/375/390/768/1024/1440 px y zoom 200 %».
4. **Acta G1:** reestructurada con los apartados 1–12; decisión, condición de aceptación y casillas sin marcar; estado PENDIENTE DE RATIFICACIÓN.
5. **`WEB_G1_REVIEW_01_INFORME.md` §10, fila 4:** nota de que la recomendación de Contacto queda revisada en DEC-04.
6. **`99_Manifest_SHA256.md`:** hashes recalculados y entregables nuevos añadidos.
7. **`.gitignore`** (WEB-00).

No se ha modificado copy aprobado, composiciones, identidad, servicios, sectores, biografías, referencias, stack ni condiciones de publicación.

## 10. Preparación para G2
**READY WITH CONDITIONS.** WEB-01 puede empezar cuando: (1) se ratifique el acta con DEC-01/02/08/09; (2) se ejecuten las operaciones Git de DEC-13 y se inspeccione `origin/main`; (3) se resuelva DEC-03 o se retire D02 formalmente. Ninguna de estas condiciones exige trabajo técnico adicional de diseño. Las decisiones B y C no bloquean WEB-01 ni WEB-02 y tienen fecha límite en `WEB_G1_CLOSE_DECISIONES.md`.
