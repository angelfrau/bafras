# BAFRAS WEB — WEB-G1-CLOSE · Decisiones de dirección
**Fecha:** 03/11/2026 · **Estado de todas las decisiones:** PENDIENTES. Ninguna se ha aplicado. Cada una incluye un texto de aprobación que dirección puede firmar o rechazar tal cual.

Urgencia: **A** antes de WEB-01/G2 · **B** antes de la vertical G3 · **C** antes de publicar (G4).

## Estado tras WEB-00 FINAL (03/11/2026)
Dirección comunicó por escrito las decisiones recogidas en el apartado A del acta. Las demás siguen pendientes. Ninguna decisión se ha marcado como aprobada sin esa comunicación.

| ID | Estado | Resolución |
|---|---|---|
| DEC-01 | **Pendiente** | Acta actualizada con el apartado A; falta la ratificación formal (§12) |
| DEC-02 | **Decidida** (A.2) | Diagramas no obligatorios para el lanzamiento; incorporación futura posible |
| DEC-03 | **Parcial** | D02 V1.0-R reconstruido e incorporado (`02_posicionamiento.md`, §17); pendiente de ratificación. D01 sigue pendiente (G4) |
| DEC-04 | **Resuelta** por criterio de dirección (A.7) | Adenda 03.G1-02 de D03. Difiere de la propuesta inicial en CO-03: rige el H2 de D03, no el de la maqueta (03.G1-01). Adaptar CO-03 al teléfono queda como opción editorial |
| DEC-05 | **Pendiente** | Las propuestas de title y meta no se han incorporado |
| DEC-06 | **Resuelta** (A.7) | «Experiencia profesional del equipo» (03.K §2, la más reciente) y «Proyecto BAFRAS». Sustituye la recomendación inicial («previa del equipo») |
| DEC-07 | **Resuelta** (A.7) | Regla de UX de 03.K §2: variante sin tarjetas; se mantiene la entrada de menú |
| DEC-08 | **Principio decidido** (A.4) | WCAG AA sin alterar innecesariamente la identidad; la regla concreta se valida en G2-02 |
| DEC-09 | **Decidida** (A.3) | Tokens y componentes se consolidan en la implementación |
| DEC-10 | **Pendiente** | Logo maestro y créditos |
| DEC-11 | **Pendiente** | Formulario, hosting y dominio |
| DEC-12 | **Decidida y aplicada** | Originales de Commons solo en local, verificados por SHA-1 y recuperables; originales propios versionados (commit D) |
| DEC-13 | **Sustituida** por la estrategia de dirección | Única rama de desarrollo `feat/contingut-v2`; `main` intacta; sin `v2/desarrollo`; sin `push`. Commits A–D ejecutados |
| DEC-14 | **Pendiente** | Idiomas de lanzamiento |
| DEC-15 | **Pendiente** | Etiquetas H05 |
| DEC-16 | **Pendiente** | Rutas ES (WEB-G2-00) |

## Resumen priorizado (propuesta original de WEB-G1-CLOSE)

| ID | Decisión | Incidencias | Urgencia | Límite |
|---|---|---|---|---|
| DEC-13 | Autorizar las operaciones Git de WEB-00 y verificar la fuente de GitHub Pages | WGR-036, 092, 093 | **A** | Antes de WEB-01 |
| DEC-03 | Recuperar D02 (y aportar D01) | WGR-002, 091 | **A** | Antes de WEB-01 (D02) / G4 (D01) |
| DEC-01 | Ratificar el acta G1 con excepciones | WGR-090, 072 | **A** | Antes de WEB-01 |
| DEC-02 | Excepción de diagramas técnicos | WGR-050 | **A** | Con DEC-01 |
| DEC-08 | Regla de contraste | WGR-052 | **A** | Con DEC-01 |
| DEC-09 | Tokens y complemento del catálogo de componentes | WGR-051, 063 | **A** | Con DEC-01 |
| DEC-16 | Registro de rutas ES | WGR-031 | **A** | Cierre de WEB-G2-00 |
| DEC-12 | Versionado de los originales de imagen | WGR-099 | **A** | Commit C |
| DEC-04 | Copy de Contacto | WGR-020, 021, 022 | B | Antes de WEB-G3-01a |
| DEC-05 | Title y meta de cuatro páginas | WGR-040 | B | Antes de WEB-G3-01a |
| DEC-15 | Etiquetas H05 | WGR-025 | B | Antes de WEB-G3-01a |
| DEC-06 | Etiquetas de atribución | WGR-023 | B | Antes de WEB-G3-02 |
| DEC-07 | Proyectos y experiencia sin referencias autorizadas | WGR-026 | B | Antes de WEB-G3-02 |
| DEC-10 | Logo maestro y créditos de imagen | WGR-060, 061 | B | Antes de WEB-G2-02 |
| DEC-11 | Proveedor de formulario, hosting y dominio | WGR-033, 039 | B/C | G3-01b (formulario) / G4 |
| DEC-14 | Idiomas de lanzamiento | WGR-032, 085 | C | Antes de WEB-G4-01 |

