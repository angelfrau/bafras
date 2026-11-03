# BAFRAS Engineering — B01 · Auditoría técnica, visual y arquitectónica del repositorio

Fecha: **03/11/2026**, Europe/Madrid. Intervención: lectura, diagnóstico y documentación. Base examinada: copia de trabajo local de `bafras/`, incluidos sus cambios previos sin confirmar. No se ha auditado una web remota ni se ha publicado nada.

Convención de referencias: las rutas de código son relativas a `bafras/`; `D02`, `D03`, `D04` y `D05` corresponden, respectivamente, a `docs/project_v02/02_posicionamiento.md`, `03_contenido_editorial.md`, `04_arquitectura_software.md` y `05_sistema_visual.md`. `archivo:Lx–Ly` indica líneas de la copia examinada. La carpeta denominada `project_v02` en el encargo está realmente dentro de `docs/`; este informe se entrega allí junto a los cuatro documentos.

Clasificación utilizada:

- **VERIFICADO:** observación respaldada por archivos, lectura directa de recursos o ejecución de comprobaciones locales.
- **INFERIDO:** consecuencia técnica razonada; no equivale a comportamiento observado en navegador.
- **NO VERIFICADO:** dato o comportamiento pendiente de comprobación.
- **RECOMENDACIÓN:** propuesta para una fase posterior; no es una modificación autorizada en B01.

## 1. Resumen ejecutivo

**VERIFICADO.** La web es estática y tiene una base pequeña: un `index.html` de **1208 líneas**, cuatro CSS con **868 líneas** en conjunto, tres JavaScript con **134 líneas**, un validador Python y una suite de **18 pruebas**. Python no genera HTML ni atiende consultas. Existen **13 vistas virtuales**: las nueve páginas objetivo, tres fichas de experiencia y Conocimiento. Todas viven en el mismo HTML y se seleccionan mediante fragmentos `#/ruta@ancla`.

**VERIFICADO.** Hay identidad visual recuperable: seis colores centrales del kit, superficies cálidas ya utilizadas, Inter, contenedor de 1180 px, botones discretos, líneas divisorias y composiciones editoriales de texto más evidencia. La identidad no necesita una paleta nueva. Sí necesita documentar la cascada efectiva: `pages.css` modifica reiteradamente reglas base y de componentes, y contiene también reglas globales.

**VERIFICADO.** La presencia de las nueve vistas no implica conformidad con D03. Cambian los títulos y textos; Inicio antepone necesidades a capacidades, añade visión de sistema y carece del bloque H05 Sectores; Sectores conserva siete grupos diferentes de los seis aprobados; Automatización conserva entregables y evidencias pendientes; Proyectos presenta tres tarjetas agregadas frente a las seis referencias previstas; el menú incluye Conocimiento, excluido del lanzamiento por D03:L28–29.

**VERIFICADO.** La suite pasa: **18 passed in 0.23s**. El validador también pasa, con avisos de **33 coincidencias de placeholders y 10 de verificaciones**. Son recuentos por expresión regular, no 43 componentes distintos. Un inventario por elementos encuentra **30 slots visuales**, **21 elementos `placeholder`** y **6 `verify`**. Los estados no impiden que se muestren las referencias: el HTML contiene cifras, nombres y notas internas pendientes. Además, pruebas y validador exigen «Áreas técnicas» y rechazan «Capacidades», contrario al menú aprobado en D03.

**VERIFICADO / NO VERIFICADO.** Contacto tiene envío cliente a FormSubmit, etiquetas persistentes, validación HTML nativa, bloqueo del botón y aviso de estado. La política de privacidad es un marcador y los enlaces legales son `#`. No se ha comprobado la recepción en el buzón, la activación del proveedor, la protección de servidor o la entregabilidad. El pie afirma «BAFRAS Engineering S.L.» sin que los documentos examinados acrediten esa forma jurídica.

**NO VERIFICADO.** No se han obtenido capturas del sitio: Chrome no ofreció una sesión de depuración utilizable y Edge headless terminó con error de GPU/acceso en este entorno. No se han instalado dependencias. Responsive, teclado y contraste sobre imágenes se evalúan por código y quedan pendientes de prueba visual. Se inspeccionó directamente el WebP conceptual de visión de sistema; eso no constituye una captura de página.

**RECOMENDACIÓN.** El siguiente trabajo debe completar D05 con los valores reales, las composiciones de las nueve páginas, sus estados y la trazabilidad a D03. La futura migración Python + Jinja2 + Pydantic v2 es compatible con gran parte del HTML/CSS y los recursos, pero permanece subordinada al diseño aprobado. B01 no cierra G1 ni inicia el Bloque 02.

## 2. Alcance y documentación examinada

### 2.1. Fuentes y autoridad

| Fuente | Estado y contenido encontrado | Uso en esta auditoría |
|---|---|---|
| D02, 2347 líneas | Biblioteca consolidada 1.0-RC, candidata interna; síntesis estratégica, compradores, evidencia, localización y antecedentes íntegros | Necesidad → análisis → criterio → alcance; integración cuando aporta valor; separación de experiencia personal, proyecto corporativo y ejemplo conceptual. D02:L22–32, L50–66, L68–139 y L2295–2346 |
| D03, 1220 líneas | Documento Maestro 03 Definitivo; estado rector y decisiones 03.K/03.K.2 superpuestos a historial | Fuente de copy y jerarquía. Ocho páginas con texto cerrado; Proyectos con estructura aprobada y referencias condicionadas. D03:L4–20 |
| D04, 125 líneas | Arquitectura de producto y software V2.0, 03/11/2026 | Arquitectura objetivo, límites de capas, publicación desacoplada y gates; no implementación. D04:L10–41, L69–111 |
| D05, 78 líneas | Sistema visual UX/UI V2.0, 03/11/2026 | Especificación visual propuesta, todavía sin valores reales ni maquetas aprobadas. D05:L4–18, L60–78 |
| Documentación técnica existente | `README.md`, `docs/architecture.md`, `visual-system-v1.md`, `visual-component-inventory.md`, `visual-evidence-map.md`, `website-visual-assets.md`, backlog y notas de pasadas visuales | Antecedentes contrastados con código; no sustituyen D03–D05 |
| Auditorías anteriores | `docs/audits/01…07*.md`, especialmente decisión arquitectónica 03 | Antecedentes; sus alternativas no reabren el stack ratificado en D04 |
| Código y recursos | `index.html`, CSS, JS, `pyproject.toml`, `CNAME`, validador, pruebas y `assets/images/` | Estado implementado y evidencia primaria |

**VERIFICADO.** Los cuatro documentos pedidos están disponibles. **NO VERIFICADO.** No están en esta copia el Documento 01 ni los CSV de `02_anexos_datos/` citados por D02. Tampoco los repositorios, muestras o esquemas de los dos softwares de estudios. No se certifican los 56 servicios, la equivalencia de traducciones, la autoría de proyectos o los permisos de imágenes a partir de referencias textuales.

### 2.2. Procedimiento y límites

**VERIFICADO.** Se inventariaron archivos, rutas, encabezados, anclas, tokens, media queries, referencias de recursos y estados; se leyeron los módulos productivos, validaciones y especificaciones; se extrajeron tamaños de imágenes con Pillow ya instalado; se calcularon contrastes sRGB de parejas sólidas; se ejecutaron las comprobaciones existentes sin cachés nuevas (`python -B tools/validate.py` y `python -B -m pytest -p no:cacheprovider -q`). No se envió el formulario ni se contactó con terceros.

**VERIFICADO.** La copia ya contenía modificaciones en HTML, CSS, JS, pruebas y validador, además de documentación sin seguimiento. Se auditó esa copia, no solo el último commit. Git requirió una excepción `safe.directory` limitada al comando de lectura por diferencia de propietario; no se modificó configuración global. No se localizaron archivos `AGENTS.md` aplicables en el árbol examinado ni en los ancestros comprobados.

Evidencias complementarias dentro de esta misma carpeta:

- [Inventario estático](evidencias_B01/inventario_estatico.json): rutas, H1/H2 con líneas, estados, anclas, HEX, breakpoints y contrastes.
- [Registro de comprobaciones](evidencias_B01/comprobaciones.txt): comandos, resultados y limitaciones del navegador.

**NO VERIFICADO.** No hay mediciones de rendimiento, renderizado, zoom, lector de pantalla, respuestas del hosting, DNS/correo, cabeceras HTTP, CSP ni auditoría jurídica. Las menciones a privacidad se limitan a comparar implementación y especificación interna, sin emitir un dictamen legal.

## 3. Arquitectura actual verificada

### 3.1. Árbol y puntos de entrada

