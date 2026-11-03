# BAFRAS ENGINEERING — DOCUMENTO MAESTRO 03 DEFINITIVO
## Especificación editorial y contenido web en español · Consolidación de estados 2026-11-03 · Versión vigente V1.22 (línea base G1) + adenda 03.G1-02

**Estado:** Base editorial cerrada por aprobación del promotor. Son definitivos los textos aprobados de Inicio, Capacidades, sus tres especialidades, Sectores, Sobre BAFRAS y Contacto. La **estructura** de «Proyectos y experiencia» está aprobada, pero las descripciones de referencias son **borradores sujetos a fichas y autorización**; no deben mostrarse como hechos comprobados. Las traducciones ES→CA/EN/DE aún no están aprobadas.

### Decisiones vinculantes que prevalecen sobre marcadores históricos
- Equipo: **Murti — ingeniero industrial; Àngel — ingeniero industrial; Amin — ingeniero técnico electrónico**. Las especialidades de cada ficha se confirmarán con sus titulares antes de publicar.
- Contacto público y destino del formulario: **info@bafras.com**. Sustituye todos los marcadores históricos «correo pendiente».
- BAFRAS gestiona operativamente las consultas. El titular jurídico y la identificación completa para aviso legal y privacidad se consignarán cuando estén confirmados; la etiqueta comercial no sustituye la identificación jurídica.
- Formulario: nombre obligatorio; empresa opcional; email obligatorio; mensaje obligatorio; envío seguro al correo corporativo; sin CRM ni base de datos adicional en V1; confirmación solo después de aceptación real del servicio de envío; errores recuperables.
- Los trabajos previos de los fundadores **no** se presentarán como encargos de BAFRAS. Ningún resultado, responsabilidad, imagen, nombre de cliente o tecnología de una referencia pendiente se publicará sin respaldo.
- Los servicios publicados respetarán el alcance y estado de la taxonomía del Documento 01. No se ofrece IA/ML como línea actual, auditoría/certificación de ciberseguridad OT ni soporte 24/7 por defecto.


### Registro vigente de coordinación editorial–visual (03/11/2026)

**Ámbito y precedencia.** Este documento 03 es la autoridad exclusiva del **contenido editorial**: títulos, párrafos, etiquetas, enlaces previstos, orden y bloques H01–H07 / INF-01–INF-07 / ENE / DIG. El Documento 05 es la autoridad exclusiva de **composición, selección de imágenes, estilos y responsive**. Documento 04 rige implementación y pruebas; Documento 01 rige catálogo y habilitación de publicación. Ninguna decisión de diseño modifica el copy sin aprobación editorial explícita.

| Materia | Estado vigente | Documento rector |
|---|---|---|
| Inicio H01–H07 | **Copy aprobado**; composición C04 Inicio V3 **validada por el promotor** | D03 para texto; D05 §23/§26 para diseño |
| H01, fotografía | **R24 aprobada**; no interpretar la antigua alternativa genérica «fotografía o composición» como selección abierta | D05 §18/§26 |
| H02, imágenes de las tres capacidades | **R23 / R22 / R21** mantenidas como selección de la maqueta validada | D05 §23/§26 |
| H03, imagen de apoyo | **R03 aprobada**; imagen contextual, no proyecto propio | D05 §23/§26 |
| Infraestructuras INF-01–INF-07 | **Copy aprobado**; composición **C04-INF-V2 validada expresamente por el promotor** | D03 para texto; D05 §25/§26 para diseño |
| INF-01, fotografía | **R18** ratificada con la validación de INF-V2 | D05 §25/§26 |
| Sistemas energéticos / Automatización | Copy aprobado; diseño específico **pendiente de C04-ENE/C04-DIG**. R10/R01 son selecciones de partida, no aprobación de sus maquetas | D03 y D05 §26 |
| Proyectos y experiencia | Arquitectura aprobada; referencias provisionales **no publicables** sin evidencia y autorización | D03 |
| Publicación / G1 | **No aprobados**. La validación compositiva no acredita QA, traducciones, licencias concretas ni habilitación de servicios | D04 y D05 |

**Control de antecedentes:** expresiones como «pendiente de aprobación editorial» en encabezados de iteraciones históricas INF/ENE/SEC, «selección visual pendiente» en notas antiguas de INF, «correo pendiente» en el bloque histórico CO-03 y la opción fotográfica abierta en H01 son **fotografías del estado anterior**, no instrucciones vigentes. No eliminamos el histórico ni alteramos el texto público aprobado. En Contacto prevalece `info@bafras.com`, sujeto a prueba operativa. Los componentes no deben extraer al HTML anotaciones históricas, corchetes ni notas de auditoría.

**Nota de control documental WEB-G1-REVIEW-01 (03/11/2026, no modifica copy ni decisiones):** (1) La fila «Sistemas energéticos / Automatización» de la tabla anterior refleja el estado previo a las aprobaciones de composición C04-ENE-V2 y C04-DIG-V1 (D05 §29 y §31); el estado vigente del diseño de las nueve páginas es el de la adenda 03.G1-01 y D05 §47.3/§48. La fila «Publicación / G1» sigue vigente. (2) El «inventario de bloques y estados del Documento 04» citado en la regla de lectura siguiente no existe todavía como tal en D04 V2.4; hasta que G2 lo formalice, usar `WEB_G1_REVIEW_01_TRAZABILIDAD.md` como matriz de trabajo no vinculante. (3) La propuesta de arquitectura de 03.J §7 (evaluación de Astro/SSG y nombres de modelos) es antecedente: rige D04 V2.4, conforme al ámbito fijado en este registro. (4) Las divergencias internas de copy detectadas (Contacto CO-01/CO-02/CO-03, etiquetas de atribución, ficha de equipo) se registran para decisión editorial en `WEB_G1_REVIEW_01_INCIDENCIAS.csv`; no se han resuelto en este documento.

### Regla de lectura y extracción
La **Parte editorial** del documento histórico se conserva a continuación, sin reescrituras de copy. Las notas de auditoría y propuestas de implementación incluidas en ese historial son **antecedentes internos**, no texto visible de la web. En caso de contradicción entre un marcador histórico y las decisiones vinculantes anteriores, prevalecen estas últimas. Para desarrollo usar el inventario de bloques y estados del Documento 04, no publicar el Markdown maestro sin filtrar.

---
# BAFRAS Engineering — Documento Maestro 03 · Consolidación editorial v1.17

**Estado vigente (2026-11-02):** Aprobadas editorialmente: Inicio, Capacidades, Infraestructuras e instalaciones, Sistemas energéticos, Automatización y control, Sectores, Sobre BAFRAS y Contacto. «Proyectos y experiencia» V1.1: arquitectura aprobada; textos de referencias provisionales, sin habilitación de publicación hasta verificar proyectos, funciones, autorizaciones y evidencias. Decisiones concretas de publicación y contenido 03.K incorporadas; auditoría transversal 03.J completada: se documentan incidencias y criterios de aceptación; no implica implementación ni aprobación de traducciones.

## PARTE A — HOMEPAGE APROBADA (texto conservado)

# BAFRAS Engineering — Documento Maestro 03
## Iteración 03.B.4 — Homepage: contenido editorial aprobado
Fecha: 2026-11-02 · Estado: H01–H07 aprobadas editorialmente por el usuario; diseño visual y publicación pendientes.

### Decisiones aprobadas de arquitectura
Inicio; Capacidades (Infraestructuras e instalaciones, Sistemas energéticos, Automatización y control); Sectores; Proyectos y experiencia; Sobre BAFRAS; Contacto. Conocimiento fuera del lanzamiento. Hero equilibrado. La denominación «Automatización y control» es la etiqueta pública de la tercera capacidad; los servicios específicos siguen definidos en Documento 01.

### Principio editorial
Necesidad real → estudio y criterio → actuación/entregable → valor condicionado. No atribuir a BAFRAS experiencia previa de los fundadores. No prometer ahorros o resultados garantizados. Documento 01 es fuente de servicios y límites; Documento 02 de posicionamiento, mensajes y evidencias.

## H01 · Hero — opción A aprobada
**Eyebrow:** BAFRAS ENGINEERING · INGENIERÍA MULTIDISCIPLINAR
**H1:** Ingeniería para instalaciones, energía y automatización.
**Subtítulo destacado:** Comprender cada reto. Desarrollar la solución adecuada.
**Texto:** Analizamos necesidades, evaluamos alternativas y desarrollamos soluciones de ingeniería adaptadas a cada proyecto. Integramos distintas especialidades cuando el reto lo requiere.
**CTA principal:** Cuéntanos tu proyecto → Contacto.
**CTA secundario:** Explorar capacidades → Capacidades.
**Visual:** fotografía técnica real con derechos verificados, o composición de sistemas vinculada a las capacidades; no utilizar afirmaciones visuales engañosas.
**Estado:** opción A validada expresamente por el usuario el 02/11/2026. Alternativas B y C descartadas. La aprobación es editorial y no supone aprobación del diseño gráfico o publicación.

## H02 · Capacidades
**H2:** Tres áreas de ingeniería. Un criterio común.
**Introducción:** Trabajamos en instalaciones e infraestructuras, sistemas energéticos y automatización y control. Cada especialidad puede responder a una necesidad concreta o integrarse con las demás cuando el proyecto lo requiere.

**Tarjeta 1 — Infraestructuras e instalaciones**
Diseño, análisis y asistencia técnica para instalaciones eléctricas, mecánicas y sistemas auxiliares en edificios e infraestructuras.
**Ejemplos:** instalaciones eléctricas; climatización y ventilación; coordinación y supervisión técnica.
**Enlace:** Ver infraestructuras e instalaciones → capacidad INF.

**Tarjeta 2 — Sistemas energéticos**
Estudios y proyectos para comprender la demanda, evaluar alternativas y desarrollar sistemas de generación, almacenamiento y gestión de energía.
**Ejemplos:** análisis energético; instalaciones renovables; almacenamiento e integración energética.
**Enlace:** Ver sistemas energéticos → capacidad ENE.

**Tarjeta 3 — Automatización y control**
Ingeniería de instrumentación, supervisión y control para mejorar la operación y la información disponible sobre instalaciones y procesos.
**Ejemplos:** automatización de instalaciones; sistemas de supervisión; integración de datos y equipos.
**Enlace:** Ver automatización y control → capacidad DIG.

**Enlace complementario:** Todas nuestras capacidades → índice Capacidades.

## H03 · Necesidades
**H2:** Partimos de lo que necesita tu instalación o proyecto.
**Introducción:** No todos los encargos requieren una solución nueva. A veces el primer paso es entender cómo funciona un sistema, identificar sus limitaciones o comparar opciones antes de invertir.

**Situación 1 — Una instalación que no funciona como debería.**
Analizamos el funcionamiento y los condicionantes para identificar posibles causas y definir actuaciones justificadas.
**Enlace:** Infraestructuras e instalaciones.

**Situación 2 — Una decisión energética que necesita fundamento.**
Estudiamos consumos, necesidades y alternativas técnicas antes de definir una inversión o una modificación del sistema.
**Enlace:** Sistemas energéticos.

**Situación 3 — Equipos y datos que no trabajan de forma coordinada.**
Evaluamos necesidades de instrumentación, comunicación, supervisión y control para plantear una integración proporcionada.
**Enlace:** Automatización y control.

**Situación 4 — Un proyecto que requiere varias especialidades.**
Definimos interfaces y responsabilidades técnicas para coordinar las disciplinas que intervienen.
**Enlace:** Capacidades.

## H04 · Filosofía y forma de trabajar (fusión de integración y metodología)
**H2:** Primero comprender. Después decidir cómo intervenir.
**Texto:** Una solución de ingeniería debe responder al problema, al contexto de uso y a los condicionantes del proyecto. Por eso definimos el alcance, contrastamos alternativas y concretamos los criterios de diseño y comprobación que correspondan a cada encargo.

**Paso 1 — Comprender:** necesidades, funcionamiento y restricciones.
**Paso 2 — Evaluar:** causas, opciones y sus implicaciones técnicas y económicas cuando proceda.
**Paso 3 — Desarrollar:** estudios, proyectos, integración o asistencia técnica según el alcance contratado.
**Paso 4 — Verificar:** criterios de comprobación y documentación de los resultados que correspondan al trabajo.

**Cierre:** No todas las actuaciones requieren las tres especialidades ni todas las fases: el alcance se define para cada proyecto.
**Enlace:** Conoce nuestra forma de trabajar → Sobre BAFRAS.

## H05 · Sectores
**H2:** Ingeniería aplicada a distintos entornos.
**Texto:** Las necesidades cambian según el uso del edificio, la continuidad operativa, los equipos y las exigencias del proyecto. Adaptamos el análisis y el alcance técnico a cada contexto.
**Grupos de portada propuestos (etiquetas a contrastar con taxonomía sectorial):**
- Hoteles y alojamientos turísticos.
- Industria y procesos.
- Edificios terciarios y comerciales.
- Equipamientos e instalaciones públicas.
**Enlace único:** Explorar sectores → Sectores.
**Nota:** los cuatro grupos son una selección editorial de portada, no una taxonomía nueva ni exclusión de otros sectores.

## H06 · Proyectos y experiencia
**H2:** Experiencia técnica que respalda nuestro trabajo.
**Texto:** BAFRAS reúne profesionales con experiencia en proyectos de instalaciones, energía y sistemas técnicos. Presentamos las referencias indicando el trabajo realizado, la responsabilidad asumida y si corresponde a una trayectoria profesional previa o a un encargo propio de BAFRAS.
**Enlace:** Conocer proyectos y experiencia → Proyectos y experiencia.
**Regla de publicación:** NO mostrar tarjetas, clientes, logos, imágenes, cifras ni nombres de proyectos hasta verificar evidencias, roles y permisos. Si no hay referencias autorizadas, mantener solo el bloque textual anterior o fusionarlo con H07, sin simular portfolio.

## H07 · Cierre y contacto
**H2:** ¿Tienes un proyecto o una necesidad técnica que estudiar?
**Texto:** Cuéntanos qué necesitas, en qué fase se encuentra el proyecto y qué cuestiones quieres resolver. Valoraremos cómo podemos ayudarte y qué información hace falta para definir el siguiente paso.
**CTA:** Hablemos de tu proyecto → Contacto.
**Microcopy:** También colaboramos con otras ingenierías, instaladores y equipos técnicos.

## Cabecera y pie
**Menú:** Capacidades (índice y tres subpáginas), Sectores, Proyectos y experiencia, Sobre BAFRAS, Contacto; logo → Inicio; selector ES/CA/EN/DE solo para idiomas efectivamente publicados.
**Footer:** identidad y contacto verificables, navegación secundaria, aviso legal y privacidad según requisitos aplicables; no publicar datos o políticas ficticios.

## Recorridos comprobables
1. Cliente con problema HVAC: Inicio → necesidad «instalación» → Infraestructuras e instalaciones → Contacto.
2. Responsable de energía: Inicio → tarjeta Sistemas energéticos → página ENE → Proyectos y experiencia → Contacto.
3. Ingeniería colaboradora: Inicio → Capacidades → especialidad → Sobre BAFRAS → Contacto.
4. Dirección de hotel: Inicio → Sectores → capacidad relevante → Contacto.
5. Visitante que necesita confianza: Inicio → Proyectos y experiencia → ficha autorizada → Contacto.
6. Visitante preparado para contratar: Inicio → CTA hero → Contacto.

## Criterios de revisión de esta iteración
**Propuesta para aprobar:** textos H01–H07, orden, CTA y enlaces. **Bloqueos antes de publicación:** permisos y atribuciones de referencias, imágenes, datos legales, revisión técnica final, cuatro idiomas, enlaces reales y formulario verificado. Los nombres de grupos sectoriales son una selección de portada pendiente de cotejo con el inventario canónico. No se ha implementado ni probado la página.


