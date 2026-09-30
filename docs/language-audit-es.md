# Auditoría lingüística — BAFRAS.com ES

## 1. Objetivo

BAFRAS.com tendrá versiones en español, inglés y alemán. Esta auditoría corresponde a la versión española y busca que interfaz, contenido editorial y taxonomía comercial mantengan un uso coherente del español, sin traducir de forma artificial marcas, acrónimos ni vocabulario técnico internacional.

## 2. Alcance auditado

- Archivos de contenido y configuración revisados: `index.html`; estructura del repositorio y carpeta `docs/`.
- El sitio está implementado en un único HTML con vistas delimitadas por `data-pagina`; no se encontraron fuentes de contenido adicionales ni dependencias de interfaz.
- Vistas y secciones revisadas: cabecera y navegación; Home; capacidades y fichas; sectores; proyectos y fichas de experiencia; conocimiento; sobre BAFRAS/equipo; contacto y colaboración; footer.
- Fuentes de texto: HTML visible, objeto JavaScript `TITULOS`, metadatos iniciales y dinámicos, opciones y estados del formulario, tooltips `title`, nombres accesibles `aria-label` y textos asignados desde JavaScript al enviar el formulario.
- Imágenes y SVG: los retratos reciben `alt=""` y son decorativos; el logo expone el nombre de marca. El texto `ENGINEERING` forma parte del logotipo oficial.
- Baseline Git: rama `feat/contingut-v2`; `index.html` ya aparecía modificado al iniciar esta tarea por la iteración previa de Home. Ese trabajo se conservó. No había carpeta `docs/`.

## 3. Criterios

- La interfaz y el contenido editorial se expresan en español.
- Los nombres comerciales de capacidades y sectores se normalizan con el glosario español.
- Acrónimos técnicos, marcas, estándares y nombres propios se mantienen cuando su forma internacional es natural.
- Se adapta el inglés técnico solo cuando una formulación española resulta clara y habitual; no se traducen slugs, identificadores ni nombres de variables.
- Se revisan por contexto los metadatos y atributos accesibles, además del texto visible.

## 4. Hallazgos

| Ubicación | Texto anterior | Clasificación | Texto nuevo | Motivo |
|---|---|---|---|---|
| Navegación, Home, fichas, referencias, formulario y footer | Infrastructure / Infrastructure & Engineering | ADAPTAR | Infraestructura e Ingeniería | Nombre canónico de la capacidad. |
| Navegación, Home, fichas, referencias, formulario y footer | Energy Systems | ADAPTAR | Sistemas Energéticos | Nombre canónico de la capacidad. |
| Navegación, Home, fichas, referencias, formulario y footer | Digital Systems / Digital Systems & Automation | ADAPTAR | Sistemas Digitales y Automatización | Nombre canónico completo de la capacidad. |
| Navegación, tarjetas, vista de sectores y metadatos | Hospitality | TRADUCIR | Hoteles y turismo | Se elige una formulación directa, adecuada a navegación y sector. |
| Textos de hotelería y turismo | resorts | TRADUCIR | complejos turísticos | Equivalente natural en español; no se conserva un anglicismo decorativo. |
| Títulos sectoriales | Edificios y terciario / Infrastructure (sector) | ADAPTAR | Edificios y sector terciario / Infraestructuras | Distingue el sector de la capacidad Infraestructura e Ingeniería. |
| Formulario y colaboración | Project Manager(s) | ADAPTAR | responsable(s) de proyecto; dirección de proyectos para la función | La formulación distingue el rol profesional de la función. |
| Metodología de Home | commissioning | ADAPTAR | verificación; junto a “puesta en marcha” | Evita duplicar en inglés una actividad ya expresada en español. |
| Proyecto y biografía de energía marina | offshore | ADAPTAR | eólica marina / entornos marinos | Describe el sector o entorno con términos españoles naturales. |
| Biografía del equipo | machine learning / edge machine learning | ADAPTAR | aprendizaje automático / aprendizaje automático en dispositivos periféricos | Prioriza el español; la segunda equivalencia queda sujeta a validación técnica. |
| Tooltip del selector | Català: pendent de traducció; English: translation pending; Deutsch: Übersetzung ausstehend | TRADUCIR | Catalán, Inglés y Alemán: traducción pendiente | Los tooltips también forman parte de la interfaz accesible en español. |
| `aria-label` del diagrama de Home | Infrastructure, Energy Systems y Digital Systems forman un sistema conectado | ADAPTAR | Sistema conectado: Infraestructura e Ingeniería, Sistemas Energéticos y Sistemas Digitales y Automatización | Mantiene el nombre accesible alineado con las etiquetas visibles. |
| Metadatos iniciales y objeto `TITULOS` | Nombres de capacidades y hospitality en inglés | ADAPTAR | Nombres canónicos españoles en títulos y descripciones | El título del documento y los metadatos cambian junto con cada ruta. También se completaron descripciones de proyecto que terminaban truncadas, usando información ya presente en sus fichas. |
| Marca, logotipo y nombres propios | BAFRAS Engineering; ENGINEERING; LinkedIn; Python; MATLAB; Dogger Bank A; Vineyard Wind 1; NextGenerationEU; PITEIB | MANTENER | Sin cambios | Marca, nombres oficiales de proyectos/organizaciones y productos. |
| Contenido técnico | BMS, SCADA, BESS, VPP, V2G, AMI, HVAC, MEP, CAPEX, OPEX, FV, MWp, MWh | MANTENER | Sin cambios | Acrónimos y unidades usados de forma habitual en ingeniería y energía. PLC no aparece en el contenido auditado. |
| Selector de idioma | ES / CA / EN / DE, botones de CA/EN/DE deshabilitados | MANTENER | Sin cambio funcional; tooltips en español | Los idiomas no implementados no parecen seleccionables ni provocan una traducción parcial. |
| Rutas e identificadores | `capacidades/infrastructure`, `energia-offshore-internacional`, claves de `TITULOS` | MANTENER | Sin cambios | Son slugs e identificadores internos, no etiquetas visibles; se conservan para no romper routing. |

