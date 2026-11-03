# BAFRAS WEB — WEB-G1-REVIEW-01
## Auditoría multidisciplinar, corrección ejecutiva y consolidación del paquete G1

**Fecha:** 03/11/2026. **Ámbito:** `docs/project_v02/` y su relación con el repositorio `bafras/`. **Naturaleza:** auditoría documental, técnica y visual con correcciones documentales acotadas. **No se ha modificado código productivo, no se ha iniciado la refactorización y no se ratifica G1 en nombre de dirección.**

**Documentos de la revisión:** este informe; `WEB_G1_REVIEW_01_INCIDENCIAS.csv` (61 incidencias); `WEB_G1_REVIEW_01_TRAZABILIDAD.md`; `WEB_G1_REVIEW_01_PLAN_IMPLEMENTACION.md`; evidencias en `evidencias_WEB_G1_REVIEW_01/`.

---

## 1. Resumen de resultados

- **El contrato es coherente en lo fundamental.** D03 V1.22, D04 V2.4 y D05 V4.12 no se contradicen en arquitectura, alcance de páginas ni stack. Las nueve composiciones están aprobadas individualmente (D05 §47.3) y las maquetas reproducen el copy D03 casi literalmente en siete de nueve páginas.
- **Hay un bloqueo de gobierno real.** El contrato G1 (D04 §8, D05 §8.5) exige diagramas conceptuales INF/ENE/DIG, pero las composiciones aprobadas los descartan expresamente. El acta G1 no puede firmarse tal como está redactado el contrato sin registrar una excepción (**WGR-050, P0**).
- **El copy de Contacto no es implementable sin decisión editorial.** D03 contiene tres versiones del mensaje de éxito/error, dos introducciones y una ayuda duplicada, y no tiene copy aprobado para el bloque con teléfono (**WGR-020…022**).
- **Primera verificación en navegador del paquete.** Chrome 156 headless funcionó en este entorno, a diferencia de B01 y AUD-G1-03. Resultados:
  - Desbordamiento horizontal: 59 de 60 combinaciones maqueta × ancho correctas. Sobre BAFRAS desborda 27 px a 320 px.
  - Contraste: el par verde `#1A7A5A` sobre arena `#ECE8DD` (4,31:1) se usa como texto normal en las nueve maquetas.
  - Esto no constituye QA visual completo ni WCAG.
- **Faltan piezas del paquete.** No están D02 (primera autoridad de la jerarquía) ni D01. Tampoco AUD-G1-01, los CSV de AUD-G1-03, el script de QA ni los prototipos de integración que D04 §14 da por disponibles.
- **Preparación: READY WITH CONDITIONS.** WEB-G2-00 puede empezar ya, porque no toca código productivo. WEB-G2-01 y siguientes requieren el acta G1 firmada con cuatro excepciones registradas.

## 2. Inventario documental

Integridad: las 19 entradas del manifiesto original verificaban SHA-256 al iniciar. Tras esta revisión, el manifiesto se ha recalculado.

| Artefacto | Versión vigente identificada | Estado | Observación |
|---|---|---|---|
| D02 Posicionamiento | — | **Ausente** | No existe en ninguna ruta del proyecto (WGR-002) |
| D01 Taxonomía de servicios | — | **Ausente** | Citado por D03 como rector de publicación de servicios (WGR-002, 084) |
| `03_contenido_editorial_V1_22_baseline_G1.md` | V1.22 | Copy aprobado (8 páginas); PE con arquitectura aprobada y referencias provisionales | La cabecera no indicaba versión (corregido) |
| `04_arquitectura_software_V2_4_handoff_G1.md` | V2.4 (cuerpo V2.0 + §11–§14) | Aprobado en decisiones principales | La cabecera decía V2.0 (corregido) |
| `05_sistema_visual_V4_12_baseline_G1.md` | V4.12 (§48) | 9/9 composiciones aprobadas | La cabecera decía V3.9 (corregido) |
| Maquetas `maquetas_aprobadas/*.zip` (9) | Inicio V3, CAP V1, INF V2, ENE V2, DIG V1, SEC V3, PE V1, SB V1, CO V2 | Aprobadas (D05 §48) | Coinciden con D05 §48. Capturas solo en CAP (5), PE (8) y SB (1) |
| `soporte_auditoria/AUD-G1-02_*` | Basados en D04 V2.3 / D05 V4.11 | Catálogo pendiente de aceptación | Contenido compatible con las versiones vigentes (WGR-009) |
| `soporte_auditoria/AUD-G1-03_*` | Basados en D03 V1.21 | Informe y plan de cierre | Citan CSV y script ausentes (WGR-003) |
| AUD-G1-01 | — | **Ausente** | Citado por D04 §14 (WGR-003) |
| `01_Briefing_Tecnico_Desarrollo.md` | DEV-HANDOFF-01 | Vigente | Matriz de anchos reducida (corregido) |
| `02_Acta_Propuesta_Cierre_G1.md` | Propuesta | **Sin firmar** | Matriz de anchos corregida; referencia a decisiones previas añadida |
| `00_Inventario_Artefactos.md`, `99_Manifest_SHA256.md` | — | Vigentes | Manifiesto recalculado |
| `BAFRAS_WEB_B01_AUDITORIA_REPOSITORIO.md` | B01 | Histórico (repositorio antiguo) | Conservado sin cambios, como establece B02-PREP-01 |
| `B02_PREP_01_INVENTARIO_RECURSOS_VISUALES.md` | B02-PREP-01 | Inventario de 55 recursos | Dos enlaces rotos corregidos |
| `../../../B02_Auditoria_Visual_BAFRAS/` (fuera del repositorio) | B02.0 | 86 capturas del sitio público v9 | Evidencia G0 no registrada en el paquete (WGR-075) |