## PARTE B — CAPACIDADES (propuesta final auditada)

# BAFRAS Engineering — Documento Maestro 03
## Página «Capacidades» · Contenido editorial final ES · v1.1
Fecha: 2026-11-02
Estado: versión consolidada tras auditoría multidisciplinar; pendiente de validación expresa del usuario para considerarla aprobada. La homepage H01–H07 permanece aprobada y sin cambios.

## Función y navegación
Página índice para orientar hacia las tres capacidades y mostrar cuándo se combinan. No sustituye las páginas técnicas, ni constituye un inventario exhaustivo de servicios. Navegación global: Inicio / Capacidades / Sectores / Proyectos y experiencia / Sobre BAFRAS / Contacto. «Conocimiento» no se publica. La etiqueta pública es «Automatización y control» (ID interno DIG).

---
# TEXTO DESTINADO A PUBLICACIÓN (ES)

## C01 · Cabecera
**Antetítulo:** NUESTRAS CAPACIDADES

**H1:** Tres especialidades de ingeniería. Soluciones ajustadas a cada proyecto.

**Introducción:** Desarrollamos estudios, proyectos y asistencia técnica en infraestructuras e instalaciones, sistemas energéticos y automatización y control. Cada encargo puede abordarse desde una especialidad o requerir la coordinación de varias, según sus necesidades y condicionantes.

**Enlace de orientación:** Explorar las especialidades → ancla C02.

## C02 · Nuestras áreas de ingeniería
**H2:** Encuentra la especialidad que necesita tu proyecto.

**Introducción:** Conoce el alcance de cada área y las actuaciones que podemos estudiar o desarrollar.

### Infraestructuras e instalaciones
Ingeniería para el diseño, análisis y mejora de instalaciones eléctricas, mecánicas y auxiliares en edificios e infraestructuras. Intervenimos en nuevas actuaciones y en la revisión o adaptación de sistemas existentes, con el alcance técnico definido en cada encargo.

**Ámbitos destacados:** Instalaciones eléctricas de baja y media tensión · Climatización, ventilación y sistemas térmicos · Instalaciones hidráulicas y saneamiento · Coordinación y asistencia técnica.

**Enlace:** Ver infraestructuras e instalaciones → página de capacidad INF.

### Sistemas energéticos
Analizamos la demanda y el funcionamiento energético de instalaciones para evaluar alternativas de eficiencia, generación, almacenamiento y gestión de energía. Desarrollamos estudios y proyectos considerando los datos disponibles, las condiciones de operación y la viabilidad de las soluciones.

**Ámbitos destacados:** Análisis y auditoría energética · Eficiencia y optimización · Fotovoltaica y autoconsumo · Almacenamiento y gestión energética.

**Enlace:** Ver sistemas energéticos → página de capacidad ENE.

### Automatización y control
Diseñamos y desarrollamos soluciones de instrumentación, control, supervisión e integración para instalaciones y procesos. Abordamos la adquisición de datos, la comunicación entre equipos y las funciones de automatización necesarias para su operación y seguimiento.

**Ámbitos destacados:** Instrumentación y adquisición de datos · PLC y controladores DDC · BMS y SCADA · Comunicaciones, integración y software técnico.

**Enlace:** Ver automatización y control → página de capacidad DIG.

## C03 · Ingeniería que conecta disciplinas
**H2:** Cuando las instalaciones, la energía y el control están relacionados.

**Texto:** En determinados proyectos, una decisión técnica afecta a varias especialidades. Analizamos esas relaciones para definir las actuaciones y responsabilidades necesarias, sin incorporar disciplinas o tecnologías que el proyecto no requiera.

**Ejemplo 1 — Modernización de una instalación térmica.** Puede ser necesario estudiar los equipos y circuitos, revisar la demanda energética y adaptar las estrategias de regulación y control.

**Ejemplo 2 — Autoconsumo y almacenamiento.** La incorporación de generación fotovoltaica o baterías puede requerir estudiar el perfil energético, desarrollar la instalación eléctrica e integrar medida, supervisión y control.

**Ejemplo 3 — Problemas de funcionamiento en una instalación.** Antes de decidir una reforma, puede ser conveniente comprobar las condiciones de operación, el estado de los equipos y las señales o secuencias de control.

**Enlaces contextuales:** Las denominaciones de las capacidades implicadas enlazan a sus páginas respectivas.

## C04 · Cómo podemos colaborar
**H2:** Ingeniería en distintas fases de un proyecto.

**Introducción:** Podemos intervenir en una actuación concreta o acompañar varias fases, con un alcance y unos entregables definidos para cada encargo.

**Diagnóstico y estudios.** Inspección técnica dentro del alcance contratado, análisis de datos, mediciones y evaluación de alternativas.

**Diseño y proyecto.** Definición de soluciones, cálculos, planos, especificaciones y documentación técnica.

**Asistencia y coordinación.** Apoyo a la planificación, revisión de interfaces, seguimiento técnico y coordinación con los agentes del proyecto.

**Programación, integración y verificación.** Configuración de sistemas, pruebas y documentación de resultados cuando estas actuaciones formen parte del encargo.

## C05 · Contacto
**H2:** ¿Qué necesitas resolver o desarrollar?

**Texto:** Cuéntanos el contexto de tu instalación o proyecto y qué objetivo persigues. Revisaremos la información inicial para valorar cómo podemos colaborar y qué alcance técnico conviene estudiar.

**CTA principal:** Cuéntanos tu proyecto → Contacto.

**Enlace secundario:** Conoce nuestros proyectos y experiencia → Proyectos y experiencia.

---
# ESPECIFICACIÓN DE DISEÑO Y FLUJOS (NO VISIBLE COMO COPY)

## Jerarquía visual
1. C01 hero compacto, menos dominante que el de Inicio; H1 y texto de entrada, sin fotografía obligatoria.
2. C02 es el bloque principal: tres tarjetas o paneles de igual jerarquía, título, párrafo, ámbitos y enlace explícito. No ocultar capacidades en carrusel.
3. C03 tres ejemplos breves; rotular visualmente como «Ejemplos de aplicación» para no confundir con referencias ejecutadas.
4. C04 cuatro modalidades en composición compacta; no presentarlas como proceso obligatorio ni como promesa de ejecución material.
5. C05 CTA de contacto destacado, enlace secundario de credibilidad.

## Recorridos
- Visitante que conoce la disciplina: menú → Capacidades → tarjeta técnica → página hija → Contacto.
- Visitante con problema mixto: Inicio → Capacidades → ejemplo C03 → páginas de especialidad → Contacto.
- Ingeniería colaboradora: Capacidades → modalidades C04 → Sobre BAFRAS o Contacto.
- Visitante sin diagnóstico: Capacidades → C05 → Contacto.
- Acceso SEO directo a página hija: breadcrumb a Capacidades, relación con otras capacidades y CTA a Contacto; no obligar a visitar el índice.

## Contratos de enlace
- C01 ancla interna #especialidades.
- C02 tres enlaces a páginas hijas, con etiquetas públicas aprobadas.
- C03 enlaces por disciplina únicamente cuando aporten orientación; evitar más de tres enlaces por ejemplo.
- C05 Contacto y Proyectos y experiencia.
- Cabecera y pie globales mantienen navegación y acceso a contacto; evitar CTA duplicados en cada bloque.

## Guardarraíles editoriales
- Ejemplos C03 son hipotéticos, no proyectos ni paquetes contratados. Rotularlos como aplicaciones.
- Las actividades profesionales y las responsabilidades reguladas se concretan según competencias, habilitaciones, designaciones y contrato. No se presupone ejecución material ni inspección acreditada.
- No publicar IA/ML como servicio operativo: DIG-18 figura como futuro en Doc01.
- No prometer ahorros, rendimientos, resultados ni certificaciones.
- No afirmar que la empresa ha realizado proyectos por el mero hecho de que los fundadores tengan experiencia previa.
- Las etiquetas «ámbitos destacados» son ilustrativas, no inventario completo de los 56 servicios ofertables.
- Localizaciones CA/EN/DE requieren adaptación y validación editorial independientes.

## Auditoría multidisciplinar — decisiones
**Dirección:** se mantiene la arquitectura de páginas aprobada; no se abren páginas nuevas.
**Comercial:** H1 más específico; C02 dirige por especialidad; C03 responde a proyectos mixtos; C05 conversión sin presión.
**Ingeniería:** terminología ajustada; se elimina la inferencia de que todas las fases están incluidas; se diferencia verificación de certificación externa.
**UX:** cinco bloques, tarjetas de igual importancia, enlaces descriptivos y navegación no lineal.
**Marca:** se reduce lenguaje genérico y repetición literal de la homepage.
**SEO:** página hub temática; profundidad técnica en páginas hijas, sin crear páginas de servicios artificiales.

## Trazabilidad de fuentes
Doc01 `engineering-service-taxonomy-v0.99-normalizada.md`: capacidades CAP-INF/CAP-ENE/CAP-DIG; modalidades MOD-AUD, MOD-EST, MOD-PRO, MOD-AT, MOD-COM, MOD-PRU y límites de ejecución; líneas futuras. Doc02 `01_Documento_Maestro_02_Consolidado.md`: enfoque necesidad → criterio → entregable, límites de evidencia y escenarios integrados. Doc03 homepage V1.1: identidad y secciones H01–H07 aprobadas, sin cambios. Los textos de esta página son síntesis editorial, no citas literales.

**Estado:** texto propuesto como versión final para validación del usuario. No afirmar aprobación antes de recibirla.


---

# PARTE C — INFRAESTRUCTURAS E INSTALACIONES (REVISIÓN 03.D.2, PENDIENTE DE APROBACIÓN)

# BAFRAS Engineering — Documento 03 · Página «Infraestructuras e instalaciones»
**Iteración 03.D.2 · revisión multidisciplinar de equilibrio · 02/11/2026**

**Ruta conceptual:** Inicio > Capacidades > Infraestructuras e instalaciones. **Estado:** revisión propuesta, pendiente de aprobación del usuario. **Fuentes:** Documento Maestro 01 v0.99-N (apartados 3, 4.1, 5); Documento Maestro 02 consolidado v1.0 RC (CAP-INF, apartados 3.1–3.5); Documento 03 consolidado v1.2. Los estados de publicación de los servicios en Documento 01 siguen siendo `PENDIENTE_PUBLICACION`; esta propuesta no los convierte automáticamente en `PUBLICABLE`.

## INF-01 · Hero
**Eyebrow:** CAPACIDADES / INFRAESTRUCTURAS E INSTALACIONES

**H1:** Ingeniería de instalaciones para edificios, infraestructuras y procesos.

**Subtítulo:** Diseñamos, analizamos y revisamos instalaciones eléctricas, mecánicas e hidráulicas, atendiendo a las condiciones de uso, funcionamiento y mantenimiento de cada proyecto.

**Texto de apoyo:** Trabajamos tanto en nuevas actuaciones y reformas como en el diagnóstico de instalaciones existentes. Definimos el alcance técnico, estudiamos las alternativas que procedan y coordinamos las interfaces entre disciplinas cuando el proyecto lo requiere.

**CTA principal:** Cuéntanos tu proyecto → Contacto. **Enlace secundario:** Ver ámbitos de ingeniería → ancla #ambitos.

## INF-02 · Cuándo podemos ayudarte
**H2:** Desde el diseño inicial hasta la revisión de una instalación existente.

**Introducción:** Cada encargo parte de una necesidad distinta. Antes de definir una actuación, identificamos qué información existe, qué condicionantes deben comprobarse y qué resultado técnico necesita el cliente.

1. **Nueva instalación, reforma o ampliación.** Definimos necesidades, cargas y requisitos de uso para desarrollar la ingeniería y coordinar las instalaciones implicadas.
2. **Funcionamiento deficiente o incidencias recurrentes.** Revisamos el comportamiento de equipos y redes para identificar posibles causas, limitaciones y actuaciones justificadas.
3. **Infraestructura técnica con requisitos específicos.** Estudiamos redes eléctricas, hidráulicas o servicios auxiliares atendiendo a capacidad, operación e interfaces.
4. **Adecuación técnica y seguridad.** Evaluamos los requisitos aplicables al alcance del proyecto y la documentación necesaria para definir las actuaciones.
5. **Decisiones de reforma, compra o inversión.** Analizamos el estado técnico de instalaciones y activos para orientar prioridades y estimaciones de intervención.

**Interacción:** enlaces de ancla solo donde haya correspondencia inequívoca; evitar que cada necesidad tenga una falsa equivalencia con una única especialidad.

## INF-03 · Ámbitos de ingeniería {#ambitos}
**H2:** Instalaciones y sistemas que podemos estudiar y desarrollar.

**Introducción:** Trabajamos en cuatro ámbitos técnicos de instalaciones, con servicios de diagnóstico y coordinación que pueden aplicarse a cualquiera de ellos. El alcance se define para cada encargo.

### Electricidad e infraestructura eléctrica
Diseño y revisión de instalaciones de baja tensión, redes de media tensión y centros de transformación, incluyendo distribución eléctrica, cuadros, protecciones, puesta a tierra e iluminación.

**Referencia técnica y alcance:** INF-01, INF-02, INF-13, INF-16. El estudio de cargas críticas y continuidad eléctrica se desarrolla cuando el encargo lo requiere. No se atribuyen a BAFRAS decisiones reservadas a distribuidoras u operadores.

### Climatización, ventilación y refrigeración
Ingeniería de climatización y producción térmica, ventilación y extracción, redes de distribución y refrigeración comercial o industrial, considerando las condiciones de uso y operación.

**Referencia técnica y alcance:** INF-03, INF-04, INF-24. El control y la programación de BMS se desarrollan en la capacidad «Automatización y control» cuando corresponda.

### Agua, hidráulica y servicios auxiliares
Diseño y revisión de instalaciones de fontanería, agua caliente sanitaria, saneamiento y drenaje, redes hidráulicas, bombeos, depósitos y servicios auxiliares industriales.

**Referencia técnica y alcance:** INF-05, INF-14, INF-15, INF-23. Las actuaciones sobre eficiencia de recursos se coordinan con «Sistemas energéticos» según el encargo.

### Protección y condiciones técnicas de las instalaciones
Ingeniería de instalaciones activas de protección contra incendios y estudios de acústica y vibraciones relacionados con equipos e instalaciones.

**Referencia técnica y alcance:** INF-06, INF-20. La oferta no equivale a inspección reglamentaria independiente, certificación acreditada o desarrollo automático de una estrategia integral de evacuación.

### Diagnóstico, coordinación y gestión técnica de activos
**Tratamiento visual:** bloque transversal diferenciado, no quinta tarjeta idéntica a las anteriores.

Además del diseño de instalaciones, realizamos diagnósticos técnicos de sistemas existentes, coordinación entre especialidades, evaluación del estado de activos y planificación de actuaciones. Estas tareas pueden aplicarse a cualquiera de los ámbitos anteriores.

**Referencia técnica y alcance:** INF-09, INF-17, INF-18, INF-25. No implica asumir el mantenimiento material ni la autoría de proyectos ajenos.

**Regla de presentación:** los textos anteriores son el contenido visible recomendado. Las referencias de catálogo, exclusiones y matices técnicos son metadatos editoriales internos, no texto público de la página. Los entregables se explican una sola vez en INF-04.

## INF-04 · Qué podemos entregar
**H2:** Del diagnóstico a la documentación de proyecto y la asistencia técnica.

**Introducción:** El resultado se acuerda en cada encargo. Estas son modalidades y entregables habituales, no fases obligatorias ni un paquete cerrado.

