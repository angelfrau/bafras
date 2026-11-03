# BAFRAS ENGINEERING — DOCUMENTO 05
## Sistema visual y diseño UX/UI · V4.12 — línea base visual G1 (§48) · 03/11/2026

**Nota de control documental WEB-G1-REVIEW-01 (03/11/2026):** la cabecera original de este documento identificaba la versión V3.9 (C04 Capacidades V1 validada). El párrafo «Estado rector» siguiente se conserva como histórico de esa versión; el estado vigente de las nueve composiciones es el de §47.3 y §48 (9/9 aprobadas; G1 pendiente de ratificación expresa). No se modifica ninguna decisión de diseño.

**Estado rector (03/11/2026):** C01 aprobado; C02 correcciones validadas; C03 recursos registrados; C04 **Inicio V3, Infraestructuras V2, Sistemas energéticos V2 y Automatización y control V1 aprobados en composición por el promotor**. R24/H01, R23–R22–R21/H02, R03/H03, R18/INF, R10+R08/ENE y R01+R03/DIG quedan vinculados a las maquetas aprobadas; la repetición de R03 en DIG fue expresamente aceptada al validar DIG V1. **Capacidades (C01–C05) V1 aprobada en composición por el promotor**. G1 y QA de navegador, responsive, accesibilidad, localización, navegación y publicación siguen pendientes. D03 es fuente de contenido, D05 de diseño y D04 de arquitectura. Los estados históricos no prevalecen sobre estas aprobaciones.

## 1. Criterios vinculantes

Reutilizar sin alterar arbitrariamente logotipo, paleta, tipografías, símbolos y activos reales BAFRAS. La identidad existente se extraerá de los CSS y recursos del repositorio. Diseño sobrio, preciso, técnico, contemporáneo, legible, sin recursos de stock que simulen proyectos. **Diseño visual detallado y aprobado antes de refactorizar código productivo** (gate G1 del Documento 04).

**Pendiente de inspección:** HEX, fuentes, tamaños y pesos tipográficos reales, breakpoints y componentes existentes. Ningún valor numérico propuesto se considerará token definitivo sin comprobarlo contra el repositorio. Mantener nomenclatura existente cuando sea clara; normalizar solo duplicados o inconsistencias verificadas.

## 2. Gramática visual común

**Composición:** cabecera consistente, hero con título claro, introducción y CTA; secciones con jerarquía H2/H3, espacios regulares, ancho de lectura controlado; pie común. En escritorio, contenedor aprox. 1120–1240 px a validar; grid CSS sin framework; en móvil una columna para contenido técnico, con diagramas adaptados, no miniaturizados. No imponer idéntica distribución a las nueve páginas.

**Tipografía:** escala fluida `clamp()` cuando resulte apropiado, tamaños legibles, longitud de línea de 65–75 caracteres como referencia, especial atención a títulos en alemán y accesibilidad. **Color:** usar paleta real y tokens semánticos para superficies, texto, acento, enlaces, bordes, foco y estados; no asignar nuevos colores arbitrarios a INF/ENE/DIG. **Movimiento:** mínimo, respetar `prefers-reduced-motion`. **Contraste y controles:** objetivo WCAG 2.2 AA; foco visible, navegación teclado, objetivos táctiles adecuados, estados de error comprensibles.

**Gráficos técnicos:** ilustraciones vectoriales propias que expliquen relaciones reales; sin cifras ni conexiones inventadas, con leyenda y alternativa textual. Fotografías reales autorizadas; si faltan, no suplir con imágenes que parezcan evidencia de obra. Tablas y gráficos de estudios: títulos, unidades, fuente, metodología/limitaciones y adaptación móvil.

## 3. Biblioteca mínima y nomenclatura única

**Componentes globales:** `SiteHeader` (incluye menú móvil y selector de idioma), `SiteFooter`, `PageHero`, `SectionHeading`, `ContactBand`, `MediaFigure` (variante `technical-diagram`), `ContactForm`.

**Patrones editoriales reutilizables:** `ContentCard` (variantes `capability`, `technical-area`, `sector`), `ExperienceCard` (variantes `featured`, `compact`, `study`), `FounderProfile`, `DeliverableList`, `NeedList`. Un componente se extrae solo cuando hay repetición real o ventaja clara. No crear un componente específico por sección del Documento 03.

**Composiciones específicas:** `IntegratedSystemFigure`, `BuildingServicesFigure`, `EnergyFlowFigure`, `ControlArchitectureFigure`, `StudyResultsSection`. Son **nombres de diseño**, no clases Python obligatorias; pueden implementarse como SVG/HTML semántico y CSS. No confundir componentes visuales con modelos de datos.

## 4. Arquitectura visual por página, vinculada al Documento 03

| Página | Orden visual obligatorio según copy | Composición distintiva | Móvil |
|---|---|---|---|
| **Inicio** H01–H07 | Hero → 3 capacidades → necesidades → filosofía → sectores → experiencia → cierre | Hero asimétrico, visual integrador de INF/ENE/DIG, 3 tarjetas de igual peso | Texto antes del visual; tarjetas apiladas |
| **Capacidades** C01–C05 | Hero → 3 especialidades → integración → colaboración → CTA | Tres paneles amplios con mini-esquemas homogéneos | Una especialidad por fila |
| **Infraestructuras** INF-01–07 | Hero → necesidades → 4 ámbitos + transversal → entregables → conexiones → experiencia → CTA | Esquema de edificio e instalaciones; grid 2×2 | Reemplazar diagrama denso por módulos legibles |
| **Sistemas energéticos** ENE-01–07 | Hero → necesidades → 6 ámbitos + transversal → entregables → conexiones → experiencia → CTA | Red/FV/BESS/demanda/movilidad/térmica; flechas con semántica real | Diagrama por bloques, no escalado ilegible |
| **Automatización** DIG-W01–07 | Hero → necesidades → 6 ámbitos + transversal → entregables → conexiones → experiencia → CTA | Sensores → PLC/DDC → SCADA/BMS → software; conexiones y leyenda | Flujo vertical legible |
| **Sectores** SEC | Hero → 6 sectores → problemas comunes → colaboración → CTA | Retícula 2×3 de tarjetas con iconografía técnica uniforme | Una tarjeta por fila |
| **Proyectos y experiencia** PE | Hero → 3 referencias destacadas → 3 complementarias → CTA | Fotografía autorizada o figura técnica, etiqueta de atribución visible; futura ficha `study` | Tarjetas apiladas; datos clave primero |
| **Sobre BAFRAS** SB | Hero → tres fundadores → filosofía/metodología → experiencia → CTA | Perfiles equilibrados y retratos reales autorizados | Una ficha por fila |
| **Contacto** CO | Hero breve → formulario + email → privacidad | Composición 7/5 aproximada; sin imagen decorativa | Formulario y correo visibles sin fricción |

**Fidelidad:** los textos se extraen del Documento 03, sin recortarlos para que encajen. Si una sección resulta extensa, ajustar composición primero; una propuesta de edición debe tramitarse como cambio editorial separado.

## 5. Detalle de diagramas por especialidad

**INF — instalaciones integradas:** esquema conceptual de edificio con capas eléctricas, climatización, hidráulica y protección; incluir transversal de diagnóstico/coordinación fuera de la ilustración. No presentar como plano de ejecución. **ENE — balance de activos:** entradas/salidas y flujos entre red, FV, almacenamiento y consumos, con flechas correctas; no representar instalación real sin datos. **DIG — arquitectura de control:** diferenciar medida, comunicaciones, control, supervisión y optimización; distinguir señal y actuación con texto/estilo de línea además de color. Los tres comparten grosor de línea, iconografía, tipografía, espaciado y paleta.

## 6. Diseño de proyectos BAFRAS y estudios publicables

La sección Proyectos y experiencia debe distinguir claramente **«Proyecto desarrollado por BAFRAS»** de **«Experiencia profesional previa del equipo»**. No mezclar ambos bajo un encabezado que atribuya trabajos previos a la empresa. La arquitectura existente de tres referencias destacadas y tres complementarias se mantiene como patrón editorial, **no como límite máximo**. Las dos nuevas referencias BAFRAS podrán incorporarse mediante tarjetas adicionales o una subsección identificada, tras validar su contenido y permisos.

**Tarjeta de estudio:** categoría, nombre del proyecto, intervención BAFRAS verificada, imagen o gráfico principal, resumen del hallazgo/alcance, CTA «Ver estudio» solo si la ficha está publicada. No poner datos o gráficos sin contexto. **Ficha de proyecto/estudio futura:** hero breve → contexto y objetivo → alcance/rol BAFRAS → metodología → resultados clave → gráficos/tablas → informe descargable (si autorizado) → límites/supuestos → capacidades relacionadas → CTA. La página debe funcionar aunque el estudio solo aporte un SVG y un PDF; las interacciones JS son mejora opcional.

**Tratamiento visual de resultados:** un único patrón `StudyResultsSection` para encuadre, títulos, pie, unidades y leyenda; no imponer una librería de gráficos a los softwares. Un gráfico generado por Python puede publicarse como SVG/PNG/WebP; tablas como HTML accesible y descarga CSV; informes HTML deben revisarse y aislar estilos/scripts para no romper la web. No reproducir sin adaptación el CSS del informe dentro del sitio.

## 7. Estados y comportamiento responsive

Definir para cabecera, menú móvil, selector de idioma, botones, tarjetas enlazables y formulario: normal, hover, focus-visible, activo, error, éxito y carga donde aplique. Comprobar zoom 200 %, teclado, móvil estrecho, títulos largos CA/DE, SVG adaptados, tablas con encabezados y desplazamiento accesible cuando sea necesario. No usar carruseles automáticos ni ocultar información clave en hover.

## 8. Entregables obligatorios del diseño ANTES del refactor

1. **Inventario de marca real:** paleta HEX, tipografías/licencias, logo, CSS y elementos gráficos, con tabla de tokens actuales → tokens normalizados; capturas de baseline.
2. **Catálogo aprobado de componentes:** catálogo mínimo, variantes reales, tamaños, estados y reglas responsive de navegación, botones, tarjetas, diagramas, módulos de evidencia, formularios y CTA; no una biblioteca ficticia extensa.
3. **Nueve wireframes completos:** uno por página, tanto en escritorio como en móvil, con cobertura y trazabilidad de todos los bloques editoriales del Documento 03; revisar densidad y recorridos.
4. **Tres maquetas completas de alta fidelidad:** Inicio, Infraestructuras e instalaciones y Contacto. Añadir **maquetas detalladas de los módulos visuales singulares de las seis páginas restantes**: Sistemas energéticos, Automatización y control, Sectores, Proyectos y experiencia, Sobre BAFRAS y Capacidades. Deben resolver sus particularidades y permitir reconstruir inequívocamente cada página mediante los patrones y variantes aprobados; no se exigen nueve prototipos completos e independientes de alta fidelidad si se cumple este criterio.
5. **Diagramas conceptuales:** INF, ENE y DIG con lenguaje visual común y versiones móviles.
6. **Especificación de estudios:** tarjeta, ficha y módulo de resultados, demostrados con **muestras anonimizadas** de los dos estudios cuando estén disponibles; la falta de estas muestras no bloquea G1 de la web corporativa.
7. **Especificación del sistema visual:** colores, tipografía, retículas, espaciados, componentes, comportamiento responsive y accesibilidad, con valores reales contrastados contra el repositorio.
8. **Revisión visual global:** demostrar que las nueve páginas, concordantes con el Documento 03, pueden implementarse sin decisiones estéticas fundamentales pendientes; documentar patrones, variantes y excepciones explícitas sin dejar decisiones fundamentales abiertas.
9. **Acta de aprobación expresa de dirección:** registrar documentalmente la aprobación del paquete completo anterior, conforme al contrato G1 del Documento 04, §8, unificado por la decisión B02-PREP-01. La aprobación autoriza planificar la implementación; cualquier intervención productiva requiere su autorización correspondiente y sigue sujeta a los gates posteriores. No acredita por sí misma que recursos gráficos, referencias profesionales, datos técnicos, formulario o requisitos legales estén preparados para publicación. Esta consolidación documental no inicia G1 ni lo declara completado.

## 9. Evaluación multidisciplinar tras consolidación

- **Dirección y comercial:** mensaje y flujo B2B coherentes con Documento 03; se añade espacio explícito para proyectos propios BAFRAS sin falsear atribuciones.
- **Diseño/UX:** una gramática común y nueve composiciones diferenciadas; falta aún validación con marca y maquetas reales.
- **Frontend/accesibilidad:** componentes mínimos, semántica y estados definidos; no se exige JS para leer contenido.
- **Arquitectura:** diseño desacoplado de motor y de estructura de datos; no se duplican decisiones técnicas del Documento 04.
- **Ingeniería de estudios:** gráficos, tablas e informes pueden incorporarse sin rehacer la web; no se presupone formato exacto de los softwares.

**Dictamen:** coherencia conceptual alcanzada; **diseño final NO cerrado** hasta completar y aprobar los entregables de §8 con el repositorio real. La refactorización productiva permanece bloqueada por G1, no por la disponibilidad de los dos estudios.


---

## 10. Acta de consolidación B02.1 — 03/11/2026

**Alcance:** se conserva íntegramente la estructura precedente de D05 y se registra el avance del chat de diseño. Esta actualización documental no equivale al cierre formal de G1 ni autoriza modificaciones productivas.

### 10.1 Decisiones y alcance de aprobación

| ID | Decisión | Justificación | Alcance y estado | Evidencia | Aceptación / condición de verificación |
|---|---|---|---|---|---|
| VIS-001 | Conservar identidad cromática BAFRAS | Continuidad de marca | Principio aprobado | Diagnóstico B02.1-P01 | Paleta contrastada con CSS/activos y accesibilidad |
| VIS-002 | Mantener Inter y mejorar jerarquías | Legibilidad y coherencia | Principio aprobado | Diagnóstico B02.1-P01 | Escala legible en escritorio/móvil |
| VIS-003 | Mantener composición editorial, diversificando patrones | Evitar plantilla repetitiva | Principio aprobado | Diagnóstico B02.1-P01 | Variantes justificadas por función |
| VIS-004 | Sustituir hero sintético | Evitar representación engañosa | Principio aprobado | Diagnóstico B02.1-P01 | Hero final sin atribuciones falsas |
| VIS-005 | Diversificar componentes | Adecuación función-forma | Principio aprobado | Diagnóstico B02.1-P01 | Catálogo sin proliferación gratuita |
| VIS-006 | Distinguir concepto, evidencia y dato | Rigor técnico | Principio aprobado | Diagnóstico B02.1-P01 | Etiquetado y procedencia verificables |
| VIS-007 | Mejorar navegación y accesibilidad | Usabilidad universal | Principio aprobado | Diagnóstico B02.1-P01 | Teclado, lector de pantalla, 320 px y WCAG 2.2 AA |
| VIS-008 | Controlar procedencia visual | Derechos y credibilidad | Principio aprobado | Inventario B02-PREP-01 | Ningún recurso publicado sin autorización |
| VIS-009 | Dirección creativa editorial + documental + sistemas | Une sofisticación, prueba y explicación técnica | **Aprobada** | EV-03 v0.1–v0.4 | Las nueve páginas usan una gramática coherente sin cuotas rígidas |
| VIS-010 | Color y tokens semánticos | Consistencia | **En validación** | EV-03 v0.4 | Valores cotejados con repositorio; contraste medido |
| VIS-011 | Tipografía editorial/técnica | Jerarquía | **En validación** | EV-03 v0.4 | Escala, pesos y textos largos comprobados |
| VIS-012 | Retícula y composición | Flexibilidad | **En validación** | EV-03 v0.4 | Contenedor, columnas y responsive medidos |
| VIS-013 | Espaciado y geometría | Ritmo sobrio | **En validación** | EV-03 v0.4 | Espacios y radios contrastados con CSS |
| VIS-014 | Fotografía documental | Autenticidad | **En validación** | R01–R55, EV-03 | Permisos, recortes y pies documentados |
| VIS-015 | Responsive y accesibilidad | Robustez | **En validación** | EV-03 v0.4 | Pruebas reales 320/390/768/1024/1440, zoom y teclado |
| VIS-016 | Lenguaje de diagramas | Precisión técnica | **Propuesta** | Pendiente INF/ENE/DIG | Conexiones, leyendas y versiones móviles verificadas |
| VIS-017 | Magnitudes y datos | Trazabilidad | **Propuesta** | Pendiente | Unidades, fuente, contexto y alternativa accesible |
| VIS-018 | Estados de interacción | Usabilidad | **Propuesta** | Pendiente | Estados normal/hover/foco/activo/error/carga donde apliquen |
| VIS-019 | Robustez editorial y multilingüe | Fidelidad a D03 | **Propuesta** | Pendiente | No truncar copy; pruebas CA/DE/ES/EN disponibles |

**Validación adicional:** la **composición conceptual de Inicio H01–H07, EV-03 v0.4**, queda aprobada como *referencia de composición y dirección estética*, no como aprobación de textos reconstruidos, métricas ilustrativas, logotipo provisional, recursos publicables, especificaciones dimensionales o prototipo móvil funcional. La aprobación no modifica el Documento 03.

**Evidencia:** EV-03 v0.1, v0.2, v0.3 y v0.4 son identificadores del historial de diseño; antes de G1 deberán archivarse los ficheros/capturas concretos con rutas y versiones verificables. La referencia documental por sí sola no acredita que un archivo esté incorporado al repositorio.

**Recursos:** el inventario B02-PREP-01 enumera R01–R55 y advierte expresamente que la inspección **no acredita permiso de publicación**. Su utilización en prototipos no autoriza publicación.

### 10.2 Dictamen de cierre de B02.1

La **dirección creativa y composición maestra están validadas**. El cierre **documental intermedio** se registra con esta revisión. El cierre **técnico completo de fundamentos** sigue condicionado a la inspección del repositorio y las evidencias dimensionales/responsive. B02.2 puede iniciarse sin esperar a que se cierre G1.

### 10.3 Implicaciones para revisión posterior de D04

- Confirmar contratos de rutas y localización del menú a partir de D03/D04.
- Verificar cómo se obtiene el idioma actual y la disponibilidad de traducciones.
- Asegurar semántica y accesibilidad del menú móvil sin imponer framework.
- Mantener los componentes de presentación desacoplados del contenido aprobado.
- Ninguno de estos puntos implica modificación automática de D04.

---

## 11. B02.2 / C01 — Antecedente histórico v0.1 (SUPERADO por sección 12)

**Estado: PROPUESTA NO APROBADA.** C01 es el identificador del paquete de trabajo de componentes y **no debe confundirse** con el bloque editorial C01 de la página Capacidades del Documento 03.

### 11.1 Alcance y decisiones candidatas

| ID | Decisión propuesta | Motivo | Evidencia prevista | Criterio de aceptación |
|---|---|---|---|---|
| VIS-020 | Cabecera editorial ligera con marca, navegación y contacto | Claridad B2B | Wireframe escritorio y móvil C01 | Acceso directo a áreas clave y contacto |
| VIS-021 | Menú móvil accesible de apertura explícita | Operación predecible | Prototipo de estados | Apertura/cierre por teclado, foco gestionado |
| VIS-022 | Selector de idioma coherente con rutas disponibles | Robustez editorial | Matriz de idiomas/rutas | Sin enlaces rotos ni traducciones ficticias |
| VIS-023 | Pie corporativo estructurado y discreto | Cierre y orientación | Wireframe footer | Acceso a contacto, rutas y enlaces legales vigentes |
| VIS-024 | Contenedor, bandas y breadcrumbs contextuales | Orientación sin ruido | Wireframes interiores | Jerarquía visual estable y semántica correcta |

### 11.2 SiteHeader — contrato visual candidato

**Estructura:** marca a la izquierda; enlaces de primer nivel al centro/derecha; contacto distinguible sin competir con la marca; selector de idioma compacto. Cabecera de superficie clara, tipografía Inter y separador inferior sutil. Evitar barras dobles y exceso de iconos.

**Navegación:** reflejar exclusivamente páginas y etiquetas aprobadas por D03. La lista siguiente es un **mapa de agrupación provisional** a contrastar, no copy aprobado de menú: Inicio; Capacidades (con acceso a Infraestructuras, Sistemas energéticos y Automatización); Sectores; Proyectos y experiencia; Sobre BAFRAS; Contacto. El menú no debe introducir páginas nuevas.

**Comportamiento escritorio:** navegación visible cuando exista espacio real; estado activo por ruta con indicación no exclusivamente cromática; desplegable de Capacidades solo si simplifica el acceso y supera pruebas de teclado. No exigir menú sticky: comparar variante estática y sticky compacta en prototipo, con atención a altura útil y saltos de layout.

**Comportamiento móvil:** marca + botón «Menú» claramente identificado; panel de navegación que permite ver las rutas y subrutas sin hover; no se oculta información esencial. El contenido de página permanece en orden de lectura coherente. El selector de idioma se integra en el menú si la anchura lo exige.

**Estados obligatorios:** default, hover (si existe puntero), focus-visible, actual, expanded/collapsed, disabled solo si hay razón real. Control de foco y Escape según patrón escogido (disclosure o diálogo); no declarar comportamiento modal si no se implementa como tal.

**Dimensiones candidatas, NO tokens:** cabecera 72–84 px escritorio y 60–72 px móvil; área táctil objetivo 44×44 px; contenedor aproximado 1180 px dentro del rango D05 1120–1240 px; separación horizontal 24–32 px. Validar con el logo y los CSS reales. La referencia WCAG 2.2 AA para tamaño mínimo de objetivo es 24×24 CSS px con excepciones; 44×44 px es el objetivo de diseño preferido.

### 11.3 SiteFooter — contrato visual candidato

Pie con fondo pino, información corporativa verificable, enlaces a las páginas publicadas y acceso a contacto; zona legal subordinada visualmente. Sin indicadores comerciales inventados ni direcciones o datos no confirmados. En móvil, columnas apiladas y orden lógico de lectura. Deben comprobarse los enlaces legales reales antes de G1.

### 11.4 Layout primitives — contrato visual candidato

- **Container:** ancho máximo candidato 1180 px, márgenes laterales fluidos y anchura de lectura controlada; no fijar hasta auditoría CSS.
- **SectionBand:** superficies papel/blanco/piedra/pino usadas con propósito, no alternancia automática.
- **Breadcrumbs:** solo páginas interiores donde mejoren orientación; Inicio no los necesita. Etiquetas y rutas reales, `aria-current` para ubicación actual; no duplicar la navegación principal.
- **PageShell:** secuencia semántica header → main → footer; enlace «Saltar al contenido» visible al recibir foco; un H1 por página.
- **Responsive:** decidir cambio a menú compacto por ajuste real del contenido, no por breakpoint arbitrario; comprobar 320, 390, 768, 1024 y 1440 px y zoom al 200 %.

### 11.5 Wireframes textuales para la siguiente evidencia C01-EV-01

**Escritorio, cabecera:**

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ BAFRAS        Capacidades  Sectores  Proyectos  Sobre BAFRAS  Idioma   │
│                                                    Contacto             │
└─────────────────────────────────────────────────────────────────────────┘
                      [Saltar al contenido al recibir foco]