```text
bafras/
├── index.html                 # único documento de entrada; 13 vistas
├── css/
│   ├── tokens.css             # 21 líneas: identidad, aliases, fuente, ancho
│   ├── base.css               # 22 líneas: reset, escala y utilidades
│   ├── components.css         # 378 líneas: globales + patrones + especialidades
│   └── pages.css              # 447 líneas: páginas + ajustes globales + router visual
├── js/
│   ├── site.js                # 20 líneas: menú, retratos, año
│   ├── router.js              # 103 líneas: rutas, títulos, selección y scroll
│   └── form.js                # 11 líneas: envío AJAX y estados
├── assets/images/
│   ├── brand/{logos,symbols,favicon,social}/
│   ├── home/{hero,vision}/
│   ├── experience/mep/
│   ├── team/
│   └── misc/a
├── tools/validate.py          # comprobaciones estáticas y avisos
├── tests/test_structure.py    # 18 pruebas
├── docs/                     # contenido de referencia; no consumido por la web
│   ├── audits/
│   ├── content/
│   └── project_v02/
├── pyproject.toml
├── README.md
├── .gitignore
└── CNAME                     # bafras.com
```

**VERIFICADO.** No hay `package.json`, gestor Node, plantillas Jinja, modelos Pydantic, directorio de contenido por idioma, generador, artefacto `dist`, sitemap, robots ni workflows `.github` en el árbol inventariado. `pyproject.toml:L1–10` declara `bafras-site` 0.5.0, Python ≥3.10 y opciones pytest; no declara dependencias ni extras de desarrollo. Que pytest esté instalado en esta máquina no hace reproducible su instalación desde el proyecto.

### 3.2. Flujo real

```text
Edición manual de index.html + CSS + JS + imágenes
                         │
                         ├── Python validate.py / pytest (comprobación local)
                         │
                         └── servidor estático → index.html
                                                ├── CSS: tokens → base → components → pages
                                                ├── site.js: menú / retratos / año
                                                ├── router.js: hash → .pagina.activa + title/meta
                                                └── form.js → FormSubmit externo → buzón (no probado)

docs/*.md y docs/project_v02/*.md → lectura humana; sin conexión de generación al HTML
```

**VERIFICADO.** CSS se carga en `index.html:L13–16`; JS con `defer` en L1204–1206. Las vistas están ocultas por `.pagina{display:none}` y activadas por `.activa` (`css/pages.css:L436–445`). El router cambia clase, título, descripción y posición de scroll (`js/router.js:L56–102`). Sin JavaScript, el `noscript` muestra **todas** las vistas seguidas (`index.html:L17`): existe acceso textual de emergencia, pero no navegación independiente por página.

**VERIFICADO.** `site.js` depende de `#cabecera`, `#menuBoton`, `[data-foto]` y `#anio`. Prueba candidatos de retrato por nombre/extensión hasta cargar el primero válido (`js/site.js:L7–18`). `form.js` depende de `#formulario`, `#avisoForm` y del botón de envío. No hay acoplamiento con motores Python ni cálculo técnico en navegador.

### 3.3. Rutas, publicación y validación

**VERIFICADO.** La ruta se lee de `location.hash`; `@` separa un ancla local. Una ruta desconocida selecciona Inicio. Títulos y descripciones están duplicados conceptualmente respecto al contenido en `TITULOS`, sin registro editorial compartido. Las anclas se buscan exclusivamente dentro de `.pagina.activa`. Se verificaron estáticamente las anclas de los enlaces `#/…@…`: no se encontraron destinos en otra vista ni IDs duplicados. Esto no prueba scroll ni foco en navegador.

**VERIFICADO.** `README.md` y `docs/architecture.md` describen despliegue estático compatible con GitHub Pages. `CNAME:L1` contiene `bafras.com`. **NO VERIFICADO.** No hay evidencia local suficiente para afirmar que ese sea el despliegue activo, su rama/carpeta de publicación, HTTPS, configuración de Pages o canal de promoción. No existe pipeline de despliegue versionado en esta copia.

**VERIFICADO.** El validador comprueba ficheros mínimos, orden de CSS/JS, `defer`, enlaces locales de recursos, existencia global de rutas/anclas, endpoint del formulario, retratos y patrones de codificación (`tools/validate.py:L136–215`). Los avisos de publicación se imprimen y el programa devuelve éxito (`L220–243`). Las pruebas verifican sobre todo presencia de clases, conteos, textos exactos y atribución básica, con mayor cobertura de Infraestructuras y Energía (`tests/test_structure.py:L57–348`). No hay pruebas de navegador o extremo a extremo.

## 4. Inventario de identidad visual

### 4.1. Paleta y variables reales

Todos los valores de esta tabla son **VERIFICADOS** en `css/tokens.css`.

| Variable / papel actual | HEX o definición | Ubicación | Naturaleza |
|---|---|---|---|
| `--pino` · Deep Green | `#0E2B25` | L3 | Color corporativo central, fondos oscuros y marca |
| `--verde` · BAFRAS Green | `#1A7A5A` | L4 | Acento, enlaces, CTA, numeración y foco |
| `--piedra-verde` · Stone Green | `#4F7B6E` | L5 | Bordes técnicos y acentos secundarios |
| `--tinta` · Graphite | `#2A2A2A` | L6 | Texto principal |
| `--gris-claro` · Light Gray | `#E6E6E6` | L7 | Texto secundario sobre oscuro y estados |
| `--blanco` | `#FFFFFF` | L8 | Superficie y texto sobre oscuro |
| `--beige` / `--piedra` | `#ECE8DD` / alias | L12–13 | Superficie cálida existente; no paleta propuesta |
| `--beige-claro` / `--papel` | `#F7F5F0` / alias | L12–13 | Fondo general |
| `--beige-linea` / `--linea` | `#D8D2C3` / alias | L12–13 | Separadores |
| `--gris` | `#4A5550` | L14 | Texto secundario sobre claro |
| `--pino-2` / `--pino-3` | alias de `--pino` / `--piedra-verde` | L10 | Alias históricos, no colores nuevos |
| `--verde-claro` | alias de `--gris-claro` | L11 | Nombre engañoso: el valor real es gris |
| `--display`, `--texto` | Inter + sistema/Segoe UI/Helvetica/Arial/sans-serif | L15–16 | Misma familia para títulos y cuerpo |
| `--ancho` | `1180px` | L17 | Ancho máximo de caja `.envoltura` |

**VERIFICADO.** Fuera de tokens aparecen `#fff` (equivalente a blanco), `#f4f2eb` y `#f6f4ee` en slots (`css/pages.css:L395`; `css/components.css:L272`), además de numerosos `rgba()` derivados de verdes, blanco y papel. `color-mix()` aparece en botones y slots. Estas variantes sirven a overlays, transparencias, bordes y placeholders; no son nuevas familias corporativas.

**RECOMENDACIÓN.** Registrar en D05 la función de cada variante antes de consolidar. `--pino-2` no requiere un token cromático independiente; `--verde-claro` merece aclarar su semántica. Decidir si dos fondos tan próximos para slots tienen una distinción intencionada; no sustituirlos automáticamente.

### 4.2. Tipografía y escala efectiva

**VERIFICADO.** `index.html:L10–12` solicita Inter a Google Fonts con pesos **400/500/600** y `display=swap`. No hay fuentes locales ni licencia de fuente adjunta. Hay reglas que piden **700**, por ejemplo `.energy-axis li`, etiquetas de dominios (`css/components.css:L236, L241, L254`); ese peso no está incluido expresamente en la petición. **INFERIDO.** Puede resolverse por síntesis o sustitución según el navegador y la respuesta de la fuente; no se verificó la fuente finalmente renderizada.

| Elemento | Valor definido / efectivo por cascada | Fuente |
|---|---|---|
| Cuerpo | `17px`, peso 400; interlineado de body pasa de 1.75 a 1.7; `p/li/dd/dt/label` a 1.65 | `base.css:L3`; `pages.css:L153–159` |
| H1 general | `clamp(2.3rem,5.2vw,4.1rem)`, 400; line-height 1.08 | `base.css:L8–9`; `pages.css:L155` |
| H1 Inicio | `clamp(2.1rem,4.4vw,3.6rem)`, 400; ancho final 16ch | `components.css:L59`; `pages.css:L381` |
| H2 general | `clamp(1.9rem,3.6vw,2.8rem)`, 400; line-height 1.18 | `base.css:L10`; `pages.css:L156` |
| H3 general / tarjetas | 1.25rem, 500; tarjetas normalizadas a 1.3 y tracking −.01em | `base.css:L11`; `pages.css:L142, L157` |
| H4 general | De 1.05rem a 1.0625rem, 500; hay overrides locales a 1rem | `base.css:L12`; `pages.css:L147`; `components.css:L255` |
| Entradilla | 1.25rem, 1.55; max-width base 58ch, cabeceras internas 68ch | `base.css:L16`; `pages.css:L158, L361` |
| Texto secundario de tarjetas | Frecuente .95rem; `.technical-scope` .92rem | `pages.css:L143`; `components.css:L140` |
| Microtexto / etiquetas | .85rem habitual; .78/.76/.72/.68/.62rem en variantes técnicas | `pages.css:L145`; `components.css:L139, L184, L236–254, L273–278` |
| Métricas Energía | `clamp(1.35rem,3vw,2.1rem)`; experiencia destacada hasta `clamp(1.8rem,5vw,3.8rem)` | `components.css:L263, L271` |