- **Diagnóstico y estudios:** informes de estado, mediciones y análisis, cálculos preliminares, alternativas y criterios de intervención.
- **Diseño y proyecto:** memorias, cálculos justificativos, esquemas, planos, especificaciones, mediciones y documentación de contratación cuando proceda.
- **Asistencia técnica y coordinación:** revisión de documentación, gestión de interfaces, soporte técnico y seguimiento según responsabilidades contratadas.
- **Pruebas y verificación:** protocolos, resultados, incidencias y documentación de comprobación cuando formen parte del alcance.

**Nota de precisión:** la dirección facultativa, la tramitación, la ejecución material y las verificaciones reglamentarias tienen requisitos y responsabilidades específicos; no están incluidas automáticamente en cualquier encargo.

## INF-05 · Relación con otras capacidades
**H2:** Instalaciones que se relacionan con la energía y el control.

**Texto:** Una reforma térmica puede requerir un estudio de demanda y regulación; una infraestructura eléctrica puede formar parte de una instalación de autoconsumo; y una incidencia operativa puede estar relacionada con sensores o secuencias de control. Cuando estas relaciones son relevantes, coordinamos el trabajo con las otras especialidades de BAFRAS, definiendo los límites de cada actuación.

**Enlace 1:** Sistemas energéticos → página ENE. **Enlace 2:** Automatización y control → página DIG.

## INF-06 · Experiencia y confianza
**H2:** Experiencia técnica aplicada a instalaciones reales.

**Texto:** El equipo de BAFRAS reúne experiencia profesional en ingeniería y revisión de instalaciones de edificios e infraestructuras. En «Proyectos y experiencia» detallamos las actuaciones documentadas, la participación de cada profesional y el contexto en el que se realizaron.

**Enlace:** Conocer proyectos y experiencia → índice de referencias.

**Regla de publicación:** no mostrar cifras, clientes, logotipos o fotografías de referencias concretas sin validación y permisos; distinguir trabajos previos de los fundadores de proyectos contratados por BAFRAS.

## INF-07 · Contacto
**H2:** ¿Necesitas diseñar, revisar o mejorar una instalación?

**Texto:** Cuéntanos qué tipo de instalación tienes, en qué fase se encuentra el proyecto y qué necesitas resolver. Revisaremos la información inicial para valorar el alcance de ingeniería y el siguiente paso.

**CTA:** Cuéntanos tu proyecto → Contacto.

---
## Contrato de navegación y experiencia de usuario
- **Entrada desde Inicio o Capacidades:** el visitante reconoce INF en el hero y localiza la familia técnica; desde ella puede consultar entregables o contactar.
- **Entrada desde buscador:** H1 descriptivo, contexto y navegación de migas; ninguna información esencial depende de haber visto Inicio.
- **Cliente con incidencia:** INF-02 «Funcionamiento deficiente» → INF-03 «Diagnóstico...» → INF-04 «Diagnóstico y estudios» → Contacto.
- **Arquitectura, instaladora o promotora:** INF-03 ámbito técnico → INF-04 «Diseño y proyecto / asistencia» → Contacto.
- **Proyecto multidisciplinar:** INF-05 → ENE o DIG → Contacto.
- **Cliente que necesita confianza:** INF-06 → Proyectos y experiencia → Contacto.
- **Navegación de escritorio:** índice de anclas discreto si el diseño lo permite; móvil con anclas en lista compacta, sin menús secundarios complejos.
- **CTA:** principal en hero y cierre; enlaces contextuales entre medias; evitar un botón comercial en cada familia.

## Auditoría multidisciplinar y límites
**Dirección/comercial:** la página responde a problemas de compra, no solo a nombres de instalaciones. **Ingeniería:** se han mantenido fronteras con ENE/DIG, modalidades y exclusiones de Doc01. **UX:** cinco familias técnicas y rutas por intención; no crear fichas por servicio de manera automática. **Marca:** lenguaje sobrio, sin superlativos ni resultados garantizados. **SEO:** un H1, H2 descriptivos, estructura semántica y enlaces internos. **Legal/editorial:** ningún texto acredita por sí solo habilitaciones o experiencia corporativa; los estados de catálogo requieren aprobación de publicación.

**Exclusiones expresas del Documento 01:** INF-19 (gases técnicos) e INF-21 (instalaciones especiales) son líneas futuras `NO_PUBLICAR`. INF-07, 08, 10, 11, 12 y 22 son registros históricos redirigidos y no se presentan como servicios autónomos. Se han empleado las modalidades aplicables en lugar de convertirlos en nuevos servicios.

**Pendiente de validación:** texto completo INF-01–INF-07, selección visual y atribución de referencias. No implementar ni publicar antes de aprobación editorial y comprobaciones de habilitación cuando procedan.

## Dictamen de la iteración 03.D.2 — Equilibrio y profundidad
- **Dirección/comercial:** mantener el alcance de las cinco familias; diferenciar cuatro ámbitos de instalaciones y una intervención transversal.
- **Ingeniería:** conservar referencias internas y exclusiones; evitar equiparar la familia de protección/acústica con una oferta integral de seguridad del edificio.
- **UX:** cuatro tarjetas técnicas comparables y un bloque transversal de ancho completo; no usar cinco tarjetas visualmente idénticas.
- **SEO:** conservar vocabulario técnico esencial en texto HTML visible, sin convertir la página en un glosario.
- **Marca:** mantener títulos descriptivos y párrafos de extensión similar, sin relleno para forzar simetría.
- **Contenido:** explicar actuaciones y entregables en INF-04, evitando listas repetidas bajo cada ámbito.
- **Publicación:** aprobación de copy no sustituye revisión de estados de servicio, habilitaciones y referencias.

**Decisión solicitada:** validar esta presentación de cuatro ámbitos técnicos + un bloque transversal. No se altera el resto de la página.

## REGISTRO DE APROBACIÓN — ITERACIÓN 03.D.3
**Decisión del usuario:** «confirmo cuatro ámbitos + bloque transversal de diagnóstico. cerramos infraestructura». La sección INF queda **APROBADA EDITORIALMENTE**, con el contenido de 03.D.2 y la jerarquía de cuatro ámbitos más diagnóstico transversal. No equivale a aprobación de diseño gráfico, habilitaciones, referencias ni publicación.

---

---

# PARTE NUEVA — SISTEMAS ENERGÉTICOS (PROPUESTA AUDITADA, NO APROBADA)

# BAFRAS Engineering — Sistemas energéticos
## Documento 03 · Iteración 03.E.2 · Propuesta editorial V1.1

**Estado:** propuesta auditada, pendiente de validación del usuario. No publicada.
**Base:** Documento 01, taxonomía ENE-01 a ENE-23 (ENE-09 redirigida a modalidad de estudios), Documento 02 y página ENE V1.0 del Documento 03. La comparación con ofertas habituales de consultoría e ingeniería energética es criterio profesional complementario, no prueba de que BAFRAS preste todos los servicios del mercado.

## Dictamen de auditoría
La V1.0 agrupa indebidamente auditoría y gestión energética recurrente, recarga con microredes, y planificación económica con huella de carbono. Se propone **seis ámbitos editoriales** y un bloque transversal de modalidades. Los ámbitos no son servicios nuevos ni sustituyen la taxonomía técnica. La calidad de suministro, las comunidades energéticas, la gestión de suministros y la previsión quedan explícitas.

## ENE-01 · Hero
**Eyebrow:** CAPACIDADES / SISTEMAS ENERGÉTICOS

**H1:** Ingeniería para comprender, mejorar y transformar sistemas energéticos.

**Texto principal:** Analizamos consumos, evaluamos alternativas y desarrollamos proyectos de eficiencia energética, generación renovable, almacenamiento, electrificación y gestión de la energía. Trabajamos con datos y criterios técnicos para adaptar cada actuación a las necesidades y condiciones de operación de la instalación.

**Texto de apoyo:** Podemos intervenir en el diagnóstico de sistemas existentes, el estudio de nuevas inversiones y la definición de estrategias de operación y seguimiento.

**CTA principal:** Cuéntanos tu proyecto → Contacto.
**CTA secundario:** Explorar ámbitos de actuación → ENE-03.

## ENE-02 · Necesidades del cliente
**H2:** ¿Qué decisión energética necesitas tomar?

**Introducción:** Antes de invertir o modificar una instalación, conviene conocer cómo se utiliza la energía, qué condicionantes existen y qué resultados pueden esperarse de cada alternativa.

1. **Entender y reducir consumos.** Analizamos demanda, funcionamiento y oportunidades de eficiencia.
2. **Producir o almacenar energía.** Estudiamos generación renovable, autoconsumo, baterías y su integración.
3. **Electrificar instalaciones o procesos.** Comparamos alternativas de suministro, producción térmica y recuperación energética.
4. **Incorporar recarga o coordinar varios activos.** Evaluamos necesidades de potencia, operación y flexibilidad.
5. **Controlar costes y mejorar el seguimiento.** Revisamos suministros, indicadores, previsiones y estrategias de gestión.
6. **Planificar la descarbonización.** Cuantificamos consumos y emisiones y estudiamos actuaciones de reducción.

## ENE-03 · Ámbitos de actuación
**H2:** Seis ámbitos de ingeniería energética.

**Introducción:** Desde la caracterización de la demanda hasta la integración de nuevos activos, abordamos los sistemas energéticos desde las especialidades que requiere cada proyecto.

### 1. Diagnóstico y eficiencia energética
Caracterizamos consumos, curvas de demanda y balances energéticos para comprender el funcionamiento de edificios, instalaciones y procesos. Evaluamos rendimientos, oportunidades de mejora y medidas de eficiencia, con estimaciones basadas en datos e hipótesis identificadas.

**Incluye:** auditorías energéticas; análisis de demanda; eficiencia y optimización; estudios de potencia y calidad de energía; diagnóstico de rendimiento de plantas fotovoltaicas y baterías.

### 2. Generación renovable y almacenamiento
Estudiamos y desarrollamos sistemas fotovoltaicos, autoconsumo y almacenamiento electroquímico. Analizamos producción, demanda, dimensionamiento, conexión e integración, incluidos autoconsumo colectivo, soluciones híbridas y configuraciones técnicas para comunidades energéticas cuando proceda.

**Incluye:** fotovoltaica; autoconsumo individual y colectivo; BESS; hibridación; estudios de producción y rendimiento.

### 3. Electrificación y sistemas térmicos
Evaluamos la sustitución de combustibles y las alternativas para producir, distribuir y aprovechar energía térmica. Estudiamos electrificación, recuperación de calor, almacenamiento térmico y redes de calor y frío, coordinando el diseño de equipos y circuitos con Infraestructuras e instalaciones.

**Incluye:** electrificación térmica; recuperación de calor; almacenamiento térmico; sistemas centralizados y redes térmicas.

### 4. Movilidad eléctrica y sistemas energéticos integrados
Estudiamos infraestructuras de recarga y su relación con la potencia disponible, la demanda y los demás activos energéticos. También definimos criterios de coordinación para microredes, sistemas híbridos y estrategias de flexibilidad, incluyendo interfaces de medida y control cuando corresponda.

**Incluye:** recarga de vehículos eléctricos; potencia y simultaneidad; microredes; coordinación de generación, baterías y cargas; flexibilidad.

### 5. Gestión, monitorización y costes energéticos
Definimos indicadores y criterios de seguimiento para conocer el comportamiento energético a lo largo del tiempo. Analizamos suministros, facturación y contratos, presupuestos y previsiones de demanda o generación, y planteamos estrategias de operación y gestión energética según el alcance acordado.

**Incluye:** medida y monitorización; seguimiento energético; auditoría de suministros; optimización de costes y contratos; previsiones; gestión energética recurrente.

### 6. Descarbonización y sostenibilidad energética
Estudiamos escenarios de reducción de emisiones y hojas de ruta para transformar el uso de la energía en edificios, instalaciones y organizaciones. Elaboramos inventarios y análisis de huella de carbono dentro de límites y metodologías definidos, diferenciando las estimaciones de una verificación independiente.

**Incluye:** planes de descarbonización; escenarios energéticos; huella de carbono; contabilidad de emisiones; priorización de actuaciones.

### Nota de alcance — eficiencia hídrica
La auditoría y eficiencia hídrica (ENE-23) permanece en la oferta técnica y puede mencionarse como servicio complementario en proyectos de eficiencia de recursos. No se presenta como séptimo ámbito energético ni se confunde con el diseño de redes hidráulicas, propio de Infraestructuras e instalaciones.

## ENE-04 · Qué podemos entregar
**H2:** Estudios, proyectos y asistencia técnica adaptados a cada encargo.

- **Diagnóstico y auditoría:** caracterización de consumos, líneas base, balances, informes y oportunidades de mejora.
- **Viabilidad y alternativas:** dimensionamiento, simulaciones, escenarios operativos y comparativas técnico-económicas con hipótesis explícitas.
- **Ingeniería y proyecto:** cálculos, memorias, esquemas, planos, especificaciones y documentación técnica.
- **Integración y seguimiento:** requisitos de medida y control, protocolos de pruebas, indicadores y seguimiento de resultados cuando proceda.

**Criterio:** viabilidad y planificación son modalidades transversales, no un área de ingeniería separada. No se garantizan ahorros, retornos, subvenciones o resultados de previsión. Dirección facultativa, ejecución, tramitación, inspección reglamentaria y operación recurrente se acuerdan expresamente cuando correspondan.

## ENE-05 · Integración con otras capacidades
**H2:** Energía, instalaciones y control: especialidades coordinadas.

Un sistema de autoconsumo o almacenamiento necesita una infraestructura eléctrica adecuada y puede requerir estrategias de supervisión. La electrificación térmica puede implicar modificaciones mecánicas y de regulación. Definimos los límites y responsabilidades de cada disciplina según el proyecto.

**Enlace:** Infraestructuras e instalaciones → ingeniería eléctrica, mecánica e hidráulica.
**Enlace:** Automatización y control → instrumentación, comunicaciones, programación y supervisión.

## ENE-06 · Proyectos y experiencia
**H2:** Experiencia técnica en sistemas energéticos.

El equipo de BAFRAS reúne experiencia profesional en el estudio y desarrollo de sistemas energéticos. En «Proyectos y experiencia» presentamos referencias documentadas, diferenciando la participación profesional previa de los fundadores de los proyectos contratados directamente por BAFRAS.

**Enlace:** Conocer proyectos y experiencia.

## ENE-07 · Contacto
**H2:** ¿Tienes una decisión energética que estudiar?

Cuéntanos qué instalación o activo quieres analizar, qué información tienes disponible y qué objetivo persigues. Valoraremos el punto de partida y el alcance técnico necesario para avanzar.

**CTA:** Cuéntanos tu proyecto → Contacto.

## Navegación y diseño
- Migas: Inicio / Capacidades / Sistemas energéticos.
- ENE-02: seis situaciones breves con anclas a ENE-03, sin crear nuevas URLs.
- ENE-03: seis tarjetas en retícula 2×3 en escritorio y una columna en móvil. Título, descripción de 40–65 palabras y línea de servicios identificables. Sin imágenes genéricas obligatorias en cada tarjeta.
- ENE-04: cuatro modalidades transversales, visualmente separadas de los seis ámbitos.
- Dos CTA de contacto (hero y cierre), enlace a experiencia y enlaces a INF/DIG.
- Evitar que recarga, BESS, huella de carbono o gestión recurrente parezcan servicios ejecutados o certificados sin evidencia.