```

**Móvil, cabecera y menú abierto:**

```text
┌──────────────────────────────┐
│ BAFRAS               Menú ☰  │
├──────────────────────────────┤
│ Capacidades                  │
│   Infraestructuras           │
│   Sistemas energéticos       │
│   Automatización             │
│ Sectores                     │
│ Proyectos y experiencia      │
│ Sobre BAFRAS                 │
│ Contacto                     │
│ Idioma                       │
└──────────────────────────────┘
```

Son esquemas de arquitectura visual; las etiquetas finales dependen del Documento 03.

### 11.6 Matriz de QA y condiciones para aprobar C01

1. Todas las rutas enlazadas existen y mantienen su jerarquía editorial.
2. Navegación completa por teclado; foco visible y orden lógico; menú abre/cierra sin pérdida de foco.
3. Menú usable a 320 px, zoom 200 %, orientación vertical/horizontal y textos largos en idiomas disponibles.
4. Ninguna acción depende únicamente de hover, color o movimiento.
5. Estado actual y estado expandido comprensibles para lector de pantalla.
6. Menú y selector de idioma no ocultan el CTA de contacto ni introducen scroll horizontal.
7. Footer con enlaces correctos y sin atribuciones/datos corporativos inventados.
8. Contraste WCAG 2.2 AA verificado sobre colores definitivos.
9. Capturas de cabecera/pie en escritorio y móvil, estados abierto/cerrado y focus-visible, archivadas como evidencia.
10. Comparación con CSS, activos y contratos de D04 antes de fijar dimensiones.

**Pendientes explícitos para decisión de dirección:** cabecera estática frente a sticky compacta; desplegable Capacidades frente a enlaces planos; presentación del selector de idioma; densidad y número de columnas del footer. Ninguno se considera aprobado por esta propuesta.

**Gate:** G1 permanece NO APROBADO. No modificar código productivo.


---

## 12. B02.2 / C01 v0.3 — Especificación de diseño APROBADA (03/11/2026)

**Acto de aprobación:** el promotor confirma expresamente C01 v0.3. Esta sección **prevalece** sobre las propuestas C01 v0.1/v0.2 y las alternativas de la sección 11 cuando exista contradicción. La aprobación se refiere al **diseño y contrato de comportamiento**, no a código implementado, inspección completa del repositorio ni publicación. **G1 sigue NO APROBADO.**

### 12.1 Principio rector y límites

**Conservar la apariencia y los componentes actuales que funcionan; adaptar etiquetas, destinos y jerarquía al Documento 03; corregir únicamente fallos demostrados de accesibilidad, móvil e idiomas.** Evitar cambios cosméticos, rediseños, sustituciones masivas de CSS/DOM/JS, nuevas dependencias o abstracciones innecesarias. La versión actual de la web es referencia de regresión, no una maqueta a reconstruir.

La auditoría B02.0 y la conversación C01 v0.3 citan como referencias una cabecera sticky translúcida de ~77 px, desplegables claros con filete verde y sombra suave, subrayado verde de página activa, botón Contacto verde y tipografía Inter. **Estas observaciones deben corroborarse con capturas y código antes de imponer medidas exactas**; ~77 px no es un token nuevo. Se conservan logotipo original, paleta y geometría existentes salvo defecto verificable.

### 12.2 Registro de decisiones VIS-020 a VIS-024 — APROBADAS

| ID | Decisión aprobada | Justificación | Evidencia / validación pendiente |
|---|---|---|---|
| VIS-020 | **Conservar** cabecera clara/translúcida, sticky, logo original, navegación horizontal, estado activo y botón verde Contacto; actualizar solo estructura editorial y destinos | Coherencia visual y conversión B2B sin rediseño innecesario | Capturas baseline + inspección CSS/DOM; CA-01 a CA-03 |
| VIS-021 | **Conservar** estilo de desplegables y menú móvil; corregir acceso al índice y subpáginas, teclado, foco, expansión y overflow | Resolver defectos de navegación sin sustituir componentes | Pruebas 320/375/390 px, teclado y lector de pantalla; CA-04 a CA-06 |
| VIS-022 | **Conservar** presentación del selector de idioma; mostrar solo idiomas publicados y destinos equivalentes válidos | Evitar traducciones ficticias y enlaces rotos | Matriz página × idioma; CA-07 |
| VIS-023 | **Conservar** estética del footer; ajustar enlaces y contenido a D03, sin duplicación pesada ni datos corporativos inventados | Orientación y credibilidad | Capturas baseline, comprobación legal y de enlaces; CA-08 |
| VIS-024 | Mantener estructura global y breadcrumbs contextuales existentes cuando sean útiles; introducir únicamente correcciones semánticas y accesibles justificadas | Consistencia sin sobreingeniería | Inspección de plantillas, pruebas de foco y rutas |

**Quedan descartadas** las propuestas anteriores de eliminar el botón verde Contacto, pasar por defecto a cabecera estática, imponer nuevas medidas de cabecera o sustituir el lenguaje visual del footer. No se fija un nuevo número de columnas ni se fuerza una nueva composición de menú por preferencias estéticas.

### 12.3 Contrato editorial vinculante (Documento 03)

Navegación principal: **Inicio** (accesible mediante el logotipo), **Capacidades**, **Sectores**, **Proyectos y experiencia**, **Sobre BAFRAS**, **Contacto**, selector **ES/CA/EN/DE** solo para idiomas realmente publicados. **No incluir «Conocimiento».**

**Capacidades** ofrece un enlace independiente al índice y accesos directos a **Infraestructuras e instalaciones**, **Sistemas energéticos** y **Automatización y control**. No sustituir esos títulos por taxonomías de marketing. La navegación de Proyectos y experiencia lleva al índice; fichas individuales únicamente si se verifican, autorizan y publican. La arquitectura editorial base tiene nueve páginas, ampliable a doce con las tres fichas condicionadas; las páginas legales son auxiliares. Los slugs y rutas técnicas se validarán con D04, sin inventarlos desde D05.

### 12.4 Contrato de componentes y criterios de aceptación

**C01.1 — `SiteHeader` / marca y persistencia**

- **CA-01.1**: presente en todas las páginas publicadas; logo original enlaza a Inicio en el idioma activo.
- **CA-01.2**: se mantiene el comportamiento sticky y la composición existente sin salto de layout, oclusión de contenido o regresión visual injustificada.
- **CA-01.3**: capturas antes/después verifican logo, alturas observadas, alineaciones, colores y espaciados sin imponer nuevos tokens.

**C01.2 — navegación principal y estado activo**

- **CA-02.1**: etiquetas, jerarquía y destinos coinciden con D03; «Conocimiento» no figura.
- **CA-02.2**: cada enlace resuelve a página publicada; no existen enlaces rotos, duplicados o falsos destinos.
- **CA-02.3**: la sección activa se identifica sin depender exclusivamente del color; las páginas interiores señalan su sección matriz.
- **CA-02.4**: el desplegable conserva apariencia actual, no se recorta y puede operarse sin hover exclusivo.

**C01.3 — CTA Contacto**

- **CA-03.1**: conserva botón verde y ubicación funcional actual; enlaza directamente a Contacto.
- **CA-03.2**: es activable con teclado, tiene foco visible y sigue siendo localizable en móvil.

**C01.4 — desplegable Capacidades**

- **CA-04.1**: índice accesible de forma independiente de la expansión; tres especialidades con sus nombres aprobados.
- **CA-04.2**: apertura/cierre mediante teclado y puntero; Escape cierra y devuelve el foco al activador cuando corresponde al patrón implementado.
- **CA-04.3**: submenú cerrado no deja controles ocultos en la secuencia de tabulación; estados comunicados mediante semántica accesible.
- **CA-04.4**: no alterar colores, filete, sombra ni estructura salvo corrección justificada.

**C01.5 — menú móvil**

- **CA-05.1**: cero desbordamiento horizontal a 320, 375 y 390 px y con zoom 200 %; ningún contenido esencial inaccesible.
- **CA-05.2**: acceso a todas las rutas publicadas, con agrupación de Capacidades expandible si mejora la navegación; enlace al índice siempre independiente.
- **CA-05.3**: menú abre y cierra por teclado/toque, Escape cuando está abierto; foco y estados de expansión gestionados correctamente, sin trampas.
- **CA-05.4**: Contacto fácilmente accesible; sin proliferación de enlaces duplicados ni nuevo estilo visual injustificado.

**C01.6 — accesibilidad transversal**

- **CA-06.1**: enlace «Saltar al contenido» visible al recibir foco y operativo; regiones semánticas `header`, `nav`, `main` y `footer` adecuadas.
- **CA-06.2**: foco visible y orden lógico; elementos ocultos no enfocables; navegación completa sin ratón.
- **CA-06.3**: comprobación manual con teclado y lector de pantalla, y contraste/objetivos conforme a WCAG 2.2 AA en el alcance intervenido.
- **CA-06.4**: las 27 tabulaciones citadas en auditoría son una **señal de diagnóstico**, no un objetivo numérico arbitrario; eliminar pasos innecesarios sin perder destinos útiles.

**C01.7 — selector de idiomas**

- **CA-07.1**: idioma activo identificado y únicamente idiomas realmente publicados ofrecidos como destinos.
- **CA-07.2**: cambio a página equivalente cuando exista; alternativa explícita y comprensible cuando no exista, sin simular traducciones.
- **CA-07.3**: selector accesible por teclado; rutas y metadatos coherentes con D04; traducciones revisadas antes de publicación.

**C01.8 — `SiteFooter`**

- **CA-08.1**: conserva identidad, superficies, tipografía y composición actual salvo defecto demostrado.
- **CA-08.2**: enlaces reales a capacidades, secciones corporativas, contacto y legales publicados; idioma cuando proceda, sin replicar de manera pesada toda la cabecera.
- **CA-08.3**: sin datos legales provisionales ni referencias inventadas; cero overflow en móvil; navegación por teclado y foco visible.

### 12.5 Matriz mínima de pruebas y evidencia

| Contexto | Resoluciones / escenarios | Comprobación obligatoria |
|---|---|---|
| Móvil | 320, 375, 390 px; zoom 200 % | Menú cerrado/abierto, expansión, Contacto, idiomas, overflow |
| Tableta | 768, 1024 px | Transición de navegación y ausencia de solapes |
| Escritorio | 1440 px y ancho real de referencia | Sticky, dropdown, estado activo, CTA, footer |
| Teclado | Tab, Shift+Tab, Enter, Espacio, Escape según control | Salto al contenido, orden y recuperación de foco |
| Asistencia | Lector de pantalla representativo | Etiquetas, estado expandido, navegación y regiones |
| Editorial | Inicio, especialidad, Proyectos y experiencia, Contacto | Rutas, idioma, estado activo, footer y ausencia de fichas no aprobadas |

**Evidencias a registrar:** inventario de archivos/componentes y selectores existentes; capturas baseline y posteriores (cabecera/footer en escritorio y móvil, menú y foco); matriz de enlaces por idioma; resultados de pruebas manuales y automatizadas disponibles; diferencias visuales justificadas y defectos pendientes. Las observaciones históricas de 24 enlaces móviles y 9 px de desbordamiento a 320 px se deben **reproducir o rectificar** contra el baseline real antes de fijarlas como defectos actuales.

### 12.6 Condiciones de transferencia a desarrollo (no autorización)

**Fase 0 — inspección/baseline obligatoria:** identificar plantillas, CSS, JS, rutas y configuración de idiomas; registrar comportamiento y evidencias; proponer el cambio mínimo por causa raíz. **No tocar código productivo en esta fase.**

**Fases futuras, condicionadas a G1:** (1) alinear etiquetas y destinos a D03; (2) corregir defectos de accesibilidad, móvil e idiomas; (3) ejecutar QA y comparar antes/después; (4) solicitar aprobación de publicación. Reutilizar componentes y estilos existentes; no reescribir navegación ni introducir dependencias sin justificación. Los contratos de arquitectura, organización de código y gates pertenecen a D04; el plan operativo y el detalle de archivos afectados se documentarán en el plan de ejecución, no como decisiones visuales nuevas.

### 12.7 Cierre documental y siguiente paquete

**C01 v0.3: APROBADO A NIVEL DE DISEÑO** por el promotor. **Implementación: NO INICIADA / NO VERIFICADA.** **G1: NO APROBADO.** Los fundamentos VIS-010 a VIS-019 conservan sus estados anteriores. Siguiente paquete de diseño: **B02.2/C02 — Componentes editoriales y comerciales**; no reabrir C01 salvo evidencia de contradicción con D03/D04 o defectos reproducibles.


---

## 13. B02.2 / C02 v0.2 — Contrato de componentes editoriales y comerciales (CORRECCIONES VALIDADAS)

**Fecha:** 03/11/2026. **Revisión:** V2.3.1; correcciones de C02 validadas por dirección, sin aprobación de G1. **Autoridad:** D03 determina contenido, denominaciones, orden y destinos; este D05 determina presentación, composición, estados y criterios de aceptación; D04 determina arquitectura e implementación. **Precedencia:** los apartados aprobados de este documento (en especial §4, §10 y §12) prevalecen sobre ilustraciones o propuestas de trabajo posteriores no aprobadas. **No se modifica ningún archivo productivo.**

### 13.1 Objetivo y criterio de intervención

Cerrar las decisiones de diseño necesarias para representar el contenido editorial aprobado con una biblioteca mínima de componentes. **La auditoría B01 del 03/11/2026 describe una copia histórica del repositorio; es inventario de recursos y patrones, NO el diseño objetivo.** Se reutilizará una estructura histórica solo cuando sea compatible con D03 y con las decisiones aprobadas de D05. No se invierte esa precedencia. Se prohíbe sustituir una composición aprobada por otra simplemente porque esta última exista en el código.

El trabajo de C02 cubre `PageHero`, `SectionHeading`, `ContentCard` (capability/technical-area/sector), `NeedList`, `DeliverableList`, bloque editorial de metodología, `ExperienceCard` (featured/compact/study) y `ContactBand`. `MediaFigure` se usa como soporte y su lenguaje gráfico definitivo corresponde a C03; `FounderProfile`, `ContactForm` y las composiciones completas se especifican en C04/C05 según proceda. Los nombres son **contratos de presentación**, no obligación de crear clases, módulos ni CSS nuevos.

**Regla de cierre de variantes:** C02 define las familias y límites de diseño. Cuando C02 admite más de una disposición, C04 deberá seleccionar explícitamente la variante de cada bloque, documentar su geometría y comportamiento responsive, y dejar constancia de la decisión antes de G1. Ninguna alternativa queda a elección libre de Codex.

**Regla general de conservación:** mantener marca, colores, tipografía Inter, geometría sobria, contenedor y ritmos editoriales aprobados; modificar solo lo exigido por el contenido, la accesibilidad o una decisión de diseño aprobada. El inventario B01 identifica CSS de partida (`tokens.css`, `base.css`, `components.css`, `pages.css`), pero la implementación futura se evaluará contra el estado del repositorio disponible en G1, no contra una copia antigua.

### 13.2 Matriz de decisiones VIS-025 a VIS-031

| ID | Decisión especificada | Precedencia / restricción | Estado | Verificación de diseño |
|---|---|---|---|---|
| VIS-025 | Reutilizar gramática visual, patrones y tokens existentes **cuando sean compatibles** con D03/D05; sin rediseño global | VIS-001–003, VIS-009 | **Propuesta C02** | Comparativa de componente con referencia aprobada; cambios justificados |
| VIS-026 | Tres familias de hero: Inicio, especialidad e interior compacto; no variantes arbitrarias por página | §3–4; H01, INF/ENE/DIG, restantes | **Propuesta C02** | Jerarquía, CTA, longitud de texto, móvil |
| VIS-027 | `ContentCard` por función: H02 tres tarjetas de igual peso; ámbitos y sectores con variantes justificadas | **H02 de §4 y D03 prevalece sobre filas históricas del repositorio** | **Propuesta C02** | Tres tarjetas equivalentes y enlaces; seis sectores 2 columnas × 3 filas |
| VIS-028 | Diferenciar necesidad del cliente, entregable técnico y secuencia de trabajo; no mezclar sus mensajes | H03/H04 y especialidades D03 | **Propuesta C02** | Etiquetas, orden, número y función correctos |
| VIS-029 | Definir únicamente dirección visual y estados de experiencia para el futuro; en esta fase publicar solo el contenido editorial aprobado en D03, sin exigir expedientes ni referencias de fundadores | H06, PE, VIS-006/008, §6 | **Propuesta C02** | Cero referencias/cifras/imágenes no autorizadas en salida pública |
| VIS-030 | Conservar banda CTA corporativa, variando exclusivamente copy y acciones aprobadas | H07 y cierres D03; C01 CTA global ya aprobado | **Propuesta C02** | Enlaces reales, foco, contraste, responsive |
| VIS-031 | Comprobar reutilización y variantes en las nueve páginas, sin imponer un único layout | §4; D03; VIS-009 | **Propuesta C02** | Matriz de cobertura y excepciones documentadas |

**Nota de estado:** las correcciones de C02 v0.2 recogidas en esta revisión han sido validadas por dirección. VIS-025–031 no alteran ni reabren VIS-001–024. La aprobación integral de diseño C02 y G1 se registra separadamente; esta validación no acredita pruebas de navegador ni autoriza implementación.

### 13.3 C02.1 — `PageHero`

**Finalidad:** identificar la página, comunicar su propuesta y orientar la siguiente acción. **Invariantes:** H1 único por página publicada, eyebrow solo si lo contempla D03, subtítulo/introducción íntegros, CTA con destino real; espacio y contraste suficientes; no simular fotografías de trabajos propios. Mantener estilo tipográfico, botones y tratamiento editorial aprobados.

| Variante | Aplicación | Composición y contenido obligatorio | Restricciones |
|---|---|---|---|
| `home` | H01 | Hero **asimétrico**; eyebrow, H1, subtítulo, texto, CTA principal Contacto y secundario Capacidades; visual integrador de INF/ENE/DIG | Opción A editorial aprobada; no sustituir por un eslogan; **Se conserva la composición aprobada, no automáticamente la fotografía histórica**. VIS-004 exige sustituir el recurso sintético; selección definitiva y derechos en C03 |
| `specialty` | INF-01, ENE-01, DIG-W01 | H1 de especialidad, explicación de alcance y CTA que corresponda a D03; visual técnico complementario cuando esté aprobado | No copiar el hero de Inicio; no inventar métricas ni diagrama final (C03) |
| `interior` | Capacidades, Sectores, Proyectos, Sobre BAFRAS, Contacto | Cabecera editorial compacta, título e introducción D03; breadcrumbs cuando corresponda a C01 | No forzar fotografía o CTA en páginas cuyo bloque editorial no los requiere |

**Regla sobre el medio:** conservar la composición H01 aprobada no supone conservar la fotografía de la versión antigua. C03 decidirá el recurso final conforme a VIS-004; Codex no podrá elegirlo.

**Responsive:** en móvil el texto y CTA preceden al visual; no recortar H1, subtítulos ni botones. El recurso puede sustituirse por una versión simplificada o suprimirse si es puramente decorativo, nunca si contiene información imprescindible. **CA-C02-01:** las tres variantes se distinguen por función; H01 mantiene los dos CTA y el orden aprobado; los nueve H1 corresponden a D03; no hay desbordamiento a 320/375/390 px ni pérdida de texto al 200 % de zoom; el hero definitivo supera revisión de contraste y derechos.

### 13.4 C02.2 — `SectionHeading` y flujo editorial

**Finalidad:** estructurar la lectura sin añadir ruido visual. **Invariantes:** H2 para sección principal, H3 para subsección, introducción solo cuando existe en D03, líneas y espaciados de la gramática visual aprobada. La etiqueta superior (`eyebrow`) es opcional y nunca debe introducir copy nuevo. Ancho de lectura controlado; tipografía Inter y pesos sobrios. No convertir cada sección en una tarjeta, ni inventar divisores o iconos para llenar espacio.

**Variantes:** `standard` (título + texto opcional), `split` (título y explicación en columnas cuando la longitud lo permita), `compact` (subsección técnica). Estas son **variantes de composición**, no nombres obligatorios de CSS. **CA-C02-02:** jerarquía semántica y visual consistente en nueve páginas; ningún texto editorial omitido o truncado; lectura natural al apilar columnas; contraste y microtexto revisados contra fondos reales.

### 13.5 C02.3 — `ContentCard` (tres funciones, no una tarjeta universal)

| Variante | D03 | Diseño vinculante | Interacción / aceptación |
|---|---|---|---|
| `capability` | **H02**, índice C02 | **Tres tarjetas de igual peso visual** en H02, con nombre, descripción, ejemplos y enlace individual; enlace complementario al índice. La composición conceptual de H02 está aprobada en §4. En el índice de Capacidades se mantienen tres **paneles amplios con mini-esquemas homogéneos** según §4; C04 fijará sus proporciones, orden y distribución definitiva sin cambiar H02 | Toda la tarjeta solo será enlace si no contiene enlaces anidados; CTA distinguible; sin contenido esencial en hover; apilado móvil |
| `technical-area` | INF-03 (4 ámbitos + transversal), ENE-03 y DIG-W03 (6 ámbitos + transversal) | Bloques técnicos con título y descripción íntegra, estructura suficientemente flexible para diferente densidad; transversal diferenciado como función integradora, no un ámbito inventado | Numeración solo si ayuda; sin inventar cifras; diagrama técnico asociado se especifica en C03 |
| `sector` | H05 selección de 4 grupos; SEC-02 6 sectores | En Inicio, cuatro grupos **como selección editorial**, no taxonomía definitiva; en página Sectores, **2 columnas × 3 filas** en escritorio según D03; iconografía solo si es técnica y uniforme | Enlaces contextuales solo si D03 los contempla y tienen destino; una columna en móvil |

**Cierre de disposición:** las variantes y sus posibles distribuciones no constituyen opciones de implementación. C04 asignará una composición concreta a cada bloque de D03 y documentará excepciones justificadas.

**Prohibiciones:** reemplazar H02 por filas editoriales antiguas sin nueva aprobación; iconografía genérica ornamental; sombras y radios nuevos sin razón; hacer que todas las tarjetas tengan idéntica cantidad de texto a costa del copy; ocultar texto detrás de hover. **CA-C02-03:** H02 = 3 tarjetas equivalentes y 3 enlaces de especialidad + enlace índice; INF/ENE/DIG conservan cantidades y transversal D03; SEC-02 = 6 grupos con orden aprobado y retícula 2×3; funcionamiento y lectura correctos en móvil.

### 13.6 C02.4 — `NeedList` y `DeliverableList`

**`NeedList`:** describe la situación del cliente, su implicación técnica y el destino de profundización cuando D03 lo indica. En H03 son **exactamente cuatro situaciones**, en el orden de D03, con sus enlaces a INF, ENE, DIG y Capacidades. En especialidades se utiliza el bloque de necesidades propio INF-02 / ENE-02 / DIG-W02; no se copia H03. Composición editorial de filas/lista, con separadores y espaciado sobrios, sin necesidad de cuatro tarjetas nuevas.

**`DeliverableList`:** presenta modalidades o resultados técnicos que el servicio puede entregar según el alcance contratado. Se alimenta exclusivamente de C04, INF-04, ENE-04 y DIG-W04 según la página. Puede usar columnas o listas agrupadas, pero no convertir los entregables en promesas automáticas ni añadir documentos que D03 no incluya. **No fusionar necesidades y entregables en un mismo bloque.**

**CA-C02-04:** H03 cuatro situaciones completas y enlaces correctos; cada especialidad conserva su bloque de necesidades; listas de entregables fieles a D03, con jerarquía legible, sin chips de microtexto inaccesibles ni truncamientos en móvil.

### 13.7 C02.5 — Bloque de filosofía, integración y proceso

**H04:** mantener **cuatro pasos en orden**: Comprender → Evaluar → Desarrollar → Verificar, cada uno con explicación D03, texto introductorio, cierre sobre alcance variable y enlace a Sobre BAFRAS. Presentar como **secuencia editorial numerada**, no cuatro CTA ni un embudo comercial obligatorio. En móvil, secuencia vertical con orden DOM coincidente. La secuencia no significa que todas las fases se contraten siempre.

**Capacidades C03/C04 (IDs editoriales de D03, no paquetes de trabajo de diseño):** diferenciar **ingeniería que conecta disciplinas** de **cómo podemos colaborar**; el bloque editorial C04 se organiza según las cuatro modalidades aprobadas en D03. **Estas modalidades son formas de intervención, no cuatro fases sucesivas ni un proceso obligatorio.** H04, en cambio, expresa una filosofía conceptual en cuatro pasos. Los bloques de especialidad no deben copiar automáticamente ninguna de ambas estructuras. No heredar automáticamente los ocho pasos y cinco fases del HTML auditado. **CA-C02-05:** cuatro pasos H04 íntegros, cierre explícito y enlace; integración y modalidades no duplicadas ni confundidas; lectura correcta sin animación y sin JS.

### 13.8 C02.6 — `ExperienceCard` y dirección visual de experiencia (SIN BLOQUEO DE C02)

**Alcance de esta fase:** C02 define exclusivamente la **dirección visual** y las variantes de presentación de experiencia; **no se exige definir ahora proyectos individuales ni expedientes de experiencia de los fundadores**. El contenido que se traslade a la web en esta fase es **exactamente el aprobado en D03**. La ausencia de referencias individualizadas no bloquea el cierre de C02, C03, C04 ni el diseño corporativo. No se crean tarjetas ni ejemplos ficticios para llenar la composición.

**Familias visuales previstas para cuando existan contenidos publicables:** `featured` (referencia destacada), `compact` (complementaria) y `study` (entrada a ficha). Se mantiene una presentación sobria, con atribución visible, jerarquía editorial, figura documental opcional y CTA solo si existe destino real. La composición potencial de **3 destacadas + 3 complementarias** es una capacidad de diseño futura, **no una cuota de publicación actual** ni un requisito para cerrar C02.

**Cuatro estados contemplados en el contrato visual, sin exigir su materialización actual:**

1. **Referencia autorizada y ficha publicada:** tarjeta con contenido aprobado y enlace real.
2. **Referencia autorizada sin ficha pública:** tarjeta solo si D03 y la autorización de publicación la contemplan; sin enlace ficticio.
3. **Referencia o medios no definidos/autorizados:** no publicar tarjeta, nombre, logo, cifra, fotografía, placeholder ni espacio vacío. Mantener exclusivamente el bloque editorial aprobado en D03; si D03 prevé un cierre textual sin tarjetas, se respeta.
4. **Estudio propio BAFRAS:** atribución corporativa inequívoca cuando exista un estudio real y esté aprobado para publicación.

**Regla de alcance:** la comprobación de expedientes, fotografías, cifras y permisos será obligatoria **antes de publicar una referencia concreta**, no para aprobar ahora el lenguaje visual del componente. C03 especificará tratamiento de medios; C04 fijará la composición efectiva con el contenido disponible de D03. **CA-C02-06 (diseño):** variantes y estado sin referencias especificados; ninguna tarjeta ficticia ni hueco reservado; atribución visual inequívoca cuando proceda. **Verificación de publicación futura:** expedientes y permisos solo para referencias efectivamente incorporadas.

### 13.9 C02.7 — `ContactBand`

**Finalidad:** cierre claro y consistente sin competir con el hero ni multiplicar acciones. Conservar banda corporativa oscura, geometría, símbolo y variantes de botón ya aprobadas, sujeto a contraste y accesibilidad. **H07:** título, texto, CTA «Hablemos de tu proyecto» y microcopy de colaboración, íntegros según D03. En páginas interiores, usar el texto y CTA específico de su bloque editorial, sin normalizar copy a una frase universal. No introducir formularios dentro de la banda ni CTA adicionales no previstos.

**CA-C02-07:** destino Contacto correcto; contraste y foco visibles; banda y botón adaptados a 320 px y zoom 200 %; ningún texto se pierde; no se altera la cabecera ni el CTA global de C01.

### 13.10 Matriz de cobertura de nueve páginas

| Página | Hero | Componentes C02 y orden de uso | Condición especial |
|---|---|---|---|
| Inicio | `home` H01 | H02 `capability` (3 tarjetas) → H03 `NeedList` (4) → H04 proceso (4) → H05 `sector` (4 selección) → H06 bloque editorial D03; `ExperienceCard` solo cuando proceda → H07 `ContactBand` | Mantener H01–H07 sin insertar bloques editoriales nuevos; H06 puede ser solo texto |
| Capacidades | `interior` C01 | C02 3 paneles → C03 integración → C04 4 modalidades → C05 CTA | Mini-esquemas C03 se concretan en C03 de diseño; no repetir ciclo histórico de 8+5 |
| Infraestructuras | `specialty` INF-01 | INF-02 necesidades → INF-03 4 ámbitos + transversal → INF-04 entregables → INF-05 conexiones → INF-06 texto editorial D03 (tarjetas futuras condicionadas) → INF-07 CTA | Figura de edificio corresponde a C03 |
| Sistemas energéticos | `specialty` ENE-01 | ENE-02 necesidades → ENE-03 6 ámbitos + transversal → ENE-04 entregables → ENE-05 conexiones → ENE-06 texto editorial D03 (tarjetas futuras condicionadas) → ENE-07 CTA | Flujos físicos corresponden a C03 |
| Automatización y control | `specialty` DIG-W01 | DIG-W02 necesidades → DIG-W03 6 ámbitos + transversal → DIG-W04 entregables → DIG-W05 conexiones → DIG-W06 texto editorial D03 (tarjetas futuras condicionadas) → DIG-W07 CTA | Arquitectura OT/control corresponde a C03 |
| Sectores | `interior` SEC-01 | SEC-02 6 sectores (2 columnas × 3 filas) → SEC-03 problemas → SEC-04 colaboración → CTA según D03 | No confundir cuatro grupos de portada con seis de página |
| Proyectos y experiencia | `interior` PE | 3 featured + 3 compact **como patrón potencial, no exigido ahora** → contenido y explicación de evidencia exactamente según D03, más CTA aprobado | No bloquear diseño por falta de referencias individuales de fundadores; sin tarjetas ni huecos ficticios; estudios futuros conforme §6 |
| Sobre BAFRAS | `interior` SB | perfiles de fundadores (fuera del detalle C02) → filosofía/metodología → experiencia → CTA | Retratos y perfiles requieren tratamiento específico C04/C03 |
| Contacto | `interior` CO | formulario + correo y privacidad; `ContactBand` solo si D03 lo contempla, sin duplicar cierre | `ContactForm` y estados se especifican en C05; cuatro campos según D03 |

**Obligación de trazabilidad C04:** para **cada bloque y subbloque** de D03 se registrarán ID editorial, referencia inequívoca a la sección/copy rector, familia y variante C02, composición definitiva, orden, CTA/destino, recurso C03 (si aplica), responsive y condición de publicación. La matriz será de cobertura, **sin duplicar íntegramente D03**. Ninguna fila de esta tabla sustituye esa trazabilidad exhaustiva.

### 13.11 Criterios de aceptación transversales y evidencias

| ID | Verificación exigida | Evidencia prevista |
|---|---|---|
| CA-C02-08 | Ningún componente altera la jerarquía o el copy de D03 | Matriz de IDs y revisión editorial completa |
| CA-C02-09 | Se conservan paleta, Inter, botones, contenedor y geometría aprobados; cualquier excepción queda motivada | Comparación con baseline visual disponible y registro de diferencias |
| CA-C02-10 | Reflujo sin pérdida de contenido a 320/375/390/768/1024/1440 px y zoom 200 %; teclado/foco y contrastes WCAG 2.2 AA en el alcance | Capturas y checklist de accesibilidad, pruebas manuales/automatizadas posteriores |
| CA-C02-11 | La solución admite textos más largos sin recorte y no presupone idiomas sin traducción publicada | Pruebas con contenido de longitud representativa; matriz de disponibilidad |
| CA-C02-12 | No hay nuevas dependencias, componentes duplicados o reglas CSS globales innecesarias por exigencia de diseño | Inspección técnica durante ejecución posterior a G1; competencia de D04 |
| CA-C02-13 | No se publica ninguna referencia, cifra, logo, foto o ficha sin expediente autorizado | Inventario de recursos y expedientes; prueba de estado sin referencias |
| CA-C02-14 | Las nueve páginas quedan cubiertas por las variantes, con excepciones explícitas | Matriz §13.10 y maquetas de C04 |

**Dos niveles de aceptación, no intercambiables:** (A) **aceptación documental de diseño**: decisiones, variantes, estados y trazabilidad aprobados en D05/C04, sin exigir navegador ni publicación de referencias de fundadores; (B) **verificación productiva posterior a G1**: implementación fiel, pruebas de renderizado, accesibilidad, enlaces, contraste, responsive y recursos efectivamente publicados. No se marcará (B) como superado por aprobar (A). CA-C02-13 se aplica a **referencias que efectivamente se decida publicar**, no bloquea el diseño sin ellas.

**Pruebas todavía NO realizadas:** renderizado real, capturas comparativas, contraste sobre fotografías, derechos de imagen, lector de pantalla, funcionalidad de formularios y revisión de traducciones. No marcar estas condiciones como superadas solo porque estén especificadas.

### 13.12 Transferencia controlada a C03/C04/C05 y cierre del paquete

- **C03 — recursos y diagramas:** seleccionar y especificar medios definitivos; hero visual final conforme a VIS-004 sin reutilización automática de la foto histórica, `MediaFigure`, diagramas de INF/ENE/DIG, leyendas, alternativas móviles y derechos. C02 no aprueba una fotografía o diagrama concreto.
- **C04 — composición de páginas:** wireframes/maquetas y disposición exacta de los bloques D03 en nueve páginas; **seleccionar sin ambigüedad cada variante**, cerrar posiciones, anchos relativos, responsive y excepciones, y entregar **matriz de cobertura por bloque y subbloque con referencias inequívocas a D03**, sin duplicar su texto ni reabrir Inicio.
- **C05 — estados y QA:** formulario, interacción, validación transversal, estados de error/carga, accesibilidad y comprobación de publicación; **separar aprobación documental de pruebas productivas** y verificar permisos solo de recursos efectivamente publicados.
- **G1:** pendiente; requiere entregables y aprobación expresa conforme §8 y D04. C02 documentado no equivale a permiso para refactorizar.

**Decisión de dirección (03/11/2026):** validadas las correcciones sobre cierre de variantes en C04, distinción de proceso/modalidades, cuatro estados sin huecos ficticios, separación de aceptación documental y productiva, conservación de composición del hero pero no de la fotografía histórica, y trazabilidad por referencias inequívocas. **No se bloquea C02 por no definir todavía proyectos de experiencia de los fundadores.**

**Dictamen multidisciplinar C02:** dirección/estrategia B2B valida la secuencia problema → capacidad → confianza → contacto; ingeniería verifica que no se inventan capacidades, resultados ni atribuciones; editorial garantiza fidelidad a D03; UX mantiene composiciones aprobadas y variantes por función; frontend/accesibilidad exige estados y verificabilidad sin imponer nuevas tecnologías. **Estado final de este apartado: CORRECCIONES C02 v0.2 VALIDADAS POR DIRECCIÓN; CIERRE FORMAL INTEGRAL C02 Y G1 SEPARADOS.**

## 14. B02.2 / C03 v0.1 — Antecedente de propuesta (SUPERADO EN CRITERIO POR §15; NO APROBADO)

**Estado:** diseño iniciado, no aprobado. Esta sección no modifica C01/C02 ni autoriza implementación. Fuentes rectoras: D03 (copy y taxonomía), D05 §§4–8, VIS-004/006/008/009/014/016/017 y §13.12. La auditoría B01 es exclusivamente inventario de la versión antigua, no objetivo visual. C04 fijará ubicación, dimensiones y composición final por bloque; C05 verificará accesibilidad y publicación.

### 14.1 Objetivo, equipo y decisiones no reabribles

**Objetivo:** definir el contenido semántico, estilo, estados y entregables de cada medio, de forma que Codex no seleccione imágenes, invente diagramas ni deduzca conexiones por iniciativa propia. Perspectivas de revisión: dirección creativa/branding (coherencia), INF/ENE/DIG (corrección física y funcional), comercial/editorial (claridad B2B y fidelidad D03), UX/accesibilidad (lectura y responsive), frontend (SVG/HTML/recursos estáticos sin dependencia adicional).

**Invariantes:** (a) composición H01 y sus dos CTA ya aprobados; (b) H02 tres tarjetas equivalentes; (c) identidad BAFRAS y lenguaje editorial + documental + sistemas; (d) diferencia entre esquema conceptual, evidencia documental y resultado cuantitativo; (e) ningún recurso no autorizado ni proyecto ficticio; (f) ningún dibujo sustituye el copy aprobado; (g) no se requiere disponer de proyectos de experiencia de fundadores para cerrar el diseño.

### 14.2 Taxonomía de recursos y su función

| Tipo | Función | Identificación visible / alternativa | Restricción |
|---|---|---|---|
| Conceptual integrador | Explicar relación INF–ENE–DIG | Pie «Esquema conceptual» cuando pueda confundirse con proyecto; alternativa textual | No implica una instalación existente ni conexión universal |
| Diagrama técnico de especialidad | Explicar ámbitos, subsistemas y relaciones | Título y leyenda de líneas/flechas; alternativa textual estructurada | Sin datos, unidades o flechas físicamente falsas |
| Mini-esquema | Orientar cada capacidad en tarjetas/paneles | Nombre de capacidad en texto adyacente; decorativo si redundante | Misma gramática, no mismo dibujo repetido |
| Fotografía documental | Mostrar persona, instalación o contexto real | Pie y atribución cuando proceda; licencia/permiso | No equivale automáticamente a proyecto BAFRAS |
| Evidencia técnica | Plano, captura, tabla, foto o informe real | Fuente, fecha/versión y alcance cuando proceda | No mostrar capturas con información sensible |
| Resultado de estudio | Presentar magnitudes y hallazgos verificables | Unidades, periodo, fuente, supuestos y limitaciones | No generar resultados de ejemplo como si fueran reales |

### 14.3 C03.1 — Visual del hero H01 e integración corporativa

**Decisión de dirección propuesta C03-VIS-01:** conservar exactamente la composición asimétrica y la jerarquía aprobadas para H01, pero sustituir el recurso sintético antiguo conforme VIS-004. Elegir como dirección preferente una **composición técnica integradora propia**, no una fotografía genérica. La alternativa documental de fotografía real se conserva como opción de diseño solo si se identifica recurso, derechos y adecuación narrativa y dirección la aprueba expresamente. No se autoriza a Codex a escoger entre ambas.

**Contenido del visual integrador:** tres dominios identificados como «Infraestructuras e instalaciones», «Sistemas energéticos» y «Automatización y control», con un elemento de proyecto/sistema común y relaciones de colaboración interdisciplinar. **No** representar flujo físico directo INF→ENE→DIG, ni atribuir el esquema a un proyecto. El concepto debe leerse sin texto diminuto y sin introducir una cuarta capacidad. No duplicar dentro de la imagen el H1, subtítulo o CTA de D03.

**Escritorio:** el visual ocupa la región prevista por la composición H01 aprobada, con jerarquía subordinada al texto. **Móvil:** texto y CTA antes del visual; versión simplificada de tres dominios, no reducción proporcional del diagrama de escritorio. C04 cerrará medidas, posición exacta, recorte y fondos. Si el visual es puramente redundante con el texto, puede marcarse decorativo; si añade relaciones relevantes, alternativa textual.

**Evidencia pendiente:** boceto técnico vectorial desktop y móvil, revisión semántica INF/ENE/DIG, contraste y elección explícita de recurso final. **No se declara aprobado el recurso en v0.1.**

### 14.4 C03.2 — Gramática gráfica común

- **Color:** exclusivamente tokens BAFRAS; no codificar especialidades por colores arbitrarios. Diferenciar clases de conexión con trazo, flecha y etiqueta además de color.
- **Forma:** geometría sobria, líneas finas, esquinas discretas, contenedores y retícula alineados a D05. Sin sombras 3D, isometría decorativa, iconos de stock o fondos que parezcan fotografías de instalaciones reales.
- **Tipografía:** Inter; etiquetas suficientemente legibles, sin microtexto como portador único de información. Títulos y explicaciones editoriales quedan en HTML, no incrustados en imágenes rasterizadas.
- **Semántica:** cada nodo representa un activo, subsistema o función identificable; las flechas indican una relación declarada, nunca decoración. Una línea no direccional representa asociación, no flujo de energía ni señal.
- **Leyenda:** definir expresamente tipo de línea, dirección y significado. Si una relación depende del caso de proyecto, rotular «según configuración» o no dibujarla.
- **Salida:** SVG accesible como formato maestro de diagramas; versión móvil simplificada cuando el contenido lo requiera; fallback textual HTML. PNG/WebP solo como derivados para contextos compatibles, sin imponer formato único a estudios.
- **No incluir** cifras, marcas comerciales, topologías de instalaciones concretas, clientes, logotipos de terceros ni resultados sin fuente y permiso.

### 14.5 C03.3 — Diagrama INF: instalaciones integradas

**Finalidad:** representar un edificio/infraestructura como soporte de **cuatro ámbitos D03 INF-03**: electricidad e infraestructura eléctrica; climatización, ventilación y refrigeración; agua, hidráulica y servicios auxiliares; protección y condiciones técnicas de las instalaciones. La función transversal «Diagnóstico, coordinación y gestión técnica de activos» se presenta como capa transversal **fuera del dibujo de los cuatro ámbitos**, no como quinto subsistema físico.

**Composición candidata:** silueta/volumen esquemático de edificio, cuatro áreas técnicas identificadas mediante etiquetas y conexiones funcionales solo cuando sean genéricas y correctas. Evitar superponer redes reales, esquemas unifilares, tuberías y dispositivos de protección en una ilustración que pudiera confundirse con proyecto constructivo. La capa transversal se representa como marco de coordinación o banda editorial, sin flechas de flujo material.

**Versión móvil:** cuatro módulos secuenciales con un encabezado común de edificio/instalación; transversal en bloque separado. **Aceptación técnica:** ningún ámbito omitido; climatización y ventilación no confundidas con programación BMS; la figura no aparenta un plano de ejecución.

### 14.6 C03.4 — Diagrama ENE: sistema energético y relaciones

**Finalidad:** mostrar relaciones conceptuales entre demanda, suministro/red, generación, almacenamiento y gestión, sin sugerir que todos los proyectos contienen todos los activos. La representación debe reflejar los **seis ámbitos de D03 ENE-03**: diagnóstico y eficiencia; generación renovable y almacenamiento; electrificación y sistemas térmicos; movilidad e integración; gestión/monitorización/costes; descarbonización. La eficiencia hídrica se mantiene como nota transversal/complementaria conforme D03, no como séptimo ámbito inventado.

**Composición candidata:** zona central de demanda/instalación; activos opcionales de red, renovables, almacenamiento, sistemas térmicos y movilidad; funciones de análisis/gestión en capa separada. **Flujos físicos** (electricidad/calor) y **flujos informativos** (medida/gestión) no se mezclan en una misma flecha. No indicar carga/descarga, exportación o autoconsumo como flujos universales sin una configuración explícita. Descarbonización es objetivo/ámbito de evaluación, no una máquina física.

**Versión móvil:** dos niveles: activos físicos y capa de análisis/gestión, con lista textual de seis ámbitos; relaciones explicadas por leyenda. **Aceptación técnica:** flechas verificadas individualmente, sin balances ni magnitudes ficticias; todos los ámbitos editoriales encuentran correspondencia, sin convertir el diagrama en una taxonomía duplicada ilegible.

### 14.7 C03.5 — Diagrama DIG: arquitectura funcional de control

**Finalidad:** explicar instrumentación, control, supervisión, integración OT y software técnico según **seis ámbitos DIG-W03**: instrumentación/telemetría; PLC/DDC; HMI/SCADA/BMS; comunicaciones OT; software/datos; control e integración de activos energéticos. Diagnóstico, pruebas y evolución se muestran como función transversal, no como sexta etapa de un proceso lineal.

**Composición candidata:** capas funcionales «campo/medida», «control local PLC/DDC», «supervisión HMI/SCADA/BMS», «software/análisis», conectadas por una capa de «comunicaciones e interfaces OT»; rama de integración energética cuando corresponda. Distinguir explícitamente **señal medida**, **orden/consigna** y **actuación física**, mediante trazos y leyenda. El control local no depende necesariamente de una conexión a SCADA o a la nube; no dibujar una arquitectura obligatoriamente cloud.

**Versión móvil:** capas verticales con conexiones reducidas y leyenda accesible. **Aceptación técnica:** SCADA no sustituye PLC/DDC, telemetría no implica actuación, OT no se presenta como servicio de certificación de ciberseguridad, y los modelos/simulaciones no se anuncian como IA por defecto.

### 14.8 C03.6 — Mini-esquemas y recursos por página

| Página/bloque D03 | Recurso C03 previsto | Carácter | Cierre posterior |
|---|---|---|---|
| H01 | Integrador INF/ENE/DIG | Conceptual, candidato prioritario | Selección final y alta fidelidad C03/C04 |
| H02 | Tres mini-esquemas homogéneos | Conceptual y subordinado a tarjetas | C04: tamaño, alineación y versión móvil |
| Capacidades C02/C03 | Mini-esquemas de cada especialidad y relación de integración | Conceptual | C04: ubicación y densidad |
| INF-03 | Diagrama de instalaciones | Conceptual | C04: ubicación y relación con cuatro ámbitos |
| ENE-03 | Diagrama de activos/funciones energéticas | Conceptual | C04: ubicación y relación con seis ámbitos |
| DIG-W03 | Arquitectura funcional de control | Conceptual | C04: ubicación y relación con seis ámbitos |
| SEC-02 | Iconografía técnica solo si mejora lectura | Opcional, no obligatoria | C04: decisión expresa por seis sectores |
| PE / INF-06 / ENE-06 / DIG-W06 | Medios de experiencia | Condicionados al contenido de D03 | Sin bloquear diseño; no inventar referencias |
| SB | Retratos reales de fundadores | Documental, condicionado a permisos | C04: tratamiento y recorte |
| Contacto | Ninguna imagen decorativa obligatoria | No requerida | C04: composición limpia |

### 14.9 C03.7 — Fotografías, figuras y resultados

**Fotografías:** documentar recurso, titular/procedencia, derecho de uso, relación real con BAFRAS o experiencia anterior, personas identificables, pie y alt. Los archivos presentes en la auditoría B01 son candidatos, no recursos aprobados. No publicar imágenes de stock/sintéticas como evidencia de proyectos. Los retratos de fundadores se tratarán de forma consistente; el diseño no depende de que estén aprobados hoy.

**MediaFigure:** variantes `conceptual`, `documentary`, `technical-diagram`, `study-result`; propiedades de diseño: título opcional, imagen/SVG, pie, fuente, alt/alternativa, estado de autorización y versión móvil cuando proceda. No implica nueva clase software. Una figura puramente decorativa no requiere texto alternativo redundante.

**Estudios:** gráficos con título, unidad, periodo, fuente y supuestos; tablas con encabezados y unidades; PDF solo si autorizado. Ningún valor de muestra se presentará como resultado real. No imponer una librería de visualización a los motores Python.

### 14.10 Registro propuesto y criterios de aceptación de diseño

| ID | Decisión propuesta | Estado |
|---|---|---|
| VIS-032 | Priorizar composición integradora propia para H01, sin escoger recurso final automáticamente | PROPUESTA |
| VIS-033 | Gramática técnica común: nodos, líneas, flechas, leyenda y alternativas | PROPUESTA |
| VIS-034 | INF: cuatro ámbitos físicos + transversal diferenciada | PROPUESTA |
| VIS-035 | ENE: separar activos, flujos físicos y funciones de análisis/gestión | PROPUESTA |
| VIS-036 | DIG: separar medida, control, supervisión, comunicaciones y software | PROPUESTA |
| VIS-037 | Recursos documentales y resultados con procedencia, atribución y contexto | PROPUESTA |
| VIS-038 | Móvil mediante simplificación semántica, no reducción ilegible | PROPUESTA |

**CA-C03-D01:** cada recurso tiene función, clasificación conceptual/documental/resultado y correspondencia con ID de D03. **D02:** todos los diagramas muestran solo relaciones revisadas por ingeniería. **D03:** diagramas de escritorio y móvil especificados con leyenda y alternativa textual. **D04:** sin paleta, tipografía o iconografía nueva no aprobada. **D05:** ningún recurso condicionado se da por autorizado por estar en disco. **D06:** C04 puede colocar cada figura sin decidir su semántica; la selección final de H01 y los dibujos de alta fidelidad quedan pendientes de revisión explícita.

### 14.11 Entregables de evidencia y transferencia

**C03-EV-01:** boceto de composición integradora H01 desktop/móvil y elección expresa del recurso. **C03-EV-02:** lámina de gramática común (nodos, conexiones, etiquetas, leyendas). **C03-EV-03/04/05:** diagramas INF, ENE, DIG revisados por especialistas, con versiones móviles y alternativas textuales. **C03-EV-06:** catálogo de medios con procedencia, permiso y estado; no bloquea diseño corporativo si hay recursos futuros. **C03-EV-07:** revisión conjunta de coherencia y aceptación documental. Las maquetas y cotas finales pertenecen a C04; pruebas productivas a C05 y posterior G1.

**Límites:** C03 v0.1 es un contrato semántico y dirección gráfica para revisión, no un diseño visual de alta fidelidad terminado. No se han generado aún los SVG definitivos ni validado permisos, contraste sobre imágenes o comportamiento en navegador. No se autoriza implementación.


---

## 15. B02.2 / C03 v0.2 — Selección e integración editorial de medios (PROPUESTA PARA REVISIÓN)

### 15.1 Cambio de enfoque y precedencia

Este apartado sustituye **como propuesta de dirección** el enfoque prescriptivo de §14, sin borrar su trazabilidad histórica. C03 decide **qué medio** aporta valor a cada bloque del Documento 03, cuál de los activos existentes es candidato, qué función cumple y qué condiciones exige. No se impone la producción de diagramas INF/ENE/DIG ni de mini-esquemas. C04 decidirá su composición dimensional final respetando C01, C02, VIS-009 y H01–H07. El contenido literal procede de D03, no de C03. La auditoría B01 describe recursos de una versión antigua y no determina el resultado final.

**Jerarquía de medios:** (1) composición editorial sin imagen cuando sea suficiente; (2) fotografía/documento real pertinente y autorizado; (3) reutilización de ilustración conceptual existente cuando explique algo; (4) esquema sintético nuevo solo con justificación explícita de valor informativo. No hay cuota de imágenes por página. No hay obligación de gráficos, diagramas de flujo ni iconos.

### 15.2 Inventario disponible: candidatos, no selección definitiva

La auditoría B01 documenta 33 imágenes en `assets/images/`: logo/símbolo y variantes, fotografía `home/hero/bafras_transicion_energetica.jpg`, ilustración conceptual de visión de sistemas (PNG/WebP), tres retratos con variantes y seis fotografías MEP (Formentor, centro educativo y residencia de Ibiza). **No se dispone en este expediente de la inspección visual de los archivos originales ni de un registro suficiente de derechos**. Por ello no se declara ningún recorte, selección definitiva ni permiso de publicación. Los logotipos y símbolos deben respetar los maestros de identidad ya aprobados. El inventario es evidencia de disponibilidad histórica, no de publicación.

### 15.3 Matriz de medios por página y bloque editorial

| Página / IDs D03 | Decisión de medios propuesta | Integración editorial | Condición |
|---|---|---|---|
| Inicio H01 | Un recurso integrador, a seleccionar entre fotografía técnica real pertinente y composición conceptual propia; conservar composición H01 aprobada | Imagen subordinada a H1, subtítulo y dos CTA | No reutilizar automáticamente hero antiguo; aprobar recurso y recorte explícitamente |
| Inicio H02 | Tres tarjetas de igual peso; sin obligación de iconos o mini-esquemas | Títulos, ejemplos y enlaces íntegros según D03 | No introducir tres gráficos como requisito |
| Inicio H03–H05 | Preferencia por tipografía, listas y numeración; sin imagen obligatoria | Cuatro necesidades, cuatro pasos de filosofía y selección de sectores | No duplicar contenido en dibujos |
| Inicio H06–H07 | Texto editorial y CTA; imágenes solo si referencia autorizada | H06 puede quedar textual según D03; H07 sin imagen | No bloquear por portfolio pendiente |
| Capacidades C02 | Un recurso contextual por especialidad **solo si existe tríada coherente y pertinente**; alternativa sin imagen | Acompañar descripciones INF/ENE/DIG, no sustituirlas | La simetría no justifica imágenes genéricas |
| Capacidades C03 | Ilustración de visión de sistemas existente como candidata; alternativa composición textual | Explicar relación de disciplinas sin afirmar integración obligatoria | Inspeccionar ilustración, pertinencia y derechos |
| Capacidades C04–C05 | Sin imagen necesaria | Modalidades y contacto resueltos con C02 | Sin diagramas de proceso obligatorios |
| INF-01–INF-03 | Fotografía documental de instalaciones/edificio pertinente como candidata; ámbitos editoriales sin diagrama obligatorio | Fotografía junto a hero o introducción; cuatro ámbitos + transversal conservan sus textos | Fotografías MEP no se atribuyen automáticamente a BAFRAS |
| INF-04–INF-07 | Listas de entregables, integración y contacto principalmente tipográficos | Si existe evidencia técnica autorizada, se integra en bloque de experiencia | No inventar planos ni referencias |
| ENE-01–ENE-03 | Fotografía energética pertinente, si existe; sin diagrama universal obligatorio | Seis ámbitos y nota de eficiencia hídrica se resuelven editorialmente | Esquema solo si aclara una relación concreta |
| ENE-04–ENE-07 | Sin imagen obligatoria; evidencia autorizada en experiencia cuando proceda | Entregables, relación entre capacidades y CTA | Sin balances o resultados sintéticos ficticios |
| DIG-W01–DIG-W03 | Fotografía de instrumentación, cuadro, control o supervisión **real**, si existe | Acompaña la introducción; seis ámbitos editoriales completos | No inventar interfaces SCADA ni pantallas de clientes |
| DIG-W04–DIG-W07 | Preferencia por composición editorial; captura técnica real solo si aporta evidencia | Entregables, integración, experiencia y CTA | Revisar información sensible y derechos |
| SEC-01–SEC-05 | Seis bloques textuales sin seis fotografías ni seis iconos obligatorios | Priorizar lectura, diferencias sectoriales y CTA | Fotografía contextual solo si mejora una sección concreta |
| PE-01–PE-04 | Fotografías de proyectos solo con referencia, función y autorización verificadas | El texto D03 se publica según sus propias condiciones; no crear huecos visuales | Experiencia de fundadores pendiente NO bloquea C03 |
| SB-01–SB-05 | Retratos reales de los tres fundadores, si publicables | Encadre, proporción y jerarquía homogéneos junto a perfiles | Verificar identidad, derechos y calidad de cada variante |
| CO-01–CO-04 | Sin imagen | Hero, formulario, contacto directo y cierre claros | Priorizar usabilidad y ausencia de ruido |

### 15.4 Criterios de integración y selección

1. **Función antes que cantidad.** Cada recurso se justifica con una frase: qué añade al texto de D03. Si no añade información, contexto o confianza, se omite.
2. **Relación visual-textual.** Fotografía contextual junto al bloque que explica; evidencia documental junto a la referencia acreditada; ilustración conceptual junto a explicación de integración. No desplazar CTA ni recortar copy para hacer sitio.
3. **Fotografía real y permiso.** No convertir fotografías de proyectos previos de los fundadores en proyectos de BAFRAS. Registrar titular, autor, procedencia, autorización, uso y pie si corresponde.
4. **Unidad estética.** Inter, paleta, retícula, geometría y ritmo ya definidos; sin overlays ornamentales, galerías excesivas, iconos stock ni efectos gratuitos. Fotografías con tratamiento consistente y sin filtros que distorsionen evidencia.
5. **Responsive.** Definir encuadre móvil y desktop por fotografía seleccionada; preservar sujetos, equipos y lectura; no obligar a usar el mismo crop. Medios decorativos con alt vacío; medios informativos con alternativa útil.
6. **Recursos sintéticos.** Permitidos como **conceptuales** cuando explican una relación real y no sugieren un proyecto ejecutado. No producir un diagrama por especialidad por defecto; no usar gráficos con números ficticios.
7. **Estados sin medio.** Diseño válido sin fotografía, con el texto íntegro y sin huecos vacíos, placeholders publicados ni módulos ficticios.

### 15.5 Decisiones abiertas acotadas y evidencia necesaria

- **MED-01:** inspeccionar visualmente archivos originales del directorio `assets/images/` y registrar miniatura, nombre/ruta exacta, dimensiones, orientación, calidad y derechos. Auditoría textual insuficiente para aprobar la imagen.
- **MED-02:** elegir **un** recurso H01 y validar su recorte desktop/móvil frente a la composición aprobada.
- **MED-03:** evaluar si la ilustración conceptual existente funciona en Capacidades C03; conservarla, ajustarla o descartarla con motivo explícito.
- **MED-04:** seleccionar fotografías para INF, ENE y DIG únicamente si existen recursos pertinentes y publicables; si no, usar variante editorial sin imagen.
- **MED-05:** definir recorte y uniformidad de retratos de fundadores.
- **MED-06:** definir relación entre las seis fotografías MEP y las referencias D03 sin inventar atribuciones; no bloquear diseño si quedan pendientes.
- **MED-07:** identificar un único posible esquema nuevo de integración, **solo si** la revisión visual demuestra que el recurso existente y el texto no bastan; de otro modo no producir ninguno.

### 15.6 Entrega C03 → C04 y estado

**Entregables para cerrar C03:** catálogo de medios seleccionados con rutas exactas y derechos/estado, mapa D03→medio o «sin medio», prueba de integración H01 desktop/móvil, muestra de bloque de especialidad con y sin fotografía, tratamiento de retratos y reglas de recorte/pies/alt. C04 cierra disposición, medidas y responsive por bloque. C05 valida navegador y accesibilidad. **No se autoriza a Codex a escoger fotografías o producir diagramas por su cuenta.**

**Estado:** propuesta v0.2 pendiente de validación del promotor y de inspección visual de assets originales. C01/C02 permanecen aprobados. G1 sigue pendiente.


## 16. B02.2 / C03 v0.3 — Selección concreta basada en B02-PREP-01 (PROPUESTA PARA APROBACIÓN)

### 16.1 Fuente, alcance y precedencia

Este apartado desarrolla y precisa §15. Es **la propuesta operativa vigente de C03**; §14 es antecedente no aprobado. Fuente factual: `B02_PREP_01_INVENTARIO_RECURSOS_VISUALES.md` (03/11/2026), inventario de la biblioteca `assets/images/BAFRAS_Website_Visual_Assets_V1/` (LIB). La inspección del informe acredita 55 archivos de imagen: 26 fotografías con original y WebP, más 3 gráficos DEMO WebP. **No se ha accedido en esta revisión a los propios archivos binarios de LIB ni a sus hojas de contacto**; la selección es razonada a partir de las descripciones y observaciones del informe, no aprobación de recortes. Los ID `Rxx` pertenecen al inventario, no a D03; `lib:H01` tampoco significa el bloque editorial H01. D03 conserva autoridad sobre contenido y orden; C01/C02 sobre composición; C04 cierra las maquetas.

Rutas de las imágenes WebP: las rutas de la tabla son relativas a la raíz del repositorio (biblioteca reorganizada en WEB-00 FINAL; fuentes y manifiestos en `media-library/`; antes se prefijaba `assets/images/BAFRAS_Website_Visual_Assets_V1/`). No son todavía rutas públicas ni recursos enlazados. No mover/copiar archivos ni editar HTML en esta fase.

**Selección visual ≠ autorización de publicación.** Las licencias CC BY/CC BY-SA, CC0, dominio público y «Propio» son declaraciones del paquete; deben contrastarse por recurso, incluida atribución, modificaciones, personas y marcas. Ninguna fotografía de tercero prueba un proyecto BAFRAS.

### 16.2 Catálogo corto de imágenes candidatas y ubicación

| ID | Ruta WebP relativa a LIB | Papel de diseño / sección D03 | Integración y límites | Prioridad |
|---|---|---|---|---|
| R24 | `assets/images/home/hero/home-hero-engineering.webp` | Inicio H01, candidato A | Fotografía de sala de bombas; hero asimétrico aprobado, texto **fuera** de la imagen; dominante roja y recorte móvil por validar; no tratar como obra propia | Alta, comparar |
| R23 | `assets/images/home/capabilities/home-cap-infrastructure.webp` | Inicio H02 tarjeta INF; Capacidades C02 INF; INF-01 candidato alternativo; H01 candidato B | Sala técnica de varias instalaciones; imagen separada del texto; comprobar que la repetición entre páginas no sea excesiva | Alta |
| R22 | `assets/images/home/capabilities/home-cap-energy.webp` | Inicio H02 tarjeta ENE; Capacidades C02 ENE como alternativa | FV sobre cubierta; mantener mismo ratio visual que R23/R21; no atribuir potencia ni titular | Alta |
| R21 | `assets/images/home/capabilities/home-cap-digital.webp` | Inicio H02 tarjeta DIG; Capacidades C02 DIG como alternativa | Primer plano de módulos; mismo ratio, altura y tratamiento que R23/R22; no atribuir programación | Alta |
| R18 | `assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp` | INF-03, apoyo a climatización y ventilación | Se observa principalmente UTA, no «conductos» en abstracto; foto secundaria opcional, no una por disciplina | Media-alta |
| R10 | `assets/images/capabilities/energy/generation/energy-pv-rooftop.webp` | ENE-01 entrada; ENE-03 generación | Foto contextual con texto lateral, sin superposición; evitar que toda ENE parezca exclusivamente FV | Alta |
| R08 | `assets/images/capabilities/energy/electrification/energy-heat-pumps.webp` | ENE-03 sistemas térmicos; alternativa ENE-01 | Sala de tuberías/bombas; no afirmar que la imagen prueba bomba de calor específica | Media |
| R01 | `assets/images/capabilities/digital/automation/digital-plc-control-panel.webp` | DIG-W01 entrada; DIG-W03 control | Armario abierto; texto lateral; no atribuir fabricante, PLC ni intervención BAFRAS sin respaldo | Alta |
| R03 | `assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp` | DIG-W03 instrumentación; INF-05 relación opcional | Conservar instrumento y conexiones; no inferir magnitud medida | Media |
| R15 | `assets/images/capabilities/infrastructure/electrical/infra-electrical-distribution.webp` | INF-03 electricidad, alternativa a R18 como segunda foto | Pasillo de cuadros; no añadir cifras de potencia/tensión | Reserva |
| R20 | `assets/images/capabilities/infrastructure/plumbing-fire/infra-plumbing-piping.webp` | INF-03 hidráulica, si C04 evidencia necesidad | Imagen de tuberías, válvulas y conexiones; no forzar cobertura visual de todos los ámbitos | Reserva |
| R12 | `assets/images/capabilities/energy/storage/energy-battery-storage.webp` | ENE-03 almacenamiento, condicionado | Contenedores/equipos exteriores; identidad BESS declarada pero no demostrable visualmente; acompañar con texto genérico correcto | Reserva |
| R26 | `assets/images/sectors/industry/sector-industry.webp` | H05 industria o SEC-02 industria, solo si se aprueba variante fotográfica | Contexto industrial genérico; no alegar cliente o experiencia | Reserva |
| R25 | `assets/images/sectors/hospitality/sector-hospitality.webp` | H05 hoteles o SEC-02 turismo, solo si se aprueba variante fotográfica | Hotel identificable: riesgo alto de falsa relación comercial | Reserva no preferente |
| R27 | `assets/images/sectors/infrastructure/sector-infrastructure.webp` | H05 equipamientos/servicios públicos, solo si procede | Instalación documentada como depuradora; no equivale a todas las infraestructuras | Reserva |
| R28 | `assets/images/sectors/sports/sector-sports.webp` | SEC-02 equipamientos, solo si procede | Piscina: no crear un séptimo sector ni usarla para representar educación/salud | Reserva |
| R29 | `assets/images/sectors/tertiary/sector-tertiary.webp` | H05/SEC-02 terciario, solo si procede | Edificio identificable; no aparentar proyecto BAFRAS | Reserva no preferente |

**No seleccionados para la web corporativa V1 como evidencia:** R02/R06/R11 (gráficos con datos sintéticos); R04/R05/R13/R14/R17 (personas o situaciones ajenas y mayor riesgo de atribución); R16 (plano ajeno que puede parecer entregable propio); R07 (recarga con marcas/matrículas, solo reconsiderar por necesidad editorial); R09/R19 (uso técnico específico no confirmado visualmente). No se descartan de la biblioteca: se excluyen de la selección inicial, salvo revisión justificada y autorizada.

### 16.3 Matriz editorial de las nueve páginas — decisión por bloque

**Regla común de integración:** imagen y texto en regiones separadas; no superponer copy sobre equipos densos; preservar texto íntegro D03 y CTA; no introducir galerías, carruseles o tarjetas adicionales para consumir inventario. La tabla define recurso candidato y alternativa; C04 fija su posición y tamaño exactos en wireframe/maqueta.

| Página / bloque D03 | Decisión visual C03 | Recurso y disposición propuesta | Alternativa/condición |
|---|---|---|---|
| Inicio H01 | **Una imagen principal**, comparar dos candidatas | A: R24, B: R23. Hero asimétrico, texto y CTA en columna independiente; foto como bloque contiguo, no fondo de texto | Si ambos fallan encuadre/contraste, composición conceptual sin fingir evidencia; C04 debe decidir entre A/B/alternativa |
| Inicio H02 | **Tres imágenes equilibradas**, una por capacidad | R23 INF, R22 ENE, R21 DIG. Parte superior de las tres tarjetas de igual peso, relación 4:3 uniforme | Si no se validan derechos de alguna, resolver las tres tarjetas sin foto para preservar simetría |
| Inicio H03 | **Sin imagen** | Cuatro necesidades editoriales de D03 | No añadir ilustraciones de cada problema |
| Inicio H04 | **Sin imagen** | Cuatro pasos y cierre, tipografía y numeración | No diagrama de flujo obligatorio |
| Inicio H05 | **Preferencia sin imágenes** | Cuatro grupos de portada en composición tipográfica | R25/R26/R29/R27 solo si C04 demuestra valor y coherencia; no convertir en cinco/seis tarjetas fotográficas |
| Inicio H06 | **Sin fotografía de experiencia no acreditada** | Bloque textual D03, enlace | No usar R24 ni otras imágenes genéricas como portfolio |
| Inicio H07 | **Sin imagen** | Banda CTA C02 | — |
| Capacidades C01 | **Sin imagen** | Hero compacto editorial | — |
| Capacidades C02 | **Sin foto por defecto o tríada uniforme** | Opción A: composición editorial; B: R23/R22/R21, junto a cada especialidad, mismas proporciones | Evitar repetir exactamente la tríada H02 sin valor añadido; C04 escogerá A/B |
| Capacidades C03 | **Sin diagrama obligatorio** | Tres ejemplos de relación entre disciplinas en texto D03 | Evaluar ilustración histórica del sitio (no incluida en LIB) solo tras inspección; no equiparar con `lib:H02` ausente |
| Capacidades C04–C05 | **Sin imagen** | Modalidades y CTA | — |
| INF-01 | **Una foto de entrada** | R23 como candidata principal; alternativa R17 descartable por persona ajena, preferir R15 si interesa enfoque eléctrico | Evitar repetición hero H01/H02; si R23 ya domina Inicio, valorar R15 o variante sin foto |
| INF-02 | **Sin imagen** | Necesidades | — |
| INF-03 | **Una foto secundaria opcional** | R18 UTA; R15 electricidad o R20 hidráulica como reservas; ámbitos y transversal siguen completos | No una foto por ámbito; no hay foto específica de acústica |
| INF-04–INF-07 | **Sin imagen nueva** | Entregables, conexiones, experiencia textual y CTA | No utilizar R16 como plano propio ni R13 como prueba propia |
| ENE-01 | **Una foto de entrada** | R10 FV, junto al hero/introducción | Acompañar copy completo para no reducir la especialidad a FV |
| ENE-02 | **Sin imagen** | Necesidades | — |
| ENE-03 | **Una foto secundaria opcional** | R08 sistemas térmicos; R12 reserva de almacenamiento con cautela | No gráficos DEMO ni obligación de foto para cada ámbito |
| ENE-04–ENE-07 | **Sin imagen nueva** | Entregables, conexiones, experiencia y CTA | No E08 inexistente ni balances inventados |
| DIG-W01 | **Una foto de entrada** | R01 cuadro de control, junto al texto | No atribuir sistemas a BAFRAS |
| DIG-W02 | **Sin imagen** | Necesidades | — |
| DIG-W03 | **Una foto secundaria opcional** | R03 instrumentación | R04/R05 no preferidos por personas/pantallas ajenas |
| DIG-W04–DIG-W07 | **Sin imagen nueva** | Entregables, integración, experiencia y CTA | No D07 inexistente ni pantallas ficticias |
| Sectores SEC-01–05 | **Sin fotos de sectores por defecto** | Seis sectores según D03; iconografía uniforme solo si aporta claridad y se valida en C04 | Las cinco imágenes S01–S05 no determinan taxonomía; no crear «deportes» separado |
| Proyectos PE-01–04 | **Sin foto de proyectos ajenos** | Publicar solo contenido D03 habilitado; sin tarjetas o huecos ficticios de referencias | No bloquea C03 por expedientes pendientes; imágenes reales se incorporarán cuando estén autorizadas |
| Sobre BAFRAS SB-01–05 | **Retratos propios condicionados, no LIB** | Tres retratos históricos del sitio existente: comprobar archivos, permiso, consistencia y encuadre; si no, perfiles tipográficos homogéneos | Ninguna foto R04/R05/R13/R17 representa a los fundadores |
| Contacto CO-01–04 | **Sin imagen** | Hero compacto, formulario, email y privacidad | No decoración para llenar espacio |

### 16.4 Reglas de composición y tratamiento que C04 debe materializar

1. **Formato:** R21/R22/R23 y la mayoría de fotografías técnicas son WebP 1600×1200 (4:3); se respetará relación común en tarjetas H02. R24 es 1920×1080 (16:9), no forzar a 4:3 sin validar recorte. Los originales son respaldo para recortes nuevos, no ficheros de producción por defecto.
2. **Separación texto/foto:** nunca colocar H1, CTA o párrafos sobre una foto densa salvo maqueta específica con contraste demostrado. En H01 la foto ocupa región propia de la composición asimétrica; en H02 la imagen antecede a los textos dentro de cada tarjeta; en especialidades, foto contextual al lado de la introducción o del ámbito relacionado.
3. **Unidad visual:** marco/ratio homogéneo por conjunto, esquinas y bordes según tokens BAFRAS, sin filtros verdes, sombras decorativas, collages, logotipos superpuestos ni nuevos acentos cromáticos.
4. **Móvil:** el texto esencial precede a la imagen; recorte por recurso validado para 320/375/390 px y ampliación; si pierde sujeto/equipo o distrae, se permite mostrar encuadre íntegro o suprimir la foto contextual sin dejar hueco. H02 conserva las tres tarjetas.
5. **Semántica:** `alt` contextual, no repetir el título adyacente; imagen puramente ornamental con `alt=""`; pie/atribución y licencia según comprobación real. No usar `alt_es` del manifiesto automáticamente. El crédito puede resolverse en sección de créditos accesible cuando la licencia lo permita.
6. **No repetición innecesaria:** R23 aparece como candidato en H01, H02 e INF; **no aprobar simultáneamente las tres apariciones sin revisión visual global**. Preferir H02 como ubicación base; comparar H01 con R24 y para INF R15/R18 si resulta redundante.
7. **Licencias:** validar individualmente fuente externa, titularidad, versión de licencia, atribución, modificaciones/recortes y terceros reconocibles. Para BY-SA revisar específicamente obligaciones aplicables al material adaptado; no asumir que READY del proveedor equivale a aprobado por BAFRAS.
8. **Gráficos y esquemas:** 0 nuevos por defecto en V1. R02/R06/R11 quedan fuera de la publicación corporativa inicial porque sus cifras son DEMO. Solo se autoriza un nuevo esquema si dirección valida pregunta concreta que resuelve, datos/relaciones, texto alternativo y emplazamiento en D03; no se fabrica como sustituto de evidencia.

### 16.5 Registro de decisiones y pendientes de evidencia

| Código | Decisión o prueba requerida | Responsable de cierre | Estado |
|---|---|---|---|
| MED-08 | Elegir H01 R24 vs R23 vs recurso conceptual tras ver desktop y móvil; validar densidad/rojo | Dirección creativa + promotor, en C04 | ABIERTO |
| MED-09 | Validar tríada H02 R23/R22/R21 como conjunto, incluyendo permisos y recortes | UX + derechos + promotor | CANDIDATA |
| MED-10 | Decidir Capacidades C02 con/sin imágenes, evitando duplicación de H02 | UX + promotor, en C04 | ABIERTO |
| MED-11 | Resolver INF-01 R23/R15 y ENE-01 R10 y DIG-W01 R01 en maquetas | UX + especialistas | CANDIDATAS |
| MED-12 | Verificar retratos del sitio anterior y condiciones de uso; LIB no los incluye | Dirección + equipo | ABIERTO NO BLOQUEANTE PARA C03 |
| MED-13 | Verificar licencias y créditos de cada imagen **seleccionada**; no es necesario aprobar las 29 | Responsable publicación/derechos | PENDIENTE PARA PUBLICACIÓN |
| MED-14 | Inspeccionar los WebP concretos y hojas de contacto reales y revisar recortes desktop/móvil | Diseño/UX | PENDIENTE PARA CIERRE VISUAL |
| MED-15 | Confirmar no usar imágenes de terceros como experiencia profesional acreditada; respetar D03 | Editorial + dirección | REGLA FIJADA |
| MED-16 | Verificar si ilustración conceptual histórica existe, se entiende y añade valor a Capacidades C03 | Diseño/UX | OPCIONAL |

**Condición de transferencia:** C04 recibirá esta matriz y seleccionará explícitamente variantes A/B donde estén abiertas; ningún desarrollador puede elegir automáticamente imágenes del manifiesto. G1 sigue pendiente hasta wireframes, maquetas y aprobación expresa. Esta sección es una **propuesta de selección** y no certifica disponibilidad material de LIB en el entorno de diseño ni derechos de publicación.


## 17. B02.2 / C03 v0.4 — Revisión visual directa de 29 WebP y pruebas de composición (PROPUESTA PARA VALIDACIÓN)

### 17.1 Evidencia inspeccionada y alcance

Se abrió `BAFRAS_Website_Visual_Assets_V1_sin_originales.zip` y se visualizaron los 29 WebP preparados, todos accesibles. No se incluyeron los 26 originales de mayor resolución ni recursos históricos externos al paquete (retratos y símbolos del sitio anterior). Las observaciones siguientes sustituyen las decisiones basadas únicamente en el inventario de §16 donde sean más precisas; no reabren C01/C02 ni el contenido D03. El documento conserva §§14–16 por trazabilidad.

Se generaron dos láminas de **bocetos de integración** con las imágenes reales, para escritorio y móvil. Los textos visibles son abreviaciones de muestra, **no el copy aprobado de D03**, y la cabecera es un marco esquemático, **no la reproducción final de C01**. Son pruebas de ratio, equilibrio y jerarquía, no wireframes completos ni validación de WCAG. C04 insertará el texto íntegro y cerrará todas las medidas, tokens y estados.

- `C03_contacto_29.jpg`: las 29 imágenes con nombres.
- `C03_comparativas_escritorio.jpg`: hero R24/R23, H02 R23/R22/R21 y entradas INF R18, ENE R10, DIG R01.
- `C03_comparativas_movil.jpg`: los mismos recursos con encuadre móvil.

### 17.2 Matriz individual — selección y emplazamiento

Las rutas son relativas a la raíz del repositorio (antes de WEB-00 FINAL, a `assets/images/BAFRAS_Website_Visual_Assets_V1/`); son rutas de biblioteca, **no URLs de producción**. Los IDs R proceden de la auditoría B02-PREP-01. El formato de todas las imágenes es WebP; salvo R24 (16:9) y R25–R29 (8:5), las preparadas son 4:3.

| ID | Archivo WebP relativo a LIB | Bloque D03 | Decisión tras ver imagen | Integración, ratio y tratamiento | Alternativa |
|---|---|---|---|---|---|
| R01 | `assets/images/capabilities/digital/automation/digital-plc-control-panel.webp` | DIG-W01 | **SELECCIONADA** | 4:3; entrada editorial lateral; mantener cuadro completo | R21 |
| R02 | `assets/images/capabilities/digital/data/digital-data-analysis.webp` | — | **EXCLUIDA** | Gráfico DEMO; textos y sellos pequeños | — |
| R03 | `assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp` | DIG-W03 | **RESERVA** | 4:3; detalle de instrumentación en bloque relacionado | R21 |
| R04 | `assets/images/capabilities/digital/scada/digital-building-management.webp` | — | **EXCLUIDA** | Persona y pantalla de tercero; no equipo BAFRAS | — |
| R05 | `assets/images/capabilities/digital/scada/digital-scada-screen.webp` | — | **EXCLUIDA** | Persona e interfaz ajenas | — |
| R06 | `assets/images/capabilities/energy/analysis/energy-demand-analysis.webp` | — | **EXCLUIDA** | Datos sintéticos; no evidencia de estudio | — |
| R07 | `assets/images/capabilities/energy/electrification/energy-ev-charging.webp` | ENE-03 | **RESERVA** | Solo si la movilidad exige apoyo; evitar matrículas y marcas | — |
| R08 | `assets/images/capabilities/energy/electrification/energy-heat-pumps.webp` | ENE-03 | **SELECCIONADA SECUNDARIA** | 4:3; sala térmica, no afirmar equipo específico | R20 |
| R09 | `assets/images/capabilities/energy/generation/energy-electrical-infrastructure.webp` | INF-03 | **RESERVA** | Transformador visible; imagen eléctrica puntual | R15 |
| R10 | `assets/images/capabilities/energy/generation/energy-pv-rooftop.webp` | ENE-01 | **SELECCIONADA** | 4:3; fotografía a la derecha del texto; FV no resume toda la especialidad | R08 |
| R11 | `assets/images/capabilities/energy/management/energy-management-dashboard.webp` | — | **EXCLUIDA** | Dashboard DEMO con valores ficticios | — |
| R12 | `assets/images/capabilities/energy/storage/energy-battery-storage.webp` | ENE-03 | **RESERVA** | Equipos exteriores; BESS no verificable solo por fotografía | — |
| R13 | `assets/images/capabilities/infrastructure/construction/infra-commissioning-testing.webp` | — | **EXCLUIDA** | Técnico ajeno; no acreditar commissioning propio | — |
| R14 | `assets/images/capabilities/infrastructure/construction/infra-construction-site.webp` | — | **EXCLUIDA** | Contraluz, poca legibilidad y persona ajena | — |
| R15 | `assets/images/capabilities/infrastructure/electrical/infra-electrical-distribution.webp` | INF-03 | **RESERVA** | Pasillo de cuadros; imagen eléctrica secundaria | R09 |
| R16 | `assets/images/capabilities/infrastructure/engineering/infra-technical-plans.webp` | — | **EXCLUIDA** | Plano ajeno, no entregable BAFRAS; detalle ilegible en móvil | — |
| R17 | `assets/images/capabilities/infrastructure/mechanical/infra-hvac-plant.webp` | — | **EXCLUIDA** | Instalación compleja con persona ajena; imagen poco neutra | — |
| R18 | `assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp` | INF-01 | **SELECCIONADA** | 4:3; entrada contextual; se ve UTA, no únicamente conductos | R23 |
| R19 | `assets/images/capabilities/infrastructure/plumbing-fire/infra-fire-protection.webp` | INF-03 | **RESERVA** | Red de equipos; uso contra incendios no evidente | R20 |
| R20 | `assets/images/capabilities/infrastructure/plumbing-fire/infra-plumbing-piping.webp` | INF-03 | **RESERVA** | Hidráulica y tuberías; opcional, no llenar todos los ámbitos | R18 |
| R21 | `assets/images/home/capabilities/home-cap-digital.webp` | H02 DIG | **SELECCIONADA** | 4:3; tarjeta idéntica en ratio y altura a R22/R23 | R01 |
| R22 | `assets/images/home/capabilities/home-cap-energy.webp` | H02 ENE | **SELECCIONADA** | 4:3; tarjeta equivalente, sin texto superpuesto | R10 |
| R23 | `assets/images/home/capabilities/home-cap-infrastructure.webp` | H02 INF | **SELECCIONADA** | 4:3; tarjeta equivalente; evitar duplicar en hero/INF | R18 |
| R24 | `assets/images/home/hero/home-hero-engineering.webp` | H01 | **PREFERIDA PENDIENTE APROBACIÓN** | 16:9 fuente; recorte desktop ~1.57:1 y móvil ~1.2:1 probados; dominante roja | R23 |
| R25 | `assets/images/sectors/hospitality/sector-hospitality.webp` | H05/SEC-02 | **RESERVA NO PREFERENTE** | Hotel identificable, no cliente; sector se resuelve con tipografía | — |
| R26 | `assets/images/sectors/industry/sector-industry.webp` | H05/SEC-02 | **RESERVA** | Industria; solo si se aprueba variante con fotografía | — |
| R27 | `assets/images/sectors/infrastructure/sector-infrastructure.webp` | H05/SEC-02 | **RESERVA** | Instalación de servicios públicos, no experiencia propia | — |
| R28 | `assets/images/sectors/sports/sector-sports.webp` | SEC-02 | **RESERVA NO PREFERENTE** | Piscina no representa todos los equipamientos | — |
| R29 | `assets/images/sectors/tertiary/sector-tertiary.webp` | SEC-02 | **RESERVA NO PREFERENTE** | Edificio reconocible; no referencia propia | — |

### 17.3 Selección por página y control de densidad

| Página / bloque | Composición propuesta tras revisión visual | Decisión |
|---|---|---|
| Inicio H01 | Hero asimétrico C01/C02; R24 en región propia a la derecha en desktop y después del texto en móvil; no texto superpuesto | **R24 APROBADA por dirección (03/11/2026); R23 alternativa de contingencia únicamente con nueva decisión** |
| Inicio H02 | Tres tarjetas iguales con R23 INF, R22 ENE, R21 DIG, imagen arriba 4:3, texto debajo | **Selección recomendada** |
| Inicio H03–H07 | Tipografía y componentes C02; sin fotografía; H06 solo contenido permitido D03 | Sin nuevo recurso |
| Capacidades C01–C05 | Hero y tres capacidades editoriales sin repetir las fotos de H02; ejemplos de integración en texto; sin diagrama obligatorio | Sin fotografía nueva por defecto |
| Infraestructuras INF-01 | R18 como imagen de entrada lateral, evitando duplicar R23; no convertir la UTA en representación exhaustiva de INF | **R18 seleccionada** |
| Infraestructuras INF-03 | R15/R20 solo si C04 justifica necesidad y no satura; resto tipográfico | Reservas, no obligatorias |
| Sistemas energéticos ENE-01 | R10 como imagen lateral, preservando FV y contexto de cubierta | **R10 seleccionada** |
| Sistemas energéticos ENE-03 | R08 como imagen térmica secundaria separada de la lista de seis ámbitos | **R08 secundaria candidata**; puede omitirse en C04 por densidad |
| Automatización DIG-W01 | R01 como fotografía contextual de armario y cableado | **R01 seleccionada** |
| Automatización DIG-W03 | R03 como imagen de instrumentación secundaria solo si mejora lectura | Reserva opcional |
| Sectores SEC-01–05 | Seis grupos 2×3 en desktop, sin seis fotos heterogéneas; iconografía uniforme solo si se valida | Sin fotografías por defecto |
| Proyectos PE-01–04 | Sin fotos de stock como referencias propias; usar únicamente contenido D03 y medios propios acreditados | No bloquea C03 |
| Sobre BAFRAS SB-01–05 | Retratos auténticos del sitio anterior no presentes en este ZIP; perfiles tipográficos si faltan | Pendiente de inspección específica, no bloqueo de C03 |
| Contacto CO-01–04 | Sin imagen; formulario y vías de contacto | Cerrado como criterio |

### 17.4 Evaluación de composición y responsive

- **Hero R24:** composición de fuerte identidad industrial, excelente perspectiva, pero rojo intenso y gran densidad. La fotografía funciona mejor como bloque separado; evitar filtros corporativos para disimularla. En la prueba móvil 6:5 se mantiene parte de las bombas, aunque se pierde contexto periférico. **Aprobada por dirección para H01 el 03/11/2026; recorte final se valida en C04**.
- **Hero R23:** más sobrio y cromáticamente compatible, pero la escena parece una sala de instalaciones mecánicas y se repetiría en H02; reduce la diversidad visual. Reserva si dirección rechaza R24.
- **H02 R23/R22/R21:** coherencia de encuadre 4:3 y diferenciación de especialidades. Las tres tienen distinta densidad/temperatura de color, aceptable en fotografías documentales sin filtros uniformadores. En móvil apilar una tarjeta por fila y conservar imagen 4:3 sin recorte agresivo.
- **INF R18:** encuadre panorámico dentro de 4:3 con UTA verde. Aporta claridad temática, pero no representa todos los subsistemas INF; el copy D03 conserva la amplitud.
- **ENE R10:** cubierta FV legible en escritorio y móvil; su uso requiere evitar que toda la página se perciba como exclusivamente solar. R08 compensa con temática térmica.
- **DIG R01:** armario y borneros legibles en desktop; en móvil el detalle fino pierde relevancia, pero se mantiene la lectura de automatización. No etiquetar fabricante o protocolo.
- **Prueba de recorte:** se han producido versiones de boceto en ~1280 px escritorio y ~440 px móvil; **no** se han verificado todas las anchuras 320/375/390/768/1024/1440, zoom 200 %, contraste WCAG ni dispositivos reales. C04/C05 lo harán.
- **Texto:** no sobreponer titulares/CTA sobre fotografías técnicas; respetar composición asimétrica H01 y posición móvil texto antes de imagen. Las dimensiones de boceto no son tokens aprobados.

### 17.5 Derechos, atribuciones y publicación

El promotor indica que las imágenes son libres para utilizar. Se acepta como **autorización de selección editorial y uso en prototipos**, no como sustituto de los términos concretos del paquete. Según la auditoría, existen recursos CC BY, CC BY-SA, CC0, dominio público y tres gráficos declarados propios; **libre uso no equivale a ausencia de atribución**. Antes de publicación se cotejarán licencia, crédito, URL, modificaciones/recorte y derechos adicionales por recurso efectivamente utilizado, con base en los manifiestos `attribution.md` y `media-manifest.yaml`. No se bloqueará el trabajo de diseño por ello; tampoco se afirmará que se ha realizado una verificación jurídica externa. Las fotos de terceros nunca se presentarán como obras o personal BAFRAS.

### 17.6 Cierre de decisiones y transferencia a C04

- **MED-08 — CERRADA 03/11/2026:** dirección aprueba R24 para H01. R23 queda solo como alternativa histórica de comparación, no opción abierta para implementación.
- **MED-09:** validar tríada R23/R22/R21, con igual proporción y jerarquía; selección recomendada.
- **MED-10:** Capacidades sin repetir tríada H02; solo reconsiderar con justificación editorial en C04.
- **MED-11:** INF-01 R18; ENE-01 R10; DIG-W01 R01; secundarias ENE-03 R08, INF-03 R15/R20 y DIG-W03 R03 solo según necesidad.
- **MED-12:** retratos de fundadores e ilustración histórica fuera de ZIP; inspección pendiente, no requisito para cerrar selección de esta biblioteca.
- **MED-13:** crédito y licencias por imagen seleccionada antes de publicación.
- **MED-14:** inspección visual directa de los 29 WebP y primeras pruebas escritorio/móvil **realizada**; validación responsive exhaustiva y high fidelity siguen pendientes.
- **MED-15:** prohibición de utilizar fotos ajenas como prueba de experiencia propia, vigente.
- **MED-16:** no crear diagramas ni gráficos sintéticos nuevos por defecto; revisar solo si C04 detecta una necesidad concreta no cubierta por texto/foto.

**Estado actualizado 03/11/2026:** selección R24/H01 aprobada expresamente. Otras recomendaciones C03 conservan su estado propio. C04 autorizado para diseño documental; G1 no concedido ni web productiva modificada.


## 18. Acta de decisión C03 / MED-08 — Aprobación del hero H01 (03/11/2026)

**Decisión expresa del promotor:** «Valido R24 como imagen del hero H01. Actualiza el Documento 05 y continuemos con C04.» Esta decisión prevalece sobre cualquier mención previa a R24 como candidata o pendiente en §§15–17.

| Campo vinculante | Decisión |
|---|---|
| Página y bloque D03 | Inicio · **H01**, edición D03 02/11/2026 |
| Imagen aprobada | **R24 / lib:H01** — `home-hero-engineering.webp` |
| Ruta de biblioteca | `assets/images/home/hero/home-hero-engineering.webp` (relativa a `bafras/`) |
| Archivo preparado | WebP, **1920 × 1080 (16:9)**, sin transparencia; fotografía de sala industrial con bombas y tuberías rojas |
| Composición | **Hero asimétrico ya aprobado**: texto y CTA en zona independiente; fotografía en región visual lateral de escritorio; en móvil, texto antes de imagen |
| Tratamiento | Sin texto superpuesto, sin recoloración corporativa, sin afirmar que la instalación pertenece a BAFRAS; recorte con bombas y perspectiva reconocibles |
| Responsive | C04 fijará `object-position`, proporción de contenedor y encuadres 320/375/390/768/1024/1440 y zoom 200 %; la prueba preliminar móvil 6:5 no equivale a aceptación final |
| Alternativa | R23 fue comparada y **no seleccionada** para H01; su uso exigiría nueva aprobación de dirección |
| Texto y enlaces | **Exactamente D03 H01**: H1, subtítulo, cuerpo, CTA Contacto y Capacidades; no copiar texto de bocetos |
| Licencia declarada | **CC BY 2.0**, autor declarado Steve Jurvetson; uso comercial y crédito conforme a condiciones concretas de fuente; verificar atribución antes de publicar |
| Estado | **Selección editorial aprobada**; aprobación de imagen ≠ G1 ni autorización de publicación sin atribución y controles correspondientes |

**Cierre C03:** no se exige crear diagramas, gráficos o fotografías adicionales. R23/R22/R21 en H02 y R18/R10/R01 en especialidades se mantienen como selección profesional propuesta en §17; C04 podrá concretar su integración, sin presentarlas como aprobaciones expresas independientes.

## 19. B02.2 / C04 v0.1 — Arranque de composición detallada de nueve páginas (DISEÑO DOCUMENTAL EN CURSO)

### 19.1 Alcance, autoridad y método de trabajo

C04 convierte D03 (orden y textos), D05 §§10–13 (dirección y componentes C01/C02), §17 (selección de medios) y §18 (R24 aprobado) en **composiciones reproducibles**, sin editar HTML/CSS/JS ni iniciar G1. Los wireframes no cambian el contenido, ni inventan casos, cifras, diagramas o referencias. C04 debe producir **nueve wireframes completos de escritorio y móvil**, **tres maquetas completas de alta fidelidad** (Inicio, Infraestructuras, Contacto) y los módulos singulares de las otras seis páginas, según D05 §8. Este §19 es el **contrato inicial de composición**, no una afirmación de que ya se han producido esos entregables.

Equipo de revisión: dirección creativa y marca (ritmo y jerarquía), UX y accesibilidad (lectura, navegación, teclado y responsive), ingeniería INF/ENE/DIG (rigor semántico), dirección comercial (recorridos y CTA), arquitectura frontend (factibilidad sin imponer implementación).

**Reglas:** (a) D03 gobierna el copy y el orden; (b) las decisiones aprobadas C01/C02 no se reabren; (c) las variantes se cierran **en C04 antes de G1** y no quedan a elección de Codex; (d) fotografía documental siempre separada de la tipografía salvo decisión visual expresa; (e) densidad gráfica moderada, sin recurso por obligación; (f) referencias de fundadores o proyectos pendientes no bloquean composición, pero no generan tarjetas vacías.

### 19.2 Matriz inicial de cobertura D03 → composición → medio

| Página | Bloques D03 obligatorios en orden | Composición inicial que debe resolver C04 | Medio/estado C03 |
|---|---|---|---|
| **Inicio** | H01, H02, H03, H04, H05, H06, H07 | Hero asimétrico; 3 tarjetas iguales; 4 necesidades; 4 pasos conceptuales; 4 grupos sectoriales; experiencia editorial condicional; banda final de contacto | **H01 R24 aprobada**; H02 R23/R22/R21 propuestas; resto sin foto obligatoria |
| **Capacidades** | C01–C05 | Hero textual; 3 paneles equivalentes de especialidad; integración de disciplinas con ejemplos; **4 modalidades de colaboración** diferenciadas de H04; CTA | Sin nueva imagen por defecto; no repetir trío H02 |
| **Infraestructuras** | INF-01–INF-07 | Hero con imagen lateral; necesidades; 4 ámbitos + transversal; entregables; relaciones INF/ENE/DIG; experiencia editorial; CTA | R18 entrada propuesta; R15/R20 solo reservas |
| **Sistemas energéticos** | ENE-01–ENE-07 | Hero con imagen lateral; necesidades; 6 ámbitos + nota hídrica; entregables; integración; experiencia editorial; CTA | R10 entrada propuesta; R08 secundaria condicional |
| **Automatización** | DIG-W01–DIG-W07 | Hero con imagen lateral; necesidades; 6 ámbitos + transversal; entregables; interfaces; experiencia editorial; CTA | R01 entrada propuesta; R03 secundaria condicional |
| **Sectores** | SEC-01–SEC-05 | Hero textual; **6 grupos en 2 columnas × 3 filas escritorio**, 1 columna móvil; problemas comunes; colaboración; CTA | Sin fotografías sectoriales por defecto; sin inventar sexto recurso gráfico |
| **Proyectos y experiencia** | PE-01–PE-04 | Hero textual; índice de referencias **solo en estado publicable**; criterio de atribución; CTA | Ninguna fotografía genérica como prueba; no imponer 3+3 ni huecos |
| **Sobre BAFRAS** | SB-01–SB-05 | Hero textual; 3 perfiles del equipo; método; experiencia/colaboración; CTA | Retratos propios aún no inspeccionados; variante tipográfica neutral sin rostros ajenos |
| **Contacto** | CO-01–CO-04 | Hero/introducción compacta; formulario accesible y contacto alternativo; orientación y privacidad; cierre | Sin imagen |

La matriz es de **cobertura de bloques**, no reemplaza la tabla de trazabilidad de **cada bloque/subbloque** exigida en §13.10: esa tabla deberá registrar identificador D03 inequívoco, contenido, variante C02, ubicación, CTA/destino, recurso C03, condiciones editoriales, escritorio/móvil y estado de aprobación.

### 19.3 Primeras decisiones de composición C04, a verificar en wireframes

**C04-H01 — Hero de Inicio:** conservar la composición asimétrica aprobada, con H1 y CTA sobre fondo liso y **R24 a la derecha** en escritorio; móvil apilado **texto → CTA → imagen**, sin texto superpuesto. Se evitará usar R24 como prueba de obra propia. Recorte final de la fotografía pendiente de la maqueta high fidelity, no de Codex.

**C04-H02 — Capacidades en Inicio:** tres tarjetas iguales, imagen 4:3 superior, contenido D03 íntegro, ejemplos y enlace inferior. R23/R22/R21 se ensayan como conjunto; sin transformar las imágenes en iconos ni jerarquizar una especialidad por tamaño.

**C04-H03/H04/H05:** composiciones tipográficas con separadores y numeración moderada. H03 son cuatro necesidades, H04 son cuatro principios de trabajo no contractuales, H05 son cuatro grupos de portada; no sustituirlos por seis sectores de SEC-02.

**C04-INF/ENE/DIG:** estructura coherente de cabecera con fotografía independiente y amplitud de servicios preservada en el texto. Las imágenes de entrada **no representan exhaustivamente** cada especialidad. No imponer foto a cada ámbito ni diagramas de flujo; C04 justificará cualquier segunda imagen por mejora concreta de comprensión.

**C04-SEC:** seis tarjetas editoriales homogéneas, sin depender de imágenes heterogéneas del inventario. **C04-PE:** versión sin fichas publicables si faltan evidencias, conservando el contenido D03 permitido. **C04-SB:** tres perfiles con igualdad de peso y alternativa tipográfica. **C04-CO:** foco en el formulario de cuatro campos (nombre, correo y mensaje obligatorios; empresa opcional), email alternativo y privacidad; sin decoración fotográfica.

### 19.4 Entregables y criterios de validación para C04

1. **C04-EV-01:** nueve wireframes de página completa en escritorio y móvil; ningún bloque D03 ausente o reordenado sin decisión expresa.
2. **C04-EV-02:** maquetas completas de alta fidelidad de Inicio, Infraestructuras y Contacto; tipografía, proporciones, color, espaciado, medios y estados de interacción especificados.
3. **C04-EV-03:** módulos distintivos de las otras seis páginas, suficientes para reconstruirlas sin decisiones estéticas libres.
4. **C04-EV-04:** matriz granular de cobertura y CTA por subbloque D03, más tabla de medios con ID R, ruta, encuadre escritorio/móvil, texto alternativo contextual y crédito.
5. **C04-EV-05:** pruebas de diseño 320/375/390/768/1024/1440, zoom 200 %, texto CA/DE largo, estados de teclado y foco; la prueba real de navegador se reserva para implementación/C05 según contrato.
6. **C04-EV-06:** variantes y estados sin experiencia acreditada/retratos, sin falsos placeholders; registro de decisiones abiertas y resolución antes de G1.

**Secuencia inmediata:** (1) wireframe completo Inicio con R24 y trío H02; (2) wireframe completo Infraestructuras y Contacto; (3) resto de seis páginas; (4) tres maquetas hi-fi y módulos singulares; (5) revisión conjunta y cierre C04. **Estado:** C04 v0.1 iniciado a nivel de especificación, pendiente de evidencias gráficas; G1 sigue sin aprobarse.

---

## 20. B02.2 / C04 v0.2 — Wireframe completo Inicio H01–H07 · propuesta visual para revisión · 03/11/2026

**Estado:** EVIDENCIA PRODUCIDA, PENDIENTE DE VALIDACIÓN DE DIRECCIÓN. No es aprobación de alta fidelidad, G1 ni autorización de implementación. Esta sección complementa §19 sin modificar D03, C01, C02 o selección aprobada R24. Las evidencias son un prototipo HTML autónomo y capturas de página completa en `C04_Inicio/`; el HTML es **instrumento de diseño**, no código destinado a la web productiva. Los colores y la fuente del boceto son aproximaciones funcionales y no tokens corporativos aprobados.

### 20.1 Evidencias y trazabilidad

| Evidencia | Archivo | Propósito |
|---|---|---|
| C04-IN-01 | `C04_Inicio/wireframe_inicio.html` y `C04_Inicio/assets/R24.webp`, `R23.webp`, `R22.webp`, `R21.webp` | Página completa, copy literal D03 y fotografías reales, diseño fluido, sin modificar web productiva |
| C04-IN-02 | `C04_Inicio/C04_inicio_desktop.png` | Captura completa 1440 px |
| C04-IN-03 | `C04_Inicio/C04_inicio_mobile.png` | Captura completa 390 px |
| C04-IN-04 | `C04_Inicio/C04_inicio_mobile_320.png` | Captura completa 320 px |
| C04-IN-05 | `C04_Inicio/C04_inicio_tablet.png` | Captura completa 768 px |
| C04-IN-06 | `C04_Inicio/C04_inicio_desktop_1024.png` | Captura completa 1024 px |

**Verificación efectuada:** renderizado automatizado de la página completa en Chromium con contenido HTML e imágenes incrustadas en memoria; en 320, 390, 768, 1024 y 1440 px no se detectó desbordamiento horizontal del documento. No se ha probado zoom 200 %, idiomas CA/DE, lector de pantalla, funcionalidad de navegación ni contraste WCAG de la identidad final. El prototipo emplea enlaces de anclaje **solo ilustrativos**: las rutas reales deberán apuntar a páginas definidas en D03/D04. El menú móvil es representación estática y no interacción implementada.

### 20.2 Matriz de composición de Inicio

| Bloque | Contenido D03 | Composición escritorio propuesta | Móvil propuesto | Imagen/elementos | Regla comercial y semántica |
|---|---|---|---|---|---|
| H01 | Eyebrow, H1, subtítulo, cuerpo, dos CTA exactos | Dos columnas asimétricas, texto a izquierda y foto a derecha, fondo sin textura bajo copy | Una columna: eyebrow → H1 → subtítulo → cuerpo → CTA → imagen | **R24 aprobada**, imagen independiente, `object-fit: cover`, foco visual central provisional | H1 único; CTA primario Contacto y secundario Capacidades; sin presentar fotografía como obra BAFRAS |
| H02 | H2, introducción, tres tarjetas con texto, tres ejemplos y enlace, enlace complementario | Tres tarjetas equivalentes con imagen superior, contenido íntegro y enlace alineado en base | Tarjetas apiladas, imagen 16:10 provisional para reducir altura de desplazamiento | **R23 INF / R22 ENE / R21 DIG**, candidatas aún sin aprobación expresa | Ninguna especialidad privilegiada; cada enlace conduce a su subpágina, no a un ancla interna |
| H03 | H2, intro, cuatro necesidades con explicación y enlace | Matriz 2×2 de **filas editoriales** con separadores, numeración discreta, sin tarjetas fotográficas | Cuatro filas verticales con título, texto y enlace visibles | Sin imágenes ni iconos | Orden de necesidades D03; enlaces a INF, ENE, DIG y Capacidades |
| H04 | H2, texto, cuatro pasos, cierre y enlace | Cuatro columnas de pasos 01–04, línea superior; conclusión independiente | Cuatro pasos verticales con línea superior y cierre posterior | Sin diagrama de flujo ni imágenes | No confundir pasos conceptuales con fases contractuales ni con cuatro modalidades C04 de Capacidades |
| H05 | H2, texto, cuatro grupos de portada, enlace único | Cuatro paneles tipográficos de igual peso, sin fotos heterogéneas | Cuatro paneles verticales | Sin fotografías sectoriales | Cuatro grupos de portada D03, no sustituyen seis sectores de la página Sectores |
| H06 | H2, texto y enlace, sin referencias publicables | Bloque editorial de lectura breve con una columna de texto principal | Bloque editorial de una columna | Sin tarjetas de proyectos ni fotos genéricas | La nota explicativa de ausencia de referencias en prototipo es **anotación de diseño**, no copy para publicar; no mostrarla en web |
| H07 | H2, texto, CTA, microcopy | Banda de cierre de contraste moderado y CTA prominente | Banda vertical con botón de ancho disponible | Sin fotografía | CTA a Contacto; microcopy de colaboración íntegro |
| Global | Menú y pie según D03/C01 | Cabecera horizontal, navegación y contacto destacado; pie compacto | Cabecera con botón de menú como representación de patrón C01; pie apilado | Logo textual **solo marcador de posición**, no sustituto del logo oficial | Idiomas solo publicados, enlaces reales, información legal/contacto verificada antes de publicación |

### 20.3 Decisiones de ritmo y jerarquía

1. **H01 como apertura principal**: imagen R24 tiene peso suficiente sin texto sobreimpreso. Evitar una segunda foto hero, overlays oscuros o gradientes decorativos.
2. **H02 es el único bloque con una tríada fotográfica**. Mantener recortes consistentes, igual anchura, altura y posición de enlace; la equivalencia no exige igual longitud de texto.
3. **H03 y H04 se diferencian**: necesidades = 2×2 editorial; filosofía = secuencia conceptual de cuatro pasos sin flechas ni promesas de proceso fijo.
4. **H05 se simplifica** a cuatro etiquetas sectoriales tipográficas; sin iconos o fotos obligatorios. Evitar monotonía mediante contraste entre fondos blancos/superficies neutras, no mediante gráficos artificiales.
5. **H06 no debe aparentar una cartera acreditada**. En el boceto aparece una nota de producción que se eliminará en la maqueta publicable; la versión de publicación muestra solo D03 permitido.
6. **H07 cierra la lectura con CTA directo**, evitando formulario incrustado en portada; formulario completo pertenece a Contacto.
7. **El diseño debe ser legible y escaneable**: título claro, introducción limitada en anchura, tarjetas técnicas sin decoración superflua, separadores y espaciado estable. No editar copy D03 para reducir alturas.

### 20.4 Decisiones propuestas y pendientes de validación

| ID | Propuesta | Estado | Criterio de aprobación |
|---|---|---|---|
| C04-IN-D01 | H01 dos columnas con R24 lateral; móvil texto antes de foto | Propuesta coherente con aprobación previa | Revisar proporción/foco de imagen en alta fidelidad |
| C04-IN-D02 | H02 trío R23/R22/R21 con imágenes superiores | Propuesta | Aprobar conjunto y equilibrio de tarjetas |
| C04-IN-D03 | H03 2×2 sin imágenes | Propuesta | Lectura y jerarquía de las cuatro situaciones |
| C04-IN-D04 | H04 cuatro columnas sin flechas | Propuesta | Diferenciación entre filosofía y proceso contractual |
| C04-IN-D05 | H05 cuatro paneles sin fotos | Propuesta | Sobriedad y escaneabilidad |
| C04-IN-D06 | H06 texto sin fichas, sin anotación de producción en publicación | Propuesta | Ausencia de atribuciones engañosas |
| C04-IN-D07 | H07 banda final con CTA principal | Propuesta | Conversión sin redundancia |
| C04-IN-D08 | Cabecera y footer como representación C01, sin inventar logo ni legales | Propuesta | En maquetas usar marca real, menú interactivo y enlaces correctos |

**Transferencia a D04 (sin prescribir código):** la composición es realizable con componentes aprobados `PageHero`, `ContentCard(capability)`, `NeedList`, patrón de pasos de filosofía, sectores editoriales, bloque de experiencia y `ContactBand`. Mantener H01–H07 en orden D03, sin inventar modelos por bloque. Recursos de imágenes con identificador y atribución trazables; CSS responsive basado en contenido y tokens reales. El HTML de evidencia no debe copiarse como plantilla productiva: contiene estilos de prueba, rutas de anclaje y anotaciones de diseño. La implementación futura verificará accesibilidad, navegación, traducciones y cumplimiento de licencias.

**Próxima decisión:** revisión por dirección de la composición completa, especialmente densidad de H02 y tratamiento tipográfico H03–H05. No se declara aprobado C04-IN hasta esa validación. G1 sigue pendiente.


## 21. C04 — Iteración visual 02 de Inicio (propuesta, no aprobada)

**Fuente editorial:** Documento 03, Parte A, H01–H07. La maqueta conserva literalmente H1, H2, subtítulos, párrafos, listas, títulos y microcopy de las siete secciones; se aplican las decisiones vinculantes de 03 para el correo público `info@bafras.com`. Los indicadores de sección y notas de wireframe dejan de ser visibles en la maqueta.

**Fuente cromática auditada:** B01: pino `#0E2B25`, verde `#1A7A5A`, piedra verde `#4F7B6E`, tinta `#2A2A2A`, gris `#4A5550`, papel `#F7F5F0`, beige `#ECE8DD`, línea `#D8D2C3`, blanco `#FFFFFF`. Tipografía Inter con fallback de sistema; no se adjunta fuente licenciada. La cabecera textual BAFRAS es un sustituto provisional del logotipo original, no una recreación aprobada.