**VERIFICADO.** No se cambia `html{font-size}`; los rem dependen del tamaño raíz del navegador, no de los 17px del body. Con raíz habitual de 16px, .62rem equivale a 9.92px y .78rem a 12.48px. **RECOMENDACIÓN.** Comprobar esos tamaños con textos técnicos reales y títulos alemanes, sin adoptar la escala como aprobada por el mero hecho de existir.

### 4.3. Espacio, contenedores, retículas y breakpoints

| Elemento | Estado real verificado | Archivo y líneas |
|---|---|---|
| Contenedor | `max-width:1180px`, centrado; padding lateral `clamp(20px,4vw,40px)`, `border-box` | `tokens.css:L17–18`; `base.css:L1, L14` |
| Lectura | `.prosa` y `.texto-medio` 62ch; `.entradilla` 58ch; patrones de layout declaran `--measure-copy:64ch`; excepciones 68–82ch | `base.css:L15–16`; `components.css:L141–143`; `pages.css:L199, L311, L361, L375` |
| Ritmo de sección | Base 64–120px; luego `--sp-seccion:72–112px`; definición final **`clamp(56px,6vw,80px)`** | `base.css:L21`; `pages.css:L182–183, L254` |
| Flujo interior | 24px genérico, 16px tras H2/H3; 40px hacia grupos; 32px hacia enlaces; excepciones de cabecera | `pages.css:L184–198, L255–262` |
| Tarjetas | Gap frecuente 24px, padding final 28px para familia heredada; variantes editoriales con padding vertical 28–38px | `pages.css:L203–205, L307, L406, L409` |
| Editorial | `.layout-editorial`: .72/1.28; evidence 1/.82, inversa .9/1; feature .92/1.08 | `components.css:L141–146` |
| Especialidades | Hero 1/.72; módulos de tres columnas con número; mapas de dos columnas; entregables divididos .7/1.3 | `components.css:L150–162, L185–200` |
| Inicio | Capacidad con número/texto/visual; experiencia visual + identidad/detalle por áreas de grid | `pages.css:L405–413` |
| Contacto | 1/1.1; cae a una columna a 860px | `components.css:L338–339` |
| Pie | 1.4/1/1, una columna a 760px | `components.css:L368–376` |

**VERIFICADO.** `--layout-gap` y `--measure-copy` son variables locales adicionales (`components.css:L141`); `--sp-seccion` está en `pages.css`, no en `tokens.css`. En estado actual 1180px incluye el padding: el área interna puede ser de 1100px al alcanzar 40px por lado. El rango 1120–1240px de D05:L14 es una referencia pendiente de validación, no una orden de ensancharlo.

**VERIFICADO.** Hay **14 umbrales distintos**: 280, 380, 430, 520, 560, 600, 700, 760, 820, 860, 900, 1000, 1024 y 1100px. 1000 y 1100 tienen también usos `min-width`; no todos los cambios son solo para móvil. Fuentes: `components.css:L40–49, L55–115, L279–282, L303–334, L339–376`; `pages.css:L211–218, L232–233, L335–339, L388–429`.

**INFERIDO.** Los múltiples umbrales responden en parte a composiciones diferentes; no son automáticamente catorce errores. La dispersión obliga a revisar la misma familia en varios puntos de cascada, especialmente entre 700/820/900/1024px. **RECOMENDACIÓN.** Documentar el propósito de cada transición y comprobar anchos intermedios antes de reducirlos.

### 4.4. Bordes, radios, sombras y estados

**VERIFICADO.** Predominan bordes de **1px** con `--linea`; botones e inputs usan 1.5px/1px y radios de **2px**; tarjetas recientes tienen radio **0** y sin sombra (`components.css:L6, L351`; `pages.css:L416–422`). Los acentos de tarjeta suelen ser 3px y algunos bloques 4px. Las numeraciones circulares son variantes funcionales (`pages.css:L50, L226`), no un radio general alternativo.

**VERIFICADO.** Sombras específicas: desplegable `0 12px 30px rgba(14,43,37,.12)`; texto hero `0 1px 22px rgba(14,43,37,.5)`; borde interior de slot `inset 0 0 0 1px rgba(255,255,255,.55)`. Cabecera translúcida con blur de 8px (`components.css:L18, L28, L272`; `pages.css:L247, L395`).

**VERIFICADO.** Botón base inline-flex, padding 15×24px, peso 500, transición .2s. Variante llena verde con texto blanco; sobre oscuro, blanca con texto pino; variante secundaria de contorno. Enlaces de texto subrayados con borde. Foco global de 2px y offset 3px; override claro sobre oscuro (`components.css:L5–15`; `base.css:L6–7`). No se localizan estilos propios de error por campo, carga con spinner ni estado visual específico `:disabled` de botón de envío; hay bloqueo y cambio de texto en JS.

### 4.5. Marca, símbolos, iconografía e imágenes

| Grupo | Recursos existentes | Uso real / observación |
|---|---|---|
| Logo y símbolo en página | Sprite SVG inline `#isotipo`, `#logo-h`, `currentColor`; palabra ENGINEERING como texto Inter | `index.html:L20–96`; cabecera L100 y pie L1180 usan `#logo-h`. El nombre accesible está en enlace/SVG |
| Logos externos | Horizontal/vertical deep SVG y variantes `_corregido`; PNG blancos/verdes 2400px; `logo_h_*` 1200px y `logo_v_blanco` | `assets/images/brand/logos/`. Son versiones, no duplicados binarios idénticos; cuál es el maestro aprobado requiere confirmar |
| Símbolos | SVG deep; PNG blanco/verde 2048×1945; variantes 512×487 | `assets/images/brand/symbols/`. Conservar el trazado y confirmar usos por tamaño |
| Favicon/social | ICO 16×16 y avatar PNG 400×400 | Archivos existen; el favicon servido por HTML es un SVG base64 en L9, no el ICO comprobado por tests |
| Hero | `home/hero/bafras_transicion_energetica.jpg`, 1248×832, 504536 bytes | Fondo CSS, no `<img>`; `components.css:L53–54`; overlay final uniforme pino al 50% en `pages.css:L245–247`. Derechos y procedencia no acreditados aquí |
| Visión de sistema | PNG 1536×1024, 1906658 bytes; WebP 1400×933, 113786 bytes | Se usa WebP con width/height, alt, lazy y async (`index.html:L143–145`). Ilustración conceptual de edificios, energía y control; no plano ni prueba de obra |
| Equipo | Murti, Àngel y Amin: JPG 912×1136; PNG 476×520, 520×520, 400×400 respectivamente | Seis archivos; JS intenta PNG antes de JPG. Tres perfiles y responsable DIG tienen contenedores `data-foto`; consentimiento y correspondencia no verificados |
| Experiencia MEP | Formentor/Montesion/Ibiza, dos JPG por referencia, todos 1200×800, entre 100592 y 304180 bytes | Seis archivos presentes en `experience/mep/`, sin referencias desde HTML/CSS/JS actuales; no equivalen a fotos publicables aprobadas |
| Otros | `assets/images/misc/a`, 2 bytes | Sin uso localizado; no retirado en B01 |

**VERIFICADO.** Inventario gráfico: **33 archivos de imagen** (16 PNG, 10 JPG, 5 SVG, 1 ICO, 1 WebP), más el archivo `misc/a`. No se encontraron archivos de imágenes con hash SHA-256 idéntico. Hay variantes de resolución/formato que pueden tener finalidad distinta; no se clasifican como duplicación innecesaria solo por el nombre.

**VERIFICADO.** La iconografía operativa usa flechas, numeración, líneas CSS y el símbolo BAFRAS; no hay una biblioteca externa de iconos ni un conjunto uniforme de seis iconos sectoriales. `css/components.css:L164–169` define un esquema de nodos, pero no demuestra que exista el futuro diagrama técnico INF/ENE/DIG. La imagen conceptual de Inicio carece de unidades/leyenda de flujos; debe seguir tratándose como ilustración.

**RECOMENDACIÓN.** Conservar recursos y geometría de marca; completar en D05 inventario de maestro, variantes, tamaños mínimos, fondos permitidos y registros de licencia/permiso. Que una imagen exista en disco o incluya metadatos no prueba derechos. No incorporar automáticamente las seis fotos MEP para rellenar huecos.

## 5. Catálogo de componentes existentes

Todas las ubicaciones y variantes de la tabla son **VERIFICADAS por código**; los problemas de composición son inferencias donde se indica. Las decisiones de la última columna son **RECOMENDACIONES posteriores**. Se catalogan patrones actuales, sin crear una biblioteca nueva.