## Matriz de cobertura del catálogo
| Código | Servicio técnico del Documento 01 | Presentación V1.1 |
|---|---|---|
| ENE-01 | Auditoría y caracterización energética | Ámbito 1 |
| ENE-02 | Eficiencia y optimización | Ámbito 1 |
| ENE-03 | Medición y monitorización | Ámbito 5 |
| ENE-04 | Fotovoltaica y autoconsumo | Ámbito 2 |
| ENE-05 | Almacenamiento electroquímico | Ámbito 2 |
| ENE-06 | Electrificación térmica | Ámbito 3 |
| ENE-07 | Integración y pruebas | Modalidad transversal |
| ENE-08 | Estrategias de operación | Ámbitos 4 y 5 |
| ENE-09 | REDIRIGIDO a modalidad de estudios | Modalidad transversal, no servicio autónomo |
| ENE-10 | Recarga EV | Ámbito 4 |
| ENE-11 | Auditoría de suministros | Ámbito 5 |
| ENE-12 | Gestión recurrente y medición de resultados | Ámbito 5 |
| ENE-13 | Redes térmicas | Ámbito 3 |
| ENE-14 | Microredes y flexibilidad | Ámbito 4 |
| ENE-15 | Potencia, calidad de energía y demanda | Ámbito 1 |
| ENE-16 | Autoconsumo colectivo y comunidades energéticas | Ámbito 2 |
| ENE-17 | Descarbonización y hojas de ruta | Ámbito 6 |
| ENE-18 | Huella de carbono | Ámbito 6 |
| ENE-19 | Diagnóstico FV/BESS | Ámbito 1 (referencia en 2) |
| ENE-20 | Previsión de demanda y generación | Ámbito 5 |
| ENE-21 | Costes y contratos energéticos | Ámbito 5 |
| ENE-22 | Almacenamiento térmico y recuperación | Ámbito 3 |
| ENE-23 | Auditoría y eficiencia hídrica | Servicio complementario transversal |

## Auditoría multidisciplinar
**Dirección:** seis ámbitos mejoran cobertura sin prometer una empresa instaladora, comercializadora, O&M o verificadora.
**Ingeniería:** separa sistemas físicos (2, 3, 4) de diagnóstico (1), gestión (5) y descarbonización (6); viabilidad y pruebas son modalidades.
**Comercial:** presenta explícitamente costes, contratos, recarga, comunidades energéticas, almacenamiento, emisiones y calidad de suministro.
**UX:** seis tarjetas breves son más escaneables que cinco párrafos largos; bloque transversal para entregables.
**SEO:** términos buscables visibles en subtítulos y ejemplos, sin proliferación de páginas ni promesas no acreditadas.
**Legal y evidencia:** mantener separación entre capacidad ofertable, experiencia profesional y actividad realmente contratada; comprobar habilitaciones, permisos y acreditaciones según cada servicio.

**Estado:** V1.1 propuesta auditada; pendiente de validación editorial del usuario. No modificar las páginas aprobadas.


---

# PARTE E — AUTOMATIZACIÓN Y CONTROL · ITERACIÓN 03.F.2 V1.1 (APROBADA)

# BAFRAS Engineering — Automatización y control
## Documento 03 · Iteración 03.F.2 · Texto editorial definitivo V1.1
**Estado:** APROBADO Y CERRADO EDITORIALMENTE por solicitud del usuario (2026-11-02). La aprobación editorial no equivale a publicación ni sustituye la validación de servicios y evidencias.
**Base:** Documento 01, taxonomía normalizada V0.99, DIG-01 a DIG-22; Documento 02, CAP-DIG y DIG-N1 a DIG-N5; revisión de V1.0.

## DIG-W01 · Cabecera
**Eyebrow:** CAPACIDADES / AUTOMATIZACIÓN Y CONTROL
**H1:** Ingeniería de automatización y control para instalaciones y procesos.
**Texto principal:** Analizamos el funcionamiento de equipos e instalaciones para definir qué conviene medir, automatizar, supervisar o integrar. Desarrollamos soluciones de instrumentación, control, comunicaciones y software técnico adaptadas a los requisitos de cada proyecto.
**Texto de apoyo:** Trabajamos tanto en sistemas existentes como en nuevas actuaciones, definiendo funciones, interfaces y criterios de verificación antes de intervenir.
**CTA principal:** Cuéntanos tu proyecto → Contacto.
**CTA secundario:** Explorar ámbitos de actuación → #ambitos.

## DIG-W02 · Necesidades del cliente
**H2:** Cuando necesitas comprender, controlar o conectar mejor tus sistemas.
**Introducción:** No siempre es necesario sustituir equipos o implantar una nueva plataforma. Primero conviene entender cómo funciona la instalación y qué limitaciones presenta.
1. **Faltan datos para saber qué ocurre.** Estudiamos qué variables medir, cómo adquirirlas y cómo presentar información útil.
2. **El control es manual, inestable o difícil de ajustar.** Revisamos señales, secuencias y modos de funcionamiento para definir mejoras.
3. **Los equipos no intercambian información.** Analizamos protocolos, compatibilidades e interfaces para valorar su integración.
4. **La automatización existente necesita modernizarse.** Evaluamos limitaciones y alternativas, considerando los equipos que pueden conservarse.
5. **Los datos no se traducen en decisiones.** Desarrollamos análisis, herramientas y modelos técnicos cuando aportan una utilidad definida.

## DIG-W03 · Ámbitos de actuación
**H2:** Del dato al control: seis ámbitos de ingeniería conectados.
**Introducción:** Cada ámbito responde a una función distinta. Podemos abordarlos de forma independiente o coordinarlos cuando el proyecto lo requiere.

### 1. Instrumentación, adquisición de datos y telemetría
Definimos las variables a medir, los sensores y la adquisición de señales para obtener información fiable de equipos e instalaciones. También estudiamos el registro y la transmisión remota de datos, sin confundir monitorización con control de equipos.
**Etiquetas:** Sensores · Señales · Telemetría · Monitorización remota.

### 2. Ingeniería de automatización y programación de control
Definimos funciones y secuencias de operación, arquitecturas de control, enclavamientos y criterios de funcionamiento. Desarrollamos programación y parametrización de PLC o DDC según los controladores y el alcance contratado.
**Etiquetas:** Lógica de control · PLC/DDC · Secuencias · Automatismos.

### 3. Supervisión y control técnico de instalaciones
Diseñamos interfaces de operación, alarmas, tendencias y funciones de supervisión mediante HMI, SCADA o BMS. En edificios, coordinamos el control técnico con las características de sus instalaciones; la supervisión no sustituye la lógica de los controladores.
**Etiquetas:** SCADA/HMI · BMS · Alarmas · Operación.

### 4. Integración de equipos, comunicaciones y arquitectura OT
Estudiamos la interoperabilidad entre equipos, protocolos industriales y redes de operación. Definimos interfaces y requisitos de comunicación, incluyendo consideraciones de segmentación y seguridad OT en el diseño, sin ofrecer auditorías especializadas o certificaciones de ciberseguridad.
**Etiquetas:** Protocolos · Redes OT · Interoperabilidad · Interfaces.

### 5. Software técnico, datos y aplicaciones de ingeniería
Desarrollamos herramientas para procesar y analizar datos, automatizar cálculos e integrar aplicaciones mediante API. También abordamos modelos físicos, simulaciones y algoritmos de optimización cuando los datos y el objetivo lo permiten, sin equipararlos automáticamente a inteligencia artificial o gemelos digitales operativos.
**Etiquetas:** Analítica · Software técnico · API · Simulación · Optimización.

### 6. Control e integración de activos energéticos
Desarrollamos funciones de supervisión y control para generación, almacenamiento y gestión energética, incluyendo integración EMS o PPC cuando corresponda. Las estrategias de explotación y el dimensionamiento energético se definen desde Sistemas energéticos; aquí abordamos su implementación técnica.
**Etiquetas:** EMS · PPC · Consignas · Integración de activos.

**Bloque transversal — Diagnóstico, pruebas y evolución de sistemas**
Revisamos automatismos existentes, documentamos interfaces, realizamos pruebas de integración y puesta en marcha funcional cuando forman parte del encargo. El soporte evolutivo se define mediante condiciones específicas; no implica mantenimiento continuo ni disponibilidad 24/7.

## DIG-W04 · Entregables
**H2:** De los requisitos funcionales a la verificación del sistema.
- **Diagnóstico y definición:** inventarios de equipos y señales, análisis funcional y requisitos.
- **Diseño:** arquitecturas, diagramas, listas de señales y secuencias de control.
- **Desarrollo e integración:** programación, parametrización, interfaces y aplicaciones según alcance.
- **Pruebas y documentación:** protocolos, registros de resultados y criterios de aceptación.
**Nota:** Las actuaciones y los entregables dependen del alcance contratado.

## DIG-W05 · Relación con otras capacidades
**H2:** El control debe responder a la instalación y a sus objetivos.
**Infraestructuras e instalaciones:** diseño y condiciones físicas de equipos, redes e instalaciones eléctricas o mecánicas. → Infraestructuras e instalaciones.
**Sistemas energéticos:** análisis de demanda, estrategias de eficiencia y operación de generación o almacenamiento. → Sistemas energéticos.
**Texto de cierre:** Coordinamos estas especialidades cuando una actuación requiere decisiones sobre equipos, energía y automatización.

## DIG-W06 · Proyectos y experiencia
**H2:** Experiencia técnica en control, integración y sistemas digitales.
**Texto:** En «Proyectos y experiencia» presentamos actuaciones documentadas y la participación concreta de los profesionales del equipo, diferenciando su trayectoria anterior de los proyectos contratados por BAFRAS.
**Enlace:** Conocer proyectos y experiencia → índice de proyectos.

## DIG-W07 · Contacto
**H2:** ¿Necesitas revisar, automatizar o integrar un sistema?
**Texto:** Cuéntanos qué equipos o procesos intervienen, cómo funcionan actualmente y qué necesitas resolver. Valoraremos la información inicial para definir el posible alcance técnico y los siguientes pasos.
**CTA:** Cuéntanos tu proyecto → Contacto.

## Navegación, diseño y SEO
- Ruta principal: Capacidades → Automatización y control → necesidades → ámbito → entregables → Contacto.
- Rutas cruzadas: desde Infraestructuras (BMS/instalaciones) y Sistemas energéticos (EMS/PPC) hacia los ámbitos 3 o 6.
- Anclas: #necesidades, #ambitos, #entregables, #integracion.
- Seis tarjetas equilibradas en cuadrícula 2×3 en escritorio, una columna en móvil; bloque transversal a ancho completo. Etiquetas técnicas secundarias; no desplegar 22 servicios ni usar acrónimos como únicos títulos.
- CTA principal en cabecera y cierre; enlaces contextuales a INF, ENE y experiencia.
- SEO title: Automatización y control de instalaciones y procesos | BAFRAS Engineering
- Meta description: Ingeniería de instrumentación, PLC/DDC, SCADA, BMS, integración OT y software técnico para instalaciones y procesos.
- Imágenes: reales o licenciadas; no presentar imágenes de terceros como proyectos propios.

## Auditoría de cobertura y límites (uso interno, no publicar)
| Familia pública | Fichas DIG representadas | Frontera |
|---|---|---|
| Instrumentación y telemetría | DIG-01, DIG-11 | Medición ≠ telecontrol; ENE-03 estrategia de medida energética |
| Automatización y programación | DIG-02, DIG-10 | Ingeniería funcional ≠ programación específica |
| Supervisión | DIG-04, DIG-05 | SCADA/HMI/BMS ≠ controladores; diseño térmico INF |
| Integración OT | DIG-03, DIG-06, DIG-20 | Protocolos ≠ red OT ≠ API; seguridad solo requisitos de diseño |
| Software técnico y datos | DIG-07, DIG-08, DIG-16, DIG-17, DIG-19 | Analítica ≠ aplicación ≠ simulación ≠ optimización; no IA/ML |
| Activos energéticos | DIG-12 | Implementación EMS/PPC ≠ estrategia ENE-08 |
| Transversal | DIG-09, DIG-14, DIG-22 | Pruebas, modernización y soporte acotados |

**Registros redirigidos:** DIG-13 → DIG-03; DIG-15 → DIG-07; DIG-21 → STD-QA; no son ofertas autónomas. **Registro futuro excluido:** DIG-18 (IA/ML, NO_PUBLICAR). La correspondencia cubre los 18 registros DIG activos no redirigidos y deja los otros cuatro explícitamente tratados. **Advertencia:** los estados PENDIENTE_PUBLICACION de las fichas de la taxonomía requieren aprobación de publicación separada; la aprobación editorial de esta página no los modifica.

**Dictamen final:** cobertura editorial suficiente, seis funciones distintas, sin duplicación de servicios entre INF/ENE/DIG, densidad reducida frente a V1.0. Página cerrada editorialmente; implementación, traducciones, evidencias y autorización de publicación pendientes.



---

# PARTE F — SECTORES · V1.1 APROBADA EDITORIALMENTE

# Documento 03 · Iteración 03.G.2 — Sectores V1.1
**Estado:** propuesta auditada para validación editorial; no aprobada aún. **Base:** Documento 03 V1.9, Documento 02 (S01–S20, aplicaciones y reglas de evidencia), Documento 01 (servicios ofertables).

## Dictamen multidisciplinar
- **Dirección y comercial:** priorizar contextos de compra comprensibles; turismo e industria primero como hipótesis de foco, no como afirmación de experiencia o demanda contrastada.
- **Ingeniería:** evitar equiparar sector con competencia acreditada o referencias ejecutadas; no prometer continuidad, ahorros ni capacidades reguladas.
- **UX:** mantener seis entradas, reducir textos y evitar tres enlaces de capacidad repetidos en cada tarjeta; navegación mediante anclas y un enlace contextual principal por grupo.
- **SEO:** títulos con términos que busca el comprador, sin generar subpáginas sectoriales superficiales.
- **Marca:** lenguaje orientado a problemas, sobrio y verificable; no mostrar fotos de proyectos ajenos como propios.

## Hallazgos y cambios respecto a V1.0
1. El grupo «Energía, tecnología y entornos especializados» mezclaba comunidades energéticas, centros de datos y residencial premium, sin criterio compartido. **Se mueve S20 al grupo de edificación** y se renombra el sexto como «Comunidades energéticas e infraestructuras tecnológicas» (S18–S19).
2. «Edificación, rehabilitación y gestión de activos» mezclaba tipologías con perfiles de comprador, pero el punto común es **promover, reformar o gestionar un inmueble**. Se amplía explícitamente a residencial (S20). Promotores, instaladoras y estudios técnicos aparecen también en la sección de colaboración, sin duplicar como sector independiente.
3. Se elimina la introducción redundante SEC-02; se integra la explicación en el hero y en una frase antes de tarjetas.
4. Las seis tarjetas se reducen a **situación operativa + ejemplos reconocibles + enlace principal**. Se evitan catálogos de servicios y CTA repetidos.
5. Se mantiene una sección breve de problemas transversales y colaboración, porque aportan rutas alternativas al visitante que no se reconoce en un grupo.
6. No se presenta la clasificación como cartera de clientes o experiencia demostrada. Orden comercial provisional sujeto a revisión con oportunidades reales.

# Contenido web publicable propuesto

## SEC-01 · Hero
**Eyebrow:** SECTORES
**H1:** Ingeniería para edificios, industria e infraestructuras.
**Texto:** Cada actividad plantea condiciones distintas de uso, operación y mantenimiento. Aplicamos nuestras capacidades en instalaciones, energía y automatización para estudiar necesidades concretas y definir soluciones ajustadas al contexto de cada proyecto.
**CTA principal:** Explorar sectores → #sectores
**CTA secundario:** Cuéntanos tu proyecto → Contacto

## SEC-02 · Sectores
**H2:** Entendemos el entorno antes de definir la actuación.
**Introducción:** Estos son algunos de los ámbitos en los que podemos aportar ingeniería. Los ejemplos describen necesidades que podemos estudiar; no son referencias de proyectos ejecutados.

