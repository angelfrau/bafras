# WEB-G1-REVIEW-01 · Matriz de trazabilidad de las nueve páginas

**Fecha:** 03/11/2026. **Naturaleza:** matriz de trabajo **no vinculante** para G2/G3. No sustituye a D03 (copy), D04 (contratos) ni D05 (diseño), ni reproduce su texto. Los números de línea `D03 Lnnn` se refieren a `03_contenido_editorial_V1_22_baseline_G1.md` tal como queda tras esta revisión. Las incidencias `WGR-nnn` están en `WEB_G1_REVIEW_01_INCIDENCIAS.csv`.

**Leyenda de verificación de maquetas.** «Desbordamiento 6/6» indica que no hay desbordamiento horizontal a 320, 375, 390, 768, 1024 y 1440 px (Chrome 156 headless, iframe de ancho fijo, `evidencias_WEB_G1_REVIEW_01/desbordamiento_resultados.json`). No equivale a revisión visual humana, teclado, lector de pantalla, zoom 200 % ni WCAG. «Contraste» resume `contraste_resultados.json` (texto sobre fondo sólido, indicativo).

## 1. Matriz resumen

| Página | Ruta ES (propuesta, pendiente de ratificar · WGR-031) | Bloques D03 | Contratos D04 | Diseño D05 (aprobación) | Maqueta aprobada y capturas | Desbordamiento | Incidencias principales |
|---|---|---|---|---|---|---|---|
| Inicio | `/es/` | H01–H07, L55–140 | §3, §4 `Page`/`Section`/`Media`/`Experience`; §13 contacto | §23, §26 (V3 aprobada) | `C04_Inicio_V3/inicio_v3.html`; sin capturas | 6/6 | WGR-025, 027, 040, 052, 058 |
| Capacidades | `/es/capacidades/` | C01–C05, L170–238 | §3, §4 | §35 (V1 aprobada) | `C04_CAP_V1/capacidades.html`; 5 PNG (320/390/768/1024/1440) | 6/6 | WGR-027, 028, 040, 052, 053, 057 |
| Infraestructuras e instalaciones | `/es/capacidades/infraestructuras-instalaciones/` | INF-01–INF-07, L296–387 | §3, §4 | §25, §26 (V2 aprobada) | `C04_INF_V2/infraestructuras_v2.html`; sin capturas | 6/6 | WGR-040, 050, 052, 057, 058 |
| Sistemas energéticos | `/es/capacidades/sistemas-energeticos/` | ENE-01–ENE-07, L436–528 | §3, §4 | §28, §29 (V2 aprobada) | `C04_ENE_V2/sistemas_energeticos_v2.html`; sin capturas | 6/6 | WGR-040, 050, 052, 057 |
| Automatización y control | `/es/capacidades/automatizacion-control/` | DIG-W01–W07, L585–656 | §3, §4 | §30, §31 (V1 aprobada) | `C04_DIG_V1/automatizacion_control_v1.html`; sin capturas | 6/6 | WGR-050, 052, 057, 058 |
| Sectores | `/es/sectores/` | SEC-01–SEC-05, L708–762; adendas 03.SEC.CAT-01/02 | §11, §12 `DownloadableResource` | §36–§39 (V3 aprobada) | `C04_SEC_V3_aprobado/sectores_v3.html`; sin capturas (las de V2 no están en el paquete) | 6/6 | WGR-012, 052, 053, 058, 086 |
| Proyectos y experiencia | `/es/proyectos-experiencia/` | PE-01–PE-04, L810–862 | §3, §4 `Experience`, `StudyPublication` | §40, §41 (V1 aprobada) | `proyectos-experiencia.html` + `plantilla-ficha-proyecto.html`; 8 PNG | 6/6 (índice y ficha) | WGR-023, 026, 027, 080 |
| Sobre BAFRAS | `/es/sobre-bafras/` | SB-01–SB-05, L925–977; 03.K §1 | §4 (sin modelo de persona · WGR-030) | §42–§44 (V1 aprobada) | `C04_SB_V1/sobre-bafras.html`; 1 PNG escritorio | **5/6 (desborda a 320 px)** | WGR-024, 059, 081 |
| Contacto | `/es/contacto/` | CO-01–CO-04, L981–1028; 03.K §3; 03.K.2; adenda 03.CO-02 | §7, §13 | §45–§47 (V2 aprobada) | `contacto.html`; sin capturas | 6/6 | WGR-020, 021, 022, 033, 056, 082 |