---

### DEC-01 · Ratificación del acta G1
- **Contexto:** las nueve composiciones están aprobadas una a una (D03 03.G1-01; D05 §48), pero el gate exige un acta expresa (D04 §8, §14).
- **Opciones:** (a) ratificar con las excepciones DEC-02, DEC-08 y DEC-09; (b) ratificar sin excepciones, lo que exige producir antes los diagramas; (c) no ratificar.
- **Recomendación:** (a).
- **Consecuencias:** con (a) puede empezar WEB-01. Con (b), WEB-01 queda bloqueada hasta tener los diagramas. Con (c), no hay intervención productiva.
- **Texto de aprobación:** «Dirección ratifica el acta `02_Acta_Propuesta_Cierre_G1.md` con las excepciones de sus apartados 4, 5 y 6 y acepta el catálogo de su apartado 3. La ratificación autoriza planificar e iniciar la implementación incremental; no autoriza publicación.»

### DEC-02 · Excepción de diagramas técnicos (D05 §8.5)
- **Contexto:** D05 L66 (§8.5) y L576 (C03-EV-03/04/05) exigen diagramas INF/ENE/DIG. Las composiciones aprobadas los excluyen expresamente (D05 L1049 INF-05 «sin diagrama ficticio de integración», L1218 ENE-05 «sin gráfico inventado», L1250 DIG «sin flujogramas inventados»). El conflicto afecta solo a esas tres páginas. Ninguna maqueta tiene hueco reservado para diagramas.
- **Opciones:** (a) excepción y mejora futura opcional; (b) encargar los tres diagramas antes de G2.
- **Recomendación:** (a). Las composiciones aprobadas funcionan sin diagramas, y unos diagramas sin relaciones revisadas por ingeniería incumplirían CA-C03-D02.
- **Consecuencias:** (a) no modifica maquetas ni copy; los diagramas pueden añadirse más adelante como sección opcional de `Section`. (b) retrasa G2 y requiere revisión de especialistas.
- **Texto de aprobación:** el apartado 4 del acta, literal.

### DEC-03 · Recuperación de D02 y aportación de D01
- **Contexto:** D02 (`02_posicionamiento.md`, 2347 líneas, 1.0-RC) estaba en el paquete el 02/11/2026 (B01 L5, L36) y hoy no está en ningún lugar del proyecto. D01 nunca ha estado. D03 remite a D01 para el estado de publicación de los servicios.
- **Opciones:** (a) recuperarlo desde una copia externa (papelera de reciclaje, historial de OneDrive o Drive, correo o herramienta de origen) y reincorporarlo; (b) declarar D02 retirado y D03 como autoridad superior efectiva.
- **Recomendación:** (a) para D02, antes de WEB-01. Para D01, aportarlo antes de G4.
- **Consecuencias:** sin D02, la jerarquía de autoridad queda incompleta, aunque D03 sigue siendo vinculante para el contenido. Sin D01 no se puede habilitar la publicación de servicios (WGR-084).
- **Texto de aprobación:** «Se reincorpora D02 en `docs/project_v02/02_posicionamiento.md` (versión ___) y D01 en ___, o bien: “D02 queda retirado; D03 V1.22 actúa como autoridad superior para posicionamiento hasta nueva versión”.»

### DEC-04 · Copy de Contacto (revisa la recomendación de WEB-G1-REVIEW-01)
- **Contexto, variantes localizadas:**