| Nombre descriptivo | Ubicación | Uso | Variantes | Reutilización | Problemas respaldados / límites | Recomendación |
|---|---|---|---|---|---|---|
| Cabecera y navegación | HTML:L98–119; components:L18–49; site:L2–6 | Global | Desplegables escritorio; menú expandido ≤1100px; idiomas deshabilitados | Alta | Menú no conforme D03; idiomas desaparecen en móvil; sin cierre Escape/clic exterior programado | Conservar estructura y marca; adaptar estados y navegación |
| Botón y enlace | components:L6–15; base:L6–7 | Global | Lleno, contorno, oscuro; enlace textual | Alta | Falta especificación de error/carga/disabled; copy CTA divergente | Conservar y documentar estados reales |
| Hero fotográfico | HTML:L122–135; components:L52–71; pages:L245–247, L379–381 | Inicio | Fondo fotográfico, overlay y altura específica | Media | Copy distinto de H01; contraste sobre fotografía no verificado | Conservar recurso condicionado a permiso; adaptar composición a D03 |
| Cabecera editorial interior / migas | HTML:L273–287, L380–395; components:L123–124, L150–151; pages:L361–363 | Capacidades, INF/ENE/DIG y fichas | Con slot; cabecera sencilla; migas en párrafo | Alta | CTA principal del hero técnico aprobado ausente; migas sin landmark nav | Adaptar; conservar escala y soporte |
| Encabezado y flujo | base:L14–16; pages:L184–200, L255–262 | Casi todas | `flujo`, `prosa`, `entradilla`, `mas`, `eyebrow` | Alta | Reglas globales repartidas y sobrescritas | Consolidar documentación de valores efectivos |
| Tres layouts editoriales | components:L141–146, L281; HTML:L138, L416, L564, L621 | Inicio, INF, ENE | Editorial, evidence/inversa, feature | Alta | Especializaciones con mayor especificidad cambian sus proporciones; nombres no garantizan un único comportamiento | Conservar gramática y definir variantes justificadas |
| Lista de necesidades | HTML:L153–159; pages:L75–81, L208–218, L300–305 | Inicio | Tarjeta heredada; fila enlazable de Inicio | Alta | Cinco entradas actuales vs cuatro en H03; varias reglas heredadas sobre la misma familia | Adaptar al copy; consolidar variantes |
| Fila de capacidad | HTML:L168–194, L293–334; components:L152–161; pages:L405–408 | Inicio e índice | Número + texto + visual; módulo invertido | Alta | Nombres/copy antiguos; todos los visuales son slots; no equivalencia automática entre ambas familias | Conservar patrón; adaptar sin imponer una composición idéntica |
| Slot de evidencia | pages:L343–350, L395–404; components:L272–278; HTML:L171–175 | Inicio, capacidades, experiencias y fichas | plan/photo/diagram/dashboard/data/document | Alta como soporte de trabajo | 30 slots; 21 estados explícitos placeholder; instrucciones y asset IDs pueden mostrarse; estado incompleto en otros slots | Conservar trazabilidad interna; retirar marcadores de futuras vistas publicables |
| Mapas de área | HTML:L401–406, L533–543, L662–669; components:L185–194 | INF/ENE/DIG | 4/6/6 entradas; eje ENE; flujo DIG | Media | Coincidencia de cantidad no equivale a ámbitos D03; DIG contiene CONTENT PENDING | Adaptar taxonomía visual al contenido aprobado |
| Lista técnica con evidencia lateral | HTML:L416–447; components:L217–234 | INF | Cinco disciplinas; pasos de proyecto; rail sticky | Media | Organización por fases y cinco disciplinas diferente de cuatro ámbitos + transversal aprobado | Conservar lista/rail como recurso; adaptar composición |
| Momentos narrativos energéticos | HTML:L552–585; components:L244–258 | ENE | Tres momentos; central invertido; pares/trío de dominios | Media | No presenta los seis ámbitos aprobados como tales; descarbonización sin bloque equivalente | Adaptar; no preservar su división a costa del copy |
| Entregables | HTML:L452–461, L590–599, L683–691; components:L195–200 | INF/ENE/DIG | Grupos de prosa; chips | Alta | 5/5 grupos frente a 4 modalidades editoriales; DIG incluye DELIVERABLES TO DEFINE | Conservar tratamiento sobrio; adaptar contenido |
| Ciclo y flujo técnico | HTML:L345–368, L697; components:L173–183, L201–203 | Índice, DIG | 8 pasos, 5 fases, cadena de términos | Media | Ocho pasos + cinco fases repiten parte de la explicación; D03 pide 4 modalidades, no proceso obligatorio | Consolidar según decisión editorial; no reescribir en B01 |
| Experiencia destacada / complementaria | HTML:L483–486, L621, L704–706; components:L204–211 | INF/ENE/DIG | Feature + supporting; slot y métricas | Alta | Referencias verify visibles; permisos no acreditados | Conservar patrón y atribución, condicionar publicación |
| Índice y ficha de proyecto | HTML:L821–848, L858–1001; components:L285–311; pages:L111–122, L414–418 | Proyectos y tres fichas | Tarjeta feature; ficha `dl`; listas técnicas | Alta | Solo 3 agregadas; enlaces activos a fichas con pendientes; cifras divergentes | Adaptar a 3 destacadas + 3 complementarias y permisos |
| Métricas técnicas | HTML:L621; components:L147–149, L261–271 | ENE; variantes en Inicio y fichas | `dl`, cifra fluida, línea de magnitudes | Alta | Mismo programa con cifras inconsistentes en varias páginas | Conservar formato, consolidar dato tras verificación |
| Bloque sectorial | HTML:L743–800; pages:L9–14, L365–372 | Sectores | Siete filas con chips; CSS de tarjetas `.sector` también existe | Media | El HTML actual no usa la retícula de seis tarjetas prevista; chips sin enlace contextual a capacidad | Adaptar a D03; no asumir que `.sectores` ya implementa la página |
| Perfil fundador / responsable | HTML:L714–717, L1057–1084; pages:L129–135, L277–288, L373–375; site:L7–18 | Sobre BAFRAS y DIG | Perfil largo, tira compacta, retrato con fallback | Alta | Biografías extensas y títulos no alineados a 03.K; retratos dependen de JS | Conservar retratos/fallback y estructura; adaptar ficha breve |
| Colaboración | HTML:L251–254, L1166–1171; pages:L330–333, L423–425 | Inicio y Contacto | Banda editorial; cinco tarjetas de audiencia | Media | Contacto adquiere una sección larga adicional y más selecciones que la versión de cuatro campos | Adaptar recorrido aprobado |
| Formulario y contacto directo | HTML:L1116–1162; components:L338–359; form:L1–11 | Contacto | Dos columnas, mailto, fila de campos, aviso | Alta | Siete controles visibles; privacidad pendiente; backend externo no probado | Conservar labels, email y feedback; adaptar especificación y probar después |
| Banda CTA | components:L361–365; HTML:L259–268, L504–509 | Casi todas | Oscura con símbolo decorativo; variaciones de texto/botones | Alta | Copy y cantidad de CTA no uniformes; símbolo embebido también como base64 | Conservar y documentar variantes |
| Pie | HTML:L1176–1203; components:L368–376; pages:L270–271 | Global | Tres columnas; legal | Alta | Forma jurídica no acreditada, enlaces `#`, Conocimiento | Conservar patrón; adaptar datos y navegación posteriormente |
| Patrones heredados sin uso en HTML | components:L74–100, L106–115, L291–304, L314–334; pages:L2–8 | Reglas `.capas`, `.metodo`, `.pilar`, `.proyecto`, `.sector`, `.socio`, `.entrada` | Familias de tarjeta/proceso antiguas | Baja actual | Se conserva CSS sin consumidor actual localizado; puede confundir con catálogo implementado | Marcar como candidatos a retirada tras revisar alcance; no borrar ahora |

## 6. Inventario de páginas, navegación y contenido

### 6.1. Nueve páginas objetivo frente al HTML

Las existencias y diferencias siguientes son **VERIFICADAS**. Las referencias a copy son comparación documental, no propuesta de reescritura.