No hay duplicados de D03, D04 ni D05: cada uno tiene una sola versión en el paquete. El historial de versiones previas no está en Git porque `docs/project_v02/` está **sin seguimiento**. Por eso las correcciones de esta revisión se documentan en §5 y en el manifiesto, y conviene confirmarlas en Git.

## 3. Evaluación por disciplina

**Producto / dirección.** Alcance, nueve páginas, menú de seis destinos y reglas de atribución son coherentes entre D03, D04 y D05. Quedan abiertas decisiones de producto concretas:
- variante de lanzamiento de Proyectos y experiencia sin referencias autorizadas (WGR-026);
- idiomas de lanzamiento (WGR-032);
- proveedor de formulario y hosting (WGR-033, 039);
- logo maestro (WGR-060);
- metadatos SEO de cuatro páginas (WGR-040).

**Arquitectura de software.** El stack y los límites de capas son claros y proporcionados (D04 §1–§2), y el contrato de catálogos PDF (§11–§12) es completo y comprobable. Lo que falta es concreción de contratos, no una arquitectura distinta:
- el modelo de contenido no cubre configuración de sitio, navegación, sector, persona, cadenas de interfaz ni SEO (WGR-030);
- `Media` no tiene campos para la atribución que exigen 7 de las 9 imágenes asignadas, con licencias CC BY/BY-SA (WGR-034);
- las rutas siguen «propuestas» (WGR-031);
- no hay dependencias declaradas ni build reproducible (WGR-037);
- hay trabajo sin confirmar en el repositorio que condiciona el rollback (WGR-036).

No se justifica ninguna dependencia ni servicio adicional, salvo PyYAML (opcional) y el proveedor de envío del formulario.

**UX/UI y marca.** La gramática visual es consistente: pino, verde, papel, arena, línea, tinta e Inter en las nueve maquetas, y los tokens heredados coinciden. Problemas:
- La especificación del sistema visual (D05 §8.1, §8.7; VIS-010…019) sigue «en validación». Cada maqueta define su contenedor (1200–1280 px), sus cortes (350–1100 px) y su escala tipográfica (WGR-051).
- Faltan diseños de elementos que exige el contrato: pie único (WGR-054), estados del formulario (el paquete C05 nunca se produjo, WGR-056), migas (WGR-057) y créditos de imagen (WGR-061).
- La exigencia de diagramas no se ha cumplido (WGR-050).

**Frontend y accesibilidad.** Las maquetas son buenas referencias semánticas: un H1 por página, landmarks y la mayoría con enlace de salto. Pero no son reutilizables como código:
- cabeceras heterogéneas y navegación local de página (WGR-055);
- sin enlace de salto en cuatro maquetas (WGR-058);
- grises locales fuera de tokens con contraste insuficiente (WGR-053);
- el par verde/arena por debajo de 4,5:1 (WGR-052);
- desbordamiento de Sobre BAFRAS a 320 px (WGR-059).

**QA.** La matriz de anchos estaba reducida en el briefing, el acta y D04 §14 respecto a lo aprobado en D05 §12.5. Se ha unificado en 320/375/390/768/1024/1440 px + zoom 200 %. Sobre la paridad editorial, como el contenido productivo se ingerirá de datos derivados de D03, el criterio correcto es D03 → contenido → `dist`, no maqueta → D03 (WGR-073). Sin ejecutar: teclado, lector de pantalla, zoom 200 % y revisión visual humana (WGR-071, 074).