**Medios:** H01 R24 aprobada; H02 R23, R22, R21. Resto sin fotografías; H06 no simula proyectos. Las imágenes son ilustraciones sectoriales y no evidencia de proyectos propios.

**Composición:** hero asimétrico con fotografía a la derecha en escritorio y debajo del texto en móvil; H02 tres tarjetas equivalentes 4:3 en escritorio y una columna en móvil; H03 necesidades 2×2 y una columna; H04 cuatro pasos en línea y columna; H05 cuatro sectores en fila grande, dos columnas intermedias y una en móvil; H06 editorial; H07 cierre sobre pino.

**Evidencias de iteración 02:** `C04_Inicio_V2/inicio_v2.html`, `inicio_v2_desktop.png` (1440), `inicio_v2_desktop_1024.png`, `inicio_v2_tablet.png` (768), `inicio_v2_mobile.png` (390), `inicio_v2_mobile_320.png`; `C04_Inicio_V2_BAFRAS.zip` contiene las imágenes WebP usadas y HTML portable. Verificación automatizada de ausencia de overflow horizontal a los cinco anchos.

**Limitaciones de la evidencia:** navegación entre páginas representada por URLs futuras; el menú móvil no es interactivo en esta maqueta; el logotipo es tipográfico provisional; no se han ejecutado pruebas completas de teclado, lector de pantalla ni traducciones. El material es una propuesta C04 de alta fidelidad, no un artefacto de producción.