| Página | Ruta actual y líneas HTML | Bloques implementados | Diferencias respecto a D03 |
|---|---|---|---|
| Inicio | `#/` · L121–271 | Hero; visión de sistema; cinco necesidades; tres filas de capacidad; método; tres experiencias; colaboración; cierre | H01 distinto; orden H02/H03 invertido y visión añadida; H03 pide cuatro situaciones; H04 abreviado y enlaza al ciclo de Capacidades en lugar de Sobre BAFRAS; **H05 Sectores ausente**; H06 publica nombres/cifras sin expediente aportado. D03:L34–118 |
| Capacidades | `#/capacidades` · L272–378 | Hero; tres módulos; flujo integrado de ocho pasos; ciclo de cinco fases; CTA | Título, denominaciones y párrafos distintos; C03 pide tres ejemplos de aplicación, sustituidos por un proceso; C04 pide cuatro modalidades; falta enlace de C05 a experiencia. D03:L149–217 |
| Infraestructuras e instalaciones | `#/capacidades/infrastructure` · L379–511 | Hero; mapa de cuatro fases; cinco disciplinas; cuatro pasos de proyecto/obra; cinco grupos de entregables; integración; experiencias; equipo; relacionadas; CTA | INF-02 necesidades sin bloque equivalente; mapa de cuatro fases no es la clasificación de cuatro ámbitos; climatización/ventilación separadas, sin presentar refrigeración/acústica y transversal según D03; experiencias concretas pendientes y bloques de equipo añadidos. D03:L275–366 y L397–398 |
| Sistemas energéticos | `#/capacidades/energy-systems` · L512–641 | Hero; siete verbos; mapa de seis grupos; tres momentos/siete dominios; cinco entregables; integración; UIB; equipo; CTA | ENE-02 necesidades sin bloque equivalente; los seis grupos son otros: separa FV/BESS e introduce estudios como ámbito; térmica, descarbonización y eficiencia hídrica no se presentan conforme al aprobado; prioriza UIB en lugar del bloque general con enlace a experiencia. D03:L415–507 |
| Automatización y control | `#/capacidades/digital-systems` · L642–733 | Hero antiguo; mapa de seis; cuatro áreas; entregables pendientes; flujo; experiencia pendiente; responsable; relacionadas; CTA | Nombre público incorrecto; DIG-W02 necesidades ausente; cuatro áreas no son las seis de DIG-W03; commissioning aparece como sexta entrada en vez de control energético; transversal de diagnóstico/pruebas sin desarrollo aprobado; texto interno inglés visible. D03:L564–640 |
| Sectores | `#/sectores` · L734–809 | Hero; siete bloques con ámbitos/chips; cierre | No coincide con los seis grupos SEC-02; faltan SEC-03 problemas transversales y SEC-04 colaboración como bloques aprobados; sin enlaces de capacidad por grupo. D03:L687–750 |
| Proyectos y experiencia | `#/proyectos` · L810–857 | Hero «Proyectos»; tres tarjetas enlazadas; CTA | PE-02 requiere seis candidatas organizadas en tres áreas, 3 destacadas + 3 complementarias; PE-03 explicación de evidencia ausente. Las tarjetas agregan MEP y eólico, no reflejan las seis referencias; no incorporan etiqueta explícita por tarjeta. D03:L778–849, L1173–1180 |
| Sobre BAFRAS | `#/sobre-bafras` · L1036–1105 | Hero; quiénes somos; tres biografías; valores; CTA | Añade historia antes del equipo; perfiles extensos y cifras; no refleja titulación exacta de Àngel/Amin en 03.K; método delegado a Capacidades; falta bloque SB-04 con enlace a experiencia. D03:L904–954, L1163–1171 |
| Contacto | `#/contacto` · L1106–1174 | Hero; correo a la izquierda; formulario a la derecha; colaboración extensa | H1/copy diferentes; cuatro campos previstos frente a siete controles visibles (añade teléfono y dos selectores); falta CO-04 aprobado. En móvil el DOM deja correo antes de formulario, contrario al orden D03:L998. D03:L960–1004 y 03.K/03.K.2 |

**VERIFICADO.** En ninguna de las nueve vistas se ha comprobado equivalencia íntegra de texto con el documento: hay divergencias explícitas, incluidas sus nueve cabeceras. Los IDs editoriales H/C/INF/ENE/DIG/SEC/PE/SB/CO no son identificadores operativos de bloques en el HTML; los anclajes existentes son nombres de secciones anteriores. Esto hace necesaria una matriz de correspondencia antes de diseñar, sin renombrar código en esta auditoría.

### 6.2. Vistas adicionales, navegación e idiomas

**VERIFICADO.** Tres fichas adicionales activas:

| Ruta adicional | Líneas HTML | Observación |
|---|---|---|
| `#/proyectos/experiencia-del-equipo/campus-universitario` | L858–905 | Rol, empresa, cifras y financiación; contexto aún pendiente |
| `#/proyectos/experiencia-del-equipo/mep-hoteles-colegios-residencial` | L906–953 | Referencia agregada; resultados/contexto pendientes |
| `#/proyectos/experiencia-del-equipo/energia-offshore-internacional` | L954–1001 | Empresas y potencias; resultados/contexto pendientes |
| `#/conocimiento` | L1002–1035 | Artículos, casos, guías e innovación en preparación; fuera del lanzamiento aprobado |

**VERIFICADO.** El menú principal incluye Áreas técnicas, Sectores, Proyectos, Conocimiento, Sobre BAFRAS y Contacto; Inicio se alcanza con el logo (`href=""`). Que haya seis enlaces principales no significa que sean las seis entradas de la arquitectura aprobada. Submenús enlazan capacidades y anclas; el pie repite denominaciones antiguas. Los enlaces legales `href="#"` no llevan a políticas: el router interpreta ese hash como Inicio (`index.html:L104–109, L1185–1200`; `router.js:L60–64, L81–102`).

**VERIFICADO.** Hay `html lang="es"` y selector ES/CA/EN/DE, con CA/EN/DE deshabilitados y títulos «traducción pendiente». ES no tiene manejador de cambio. No hay contenido localizado, rutas por idioma, diccionarios de interfaz, canonical, hreflang, Open Graph ni sitemap/robots. En móvil `.idiomas` permanece oculta incluso con el menú abierto (`components.css:L35–49`). Hay preparación nominal, no internacionalización funcional.

**RECOMENDACIÓN.** Para D05, representar el selector solo con versiones publicadas, su ubicación móvil y el caso de ficha no disponible en otro idioma. Las traducciones deben partir de D03, no del HTML actual. Confirmar la variante catalana y revisión humana de CA/EN/DE según D02:L68–88, L129–139; no inventar copy para llenar las cuatro versiones.

### 6.3. Atribución y discrepancias de datos

**VERIFICADO.** Inicio y especialidades contienen avisos de experiencia previa; eso es un elemento positivo que conservar. Sin embargo, comentarios `VERIFY BEFORE PUBLISHING` o atributos `verify` no bloquean publicación. La referencia UIB muestra:

- **≈7,6 MWp** en Inicio (`index.html:L216`).
- **7,576 MWp** y **2 × 5,016 MWh** en Energía (`L621`).
- **~7,4 MWp** en índice, ficha y perfil (`L827, L881, L1062–1063`).
- **18 M€** en ficha y perfil (`L883, L1062–1063`).

**NO VERIFICADO.** No se aportó la evidencia que determine si las cifras son fases diferentes, redondeos, errores o actualizaciones; no se elige una. Las potencias de parques eólicos y referencias a clientes/empleadores también son afirmaciones del HTML, no hechos acreditados por esta auditoría. D03:L112, L843–885, L1176–1178 exige ficha, alcance, atribución y permisos antes de mostrarlos como referencia verificable.

**VERIFICADO.** La biografía menciona IA/ML como trayectoria personal (`L1061–1063`) y Conocimiento alude a IA (`L1025–1026`). **INFERIDO.** Su proximidad a capacidades comerciales puede crear ambigüedad, pero una biografía con IA no demuestra por sí sola que se venda IA como servicio. **RECOMENDACIÓN.** Revisar el contexto con editorial y D01, sin eliminar ni convertir esas menciones en oferta por inferencia.

## 7. Responsive, accesibilidad y UX

### 7.1. Evaluación por código y comprobaciones pendientes

| Aspecto | Clasificación y evidencia | Resultado / implicación |
|---|---|---|
| Escritorio | **VERIFICADO**, CSS grid y ancho limitado | Layouts de 2/3 columnas, cabecera sticky 76px, listas/rails sticky; no se acredita equilibrio visual sin renderizado |
| Tablet | **VERIFICADO**, media queries 1100/1024/900/860/820 | Menú colapsado ya a 1100; mapas a una columna a 1024; layouts editoriales a 820, con especializaciones. Anchos intermedios: **NO VERIFICADO** |
| Móvil | **VERIFICADO**, ajustes hasta 280px | Muchos grupos se apilan; logo se reduce a 380/280. Reglas existen, pero overflow, recortes y tamaños táctiles reales: **NO VERIFICADO** |
| Menú | **VERIFICADO**, button + aria-controls/expanded; CSS focus-within | Submenús accesibles por focus-within en escritorio y desplegados en móvil abierto. No hay Escape, cierre exterior ni restitución explícita de foco; impacto práctico pendiente de prueba |
| Foco tras navegar | **VERIFICADO**, router solo clases/scroll/meta | No mueve foco a main/H1 ni anuncia cambio de vista. **INFERIDO:** puede perderse contexto, especialmente desde enlaces dentro de la vista que se oculta |
| Salto al contenido | **VERIFICADO**, `.salto` existe en pages:L35–36, sin enlace en HTML | Hay estilo disponible, falta el control real; main tampoco ofrece un destino de salto con ID |
| Semántica | **VERIFICADO**, header/nav/main/footer, H1 por vista, listas, dl, figure | Base aprovechable. Trece H1 en el documento y todos visibles con noscript; no son trece páginas HTTP. Migas en `<p>`; algunos H4 se compensan con `role=heading aria-level=3` |
| Imágenes | **VERIFICADO**, WebP con alt/dimensiones/lazy; retratos aria-hidden | Retratos se tratan como redundantes junto a nombres; verificar con lector. Fondo hero decorativo. Los slots no son evidencias reales |
| Movimiento | **VERIFICADO**, reduced-motion en CSS y router | Suprime animaciones/transiciones y ajusta scroll. La preferencia del router se lee una sola vez. Cambio de preferencia con página abierta y transiciones rápidas: **NO VERIFICADO** |
| Formularios | **VERIFICADO**, labels implícitos, required, email, autocomplete, role=status | Buena base. Sin errores propios asociados por campo ni ayuda descrita por aria-describedby; validación/errores del servidor: **NO VERIFICADO** |
| Error de envío | **VERIFICADO**, form:L7–10 | Conserva campos en rechazo de fetch y ofrece mailto. Éxito basado solo en `r.ok`; no interpreta confirmación semántica del JSON del proveedor |
| Conectividad | **VERIFICADO**, fuentes externas y fetch | Fuentes con fallbacks. No hay timeout o cancelación explícita en envío; **INFERIDO:** una petición que tarde puede prolongar el bloqueo del botón |
| Robustez de hash | **VERIFICADO**, router:L61, L67 | decodeURIComponent sin captura; selector CSS construido con ID sin escapar. Un hash malformado puede provocar excepción; no se ejecutó prueba dinámica |
| Zoom / tacto / lector | **NO VERIFICADO** | Pendientes zoom 200%, móvil estrecho, objetivos táctiles, orden de foco, anuncio de éxito/error y lectura de diagramas |

