# BAFRAS.com â€” Visual Asset Requirements

## Purpose

Este inventario identifica evidencia visual tÃ©cnica real disponible y material que falta para que BAFRAS.com muestre ingenierÃ­a, activos y proyectos sin recurrir a recursos genÃ©ricos ni atribuciones no verificadas.

## Asset principles

- Se prioriza material real de proyectos; no se utiliza stock salvo aprobaciÃ³n explÃ­cita.
- No se representa un recurso conceptual como si fuera documentaciÃ³n de un proyecto ejecutado.
- Se anonimiza la informaciÃ³n sensible cuando proceda.
- Se verifican derechos de publicaciÃ³n, confidencialidad y restricciones contractuales antes de publicar.
- Se distingue **EXPERIENCIA DEL EQUIPO** de **PROYECTO BAFRAS**. La primera corresponde a la trayectoria previa de integrantes; la segunda, a trabajos desarrollados directamente por BAFRAS.

## Home â€” System Vision

**STATUS:** AVAILABLE

**ASSET:** `assets/images/home/vision/bafras-system-vision-diagram.png` (original, 1536 Ã— 1024, 1,906,658 bytes); versiÃ³n web derivada `assets/images/home/vision/bafras-system-vision-diagram.webp` (1400 Ã— 933, 113,786 bytes).

**USE:** SecciÃ³n VisiÃ³n de Sistema de Home.

**TREATMENT:** IlustraciÃ³n conceptual sin rÃ³tulos; las etiquetas se mantienen en HTML para poder traducirlas. El WebP se redimensionÃ³ y se aplanÃ³ sobre el fondo `#0E2B25` de la secciÃ³n para preservar bordes suaves y evitar artefactos de transparencia; pesa aproximadamente un 94% menos que el original. No debe presentarse como esquema o plano de una instalaciÃ³n ejecutada.

## Home â€” Capabilities

### Infraestructura e IngenierÃ­a

**STATUS:** ASSET REQUIRED

**PREFERRED MATERIAL:**
- Plano MEP o esquema unifilar publicable.
- FotografÃ­a de instalaciÃ³n elÃ©ctrica, HVAC, sala tÃ©cnica u obra.
- Detalle tÃ©cnico o modelo BIM aprobado.

**PURPOSE:** Demostrar capacidad de ingenierÃ­a fÃ­sica e instalaciones.

**CURRENT SLOT:** La fila de capacidad tiene un slot de medio opcional y oculto (`data-asset-slot="infraestructura"`). Activarlo solo al enlazar un recurso aprobado.

### Sistemas EnergÃ©ticos

**STATUS:** ASSET REQUIRED

**PREFERRED MATERIAL:**
- FotografÃ­a de instalaciÃ³n FV o BESS.
- Diagrama energÃ©tico o de integraciÃ³n.
- Curva de consumo con datos autorizados.

**PURPOSE:** Demostrar capacidad de ingenierÃ­a energÃ©tica.

**CURRENT SLOT:** La fila de capacidad tiene un slot de medio opcional y oculto (`data-asset-slot="sistemas-energeticos"`). Activarlo solo al enlazar un recurso aprobado.

### Sistemas Digitales y AutomatizaciÃ³n

**STATUS:** ASSET REQUIRED

**PREFERRED MATERIAL:**
- Captura autorizada de SCADA, HMI o BMS.
- Arquitectura de control, armario de automatizaciÃ³n o visualizaciÃ³n de datos operativos.

**PURPOSE:** Mostrar la conexiÃ³n entre sistemas digitales y activos fÃ­sicos.

**CURRENT SLOT:** La fila de capacidad tiene un slot de medio opcional y oculto (`data-asset-slot="sistemas-digitales"`). Activarlo solo al enlazar un recurso aprobado.

## Home â€” Experience

Los tres espacios de caso estÃ¡n preparados para una imagen opcional y oculta; no se muestran placeholders al visitante.

### Campus universitario

**STATUS:** ASSET REQUIRED

**PREFERRED:** FotografÃ­a publicable de instalaciÃ³n FV/BESS, diagrama energÃ©tico, SCADA o monitorizaciÃ³n, esquema tÃ©cnico o plano.

**DATA REQUIRED:** Home V2.1 solicita 7,6 MWp fotovoltaicos y 10 MWh de almacenamiento, ademÃ¡s de V2G, AMI, SCADA y VPP. La ficha interior existente indica ~7,4 MWp FV, +10 MWh BESS y 18 Mâ‚¬ de financiaciÃ³n pÃºblica. Resolver esta discrepancia y validar contexto/derechos antes de publicaciÃ³n.

### Proyecto hotelero

**STATUS:** ASSET REQUIRED

**PREFERRED:** Plano MEP, HVAC, instalaciÃ³n elÃ©ctrica, sala tÃ©cnica, fotografÃ­a de obra, detalle constructivo o instalaciÃ³n terminada.

**DATA REQUIRED:** Home V2.1 indica Hotel Formentor, centros educativos y proyectos residenciales en Ibiza, segÃºn el texto proporcionado para esta iteraciÃ³n. Verificar nombres, atribuciÃ³n y autorizaciÃ³n. La ficha previa indica Mallorca e Ibiza, siete aÃ±os de experiencia, diseÃ±o y obra, mediciones y certificaciÃ³n; no se dispone de magnitudes de proyecto publicadas.

### Sistemas energÃ©ticos internacionales

**STATUS:** ASSET REQUIRED

**PREFERRED:** Infraestructura eÃ³lica marina, sistemas elÃ©ctricos, automatizaciÃ³n/control, arquitectura tÃ©cnica o puesta en marcha.

**DATA REQUIRED:** Dogger Bank A â€” 1,2 GW y Vineyard Wind 1 â€” 806 MW aparecen en Home V2.1 y las fichas existentes. Sistemas tÃ©cnicos: sistemas elÃ©ctricos, automatizaciÃ³n, control y puesta en marcha (commissioning). Confirmar atribuciÃ³n concreta, contexto de participaciÃ³n y datos publicables; no usar la cifra agregada como sustituto de las referencias.

## Publication checks

Antes de publicar cualquier recurso futuro, verificar:

- Derechos de publicaciÃ³n y autorizaciÃ³n del titular.
- Confidencialidad y restricciones de NDA.
- Datos personales, nombres de clientes y logotipos.
- Direcciones, firmas, precios y credenciales.
- Direcciones IP, identificadores internos y datos operativos sensibles.
- InformaciÃ³n tÃ©cnica cuya publicaciÃ³n pueda crear riesgos de seguridad o revelar propiedad intelectual.

La anonimizaciÃ³n no convierte automÃ¡ticamente material confidencial en publicable.