**Pendiente de decisión:** validación estética de la maqueta, incorporación del logotipo corporativo real, revisión de densidad de H02 y ritmo H03–H06, y aprobación G1 antes de cambios productivos.


## 22. C04 Inicio — Iteración visual 03: ritmo editorial H03–H06 (PROPUESTA)

**Motivación:** el promotor identifica exceso de homogeneidad en H03–H06: sucesión de franjas horizontales tipográficas sin suficiente contraste compositivo. La intervención es localizada, no altera D03, el orden H01–H07 ni los medios aprobados de H01/H02. **Pendiente de aprobación del promotor; G1 permanece cerrado.**

### 22.1 Decisiones del equipo multidisciplinar

| Bloque | Composición propuesta | Medio y tratamiento | Móvil | Restricción |
|---|---|---|---|---|
| H03 Necesidades | Apertura asimétrica: título/introducción izquierda y fotografía contextual derecha; cuatro situaciones 2×2 con divisores finos, sin tarjetas decorativas | **R03**, `assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp`; recorte apaisado `object-fit: cover`, centro 46 %; leyenda que distingue imagen contextual de proyecto | Foto bajo la introducción; situaciones en una columna | No afirmar que R03 corresponde a un trabajo BAFRAS; no añadir nuevos claims |
| H04 Filosofía | Introducción en dos columnas, secuencia editorial de cuatro pasos con números grandes y líneas divisorias; sin flechas ni diagrama técnico ficticio | Ninguna fotografía nueva | Secuencia vertical legible | Mantener los cuatro pasos y cierre literal D03 |
| H05 Sectores | Bloque verde pino con columna editorial y matriz 2×2 de cuatro sectores; CTA integrado en la columna editorial | Sin fotografía: una foto de un único sector rompería equivalencia de los cuatro | Texto primero y matriz 2×2, tarjetas reducidas | No convertir los cuatro grupos de portada en taxonomía definitiva |
| H06 Experiencia | Bloque claro de respiro, texto editorial y recuadro de atribución; jerarquía distinta de H04 y H05 | Sin fotografía ni logos de proyectos | Una columna, recuadro bajo texto | No inventar referencias, cifras, clientes o proyectos |
| H07 Contacto | Banda de cierre existente | Sin cambios | Sin cambios | Evitar dos bandas oscuras consecutivas: H06 claro entre H05 y H07 |