### 1. Turismo, comercio y edificios terciarios
**Texto:** Hoteles, alojamientos, oficinas y comercios necesitan mantener el confort y la actividad mientras gestionan instalaciones y costes operativos. Estudiamos, por ejemplo, el funcionamiento de la climatización, las reformas en edificios en uso y las oportunidades de mejora energética.
**Ejemplos breves:** Climatización y ACS · Consumos y autoconsumo · Supervisión de instalaciones.
**Enlace contextual:** Explorar Sistemas energéticos → Sistemas energéticos.

### 2. Industria, logística y agroindustria
**Texto:** En plantas productivas, almacenes y actividades agroindustriales, las decisiones sobre instalaciones y control afectan al proceso. Podemos analizar consumos, servicios auxiliares, refrigeración, bombeos y necesidades de instrumentación o automatización.
**Ejemplos breves:** Picos de demanda · Frío y bombeos · Integración de equipos.
**Enlace contextual:** Explorar Automatización y control → Automatización y control.

### 3. Infraestructuras y servicios públicos
**Texto:** Las instalaciones municipales, las redes de agua y los servicios urbanos requieren criterios de operación, mantenimiento y renovación. Abordamos estudios y proyectos de instalaciones, energía y telecontrol, considerando las condiciones de cada organismo o gestor.
**Ejemplos breves:** Alumbrado · Redes hidráulicas · Telemetría y telecontrol.
**Enlace contextual:** Explorar Infraestructuras e instalaciones → Infraestructuras e instalaciones.

### 4. Salud, educación y equipamientos
**Texto:** Centros sanitarios, residencias, campus y espacios deportivos o culturales combinan ocupación variable, exigencias de confort y continuidad de uso. Estudiamos instalaciones térmicas y eléctricas, consumo energético y sistemas de supervisión.
**Ejemplos breves:** Ventilación · Producción térmica · Renovación por fases.
**Enlace contextual:** Explorar Infraestructuras e instalaciones → Infraestructuras e instalaciones.

### 5. Edificación, rehabilitación y activos inmobiliarios
**Texto:** En obra nueva, rehabilitación, edificios gestionados y vivienda residencial, es importante coordinar las instalaciones con el uso, el presupuesto y las restricciones de ejecución. Colaboramos en estudios, diseño y revisión técnica de instalaciones y soluciones energéticas.
**Ejemplos breves:** Coordinación de instalaciones · Reformas · Fotovoltaica y electrificación.
**Enlace contextual:** Explorar Infraestructuras e instalaciones → Infraestructuras e instalaciones.

### 6. Comunidades energéticas e infraestructuras tecnológicas
**Texto:** Las comunidades energéticas y las instalaciones tecnológicas plantean retos diferentes, pero ambas requieren decisiones rigurosas sobre suministro, medida e integración. Podemos estudiar autoconsumo compartido y almacenamiento, o necesidades de alimentación, refrigeración y supervisión de equipos críticos, según el caso.
**Ejemplos breves:** Autoconsumo colectivo · Continuidad eléctrica · Monitorización.
**Enlace contextual:** Explorar Sistemas energéticos → Sistemas energéticos.

## SEC-03 · Problemas que atraviesan sectores
**H2:** ¿Tu necesidad no encaja en una categoría?
**Texto:** Una instalación que no rinde como debería, una inversión energética por evaluar o varios equipos que no intercambian datos pueden aparecer en actividades muy distintas. Partimos del problema técnico y definimos qué especialidades hacen falta.
**Enlace:** Ver nuestras capacidades → Capacidades.

## SEC-04 · Colaboración profesional
**H2:** Ingeniería también para equipos de proyecto.
**Texto:** Colaboramos con promotores, gestores de instalaciones, estudios de arquitectura e ingeniería, constructoras e instaladoras en trabajos concretos de estudio, proyecto, diagnóstico y asistencia técnica. Acordamos entregables, coordinación y responsabilidades para cada colaboración.
**Enlace:** Conoce BAFRAS → Sobre BAFRAS.

## SEC-05 · Contacto
**H2:** Cuéntanos qué necesitas resolver.
**Texto:** Indícanos el tipo de actividad o instalación, el estado del proyecto y la decisión o problema que quieres abordar. Valoraremos qué información necesitamos para concretar el siguiente paso.
**CTA:** Cuéntanos tu proyecto → Contacto.

# UX y publicación (interno)
- URL `/sectores/`; seis tarjetas en 2 columnas × 3 filas en escritorio, una columna en móvil. No carrusel: permite comparar los seis ámbitos sin ocultarlos.
- Cada tarjeta: título, 2 frases, línea de ejemplos y un enlace principal a capacidad. No tres enlaces repetidos por tarjeta.
- Anclas opcionales de navegación al comienzo, con etiquetas abreviadas: Turismo y terciario; Industria y logística; Servicios públicos; Salud y educación; Edificación; Energía y tecnología. Evitar duplicar tarjetas como menú si el espacio móvil es reducido.
- Un CTA contacto en hero y uno al final. No añadir CTA comercial dentro de cada tarjeta.
- SEO title: Sectores de ingeniería | Edificios, industria y energía | BAFRAS.
- Meta description: Ingeniería de instalaciones, sistemas energéticos y automatización para hoteles, industria, servicios públicos, equipamientos y edificios.
- Imágenes: utilizar fotografías genéricas con licencia y sin insinuar trabajos realizados, o iconografía uniforme; preferencia UX por iconografía uniforme en las seis tarjetas para reducir altura y evitar atribución implícita.
- Prioridad visual: orden editorial de lectura, no etiquetas de «sector líder» ni ranking comercial.

## Matriz de cobertura interna
| Grupo | IDs del Documento 02 | Nº |
|---|---|---:|
| Turismo, comercio y edificios terciarios | S02, S07, S09 | 3 |
| Industria, logística y agroindustria | S03, S08, S10 | 3 |
| Infraestructuras y servicios públicos | S01, S11, S12, S13 | 4 |
| Salud, educación y equipamientos | S15, S16, S17 | 3 |
| Edificación, rehabilitación y activos inmobiliarios | S04, S05, S06, S14, S20 | 5 |
| Comunidades energéticas e infraestructuras tecnológicas | S18, S19 | 2 |
**Total: 20/20 sectores, sin duplicaciones.** La agrupación 6 es un contenedor de navegación, no una afirmación de equivalencia técnica entre comunidades energéticas y centros de datos.

## Riesgo residual y recomendación
El sexto grupo sigue siendo heterogéneo por naturaleza, pero reúne dos nichos de menor volumen dentro del inventario y evita crear una séptima tarjeta desequilibrada. Si la estrategia comercial prioriza uno de ellos, será preferible crear una página sectorial específica más adelante, con contenido y evidencias reales, no forzar el índice actual. **Recomendación del equipo: aprobar V1.1 como base publicable, pendiente de conformidad del usuario y validación de derechos visuales.**


---

## PARTE G — PROYECTOS Y EXPERIENCIA (arquitectura aprobada; referencias no publicables sin verificación)

# PARTE G — PROYECTOS Y EXPERIENCIA · ITERACIÓN 03.H.2 V1.1 (ARQUITECTURA APROBADA; EVIDENCIAS PENDIENTES)

# Documento 03 · Iteración 03.H.2 — Proyectos y experiencia V1.1

**Estado:** arquitectura editorial V1.1 aprobada por el usuario el 02/11/2026. Referencias y atribuciones no verificadas; no aptas todavía para publicación como cartera de proyectos ejecutados.

## Decisiones del equipo multidisciplinar
- Mantener seis referencias candidatas en tres áreas, con tres destacadas (Formentor, eólico, transición energética UIB) sujetas a evidencia.
- Sustituir la descripción acumulativa de sistemas por el esquema **contexto → reto → intervención acreditada → fases y entregables → resultado documentado**.
- El índice presenta un máximo de 2-3 frases por tarjeta y 2-4 etiquetas verificadas; las listas técnicas completas se reservan a fichas.
- Eliminar la sección independiente de cuatro fases genéricas; incorporar fases verificadas en cada referencia.
- Distinguir claramente **Experiencia profesional previa del equipo** de **Proyecto contratado por BAFRAS**. No insinuar autoría corporativa sobre trabajos previos.
- Mantener tres grupos visibles con anclas, sin filtros complejos. No activar enlaces a fichas hasta tener contenido contrastado.
- Imágenes: propias autorizadas o ilustraciones neutrales inequívocamente identificadas; no presentar fotografías genéricas como evidencia.

## COPY WEB PROPUESTO — ES

### PE-01 · Hero
**Eyebrow:** PROYECTOS Y EXPERIENCIA

**H1:** Experiencia aplicada a instalaciones, energía y sistemas de control.

**Texto:** Reunimos referencias de la trayectoria profesional del equipo en edificios, infraestructuras energéticas y sistemas de automatización. Cada proyecto plantea retos distintos; por eso ponemos el foco en el contexto técnico, el trabajo realizado y la participación concreta de nuestros profesionales.

**Nota de atribución visible junto al índice:** Las referencias de experiencia profesional previa se distinguen de los encargos desarrollados directamente por BAFRAS.

### PE-02 · Referencias
**H2:** Experiencia en proyectos de distinta naturaleza.

**Intro:** Seleccionamos actuaciones que ayudan a comprender el tipo de sistemas y retos técnicos en los que ha participado el equipo.

#### Infraestructuras e instalaciones
**Introducción:** Instalaciones eléctricas y mecánicas en edificios con exigencias diferentes de confort, operación y coordinación de obra.

**Referencia destacada — Complejo hotelero · Formentor, Mallorca**
*Texto provisional, condicionado a ficha:* Ingeniería de instalaciones en un complejo hotelero donde conviven múltiples sistemas técnicos y requisitos de integración arquitectónica, confort y operación. La ficha concretará los sistemas abordados y la participación efectiva del profesional.

**Referencia complementaria — Centro educativo · Mallorca**
*Texto provisional:* Instalaciones de un equipamiento docente, con especial atención a las condiciones de ocupación, ventilación, seguridad y mantenimiento. Pendiente de confirmar instalaciones, función y fases de participación.

**Referencia complementaria — Residencia de alta gama · Ibiza**
*Texto provisional:* Integración de instalaciones técnicas en una vivienda singular, coordinando las exigencias de confort con el diseño arquitectónico. Pendiente de confirmar sistemas, alcance y fases.

#### Automatización y control
**Introducción:** Comunicaciones, regulación, supervisión y software técnico para sistemas que necesitan operar de forma coordinada.

**Referencia destacada — Control y software para sistemas eólicos**
*Texto provisional:* Experiencia en definición de comunicaciones y funciones de control de instalaciones eólicas y desarrollo de herramientas de seguimiento y mantenimiento de aerogeneradores. Se confirmará si son uno o varios proyectos, los protocolos utilizados y los módulos realmente desarrollados.

**Referencia complementaria — Diagnóstico de control HVAC · UIB**
*Texto provisional:* Revisión del funcionamiento de instalaciones térmicas y de sus sistemas de regulación y supervisión, con análisis de señales, equipos y secuencias para identificar incidencias y estudiar mejoras. No atribuir implantación de nuevos sistemas sin evidencia.

#### Sistemas energéticos
**Introducción:** Estudios, ingeniería y documentación técnica para integrar generación, almacenamiento y nuevas infraestructuras energéticas.

**Referencia destacada — Transformación energética del campus · UIB**
*Texto provisional:* Participación profesional en actuaciones técnicas vinculadas a la transformación energética del campus universitario: generación fotovoltaica, almacenamiento, infraestructura eléctrica, recarga y sistemas de medida y control. La ficha distinguirá estudios, ingeniería, pliegos técnicos y tareas de coordinación efectivamente realizadas.

### PE-03 · Cómo documentamos la experiencia
**H2:** La intervención concreta importa.

**Texto:** En cada referencia identificaremos el contexto del proyecto, la función desempeñada, los sistemas abordados y las fases de participación. Cuando existan datos contrastados, incorporaremos entregables, resultados y material gráfico autorizado.

### PE-04 · Contacto
**H2:** ¿Tu proyecto plantea retos similares?

**Texto:** Cuéntanos qué instalación o sistema necesitas desarrollar, revisar o integrar. Valoraremos qué experiencia y capacidades pueden resultar relevantes para tu encargo.

**CTA principal:** Cuéntanos tu proyecto → Contacto.
**Enlace secundario:** Explorar capacidades → Capacidades.

## Diseño de tarjeta del índice (especificación interna)
1. Categoría: INF / DIG / ENE, en lenguaje público.
2. Nombre de referencia, ubicación solo si verificable y publicable.
3. Descripción: máximo 35-45 palabras, orientada a contexto e intervención.
4. Etiqueta obligatoria: «Experiencia profesional previa» o «Proyecto BAFRAS», cuando se confirme.
5. Rol, fases y tecnologías: solo cuando estén acreditados; no usar etiquetas vacías ni valores supuestos.
6. Enlace «Ver proyecto»: únicamente si existe ficha contrastada; de lo contrario, tarjeta sin enlace.

## Estructura de ficha detallada (plantilla interna, no publicable sin evidencia)
- Identificación: nombre autorizado, ubicación, tipo de activo, periodo y contexto contractual.
- Atribución: profesional, empresa/organización en la que participó, rol y límites de responsabilidad.
- Necesidad/reto: problema real, restricciones y criterios de éxito.
- Sistemas e interfaces: instalaciones y equipos efectivamente incluidos; arquitectura y protocolos comprobados.
- Intervención: estudios, diseño, coordinación, desarrollo, dirección, pruebas o puesta en marcha **solo si consta**.
- Entregables: cálculos, planos, pliegos, software, protocolos, informes o registros acreditados.
- Resultados: solo datos documentados, con alcance y fuente; si no hay cifras, explicar la intervención sin inventarlas.
- Imágenes, nombres, logos y permisos de publicación.

## Matriz interna de ampliación técnica — NO publicar como hechos sin fichas

**Formentor:** verificar electricidad BT/MT, CT, alumbrado, climatización y producción térmica, ventilación, ACS, bombeos, saneamiento, PCI, BMS y telecomunicaciones; fases posibles: proyecto, coordinación MEP/BIM, seguimiento de obra, pruebas y recepción. No atribuirlas automáticamente.

**Centro educativo:** verificar ventilación y calidad del aire, climatización, iluminación, BT, ACS, saneamiento, PCI, control; fases de diseño, cálculos, documentación y asistencia técnica.

**Ibiza:** verificar climatización zonificada, ventilación, iluminación, ACS, hidráulica, domótica, piscina y tratamiento de agua si existen; fases de coordinación con arquitectura, proyecto, ejecución y puesta en marcha.

**Eólico:** distinguir diseño de comunicaciones y protocolos, lazos de control, SCADA, software de mantenimiento, FAT/SAT y commissioning; no atribuir control de pitch/yaw ni regulación de potencia sin documentación. Separar en dos referencias si fueron proyectos distintos.

**HVAC UIB:** sistemas de cuatro tubos, intercambiadores, bombeo con VFD, válvulas, fan coils, DDC, comunicaciones y supervisión. Distinguir diagnóstico y propuestas de cambios realmente implementados.

**Transición energética UIB:** separar programa institucional de contribución personal: análisis de demanda, FV, BESS, recarga, infraestructura MT/BT, medida/SCADA, documentación de contratación pública, pliegos, presupuestos, coordinación y seguimiento; no atribuir dirección facultativa ni resultados agregados sin respaldo.

## UX y SEO
- Tres anclas: Instalaciones · Automatización y control · Sistemas energéticos.
- Tres referencias destacadas en composición de mayor peso; otras tres en tarjetas compactas. En móvil, una sola columna.
- No añadir fotografías grandes sin material real; preferir diagramas técnicos anonimizados o visual neutro claramente ilustrativo.
- SEO: título «Proyectos y experiencia en ingeniería | BAFRAS Engineering»; descripción centrada en instalaciones, energía y automatización; evitar nombres de clientes no autorizados.
- Recorrido: Capacidades/Sectores → referencia → Contacto, con vuelta a la capacidad asociada.