## 4. Principales incoherencias

| # | Incoherencia | Fuentes | Tratamiento |
|---|---|---|---|
| 1 | Diagramas exigidos por G1 frente a composiciones aprobadas sin diagramas | D05 §8.5, §4, §5 / §25.1, §28.2, §30.1, §35.1 | Decisión en acta (WGR-050) |
| 2 | Tres textos de éxito/error del formulario | D03 L998-999, L1209, L1237 | Decisión editorial (WGR-020) |
| 3 | Dos versiones de la introducción CO-01 y de la ayuda CO-02; la maqueta usa la antigua | D03 L985, L993 / L1207-1208 | Decisión editorial (WGR-021) |
| 4 | Teléfono autorizado sin copy CO-03; la maqueta introduce texto no aprobado | D03 L1003-1011, L1287-1293; maqueta CO V2 | Decisión editorial (WGR-022) |
| 5 | Etiquetas de atribución con tres o cuatro formulaciones | D03 L804, L817, L868, L1195; D05 §6 | Decisión editorial (WGR-023) |
| 6 | Ficha de equipo de la maqueta SB distinta de 03.K | D03 L938-943 / L1184-1192; D05 §42.2 | Implementar 03.K (WGR-024) |
| 7 | Cabeceras de versión desfasadas en D03, D04 y D05 | Cabeceras | **Corregido** (WGR-001) |
| 8 | Matriz de anchos de prueba reducida en tres documentos | D04 §14, briefing, acta / D05 §12.5 | **Corregido** (WGR-006) |
| 9 | Evidencias citadas como disponibles y ausentes | D04 §14, AUD-G1-03 | Nota añadida; pendiente de incorporar (WGR-003) |
| 10 | Copy ajeno a D03 en las maquetas (eyebrows, paneles, pies) | Inicio V3, CAP, CO, PE, SB | No publicar (WGR-027) |

## 5. Correcciones ejecutadas

Todas son documentales, respaldadas por una fuente de autoridad explícita y sin cambios de copy, diseño ni arquitectura:

| Archivo | Corrección | Autoridad |
|---|---|---|
| `03_contenido_editorial_V1_22_baseline_G1.md` | Versión V1.22 en la cabecera. Nota de control: estado ENE/DIG superado por D05 §29/§31; inventario de bloques de D04 inexistente; 03.J §7 superado por D04; divergencias remitidas al CSV. **Sin cambios de copy ni de filas del registro** | Nombre de archivo, briefing, acta, D04 §14, adenda 03.G1-01 |
| `04_arquitectura_software_V2_4_handoff_G1.md` | Cabecera V2.4 y referencia a D03 V1.22 y D05 V4.12. §14: anchos 375/1024 px y zoom 200 % añadidos a los criterios diferidos; nota sobre evidencias ausentes | D05 §12.5, CA-C02-10; inspección del paquete |
| `05_sistema_visual_V4_12_baseline_G1.md` | Cabecera V4.12 y nota de que el «Estado rector» inicial es histórico frente a §47.3/§48 | D05 §48 |
| `01_Briefing_Tecnico_Desarrollo.md` | §2 evidencias realmente incluidas; §8 G1-002 con el resultado de esta revisión; §9–§10 matriz de seis anchos + zoom | D05 §12.5 |
| `02_Acta_Propuesta_Cierre_G1.md` | Matriz de seis anchos + zoom; apartado «Decisiones previas recomendadas» que remite a §10 de este informe. **Decisión propuesta y casillas sin cambios** | D05 §12.5 |
| `B02_PREP_01_INVENTARIO_RECURSOS_VISUALES.md` | Dos enlaces rotos redirigidos a los archivos vigentes | Renombrado de archivos |
| `99_Manifest_SHA256.md` | Hashes recalculados; entregables y evidencias de esta revisión añadidos | Integridad del paquete |

No se han modificado las maquetas, AUD-G1-02/03 ni B01 (son evidencias), ni ningún archivo fuera de `docs/project_v02/`.

## 6. Incidencias pendientes

61 incidencias registradas: 6 corregidas, 4 aceptadas como no bloqueantes, 5 parciales y 46 abiertas.

| Severidad | Abiertas o parciales | Tipos principales |
|---|---|---|
| **P0** | 7 | 1 de gobierno (acta G1, WGR-090); 1 de diseño (diagramas, WGR-050); 5 de publicación (referencias, perfiles, contacto operativo, legal, derechos/servicios: WGR-080…084) |
| **P1** | 25 | Decisiones editoriales de Contacto, atribución y SEO; contratos de modelo, rutas y medios; tokens, contraste, pie y estados del formulario; QA heredado de AUD-G1-03 |
| **P2** | 19 | Diseño menor (cabecera, migas, selector); implementación (enlace de salto, desbordamiento, grises, pruebas heredadas); documentación |