Todas las maquetas usan logotipo tipográfico provisional (WGR-060) y enlaces de demostración; ninguna aporta el pie global definitivo (WGR-054).

## 2. Elementos globales

| Elemento | D03 | D04 | D05 | Maquetas | Estado / incidencia |
|---|---|---|---|---|---|
| Cabecera y menú | L141–143; L165; 03.J §3 | §3 | §12 C01 v0.3 (VIS-020…024, CA-01…CA-07) | Navegación global en CAP/CO/PE/SB (con «Inicio» visible); navegación local en Inicio/INF/ENE/DIG/SEC | Especificación aprobada; composición heterogénea · WGR-055, WGR-070 |
| Migas | L255, L392, L531, L1108 | — | VIS-024 | Solo en la ficha PE | Requeridas, sin diseño · WGR-057 |
| Enlace de salto | 03.J §5 | — | CA-06.1 | Ausente en Inicio, INF, DIG, SEC | WGR-058 |
| Selector de idioma | L142 | §3 | VIS-022, CA-07 | «ES» en Inicio/SEC; ausente en el resto | WGR-062, WGR-032 |
| Pie | L143; adenda CO-02 | §13 | VIS-023, §47.1 | Distinto en cada maqueta; teléfono solo en CO | WGR-054 |
| Formulario | CO-02; 03.K §3; 03.K.2 | §7, §13 | §13.12 C05 (no producido), §45–§47 | Desactivado; sin estados | WGR-020, 021, 033, 056 |
| Créditos de imagen | 03.K §5 | §4 `Media` | §23.1, §26.2 | Sin créditos | WGR-034, WGR-061 |
| SEO por página | L663–664, L769–770, L900, L976–977, L1027–1028 | §3 | — | `<title>` de maqueta no fiable | Faltan Inicio, CAP, INF, ENE · WGR-040 |

## 3. Detalle por página

### 3.1 Inicio (H01–H07)

| Bloque D03 | Composición aprobada (D05) | Componente | Recurso | Observaciones de la maqueta |
|---|---|---|---|---|
| H01 L55 | Hero asimétrico, texto separado de la foto (§23.1) | `PageHero` `home` | R24 (CC BY 2.0) | Literal. Dos CTA correctos |
| H02 L65 | Tres tarjetas de igual peso con imagen superior | `ContentCard` `capability` ×3 + enlace al índice | R23, R22, R21 | Literal; los enlaces de tarjeta apuntan a `#necesidades` (demo) |
| H03 L86 | Apertura asimétrica + necesidades 2×2 | `NeedList` (4) + `MediaFigure` | R03 | Literal; pie de foto «fotografía contextual…» no está en D03 (WGR-027) |
| H04 L106 | Dos columnas + cuatro pasos numerados | Bloque de proceso | — | Literal; eyebrow «CRITERIO DE INGENIERÍA» no está en D03 |
| H05 L118 | Banda pino + cuatro grupos 2×2 | `ContentCard` `sector` (selección) | — | Etiquetas «propuestas» en D03 (WGR-025) |
| H06 L129 | Respiro editorial sin proyectos | Bloque editorial | — | Panel «Trayectoria profesional / Experiencia del equipo…» no está en D03 (WGR-027) |
| H07 L135 | Cierre y CTA | `ContactBand` | — | Literal; el pie solo muestra el correo (falta el teléfono) |

### 3.2 Capacidades (C01–C05)