**VERIFICADO.** Sin JS el formulario mantiene `action` POST a FormSubmit y los retratos quedan en iniciales; el sitio completo se muestra en secuencia. **INFERIDO.** Es un fallback aprovechable, aunque no cumple todavía el objetivo de páginas independientes cuyo contenido esencial no dependa del router.

### 7.2. Contraste calculado

**VERIFICADO.** Se calculó luminancia relativa sRGB de valores sólidos, sin opacidades ni imagen de fondo. Son resultados aritméticos, no una certificación de accesibilidad ni estilos computados en navegador.

| Texto / fondo | Ratio aproximada | Interpretación para el objetivo de D05 |
|---|---:|---|
| Verde `#1A7A5A` / blanco | 5.28:1 | Supera referencia 4.5:1 para texto normal |
| Verde / papel `#F7F5F0` | 4.85:1 | Supera referencia 4.5:1 |
| Stone `#4F7B6E` / blanco | 4.78:1 | Supera referencia 4.5:1 |
| Stone / papel | **4.39:1** | No alcanza 4.5:1 para texto normal; requiere revisar uso concreto |
| Gris `#4A5550` / papel | 7.12:1 | Contraste amplio |
| Gris claro `#E6E6E6` / pino | 12.10:1 | Contraste amplio |
| Tinta / papel | 13.17:1 | Contraste amplio |

**VERIFICADO.** El stone se usa como texto pequeño de `.asset-slot-k` en la última variante (`pages.css:L402`) y el slot tiene fondo `#f4f2eb`, no siempre papel. **RECOMENDACIÓN.** Comprobar cada fondo real y opacidad en la matriz de estados, especialmente microtexto, focos y controles. No cambiar el color corporativo: resolver el uso semántico y la combinación. **NO VERIFICADO.** El contraste del hero depende de la fotografía, overlay y posición del texto; no se deduce del verde sólido.

### 7.3. Jerarquía y densidad

**VERIFICADO.** INF acumula mapa de fases, disciplinas, pasos, cinco entregables, integración, referencias, equipo, relacionadas y CTA. El índice contiene ocho pasos y otro ciclo de cinco; Contacto añade cinco tarjetas de colaboración después del formulario. Son estructuras reales (`index.html:L345–368, L396–509, L1166–1171`).

**INFERIDO.** La reiteración de procesos y bloques aumenta la carga de lectura y puede desplazar el contacto. No hay medición de altura o abandono que cuantifique su impacto. **RECOMENDACIÓN.** Diseñar con el copy completo de D03, sus cuatro modalidades y sus secciones identificadas; ajustar la composición antes de proponer cambios editoriales. La solución no es recortar textos aprobados para acomodar el layout antiguo.

## 8. Problemas de arquitectura y mantenibilidad

Prioridad: **P0** condiciona publicación o evidencia; **P1** afecta al sistema visual/navegación y debe resolverse en decisiones previas a migración; **P2** deuda técnica a programar después de G1. Ninguna prioridad autoriza cambios productivos en B01.

| ID | Prioridad | Clasificación y evidencia | Impacto real y acción posterior propuesta |
|---|---|---|---|
| B01-01 · Copy y arquitectura editorial divergentes | P1 | **VERIFICADO**; tabla §6; D03 vs HTML | Diseñar sobre la web actual sin correspondencia consolidaría otra web distinta de la aprobada. **RECOMENDACIÓN:** matriz de bloques D03 → maqueta de nueve páginas |
| B01-02 · Estados sin bloqueo | P0 | **VERIFICADO**; HTML:L483–486, L621, L704; validate:L220–243 | `verify` y placeholders se sirven con todo el documento; avisos no fallan. **RECOMENDACIÓN:** definir comportamiento de diseño de referencias ausentes y, tras G1, controles de publicación |
| B01-03 · Datos repetidos y contradictorios | P0 | **VERIFICADO**; HTML:L216, L621, L827, L881, L1062 | La misma experiencia requiere corrección manual en cinco lugares y ya diverge. **RECOMENDACIÓN:** expediente y valor autorizado antes de normalización de contenido |
| B01-04 · Contacto sin cierre demostrado | P0 | **VERIFICADO / NO VERIFICADO**; HTML:L1125–1161, L1200; form:L7–10 | Envío real, servidor y privacidad no acreditados; éxito solo por HTTP. **RECOMENDACIÓN:** definir todos los estados y responsables, probar recepción más adelante |
| B01-05 · Identidad jurídica supuesta | P0 | **VERIFICADO**; HTML:L1199 frente a D03:L9, L1193, L1218 | «S.L.» no tiene soporte en las fuentes examinadas. **RECOMENDACIÓN:** recabar titular real; no validar la afirmación por estar en HTML |
| B01-06 · HTML único | P2 | **VERIFICADO**; index:L121–1174; **INFERIDO** impacto | Añadir página implica editar un monolito, navegación, metadatos y referencias; todos los borradores viajan en la respuesta. **RECOMENDACIÓN:** migración incremental a datos/plantillas después de diseño |
| B01-07 · Cascada acumulativa | P1 | **VERIFICADO**; pages:L182/L254, L292/L379, L343/L395; componentes de especialidad en components | Los valores dependen de la última regla y especificidad. **RECOMENDACIÓN:** documentar propiedad y valor efectivo de cada variante antes de consolidar CSS |
| B01-08 · Pruebas fijan versión editorial anterior | P1 | **VERIFICADO**; tests:L131–156, L197–326; validate:L147–159 | La corrección futura a «Capacidades» haría fallar tests actuales. Tests de conteos/textos no acreditan D03 ni UX. **RECOMENDACIÓN:** planificar actualización de criterios de aceptación, preservando comprobaciones de recursos y enlaces |
| B01-09 · Rutas y SEO solo cliente | P2 | **VERIFICADO**; router:L2–54, L60–102; HTML head | No hay documentos/metadatos HTTP por ruta/idioma. **INFERIDO:** limita enlazado, compartición e indexación independiente. **RECOMENDACIÓN:** mapa de equivalencias de hashes y futuras URLs, después de fijar navegación |
| B01-10 · i18n nominal | P1/P2 | **VERIFICADO**; HTML:L112–117; components:L40–49 | Solo etiquetas de idioma, ningún contenido localizado; selector sin versión móvil. **RECOMENDACIÓN:** diseñar estados publicados/no disponibles y expansiones de texto |
| B01-11 · Acoplamiento al marcado exacto | P2 | **VERIFICADO**; router:L67,L74; validate:L125–133; tests:L43–50 | Router depende de `.nav > ul > li > a`; extractores buscan la cadena exacta `<div class="pagina"…>`, que excluye variantes como Inicio con clase home. Una mejora semántica puede romper validaciones sin romper la web. **RECOMENDACIÓN:** adaptar pruebas cuando migre el contrato de páginas |
| B01-12 · Control de anclas parcial | P2 | **VERIFICADO**; validate:L187–194 | Comprueba ID global, no pertenencia a ruta ni duplicados. Comprobación suplementaria B01 no encontró esos errores actuales. **RECOMENDACIÓN:** ampliar el criterio en la futura validación, sin atribuir fallos inexistentes hoy |
| B01-13 · Recursos y documentación desfasados | P1/P2 | **VERIFICADO**; docs/website-visual-assets.md, apartado Home, habla de slots ocultos; HTML:L171–194/L217–240 los contiene visibles por CSS | Se puede planificar con un estado documental que no representa el código. **RECOMENDACIÓN:** usar este inventario como baseline y marcar antecedentes; no reescribirlos en B01 |
| B01-14 · Entorno no reproducible declarado | P2 | **VERIFICADO**; pyproject:L1–10 | No se declaran pytest ni versiones; sin pipeline. La máquina actual pasa pruebas, otra puede no disponer de tooling. **RECOMENDACIÓN:** declarar entorno mínimo y despliegue tras G1 |
| B01-15 · Accesibilidad de navegación | P1 | **VERIFICADO**; ausencia de salto real/foco de ruta; §7 | Puede dificultar contexto y navegación repetida. **RECOMENDACIÓN:** especificar foco, teclado y menú en D05 y verificar después |