**Selección de medios C03 actualizada:** se propone incorporar **R03** en H03, además de su uso secundario/reserva en DIG; no sustituye ni modifica R24 (H01), R23/R22/R21 (H02). Derechos: material de biblioteca declarado reutilizable por el promotor; conservar atribución exigida por licencia específica y registro de fuente. El archivo es una fotografía de instrumentación, no una referencia acreditada de obra. R03 **propuesta, no aprobada** hasta validación visual.

### 22.2 Implementación de maqueta de revisión

- Evidencia fuente: `C04_Inicio_V3/inicio_v3.html`; WebP reales en `C04_Inicio_V3/assets/`.
- Tokens cromáticos mantenidos: `#0E2B25`, `#1A7A5A`, `#F7F5F0`, `#ECE8DD`. No se proponen nuevos tokens normativos.
- H03–H06 cambian solo disposición y superficies; no se reescriben los párrafos de D03. Los pequeños rótulos editoriales y la leyenda fotográfica son anotaciones de maqueta a revisar, no copy D03 aprobado. El recuadro H06 añade una nota de atribución como texto de maqueta y debe retirarse o validarse editorialmente antes de publicar.
- Proporciones de escritorio: H03 cabecera 1.1/.75; H04 1/.86; H05 .88/1.12; H06 1.15/.85. Son relaciones orientativas, no dimensiones absolutas obligatorias.
- A ≤850 px las aperturas pasan a una columna; a ≤560 px H03 situaciones y H04 pasos pasan a una columna; H05 conserva matriz 2×2 mientras sea legible. Verificar en navegador 320/390/768/1024/1440 y zoom 200 % antes de G1.
- La revisión de capturas automatizadas en este entorno ha quedado bloqueada por la política de navegación del navegador; **no declarar pruebas visuales ni ausencia de overflow como verificadas** en esta iteración. Revisar HTML localmente y registrar capturas en la siguiente validación.