| Bloque | Composición aprobada (§35.1) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| C01 L170 | Hero tipográfico compacto, ancla `#especialidades` | `PageHero` `interior` | — | Literal |
| C02 L179 | Tres filas editoriales numeradas | `ContentCard` `capability` (variante filas) | — | Literal; rótulo «C02 / …» de maqueta (WGR-027) |
| C03 L205 | Banda arena, tres casos con enlaces | Bloque editorial de integración | — | Literal, pero sin la etiqueta «Ejemplos de aplicación» que exigen D03 L246 y D05 §33.4 (WGR-028) |
| C04 L218 | Cuatro modalidades 2×2 sin flechas | `DeliverableList` (modalidades) | — | Literal |
| C05 L231 | Cierre pino + enlace a experiencia | `ContactBand` | — | Literal. Gris `#8D968E` a 2,8:1 (WGR-053) |

### 3.3 Infraestructuras e instalaciones (INF-01–INF-07)

| Bloque | Composición aprobada (§26.1) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| INF-01 L296 | Hero de especialidad con foto | `PageHero` `specialty` | R18 (CC0) | Literal; sin migas (WGR-057) |
| INF-02 L307 | Cinco necesidades en lista numerada | `NeedList` (5) | — | Literal |
| INF-03 L320 | Cuatro ámbitos 2×2 + banda transversal | `ContentCard` `technical-area` + banda transversal | — | Literal; las referencias de catálogo INF-nn son internas (D03 L352) |
| INF-04 L354 | Lista editorial de entregables | `DeliverableList` | — | Literal |
| INF-05 L366 | Bloque arena con enlaces ENE/DIG | Bloque de relación | — | Enlaces demo `#inf01`; sin diagrama (WGR-050) |
| INF-06 L373 | Experiencia editorial sin panel | Bloque editorial | — | Literal |
| INF-07 L382 | Cierre pino y CTA | `ContactBand` | — | Literal |

### 3.4 Sistemas energéticos (ENE-01–ENE-07)

| Bloque | Composición aprobada (§28.2, §29) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| ENE-01 L436 | Hero asimétrico | `PageHero` `specialty` | R10 (CC BY-SA 4.0) | Literal |
| ENE-02 L448 | Seis necesidades 3/2/1 columnas | `NeedList` (6) | — | Literal |
| ENE-03 L460 | Seis capítulos numerados en tres zonas; nota hídrica diferenciada | `ContentCard` `technical-area` (variante capítulos) | R08 (CC BY-SA 4.0) | Literal; la nota hídrica (L495) no debe parecer séptimo ámbito |
| ENE-04 L498 | Banda pino con cuatro entregables | `DeliverableList` | — | Literal |
| ENE-05 L508 | Fondo papel, enlaces INF/DIG | Bloque de relación | — | Enlaces demo |
| ENE-06 L516 | Editorial sin proyectos | Bloque editorial | — | Literal |
| ENE-07 L523 | Cierre corporativo | `ContactBand` | — | Literal |

### 3.5 Automatización y control (DIG-W01–DIG-W07)

| Bloque | Composición aprobada (§30.2, §31) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| DIG-W01 L585 | Hero dos columnas | `PageHero` `specialty` | R01 (CC BY-SA 3.0) | Literal |
| DIG-W02 L593 | Cinco necesidades 2/1 columnas | `NeedList` (5) | — | Literal; ancla `#necesidades` |
| DIG-W03 L602 | Seis tarjetas 2 columnas × 3 filas + transversal | `ContentCard` `technical-area` + banda transversal | R03 (repetición aceptada, §31) | Literal; etiquetas técnicas visibles |
| DIG-W04 L633 | Lista abierta + nota | `DeliverableList` | — | Literal |
| DIG-W05 L641 | Fondo arena, dos relaciones | Bloque de relación | — | Enlaces demo |
| DIG-W06 L647 | Editorial sin referencias | Bloque editorial | — | Literal |
| DIG-W07 L652 | Cierre pino | `ContactBand` | — | Literal |

D03 L663–664 fija title y meta de DIG.

### 3.6 Sectores (SEC-01–SEC-05)