| Elemento | CO-01/CO-02 V1.1 (L983–999) | 03.K §3 (L1203–1210, «copy final», 02/11) | 03.K.2 (L1231–1240, «aprobada») |
|---|---|---|---|
| Introducción | «Explícanos… documentación técnica. Revisaremos tu consulta para valorar si podemos ayudarte y qué información convendría analizar a continuación.» | «Explícanos… documentación técnica. También puedes escribirnos directamente a info@bafras.com.» | Solo la frase «También puedes escribirnos directamente a info@bafras.com» |
| Ayuda del campo 4 | «Puedes indicar el tipo de instalación o actividad, el problema o actuación prevista, la ubicación y la fase del proyecto. No necesitas tener todos los datos.» | «Puedes indicar el tipo de instalación, la ubicación y la fase del proyecto. No necesitas tener todos los datos.» | — |
| Éxito | «Tu consulta se ha enviado correctamente. Revisaremos la información y contactaremos contigo si podemos avanzar con el encargo.» | «Hemos recibido tu consulta.» | «Tu consulta se ha enviado correctamente.» |
| Error | «No se ha podido enviar tu consulta. Puedes intentarlo de nuevo o escribirnos directamente al correo indicado en esta página.» | «No hemos podido enviar tu consulta. Puedes escribirnos a info@bafras.com.» | «No hemos podido enviar tu consulta. Escríbenos a info@bafras.com.» |
| CO-03 H2 | «¿Prefieres escribirnos directamente?» (anterior al teléfono) | — | — |

- **Evaluación de autoridad:** la aprobación más reciente, la adenda 03.CO-02 del 03/11, declara que «complementa CO-01 a CO-04 y la decisión 03.K.2 […] no altera sus textos editoriales aprobados». La maqueta CO-V2 aprobada reproduce literalmente la introducción y la ayuda de CO-01/CO-02 V1.1. La recomendación de WEB-G1-REVIEW-01 (adoptar 03.K/03.K.2 en todo) **no se sostiene** para la introducción y la ayuda: la adenda no cita 03.K §3. Para los mensajes de estado, ninguna variante es inequívoca: CO-02 V1.1 y 03.K.2 se citan ambas como vigentes.
- **Propuesta consolidada:** introducción y ayuda = CO-01/CO-02 V1.1, como en la maqueta aprobada; éxito y error = 03.K.2, la decisión específica del formulario aprobada y citada por la adenda; CO-03 = texto nuevo, que requiere aprobación: H2 «¿Prefieres contactar directamente?» (el de la maqueta) y una línea por canal, sin prometer disponibilidad. No se reescribe nada por estilo.
- **Consecuencias:** sin decisión, WEB-G3-01a no puede cerrar la paridad literal de Contacto.
- **Texto de aprobación:** «Para Contacto rigen: introducción y ayuda de CO-01/CO-02 V1.1; éxito “Tu consulta se ha enviado correctamente.” y error “No hemos podido enviar tu consulta. Escríbenos a info@bafras.com.” (03.K.2); CO-03 con H2 “¿Prefieres contactar directamente?”. Las variantes de 03.K §3 quedan como históricas. Se incorpora a D03 como adenda 03.CO-03.»

### DEC-05 · Title y meta description (propuestas no aprobadas)
- **Contexto:** D03 aporta title y meta para DIG (L663–664), Sectores (L769–770), Sobre BAFRAS (L976–977) y Contacto (L1027–1028), pero no para Inicio, Capacidades, INF ni ENE. `js/router.js` (sitio heredado) contiene variantes con «Mallorca» y «Áreas técnicas» que **no** son copy aprobado. Las propuestas derivan de los H1 y entradillas aprobados y del mapa de intención de D03 §4 (L1113). No añaden localidades porque D03 §4 prohíbe inventar mercados.