### 22.3 Estado

**C04 v3 propuesta pendiente de inspección visual y aprobación.** Si se acepta, confirmar R03 en H03 y registrar su selección definitiva en la matriz C03. La cabecera/logo y menú móvil siguen provisionales. Sin modificaciones del repositorio productivo.


## 23. Acta de validación de C04 Inicio V3 y apertura de C04 Infraestructuras — 03/11/2026

**Decisión del promotor:** «Lo veo bien. validamos y continuamos». Se valida la **composición visual de Inicio V3, H01–H07**, incluida la intervención de ritmo en H03–H06 (§22). Esta validación reemplaza el estado «propuesta» de §22 para la **composición**; no implica aceptación del código HTML de demostración como implementación productiva, aprobación de G1 ni finalización de accesibilidad y QA.

### 23.1 Decisiones aprobadas

| Elemento | Decisión validada | Medio | Estado |
|---|---|---|---|
| H01 | Hero asimétrico, texto separado de fotografía | **R24** `assets/images/home/hero/home-hero-engineering.webp` | Aprobado |
| H02 | Tres capacidades de igual peso y tarjetas con imagen superior | **R23/R22/R21** `assets/images/home/capabilities/` | Composición validada; verificar licencias/alt y recortes en QA |
| H03 | Apertura asimétrica con imagen y necesidades 2×2 | **R03** `assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp` | **Nueva selección aprobada**, fotografía contextual, nunca referencia de proyecto propio |
| H04 | Introducción a dos columnas y cuatro pasos numerados, sin diagrama artificial | Sin imagen | Aprobado |
| H05 | Banda verde pino con editorial + cuatro sectores en matriz 2×2 | Sin imagen | Aprobado |
| H06 | Respiro editorial claro, sin inventar proyectos ni atribuciones | Sin imagen | Aprobado con condición: eliminar/validar anotaciones no presentes en D03 |
| H07 | Cierre y CTA de contacto | Sin imagen | Aprobado |

**Actualización explícita de C03:** R03 deja de ser «reserva/propuesta» para H03 y pasa a **imagen asignada aprobada**. Se mantiene su uso secundario posible en DIG sin selección automática. No sustituir R24, R23, R22 ni R21. Derechos: el promotor declara la biblioteca reutilizable; conservar el registro de procedencia y los créditos exigibles por cada licencia.

### 23.2 Condiciones pendientes, sin reabrir la aprobación compositiva

- Sustituir la representación tipográfica de marca por el logotipo corporativo real y respetar C01.
- Resolver menú móvil real, navegación, foco y teclado conforme a D04/C05.
- Verificar recortes, ausencia de overflow, zoom 200 %, 320/375/390/768/1024/1440 px, contraste y longitudes CA/DE en navegador; la iteración V3 no dispone de capturas automatizadas verificadas.
- Eliminar cualquier rótulo de demostración, nota de producción o leyenda no autorizada editorialmente por D03; conservar información de créditos donde corresponda.
- No reutilizar HTML/CSS de maqueta como código productivo sin adaptación arquitectónica y validación.

### 23.3 Siguiente unidad de diseño: Infraestructuras e instalaciones (INF-01–INF-07)

**Fuente de verdad:** D03, bloques INF-01 a INF-07. Se inicia la fase de wireframe, **no se declara realizado ni aprobado** el diseño de Infraestructuras.

| Bloque D03 | Intención de composición para desarrollar y contrastar | Medios y restricciones |
|---|---|---|
| INF-01 Hero | Hero de especialidad: título y valor técnico legibles, foto lateral o composición editorial proporcionada | **R18** `assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp` como selección C03 recomendada; verificar foco y evitar reutilizar R23 de H02 |
| INF-02 Cuándo podemos ayudarte | Necesidades reconocibles y lectura rápida; evitar clonación del H03 | Preferencia tipográfica, sin foto obligatoria |
| INF-03 Ámbitos de ingeniería | Cuatro áreas principales y bloque transversal diferenciado, con jerarquía técnica y espacio para párrafos D03 | No reducir los ámbitos a cuatro etiquetas ni inventar iconografía técnica |
| INF-04 Qué podemos entregar | Lista editorial de entregables claramente escaneable | Sin imagen decorativa |
| INF-05 Relación con otras capacidades | Relaciones con ENE/DIG, enlaces y contraste de sección | Sin diagrama ficticio de integración |
| INF-06 Experiencia y confianza | Texto sobrio, sin referencias de proyectos no verificadas | No emplear fotos de terceros como trabajos propios |
| INF-07 Contacto | CTA de cierre coherente con H07 y la arquitectura de enlaces | Sin imagen |

**Criterio de dirección creativa:** heredar gramática tipográfica, cromática, aire y calidad de Inicio V3, pero **variar la composición**: no repetir exactamente H03–H06 ni añadir fotografías por obligación. Priorizar profundidad y rigor técnico. Entregables próximos: wireframe INF escritorio/móvil, matriz de componentes y estados, revisión del recorte R18 y maqueta contrastada con D03. Después, Contacto y restantes páginas.

**Estado global:** C04 Inicio V3 composición **VALIDADA**; C04 INF **EN PREPARACIÓN**; G1 **PENDIENTE**; repositorio productivo **SIN CAMBIOS**.


## 24. C04 — Infraestructuras e instalaciones · wireframe visual 01 (PROPUESTA, pendiente de validación)

**Fecha:** 03/11/2026. **Fuente editorial:** D03, Parte C, revisión 03.D.2, bloques INF-01–INF-07. Atención: D03 marca explícitamente esta parte como *pendiente de aprobación editorial*, por lo que la maqueta no autoriza publicación. **Base visual:** Inicio V3 validada, tokens y componentes C01–C03. **Evidencia:** `C04_INF/infraestructuras.html`, fotografía real `C04_INF/assets/R18.webp`, capturas desktop/móvil si se verifican. No es código de producción.

### 24.1 Composición por bloques

| Bloque | Decisión propuesta de composición | Medio / reglas | Móvil |
|---|---|---|---|
| INF-01 | Hero asimétrico con texto técnico y CTA a la izquierda, imagen a la derecha; contenido íntegro D03 | **R18**, `assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp`; imagen contextual, no trabajo propio; proporción de contenedor aprox. 1:1, `object-fit:cover`; sin texto superpuesto | Texto y CTA antes de foto; imagen aprox. 6:5 |
| INF-02 | Cinco necesidades como lista numerada editorial en dos columnas, quinto ítem en ancho parcial; no tarjetas ilustradas | Sin imagen; separadores finos y párrafos completos | Una columna, orden DOM 1–5 |
| INF-03 | Cuatro ámbitos equivalentes en cuadrícula 2×2, con descripción íntegra; transversal como banda de ancho completo, no quinta tarjeta | Sin iconografía técnica inventada; ancla `#ambitos` | Cuatro tarjetas apiladas y transversal al final |
| INF-04 | Sección de entregables: titular/introducción izquierda, cuatro modalidades a la derecha en lista de líneas | Nota de precisión literal D03 bajo la lista; no fingir proceso secuencial | Una columna, texto antes de lista |
| INF-05 | Fondo beige; texto explicativo a la izquierda, dos enlaces claros a ENE y DIG a la derecha | Enlaces sin iconos decorativos de sistemas; rutas reales se conectan al implementar | Texto antes de enlaces |
| INF-06 | Bloque editorial claro y enlace a experiencia; panel de apoyo para contraste compositivo | **Panel explicativo provisional NO_PUBLICAR**, ya que su texto no pertenece a D03; eliminarlo o aprobarlo editorialmente | Texto antes de panel |
| INF-07 | Banda final verde pino, título y CTA, coherente con H07 | Sin fotografía | Una columna |

### 24.2 Gramática compartida INF / ENE / DIG

Las tres páginas de especialidad comparten **sistema de composición**, no idéntica cantidad de tarjetas ni contenido: `SpecialtyHero`, `NeedList`, `TechnicalAreaGrid`, `CrossCuttingBand`, `DeliverableList`, `RelatedCapabilities`, `ExperienceEditorial` y `ContactBand`. La arquitectura D04 debe reutilizar solo los componentes que realmente comparten contrato; no crear abstracciones para forzar bloques no equivalentes. Los datos de cada especialidad se alimentan desde D03, con modelos Pydantic v2 cuando correspondan. El diseño debe admitir las seis áreas de ENE/DIG sin inventar nuevas categorías ni recortar textos. Las imágenes principales siguen siendo R18 (INF), R10 (ENE) y R01 (DIG), salvo decisión posterior expresa. Mantener colores pino `#0E2B25`, verde `#1A7A5A`, papel `#F7F5F0`, beige `#ECE8DD` y líneas `#D8D2C3`.

### 24.3 Revisión multidisciplinar y condiciones

- **Dirección creativa:** contraste entre bloques (hero fotográfico, necesidades editoriales, cuadrícula técnica, entregables sin tarjetas, relaciones beige, experiencia y cierre oscuro), evitando una sucesión de franjas homogéneas.
- **Ingeniería INF:** mantener cuatro ámbitos y transversal; no publicar metadatos de catálogo ni excluir matices del copy visible. Evitar fotografías de terceros como supuesta experiencia BAFRAS.
- **UX y accesibilidad:** orden semántico lineal, CTA diferenciados, sin overlay en fotos, navegación teclado y comprobación de 320/375/390/768/1024/1440 y zoom 200 %.
- **Comercial:** necesidades de cliente antes del catálogo técnico; entregables claros y contacto al final.
- **Software:** evidencia HTML portable, no plantilla final. Enlaces de páginas aún provisionales (`href="#"`), logotipo tipográfico, y panel INF-06 con texto no aprobado: no transportar directamente a producción.

**Estado:** C04-INF-v1 **PROPUESTA PARA REVISIÓN**; fotografía R18 **propuesta en composición, no aprobada expresamente como decisión definitiva**; D03-INF pendiente editorial; G1 pendiente. No se ha modificado el repositorio productivo.


## 25. C04 — Infraestructuras e instalaciones · segunda iteración y cierre técnico de propuesta (03/11/2026)

**Evidencia de revisión:** `C04_INF_V2/infraestructuras_v2.html` y `C04_INF_V2/assets/R18.webp`. El archivo HTML es una maqueta autónoma y **no constituye código productivo**. **Estado:** composición de INF **cerrada como propuesta técnica del equipo multidisciplinar, pendiente de validación del promotor**. No implica aprobación G1.

### 25.1 Auditoría crítica v1 → v2

| Hallazgo | Impacto | Resolución v2 |
|---|---|---|
| INF-06 incluía panel explicativo de maqueta ajeno a D03 | Riesgo de publicar contenido no autorizado; ruido visual | **Eliminado**. Se deja bloque editorial con anchura de lectura contenida, título, texto y enlace D03, sin tarjeta inventada. |
| Cinco necesidades INF-02 en rejilla 2×2 + quinta con anchura parcial | Último elemento visualmente residual | Mantener numeración y cinco situaciones, pero sin anchura máxima artificial en la quinta; separación editorial clara. En móvil una columna. |
| INF-02 e INF-03 demasiado próximas en lenguaje de retícula | Homogeneidad visual y pérdida de jerarquía | INF-02: lista abierta con divisores; INF-03: cuatro tarjetas delimitadas y banda transversal verde. Espaciado y ritmo ajustados. |
| Hero R18 con altura fija de 500 px | Recortes impredecibles en tablet | Contenedor de proporción relativa (~1:1 en escritorio; 6:5 y 5:4 en móvil), `object-fit:cover`, sin texto sobre imagen. |
| Menú móvil visible como botón sin interacción | Interacción engañosa | En maqueta, menú funcional con `aria-expanded`, cierre por selección y Escape. Navegación final sigue pendiente de C01/D04. |
| Leyenda de demostración y panel auxiliar | Metadatos internos expuestos al público | Eliminados de la superficie visual; la procedencia y restricciones permanecen en D05. |
| D03 histórico indica INF pendiente; cabecera vigente dice aprobado | Riesgo de interpretar un estado obsoleto | **Prevalece el estado vigente de la cabecera D03 (02/11/2026): INF editorialmente aprobado.** No confundir con habilitación de publicación de servicios en D01 ni con G1. |

### 25.2 Contrato visual de INF para ENE y DIG

| Bloque | Regla compositiva | Reutilización |
|---|---|---|
| INF-01 | Hero de especialidad: texto y CTA separados de fotografía; proporción flexible | Reutilizar patrón con **R10 ENE** y **R01 DIG**, respetando textos y focos propios |
| INF-02 | Lista numerada de necesidades, sin correspondencias ficticias con especialidades | Adaptar cantidad y longitud a D03 ENE/DIG |
| INF-03 | Retícula de cuatro áreas técnicas + banda transversal diferenciada | ENE/DIG: **seis áreas**; no reducir ni forzar transversal inexistente |
| INF-04 | Introducción editorial y lista de entregables a dos columnas | Solo si D03 de la página contiene entregables equivalentes |
| INF-05 | Sección de relación entre capacidades, fondo arena, enlaces funcionales | Enlaces específicos según D03 |
| INF-06 | Experiencia editorial de anchura controlada, sin panel ni fotografías ficticias | Mantener atribución diferenciada y verificación de referencias |
| INF-07 | Cierre corporativo verde pino y CTA | Compartir tratamiento, adaptar copy literal D03 |

**Recurso visual:** R18 `assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp` se **ratifica como selección técnica recomendada** para INF-01, sin incorporar imágenes adicionales. La aprobación definitiva del diseño visual corresponde al promotor. R23 permanece en H02 Inicio; no duplicar por defecto. Derechos: biblioteca declarada reutilizable; preservar metadatos y atribución de licencia cuando proceda.

**Tokens heredados:** pino `#0E2B25`, verde `#1A7A5A`, papel `#F7F5F0`, arena `#ECE8DD`, líneas `#D8D2C3`. Componentes semánticos: encabezado de página, lista de necesidades, rejilla de ámbitos, banda transversal, lista de entregables, enlaces de capacidades, experiencia editorial y CTA final. **No imponer un componente único rígido** a ENE/DIG: reutilizar patrón y contratos solo donde exista equivalencia real.

### 25.3 QA y condiciones para cerrar aprobación visual

- Se verificó **estáticamente** que la maqueta incluye siete bloques INF, el archivo R18 real y elimina el panel de texto no aprobado.
- Se preparó un menú móvil demostrativo con interacción y atributos ARIA; **no se ha ejecutado una prueba de navegador satisfactoria**: Chromium bloquea `file://` por política administrativa en este entorno. Por tanto, no declarar verificadas capturas ni ausencia de overflow.
- En la maqueta aislada, enlaces hacia páginas externas siguen marcados `data-preview-link=true` y redirigidos provisionalmente a la parte superior. El CTA «Cuéntanos tu proyecto» enlaza al cierre de la misma maqueta. **En producción** deberán apuntar a rutas reales localizadas, conforme a D03/D04.
- Antes de G1: probar 320/375/390/768/1024/1440 px, zoom 200 %, foco, teclado, contraste, textos CA/EN/DE, cabecera/logotipo corporativos y navegación real.
- D03 vigente indica aprobación editorial de INF; **los servicios siguen sujetos a las restricciones de publicación de D01**. No presentar proyectos previos como encargos propios.

### 25.4 Dictamen multidisciplinar

- **Dirección creativa:** aprueba como **propuesta técnica** la secuencia visual y el equilibrio de blancos, sin sumar fotos decorativas.
- **Ingeniería INF:** considera preservados los cuatro ámbitos, el transversal, los cinco problemas, los cuatro entregables y las precisiones técnicas.
- **UX/accesibilidad:** estructura y lectura móvil razonables en diseño; falta QA real de navegador y traducciones.
- **Comercial:** recorrido necesidad → capacidad → entregable → experiencia → contacto coherente.
- **Arquitectura frontend:** diseño reutilizable en ENE/DIG con variantes limitadas; no convertir la maqueta aislada en código productivo.

**Conclusión:** equipo recomienda **cerrar el wireframe INF v2 a nivel de propuesta compositiva** y solicitar validación del promotor. **No declarar aprobado por el usuario**, ni aprobar G1, ni iniciar refactorización del sitio.


## 26. Acta de conciliación D03 ↔ D05 y aprobación C04-INF-V2 (03/11/2026) — VIGENTE

### 26.1 Aprobaciones y decisiones de precedencia

El promotor **ha validado expresamente** la composición de Infraestructuras V2, posterior al dictamen §25 que todavía decía «pendiente de validación». Esa frase y las de §23 («INF en preparación») y §24 («INF-v1 propuesta») se conservan solo como **histórico de iteración** y quedan superadas por este apartado. No es necesario reinterpretar ni editar la maqueta v2 para dar por recibida la aprobación compositiva.

| Objeto | Decisión vigente | Estado |
|---|---|---|
| H01 | Hero asimétrico; **R24** `assets/images/home/hero/home-hero-engineering.webp` | Aprobado |
| H02 | Tres tarjetas equilibradas; **R23** INF, **R22** ENE, **R21** DIG, según §23 | Composición Inicio V3 validada |
| H03 | Necesidades en apertura asimétrica; **R03** `assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp` | Aprobado |
| H04–H07 | Metodología numerada, sectores verde pino, experiencia editorial y cierre, según §23 | Composición validada |
| INF-01 | Hero de especialidad con **R18** `assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp` | Composición e imagen validadas |
| INF-02 | Cinco necesidades en lista editorial numerada | Validado |
| INF-03 | Cuatro ámbitos en cuadrícula + transversal diferenciado | Validado |
| INF-04 | Entregables en lista editorial | Validado |
| INF-05 | Integración ENE/DIG en bloque arena | Validado |
| INF-06 | Experiencia editorial **sin panel provisional ni copy inventado** | Validado |
| INF-07 | Cierre y CTA verde pino | Validado |
| ENE / DIG | Reutilizar **gramática de especialidad**, no copiar exactamente cantidades o bloques. **R10** para ENE y **R01** para DIG como punto de partida C03 | C04 específico pendiente |

### 26.2 Límites entre documentos: evitar instrucciones contradictorias

1. **D03** manda sobre copy visible, taxonomía editorial y secuencia de bloques. Las descripciones visuales antiguas de H01 y las sugerencias de maquetación incluidas en D03 no autorizan sustituir R24/R18 ni alterar una composición validada.
2. **D05** manda sobre distribución, imágenes, recortes previstos, paleta, componentes y responsive. La aprobación de INF-V2 reemplaza exclusivamente el estado de «propuesta» en §§24–25; no altera los textos aprobados de INF en D03.
3. **D01** manda sobre disponibilidad comercial y publicación de servicios; **D04** sobre software, seguridad, i18n, pruebas y G1. Validar C04 no significa validar estas materias.
4. **Maquetas** `C04_Inicio_V3/inicio_v3.html` y `C04_INF_V2/infraestructuras_v2.html` son evidencias visuales, no código de producción ni fuente de copy alternativa. No trasladar sus enlaces ficticios, logotipo provisional ni textos de demostración.
5. **Derechos**: biblioteca declarada reutilizable por el promotor; mantener atribuciones exigibles según licencia y no presentar fotos contextuales como proyectos ejecutados por BAFRAS.

### 26.3 Trabajo pendiente y criterio de cierre

**Cerrado por decisión del promotor:** composición C04 Inicio V3 e Infraestructuras V2; asignación R24/R23/R22/R21/R03/R18 en sus destinos indicados. **Pendiente:** C04-ENE y C04-DIG, resto de páginas, verificación en navegador a 320/375/390/768/1024/1440 px y zoom 200 %, accesibilidad, contraste, recortes, traducciones, menú y enlaces reales, logotipo original y comprobaciones de publicación. **G1 permanece pendiente; sin cambios en software productivo.**

**Regla de mantenimiento:** toda decisión posterior aprobada debe añadirse al registro rector, indicando qué estado histórico sustituye; no editar el copy aprobado ni reabrir decisiones cerradas por simple discrepancia de un encabezado antiguo.


## 27. C04-ENE-V1 — Primera maqueta de Sistemas energéticos (03/11/2026) · PROPUESTA, NO APROBADA

**Base normativa:** D03 V1.18, ENE-01–ENE-07; D05 §26 INF-V2 aprobado como gramática de especialidad. La cabecera editorial de ENE en D03 indica **propuesta auditada pendiente de validación**, por lo que esta maqueta no convierte automáticamente el copy en aprobado.

| Bloque | Composición C04-ENE-V1 | Imagen / tratamiento | Estado |
|---|---|---|---|
| ENE-01 | Hero asimétrico, contenido izquierda, imagen derecha; en móvil texto antes de imagen | **R10** `assets/images/capabilities/energy/generation/energy-pv-rooftop.webp`, recorte `object-fit:cover` en escritorio, 4:3 en móvil | Propuesta |
| ENE-02 | Seis necesidades numeradas, dos columnas en escritorio, una en móvil | Sin fotografía adicional | Propuesta |
| ENE-03 | Seis ámbitos en retícula **2 columnas × 3 filas** escritorio, una columna móvil; descripción y línea «Incluye» en cada tarjeta | Sin iconografía o gráficos inventados; nota separada de eficiencia hídrica, no séptimo ámbito | Propuesta |
| ENE-04 | Cuatro entregables en lista editorial, introducción en columna izquierda | Sin fotografía | Propuesta |
| ENE-05 | Bloque arena, texto y enlaces a INF/DIG | Sin fotografía | Propuesta |
| ENE-06 | Experiencia editorial de anchura contenida; sin panel ni proyectos ficticios | Sin fotografía | Propuesta |
| ENE-07 | Cierre verde pino y CTA | Sin fotografía | Propuesta |

**Decisión de diseño propuesta:** R10 basta como imagen de especialidad; R08 (instalación térmica) se conserva en reserva y no se incorpora sin necesidad editorial concreta. Se mantiene la identidad cromática vigente y se reutiliza la gramática INF, sin introducir un esquema de flujos energéticos ficticio. En ENE-03 la línea «Incluye» aporta densidad: valorar si el equilibrio entre precisión y longitud de página es satisfactorio antes de validar.

**Evidencia:** `C04_ENE_V1/sistemas_energeticos_v1.html`, archivo real `C04_ENE_V1/assets/R10.webp` y paquete `C04_ENE_V1_BAFRAS.zip`. Maqueta local no productiva; enlaces entre páginas y contacto son demostrativos. Logotipo tipográfico provisional. El contenido de ENE procede de D03, sin inventar servicios ni referencias.

**QA:** se verificó mediante extracción del documento que hay siete bloques, seis necesidades, seis ámbitos, cuatro modalidades y un recurso WebP real. No hay capturas ni validación de navegador: el entorno no dispone del ejecutable Chromium de Playwright. Pendiente probar 320/375/390/768/1024/1440, zoom 200 %, foco, teclado, recorte, contraste, traducciones y navegación real. **C04-ENE-V1 requiere revisión y validación expresa del promotor. G1 pendiente.**


## 28. C04-ENE-V2 — Iteración personalizada de Sistemas energéticos (03/11/2026) · PROPUESTA

**Precedencia:** este apartado sustituye exclusivamente las decisiones compositivas ENE-V1 de §27; no modifica C04-INF-V2 aprobado, Inicio V3, ni el contenido D03 V1.18. **ENE sigue pendiente de validación editorial y visual.**

### 28.1 Diagnóstico multidisciplinar y cambios

| Hallazgo ENE-V1 | Cambio ENE-V2 | Criterio |
|---|---|---|
| ENE-02 repetía la lista larga de INF | Índice de seis decisiones en tres columnas escritorio, dos tableta, una móvil | Exploración rápida sin eliminar texto |
| ENE-03 seis tarjetas extensas 2×3 con descripción e «Incluye» | Seis capítulos editoriales numerados; tres columnas funcionales título / explicación / servicios; móvil apilado | Jerarquía técnica, lectura fluida y menos sensación de catálogo |
| ENE-03 solo texto después de la apertura | R08 contextual en cabecera de ámbitos, sin overlay ni afirmación de autoría | Representar la dimensión térmica además de la fotovoltaica del hero |
| ENE-04 tenía aspecto semejante a INF | Banda verde pino con cuatro entregables en lista | Distinguir alcance técnico de modalidad de encargo |
| ENE-05 fondo arena repetido | Fondo papel, enlaces técnicos diferenciados | Alternancia cromática sin añadir decoración |
| ENE-06 podía percibirse como otro panel comercial | Editorial de ancho contenido sin proyectos ficticios | Rigor en atribución |

### 28.2 Contrato por bloque

- **ENE-01:** hero asimétrico con R10 `assets/images/capabilities/energy/generation/energy-pv-rooftop.webp`; texto y CTA D03 intactos; imagen separada del texto.
- **ENE-02:** seis necesidades literales D03, índice visual 3/2/1 columnas según ancho; numeración editorial sin alterar orden.
- **ENE-03:** seis ámbitos literales D03; filas de tres zonas semánticas (título, explicación, «Incluye»); alternancia suave papel/arena; R08 `assets/images/capabilities/energy/electrification/energy-heat-pumps.webp` en cabecera de sección como fotografía contextual. Nota hídrica complementaria diferenciada, **no séptimo ámbito**.
- **ENE-04:** cuatro entregables y criterio literal D03; fondo verde pino, separadores suaves, texto de contraste alto.
- **ENE-05:** integración con INF/DIG y enlaces D03, fondo papel; sin gráfico inventado.
- **ENE-06:** experiencia editorial, sin fotografías atribuidas ni casos no documentados.
- **ENE-07:** CTA de cierre corporativo.