| Bloque | Composición aprobada (§37, §39) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| SEC-01 L708 | Hero editorial sin foto, dos CTA | `PageHero` `interior` | — | Literal |
| SEC-02 L715 | Seis tarjetas 2×3, acento superior, enlace a capacidad + catálogo 0/1/N | `ContentCard` `sector` + VIS-SEC-01/02 | Sin PDF reales | Literal; catálogos de Industria ilustrativos y no descargables |
| SEC-03 L749 | Banda arena + enlace a Capacidades | Bloque editorial | — | Literal |
| SEC-04 L754 | Banda colaboración + Sobre BAFRAS | Bloque editorial | — | Literal |
| SEC-05 L759 | Cierre pino | `ContactBand` | — | Literal |

`sector_id` estables en adenda 03.SEC.CAT-01 (L1245 y ss.). Con cero catálogos publicados no se renderiza ningún control (WGR-086).

### 3.7 Proyectos y experiencia (PE-01–PE-04 y ficha)

| Bloque | Composición aprobada (§40, §41) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| PE-01 L810 | Hero tipográfico + nota de atribución | `PageHero` `interior` | — | Literal |
| PE-02 L819 | Tres grupos con anclas; 3 destacadas + 3 complementarias | `ExperienceCard` `featured`/`compact` (VIS-PE-01) | Ninguno autorizado | **Textos provisionales no publicables**; etiqueta de atribución por decidir (WGR-023); variante sin referencias por decidir (WGR-026) |
| PE-03 L851 | Banda arena | Bloque editorial | — | Literal |
| PE-04 L856 | Cierre pino | `ContactBand` | — | Literal |
| Ficha | VIS-PE-02 modular | Plantilla de ficha | — | Campos entre corchetes = plantilla; no generar fichas sin evidencia |

### 3.8 Sobre BAFRAS (SB-01–SB-05)

| Bloque | Composición aprobada (§44.1) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| SB-01 L925 | Hero tipográfico | `PageHero` `interior` | — | Literal. **Desbordamiento a 320 px** (WGR-059) |
| SB-02 L933 + 03.K §1 L1184 | Tres fichas equivalentes sobre arena | `FounderProfile` (VIS-SB-01) | Sin retratos autorizados | Falta el texto de presentación de 03.K y las titulaciones; especialidades distintas de 03.K (WGR-024) |
| SB-03 L945 | Cuatro principios 2×2 + nota | Bloque de proceso | — | Literal |
| SB-04 L957 | Banda editorial | Bloque editorial | — | Literal; enlace en verde sobre arena a 4,31:1 (WGR-052) |
| SB-05 L966 | Cierre pino, dos CTA | `ContactBand` | — | Literal |

### 3.9 Contacto (CO-01–CO-04)

| Bloque | Composición aprobada (§47.1) | Componente | Recurso | Observaciones |
|---|---|---|---|---|
| CO-01 L981 | Hero claro | `PageHero` `interior` | — | Usa la introducción V1.1, no la de 03.K (WGR-021) |
| CO-02 L987 | Formulario principal (4 campos, 3 obligatorios) desactivado | `ContactForm` | — | Etiquetas correctas; ayuda V1.1 (WGR-021); estados sin diseño (WGR-056) |
| CO-03 L1003 | Columna de contacto directo con correo y teléfono | Contacto directo | — | H2 y párrafo no coinciden con D03 (WGR-022); panel «Antes de escribirnos» no está en D03 (WGR-027); `info@bafras.com` a 4,31:1 (WGR-052) |
| CO-04 L1013 | Cierre contextual | Bloque editorial | — | Literal |

## 4. Verificaciones pendientes comunes a las nueve páginas

1. Revisión visual humana en navegador, teclado, lector de pantalla y zoom 200 % sobre `dist` (WGR-071, WGR-074).
2. Paridad automática D03 → contenido estructurado → `dist` (WGR-073).
3. Derechos y créditos de cada imagen publicada (WGR-034, WGR-061, WGR-084).
4. Rutas definitivas, enlaces internos y metadatos (WGR-031, WGR-040).
5. Eliminación de toda marca de prototipo, rótulo interno y copy ajeno a D03 (WGR-027).