**VERIFICADO.** La separación inicial en cuatro CSS y tres scripts es útil y reduce complejidad respecto a mezclarlo todo en HTML. **INFERIDO.** La deuda procede de contenido duplicado, cascada, estados y contratos, no de no utilizar un framework. No hay evidencia que justifique incorporar React, SPA, CMS o backend de cálculo para resolver estos hallazgos.

## 9. Comparación con documentos 03, 04 y 05

### 9.1. Estado frente al objetivo

| Dimensión | D03 / D04 / D05 | Estado actual | Diagnóstico |
|---|---|---|---|
| Producto editorial | Nueve páginas y Conocimiento fuera del lanzamiento | Nueve vistas + tres fichas + Conocimiento | **VERIFICADO:** cobertura nominal; falta fidelidad de estructura/copy |
| Identidad | Reutilizar marca real; rellenar valores de D05 | Tokens, fuente, logos y layouts disponibles | **VERIFICADO:** material suficiente para especificar la base, no para aprobarla sin maquetas |
| Biblioteca visual | Componentes mínimos y variantes justificadas | Patrones reutilizables, especializaciones y reglas heredadas | **RECOMENDACIÓN:** mapear los existentes; nombres de D05 no obligan a clases nuevas |
| Generación | Python + Jinja2 + Pydantic v2, datos separados | HTML manual; Python valida | **VERIFICADO:** objetivo no implementado; no es tarea B01 |
| CSS/JS | CSS modular, JS progresivo | Modularidad inicial; router necesario para vistas separadas | **VERIFICADO:** CSS reaprovechable; navegación requiere migración posterior |
| Idiomas y URLs | Prefijos es/ca/en/de, slugs explícitos, equivalencias | Hashes con parte de slugs ingleses y contenido ES | **VERIFICADO:** requiere contratos y contenido; no basta activar botones |
| Publicación | Excluir drafts; metadatos y derechos validados | Marcadores y borradores en HTML, avisos no bloqueantes | **VERIFICADO:** distancia sustancial frente al contrato de publicación |
| Contacto | Cuatro campos, servidor seguro, errores y recepción real | Servicio externo, siete controles y privacidad pendiente | **VERIFICADO / NO VERIFICADO:** base cliente útil, cierre funcional no acreditado |
| Estudios | Paquetes de publicación desacoplados, figuras/tablas/informes | Slots y fichas manuales; sin paquete real | **VERIFICADO:** soporte conceptual; integración no demostrada |
| Gate G0 | Inventario y capturas desktop/móvil | Inventario y pruebas obtenidos; capturas fallidas | **NO VERIFICADO:** baseline visual incompleto |
| Gate G1 | Diseño completo y aprobación | D05 declara pendientes; no maquetas aprobadas halladas | **VERIFICADO documental:** G1 no acreditado, no procede refactor |

### 9.2. Tensiones y contradicciones documentales registradas

Se registran para sus propietarios. No se corrige ningún documento ni se adopta unilateralmente una composición nueva.

| Ref. | Fuentes precisas | Diferencia y tratamiento en B01 |
|---|---|---|
| DOC-01 | D02:L12, L137–139 y L213–217; D03:L4–20; D05:L4 | D02 describe D03 todavía por desarrollar y le asigna también UX/componentes. Las fuentes posteriores ya separan copy, arquitectura y diseño. Se registra el desfase; se usa la jerarquía indicada en el encargo |
| DOC-02 | D02:L40, L133, L2337; D03:L29, L143–144 | CAP-DIG sigue pendiente en D02; D03 fija «Automatización y control». La etiqueta pública tiene decisión expresa en D03; equivalentes CA/EN/DE siguen sin aprobación demostrada |
| DOC-03 | D03:L141, L263, L273, L404–409, L552, L668; D03:L4–20, L398, L1054 | Marcadores históricos «pendiente» frente a estado editorial cerrado. El propio D03 explica precedencia. No se trata la versión histórica como nueva reapertura ni se borran sus etiquetas |
| DOC-04 | D03:L1111–1112; D04:L4, L10–12; docs/audits/03-architecture-decision.md:L34 | Historial y auditoría antigua consideran Astro; D04 ratifica Python/Jinja2 y excluye Astro. No hay dos arquitecturas activas; se registra la necesidad de señalizar antecedentes |
| DOC-05 | D03:L112; D05:L38, L50 | Inicio prohíbe mostrar tarjetas de referencias sin evidencia; D05 ilustra tres destacadas/tres complementarias. Es una composición condicionada, no permiso de publicación. Diseñar estado sin referencias autorizadas |
| DOC-06 | D04:L103; D05:L64–65, L68 | D04 habla de wireframes y maquetas responsive de las nueve; D05 exige wireframes de nueve y alta fidelidad de tres con fragmentos críticos para seis. **Decisión pendiente:** precisión del paquete exigido para acta G1. No se declara cerrado el gate bajo una interpretación propia |
| DOC-07 | D03:L744 y D05:L37 | D03 explicita **2 columnas × 3 filas** para Sectores; D05 dice «retícula 2×3», notación potencialmente ambigua. Conservar referencia literal y confirmar orientación en maqueta, sin asumir tres columnas |
| DOC-08 | D03:L977, L1188, L1216 | Tres formulaciones de éxito, incluida decisión posterior 03.K.2. Registrar cuál se trasladará a especificación de estados conforme a precedencia editorial; no combinar textos. HTML usa otra formulación en form:L8 |
| DOC-09 | D03:L987–990, L1183, L1210–1218 | Marcador histórico de correo pendiente frente a info@bafras.com confirmado. La decisión está cerrada documentalmente; la operatividad técnica sigue sin comprobarse |
| DOC-10 | D04:L113–115; CNAME:L1 | Dominio canónico figura pendiente aunque existe CNAME bafras.com. No hay contradicción obligada: presencia de dominio no resuelve www, HTTPS, redirecciones o política canónica. Confirmar operación |

**VERIFICADO.** D04 y D05 son complementarios: responsabilidades software frente a composición/UX. Su complementariedad no elimina la necesidad de concretar el criterio documental de G1 señalado en DOC-06.

## 10. Compatibilidad con la futura publicación de estudios

La evaluación se limita a condicionantes actuales. Los formatos y contratos de D04:L69–93 son referencia futura; no se diseña ni implementa un sistema de publicación en B01.

| Necesidad | Lo que ya existe | Limitación concreta | Evaluación |
|---|---|---|---|
| Fichas de proyectos BAFRAS | Tres fichas manuales de experiencia, `dl`, texto, medios, enlaces | No hay registro estructurado, permiso/estado validado o ruta independiente; añadir ficha exige cambios en HTML/router/navegación | **VERIFICADO.** Patrón HTML aprovechable; migración posterior necesaria para repetibilidad |
| SVG/PNG/WebP | Recursos de esos formatos, SVG inline, WebP con alt/dimensiones | No hay modelo media con derechos, caption/unidades/locale; slots no prueban integración de resultados | **VERIFICADO.** Los formatos no encuentran una barrera estructural en la web estática |
| PDF | Hosting compatible con archivos estáticos por diseño | No se encuentran PDF o enlaces de informe que permitan verificar descarga y metadatos | **INFERIDO:** viable como recurso estático; **NO VERIFICADO:** hosting/MIME, accesibilidad y documento real |
| Tablas técnicas | Listas y `dl` actuales | No hay `<table>` de datos ni estilos de tabla/overflow de estudios; falta ejemplo con unidades, caption y encabezados | **VERIFICADO.** Falta patrón probado, no exige un framework |
| Gráficos interactivos | JS nativo y espacio de evidencia | No hay visualizador, librería, datasets ni ciclo de vida de gráficos entre vistas; no hay fallback real demostrado | **INFERIDO:** posible como mejora progresiva; alcance por muestra real, no por tecnología supuesta |
| Informes HTML independientes | Un sitio estático puede alojar otro documento | No hay informes, iframe, aislamiento, sanitización o CSP versionada que se puedan auditar | **NO VERIFICADO:** compatibilidad concreta de estilos/scripts. Incorporación directa podría colisionar con selectores globales `form`, `label`, `p`, `h*` |
| Metadatos y recursos de estudio | `data-asset-id`, `data-asset-kind`, estados de trabajo | No equivalen a manifest versionado, procedencia, release, metodología, permisos o clasificación de datos | **VERIFICADO:** trazabilidad parcial reutilizable, sin validación contractual |
| Independencia de motores | No existen imports o dependencias de simulaciones | No se dispone de exportaciones reales de los dos softwares | **VERIFICADO:** ausencia de acoplamiento actual; **NO VERIFICADO:** preparación de exportadores |
| Multilingüe | Copia ES manual | No hay captions/alt/resúmenes por idioma ni tratamiento de ficha inexistente en otro locale | **VERIFICADO:** requiere contenido y estados por idioma antes de publicar equivalencias |