## 5. Cambios realizados

- **Navegación:** nombres canónicos de capacidades y sectores; tooltips del selector en español.
- **Home:** diagrama visible y `aria-label`, capacidades, sectores, etiquetas de experiencia, metodología y referencias normalizados sin reescribir la estructura anterior.
- **Capacidades:** encabezados, migas de pan, responsabilidades, referencias de sector y enlaces relacionados traducidos.
- **Sectores:** “Hoteles y turismo”, “Edificios y sector terciario” e “Infraestructuras” aplicados de forma consistente.
- **Proyectos/experiencia:** etiquetas de capacidades y expresiones de eólica marina en español; se mantiene la atribución de experiencia previa.
- **Equipo:** roles y referencias de capacidad normalizados; términos de aprendizaje automático y eólica marina adaptados.
- **Contacto/colaboración:** opción de dirección de proyectos y opciones de capacidad en español; sin cambios al envío del formulario.
- **Footer:** enlaces de capacidad traducidos; marca legal conservada.
- **Interfaz:** mensajes de envío, error y confirmación revisados; ya estaban en español y no se modificaron.
- **Metadata/accesibilidad:** descripción inicial, títulos/descripciones dinámicos y `aria-label` del diagrama normalizados. El logo conserva su nombre accesible de marca.

## 6. Términos mantenidos en inglés/internacionales

- **Marca y nombres oficiales:** BAFRAS Engineering, el texto del logotipo ENGINEERING, LinkedIn, Python, MATLAB, Dogger Bank A, Vineyard Wind 1, NextGenerationEU y PITEIB.
- **Ingeniería, energía y unidades:** BMS, SCADA, BESS, VPP, V2G, AMI, HVAC, MEP, CAPEX, OPEX, FV, MWp y MWh. Se mantienen por su uso técnico internacional; el contenido circundante está en español.
- **Códigos del selector:** ES, CA, EN y DE; son códigos de idioma, y los botones de idiomas pendientes siguen deshabilitados.
- **No visibles:** slugs como `offshore`, `infrastructure` y `energy-systems`, IDs, nombres de clases CSS y claves internas de metadata. No se traducen porque alterarlos afectaría navegación o implementación.

## 7. Casos pendientes

- Validar con el equipo técnico que “aprendizaje automático en dispositivos periféricos” refleja con precisión el sentido de `edge machine learning` en la biografía.
- Confirmar si en futuras páginas técnicas conviene desarrollar MEP en su primera aparición; se mantiene aquí porque es un acrónimo aceptado por el público profesional.
- Las versiones CA, EN y DE continúan sin implementar. El comportamiento actual —botones deshabilitados con tooltips en español— es explícito y no ofrece navegación parcial.
- En el test sintético que fuerza cambios de ruta consecutivos se observó `InvalidStateError` al abortar transiciones `document.startViewTransition`; no se reprodujo en la navegación normal probada con pausa. Es comportamiento del routing/transición previo, fuera del alcance de esta normalización.
- En la auditoría inicial se observó desbordamiento horizontal en el menú móvil compartido. Se corrigió posteriormente con un ajuste responsive localizado de logo y espaciado; la validación final entre 256 y 390 px CSS no encontró overflow.

## 8. Validación

- Comparación del texto renderizado en las vistas de capacidades, sectores, proyectos y experiencia, conocimiento, equipo y contacto: sin coincidencias de los términos ingleses editoriales auditados.
- Revisión del selector, opciones del formulario, `aria-label`, tooltips, títulos y descripciones dinámicos.
- Navegación por hash conservada; las claves y slugs no se modificaron.
- Se revisaron vistas desktop, tablet y móvil en Live Server; los textos largos de capacidad se adaptan por línea. La prueba de navegación normal no registró errores de consola; la automatización rápida de cambios de ruta produjo la excepción de transición descrita en casos pendientes.
- El desbordamiento móvil detectado en la auditoría inicial se corrigió después con un ajuste responsive localizado del header/footer y ya no se reproduce entre 256 y 390 px CSS.
- `git diff --check` y diagnóstico del editor sin errores.
- No se añadieron dependencias ni se modificaron CNAME, configuración de despliegue o dominio.