| Página | Title propuesto (car.) | Meta description propuesta (car.) |
|---|---|---|
| Inicio | BAFRAS Engineering \| Ingeniería de instalaciones, energía y automatización (74) | Ingeniería multidisciplinar para instalaciones, sistemas energéticos y automatización y control: comprender cada reto y desarrollar la solución adecuada. (153) |
| Capacidades | Capacidades \| Infraestructuras, energía y automatización \| BAFRAS Engineering (77) | Estudios, proyectos y asistencia técnica en infraestructuras e instalaciones, sistemas energéticos y automatización y control, por especialidad o coordinados. (158) |
| Infraestructuras e instalaciones | Ingeniería de instalaciones e infraestructuras \| BAFRAS Engineering (67) | Diseñamos, analizamos y revisamos instalaciones eléctricas, mecánicas e hidráulicas para edificios, infraestructuras y procesos. (128) |
| Sistemas energéticos | Ingeniería de sistemas energéticos y eficiencia \| BAFRAS Engineering (68) | Analizamos consumos y desarrollamos proyectos de eficiencia energética, generación renovable, almacenamiento, electrificación y gestión de la energía. (150) |

- **Opciones:** aprobar, modificar o encargar una revisión SEO.
- **Recomendación:** aprobar, o editar en la misma tabla. Decidir además si se menciona «Mallorca», con evidencia de ámbito real.
- **Texto de aprobación:** «Se aprueban los title y meta de la tabla DEC-05 (con los cambios anotados) como adenda 03.SEO-01 de D03.»

### DEC-06 · Etiquetas de atribución
- **Contexto:** D03 L868 «Experiencia profesional previa» / «Proyecto BAFRAS»; 03.K L1195 «Experiencia profesional del equipo»; maqueta PE V1: «Experiencia profesional previa del equipo · pendiente de acreditación».
- **Recomendación:** dos etiquetas canónicas: «Experiencia profesional previa del equipo», para trabajos de los fundadores anteriores a BAFRAS, y «Proyecto BAFRAS», para encargos propios acreditados. La primera cumple a la vez L868 y 03.K y coincide con la maqueta. «Pendiente de acreditación» es un estado interno y no se publica.
- **Consecuencias:** fija el enumerado `Experience.kind` y sus etiquetas localizadas.
- **Texto de aprobación:** «Etiquetas públicas canónicas: “Experiencia profesional previa del equipo” y “Proyecto BAFRAS”. Ninguna etiqueta de estado interno es pública.»

### DEC-07 · Proyectos y experiencia sin referencias autorizadas
- **Contexto:** las seis referencias son borradores no publicables (03.K §2). 03.K §2 (regla de UX) indica mostrar texto general y no crear fichas vacías.
- **Opciones:** (a) publicar PE-01, PE-03 y PE-04 con las introducciones, sin tarjetas, y mantener la entrada de menú; (b) ocultar la página y su entrada de menú hasta tener al menos una referencia autorizada.
- **Recomendación:** (a), coherente con 03.K §2 y D05 §13.8, y sin alterar la navegación de seis entradas de D04 §3.
- **Texto de aprobación:** «Si no hay referencias autorizadas al publicar, Proyectos y experiencia se publica sin tarjetas (variante a) y mantiene su entrada en el menú.»

### DEC-08 · Regla de contraste
- **Contexto (medido, WCAG 2.x):** verde `#1A7A5A` sobre arena 4,31:1, papel 4,85:1 y blanco 5,28:1; pino sobre arena 12,33:1; tinta sobre arena 11,72:1. Afecta a eyebrows, numerales, enlaces de 11–13 px y a `info@bafras.com` (22 px, peso 600, que no cuenta como texto grande) en las nueve maquetas.
- **Opciones:** (a) regla de uso sin color nuevo: verde sobre arena solo para texto grande y no textual, y pino o tinta para texto pequeño; (b) añadir un token derivado `verde-texto` `#187154` (4,86:1 sobre arena), lo que exige modificar D05.
- **Recomendación:** (a). No toca la identidad cromática ni D05, y el cambio visual sobre arena es mínimo.
- **Texto de aprobación:** apartado 6 del acta, literal.

### DEC-09 · Tokens y complemento del catálogo
- **Recomendación:** delegar en Diseño, en WEB-G2-02, la consolidación de contenedor, cortes, escala y espaciado a partir de las maquetas, sin cambio estético. Aceptar el complemento del catálogo (acta, apartado 3).
- **Texto de aprobación:** apartados 3 y 5 del acta, literales.