Las P0 de publicación (WGR-080…084) **no son defectos demostrados**: son verificaciones previas obligatorias que D03 03.J §8 ya clasificaba como bloqueantes de lanzamiento. No bloquean G2 ni G3.

Consolidación de auditorías previas:

| Origen | Correspondencia |
|---|---|
| AUD-G1-03 G1-001…004 | WGR-070…073 |
| D03 03.J P0-01…05 | WGR-080…084 |
| B01-03 | WGR-080 |
| B01-04 | WGR-033 |
| B01-05 | WGR-083 |
| B01-08 | WGR-038 |
| B01-09 | WGR-031 |
| B01-14 | WGR-037 |
| B01 DOC-04 | WGR-011 (resuelto) |
| B01 DOC-06 | Resuelto por B02-PREP-01 |
| B01 DOC-07 | Resuelto por D05 VIS-027 («2 columnas × 3 filas») |
| B01 DOC-08 | WGR-020 |
| B01 DOC-10 | WGR-039 |

El resto de hallazgos de B01 describen el sitio antiguo, que se sustituirá; no se arrastran como incidencias.

## 7. Riesgos

| Riesgo | Probabilidad / impacto | Mitigación |
|---|---|---|
| Firmar G1 sin registrar la excepción de diagramas deja el acta en contradicción con D04 §8 | Alta / alto | Excepción explícita en el acta (WGR-050) |
| Implementar Contacto con copy de la maqueta en lugar de D03 | Media / medio | Decisiones WGR-020…022 antes de G3-01a; test de paridad |
| Publicar imágenes CC BY/BY-SA sin crédito ni aviso de modificación | Media / alto (legal) | `Media` con campos de licencia y build que falle (WGR-034) |
| Normalizar tokens alterando la estética aprobada | Media / medio | Hoja de tokens aprobada por Diseño antes de las plantillas (WGR-051) |
| Perder trabajo sin confirmar del repositorio al migrar | Media / alto | Confirmar o crear rama antes de G2-01 (WGR-036) |
| G3 bloqueado por falta de proveedor de formulario | Alta / medio | Dividir G3-01 en a/b y decidir el proveedor en paralelo (WGR-033) |
| Lanzar Proyectos y experiencia sin referencias verificadas | Media / alto (reputación) | Variante sin tarjetas aprobada (WGR-026) |
| Paquete documental sin control de versiones | Alta / medio | Confirmar `docs/project_v02/` en Git tras revisar este diff |

## 8. Evaluación de preparación para implementación

**Clasificación: READY WITH CONDITIONS.**

Justificación:
- **Requisitos e integridad editorial:** completos para ocho páginas. En PE la estructura está aprobada y la variante sin referencias es implementable. Las divergencias de copy están acotadas a Contacto, atribución y SEO, con fuentes localizadas.
- **Coherencia visual:** nueve composiciones aprobadas con gramática común; las lagunas (tokens, pie, estados, migas, créditos) pueden resolverse en G2-02 con un punto de aprobación de Diseño, sin rediseñar.
- **Viabilidad arquitectónica:** alta. Stack proporcionado, contratos verificables y convivencia sin corte con el sitio actual.
- **Recursos:** las imágenes asignadas existen y son idénticas byte a byte en maquetas y biblioteca. Licencias declaradas, no verificadas.
- **Navegación y contenidos:** contrato de navegación definido; rutas pendientes de ratificar en G2-00.
- **No es BLOCKED:** no hay contradicciones fundamentales de alcance, stack ni contenido aprobado.
- **No es READY:** el acta G1 no está firmada y su contrato exige un entregable (diagramas) que las aprobaciones posteriores descartan.

**Condiciones:**
1. Acta G1 firmada con las excepciones WGR-050, 051, 052 y 063.
2. Repositorio confirmado o con rama de baseline (WGR-036).
3. Decisiones editoriales de Contacto y SEO antes de G3-01a.
4. Proveedor de formulario antes de G3-01b.

## 9. Recomendación sobre la ratificación de G1

**Recomendación: ratificar G1 con condiciones, en el acta existente, registrando expresamente:**