**INFERIDO.** La principal barrera no es servir imágenes o PDFs; son la repetibilidad de fichas, el control de publicación, las rutas, los metadatos y el aislamiento de informes. El CSS global y el router son condicionantes reales para integrar HTML/gráficos sin romper el sitio. No hay evidencia que obligue a API, base de datos, colas o ejecución Python online.

**RECOMENDACIÓN.** Conservar como puntos de partida la figura con alternativa textual, el bloque de atribución, `dl` de datos descriptivos y la composición de evidencia. Para D05, bastará especificar tarjeta/ficha/módulo de resultados con muestras anonimizadas cuando existan; su falta no bloquea el diseño corporativo (D05:L67). No imponer a los softwares una librería de gráficos ni un modelo físico universal.

## 11. Elementos recomendados para conservar

Todas las decisiones de esta sección son **RECOMENDACIONES** basadas en los elementos verificados en §§4–5.

1. **Marca y paleta reales:** pino, verde, stone, tinta, gris claro y blanco; superficies cálidas existentes; trazado del logo/símbolo. Confirmar el fichero maestro sin redibujar marca.
2. **Inter y su jerarquía sobria:** familia compartida, pesos moderados, títulos fluidos y ancho de lectura limitado. Revisar pesos pedidos y microtexto antes de cerrar tokens.
3. **Contenedor y gramática editorial:** `.envoltura`, separación por líneas, layouts editorial/evidence/feature, con variantes demostradas. Mantener la opción de filas amplias, no convertir todas las secciones en tarjetas.
4. **Botones y enlaces:** variante llena, contorno, contraste sobre oscuro y foco visible; completar estados con la misma identidad.
5. **Patrones técnicos:** listas de entregables, mapas numerados, ficha `dl`, métricas con contexto, evidencia destacada y complementaria; adaptar jerarquía al copy aprobado.
6. **Recursos gráficos existentes:** WebP conceptual de Inicio como ilustración, original PNG como fuente, retratos y fotografías disponibles condicionados a identificación y permiso.
7. **Atribución explícita:** conservar la distinción de experiencia previa presente en Inicio/INF/ENE y extender su consistencia a tarjetas y fichas una vez verificadas.
8. **Base de contacto:** email accionable, labels persistentes, required/email/autocomplete, bloqueo de doble envío y `role=status`. El envío real y los estados deben verificarse posteriormente.
9. **Tooling útil:** comprobaciones de archivos, carga CSS/JS, recursos y enlaces. Conservar su finalidad, actualizando los supuestos editoriales cuando corresponda.
10. **Separación web/motores:** no hay acoplamiento actual que mantener con simulaciones externas; conservar esta independencia en la futura migración.

## 12. Riesgos y decisiones pendientes

| Decisión / información necesaria | Propietario propuesto | Evidencia o respuesta que falta | Relación con diseño y publicación |
|---|---|---|---|
| Alcance exacto del acta G1 | Dirección + UX + arquitectura | Resolver DOC-06: nueve maquetas completas o nueve wireframes + tres alta fidelidad + fragmentos críticos | Necesario para saber cuándo se autoriza refactor |
| Matriz editorial de nueve páginas | Editorial + UX + ingeniería INF/ENE/DIG | Cada ID de D03, orden, texto íntegro, enlace y tratamiento visual; sin trasladar notas internas | Insumo principal del Bloque 02 |
| Maestro de marca y variantes | Branding + dirección | Logo válido, usos horizontal/vertical, símbolo, tamaños, licencia/condiciones de Inter | Cierra identidad sin rediseñarla |
| Permisos de recursos | Titulares + responsables de proyecto | Fuente/licencia de hero, conceptual, retratos y seis fotos MEP; versiones autorizadas y alt | El diseño debe admitir recursos ausentes |
| Expedientes de seis referencias | Cada fundador + editorial | Rol, empleador, periodo, alcance, fases, entregables, datos y permisos según D03:L1178 | Referencias concretas siguen condicionadas; no presentarlas como BAFRAS |
| Cifras UIB y responsabilidades | Titular de la referencia + revisión técnica | Fuente que explique 7.4/7.576/≈7.6 MWp, capacidades BESS, recarga y financiación | Ninguna cifra se valida por repetición en la web |
| Identidad jurídica | Dirección + asesoría correspondiente | Titular real y datos publicables; confirmar o rectificar «S.L.» | Condiciona pie, privacidad y recogida de datos |
| Operación de contacto | Operaciones + desarrollo | Proveedor efectivo, buzón receptor probado, gestión de errores/abuso, responsable y tratamiento real | D05 debe representar carga/éxito/error; publicación exige prueba real |
| Idiomas | Editorial + revisores humanos | Variante CA, nomenclaturas CA/EN/DE, textos completos y calendario de versiones publicadas | Diseñar largos de texto y selector; no activar idiomas ficticios |
| Hosting y URLs | Arquitectura + operaciones + SEO | Origen, rama/carpeta, dominio canónico, rutas, 404 y futura compatibilidad de enlaces hash | Se define para migración; no bloquea inventariar identidad |
| Estudios | Responsables de ambos softwares | Muestra anonimizada, formatos, tamaños, tablas/unidades, scripts requeridos y permisos | Permite demostrar módulo de resultados; no bloquea G1 corporativo |
| Verificación visual | QA + UX | Navegador operativo, capturas 1440/768/390/320 y anchos intermedios, teclado/zoom/lector | G0 visual pendiente; ninguna captura se sustituye por inspección estática |

**NO VERIFICADO.** No se aportan actas de aprobación visual previas, expedientes de proyectos o licencias que cierren estas decisiones. Los documentos existentes bastan para orientar el diseño, pero no para afirmar que todas las referencias y datos están autorizados para publicación.

## 13. Recomendaciones priorizadas para el Bloque 02 — Sistema visual

Las siguientes son **RECOMENDACIONES de trabajo futuro**. Este informe no ejecuta el Bloque 02 ni modifica D05.

| Orden | Trabajo concreto | Resultado revisable esperado | Criterio de aceptación |
|---|---|---|---|
| 1 · P1 | Completar inventario de D05 desde §4 | Tabla de tokens reales y aliases, fuente/pesos, espaciado efectivo, breakpoints, marca y variantes | Cada valor tiene procedencia; no se inventa paleta, fuente o escala sustituta |
| 2 · P1 | Fijar correspondencia editorial de §6 | Matriz de las nueve páginas con IDs D03 y orden; distinguir bloques nuevos de reutilizables | H01–H07/C01–C05/INF/ENE/DIG/SEC/PE/SB/CO completos; Conocimiento fuera del lanzamiento conforme D03 |
| 3 · P1 | Definir catálogo mínimo desde §5 | Fichas de variantes existentes, tamaños y estados; reglas comunes y excepciones justificadas | No crear un componente por sección; documentar la cascada que hoy produce cada aspecto |
| 4 · P1 | Resolver navegación y formularios en diseño | Cabecera desktop/móvil, selector publicado/no disponible, foco/salto, CTA y cuatro campos de Contacto; carga/error/éxito | Navegación coherente con D03; sin `#` legales ficticios en prototipo final; estados comprensibles y accionables |
| 5 · P1 | Wireframes responsive de nueve páginas | Escritorio y móvil con copy íntegro y referencias de bloque | Cuatro ámbitos INF + transversal; seis ámbitos ENE/DIG + transversal; seis sectores; referencias 3+3 condicionadas |
| 6 · P1 | Alta fidelidad de páginas patrón | Inicio, Infraestructuras y Contacto, más demostración de cobertura de las otras seis | Revisión de densidad, anchos, títulos largos, contrastes y anchos intermedios; alcance de acta G1 previamente aclarado |
| 7 · P1 | Lenguaje de diagramas INF/ENE/DIG | Especificaciones conceptuales consistentes, leyendas y alternativa móvil/textual | Diferenciar señal/actuación y flujos; no inventar conexiones o datos reales; conservar identidad |
| 8 · P1 | Estados sin evidencia disponible | Ejemplos de experiencia sin referencia autorizada y de medio ausente | Sin clientes/cifras/botones a fichas no verificadas; no rellenar con fotografías que simulen evidencia |
| 9 · P2 | Especificar estudios a nivel visual | Tarjeta, ficha y módulo de resultados, probados con muestra cuando exista | Funciona con figura + PDF; tablas legibles; JS opcional; no depende de un motor o librería de gráficos |
| 10 · Cierre | Revisión multidisciplinar y acta G1 | Conformidad diseño/copy, estados, responsive, accesibilidad y excepciones explícitas | Dirección aprueba el diseño con evidencia; solo entonces se plantea la intervención de refactorización |

**Estado al cierre de B01:** diagnóstico y documentación entregados; pruebas estructurales satisfactorias; baseline visual de navegador pendiente; sin cambios productivos, sin alteración de documentos 02–05, sin dependencias instaladas y sin implementación de arquitectura futura.