### 28.3 Medios, estados y QA

| ID | Archivo de biblioteca | Uso | Estado |
|---|---|---|---|
| R10 | `assets/images/capabilities/energy/generation/energy-pv-rooftop.webp` | ENE-01 hero | Se mantiene propuesta C03 |
| R08 | `assets/images/capabilities/energy/electrification/energy-heat-pumps.webp` | ENE-03 cabecera de ámbitos; recorte adaptable, sin texto superpuesto | **Nueva propuesta C04-ENE-V2; pendiente de aprobación** |

Los recursos proceden de la biblioteca facilitada como reutilizable; conservar atribución y condiciones específicas de licencia. No atribuir las fotografías a proyectos ejecutados por BAFRAS.

**Evidencia:** `C04_ENE_V2/sistemas_energeticos_v2.html` y `C04_ENE_V2_BAFRAS.zip`, con R10 y R08 reales. HTML de revisión, no productivo. El logo sigue tipográfico y enlaces externos son demostrativos. No se han alterado los textos visibles de los seis ámbitos, seis necesidades ni cuatro entregables; las etiquetas de interfaz no son nuevas prestaciones.

**Verificación:** estructura, recursos y contenido comprobados estáticamente. El intento de captura Chromium no completó en el entorno; **no declarar verificados** los recortes, overflow, responsive, zoom, contraste ni interacción hasta ejecutar pruebas reales en navegador. Probar 320/375/390/768/1024/1440, zoom 200 %, teclado, CA/EN/DE y menú.

**Dictamen:** dirección creativa, UX, ingeniería energética, comercial y frontend recomiendan ENE-V2 como solución más adecuada que ENE-V1, **sin aprobarla en nombre del promotor**. No modifica G1 ni autoriza cambios de producción.


## 29. Registro de validación C04-ENE-V2 (03/11/2026) · APROBADO

**Decisión expresa del promotor:** «Validamos, continuamos con automatización y control». Se aprueba la **composición visual ENE-V2 de §28** y se sustituyen las propuestas de composición ENE-V1 de §27. Se confirma **R10** para ENE-01 y **R08** para la cabecera de ENE-03, con las rutas exactas registradas en §28.3. La aprobación es de composición visual; no convierte en aprobadas otras cuestiones editoriales, técnicas o de publicación pendientes. La estructura de capítulos numerados ENE es específica y **no se impone a DIG**. Permanecen pendientes la validación responsive en navegador, accesibilidad, logotipo y enlaces productivos. **G1 pendiente**.

## 30. C04-DIG-V1 — Wireframe visual Automatización y control (03/11/2026) · PROPUESTA

**Fuente editorial:** D03 V1.18, DIG-W01 a DIG-W07 (texto editorial aprobado). **Precedencia:** esta propuesta no modifica Inicio V3, INF V2 ni ENE V2 aprobados. Reutiliza tokens y componentes base, no la distribución particular de ENE.

### 30.1 Auditoría multidisciplinar

- **Ingeniería de automatización:** preservar diferencias entre medida, PLC/DDC, SCADA/BMS, comunicaciones OT, software técnico y EMS/PPC; no equiparar monitorización con control ni ofrecer certificación de ciberseguridad o IA como capacidades implícitas.
- **UX:** cinco necesidades en lista numerada 2/1 columnas; seis ámbitos 2×3 escritorio y 1 columna móvil, con etiquetas secundarias; transversal separado.
- **Dirección creativa:** dos fotografías reales (R01 hero, R03 contextual) y alternancia papel/arena/verde pino, sin flujogramas inventados ni capturas DEMO.
- **Dirección comercial:** lectura desde problema a ámbito, entregable, coordinación y contacto; experiencia sin proyectos ficticios.
- **Arquitectura frontend:** contratos compartidos de hero, necesidades, tarjetas y entregables; variante DIG propia para etiquetas y transversal, sin imponer capítulos ENE.

### 30.2 Contrato por sección

| Bloque D03 | Composición y comportamiento | Medios | Estado |
|---|---|---|---|
| DIG-W01 | Hero dos columnas; texto primero en móvil; CTA principal a Contacto, secundario `#ambitos` | R01 `assets/images/capabilities/digital/automation/digital-plc-control-panel.webp`, proporción visible aproximada 4:3 / recorte cover | Propuesta |
| DIG-W02 | Cinco necesidades numeradas, dos columnas escritorio, una móvil; textos íntegros | Ninguno | Propuesta |
| DIG-W03 | Encabezado con imagen contextual; seis tarjetas 2×3 escritorio / una columna móvil; cada una con título, descripción y etiquetas D03; transversal ancho completo separado | R03 `assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp`, 4:3, `object-fit:cover` | Propuesta; repetición R03 de H03 a valorar |
| DIG-W04 | Cuatro entregables como lista abierta y nota literal de alcance | Ninguno | Propuesta |
| DIG-W05 | Fondo arena, dos relaciones INF/ENE y cierre literal D03; enlaces reales solo en implementación | Ninguno | Propuesta |
| DIG-W06 | Editorial sin referencias ni fotografías de proyectos no acreditados | Ninguno | Propuesta |
| DIG-W07 | Cierre verde pino, CTA a Contacto en producción | Ninguno | Propuesta |

### 30.3 Trazabilidad, límites y QA

**Evidencia:** `C04_DIG_V1/automatizacion_control_v1.html`, `C04_DIG_V1/assets/R01.webp`, `C04_DIG_V1/assets/R03.webp`; paquete `C04_DIG_V1_BAFRAS.zip`. Las fotografías son recursos contextuales licenciados, **no fotografías de trabajos de BAFRAS**. Mantener créditos exigidos por las licencias específicas.

**Verificaciones estructurales realizadas:** presencia de siete bloques, cinco necesidades, seis ámbitos con etiquetas, bloque transversal y cuatro entregables. **No verificado:** capturas reales de navegador, comportamiento en 320/375/390/768/1024/1440, zoom 200 %, contraste WCAG, traducciones, recortes efectivos, teclado completo y enlaces entre páginas. La maqueta utiliza logotipo tipográfico provisional y enlaces no productivos. **C04-DIG-V1 requiere validación del promotor. G1 continúa pendiente.**


## 31. Acta de validación C04-DIG-V1 — APROBADO (03/11/2026)

**Decisión expresa del promotor:** «Validamos y continuamos». Se valida la composición DIG-W01–DIG-W07 descrita en §30, incluidas las seis tarjetas técnicas con etiquetas, el transversal diferenciado, el hero R01 y la fotografía contextual R03. No se reabre la elección de imágenes ni se extrapola la composición a otras páginas. Se conservan los textos D03 sin alteración. **Aprobación de diseño, no de calidad de implementación ni gate G1**. Siguen pendientes la revisión efectiva en navegador de 320/375/390/768/1024/1440 px, zoom 200 %, teclado, contraste, traducciones y logo real.

## 32. C04 — Capacidades: briefing de composición inicial (PENDIENTE DE MAQUETA Y VALIDACIÓN)

**Fuente editorial única:** D03 V1.18, página Capacidades, C01–C05. El propio D03 declara su texto como versión consolidada **pendiente de aprobación editorial expresa**; no se infiere su aprobación por validar DIG. No modificar títulos, párrafos, ámbitos destacados, ejemplos ni CTA en D05.

- **C01 — Cabecera:** hero compacto y editorial, sin fotografía obligatoria; antetítulo, H1, introducción y enlace ancla `#especialidades`. Menor altura que H01.
- **C02 — Tres áreas:** sección principal con tres paneles de igual peso y títulos/explicaciones/ámbitos/enlaces íntegros D03. Preferir tratamiento tipográfico limpio antes que repetir automáticamente R23/R22/R21, ya visibles en Inicio; evaluar fotografías solo si la comparación real demuestra mejora. En escritorio tres columnas cuando los textos lo permitan; dos o una columnas según legibilidad, sin forzar tres tarjetas estrechas.
- **C03 — Ingeniería que conecta disciplinas:** tres ejemplos de aplicación claramente rotulados como **hipotéticos**, no casos reales. Proponer composición editorial distinta de C02 (tres filas o capítulos breves), sin diagrama técnico inventado. Enlaces contextuales discretos.
- **C04 — Cómo podemos colaborar:** cuatro modalidades como cuadrícula compacta o lista abierta, evitando una falsa secuencia obligatoria de fases.
- **C05 — Contacto:** cierre corporativo con CTA principal y enlace secundario exactamente según D03.

**Revisión multidisciplinar requerida:** dirección creativa (ritmo y densidad), UX (lectura y orientación), ingeniería INF/ENE/DIG (corrección de ámbitos y ejemplos), comercial (CTA y claridad) y frontend (variantes sin abstracciones innecesarias). **Próxima evidencia:** maqueta completa desktop/móvil con texto literal D03, medios originales si se usan, y registro de diferencias respecto al patrón de especialidades. No confundir esta preparación con aprobación C04-CAP.


## 33. C04-CAP-01 — Estrategia narrativa y wireframe conceptual de Capacidades (03/11/2026) · PROPUESTA

**Fuentes y precedencia.** D03 V1.18, C01–C05 es la autoridad editorial; D05 determina exclusivamente su representación. Esta iteración sustituye la preparación genérica de §32 en cuanto a estrategia de composición, pero **no aprueba una maqueta visual**, no altera copy ni reabre Inicio/INF/ENE/DIG. La cabecera general de D03 considera Capacidades aprobada; la leyenda histórica local de Parte B que indica «pendiente» no debe prevalecer.

### 33.1 Diagnóstico multidisciplinar y propósito

- **Dirección comercial:** no convertir la página en tres silos de servicios. Permitir a clientes con problema definido, mixto o sin diagnóstico encontrar una ruta adecuada sin prometer diagnóstico gratuito ni selección automática de tecnologías.
- **Ingeniería INF/ENE/DIG:** mostrar que una misma actuación puede requerir solo una disciplina, varias o una fase inicial de comprobación. Los ejemplos C03 son supuestos ilustrativos, no proyectos ni paquetes de servicio; preservar su carácter condicional («puede», «puede ser conveniente»).
- **UX y accesibilidad:** lectura no lineal y escaneable; tres áreas de igual peso; enlaces descriptivos y orden DOM idéntico al visual; sin carrusel, acordeones obligatorios, filtros, cuestionarios o animaciones.
- **Dirección creativa:** diferencia visible entre C02 (elección de especialidad), C03 (relación entre disciplinas) y C04 (modalidades contractuales). Evitar sucesión de tres retículas de tarjetas semejantes.
- **Frontend:** componentes existentes cuando sean adecuados, variante propia de índice de capacidades y ejemplos; no imponer las maquetas particulares INF/ENE/DIG ni crear un motor de recomendación.

**Objetivo primario:** el usuario entiende que BAFRAS define el alcance según el problema y puede intervenir desde una o varias especialidades. **Objetivos secundarios:** identificar las tres áreas; entender escenarios de integración; comprender que las modalidades no son fases obligatorias; encontrar una vía de contacto aunque no conozca la solución.

### 33.2 Flujos orientativos y criterios de éxito

| Perfil | Entrada y lectura probable | Salida deseada | Riesgo a evitar |
|---|---|---|---|
| Especialidad conocida | C01 → C02 → ficha INF/ENE/DIG | Explorar la capacidad y contactar | Obligar a leer ejemplos antes de entrar |
| Problema transversal | C01 → C03 → enlaces contextuales → contacto | Entender coordinación condicionada | Representar tres disciplinas como siempre necesarias |
| Problema sin diagnóstico | C01 → C03/C04 → C05 | Poder explicar el contexto sin seleccionar área | Convertir la web en autodiagnóstico |
| Colaborador técnico | C02 → C04 → Sobre BAFRAS/Contacto | Identificar modalidad de colaboración | Prometer ejecución integral o funciones reguladas |

**Aceptación cualitativa a verificar con usuarios:** distinguir especialidades, explicar con palabras propias cuándo se combinan, reconocer que las cuatro modalidades son opciones no secuenciales, localizar el contacto sin haber elegido disciplina. No asignar métricas cuantitativas no medidas.

### 33.3 Wireframe conceptual y jerarquía C01–C05

| Bloque | Composición propuesta escritorio | Adaptación móvil | Función narrativa | Recursos |
|---|---|---|---|---|
| C01 | Hero editorial compacto, antetítulo + H1 + párrafo de anchura controlada y enlace `#especialidades`; sin imagen | Una columna; enlace visible tras intro | Enunciar que el encargo puede ser mono/multidisciplinar | Sin fotografía |
| C02 | Tres paneles equivalentes con título, párrafo, «Ámbitos destacados» y enlace. Desktop 3 columnas **solo si** longitud y ancho permiten lectura; alternativa recomendada: tres filas editoriales con índice 01–03, texto y ámbitos en subcolumnas | Una columna; títulos y enlaces siempre visibles | Elegir disciplina por su función, no por iconografía | Sin repetir R23/R22/R21 por defecto |
| C03 | **Sección protagonista diferenciada**: fondo arena suave; introducción y tres casos numerados en filas abiertas. Cada caso conserva su texto literal y puede mostrar una línea secundaria de disciplinas enlazadas, sin atribución de proyecto | Casos apilados; texto y enlaces en orden lógico | Mostrar tres situaciones donde la necesidad determina combinación de especialidades | Sin fotos de proyectos ni diagrama causal inventado |
| C04 | Cuatro modalidades como lista editorial 2×2 con numeración discreta; sin flechas ni timeline | Lista vertical | Explicar distintas formas de colaborar, no fases de un contrato | Sin imágenes |
| C05 | Cierre verde pino con pregunta H2, párrafo y CTA principal; enlace secundario de experiencia | Columna única, botones/enlaces no solapados | Convertir sin exigir diagnóstico previo | Sin imagen |

**Composición preferida para evaluar en maqueta:** C02 en tres filas editoriales de igual jerarquía en lugar de tres tarjetas densas, por la longitud literal de los párrafos y cuatro ámbitos de cada disciplina; si la maqueta 1440 demuestra legibilidad superior en tarjetas, comparar antes de cerrar. C03 debe tener mayor singularidad visual que C04; no añadir nuevas frases publicables («elige tu ruta», «te diagnosticamos») sin aprobación D03.

### 33.4 Semántica visual sin falsas inferencias

1. **No dibujar un flujo INF → ENE → DIG**: sugeriría secuencia obligatoria. No dibujar tres círculos siempre intersectados: sugeriría colaboración forzosa.
2. Si se utiliza una representación de relación, que sea un **marcador editorial no técnico** asociado a cada ejemplo (etiquetas/enlaces de capacidades), nunca un esquema de ingeniería, algoritmo de diagnóstico ni atribución de proyecto.
3. Los tres ejemplos C03 conservan exactamente sus textos: modernización térmica; autoconsumo y almacenamiento; problemas de funcionamiento. Identificar visualmente «Ejemplos de aplicación» como etiqueta de interfaz, no como nueva afirmación editorial.
4. C04 muestra modalidades independientes: Diagnóstico y estudios; Diseño y proyecto; Asistencia y coordinación; Programación, integración y verificación. No presentar las cuatro como alcance estándar de todos los contratos.
5. CTA C05 permite contactar sin seleccionar una disciplina; no hay selector obligatorio ni recomendador de servicios.

### 33.5 Decisiones de medios y relación con C03

**Primera propuesta:** página predominantemente editorial, sin imágenes nuevas. No reutilizar por defecto R23/R22/R21 de Inicio H02: repetición sin valor adicional. No incorporar imágenes sectoriales o de proyectos como evidencia de trabajos de BAFRAS. Si el primer render visual resulta demasiado homogéneo, ensayar primero contrastes de fondo, escalas tipográficas, alineaciones y densidad; cualquier nueva imagen exigirá justificar su papel y actualizar esta matriz.

### 33.6 Implicaciones técnicas y comprobaciones

- HTML: `main` con un H1 en C01; H2 para C02–C05; H3 por especialidad/ejemplo/modalidad cuando corresponda; listas semánticas cuando sean listas. Evitar duplicar contenido D03 en templates.
- Ancla `#especialidades` asociada a C02; enlaces a las tres rutas de especialidad, contextualizados en C03 cuando proceda; Contacto y Proyectos y experiencia en C05.
- CSS: layout responsive basado en anchura real del texto, `minmax(0,1fr)`, sin alturas rígidas; comprobar traducciones y zoom 200 %. C02 debe mantener peso visual equivalente incluso con párrafos de distinta longitud.
- No JS para el flujo de orientación: navegación estándar. No inventar clases Pydantic de «diagnóstico» ni lógica de recomendación.
- QA pendiente: maqueta real con copy D03 literal, render 320/375/390/768/1024/1440, teclado, foco, contraste, orden de lectura, textos CA/EN/DE y ausencia de desbordamiento.

### 33.7 Decisiones abiertas y estado

**Propuesta de diseño, no aprobación:** elegir tras comparación visual entre C02 tres tarjetas y tres filas editoriales; calibrar cuánto contraste necesita C03; verificar que C04 no parezca un procedimiento secuencial. El siguiente entregable es la **maqueta visual completa de Capacidades**, desktop/móvil, usando únicamente copy D03 y recursos aprobados. G1 pendiente y sin intervención productiva.

## 34. C04-CAP-02 — Maqueta visual completa de Capacidades V1 (03/11/2026) · PROPUESTA PARA VALIDACIÓN

**Precedencia y alcance:** Esta sección desarrolla la propuesta estratégica de §33 y sustituye su indecisión C02 para la maqueta V1, **sin constituir aprobación del promotor**. D03 V1.18 es la única fuente editorial: se han incorporado literalmente los textos de publicación C01–C05 (títulos, párrafos, ámbitos destacados, ejemplos, modalidades y CTA). No se modifica D03 ni el diseño aprobado de Inicio/INF/ENE/DIG. G1 pendiente.

### 34.1 Decisión de composición y motivación

| Bloque | Composición V1 | Razón UX/editorial | Responsive |
|---|---|---|---|
| C01 | Hero editorial compacto, H1 ancho controlado, antetítulo y ancla a C02; sin foto | Declarar que una necesidad puede abordarse desde una o varias especialidades | Columna única; sin ocultar introducción ni ancla |
| C02 | Tres **filas editoriales** numeradas, iguales en jerarquía, con subcolumnas descripción/ámbitos y enlace de especialidad | Los párrafos literales y cuatro ámbitos por área serían demasiado densos en tres tarjetas de escritorio | A una columna; cada ámbito queda bajo su propia descripción |
| C03 | Banda arena diferenciada; tres casos abiertos numerados con texto completo y enlaces contextuales discretos | Explicar combinaciones condicionales, no un diagrama de proceso ni un proyecto realizado | Casos apilados, enlaces bajo cada explicación |
| C04 | Cuatro modalidades en retícula 2×2 editorial, sin flechas ni timeline | Mostrar opciones independientes, no cuatro fases obligatorias | Una columna, mismo orden de lectura |
| C05 | Cierre verde pino, CTA principal y enlace a experiencia | Permitir contacto aunque no se conozca la especialidad | CTA y enlace apilables |

### 34.2 Identidad, recursos y contenido

- Tokens aplicados: pino `#0E2B25`, verde `#1A7A5A`, papel `#F7F5F0`, arena `#ECE8DD`, tinta `#2A2A2A`, separador `#D8D2C3`; tipografía `Inter` con fallback sistema.
- **No se añade ninguna fotografía.** Decisión editorial intencional: esta página orienta; no repite R23/R22/R21 ya presentes en Inicio ni usa fotos de terceros como evidencia de trabajos. Por tanto, **no cambia la matriz fotográfica C03**.
- Los tres ejemplos C03 son situaciones ilustrativas expresadas condicionalmente por D03, no casos ejecutados. Las etiquetas enlazadas son navegación contextual, no afirmación de que las tres disciplinas sean siempre necesarias.
- Logo BAFRAS de texto es **provisional**; sustituir por arte corporativo autorizado antes de G1. Las etiquetas pequeñas «C02 / ÁREAS DE INGENIERÍA», «C03 / INTEGRACIÓN», etc. son **señales de maqueta** y no copy D03 aprobado: eliminar/sustituir por metadatos de presentación antes de publicar.
- Los enlaces tienen rutas objetivo nominales para la futura web y no se consideran navegables en el paquete aislado.

### 34.3 Evidencias, QA y limitaciones

- Maqueta HTML: `C04_CAP_V1/capacidades.html` (autónoma, sin dependencias externas).
- Capturas completas: `C04_CAP_V1/capacidades_desktop.png` (1440), `capacidades_mobile.png` (390), `capacidades_tablet.png` (768), `capacidades_mobile_320.png` (320), `capacidades_desktop_1024.png` (1024).
- Renderizado real en Chromium mediante Playwright con contenido HTML cargado en memoria (la navegación `file://` está bloqueada por la política del entorno). Se comprobó `scrollWidth == clientWidth` en los cinco anchos citados. No se ha verificado 375 px, zoom 200 %, CA/DE, contraste automático, navegación completa por teclado, ni interacción entre páginas.
- El HTML contiene menú móvil demostrativo con `aria-expanded` y cierre por Escape; no equivale a validación funcional del sitio final.
- **Estado:** propuesta visual V1 pendiente de validación expresa; no implica G1 ni intervención productiva.


## 35. C04-CAP-03 — Acta de validación de Capacidades V1 y continuidad (03/11/2026) · APROBADA EN COMPOSICIÓN

**Decisión expresa del promotor:** «Me gusta, validamos y continuamos, actualiza documento 05». Se valida la maqueta **C04_CAP_V1** descrita en §34, con su jerarquía y composición de C01–C05. Esta aprobación **prevalece** sobre los estados «propuesta» o «pendiente de validación» que figuran en §33–§34 y sobre cualquier mención anterior de Capacidades como página sin diseño. Los textos de D03 V1.18 permanecen intactos y son la única fuente editorial.

### 35.1 Composición aprobada y límites

| Bloque | Decisión vigente | Estado |
|---|---|---|
| C01 | Hero editorial compacto, tipográfico, sin fotografía, con acceso a especialidades | Aprobado |
| C02 | Tres **filas editoriales** de igual jerarquía, numeradas, con descripción, cuatro ámbitos destacados por disciplina y enlace individual | Aprobado; reemplaza la alternativa de tres tarjetas de §33 |
| C03 | Fondo arena, tres situaciones de integración con textos D03 y enlaces contextuales; no implica secuencia ni intervención simultánea obligatoria | Aprobado |
| C04 | Cuatro modalidades independientes en retícula editorial 2×2 en escritorio, apiladas en móvil; sin flechas o cronología | Aprobado |
| C05 | Cierre verde pino con CTA de contacto y enlace a experiencia | Aprobado |
| Medios | Página deliberadamente sin fotografías; no reutilizar automáticamente R23/R22/R21 de Inicio | Aprobado |

### 35.2 Evidencia de referencia y condiciones pendientes

- Referencia de composición: `C04_CAP_V1/capacidades.html` y capturas `capacidades_desktop.png`, `capacidades_mobile.png`, `capacidades_tablet.png`, `capacidades_mobile_320.png`, `capacidades_desktop_1024.png` incluidas en `C04_CAP_V1_BAFRAS.zip`.
- Render y ausencia de desbordamiento horizontal comprobados en 320, 390, 768, 1024 y 1440 px durante la iteración §34. No se extiende esta afirmación a otros anchos o idiomas.
- **No publicar** las etiquetas de control de maqueta `C02 /`, `C03 /`, etc. ni mantener el logotipo tipográfico provisional. Sustituir por el logotipo oficial y respetar los textos D03 sin reescrituras.
- Pendiente de QA: 375 px, zoom 200 %, accesibilidad WCAG 2.2 AA, teclado, menú y rutas reales, traducciones, contrastes, estados y contenido final.
- **Aprobación de composición C04 ≠ aprobación de G1.** No autoriza intervención en código productivo.

### 35.3 Estado global y siguiente página

**Composición C04 validada:** Inicio V3; Infraestructuras V2; Sistemas energéticos V2; Automatización y control V1; **Capacidades V1**.

**Siguientes pendientes C04:** Sectores (SEC), Proyectos y experiencia (PE), Sobre BAFRAS (SB) y Contacto (CO). La siguiente página recomendada es **Sectores**, para completar la relación entre capacidades técnicas y contextos de aplicación, sin atribuir proyectos no verificados ni alterar la taxonomía de seis sectores de D03. Desarrollar propuesta y revisión visual antes de solicitar validación; no dar por aprobadas páginas aún no maquetadas.


---
## 36. C04-SEC-01 — Primera iteración Sectores y componente documental · 03/11/2026 · PROPUESTA
**Precedencia:** respeta las cinco páginas C04 ya aprobadas y los textos SEC-01–SEC-05 de D03 V1.18. Esta sección sustituye solo la antigua restricción visual «un enlace por tarjeta» para permitir el nuevo enlace de catálogo. **No supone aprobación del wireframe ni G1.**

### 36.1 Dictamen multidisciplinar
- **Dirección/comercial:** cada sector constituye una puerta de entrada de intención de compra. La descarga facilita explorar servicios sin barrera de formulario; el contacto sigue siendo CTA comercial independiente.
- **Ingeniería:** mantener lenguaje condicional de D03 y evitar que un PDF no revisado introduzca promesas, referencias o servicios no habilitados.
- **UX/arquitectura de información:** preservar seis sectores y orden; descripción + ejemplos + navegación a capacidad + descarga opcional. No crear página 10 ni un repositorio de documentos.
- **Diseño/marca:** priorizar lectura; sin seis fotos heterogéneas ni falsos proyectos; alternancia editorial y retícula sobria 2×3 escritorio, 1 columna móvil. Enlace PDF como acción secundaria de baja prominencia.
- **Software/QA:** presencia del CTA gobernada por manifiesto Pydantic validado; nunca botón deshabilitado o enlace ficticio en producción.

### 36.2 Estructura de wireframe SEC-01–SEC-05
| Bloque | Desktop | Móvil | Función |
|---|---|---|---|
| SEC-01 | Hero editorial sin fotografía; H1, texto, ancla a sectores y contacto | Columna única | Identificar contexto y doble vía de entrada |
| SEC-02 | Introducción y seis tarjetas editoriales en retícula 2×3; orden D03 por filas. Cada tarjeta incluye título, párrafo, ejemplos, enlace a capacidad y área reservable a catálogo **solo si existe** | Una columna, orden 1→6; acciones apiladas | Reconocer actividad, descubrir alcance y acceder a PDF sectorial |
| SEC-03 | Banda arena con H2, texto y enlace a Capacidades | Una columna | Atender problemas que cruzan sectores |
| SEC-04 | Banda editorial de colaboración con H2, texto y enlace Sobre BAFRAS | Una columna | Explicar colaboración con equipos de proyecto |
| SEC-05 | Cierre pino con H2, texto y CTA Contacto | Una columna | Conversión sin exigir catálogo ni sector |