## Puertas de publicación
**Pendiente:** ficha Àngel (Formentor, instituto, Ibiza); ficha Amin (parque eólico y software); ficha Murti (UIB energía y HVAC); atribución y periodos; fases y entregables; autorización de denominaciones, imágenes y datos; revisión final de referencias.

**Decisión editorial:** arquitectura V1.1 lista para revisión; copy de referencias sigue provisional. No cerrar para publicación hasta verificar hechos.



## PARTE H — SOBRE BAFRAS Y CONTACTO (V1.1 APROBADAS EDITORIALMENTE)

# Documento 03 — Iteración 03.I.2 · Sobre BAFRAS y Contacto V1.1
**Estado:** revisión comercial B2B, credibilidad y conversión aprobada editorialmente por el usuario el 02/11/2026. Datos de equipo, contactos y funcionamiento del formulario pendientes de verificación e implementación.

## Dictamen multidisciplinar (revisión simulada)
- Dirección: dar prioridad a quién forma el equipo, en qué es competente y cómo se organiza; evitar una página basada únicamente en valores abstractos.
- Comercial B2B: establecer señales de confianza verificables (personas, especialización, experiencia previa correctamente atribuida, entregables y forma de colaboración).
- Ingeniería: no equiparar disciplinas cubiertas con habilitaciones individuales; describir el método sin prometer ejecutar todas las fases en todos los encargos.
- UX: hero concreto, presentación del equipo temprana, filosofía condensada, método breve, prueba de experiencia y CTA.
- Marca: tono técnico, próximo y sobrio; sin superlativos, cifras, clientes o acreditaciones no confirmados.
- Conversión, legal y software: cuatro campos de baja fricción, orientación opcional, alternativa email, accesibilidad, privacidad, antispam y medición sin datos personales.

# PÁGINA «SOBRE BAFRAS» — COPY WEB ES V1.1

## SB-01 · Hero
**Eyebrow:** SOBRE BAFRAS
**H1:** Ingeniería con visión técnica y disciplinas complementarias.

BAFRAS Engineering reúne perfiles profesionales vinculados a las instalaciones e infraestructuras, los sistemas energéticos y la automatización y control. Abordamos cada encargo desde sus necesidades reales, con atención al funcionamiento de las instalaciones, los condicionantes del proyecto y la coordinación entre especialidades.

**Enlace contextual:** Conoce nuestra experiencia → Proyectos y experiencia.

## SB-02 · El equipo
**H2:** Profesionales con experiencias que se complementan.

La combinación de trayectorias en instalaciones de edificios, infraestructuras energéticas y sistemas de control permite estudiar problemas desde diferentes perspectivas. Cada proyecto requiere definir quién interviene, con qué responsabilidades y qué especialidades deben coordinarse.

**Componente de publicación: tres fichas de fundador (pendiente de validación de datos):**
- **Murti** — área de referencia propuesta: sistemas energéticos, análisis técnico e integración de sistemas. Validar denominación profesional, titulaciones, rol y referencias autorizadas.
- **Àngel** — área de referencia propuesta: infraestructuras e instalaciones en edificación. Validar especialización, titulaciones, rol y proyectos autorizados.
- **Amin** — área de referencia propuesta: automatización, control y software técnico. Validar especialización, titulaciones, rol y experiencias autorizadas.

**Plantilla de ficha visible:** Nombre · Especialización verificada (una línea) · Dos líneas de experiencia contrastada · Enlace a referencias relacionadas. Fotografía real y autorizada o diseño tipográfico neutro; no usar retratos generados. No atribuir a BAFRAS los encargos previos de sus fundadores.

## SB-03 · Nuestra forma de trabajar
**H2:** Primero entender. Después definir la actuación.

Un mismo síntoma puede tener distintas causas, y una solución técnicamente posible no siempre es la más adecuada para una instalación. Revisamos el contexto, contrastamos los datos disponibles y definimos un alcance proporcionado al objetivo del cliente.

**Entender el contexto.** Identificar necesidades, funcionamiento y restricciones.
**Evaluar alternativas.** Contrastar criterios técnicos y opciones viables cuando corresponda.
**Desarrollar el alcance.** Preparar los estudios, proyectos, especificaciones o integraciones contratados.
**Verificar y documentar.** Comprobar los aspectos incluidos en el encargo y entregar documentación utilizable.

No todas estas etapas forman parte de todos los contratos.

## SB-04 · Experiencia y colaboración
**H2:** Experiencia profesional aplicada a proyectos reales.

La trayectoria del equipo incluye experiencias relacionadas con instalaciones en edificación, sistemas de control industrial e infraestructuras energéticas. Las referencias se presentan con su contexto y, cuando estén verificadas, con las funciones concretas desempeñadas por cada profesional.

También colaboramos con promotores, responsables técnicos, ingenierías, estudios de arquitectura, constructoras e instaladoras, delimitando las interfaces y responsabilidades de cada participación.

**Enlace:** Ver proyectos y experiencia → Proyectos y experiencia.

## SB-05 · Cierre
**H2:** Hablemos de tu proyecto.

Si necesitas estudiar una instalación, desarrollar una actuación técnica o coordinar distintas especialidades, podemos valorar contigo el alcance del trabajo.

**CTA principal:** Cuéntanos tu proyecto → Contacto.
**CTA secundario:** Explorar capacidades → Capacidades.

## UX y SEO Sobre BAFRAS
**Orden:** Hero → equipo → forma de trabajar → experiencia y colaboración → contacto. Las fichas no deben convertirse en CV extensos. No presentar la metodología como certificación de calidad. 
**Title:** Sobre BAFRAS | Equipo e ingeniería multidisciplinar
**Meta description:** Conoce el equipo y la forma de trabajar de BAFRAS Engineering en instalaciones, sistemas energéticos y automatización y control.

# PÁGINA «CONTACTO» — COPY WEB ES V1.1

## CO-01 · Hero
**Eyebrow:** CONTACTO
**H1:** Hablemos de tu proyecto.

Explícanos brevemente qué necesitas resolver, tanto si estás definiendo una actuación como si ya dispones de planos, datos o documentación técnica. Revisaremos tu consulta para valorar si podemos ayudarte y qué información convendría analizar a continuación.

## CO-02 · Formulario
**H2:** Envíanos tu consulta.

**Campo 1:** Nombre * — etiqueta persistente.
**Campo 2:** Empresa u organización — opcional.
**Campo 3:** Correo electrónico * — formato email.
**Campo 4:** Cuéntanos qué necesitas * — textarea con ayuda: «Puedes indicar el tipo de instalación o actividad, el problema o actuación prevista, la ubicación y la fase del proyecto. No necesitas tener todos los datos.»

**Botón:** Enviar consulta.
**Información de privacidad:** texto breve y enlace real a política de privacidad; base jurídica y eventual casilla de consentimiento determinadas tras revisión legal. No exigir una aceptación genérica si la base jurídica adecuada no es el consentimiento.

**Mensaje de éxito (solo tras confirmación del servidor):** Tu consulta se ha enviado correctamente. Revisaremos la información y contactaremos contigo si podemos avanzar con el encargo.
**Mensaje de error:** No se ha podido enviar tu consulta. Puedes intentarlo de nuevo o escribirnos directamente al correo indicado en esta página.

No solicitar sector, presupuesto, teléfono, fecha límite ni servicio como obligatorios. Sin archivos adjuntos en primera versión; canal posterior para documentación. No prometer respuesta en 24 h ni reunión gratuita automática.

## CO-03 · Alternativa directa
**H2:** ¿Prefieres escribirnos directamente?

Puedes contactar por correo electrónico y describir el proyecto con el nivel de detalle que tengas disponible.

**Correo corporativo:** [PENDIENTE DE CONFIRMAR; ocultar bloque hasta disponer de dirección real].
**Ubicación / ámbito de actuación:** [PENDIENTE DE VALIDAR; no afirmar domicilio u oficina abierta al público].

Si todavía no existe un correo operativo, no publicar una alternativa ficticia; el formulario solo debe activarse cuando exista un receptor funcional y probado.

## CO-04 · Cierre contextual
**H2:** No necesitas tenerlo todo definido.

Una descripción inicial puede ser suficiente para identificar la especialidad adecuada y determinar qué información habría que revisar antes de concretar un alcance.

## Conversión, accesibilidad y tecnología
- **Jerarquía visual:** en escritorio, formulario en columna principal y correo/nota de orientación en columna secundaria; en móvil, hero → formulario → contacto alternativo. Sin CTA adicional que compita con «Enviar consulta».
- **Fricción:** cuatro campos; solo tres obligatorios; empresa opcional; sin selector obligatorio de sector. Etiquetas persistentes, indicadores de obligatorio y ayuda legible.
- **Errores:** validación en cliente y servidor, mensajes asociados a campos, conservación de datos tras fallo, estados de carga y prevención de envíos duplicados.
- **Privacidad:** minimización, información RGPD, política real, retención definida, transporte seguro, control de acceso y antispam respetuoso con la privacidad; revisión legal previa.
- **Entrega:** enviar a buzón corporativo verificado, registrar fallo sin almacenar texto sensible en logs, probar éxito y error; no mostrar éxito hasta confirmación real.
- **Medición:** evento de envío confirmado y, si es posible, consultas cualificadas agregadas; nunca contenido del mensaje, nombre o email en analítica.
- **No promesas:** no publicar SLA, horario o teléfono sin decisión operativa.

**Title:** Contacto | BAFRAS Engineering
**Meta description:** Contacta con BAFRAS Engineering para plantear un proyecto de instalaciones, energía o automatización. Cuéntanos qué necesitas resolver.

# Matriz de decisiones y verificaciones
| Elemento | Decisión editorial | Condición antes de publicar |
|---|---|---|
| Equipo | Tres fichas visibles, breves y con enlaces a experiencia | Nombres, roles, titulaciones, fotos y referencias contrastados |
| Trayectoria | Experiencia de profesionales, no portfolio corporativo atribuido | Verificación de participación y permisos |
| Método | Cuatro principios operativos, no promesa de servicio integral | Alcance real de cada contrato |
| Formulario | Nombre, empresa opcional, email y consulta | Backend, destinatario, prueba E2E y privacidad |
| Contacto alternativo | Correo directo visible | Buzón corporativo confirmado |
| Conversión | Medir envío real, no clic | Analítica sin PII y cumplimiento |
| Idiomas | ES, CA, EN, DE | Traducción y revisión editorial |

**Estado:** V1.1 aprobada editorialmente por el usuario el 02/11/2026. No se consideran verificadas las biografías, las referencias de los socios ni los datos de contacto.


---

# PARTE I — AUDITORÍA TRANSVERSAL 03.J (IMPLEMENTACIÓN CONDICIONADA)

# BAFRAS Engineering — Documento 03 · Iteración 03.J
## Auditoría transversal de coherencia, navegación, SEO y preparación para implementación · V1.0
**Fecha:** 2026-11-02  
**Alcance:** contenido consolidado V1.14, aprobación posterior de «Sobre BAFRAS» y «Contacto», arquitectura de «Proyectos y experiencia» V1.1, y criterios editoriales registrados en el Documento 03.  
**Método:** revisión simulada desde dirección, comercial B2B, ingeniería INF/ENE/DIG, UX/accesibilidad, SEO/i18n, desarrollo web, legal/privacidad y calidad. **No** es una auditoría de una web desplegada ni prueba de código.  
**Dictamen:** arquitectura editorial apta para iniciar implementación **con condiciones**. No está lista para publicación sin resolver bloqueos P0.

## 1. Inventario y estado editorial real
| Ruta conceptual | Estado editorial | Estado de publicación |
|---|---|---|
| Inicio | Aprobada | Pendiente de implementación, activos y revisión |
| Capacidades | Aprobada | Pendiente |
| Infraestructuras e instalaciones | Aprobada | Pendiente de validar alcance operativo |
| Sistemas energéticos | Aprobada | Pendiente de validar alcance operativo |
| Automatización y control | Aprobada | Pendiente de validar alcance operativo; DIG-18 IA/ML no ofertable |
| Sectores | Aprobada | Pendiente de revisión de claims, visuales y enlaces |
| Proyectos y experiencia | **Arquitectura** aprobada | **Bloqueada** para referencias concretas hasta evidencias y permisos |
| Sobre BAFRAS | Aprobada | Fichas personales y credenciales pendientes de confirmar |
| Contacto | Aprobada | **Bloqueada** hasta backend, receptor, privacidad y pruebas |
| Fichas de proyecto (hasta 3 inicialmente) | Plantilla definida | No generar páginas públicas vacías |
| Aviso legal, privacidad y cookies | No redactadas/validadas aquí | Requisito legal según implementación y tratamiento real |

**Recuento:** nueve páginas editoriales principales si se cuentan las tres capacidades específicas; seis entradas en menú superior. No confundir aprobación de copy con habilitación comercial, legal o técnica de publicación.

## 2. Coherencia estratégica y editorial
**Resultado: satisfactorio con correcciones de metadatos y estados.** La secuencia global es consistente: necesidad → análisis → alcance → entregable → contacto. INF trata instalaciones y coordinación física; ENE estudia demanda, generación, almacenamiento y estrategia energética; DIG aborda instrumentación, control, integración y software técnico. La frontera crítica EMS/PPC es **estrategia/estudio energético en ENE** frente a **implementación funcional de control en DIG**. BMS: instalación y coordinación técnica en INF frente a arquitectura/programación/supervisión en DIG. HVAC: proyecto mecánico INF, rendimiento energético ENE y control/diagnóstico DIG. Enlazar entre capacidades cuando el contexto lo justifique, no duplicar párrafos.

**Inconsistencias internas a sanear:** algunos encabezados heredados del consolidado describen versiones ya aprobadas como «pendientes» (por ejemplo, encabezados de ENE y Sectores). El estado rector al principio del documento prevalece; limpiar etiquetas históricas en una edición editorial posterior sin alterar el copy aprobado. En Proyectos, el copy provisional no debe confundirse con una referencia autorizada. Las notas «pendiente de validar», matrices internas y textos entre corchetes **no** deben llegar al HTML público.

**Señales B2B:** las tres especialidades se explican por problemas reconocibles, no por promesas de resultados. «Sobre BAFRAS» aporta personas y método; «Proyectos y experiencia» debe aportar evidencias, no duplicar currículos. «Contacto» evita pedir presupuesto/urgencia/teléfono obligatorios. No publicar frases sobre ahorros garantizados, servicio 24/7, certificaciones, habilitaciones o autoría corporativa de proyectos previos sin prueba.

## 3. Arquitectura de información y navegación
### 3.1 Rutas canónicas propuestas (decisión técnica pendiente de confirmar)
| Menú / página | Slug ES propuesto | Navegación principal |
|---|---|---|
| Inicio | `/es/` | Inicio |
| Capacidades | `/es/capacidades/` | Capacidades |
| Infraestructuras e instalaciones | `/es/capacidades/infraestructuras-instalaciones/` | Submenú Capacidades |
| Sistemas energéticos | `/es/capacidades/sistemas-energeticos/` | Submenú Capacidades |
| Automatización y control | `/es/capacidades/automatizacion-control/` | Submenú Capacidades |
| Sectores | `/es/sectores/` | Sectores |
| Proyectos y experiencia | `/es/proyectos-experiencia/` | Proyectos y experiencia |
| Sobre BAFRAS | `/es/sobre-bafras/` | Sobre BAFRAS |
| Contacto | `/es/contacto/` | Contacto |