1. **Excepción de diagramas (WGR-050):** los diagramas conceptuales INF/ENE/DIG de D05 §8.5 no se exigen para G1. Las composiciones aprobadas funcionan sin ellos, y los diagramas quedan como iteración posterior opcional, sujeta a datos reales.
2. **Normalización de tokens (WGR-051):** la especificación final de tokens (contenedor, cortes, escala, espaciado) se cierra en WEB-G2-02 a partir de las maquetas aprobadas, sin cambio estético, con aprobación de Diseño.
3. **Regla de contraste (WGR-052):** verde `#1A7A5A` sobre arena solo para texto grande; texto pequeño sobre arena en pino o tinta. No cambia la paleta.
4. **Catálogo de componentes (WGR-063, 072):** aceptar AUD-G1-02 más el complemento del plan (§2, WEB-G2-02).
5. **Verificaciones diferidas:** las del acta, con la matriz de seis anchos + zoom ya corregida.

Las demás decisiones (pie, cabecera, migas, selector, estados del formulario, créditos) son concreciones dentro de patrones aprobados. Pueden delegarse a puntos de aprobación de Diseño en G2-02 y G3-01b sin reabrir la estética.

Si dirección prefiere no aceptar la excepción 1, la alternativa es encargar los tres diagramas antes de ratificar. En ese caso, la clasificación pasa a BLOCKED para WEB-G2-01 hasta su aprobación.

## 10. Próximas decisiones de dirección

| # | Decisión | Incidencia | Antes de |
|---|---|---|---|
| 1 | Firmar el acta G1 con las excepciones de §9 | WGR-090, 050, 051, 052, 063 | WEB-G2-01 |
| 2 | Confirmar en Git el trabajo previo y `docs/project_v02/` | WGR-036 | WEB-G2-01 |
| 3 | Aportar D02 y D01 al paquete, o indicar su ubicación | WGR-002 | WEB-G2-00 / G4 |
| 4 | Copy de Contacto: éxito/error, introducción, ayuda y bloque con teléfono (recomendación: 03.K/03.K.2 y adenda CO-03; **revisada en `WEB_G1_CLOSE_DECISIONES.md` DEC-04**: introducción y ayuda de CO-01/CO-02 V1.1) | WGR-020, 021, 022 | WEB-G3-01a |
| 5 | Title/meta de Inicio, Capacidades, INF y ENE; etiquetas H05 definitivas | WGR-040, 025 | WEB-G3-01a |
| 6 | Proveedor de envío del formulario y hosting | WGR-033, 039 | WEB-G3-01b / G4 |
| 7 | Etiquetas canónicas de atribución y variante de Proyectos y experiencia sin referencias | WGR-023, 026 | WEB-G3-02 |
| 8 | Logo maestro y ubicación de créditos de imagen | WGR-060, 061 | WEB-G2-02 |
| 9 | Idiomas de lanzamiento (recomendación: ES) | WGR-032 | WEB-G4-01 |
| 10 | Titular jurídico, textos legales, verificación de licencias y referencias | WGR-080…084 | Publicación |

**Primera intervención recomendada:** WEB-G2-00, que es compatible con el estado actual porque no modifica código productivo.

---

### Anexo A · Método y evidencias

- **Lectura completa:** D03, D04, el núcleo y las actas de D05 (§1–§13 y §23–§48; §14–§22 consultadas por secciones), briefing, acta, inventario, manifiesto, AUD-G1-02/03, B02-PREP-01 (§1–§10) y las nueve maquetas extraídas en un directorio temporal fuera del repositorio.
- **Comprobaciones ejecutadas:**
  - Manifiesto: `sha256sum -c`, 19/19 correctas al inicio.
  - Enlaces Markdown internos: 96 enlaces, 2 rotos, ahora corregidos.
  - Hashes de las imágenes de las maquetas frente a la biblioteca: 10/10 idénticas.
  - Inventario estructural de las maquetas: `evidencias_WEB_G1_REVIEW_01/inventario_maquetas.txt`.
  - Desbordamiento a seis anchos: `desbordamiento_resultados.json`.
  - Contraste indicativo: `contraste_resultados.json`.
  - Comprobaciones del repositorio sin cachés: `python -B tools/validate.py` pasa con 33 avisos de placeholders y 10 de verificación, igual que en B01; `python -B -m pytest -p no:cacheprovider -q`: 18 pasadas.
- **Método de navegador:** Chrome 156.0.8078.76 headless. La ventana mínima es de 512 px, así que se midió dentro de un iframe de ancho fijo con la barra de desplazamiento oculta. Solo se mide desbordamiento horizontal y contraste de texto sobre fondo sólido. **No se han ejecutado** revisión visual humana, teclado, lector de pantalla, zoom 200 % ni auditoría WCAG; no se declaran superados.
- **Sin dependencias instaladas** y sin cambios fuera de `docs/project_v02/`.