### DEC-10 · Logo maestro y créditos de imagen
- **Contexto:** `assets/images/brand/logos/` contiene variantes `*_deep.svg`, `*_deep_corregido.svg`, PNG y `logo_h_*`. Hay 7 imágenes asignadas con CC BY o CC BY-SA que exigen crédito visible (WGR-034, 061).
- **Recomendación:** declarar maestros `BAFRAS_logo_horizontal_deep_corregido.svg` y `BAFRAS_logo_vertical_deep_corregido.svg` **si** Diseño confirma que «corregido» es la versión final. Créditos: una página «Créditos de imágenes» enlazada desde el pie, más un pie discreto en cada imagen CC (lo que recomienda `attribution.md`).
- **Texto de aprobación:** «Logo maestro: ___. Créditos: página enlazada desde el pie y crédito junto a cada imagen con licencia que lo exija.»

### DEC-11 · Formulario, hosting y dominio
- **Contexto:** D04 §7 y §9 dejan abiertos hosting y proveedor transaccional; 03.K.2 exige backend seguro, SPF/DKIM/DMARC y E2E. `CNAME` = `bafras.com` en GitHub Pages, que no ejecuta servidor.
- **Opciones:** (a) GitHub Pages con un proveedor de formularios o una función serverless externa; (b) hosting estático con funciones integradas.
- **Recomendación:** decidirlo antes de WEB-G3-01b. Hasta entonces, el formulario se construye desactivado y con el correo como alternativa (03.K §3).
- **Texto de aprobación:** «Hosting: ___. Envío del formulario: ___. Dominio canónico: https://bafras.com (con o sin www: ___).»

### DEC-12 · Originales de imagen en Git
- **Opciones:** (a) versionar solo derivados, manifiestos y `source.json`, y conservar los originales (96 MB) fuera de Git con su SHA1; (b) Git LFS; (c) commit directo.
- **Recomendación:** (a). La procedencia queda acreditada por URL, licencia y SHA1, y el historial no crece.
- **Texto de aprobación:** «Se versionan derivados, manifiestos y `source.json`; los originales se archivan en ___.»

### DEC-13 · Operaciones Git de WEB-00
- **Contexto:** `WEB_00_PLAN_SANEAMIENTO.md` §3–§5.
- **Recomendación:** autorizar en este orden: `fetch`; commit A; rama `v2/desarrollo` y commits B y C; commit D; etiqueta `prod-pre-v2`. Sin `push` hasta revisar. Comprobar en GitHub *Settings → Pages* qué rama y carpeta se publican.
- **Texto de aprobación:** «Se autorizan las operaciones 1–5 de WEB_00_PLAN_SANEAMIENTO §5; el `push` queda pendiente de revisión.»

### DEC-14 · Idiomas de lanzamiento
- **Recomendación:** lanzar solo en ES. CA/EN/DE se publican cuando estén traducidos y revisados por una persona (D03 §4; D04 §3). El selector se presenta según WGR-062.
- **Texto de aprobación:** «Lanzamiento en ES; CA/EN/DE posteriores, con revisión humana.»

### DEC-15 · Etiquetas H05
- **Contexto:** las cuatro agrupaciones de Inicio están «propuestas (etiquetas a contrastar con taxonomía sectorial)» y difieren de los seis sectores de SEC-02.
- **Recomendación:** confirmar las cuatro etiquetas como agrupación editorial de portada, distinta de la taxonomía de Sectores, o sustituirlas por nombres de SEC-02. Decisión editorial; no se propone copy nuevo.
- **Texto de aprobación:** «Las etiquetas H05 ___ son definitivas.»

### DEC-16 · Registro de rutas ES
- **Contexto:** los slugs están «propuestos»; la maqueta Inicio usa `/infraestructuras-e-instalaciones/` y `/proyectos-y-experiencia/`; el sitio heredado usa `#/rutas`.
- **Recomendación:** ratificar en WEB-G2-00 la tabla 03.J §3.1, con prefijo `/es/`, raíz que redirige a `/es/`, una página 404 y redirección de los enlaces hash heredados mediante un script mínimo en la raíz.
- **Texto de aprobación:** «Se ratifica el registro de rutas ES de WEB-G2-00 (versión ___).»