**Nota:** son propuestas, no URLs implementadas. El selector de idioma debe preservar la página equivalente cuando exista. Definir redirección de `/` a idioma predeterminado o negociación explícita; no usar detección automática opaca que impida indexar idiomas. No inventar rutas de proyectos antes de disponer de fichas.

### 3.2 Matriz mínima de enlaces y CTA
| Origen | Enlace principal | Enlaces de apoyo |
|---|---|---|
| Inicio | Contacto | Capacidades; necesidades → INF/ENE/DIG; experiencia |
| Capacidades | Cada una de las tres capacidades | Contacto |
| INF | Contacto | ENE/DIG contextuales; experiencia |
| ENE | Contacto | INF/DIG contextuales; experiencia |
| DIG | Contacto | INF/ENE contextuales; experiencia |
| Sectores | Explorar sectores (ancla) | Una capacidad relevante por grupo; Contacto |
| Proyectos y experiencia | Contacto | Capacidades; ficha **solo si verificada** |
| Sobre BAFRAS | Contacto | Experiencia; Capacidades |
| Contacto | Enviar consulta | Correo alternativo verificado; privacidad |

**Reglas UX:** una navegación primaria coherente, menú móvil accesible, estado activo, breadcrumbs en capacidades y futuras fichas, anclas existentes con offset para cabecera fija, footer con navegación/legal/contacto, CTA con texto consistente «Cuéntanos tu proyecto» en las páginas informativas. En Contacto el único CTA de formulario es «Enviar consulta». Evitar enlaces a secciones aún no publicadas; no convertir las seis tarjetas sectoriales en subpáginas sin contenido.

## 4. SEO e internacionalización
**Base editorial:** títulos y metadescripciones existen en varias páginas; deben compilarse en un registro único por ruta. Cada página requiere `title` único, `meta description` no duplicada, un H1, jerarquía H2/H3, URL canónica absoluta, etiquetas Open Graph y un `lang` correcto. No hay evidencia de pruebas sobre HTML final.

**Mapa de intención:** Inicio: ingeniería multidisciplinar; Capacidades: oferta general; INF: instalaciones eléctricas/mecánicas; ENE: eficiencia, fotovoltaica, almacenamiento y sistemas; DIG: automatización, SCADA/BMS e integración; Sectores: aplicaciones por actividad; Experiencia: referencias verificadas; Sobre BAFRAS: equipo; Contacto: contacto con ingeniería. Evitar competir internamente con varios títulos idénticos. No inventar localidades o mercados atendidos como si hubiera oficina allí.

**ES/CA/EN/DE:** preparar claves semánticas por sección, no traducir cadenas concatenadas ni slugs mecánicamente sin criterio; revisión humana técnica de términos como dirección facultativa, ACS, PCI, BMS, EMS, PPC, commissioning y autoconsumo. `hreflang` bidireccional solo para versiones existentes, con `x-default` si se define política; canonical autorreferente por idioma (no canonical de todas a ES). `sitemap.xml` solo URLs publicables; `robots.txt` no sustituye `noindex`; no indexar borradores de proyectos, páginas legales incompletas o entornos staging. Structured data `Organization`/`ProfessionalService` solo con nombre, logo, contacto y ubicación verificados; `BreadcrumbList` si las rutas reales lo sustentan. No marcar `Review`/ratings inventados.

**SEO técnico a comprobar en staging:** renderizado de títulos/metas en HTML inicial, respuesta HTTP 200/301/404, ausencia de enlaces rotos, imágenes optimizadas con alt pertinente, Core Web Vitals medidos, indexabilidad, sitemap y hreflang recíproco. No prometer rankings.

## 5. Diseño y accesibilidad
- Sistema de componentes reutilizables: `SiteHeader`, `NavMenu`, `Hero`, `CapabilityCard`, `SectorCard`, `ProjectReferenceCard`, `FounderCard`, `CTASection`, `ContactForm`, `SiteFooter`, `Breadcrumbs`, `SeoHead`.
- Escala tipográfica, ancho máximo de lectura, contraste y espaciado coherentes con identidad visual aprobada; evitar que los textos técnicos se conviertan en tarjetas excesivamente altas. En móvil, una columna legible y navegación sin hover obligatorio.
- WCAG 2.2 AA como **objetivo de aceptación**: navegación por teclado, foco visible, skip link, semántica de encabezados, labels persistentes, mensajes de error asociados, estado de envío anunciado, tamaño de objetivos táctiles y respeto a `prefers-reduced-motion`.
- Fotografías: solo activos propios o con licencia/permiso; imagen ilustrativa nunca rotulada como fotografía de un proyecto real. Evitar retratos generados de fundadores. Alt descriptivo si informativo; vacío si decorativo.

## 6. Contacto: especificación funcional y privacidad
**Contrato funcional:** `nombre` obligatorio; `empresa` opcional; `email` obligatorio; `mensaje` obligatorio. Validación tanto cliente como servidor; límites razonables de longitud, sanitización contextual, CSRF si aplica, rate limiting y antispam accesible. Envío por servidor a buzón verificado mediante proveedor o SMTP seguro; no incluir credenciales en cliente. No almacenar mensajes en analítica ni logs. Idempotencia o protección contra duplicados; mensajes de éxito **solo** tras aceptación confirmada por backend, y error recuperable sin perder contenido.

**Privacidad:** responsable, finalidad, base jurídica, conservación, destinatarios/encargados, derechos, transferencias y enlace a política real sujetos a revisión jurídica del tratamiento concreto. No imponer casilla de consentimiento genérica sin base legal; separar consentimiento comercial si alguna vez se plantea. Cookies analíticas no esenciales solo con mecanismo adecuado de consentimiento donde corresponda. No añadir adjuntos en V1.

**Pruebas E2E mínimas:** envío válido, campos obligatorios, email inválido, fallo de red, error servidor, doble clic, antispam, recepción real en buzón, lectura en móvil/teclado, no filtración de PII, idioma correcto de mensajes y accesibilidad de feedback.

## 7. Arquitectura de implementación propuesta (no decisión tomada)
**Principio:** sitio editorial predominantemente estático, contenido estructurado y componentes reutilizables; formularios como única interacción de servidor necesaria inicialmente. Es razonable evaluar Astro/SSG u otra solución equivalente según hosting, equipo y mantenimiento. No seleccionar framework por inercia ni introducir CMS antes de justificar quién actualizará contenidos y con qué frecuencia.

**Modelo mínimo de contenido:** `Page` (locale, route, seo, sections, status), `Capability`, `SectorGroup`, `ProjectReference` (type=prior_experience|bafras_project, evidence_status, publication_status, authorization, contributor_role, phases, images), `FounderProfile` (verified fields), `ContactSettings`. Separar **datos públicos** de notas internas y estados de verificación. Evitar duplicación de textos ES entre templates y datos. Build debe fallar o excluir entradas `draft/unverified` de rutas, sitemap, menús y enlaces. No crear páginas huérfanas.

**Pipeline:** validación de esquema y traducciones → generación de páginas → comprobación de enlaces → lint de metadatos/h1 → auditoría de accesibilidad → pruebas formulario → revisión legal/visual → despliegue staging → aprobación → producción. Las reglas de publicación deben comprobarse automáticamente cuando sea posible.

## 8. Registro de incidencias y puertas de salida
| ID | Prioridad | Hallazgo / acción | Responsable sugerido | Criterio de cierre |
|---|---|---|---|---|
| P0-01 | Bloqueante | Referencias de Formentor, instituto, Ibiza, eólico y UIB aún sin fichas completas | Fundadores + editorial | Rol, fase, sistemas, fechas y permisos acreditados; o excluir referencia concreta |
| P0-02 | Bloqueante | Perfiles y acreditaciones de fundadores sin verificación final | Fundadores | Nombre/rol/especialización y retratos autorizados; sin claims no acreditados |
| P0-03 | Bloqueante | Formulario y correo corporativo no operativos/verificados | Desarrollo + operaciones | Pruebas reales de recepción, errores, spam y seguridad |
| P0-04 | Bloqueante | Textos legales y tratamiento de datos pendientes | Responsable legal | Aviso legal/privacidad y cookies según implementación, validados |
| P0-05 | Bloqueante | Alcance comercial y permisos de uso de servicios/activos | Dirección + ingeniería | Revisión de claims, habilitaciones y autorización de imágenes |
| P1-01 | Alta | Estado editorial histórico inconsistente en títulos internos | Editorial | Documento fuente limpio; no exportar notas internas |
| P1-02 | Alta | Definir rutas y estrategia i18n | SEO + desarrollo | Slugs aprobados; hreflang/canonical/sitemap coherentes |
| P1-03 | Alta | Sistema de diseño responsive y accesibilidad | UX + desarrollo | Pruebas teclado/móvil/WCAG documentadas |
| P1-04 | Alta | Registro central de SEO y redirecciones | SEO + desarrollo | Un title/meta/H1/canonical por ruta, sin duplicados |
| P1-05 | Alta | Matriz de enlaces/CTA verificada | UX + QA | Sin enlaces rotos, anclas falsas ni CTAs a borradores |
| P2-01 | Media | Analítica mínima de conversión | Comercial + desarrollo | Evento de envío confirmado sin PII; medición agregada |
| P2-02 | Media | Fichas detalladas y casos de estudio | Ingeniería + comercial | Publicar solo cuando haya evidencia y derechos |

**Regla de salida:** no lanzar públicamente con P0 abiertos. Si las referencias no están verificadas, puede lanzarse una versión reducida **sin proyectos concretos ni afirmaciones de experiencia no sustentadas**, con ajuste explícito del menú y enlaces; esa alternativa requiere aprobación editorial, no es una decisión automática.

## 9. Plan de implementación y aceptación
**Fase A — Contratos editoriales:** congelar copy aprobado, confirmar rutas, registrar metadatos, inventariar imágenes y verificar claims.  
**Fase B — Base web:** layout, navegación, componentes, idiomas, SEO técnico, legales.  
**Fase C — Integración:** cargar páginas aprobadas, ocultar borradores, implementar formulario y canal de correo.  
**Fase D — QA:** responsive, teclado, accesibilidad, enlaces, SEO/i18n, rendimiento y pruebas E2E de contacto.  
**Fase E — Go/no-go:** evidencias de fundadores y proyectos, permisos, seguridad/privacidad, checklist P0 cerrado y aprobación de publicación.

**Criterios mínimos de aceptación:** nueve rutas editoriales solo si publicables; menú de seis entradas coherente; tres capacidades distinguibles; CTA contacto funcional; no claims sin evidencia; todas las rutas publicadas con SEO correcto y traducción revisada; formulario operativo y legal; sin enlaces a fichas inexistentes; revisión visual móvil/escritorio y teclado completada. Si alguna ruta no cumple, se retira o se retrasa de forma explícita.

## 10. Decisiones pendientes de dirección
1. Dominio definitivo, hosting y responsable de mantenimiento.
2. Correo corporativo, destinatarios y procedimiento de gestión de leads.
3. Perfil público definitivo de cada fundador y referencias autorizadas.
4. Idioma principal, política de slugs y calendario de publicación de CA/EN/DE.
5. Fotografías y licencias; si no existen, diseño tipográfico/técnico neutro.
6. Aprobación del alcance comercial por servicio y del contenido legal.

**Resultado final:** se aprueba el paso a **diseño técnico de implementación**, no la publicación. Documento 03 mantiene el copy aprobado y añade las condiciones para convertirlo en una web creíble, navegable, medible y mantenible.


---

# PARTE K — DECISIONES DE PUBLICACIÓN Y CONTENIDO 03.K

# BAFRAS Engineering — Decisiones de contenido y publicación (03.K)
Fecha: 2026-11-02. Naturaleza: definición editorial, comercial, técnica y funcional; no constituye certificación legal ni verificación de hechos no documentados.

## 1. Identidad profesional — decisión cerrada
- Murti: **ingeniero industrial**. Especialidad editorial: sistemas energéticos, análisis e integración energética.
- Àngel: **ingeniero industrial**. Especialidad editorial: infraestructuras e instalaciones.
- Amin: **ingeniero técnico electrónico**. Especialidad editorial: automatización, control y software técnico.
- Contacto corporativo confirmado: **info@bafras.com**.

**Texto publicable de presentación del equipo:** «BAFRAS Engineering reúne a dos ingenieros industriales y un ingeniero técnico electrónico, con perfiles complementarios en infraestructuras e instalaciones, sistemas energéticos y automatización y control. Combinamos estas perspectivas para estudiar cada proyecto y desarrollar el alcance de ingeniería que necesita.»

**Fichas visibles:** nombre + titulación exacta anterior + especialidad editorial + breve función, sin años de experiencia, colegios profesionales, números de colegiación, habilitaciones, certificaciones, cargos, responsabilidades contractuales o titulaciones adicionales no contrastadas. Antes de publicar, confirmar con cada socio la grafía de su nombre público, su consentimiento para fotografía y biografía y, si se van a alegar atribuciones profesionales reguladas, la acreditación pertinente. El texto no supone que los tres tengan la misma habilitación profesional.

## 2. Proyectos y experiencia — decisión de producto
Mantener seis referencias editoriales en tres bloques; tres destacadas (Formentor, eólica, transición energética UIB) y tres complementarias (centro educativo Mallorca, residencia Ibiza, HVAC UIB). Etiquetar inequívocamente **«Experiencia profesional del equipo»**, no «Proyectos realizados por BAFRAS». La elección de proyectos destacados es editorial y provisional.

**Regla de publicación por referencia:** ficha con nombre genérico y ubicación amplia cuando no exista autorización para identificar cliente o inmueble; nunca afirmar intervención efectiva en todas las instalaciones típicas del edificio. Separar siempre: (a) contexto del proyecto; (b) sistemas cuyo alcance se ha confirmado; (c) intervención concreta del profesional; (d) fases y entregables acreditados; (e) evidencia utilizable. No publicar marcas, clientes, logos, importes, fotografías de obra, detalles sensibles ni resultados no autorizados. Si una ficha carece de confirmación del socio sobre su participación, permanece interna. La referencia UIB debe distinguir trabajo profesional en la institución de contratos de BAFRAS.

**Ficha mínima para recabar de cada socio:** denominación publicable/anónima, sector y localización publicable, periodo aproximado, empleador/rol (interno si es confidencial), alcance exacto, sistemas realmente tratados, fases realmente desarrolladas, entregables, datos cuantitativos demostrables, permisos para nombres/fotos/logos y contacto para validación. La autorización del socio no reemplaza derechos de terceros.

**Regla de UX:** si no hay suficientes referencias verificadas, mostrar texto general de experiencia profesional verificada y tarjetas sin nombres comerciales solo cuando la intervención esté confirmada; no crear enlaces a fichas vacías. Los textos detallados de tipos de instalaciones son inventario editorial de trabajo, no aseveraciones públicas.

## 3. Contacto — decisión funcional y copy final
**Correo visible y accionable:** info@bafras.com (`mailto:info@bafras.com`). Mostrarlo cerca del formulario y en el pie de página. Verificar recepción y respuesta antes del lanzamiento; no asumir que la cuenta está técnicamente configurada solo por estar confirmada como dirección.