### 36.3 `VIS-SEC-01` — Acción secundaria «Descargar catálogo de servicios»
- **Patrón:** reutilizar enlace secundario existente con icono discreto de documento/descarga; no crear botón primario nuevo. Texto exacto ES «Descargar catálogo de servicios». Metadato visible «PDF · [idioma real]». Si se expone el título completo, que pueda envolver sin truncamiento.
- **Disponible:** enlace activo con subrayado/indicador y foco visible, dentro de la tarjeta, tras el enlace contextual de capacidad o en un grupo de acciones claro.
- **Ausente:** no renderizar CTA ni contenedor vacío; evitar desigualdades grandes de altura mediante distribución natural, **sin reservar un hueco artificial**.
- **Idioma alternativo:** mostrar idioma real explícito; nunca «Español» si el documento es EN. Política de fallback editorial explícita, desactivada por defecto.
- **Hover/focus:** cambio de subrayado/color dentro de tokens aprobados, `:focus-visible` de contraste suficiente; no depender solo de icono o color. Área táctil objetivo ≥44×44 CSS px, wrapping, orden de tabulación natural.
- **No catálogo:** la tarjeta conserva su enlace a la especialidad y el contacto general SEC-05.
- **No botón deshabilitado, modal, formulario, tracking obligatorio ni JavaScript.**

### 36.4 Prototipo de estados y limitaciones
El wireframe conceptual puede simular los estados `disponible ES`, `ausente`, `solo EN` y `título largo` con **datos demostrativos claramente rotulados**; ningún PDF de demostración debe enlazarse ni publicarse como real. El HTML de maqueta no es implementación productiva. Los enlaces a capacidades son objetivos de navegación, no evidencia de que todas las rutas estén operativas.

### 36.5 Criterios de aceptación C04-SEC
1. Los seis sectores, su orden y copy coinciden literalmente con D03.
2. El CTA documental no sustituye navegación a capacidad ni contacto.
3. Se muestran los cuatro estados de catálogo en evidencia desktop/móvil.
4. Sin recurso, no existe botón ni hueco vacío significativo.
5. Idioma real visible y títulos largos sin truncamiento.
6. Teclado, foco, zoom, contraste, 320/390/768/1024/1440 y traducciones a validar antes de G1/G4.
7. `VIS-SEC-01` y `DownloadableResource` trazables a D03/D04; sin cambios en HTML para actualizar PDFs.

**Estado:** propuesta de primera iteración; pendiente de revisión visual y validación expresa del promotor. G1 permanece pendiente.


---
## 37. C04-SEC-02 — Segunda iteración visual de Sectores V2 · 03/11/2026 · PROPUESTA PARA VALIDAR

**Precedencia:** conserva los seis sectores y los textos literales SEC-01 a SEC-05 de D03 V1.19; conserva el contrato de publicación de catálogos D04 V2.1 y el componente `VIS-SEC-01` de §36. Esta iteración sustituye únicamente la composición visual V1 de §36 en los puntos indicados. No constituye aprobación ni G1.

### 37.1 Dictamen del equipo multidisciplinar
- **Comercial/CEO:** la identificación sectorial y el enlace a la especialidad siguen siendo la acción de orientación; el catálogo queda como profundización gratuita, y el contacto general se conserva en hero y cierre.
- **UX:** retícula 2×3 en escritorio, una columna en móvil, sin fotografías, sin filtros ni selector obligatorio. Los seis sectores son igualmente accesibles; los documentos ausentes no producen controles vacíos.
- **Diseño:** tarjetas de menor peso visual, acento verde superior y números discretos; jerarquía interna: título → explicación → ejemplos → enlace técnico → enlace documental opcional. Espaciado estable sin imponer alturas fijas artificiales. El enlace documental usa icono en contorno y metadatos de idioma.
- **Ingeniería/editorial:** ningún caso se presenta como referencia ejecutada; no se modifica el copy D03. Las cuatro variantes de catálogo son datos simulados, no documentos publicados.
- **Arquitectura/QA:** la maqueta no introduce backend ni lógica de publicación. El HTML final deberá usar `DownloadableResource` validado para decidir la presencia del enlace; nunca convertir los elementos de ejemplo en enlaces reales sin PDF autorizado.

### 37.2 Variantes y aceptación
- Con catálogo ES: mostrar «Descargar catálogo de servicios» y «PDF · Español».
- Sin catálogo: omitir por completo el enlace y metadatos, mantener enlace a capacidad.
- Solo catálogo EN: mostrar «PDF · English» únicamente cuando el fallback esté autorizado.
- Título largo: permitir múltiples líneas sin truncar ni desbordar; el título completo es opcional, no obligatorio.
- En prototipo, todos los ejemplos de descarga son **elementos no interactivos**; en producción deberán ser `<a>` con `href` a archivo validado y foco visible.
- No mostrar leyenda de estados, aviso de prototipo, numeración interna de wireframe ni logotipo tipográfico provisional en producción.

### 37.3 Evidencias de maqueta
- `C04_SEC_V2/sectores_v2.html` autónomo. Capturas completas `sectores_desktop.png` (1440), `sectores_tablet.png` (768), `sectores_mobile.png` (390), `sectores_mobile_320.png` (320).
- Chromium/Playwright: `document.documentElement.scrollWidth == clientWidth` a 320, 390, 768 y 1440 px. No se afirma QA integral WCAG ni prueba de PDFs reales.
- **Estado:** propuesta visual V2 pendiente de aprobación expresa de dirección. D03 V1.19 y D04 V2.1 se mantienen sin cambios en esta iteración, ya que el nuevo trabajo es puramente compositivo.


---
## 38. C04-SEC-03 — Selector de catálogos por actividad · Iteración V3 · 03/11/2026
**Estado:** propuesta visual pendiente de validación. **Precedencia:** amplía `VIS-SEC-01` de §36–37 solo para sectores con varios documentos; conserva las tarjetas V2 y los textos D03.

**VIS-SEC-02 — Lista desplegable de catálogos sectoriales.**
- 0 documentos: sin enlace ni desplegable; 1 documento: descarga directa VIS-SEC-01; 2 o más: `<details>` con `<summary>Catálogos de servicios</summary>` e icono discreto; debajo, lista de títulos de actividad y metadatos «PDF · idioma».
- El control cerrado no exhibe títulos largos; el abierto revela todos los documentos sin sobreponer contenido a otras tarjetas, desplazando la altura de la tarjeta de forma natural. No fijar altura ni crear scroll interno.
- En Industria se ilustran **dos líneas de catálogo en estado de ejemplo**: «Fabricación de muebles y madera» y «Lavanderías industriales». Son rótulos ilustrativos, no enlaces a archivos inexistentes.
- Accesibilidad: `<summary>` nativo operable con teclado, foco visible, nombres de enlaces distinguibles, objetivos táctiles de al menos 44 px cuando sea posible; sin hover obligatorio, sin JS. En producción, solo renderizar `<a href>` tras validación del PDF.
- Internacionalización: el texto del summary es localizable; cada PDF lleva idioma real. Si hay una sola variante publicada, no mostrar selector innecesario.
- Evidencia: `C04_SEC_V3/sectores_v3.html` con control funcional de abrir/cerrar y opciones **no descargables** por ser demo. Desktop/móvil pendientes de aprobación.
- **Criterio comercial:** el sector no se subdivide en nuevas páginas; el usuario encuentra una actividad y descarga su catálogo en un paso adicional.

---
## 39. C04-SEC-04 — Aprobación expresa de Sectores V3 · 03/11/2026

**Estado: APROBADO por dirección para composición visual y UX de la página Sectores.** Sustituye el estado «pendiente de validación» de §38 y, en lo referente a la solución visual vigente, prevalece sobre las propuestas de §36–37. Las especificaciones editoriales de D03 V1.20 y arquitectónicas de D04 V2.2 permanecen vigentes.

**Decisión aprobada:** mantener los seis sectores y su orden y copy; conservar la composición editorial de tarjetas V2; adoptar `VIS-SEC-01` para un único PDF publicado y `VIS-SEC-02` para dos o más catálogos publicados por sector. Industria puede incluir catálogos especializados por actividad, inicialmente ilustrados mediante «Fabricación de muebles y madera» y «Lavanderías industriales», sin crear nuevas páginas ni atribuir publicación real a estos ejemplos. Cero recursos publicados implica ausencia total del control. El selector nativo `<details>/<summary>` no requiere JavaScript y debe presentar idioma real de cada documento.

**Condiciones de producción:** los PDF ilustrativos de la maqueta son ejemplos no descargables. Antes de publicar, enlazar exclusivamente recursos existentes, autorizados y validados mediante Pydantic v2 y el generador estático; no editar HTML para cambiar documentos. Retirar etiquetas y avisos internos de prototipo, sustituir logotipo provisional, comprobar navegación, teclado, foco, contrastes, traducciones y responsive. La aprobación visual no supone G1 ni autorización para refactorizar código productivo.

**Siguiente página C04:** Proyectos y experiencia. Mantener la distinción explícita entre proyectos de BAFRAS y experiencia profesional anterior de fundadores, y las verificaciones de atribución y permiso.


---
## 40. C04-PE-01 — Proyectos y experiencia · Maqueta índice V1 y ficha modular V1 · 03/11/2026

**Estado: PROPUESTA PARA VALIDACIÓN.** Se conserva la aprobación editorial de la arquitectura PE-01 a PE-04 de D03 V1.20. Las seis referencias y sus textos permanecen provisionales, no acreditados ni publicables. Esta iteración no modifica D03 ni D04, no autoriza publicación y no completa G1.

### 40.1 Decisión narrativa y UX
- PE-01 hero tipográfico con H1, introducción y nota de atribución de D03.
- PE-02 tres agrupaciones visibles con anclas: Infraestructuras e instalaciones, Automatización y control, Sistemas energéticos. Seis referencias candidatas en orden D03; tres destacadas con más espacio editorial y tres complementarias compactas. La categoría con una referencia ocupa ancho disponible sin huecos artificiales.
- Tarjetas con etiqueta de **experiencia profesional previa del equipo**, identificada como **pendiente de acreditación** en maqueta. Ninguna tarjeta enlaza a ficha real. Los textos de referencia se mantienen literalmente conforme a D03, pero son borradores, no afirmaciones verificadas.
- PE-03 banda arena con copy literal «La intervención concreta importa.» y párrafo D03.
- PE-04 cierre verde pino, CTA Contacto y enlace secundario Capacidades, copy literal D03.
- Sin fotografía genérica atribuida a un proyecto. Reservas visuales abstractas y expresamente identificadas como material pendiente. Sin filtros, buscador ni proyectos inventados.

### 40.2 VIS-PE-01 — Tarjeta de referencia
Campos: especialidad, título, texto breve, clasificación de procedencia, y, si constan, rol, fase y etiquetas técnicas verificadas. Variante destacada / complementaria. Solo mostrar «Ver proyecto» cuando ficha, atribución, autorización y ruta publicada estén validadas. Si falta cualquiera, tarjeta sin enlace. No simular datos para rellenar módulos.

### 40.3 VIS-PE-02 — Ficha técnica modular
Plantilla independiente y preparada para ruta localizada de proyecto futuro, conforme a D04 `Experience` y, cuando proceda, `StudyPublication`:
1. Identificación, atribución y resumen verificable (obligatorios).
2. Contexto y reto técnico (obligatorio).
3. Sistemas e interfaces realmente abordados (según evidencia).
4. Intervención, rol y límites de responsabilidad (obligatorio).
5. Entregables y material gráfico (opcional, sujeto a derechos).
6. Resultados medidos o documentados (opcional; con unidades, fuente y límites).
7. Estudio técnico e informe descargable (opcional, paquete de publicación validado).
8. Contacto y capacidad relacionada.

Los módulos opcionales se omiten si no hay datos, sin dejar tarjetas vacías. Las etiquetas entre corchetes del prototipo son **campos de plantilla**, nunca texto publicable. Una ficha de trayectoria previa no debe atribuir el proyecto a BAFRAS.

### 40.4 Responsive y evidencias
- Índice: escritorio 1440 px, tablet 768 px, móvil 390 px y 320 px. Agrupación en 2 columnas cuando cabe; una columna en móvil, preservando el orden editorial.
- Ficha: bloques de contenido + metadatos en escritorio; lectura vertical continua en móvil. Sin barra lateral fija ni tablas anchas.
- Capturas `C04_PE_V1/proyectos-experiencia_{desktop,tablet,mobile,mobile_320}.png` y `plantilla-ficha-proyecto_{desktop,tablet,mobile,mobile_320}.png`.
- Verificación Playwright/Chromium mediante `set_content`: `scrollWidth == clientWidth` en 320/390/768/1440 para ambas páginas. **No se afirma auditoría WCAG integral ni pruebas de enlaces/rutas desplegadas.**
- Prototipos: `proyectos-experiencia.html` y `plantilla-ficha-proyecto.html`; logotipo tipográfico y avisos internos provisionales. El prototipo de ficha no representa un proyecto real.

### 40.5 Criterios de aceptación antes de aprobar
- Validar jerarquía de tres destacadas y tres complementarias, y legibilidad del copy literal.
- Validar que los avisos internos se retiran en producción y que ninguna referencia no acreditada aparece en una web pública.
- Confirmar que la ficha modular permite proyectos BAFRAS y experiencia previa con atribuciones inequívocas.
- Comprobar navegación real, contraste, foco, teclado, imágenes autorizadas, localización y SEO en implementación posterior.
- Publicación de cada referencia condicionada a ficha individual, rol, entidad contratante cuando corresponda, derechos de imagen/nombre, datos y revisión de dirección.

---

## §41 — Acta de aprobación C04-PE-V1 (03/11/2026)

**Decisión de dirección:** aprobada la primera versión visual de «Proyectos y experiencia» y la plantilla modular de ficha individual, según confirmación expresa del usuario. La propuesta §40 queda consolidada como composición vigente; no constituye autorización de publicación de referencias no acreditadas ni de intervención en código productivo.

### 41.1 Elementos aprobados
- Índice PE-01 a PE-04 con contenido editorial D03, agrupación en tres especialidades y jerarquía de tres referencias destacadas y tres complementarias, condicionadas a verificación.
- Etiquetado inequívoco de experiencia profesional previa frente a proyectos contratados por BAFRAS.
- Componente VIS-PE-01 con variantes destacada y complementaria, sin enlace a ficha no publicada.
- Componente VIS-PE-02: ficha técnica individual modular, con núcleo obligatorio y módulos opcionales de fotografías, documentación, resultados y estudios técnicos; sin contenidos ficticios presentados como reales.
- Diseño responsive de escritorio y móvil según evidencias descritas en §40.

### 41.2 Condiciones que permanecen abiertas
- Verificar participación, alcance, atribución, permisos y material de cada referencia antes de publicarla; las seis referencias siguen siendo candidatas, no proyectos aprobados para difusión.
- Sustituir marcas y textos de prototipado, comprobar accesibilidad integral, enlaces, localización y SEO en fases posteriores.
- Las fichas individuales se publicarán solo con información y evidencias validadas. No se autoriza crear fichas de proyectos ficticios.
- D03 y D04 no se modifican por esta aprobación visual. **Gate G1 sigue pendiente** hasta completar y aprobar las nueve páginas y demás criterios de D04.

**Estado C04:** siete de nueve páginas con composición visual aprobada: Inicio, Capacidades, Infraestructuras, Sistemas energéticos, Automatización y control, Sectores, Proyectos y experiencia. Pendientes: Sobre BAFRAS y Contacto.


---

## §42 — C04-SB · Sobre BAFRAS — estrategia y wireframe conceptual V1 (03/11/2026)

**Estado:** propuesta de diseño pendiente de validación; no altera D03 ni aprueba G1. Se mantiene §41 y todas las decisiones anteriores.

### 42.1 Objetivo narrativo
Humanizar la marca, demostrar complementariedad verificable de tres fundadores y explicar cómo se delimita una intervención. No duplicar las páginas Capacidades ni Proyectos y experiencia; no construir tres currículos extensos.

### 42.2 Correspondencia literal con D03
- SB-01: hero tipográfico con H1 «Ingeniería con visión técnica y disciplinas complementarias.», párrafo íntegro y enlace contextual a experiencia.
- SB-02: H2 «Profesionales con experiencias que se complementan.», párrafo íntegro, presentación corporativa aprobada de dos ingenieros industriales y un ingeniero técnico electrónico y tres fichas equivalentes.
- SB-03: H2 «Primero entender. Después definir la actuación.», párrafos y cuatro principios literales de D03; evitar flechas que sugieran obligatoriedad; mostrar nota «No todas estas etapas forman parte de todos los contratos.»
- SB-04: H2 «Experiencia profesional aplicada a proyectos reales.», párrafos íntegros y enlace a Proyectos y experiencia; no reproducir referencias no verificadas.
- SB-05: H2 «Hablemos de tu proyecto.», párrafo íntegro, CTA principal Contacto y secundario Capacidades.

### 42.3 Contrato visual de fundador (VIS-SB-01, propuesto)
Tres fichas de igual jerarquía, sin ranking. Campos visibles: nombre público confirmado, titulación exacta verificada, especialidad editorial, resumen de experiencia de máximo dos líneas comprobadas y enlace a referencias relacionadas solo si existen fichas publicadas. Retrato real con autorización o alternativa tipográfica sin fotografía; nunca retrato sintético. No incluir cargos, años, habilitaciones, certificaciones, clientes, métricas o proyectos no contrastados. Orden de trabajo según D03: Murti (energía), Àngel (infraestructuras), Amin (automatización). El orden no implica jerarquía empresarial.

### 42.4 Composición recomendada
- Hero SB-01: papel, composición tipográfica amplia, sin fotografía genérica.
- Equipo SB-02: sección protagonista, fondo papel o arena, introducción y tres retratos/fichas en tres columnas en escritorio, apiladas en móvil; preferir retratos coherentes en encuadre e iluminación.
- Método SB-03: cuatro principios en cuadrícula 2×2 escritorio, lista vertical móvil; numeración solo como índice de lectura, no proceso contractual obligatorio.
- Experiencia SB-04: banda editorial con enlace a referencias; colaboración con otros agentes sin logos ni nombres no autorizados.
- Cierre SB-05: verde pino corporativo y CTA destacado.

### 42.5 Estados y accesibilidad
Con tres fotos, fotos parciales y ninguna foto: conservar proporciones y equidad; preferir solución tipográfica uniforme si faltan varias fotografías, sin iconos que simulen retratos. Enlace a experiencia oculto por ficha si no hay referencia publicable. Tarjetas sin interacción ficticia. Contraste y foco visible, alt de retratos con nombre, diseño 320–1440 px sin scroll horizontal, lectura semántica consistente. En móvil nombre y especialidad visibles antes de detalles secundarios.

### 42.6 Verificación previa a publicación
Confirmar nombres completos públicos, grafías, títulos, biografías, permisos fotográficos, alcance y atribución de experiencias; distinguir trayectoria previa de encargos BAFRAS. La siguiente iteración C04-SB-V1 debe renderizar escritorio/móvil con copy literal de D03 y variantes con/sin retratos. G1 sigue pendiente.


---

## §43 — C04-SB-V1 · Maqueta visual Sobre BAFRAS (03/11/2026)

**Estado:** estrategia §42 aprobada expresamente por dirección; primera maqueta visual entregada para revisión, aún no aprobada. No modifica D03 ni D04.

### 43.1 Composición entregada
- SB-01 hero tipográfico en papel con H1 y párrafo literal D03, enlace a experiencia.
- SB-02 equipo sobre arena, tres fichas equivalentes Murti, Àngel y Amin; especializaciones propuestas de D03, sin títulos completos ni trayectorias inventadas. Ausencia deliberada de fotografías sintéticas y enlaces a referencias no publicadas.
- SB-03 cuatro principios literales en retícula 2×2, nota de alcance contractual.
- SB-04 banda editorial arena con experiencia y colaboración, sin referencias no verificadas.
- SB-05 cierre pino con CTA principal Contacto y secundario Capacidades.

### 43.2 Evidencias y condiciones
- Prototipo `C04_SB_V1/sobre-bafras.html`; captura de escritorio disponible; capturas restantes pendientes.
- No se ha completado QA responsive automatizada; queda pendiente antes de aprobar.
- Antes de publicar: confirmar nombre completo, grafía, titulación académica exacta, trayectoria contrastada, fotografías autorizadas, atribuciones, referencias y traducciones. Retirar banda de maqueta y notas internas.
- G1 sigue pendiente: falta aprobar Sobre BAFRAS visualmente y desarrollar/validar Contacto, además de criterios globales D04.


---

## §44 — Aprobación C04-SB-V1 · Sobre BAFRAS (03/11/2026)

**Estado:** dirección aprueba expresamente la composición visual V1 de Sobre BAFRAS y ratifica la estrategia §42. La aprobación de diseño sustituye el estado «pendiente de aprobación» indicado en §43, pero **no** acredita la publicación ni la finalización del QA responsive.

### 44.1 Elementos aprobados
- Estructura editorial SB-01 a SB-05 y contenido gobernado por D03.
- Hero tipográfico, tres fichas de fundadores de idéntica jerarquía, filosofía de trabajo 2×2, bloque de experiencia y cierre comercial.
- Diferenciación de especializaciones Murti / Àngel / Amin, sin atribuciones ni méritos no contrastados.
- Estética corporativa y solución sin retratos sintéticos mientras no haya fotografías reales autorizadas.

### 44.2 Pendientes que no bloquean la aprobación de la composición
- Validar y completar datos profesionales de los fundadores y permisos de imagen antes de publicación.
- Comprobar y documentar variantes responsive (tablet, 390 px y 320 px), accesibilidad y ausencia de desbordamientos; la captura de escritorio no demuestra por sí sola el QA responsive.
- Verificar enlaces, contenido y traducciones definitivos conforme a D03 y D04.

### 44.3 Estado de G1
**8 de 9 páginas con diseño aprobado**: Inicio, Capacidades, INF, ENE, DIG, Sectores, Proyectos y experiencia, Sobre BAFRAS. Queda **Contacto**, más verificaciones transversales y entregables de G1. No iniciar implementación productiva por esta aprobación aislada.


---
## §45 — C04-CO-V1 · Contacto · propuesta visual pendiente de validación (03/11/2026)

- **Fuente editorial:** Documento 03 V1.20, bloques CO-01 a CO-04 y decisión 03.K.2. No alterar copy aprobado.
- **Composición:** hero claro en dos columnas; bloque arena con formulario principal en papel y columna secundaria de correo directo; cierre editorial claro; footer pino. En móvil hero, formulario, correo, cierre.
- **Formulario:** nombre, organización opcional, correo, consulta; tres campos obligatorios. Sin teléfono, presupuesto, sector, adjuntos ni plazos obligatorios. CTA único «Enviar consulta».
- **Prototipo seguro:** formulario visualmente desactivado; sin captura de datos ni falso éxito. Se habilitará únicamente con endpoint seguro, validación cliente/servidor, antispam, límites, correo entregable, textos legales reales y pruebas E2E.
- **Correo:** info@bafras.com, enlazado con mailto, sujeto a verificación operativa.
- **Privacidad:** texto de demostración explícito; no enlazar a política ficticia ni presuponer persona jurídica constituida.
- **Estado:** maqueta V1 para revisión; no aprobada; G1 pendiente.


## §46 — Contacto C04-CO-V2 · teléfono de contacto incorporado (03/11/2026)

A petición del fundador, se incorpora el número **+34 610 903 179** a la sección de contacto directo y al pie de página. El enlace funcional utiliza `tel:+34610903179`. Se mantiene `info@bafras.com`, el formulario desactivado hasta disponer de servicio de envío y política de privacidad, y el diseño editorial aprobado como propuesta. La publicación del número se entiende autorizada por la indicación expresa del usuario, sin atribuirle titularidad corporativa distinta de la indicada. C04-CO-V2 sigue pendiente de aprobación visual y revisión responsive.


---
## §47 — Aprobación formal C04-CO-V2 · Contacto (03/11/2026)
**Estado:** dirección valida expresamente la página Contacto V2, incluida la incorporación del teléfono **+34 610 903 179**. Esta decisión sustituye el estado «pendiente de aprobación visual» de §§45–46, sin alterar sus especificaciones técnicas ni editoriales.

### 47.1 Composición aprobada
- CO-01: cabecera/hero editorial claro y texto gobernado por D03.
- CO-02: formulario principal con nombre, organización opcional, correo y consulta; presentación desactivada mientras no exista servicio operativo y cobertura legal.
- CO-03: columna de contacto directo con `info@bafras.com` y `+34 610 903 179`, enlaces `mailto:` y `tel:` respectivamente, jerarquía visual equivalente y legibilidad móvil.
- CO-04: cierre contextual; pie corporativo con ambos datos de contacto.
- Se mantiene la paleta y el sistema de espaciado/tipografía aprobados; no se añaden WhatsApp, dirección física o promesas de respuesta.

### 47.2 Alcance y condiciones pendientes
- La validación del diseño **no acredita** la comprobación visual responsive en todas las resoluciones, accesibilidad, funcionalidad del formulario, recepción real de correo, información legal, traducciones ni despliegue.
- Verificar prototipo C04-CO-V2 en escritorio, tablet, móvil 390 px y móvil estrecho 320 px, con pruebas de foco, enlaces y desbordamiento.
- Confirmar antes del lanzamiento que el correo y el número publicados son canales atendidos y que la identidad del responsable del tratamiento y la política de privacidad son reales.

### 47.3 Estado global
**9 de 9 páginas con composición visual aprobada:** Inicio, Capacidades, INF, ENE, DIG, Sectores, Proyectos y experiencia, Sobre BAFRAS y Contacto.
**Gate G1:** pendiente de auditoría transversal, comprobaciones responsive/accesibilidad, consistencia de componentes y evidencias de aceptación; no declarar G1 cerrado ni iniciar desarrollo productivo por el mero hecho de aprobar la novena maqueta.

---
## §48 — Línea base visual para traspaso G1 (03/11/2026)
**Estado:** nueve composiciones individuales aprobadas; esta adenda congela la referencia de diseño para implementación, sin declarar superadas pruebas no ejecutadas.

**Versiones de referencia:** Inicio V3; Capacidades V1; Infraestructuras e instalaciones V2; Sistemas energéticos V2; Automatización y control V1; Sectores V3; Proyectos y experiencia V1; Sobre BAFRAS V1; Contacto V2.

**Componentes:** utilizar el catálogo AUD-G1-02 como especificación de 13 familias, sujeto a aceptación expresa en el acta G1; unificar cabecera, navegación de seis entradas, pie, CTA, tarjetas, estados de catálogos y formulario durante G2/G3. No copiar la cabecera duplicada de los prototipos integrados de ensayo.

**QA posterior obligatorio:** comprobar en navegador real escritorio/móvil, menú y foco, 320/390/768/1440 px (más 375 y 1024 px y zoom 200 %, §12.5), desbordamiento, accesibilidad y fidelidad editorial. La auditoría AUD-G1-03 registró 0/36 verificaciones responsive certificadas y 78 fragmentos editoriales por clasificar, no 78 errores confirmados.

**Gobernanza:** no reabrir estética aprobada por preferencias subjetivas; documentar excepciones si una implementación descubre defectos concretos. El cierre formal del gate requiere ratificación expresa de dirección, separada de las nueve aprobaciones individuales.