**H1:** «Hablemos de tu proyecto.»
**Introducción:** «Explícanos brevemente qué necesitas resolver, tanto si estás definiendo una actuación como si ya dispones de planos, datos o documentación técnica. También puedes escribirnos directamente a info@bafras.com.»
**Formulario:** nombre (obligatorio); empresa u organización (opcional); correo electrónico (obligatorio); «Cuéntanos qué necesitas» (obligatorio, texto libre). Ayuda: «Puedes indicar el tipo de instalación, la ubicación y la fase del proyecto. No necesitas tener todos los datos.» Botón: «Enviar consulta». Sin presupuesto, teléfono, especialidad o plazos obligatorios; sin adjuntos en V1.
**Estado de envío:** carga y bloqueo de doble envío; éxito «Hemos recibido tu consulta.» solo tras confirmación del servidor; error «No hemos podido enviar tu consulta. Puedes escribirnos a info@bafras.com.» No prometer plazo de respuesta sin proceso operativo establecido.
**Especificación:** validación cliente/servidor, protección antispam y limitación de frecuencia, TLS, no incluir mensaje personal en logs analíticos, destino de recepción autorizado, protección ante abuso, prueba real extremo a extremo, accesibilidad de etiquetas/errores/teclado, conservación y borrado definidos según política real.
**Privacidad:** aviso breve junto al formulario con enlace a política real; informar responsable, finalidad, base jurídica, destinatarios/encargados, conservación y derechos según tratamiento efectivo. No insertar una casilla genérica de «acepto» por defecto: la base jurídica y la necesidad de consentimiento se determinan al documentar el tratamiento. Si el envío no está implementado y probado, ocultar o desactivar formulario y mantener correo como alternativa real.

## 4. Documentación legal — decisión de alcance y responsabilidades
Preparar páginas reales «Aviso legal» y «Política de privacidad»; «Política de cookies» y mecanismo de consentimiento solo si las tecnologías utilizadas lo requieren. No copiar plantillas genéricas con datos inventados. Reunir previamente razón social/forma jurídica real, NIF/CIF cuando corresponda, domicilio legal publicable, datos registrales cuando proceda, responsable del tratamiento, proveedor de hosting, proveedor de correo y formulario, transferencias internacionales si existen, plazos de conservación y herramientas de analítica/cookies efectivas. Revisar textos con asesoría legal/privacidad antes de activar recogida de datos. Si no existe aún sociedad constituida, identificar correctamente al titular real del sitio y del tratamiento; no atribuirlo a una entidad inexistente.

## 5. Servicios, materiales visuales y afirmaciones — decisión editorial
Las páginas INF/ENE/DIG describen capacidades técnicas, no una garantía de que todos los servicios se prestan directamente, con habilitación propia o bajo idéntico alcance. Cruzar antes de publicar la taxonomía Documento 01 con disponibilidad real, competencias, habilitaciones, posibles colaboraciones externas y alcance contractual. No ofertar IA/ML como servicio actual ni auditorías acreditadas de ciberseguridad OT, soporte 24/7 o ahorros garantizados. Para actividades reguladas, revisar exigencias concretas y titularidad de firmas/responsabilidades.

**Imágenes:** preferencia por fotografías originales autorizadas, retratos con consentimiento y gráficos propios; imágenes de stock solo con licencia y sin atribución implícita a proyectos propios. Cada imagen debe tener fuente, titular, permiso/licencia, alcance de uso, texto alternativo adecuado y registro interno. Si falta evidencia, usar diseño gráfico neutro o prescindir de la imagen. Logos de terceros solo con permiso aplicable.

## 6. Estados operativos para implementación
**Cerrado editorialmente:** titulaciones aportadas por el usuario, especialidades editoriales propuestas, dirección de correo, estructura de perfiles, jerarquía de referencias, copy de contacto y campos del formulario, política de atribución y reglas de imágenes.
**Pendiente de dato verificable:** nombres públicos completos/biografías, confirmación y autorización de cada proyecto, datos del titular legal y tratamiento, disponibilidad efectiva de servicios, licencias de imágenes.
**Pendiente de desarrollo/prueba:** correo operativo, formulario backend, recepción, seguridad, accesibilidad, documentos legales definitivos, rutas y traducciones ES/CA/EN/DE.

**Criterio de cierre:** no convertir los datos pendientes en afirmaciones públicas. El sitio puede construirse ya con campos opcionales y estados de publicación; el lanzamiento se decide por evidencias, no por completar visualmente todas las tarjetas.


---

# Decisión 03.K.2 — Responsable operativo y destino del formulario (aprobada)

**Decisión confirmada por los fundadores:** BAFRAS gestionará las consultas recibidas a través del formulario web. El destino único de notificación y recepción es **info@bafras.com**. La versión inicial no requiere CRM, cuenta de usuario ni almacenamiento comercial adicional.

**Flujo funcional:** visitante introduce nombre, empresa opcional, correo y consulta → validación en cliente y servidor → servicio backend de envío seguro al buzón corporativo → confirmación de envío o error. En el correo recibido incluir datos del remitente y consulta, con `From` del dominio autorizado y `Reply-To` del usuario validado para facilitar la respuesta y evitar suplantación del remitente. No publicar credenciales ni enviar directamente desde el navegador usando secretos. Configurar SPF/DKIM/DMARC según proveedor y probar entregabilidad real.

**Copy público:** «También puedes escribirnos directamente a info@bafras.com». Éxito: «Tu consulta se ha enviado correctamente.» Error: «No hemos podido enviar tu consulta. Escríbenos a info@bafras.com.» No prometer respuesta en plazo fijo.

**Distinción jurídica:** «BAFRAS» queda confirmado como responsable operativo y nombre comercial, pero la política de privacidad debe identificar a la persona jurídica o física titular real del tratamiento (denominación, identificación y contacto) cuando se confirmen sus datos. No presumir constitución de una sociedad.

**Criterios de aceptación:** correo recibido en info@bafras.com; respuesta posible mediante Reply-To; validación y antispam efectivos; errores sin pérdida silenciosa; protección de datos y textos legales implementados; sin exposición de secretos; pruebas extremo a extremo completadas.


---
## ADENDA 03.SEC.CAT-01 — Catálogos de servicios por sector · 03/11/2026
**Estado:** ampliación funcional/editorial solicitada por dirección; pendiente de validación del wireframe C04-SEC. **Precedencia:** esta adenda complementa SEC-02 y sustituye exclusivamente la instrucción histórica «se evitan catálogos de servicios» y «un enlace principal por tarjeta» en cuanto impidan el CTA documental. No altera ningún texto publicable ya aprobado ni el orden de los seis sectores. El catálogo es un recurso adicional, no una nueva página ni un proyecto de referencia.

### Identificadores estables y correspondencia editorial
| Orden | Sector D03 (texto vigente) | `sector_id` | Recurso previsto |
|---|---|---|---|
| 1 | Turismo, comercio y edificios terciarios | `turismo-terciario` | PDF sectorial opcional |
| 2 | Industria, logística y agroindustria | `industria-logistica-agroindustria` | PDF sectorial opcional |
| 3 | Infraestructuras y servicios públicos | `infraestructuras-servicios-publicos` | PDF sectorial opcional |
| 4 | Salud, educación y equipamientos | `salud-educacion-equipamientos` | PDF sectorial opcional |
| 5 | Edificación, rehabilitación y activos inmobiliarios | `edificacion-rehabilitacion-activos` | PDF sectorial opcional |
| 6 | Comunidades energéticas e infraestructuras tecnológicas | `comunidades-energeticas-infraestructuras-tecnologicas` | PDF sectorial opcional |

Los `sector_id` son claves de contenido y **no** títulos públicos ni rutas a subpáginas. Cada catálogo se vincula inequívocamente a un solo `sector_id`; un sector puede tener cero, uno o varios catálogos temáticos; cada catálogo identificado tiene como máximo una versión publicable por idioma (se permiten otros idiomas mediante fallback editorial explícito). No se presume que exista ningún PDF actualmente.

### CTA y estados editoriales
- **Etiqueta de interfaz aprobable:** «Descargar catálogo de servicios»; ubicación: dentro de cada bloque SEC-02, tras los ejemplos y el enlace contextual a capacidad, o en un grupo de acciones subordinadas. Mantener ambas acciones distinguibles: capacidad = navegación técnica; PDF = profundización documental; contacto = conversión comercial general.
- **Disponible:** mostrar enlace directo al PDF, con indicación `PDF · Español` / `PDF · Català` / `PDF · English` / `PDF · Deutsch` según el idioma **real del documento**, no el de la interfaz. La interfaz puede localizar la palabra de idioma; el código de idioma debe permanecer verificable.
- **No disponible / borrador / archivo ausente:** no mostrar CTA, marcador de posición, botón deshabilitado ni «próximamente».
- **Solo en otro idioma:** mostrar únicamente si existe decisión explícita de ofrecerlo como alternativa; indicar idioma real junto al enlace. Nunca sugerir que hay traducción.
- **Título largo:** el título documental puede usarse como nombre accesible o metadato si aporta claridad, pero no debe desplazar la etiqueta principal ni truncarse.
- **Sin captación obligatoria:** descarga gratuita, directa, sin formulario, registro ni JavaScript. No inventar títulos, versiones o fechas públicas de catálogos todavía inexistentes.
- El enlace al catálogo **no sustituye** los títulos, textos, ejemplos o enlaces contextuales de SEC-02 ni el CTA de Contacto SEC-05.

### Gobernanza y trazabilidad
D03 fija la relación editorial sector–recurso y la etiqueta del CTA; D04 valida idioma, estado, archivo, ruta y publicación; D05 rige componente y estados. El manifiesto de recursos es la fuente operativa de los PDF, no el HTML. El contenido del PDF, las traducciones y sus derechos requieren revisión antes de marcarlo como publicado. Las notas históricas de SEC-02 que contradigan esta adenda quedan superadas solo en el punto de la descarga.


---
## ADENDA 03.SEC.CAT-02 — Catálogos por actividad dentro de Industria · 03/11/2026
**Estado:** propuesta de ampliación editorial solicitada por dirección, pendiente de aprobación de la composición V3. **Precedencia:** sustituye únicamente el límite de un catálogo por sector/idioma de CAT-01; mantiene los seis sectores, su orden, el contenido literal de SEC-01 a SEC-05 y la descarga directa cuando solo existe un catálogo.

- **Industria, logística y agroindustria** (`industria-logistica-agroindustria`) podrá disponer de varios catálogos específicos por actividad, p. ej. **fabricación de muebles y madera** y **lavanderías industriales**. Son líneas editoriales previstas, **no documentos disponibles ni servicios publicados acreditados**.
- Cada línea documental tendrá `catalog_id` estable e independiente de `sector_id`, y un título visible específico para que el visitante sepa qué descarga. El identificador de actividad no crea una séptima página o sector.
- Si hay **dos o más catálogos publicados y elegibles** para el idioma de interfaz, mostrar el control «**Catálogos de servicios**» que revela una lista de documentos; cada opción tendrá título de actividad, formato e idioma real y descarga directa sin formulario.
- Si hay **un solo catálogo publicado**, mostrar «**Descargar catálogo de servicios**» con enlace directo. Si no hay ninguno, omitir todo el control. Esta regla se aplica a cualquier sector que crezca en el futuro.
- Un catálogo de otro idioma solo aparece por autorización explícita de fallback, indicando el idioma real. No se listan borradores ni entradas sin PDF publicable.
- La lista y su orden son editoriales y se alimentan de datos validados; no se escriben manualmente en HTML. El contacto sigue independiente.


---
## ADENDA 03.CO-02 — Contacto V2 aprobado · 03/11/2026
**Estado:** aprobación expresa de dirección de la página Contacto C04-CO-V2. **Precedencia:** complementa CO-01 a CO-04 y la decisión 03.K.2 únicamente en los datos y canales de contacto; no altera sus textos editoriales aprobados ni los demás contenidos de D03.

- **Correo público:** `info@bafras.com` con enlace `mailto:info@bafras.com` (operatividad pendiente de comprobar).
- **Teléfono público autorizado:** **+34 610 903 179**, con enlace `tel:+34610903179`. Se muestra en la alternativa de contacto directo y en el pie de página. El número fue facilitado expresamente por el fundador para publicarlo como contacto de BAFRAS; no se presupone que sea una línea contratada a nombre de una sociedad.
- **Formulario:** se mantienen nombre, empresa u organización (opcional), correo electrónico y descripción de la consulta, sin pedir teléfono obligatorio. Se conserva el destino operativo previsto `info@bafras.com`.
- **Condición de publicación:** no activar el formulario sin tratamiento legal real, proveedor de recepción, medidas antispam y pruebas de entrega. No prometer disponibilidad telefónica ni tiempos de respuesta no confirmados.
- **Aprobación visual ≠ aprobación de publicación:** la verificación responsive, accesibilidad, textos legales, traducciones y funcionamiento de los canales sigue pendiente de cierre G1 y posteriores controles.

---
## ADENDA 03.G1-01 — Línea base editorial para desarrollo · 03/11/2026
**Estado:** nueve páginas aprobadas individualmente; contenido de D03 es fuente editorial vinculante. La auditoría AUD-G1-03 no certifica paridad literal exhaustiva de los prototipos; se difiere la comprobación completa al proceso de integración y QA, con revisión humana de diferencias reales.
- El contenido público se ingiere de datos editoriales estructurados; no se reescribe desde maquetas ni se copia automáticamente texto de demostración.
- Los bloques, servicios, CTA, referencias y atribuciones se rigen por las decisiones anteriores de D03. Ante divergencias entre HTML de prototipo y D03, prevalece D03 y se registra la excepción.
- No publicar referencias de experiencia, catálogos, estudios, traducciones o materiales sin revisión y autorización.
- Los nueve diseños individuales están aprobados. La formalización del gate G1 global queda sujeta a acta de dirección; no implica validación de publicación.

---
## ADENDA 03.G1-02 — Resolución de variantes por evidencia documental más reciente · 03/11/2026
**Estado:** aplicación del criterio comunicado por dirección en WEB-00 FINAL («las contradicciones de Contacto y las atribuciones pendientes deben resolverse según la evidencia documental más reciente»). **No crea ni reescribe copy**: indica qué texto aprobado ya existente rige cuando D03 contiene varios. Las variantes no seleccionadas se conservan como históricas.

**Contacto (CO-01 a CO-03).** Cronología: CO V1.1 (02/11) → 03.K §3 (02/11) → 03.K.2 → adenda 03.CO-02 (03/11), que declara aprobados los textos de CO-01 a CO-04 y de 03.K.2 y cuya maqueta CO-V2 los reproduce.
- **Introducción de CO-01 y ayuda del campo 4 de CO-02:** rige el texto de CO-01/CO-02 V1.1, ratificado por 03.CO-02 y por la maqueta aprobada.
- **Mensajes de estado:** rige 03.K.2, la decisión más reciente sobre el formulario. Éxito: «Tu consulta se ha enviado correctamente.» Error: «No hemos podido enviar tu consulta. Escríbenos a info@bafras.com.»
- **CO-03:** rigen el H2 y el párrafo de CO-03 de D03, que prevalecen sobre el H2 «¿Prefieres contactar directamente?» de la maqueta según 03.G1-01. El correo y el teléfono de 03.CO-02 se muestran como datos de contacto, con etiqueta de canal y sin texto adicional. Los marcadores «[PENDIENTE…]» de CO-03 quedan superados por 03.CO-02. **Pendiente editorial opcional:** el H2 y el párrafo aluden solo a escribir; adaptarlos al teléfono requiere aprobación expresa.

**Atribución de experiencia (PE).** La evidencia más reciente es 03.K §2 (02/11), posterior a la iteración PE que propuso «Experiencia profesional previa».
- Etiqueta pública para trabajos de los fundadores: **«Experiencia profesional del equipo»** (03.K §2).
- Etiqueta para encargos propios acreditados: **«Proyecto BAFRAS»** (PE, etiqueta obligatoria; 03.K no la contradice).
- «Pendiente de acreditación» es un estado interno y no se publica.
- **Sin referencias autorizadas al publicar:** se aplica la regla de UX de 03.K §2. La página mantiene texto general y no muestra tarjetas sin confirmación ni enlaces a fichas vacías; la entrada de menú se conserva (D04 §3).
