# BAFRAS Engineering — B02-PREP-01 · Consolidación G1 e inventario de recursos visuales

Fecha: **03/11/2026**, Europe/Madrid. Alcance autorizado: documentación e inspección. **G1 no iniciado ni completado. No se han diseñado páginas, integrado imágenes ni avanzado a B02.1.**

Las rutas se expresan respecto a `bafras/`. Biblioteca inspeccionada: `media-library/`, abreviada **LIB**. Los identificadores `R01…R55` son de esta inspección; `lib:H01`, `lib:I01`, etc. pertenecen al paquete y **no son los IDs de bloques editoriales D03**. La coincidencia entre algunos nombres no establece equivalencia editorial.

Clasificación de conclusiones: **VERIFICADO** = lectura, inspección visual o comprobación local; **INFERIDO** = deducción razonada; **NO VERIFICADO** = requiere comprobación adicional; **RECOMENDACIÓN** = propuesta posterior. La calidad visual se valora de forma aparente en las hojas de contactos, sin certificar nitidez de cada original al 100 %.

## 1. Resumen ejecutivo

**VERIFICADO.** D04 y D05 expresan ahora un único contrato G1: nueve wireframes completos en escritorio y móvil trazables a D03; tres maquetas completas de alta fidelidad —Inicio, Infraestructuras e instalaciones y Contacto—; módulos singulares detallados de las otras seis páginas; catálogo aprobado de componentes y estados; especificación visual; revisión global sin decisiones estéticas fundamentales abiertas; y aprobación expresa de dirección documentada. No se exigen nueve prototipos completos independientes cuando los patrones aprobados permiten reconstruir cada página inequívocamente.

**VERIFICADO.** La biblioteca existe y contiene **91 archivos: 55 imágenes y 36 archivos auxiliares**. Hay **29 WebP preparados**, **23 JPEG**, **2 MPO con extensión `.jpg`** y **1 TIFF**. Los 26 originales corresponden a 26 fotografías y los otros tres WebP son gráficos demostrativos con datos sintéticos. Todos los archivos de imagen se abrieron para inspección y generación de miniaturas. Peso conjunto: **104661354 bytes (99.81 MiB)**; los 29 WebP suman **5130586 bytes (4.89 MiB)**. No se detectó transparencia ni duplicados exactos SHA-256.

**VERIFICADO.** Las 26 parejas original/WebP tienen contenido visual correspondiente y versiones con encuadre o formato diferente. Los SHA-1 de los 26 originales coinciden con las fichas `source.json` locales. Esto prueba coherencia con los registros entregados; **no** prueba por sí mismo la autenticidad de la fuente externa ni los derechos de publicación.

**VERIFICADO.** La documentación del paquete aporta autores, URLs, licencias y estados declarados. Contradice una lectura genérica de «todo dominio público»: las 29 entradas READY declaran **20 CC BY/CC BY-SA**, **5 Public domain**, **1 CC0** y **3 Propio (BAFRAS Engineering)**. El paquete afirma haber verificado licencias; en esta intervención no se ha verificado independientemente esa afirmación. El uso comercial y las condiciones aplicables quedan pendientes de revisión por recurso.

**VERIFICADO.** Se han observado instalaciones eléctricas y mecánicas, energía, control, industria, edificios, personas en trabajo técnico y gráficos conceptuales/demostrativos. Hay material para estudiar candidatos editoriales. **RECOMENDACIÓN.** No usar estas imágenes como prueba de experiencia de BAFRAS, ni sus operadores como retratos del equipo; no forzar fotografías en Contacto o en todos los bloques.

**VERIFICADO.** Se generaron **cinco hojas de contactos** con las 55 imágenes, nombre, ID, dimensiones, formato y carpeta. Hay siete entradas del manifiesto sin imagen: H02, E08, D05, D07 y X01–X03; su ausencia coincide con sus estados pendientes. Las referencias profesionales, retratos propios, diagramas específicos y resultados de estudios siguen necesitando recursos auténticos o alternativas visuales.

## 2. Alcance y método de inspección

### 2.1. Fuentes y jerarquía

Se consultaron D02 (posicionamiento, necesidad antes que tecnología, evidencia y localización), D03 (contenido editorial y reglas de imágenes), D04 y D05 **completos antes de editar**, y B01 (§§4–7, 9 y 12–13, en particular DOC-06). Las correspondencias de §6 proceden **exclusivamente de D03**: `03_contenido_editorial.md`, edición definitiva del 02/11/2026. No se tomó copy de `index.html` ni la clasificación comercial del paquete como autoridad editorial.

D02 aporta contexto estratégico; D03 gobierna textos, contenidos, estructura, servicios y orden de secciones; D04 gobierna implementación; D05 gobierna identidad/UX/composición. La web existente es referencia técnica y visual. El paquete de imágenes es material provisional, no una orden para cambiar páginas, copiar directorios o publicar recursos.

Se leyeron `LIB/README.md`, `manifests/media-manifest.yaml`, `manifests/assets-inventory.csv`, `manifests/attribution.md`, las 26 fichas `originals/*/source.json` y el informe de adquisición. Las instrucciones de integración y generación que contienen se trataron como antecedentes: **no se ejecutaron** los scripts `demo_graphics.py`, comandos de copia ni ejemplos de integración del paquete.

### 2.2. Procedimiento técnico y visual

**VERIFICADO.** Recorrido recursivo de todos los archivos; apertura con Pillow ya instalado; lectura de formato real, dimensiones, modos, fotogramas, transparencia, EXIF/XMP/comentarios y tamaños; hashes SHA-256 de cada imagen y comparación SHA-1 de originales con registros entregados; cotejo de dimensiones/pesos WebP con YAML. YAML se leyó con PyYAML ya instalado. No hubo instalaciones ni modificaciones del entorno.

Se crearon miniaturas proporcionales incrustadas en cinco JPEG de contacto, sin copias completas adicionales de los originales. Se aplicó orientación EXIF al presentar; el TIFF binario se pasó a RGB únicamente en memoria para suavizar la miniatura. Para MPO se representó el primer fotograma. Se observaron las cinco hojas, incluidos originales y variantes; R02 y R11 se revisaron además directamente a resolución original para leer los avisos de datos sintéticos. No se editó ningún original.

**NO VERIFICADO.** No se inspeccionaron visualmente los segundos fotogramas MPO ni se hizo una evaluación 1:1 exhaustiva de los 26 originales. No se consultaron páginas externas de licencia, no se buscaron fotos adicionales y no se afirma revisión jurídica. Los metadatos documentan declaraciones; su presencia no acredita derechos y su ausencia tampoco equivale a ausencia de derechos.

### 2.3. Edición documental G1 realizada

| Documento | Apartado modificado | Cambio acotado |
|---|---|---|
| [D04](04_arquitectura_software_V2_4_handoff_G1.md) | §8 «Calidad, pruebas y gates», entrada G1 y párrafo inmediato de alcance | Sustituye la exigencia ambigua de maquetas de nueve páginas por el contrato aprobado; remite a D05 §8; distingue aprobación de diseño, planificación de implementación y preparación de publicación |
| [D05](05_sistema_visual_V4_12_baseline_G1.md) | §8 «Entregables obligatorios del diseño ANTES del refactor» | Precisa catálogo aprobado, wireframes completos, tres maquetas y módulos de las seis restantes; conserva inventario, diagramas y estudios; explicita especificación visual, revisión global y acta de dirección |

Se revisaron referencias a G0, prototipos y refactorización en D04 §§1, 8 y 10 y D05 §§1, 8 y 9. G0 sigue siendo baseline; G1 no equivale a G4 ni G5. No se alteran el stack Python/Pydantic v2/Jinja2, CSS o JS ni los demás gates. La aprobación futura G1 autoriza planificar implementación; no sustituye la autorización de una intervención productiva. Esta decisión documental resuelve el alcance señalado por B01/DOC-06; B01 se conserva como informe histórico sin modificación.

## 3. Inventario técnico

### 3.1. Lectura de las tablas y evidencias

El siguiente inventario contiene **los 55 archivos existentes**, no las 36 entradas conceptuales del manifiesto. Los enlaces apuntan al archivo original de cada fila. `H` = horizontal, `V` = vertical, `C` = cuadrada. Los 55 son H. Tamaños en KiB/MiB binarios, sin ambigüedad de unidad. La relación reducida y el cociente ancho/alto se registran también en el JSON.

**VERIFICADO.** Ninguna imagen dispone de canal alfa/transparencia efectiva en los formatos inspeccionados. `Meta sí` significa que se encontró al menos una etiqueta EXIF de descripción/autor/copyright o un bloque XMP/comentario potencialmente relevante; no que todos incluyan licencia. Se conservan en el [inventario técnico completo](evidencias_B02_recursos/inventario_tecnico.json) valores EXIF relevantes y extractos de hasta 3000 caracteres por bloque XMP/comentario, SHA-256, procedencias declaradas, fotogramas, observaciones visuales y ubicación en la hoja.

| ID / paquete | Ruta relativa a LIB (incluye nombre) | Formato | Dimensiones / aspecto | Tamaño | Orient. / alfa | Meta autoría/licencia potencial |
|---|---|---|---|---|---|---|
| R01 / D01 | [assets/images/capabilities/digital/automation/digital-plc-control-panel.webp](../../assets/images/capabilities/digital/automation/digital-plc-control-panel.webp) | WEBP | 1600×1200 · 4:3 | 200.8 KiB | H / no | No embebidos detectados |
| R02 / D06 | [assets/images/capabilities/digital/data/digital-data-analysis.webp](../../assets/images/capabilities/digital/data/digital-data-analysis.webp) | WEBP | 1600×1200 · 4:3 | 91.6 KiB | H / no | No embebidos detectados |
| R03 / D02 | [assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp](../../assets/images/capabilities/digital/instrumentation/digital-industrial-instrumentation.webp) | WEBP | 1600×1200 · 4:3 | 109.2 KiB | H / no | No embebidos detectados |
| R04 / D04 | [assets/images/capabilities/digital/scada/digital-building-management.webp](../../assets/images/capabilities/digital/scada/digital-building-management.webp) | WEBP | 1600×1200 · 4:3 | 100.5 KiB | H / no | No embebidos detectados |
| R05 / D03 | [assets/images/capabilities/digital/scada/digital-scada-screen.webp](../../assets/images/capabilities/digital/scada/digital-scada-screen.webp) | WEBP | 1600×1200 · 4:3 | 109.9 KiB | H / no | No embebidos detectados |
| R06 / E01 | [assets/images/capabilities/energy/analysis/energy-demand-analysis.webp](../../assets/images/capabilities/energy/analysis/energy-demand-analysis.webp) | WEBP | 1600×1200 · 4:3 | 62.6 KiB | H / no | No embebidos detectados |
| R07 / E05 | [assets/images/capabilities/energy/electrification/energy-ev-charging.webp](../../assets/images/capabilities/energy/electrification/energy-ev-charging.webp) | WEBP | 1600×1200 · 4:3 | 244.3 KiB | H / no | No embebidos detectados |
| R08 / E06 | [assets/images/capabilities/energy/electrification/energy-heat-pumps.webp](../../assets/images/capabilities/energy/electrification/energy-heat-pumps.webp) | WEBP | 1600×1200 · 4:3 | 240.0 KiB | H / no | No embebidos detectados |
| R09 / E04 | [assets/images/capabilities/energy/generation/energy-electrical-infrastructure.webp](../../assets/images/capabilities/energy/generation/energy-electrical-infrastructure.webp) | WEBP | 1600×1200 · 4:3 | 110.6 KiB | H / no | No embebidos detectados |
| R10 / E02 | [assets/images/capabilities/energy/generation/energy-pv-rooftop.webp](../../assets/images/capabilities/energy/generation/energy-pv-rooftop.webp) | WEBP | 1600×1200 · 4:3 | 368.8 KiB | H / no | No embebidos detectados |
| R11 / E07 | [assets/images/capabilities/energy/management/energy-management-dashboard.webp](../../assets/images/capabilities/energy/management/energy-management-dashboard.webp) | WEBP | 1600×1200 · 4:3 | 67.6 KiB | H / no | No embebidos detectados |
| R12 / E03 | [assets/images/capabilities/energy/storage/energy-battery-storage.webp](../../assets/images/capabilities/energy/storage/energy-battery-storage.webp) | WEBP | 1600×1200 · 4:3 | 109.2 KiB | H / no | No embebidos detectados |
| R13 / I08 | [assets/images/capabilities/infrastructure/construction/infra-commissioning-testing.webp](../../assets/images/capabilities/infrastructure/construction/infra-commissioning-testing.webp) | WEBP | 1600×1200 · 4:3 | 138.4 KiB | H / no | No embebidos detectados |
| R14 / I07 | [assets/images/capabilities/infrastructure/construction/infra-construction-site.webp](../../assets/images/capabilities/infrastructure/construction/infra-construction-site.webp) | WEBP | 1600×1200 · 4:3 | 126.0 KiB | H / no | No embebidos detectados |
| R15 / I01 | [assets/images/capabilities/infrastructure/electrical/infra-electrical-distribution.webp](../../assets/images/capabilities/infrastructure/electrical/infra-electrical-distribution.webp) | WEBP | 1600×1200 · 4:3 | 79.7 KiB | H / no | No embebidos detectados |
| R16 / I06 | [assets/images/capabilities/infrastructure/engineering/infra-technical-plans.webp](../../assets/images/capabilities/infrastructure/engineering/infra-technical-plans.webp) | WEBP | 1600×1200 · 4:3 | 247.6 KiB | H / no | No embebidos detectados |
| R17 / I02 | [assets/images/capabilities/infrastructure/mechanical/infra-hvac-plant.webp](../../assets/images/capabilities/infrastructure/mechanical/infra-hvac-plant.webp) | WEBP | 1600×1200 · 4:3 | 277.2 KiB | H / no | No embebidos detectados |
| R18 / I03 | [assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp](../../assets/images/capabilities/infrastructure/mechanical/infra-ventilation-ductwork.webp) | WEBP | 1600×1200 · 4:3 | 170.6 KiB | H / no | No embebidos detectados |
| R19 / I05 | [assets/images/capabilities/infrastructure/plumbing-fire/infra-fire-protection.webp](../../assets/images/capabilities/infrastructure/plumbing-fire/infra-fire-protection.webp) | WEBP | 1600×1200 · 4:3 | 182.8 KiB | H / no | No embebidos detectados |
| R20 / I04 | [assets/images/capabilities/infrastructure/plumbing-fire/infra-plumbing-piping.webp](../../assets/images/capabilities/infrastructure/plumbing-fire/infra-plumbing-piping.webp) | WEBP | 1600×1200 · 4:3 | 213.8 KiB | H / no | No embebidos detectados |
| R21 / H05 | [assets/images/home/capabilities/home-cap-digital.webp](../../assets/images/home/capabilities/home-cap-digital.webp) | WEBP | 1600×1200 · 4:3 | 158.5 KiB | H / no | No embebidos detectados |
| R22 / H04 | [assets/images/home/capabilities/home-cap-energy.webp](../../assets/images/home/capabilities/home-cap-energy.webp) | WEBP | 1600×1200 · 4:3 | 133.1 KiB | H / no | No embebidos detectados |
| R23 / H03 | [assets/images/home/capabilities/home-cap-infrastructure.webp](../../assets/images/home/capabilities/home-cap-infrastructure.webp) | WEBP | 1600×1200 · 4:3 | 184.4 KiB | H / no | No embebidos detectados |
| R24 / H01 | [assets/images/home/hero/home-hero-engineering.webp](../../assets/images/home/hero/home-hero-engineering.webp) | WEBP | 1920×1080 · 16:9 | 217.8 KiB | H / no | No embebidos detectados |
| R25 / S01 | [assets/images/sectors/hospitality/sector-hospitality.webp](../../assets/images/sectors/hospitality/sector-hospitality.webp) | WEBP | 1600×1000 · 8:5 | 167.2 KiB | H / no | No embebidos detectados |
| R26 / S02 | [assets/images/sectors/industry/sector-industry.webp](../../assets/images/sectors/industry/sector-industry.webp) | WEBP | 1600×1000 · 8:5 | 171.0 KiB | H / no | No embebidos detectados |
| R27 / S05 | [assets/images/sectors/infrastructure/sector-infrastructure.webp](../../assets/images/sectors/infrastructure/sector-infrastructure.webp) | WEBP | 1600×1000 · 8:5 | 304.6 KiB | H / no | No embebidos detectados |
| R28 / S03 | [assets/images/sectors/sports/sector-sports.webp](../../assets/images/sectors/sports/sector-sports.webp) | WEBP | 1600×1000 · 8:5 | 229.8 KiB | H / no | No embebidos detectados |
| R29 / S04 | [assets/images/sectors/tertiary/sector-tertiary.webp](../../assets/images/sectors/tertiary/sector-tertiary.webp) | WEBP | 1600×1000 · 8:5 | 192.7 KiB | H / no | No embebidos detectados |
| R30 / D01 | [originals/D01/D01_original.jpg](../../media-library/originals/D01/D01_original.jpg) | JPEG | 3264×2448 · 4:3 | 3.83 MiB | H / no | No embebidos detectados |
| R31 / D02 | [originals/D02/D02_original.jpg](../../media-library/originals/D02/D02_original.jpg) | JPEG | 3264×2448 · 4:3 | 921.0 KiB | H / no | No embebidos detectados |
| R32 / D03 | [originals/D03/D03_original.jpg](../../media-library/originals/D03/D03_original.jpg) | JPEG | 4288×2848 · 134:89 | 2.63 MiB | H / no | Sí |
| R33 / D04 | [originals/D04/D04_original.jpg](../../media-library/originals/D04/D04_original.jpg) | JPEG | 6000×4000 · 3:2 | 5.06 MiB | H / no | Sí |
| R34 / E02 | [originals/E02/E02_original.jpg](../../media-library/originals/E02/E02_original.jpg) | JPEG | 4032×2268 · 16:9 | 3.85 MiB | H / no | No embebidos detectados |
| R35 / E03 | [originals/E03/E03_original.jpg](../../media-library/originals/E03/E03_original.jpg) | JPEG | 5312×2988 · 16:9 | 6.88 MiB | H / no | Sí |
| R36 / E04 | [originals/E04/E04_original.jpg](../../media-library/originals/E04/E04_original.jpg) | JPEG | 4608×3456 · 4:3 | 4.00 MiB | H / no | Sí |
| R37 / E05 | [originals/E05/E05_original.jpg](../../media-library/originals/E05/E05_original.jpg) | JPEG | 3000×2400 · 5:4 | 6.44 MiB | H / no | Sí |
| R38 / E06 | [originals/E06/E06_original.jpg](../../media-library/originals/E06/E06_original.jpg) | JPEG | 2048×1536 · 4:3 | 841.1 KiB | H / no | No embebidos detectados |
| R39 / H01 | [originals/H01/H01_original.jpg](../../media-library/originals/H01/H01_original.jpg) | JPEG | 3676×2635 · 3676:2635 | 1.99 MiB | H / no | Sí |
| R40 / H03 | [originals/H03/H03_original.jpg](../../media-library/originals/H03/H03_original.jpg) | MPO | 4032×3024 · 4:3 | 2.71 MiB | H / no | Sí |
| R41 / H04 | [originals/H04/H04_original.jpg](../../media-library/originals/H04/H04_original.jpg) | JPEG | 4192×2256 · 262:141 | 3.63 MiB | H / no | Sí |
| R42 / H05 | [originals/H05/H05_original.jpg](../../media-library/originals/H05/H05_original.jpg) | JPEG | 4912×3264 · 307:204 | 7.89 MiB | H / no | Sí |
| R43 / I01 | [originals/I01/I01_original.jpg](../../media-library/originals/I01/I01_original.jpg) | JPEG | 4574×3136 · 2287:1568 | 866.4 KiB | H / no | Sí |
| R44 / I02 | [originals/I02/I02_original.jpg](../../media-library/originals/I02/I02_original.jpg) | JPEG | 3504×2336 · 3:2 | 6.14 MiB | H / no | Sí |
| R45 / I03 | [originals/I03/I03_original.jpg](../../media-library/originals/I03/I03_original.jpg) | JPEG | 4608×3456 · 4:3 | 3.22 MiB | H / no | Sí |
| R46 / I04 | [originals/I04/I04_original.jpg](../../media-library/originals/I04/I04_original.jpg) | MPO | 7432×5573 · 7432:5573 | 8.85 MiB | H / no | Sí |
| R47 / I05 | [originals/I05/I05_original.jpg](../../media-library/originals/I05/I05_original.jpg) | JPEG | 2288×1712 · 143:107 | 808.4 KiB | H / no | Sí |
| R48 / I06 | [originals/I06/I06_original.tiff](../../media-library/originals/I06/I06_original.tiff) | TIFF | 7200×4802 · 3600:2401 | 540.8 KiB | H / no | Sí |
| R49 / I07 | [originals/I07/I07_original.jpg](../../media-library/originals/I07/I07_original.jpg) | JPEG | 3264×2448 · 4:3 | 1.43 MiB | H / no | No embebidos detectados |
| R50 / I08 | [originals/I08/I08_original.jpg](../../media-library/originals/I08/I08_original.jpg) | JPEG | 4608×3456 · 4:3 | 2.42 MiB | H / no | Sí |
| R51 / S01 | [originals/S01/S01_original.jpg](../../media-library/originals/S01/S01_original.jpg) | JPEG | 8032×2490 · 4016:1245 | 4.89 MiB | H / no | No embebidos detectados |
| R52 / S02 | [originals/S02/S02_original.jpg](../../media-library/originals/S02/S02_original.jpg) | JPEG | 2048×1536 · 4:3 | 457.0 KiB | H / no | Sí |
| R53 / S03 | [originals/S03/S03_original.jpg](../../media-library/originals/S03/S03_original.jpg) | JPEG | 3000×2000 · 3:2 | 1.16 MiB | H / no | Sí |
| R54 / S04 | [originals/S04/S04_original.jpg](../../media-library/originals/S04/S04_original.jpg) | JPEG | 2048×1536 · 4:3 | 1.06 MiB | H / no | Sí |
| R55 / S05 | [originals/S05/S05_original.jpg](../../media-library/originals/S05/S05_original.jpg) | JPEG | 5070×3380 · 3:2 | 12.50 MiB | H / no | Sí |

### 3.2. Integridad, formatos y variantes

**VERIFICADO.** No hay grupos de duplicados binarios SHA-256 entre las 55 imágenes. Hay **26 parejas de variantes**, original y WebP, relacionadas por ID de biblioteca y cotejadas visualmente. Son archivos distintos: convertir, recortar o reducir no produce un duplicado binario. H03 e I04 muestran vistas de una sala técnica que la documentación identifica como la misma; no son el mismo encuadre ni la misma imagen.

| Paquete | Preparado | Original inspeccionado | Diferencia de versión |
|---|---|---|---|
| D01 | R01 · WebP 1600×1200 | R30 · JPEG 3264×2448 | Conversión y encuadre documentados; originales intactos |
| D02 | R03 · WebP 1600×1200 | R31 · JPEG 3264×2448 | Conversión y encuadre documentados; originales intactos |
| D04 | R04 · WebP 1600×1200 | R33 · JPEG 6000×4000 | Conversión y encuadre documentados; originales intactos |
| D03 | R05 · WebP 1600×1200 | R32 · JPEG 4288×2848 | Conversión y encuadre documentados; originales intactos |
| E05 | R07 · WebP 1600×1200 | R37 · JPEG 3000×2400 | Conversión y encuadre documentados; originales intactos |
| E06 | R08 · WebP 1600×1200 | R38 · JPEG 2048×1536 | Conversión y encuadre documentados; originales intactos |
| E04 | R09 · WebP 1600×1200 | R36 · JPEG 4608×3456 | Conversión y encuadre documentados; originales intactos |
| E02 | R10 · WebP 1600×1200 | R34 · JPEG 4032×2268 | Conversión y encuadre documentados; originales intactos |
| E03 | R12 · WebP 1600×1200 | R35 · JPEG 5312×2988 | Conversión y encuadre documentados; originales intactos |
| I08 | R13 · WebP 1600×1200 | R50 · JPEG 4608×3456 | Conversión y encuadre documentados; originales intactos |
| I07 | R14 · WebP 1600×1200 | R49 · JPEG 3264×2448 | Conversión y encuadre documentados; originales intactos |
| I01 | R15 · WebP 1600×1200 | R43 · JPEG 4574×3136 | Conversión y encuadre documentados; originales intactos |
| I06 | R16 · WebP 1600×1200 | R48 · TIFF 7200×4802 | Conversión y encuadre documentados; originales intactos |
| I02 | R17 · WebP 1600×1200 | R44 · JPEG 3504×2336 | Conversión y encuadre documentados; originales intactos |
| I03 | R18 · WebP 1600×1200 | R45 · JPEG 4608×3456 | Conversión y encuadre documentados; originales intactos |
| I05 | R19 · WebP 1600×1200 | R47 · JPEG 2288×1712 | Conversión y encuadre documentados; originales intactos |
| I04 | R20 · WebP 1600×1200 | R46 · MPO 7432×5573 | Conversión y encuadre documentados; originales intactos |
| H05 | R21 · WebP 1600×1200 | R42 · JPEG 4912×3264 | Conversión y encuadre documentados; originales intactos |
| H04 | R22 · WebP 1600×1200 | R41 · JPEG 4192×2256 | Conversión y encuadre documentados; originales intactos |
| H03 | R23 · WebP 1600×1200 | R40 · MPO 4032×3024 | Conversión y encuadre documentados; originales intactos |
| H01 | R24 · WebP 1920×1080 | R39 · JPEG 3676×2635 | Conversión y encuadre documentados; originales intactos |
| S01 | R25 · WebP 1600×1000 | R51 · JPEG 8032×2490 | Conversión y encuadre documentados; originales intactos |
| S02 | R26 · WebP 1600×1000 | R52 · JPEG 2048×1536 | Conversión y encuadre documentados; originales intactos |
| S05 | R27 · WebP 1600×1000 | R55 · JPEG 5070×3380 | Conversión y encuadre documentados; originales intactos |
| S03 | R28 · WebP 1600×1000 | R53 · JPEG 3000×2000 | Conversión y encuadre documentados; originales intactos |
| S04 | R29 · WebP 1600×1000 | R54 · JPEG 2048×1536 | Conversión y encuadre documentados; originales intactos |

**VERIFICADO.** Los dos originales MPO son R40 (`originals/H03/H03_original.jpg`, 4032×3024) y R46 (`originals/I04/I04_original.jpg`, 7432×5573), ambos con dos fotogramas. No se han convertido; la extensión `.jpg` no describe por sí sola el contenedor. El TIFF R48 mide 7200×4802, con dibujo de alto detalle y trazos muy finos: su legibilidad no se puede juzgar solo por una miniatura.

**VERIFICADO.** Las dimensiones y pesos de los 29 WebP coinciden con el manifiesto. Sus rutas `relative_path` son relativas a la raíz **del paquete**: `LIB/assets/images/…`. En el repositorio actual la biblioteca está anidada bajo `media-library/`; esas rutas no equivalen a imágenes ya integradas en la raíz web. No se han copiado ni enlazado desde el HTML.

### 3.3. Entradas sin archivo y auxiliares

| ID de biblioteca | Estado declarado | Archivo esperado dentro de LIB | Lectura de esta inspección |
|---|---|---|---|
| H02 | PENDING_ORIGINAL | `assets/images/home/vision/home-vision-system.svg` | No existe en LIB. La ilustración WebP del sitio ya descrita en B01 es otro recurso/formato; no se equipara automáticamente ni autoriza añadir una sección fuera de D03 |
| E08 | NEEDS_CREATION | `assets/images/capabilities/energy/management/energy-system-diagram.svg` | Diagrama pendiente; ninguna foto lo sustituye funcionalmente |
| D05 | NOT_FOUND | `assets/images/capabilities/digital/integration/digital-industrial-network.webp` | Recurso pendiente; no se deduce su contenido de un nombre sin imagen |
| D07 | NEEDS_CREATION | `assets/images/capabilities/digital/integration/digital-control-architecture.svg` | Arquitectura de control pendiente |
| X01 | PENDING_ORIGINAL | `assets/images/experience/uib/experience-uib-campus.webp` | Referencia auténtica pendiente |
| X02 | PENDING_ORIGINAL | `assets/images/experience/mep-buildings/experience-hotel-formentor.webp` | Referencia auténtica pendiente |
| X03 | PENDING_ORIGINAL | `assets/images/experience/offshore/experience-offshore-wind.webp` | Referencia auténtica pendiente |

**VERIFICADO.** Los 36 auxiliares son README, tres manifiestos, 26 JSON de fuente, tres copias de `demo_graphics.py` y tres documentos de reports (incluida una hoja PDF preexistente). No se cuentan como fotografías. La hoja PDF del proveedor no sustituye la inspección propia ni acredita permisos. No se ejecutaron scripts ni se generaron versiones nuevas de las imágenes, salvo miniaturas de inspección.

## 4. Clasificación temática

Las categorías siguientes se basan en contenido **observado**, no en carpetas o nombres. Una imagen puede pertenecer a varias; los conteos se refieren a **29 recursos preparados** para no duplicar fotografías por contar sus originales. Las 26 variantes originales conservan su relación con el recurso de referencia y sus diferencias de encuadre se registran en JSON.

| Código / categoría | Nº preparados (solapamiento permitido) | Recursos preparados observados |
|---|---:|---|
| INF · Infraestructuras e instalaciones | 16 | R01, R03, R08, R09, R12, R13, R14, R15, R16, R17, R18, R19, R20, R23, R24, R27 |
| ENE · Sistemas energéticos | 10 | R06, R07, R08, R09, R10, R11, R12, R17, R22, R24 |
| DIG · Automatización y control | 7 | R01, R02, R03, R04, R05, R11, R21 |
| IND · Industria y procesos | 2 | R26, R27 |
| EDI · Edificios y arquitectura técnica | 7 | R10, R22, R23, R25, R27, R28, R29 |
| EQU · Equipos e instalaciones | 22 | R01, R03, R04, R05, R07, R08, R09, R10, R12, R13, R14, R15, R17, R18, R19, R20, R21, R22, R23, R24, R26, R27 |
| PER · Personas y trabajo profesional | 6 | R04, R05, R13, R14, R17, R28 |
| ABS · Recursos abstractos o conceptuales | 4 | R02, R06, R11, R16 |
| OTR · Otros | 0 | Sin asignación: no se fuerza una categoría residual |

**VERIFICADO.** Los nombres comerciales/técnicos del paquete no siempre equivalen a lo que puede acreditarse visualmente: R18 muestra principalmente una unidad de tratamiento de aire, aunque el nombre diga ductwork; R12 muestra edificios/contenedores de equipos, no celdas de batería visibles; la función térmica exacta de R08 y el uso contra incendios de R19 proceden de su documentación. Se registran como **declarados**, no confirmados por la apariencia. Las personas observadas no se identifican como fundadores ni trabajadores de BAFRAS.

## 5. Evaluación visual

### 5.1. Hoja de revisión de los 29 recursos preparados

**VERIFICADO (observación):** descripción, detalle aparente, áreas libres y encuadre. **INFERIDO:** posible función, recorte útil, compatibilidad de fondo y riesgo de atribución. **RECOMENDACIÓN:** uso provisional sujeto a D03, revisión humana y derechos. No se ha medido contraste de texto superpuesto ni aprobado ningún encuadre. Los originales se observaron en las hojas 3–5; su evaluación vinculada figura en JSON, con límites adicionales de 1:1 y MPO.

| ID / tema | Contenido observado | Calidad y nitidez aparente | Recorte / espacio negativo | Fondo y posible función | Límites y riesgo de atribución |
|---|---|---|---|---|---|
| R01 · INF,DIG,EQU | Armario abierto con módulos, borneros y cableado. | Buena aparente; detalle técnico legible a tamaño editorial. | Recorte moderado; conservar conjunto y cableado. Espacio: Escaso. | Claro; oscuro con encuadre separado. Editorial o tarjeta. | No se verifica fabricante ni función exacta del controlador. Riesgo: Medio: instalación concreta ajena. |
| R02 · DIG,ABS | Dos gráficas de tendencias, umbral y alarma; sello de datos sintéticos. | Trazos nítidos; texto pequeño al reducir. | No recortar títulos, ejes, unidades, leyenda ni sello. Espacio: Solo márgenes, no para texto superpuesto. | Claro. Editorial demostrativa. | No es captura de plataforma ni resultado de estudio real; pierde legibilidad como tarjeta pequeña. Riesgo: Alto si se presenta como resultado o caso real. |
| R03 · INF,DIG,EQU | Instrumento de campo conectado a tuberías y válvulas. | Foco principal nítido; fondo luminoso y distraído. | Recorte alrededor del instrumento conservando conexiones. Espacio: Escaso y fragmentado. | Claro. Editorial o tarjeta técnica. | No se acredita variable, calibración ni esquema funcional por la fotografía. Riesgo: Medio. |
| R04 · DIG,PER,EQU | Persona señalando una pantalla de control en pared de sala técnica. | Buena aparente; pantalla pequeña. | No cortar gesto ni interfaz; encuadre limitado. Espacio: Escaso. | Claro. Editorial de supervisión. | No identifica por sí sola BMS, automatización instalada o personal BAFRAS. Riesgo: Alto por persona e instalación reconocibles. |
| R05 · DIG,PER,EQU | Persona ante monitor con sinóptico de depósitos y proceso. | Buena aparente; texto de pantalla no legible en miniatura. | Conservar relación operador-pantalla. Espacio: Pared clara parcial, insuficiente para hero cargado. | Claro. Editorial de supervisión. | No demuestra software propio ni función exacta del sistema. Riesgo: Alto por persona e interfaz real. |
| R06 · ENE,ABS | Curvas y áreas de demanda, producción y balance diario con datos sintéticos. | Nítida a tamaño editorial; leyenda pequeña. | No recortar ejes, leyenda ni sello. Espacio: No útil para sobreimpresión. | Claro. Editorial demostrativa. | No prueba ahorro ni rendimiento; imagen raster, no gráfico interactivo. Riesgo: Alto si se atribuye a una instalación o estudio real. |
| R07 · ENE,EQU | Fila de vehículos, conexiones y postes de recarga. | Buena aparente; composición densa. | Recorte moderado sin perder vehículo-conector. Espacio: Muy escaso. | Claro o módulo sobre oscuro. Tarjeta o editorial de movilidad. | Marcas y matrículas potencialmente identificables; no acredita tecnología V2G. Riesgo: Medio-alto. |
| R08 · INF,ENE,EQU | Sala con tuberías aisladas, bombas y equipos de intercambio. | Buena aparente; muchos elementos. | Conservar varios equipos e interconexiones. Espacio: Escaso. | Claro. Editorial térmica. | La función de bomba de calor procede de documentación, no se confirma solo por aspecto. Riesgo: Medio. |
| R09 · INF,ENE,EQU | Equipo eléctrico con radiadores y conexiones en recinto interior. | Buena; fondo y equipo ocupan casi todo el encuadre. | Conservar protecciones y contexto. Espacio: Muy escaso. | Claro. Tarjeta eléctrica. | No acredita potencia, tensión, diseño o intervención BAFRAS. Riesgo: Medio. |
| R10 · ENE,EDI,EQU | Cubierta con paneles fotovoltaicos, edificios y horizonte. | Buena; detalle suficiente. | Admite recorte horizontal moderado; conservar cubierta y paneles. Espacio: Cielo parcial. | Claro u oscuro con tratamiento de texto por validar. Editorial o tarjeta energética. | No cuantifica capacidad ni acredita proyecto propio. Riesgo: Medio. |
| R11 · ENE,DIG,ABS | Dashboard DEMO con indicadores y gráficos; valores ficticios y sello. | Nítida; demasiados detalles para tarjeta pequeña. | Mantener toda la lámina y sello. Espacio: No para texto añadido. | Claro. Editorial demostrativa grande. | Cifras ficticias, no producto operativo ni estudio; no reutilizar como tokens visuales aprobados. Riesgo: Alto si se interpreta como desempeño real. |
| R12 · ENE,INF,EQU | Contenedores o edificios de equipos con ventilación exterior y líneas aéreas. | Buena; contraste fuerte de cielo y equipos. | Conservar equipos; recorte moderado. Espacio: Cielo superior limitado. | Claro u oscuro en módulo separado. Editorial o tarjeta. | La identidad batería/híbrido la declara la ficha de fuente; no se ven celdas ni diagrama del sistema. Riesgo: Medio-alto. |
| R13 · INF,PER,EQU | Técnico con casco y chaleco ante cuadros y equipo portátil de ensayo. | Buena aparente; sujeto central. | Conservar persona, instrumento y cuadro. Espacio: Escaso. | Claro. Editorial de pruebas. | Una imagen no acredita recepción, procedimiento de commissioning ni profesional propio. Riesgo: Alto. |
| R14 · INF,PER,EQU | Persona en elevador bajo conductos o estructura de techo en obra. | Media-baja: contraluz y zonas oscuras. | Recorte limitado por iluminación y sujeto. Espacio: Oscuro pero irregular, poco apto para texto pequeño. | Oscuro; validar contraste. Editorial secundaria de obra. | Pérdida de detalle; no acredita ejecución BAFRAS. Riesgo: Alto. |
| R15 · INF,EQU | Pasillo entre alineaciones de armarios eléctricos. | Media-buena; profundidad marcada y fondo brillante. | Admite centro de perspectiva; no cortar todas las referencias de escala. Espacio: Escaso por textura. | Claro u oscuro como imagen independiente. Editorial eléctrica. | No acredita norma, capacidad o estado actual de la instalación. Riesgo: Medio. |
| R16 · INF,ABS | Plano técnico monocromo con trazados, símbolos y anotaciones. | Líneas nítidas; letra diminuta al reducir. | Solo detalle contextual, sin simular legibilidad documental completa. Espacio: Fondo blanco ocupado por dibujo. | Claro. Editorial de documentación, nunca plano de un encargo propio. | Recorte elimina contexto; escaneado histórico no equivale a entregable BAFRAS. Riesgo: Alto si se muestra como trabajo propio. |
| R17 · INF,ENE,PER,EQU | Sala industrial con grandes tuberías y equipo azul; persona de escala. | Buena aparente; composición densa. | Conservar equipo y contexto de escala. Espacio: Muy escaso. | Claro u oscuro en módulo separado. Editorial térmica. | El tipo de planta requiere fuente; persona no pertenece al equipo acreditado. Riesgo: Alto. |
| R18 · INF,EQU | Unidad larga de tratamiento de aire con puertas verdes en sala técnica. | Buena aparente, tonos oscuros. | Recorte horizontal moderado; mantener unidad y pasillo. Espacio: Escaso. | Claro u oscuro como imagen independiente. Editorial de climatización/ventilación. | El nombre ductwork no describe exactamente lo dominante: se observa unidad de tratamiento, no solo conductos. Riesgo: Medio. |
| R19 · INF,EQU | Red de tuberías, manómetros, válvulas y botellas o depósitos. | Buena aparente; composición abigarrada. | Conservar conexiones; no aislar un equipo como esquema funcional. Espacio: Muy escaso. | Claro. Editorial de instalaciones. | La aplicación contra incendios es declarada por la fuente, no se verifica por esta revisión visual. Riesgo: Medio. |
| R20 · INF,EQU | Tuberías aisladas, instrumentos, válvulas y equipos murales. | Buena aparente; luz uniforme. | Recorte moderado en torno a conexiones. Espacio: Pared clara interrumpida por tuberías. | Claro. Editorial hidráulica. | No acredita diseño ni funcionamiento de una instalación propia. Riesgo: Medio. |
| R21 · DIG,EQU | Primer plano de módulos de control, borneros y cableado multicolor. | Buena; foco selectivo y fondo desenfocado. | Recorte moderado; conservar módulos completos. Espacio: Escaso. | Claro u oscuro en módulo separado. Tarjeta de automatización. | Marcas visibles; no acredita integración o programación propia. Riesgo: Medio. |
| R22 · ENE,EDI,EQU | Paneles FV sobre cubierta plana con cielo azul. | Buena; encuadre simple. | Admite tarjeta y franja horizontal, sin perder paneles. Espacio: Cielo superior reducido. | Claro u oscuro con contraste por validar. Tarjeta energética. | No identifica potencia, rendimiento o titular del proyecto. Riesgo: Medio. |
| R23 · INF,EDI,EQU | Sala técnica con conductos aislados, tuberías y equipos murales. | Buena; tonos claros y grises. | Admite recorte moderado manteniendo pluralidad de sistemas. Espacio: Paredes parciales, no campo uniforme amplio. | Claro. Tarjeta o editorial de instalaciones. | La documentación la vincula a la misma sala que I04; no son duplicados exactos. Riesgo: Medio. |
| R24 · INF,ENE,EQU | Gran sala con bombas y tuberías rojas alineadas. | Buena; perspectiva y fuerte dominante roja. | Horizontal útil; no recortar como evidencia de BAFRAS. Espacio: Zona de techo limitada y texturada. | Oscuro con contraste a comprobar; claro como imagen. Candidata hero o editorial. | Color rojo no es nuevo acento corporativo; origen ajeno documentado localmente. Riesgo: Medio-alto por protagonismo como hero. |
| R25 · EDI | Edificio hotelero con balcones, piscina y palmeras. | Media-buena; luz contenida y detalles pequeños. | Recorte 16:10 ya cerrado; original panorámico permite otros encuadres solo en fase autorizada. Espacio: Cielo escaso. | Claro. Tarjeta sectorial de turismo. | No muestra instalaciones técnicas; hotel identificable, no cliente ni proyecto acreditado. Riesgo: Alto. |
| R26 · IND,EQU | Línea industrial con maquinaria verde y cajas sobre transporte. | Buena; detalle abundante. | Mantener relación entre línea y producto. Espacio: Muy escaso. | Claro u oscuro como imagen independiente. Tarjeta industrial. | No identifica producto, rendimiento o relación contractual. Riesgo: Medio. |
| R27 · INF,IND,EDI,EQU | Vista aérea de instalación con depósitos circulares y campos. | Buena; abundante contexto. | Recorte debe preservar depósitos; no confundir infraestructura con solar. Espacio: Campos relativamente uniformes pero texturados. | Claro. Tarjeta de servicios públicos. | El carácter de depuradora está documentado por fuente; no acredita obra propia. Riesgo: Medio-alto. |
| R28 · EDI,PER | Piscina interior de varias calles, estructura metálica y personas pequeñas. | Buena; escala amplia. | Mantener estructura y lámina de agua. Espacio: Techo blanco estructurado, no uniforme. | Claro. Tarjeta de equipamientos, no sector adicional. | No mostrar como instalación propia; no cubre por sí sola sanidad o educación. Riesgo: Medio-alto. |
| R29 · EDI | Edificio contemporáneo acristalado con lamas y pavimento exterior. | Buena; geometría marcada. | Recorte moderado manteniendo fachada. Espacio: Cielo y pavimento limitados. | Claro. Tarjeta terciaria o edificación. | Edificio identificable, no oficina o proyecto BAFRAS. Riesgo: Alto. |

### 5.2. Condicionantes comunes

- **VERIFICADO.** Las fotografías son heterogéneas en luz y color: tuberías rojas, unidades verdes, equipos azules, salas grises y exteriores. **RECOMENDACIÓN:** el diseño debe encuadrarlas con la identidad existente; sus colores no se convierten en tokens BAFRAS.
- **VERIFICADO.** Casi todas tienen alta densidad de equipos y poco espacio negativo; R24 tiene una perspectiva amplia, R10/R22 cielo parcial y R25/R29 fachadas reconocibles. **INFERIDO:** el texto al lado de la foto puede funcionar mejor que superponerlo. Contraste/recorte responsive quedan por demostrar en diseño.
- **VERIFICADO.** R02/R06/R11 llevan textos y gráficos rasterizados. **RECOMENDACIÓN:** conservar título, ejes, unidades, leyenda y sello; no tratarlos como fondos con `cover` ni como evidencia cuantitativa. No se han generado nuevos gráficos.
- **VERIFICADO.** R41 conserva una persona al fondo y R50 una fecha impresa que no aparecen igual en sus versiones preparadas. **RECOMENDACIÓN:** no intercambiar original y recorte sin revisión. La inspección no propone nuevos recortes en esta intervención.
- **NO VERIFICADO.** Calidad final en hero de pantallas de alta densidad, texto alemán/catalán sobre la composición, derechos de imagen de personas, marcas, matrículas y cambios de encuadre. La calidad aparente no constituye autorización para publicar.

## 6. Matriz provisional de correspondencia con D03

Esta matriz identifica **funciones posibles dentro de bloques existentes**. No impone una foto en cada sección, no inventa bloques y no sustituye el orden de D03 por las etiquetas `page/section` del manifiesto. Los candidatos son **RECOMENDACIONES provisionales**; los límites de publicación proceden de D03. D03 conserva su autoridad editorial completa.

| Página / bloque editorial D03 | Función visual posible y tipo necesario | Candidatos observados | Observaciones y límites |
|---|---|---|---|
| Inicio · H01, L34–42 | Fotografía técnica o composición ligada a capacidades | R24 (sala técnica), R23 (instalaciones); R10 solo si no desequilibra el mensaje | Hero equilibrado de tres capacidades; no convertirlo en referencia propia. Derechos pendientes |
| Inicio · H02, L44–63 | Apoyar las tres capacidades con igual peso | R23 INF, R22 ENE, R21 DIG | Selección de tres fotografías coherentes, opcional; sus títulos y textos vienen de D03 |
| Inicio · H03, L65–83 | Explicar cuatro necesidades con jerarquía, sin catálogo fotográfico | Ninguna obligatoria | No crear cinco tarjetas porque el paquete o la web antigua sugieran otra estructura |
| Inicio · H04, L85–95 | Método y alcance; tratamiento tipográfico o gráfico neutro | Ninguna fotografía necesaria | No añadir un bloque autónomo de visión de sistema fuera del orden aprobado |
| Inicio · H05, L97–106 | Contextos de aplicación, selección de portada | R25, R26, R29, R28/R27 como candidatos ilustrativos | D03 define cuatro grupos de portada; no confundirlos con cinco recursos sectoriales o seis grupos de Sectores |
| Inicio · H06, L108–112 | Confianza mediante experiencia acreditada | Ninguna foto LIB acredita experiencia | Mantener alternativa textual aprobada si no hay referencias autorizadas; no sustituir con hotel/FV/eólico genéricos |
| Inicio · H07, L114–118 | Cierre/contacto | Ninguna necesaria | Priorizar texto y CTA |
| Capacidades · C01, L149–156 | Hero compacto de orientación | Ninguna obligatoria | D03:L223 declara fotografía no obligatoria; no imponer hero fotográfico |
| Capacidades · C02, L158–182 | Tres especialidades comparables | R23/R15 INF, R10/R22 ENE, R21/R01 DIG | Igual jerarquía; fotos opcionales, sin alegar proyectos |
| Capacidades · C03, L184–195 | Tres ejemplos hipotéticos de relación entre disciplinas | R08/R20 (térmica), R10/R12 (autoconsumo/almacenamiento), R03/R04 (diagnóstico), solo como ilustración | No ensamblarlos como una instalación real; los mini-esquemas específicos no existen en LIB |
| Capacidades · C04–C05, L197–217 | Modalidades y contacto | Ninguna necesaria; R16 solo para ilustrar documentación | No presentar un plano ajeno como entregable propio |
| Infraestructuras · INF-01, L275–284 | Entrada técnica amplia | R23/R17/R24 | No limitar la página a un solo tipo de edificio/equipo |
| Infraestructuras · INF-02, L286–297 | Necesidades del cliente | Ninguna obligatoria | Evitar fotografía por necesidad sin aportar comprensión |
| Infraestructuras · INF-03, L299–331 | Cuatro ámbitos y diagnóstico transversal | R15/R09 electricidad; R18/R17 climatización; R20 agua; R19 protección, condicionado a ficha; sin específico de acústica | No transformar cada imagen en servicio; diagrama integrador específico pendiente |
| Infraestructuras · INF-04, L333–343 | Entregables y documentación | R16 ilustrativo; R13 como escena genérica de pruebas | No acredita autoría de planos o procedimiento de verificación. Para evidencia de entregables, exigir documentos propios anonimizados |
| Infraestructuras · INF-05, L345–350 | Conexiones con ENE/DIG | R03/R08 opcionales; preferible relación conceptual legible | No hay diagrama de interconexiones validado en LIB |
| Infraestructuras · INF-06–07, L352–366 | Experiencia y CTA | Ninguna referencia auténtica disponible en LIB | Material específico autorizado o bloque general de D03; no fotos de terceros como Formentor/Montesion/Ibiza |
| Sistemas energéticos · ENE-01–02, L415–437 | Hero y decisiones energéticas | R10/R22/R08 opcionales para hero; ninguna obligatoria en necesidades | Mantener amplitud de demanda, alternativas y térmica; no prometer ahorro |
| Sistemas energéticos · ENE-03, L439–475 | Seis ámbitos + nota complementaria | R06 diagnóstico DEMO; R10/R12 generación/almacenamiento; R08 térmica; R07 recarga; R11 gestión DEMO | No hay visual específico de descarbonización/huella ni eficiencia hídrica; no usar cifras sintéticas como cálculo de cliente |
| Sistemas energéticos · ENE-04, L477–485 | Modalidades/entregables | R06/R11 solo como ejemplo demostrativo; preferencia por documentación propia | No prueban que existan resultados de los dos softwares BAFRAS |
| Sistemas energéticos · ENE-05, L487–493 | Relación con INF y control | R09/R03 como apoyo opcional | El diagrama E08 no existe; ninguna foto demuestra un balance o arquitectura |
| Sistemas energéticos · ENE-06–07, L495–507 | Experiencia y contacto | Ninguna auténtica en LIB | Mantener texto general autorizado y CTA; no asignar la cubierta solar a UIB |
| Automatización y control · DIG-W01–02, L564–579 | Hero y necesidades | R01/R21/R03 opcionales | No asumir marcas, protocolos o autoría del sistema |
| Automatización y control · DIG-W03, L581–610 | Seis ámbitos y diagnóstico/pruebas transversal | R03 instrumentación; R01/R21 control; R04/R05 supervisión; R02 analítica DEMO | No hay imagen de red OT/arquitectura de integración ni control energético acreditado. D05/D07 del paquete son pendientes, no nuevas secciones |
| Automatización y control · DIG-W04–05, L612–624 | Entregables e interfaces | R02 solo demostración; documentación real requerida | No existe una arquitectura técnica específica validada; fotos de armarios no sustituyen diagramas/listas de señales |
| Automatización y control · DIG-W06–07, L626–634 | Experiencia y CTA | Ninguna auténtica en LIB | No representar parques eólicos ni referencias previas con stock |
| Sectores · SEC-01–02, L687–726 | Hero opcional y seis contextos sectoriales | R25 turismo; R26 industria; R27 servicios públicos; R28 equipamientos; R29 terciario/edificación; R07/R22 apoyos energéticos | D03:L750 prefiere iconografía uniforme. Cinco imágenes de carpetas no constituyen los seis grupos aprobados; R28 no crea un sector independiente «deportes» |
| Sectores · SEC-03–05, L728–741 | Problemas comunes, colaboración y cierre | Ninguna obligatoria | No usar operadores ajenos como el equipo colaborador propio |
| Proyectos y experiencia · PE-01–02, L789–828 | Índice de tres destacadas y tres complementarias con atribución | Ninguna foto LIB acredita las seis referencias | X01–X03 ausentes y tampoco cubren por sí solos centro educativo, residencia ni HVAC UIB. Estado visual alternativo o material real autorizado |
| Proyectos y experiencia · PE-03–04, L830–841 | Explicar evidencia y contacto | Ninguna obligatoria | R16 ajeno y gráficos DEMO no acreditan resultados profesionales |
| Sobre BAFRAS · SB-01–02, L904–922 y 03.K L1163–1171 | Presentación y tres fundadores | Ningún retrato del equipo en LIB | Recabar retratos propios autorizados o alternativa tipográfica neutra. No usar R04/R05/R13/R17 como socios |
| Sobre BAFRAS · SB-03–05, L924–951 | Método, experiencia/colaboración y CTA | Ninguna necesaria | Ilustración genérica solo si aporta; no simular reunión o trabajo propio |
| Contacto · CO-01–04, L960–1004 y 03.K/03.K.2 | Formulario, correo, orientación y privacidad | Ninguna necesaria | La biblioteca no es requisito para esta página. No añadir imagen decorativa o referencia para llenar una columna |

## 7. Licencias y procedencias pendientes

### 7.1. Estados de evidencia independientes

| Dimensión | Estado de esta intervención |
|---|---|
| Procedencia declarada por dirección | Material provisional de fuentes consideradas de dominio público, pendiente de documentación por recurso |
| Procedencia documentada en el paquete | **VERIFICADO localmente:** 26 JSON con URLs, metadatos y SHA-1; manifiestos/créditos para 29 recursos preparados; tres scripts para gráficos sintéticos |
| Integridad original respecto al registro local | **VERIFICADO:** 26/26 SHA-1 coincidentes; no acredita que el registro sea una certificación externa |
| Licencia declarada / atribuida por el proveedor | Valores de la tabla siguiente y campos `commercial_use_verified` del YAML; son declaraciones del paquete |
| Licencia verificada independientemente en B02-PREP-01 | **NO VERIFICADO** para los 29 recursos; no se contrastó la versión vigente de páginas externas ni la titularidad |
| Permiso comercial y condiciones de publicación | **Pendiente de verificación** por recurso, incluidos créditos, modificaciones y posibles derechos adicionales de personas/marcas |

No se inventan autores, licencias o URLs: los valores siguientes se transcriben de YAML/CSV y `source.json`. El JSON conserva las URLs declaradas para revisión posterior. Las referencias de fuente enlazan a **documentación local suministrada**, no a una comprobación web realizada. «Propio» es la declaración del paquete y no una conclusión independiente de autoría.

| Recurso preparado / paquete | Autor declarado | Licencia declarada | Soporte local de procedencia | Verificación independiente / comercial |
|---|---|---|---|---|
| R01 / D01 | Mixabest | CC BY-SA 3.0 | [Ficha local](../../media-library/originals/D01/source.json) | No realizada / pendiente |
| R02 / D06 | BAFRAS Engineering | Propio (BAFRAS Engineering) | [Ficha local](../../media-library/manifests/media-manifest.yaml) | No realizada / pendiente |
| R03 / D02 | Bitjungle | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/D02/source.json) | No realizada / pendiente |
| R04 / D04 | U.S. Army photo by Sandra Wilson | Public domain | [Ficha local](../../media-library/originals/D04/source.json) | No realizada / pendiente |
| R05 / D03 | U.S. Department of Agriculture | Public domain | [Ficha local](../../media-library/originals/D03/source.json) | No realizada / pendiente |
| R06 / E01 | BAFRAS Engineering | Propio (BAFRAS Engineering) | [Ficha local](../../media-library/manifests/media-manifest.yaml) | No realizada / pendiente |
| R07 / E05 | Mariordo (Mario Roberto Durán Ortiz) | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/E05/source.json) | No realizada / pendiente |
| R08 / E06 | Dfpearson | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/E06/source.json) | No realizada / pendiente |
| R09 / E04 | Cjp24 | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/E04/source.json) | No realizada / pendiente |
| R10 / E02 | Asurnipal | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/E02/source.json) | No realizada / pendiente |
| R11 / E07 | BAFRAS Engineering | Propio (BAFRAS Engineering) | [Ficha local](../../media-library/manifests/media-manifest.yaml) | No realizada / pendiente |
| R12 / E03 | Ysc usc | CC BY 4.0 | [Ficha local](../../media-library/originals/E03/source.json) | No realizada / pendiente |
| R13 / I08 | MTA Capital Construction Mega Projects | CC BY 2.0 | [Ficha local](../../media-library/originals/I08/source.json) | No realizada / pendiente |
| R14 / I07 | MTA Capital Construction Mega Projects | CC BY 2.0 | [Ficha local](../../media-library/originals/I07/source.json) | No realizada / pendiente |
| R15 / I01 | Achim Hering | CC BY 3.0 | [Ficha local](../../media-library/originals/I01/source.json) | No realizada / pendiente |
| R16 / I06 | Department of Homeland Security. U.S. Coast Guard. 3/1/2003 | Public domain | [Ficha local](../../media-library/originals/I06/source.json) | No realizada / pendiente |
| R17 / I02 | Helen Ltd (mediabank) | CC BY-SA 3.0 | [Ficha local](../../media-library/originals/I02/source.json) | No realizada / pendiente |
| R18 / I03 | Alf van Beem | CC0 | [Ficha local](../../media-library/originals/I03/source.json) | No realizada / pendiente |
| R19 / I05 | Vincent de Groot - http://www.videgro.net | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/I05/source.json) | No realizada / pendiente |
| R20 / I04 | Wolfmann | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/I04/source.json) | No realizada / pendiente |
| R21 / H05 | Pierre75000 | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/H05/source.json) | No realizada / pendiente |
| R22 / H04 | U.S. Army Corps of Engineers Savannah District | Public domain | [Ficha local](../../media-library/originals/H04/source.json) | No realizada / pendiente |
| R23 / H03 | Wolfmann | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/H03/source.json) | No realizada / pendiente |
| R24 / H01 | Steve Jurvetson from Los Altos, USA | CC BY 2.0 | [Ficha local](../../media-library/originals/H01/source.json) | No realizada / pendiente |
| R25 / S01 | Killarnee | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/S01/source.json) | No realizada / pendiente |
| R26 / S02 | Laempe | CC BY-SA 3.0 | [Ficha local](../../media-library/originals/S02/source.json) | No realizada / pendiente |
| R27 / S05 | Dietmar Rabich | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/S05/source.json) | No realizada / pendiente |
| R28 / S03 | kallerna | CC BY-SA 4.0 | [Ficha local](../../media-library/originals/S03/source.json) | No realizada / pendiente |
| R29 / S04 | Chixoy | Public domain | [Ficha local](../../media-library/originals/S04/source.json) | No realizada / pendiente |

### 7.2. Límites y conflictos documentales del paquete

- **VERIFICADO.** `README.md` §2 y `reports/acquisition-report.md` afirman que READY significa listo para publicación/licencia verificada. En esta auditoría READY se conserva como **estado del proveedor**, sin aprobar automáticamente uso comercial.
- **VERIFICADO.** CC BY/CC BY-SA son los valores declarados de 20 entradas, diferentes de «Public domain». Sus términos, versiones y atribuciones concretas deben revisarse en las fuentes registradas; B02-PREP-01 no emite un dictamen jurídico.
- **VERIFICADO.** El paquete incluye `attribution.md`, `license_url`, `attribution_text`, datos de autor y modificaciones; eso ofrece trazabilidad documental. No hay que reutilizar sus créditos ni sus `alt_es` sin revisión contextual en la futura selección de D03.
- **VERIFICADO.** E01/E07/D06 tienen aviso visible de datos sintéticos. Se preserva sin recortes. Sus archivos `demo_graphics.py` son auxiliares idénticos entre sí según inspección de hash, no tres imágenes originales independientes ni resultados de los dos softwares de estudios.
- **RECOMENDACIÓN.** Antes de publicar, revisar fuente, autor, licencia, crédito y modificaciones autorizadas, además de personas, marcas o lugares reconocibles cuando corresponda. Registrar la decisión y su responsable. No deducir libre uso por ausencia de EXIF o porque la imagen esté descargada.

## 8. Recursos recomendados para revisión humana

Estas son **RECOMENDACIONES de selección**, sin aprobación visual o de derechos.

| Prioridad | Recursos | Motivo de revisión |
|---|---|---|
| Alta | R24 / lib:H01 | Candidato hero técnicamente rico; dominante roja, densidad y poco espacio libre exigen probar composición y contraste, sin asociar la planta a BAFRAS |
| Alta | R23/R22/R21 / lib:H03–H05 | Trío potencial para H02/C02; comprobar peso visual equivalente y relación con copy aprobado, no con nombres históricos |
| Alta | R18 / lib:I03; R12 / lib:E03; R08 / lib:E06; R19 / lib:I05 | Revisar descripciones técnicas frente a lo realmente visible; un nombre de fichero no acredita la función |
| Alta | R02/R06/R11 / lib:D06/E01/E07 | Confirmar que la advertencia sintética permanece legible en cualquier uso futuro y que no parecen resultados acreditados; sin recortar sellos |
| Alta | R04/R05/R13/R17 y originales | Personas reales y entornos ajenos: evitar confusión con fundadores, clientes y equipo BAFRAS |
| Media | R14 / lib:I07 | Contraluz y poca nitidez aparente de zonas de trabajo; valor limitado frente a recursos claros |
| Media | R16/R48 / lib:I06 | Plano histórico muy denso, falta de legibilidad móvil; podría aparentar entregable propio si no se contextualiza |
| Media | R25/R29 y originales / lib:S01/S04 | Edificios identificables; riesgo de confundirlos con hotel cliente u oficina/obra BAFRAS |
| Media | R28 / lib:S03 | Piscina cubre solo una parte de Salud/educación/equipamientos; no arrastrar la antigua taxonomía sectorial del paquete |
| Técnica | R40/R46 | Revisar compatibilidad MPO y segundo fotograma solo si se necesitase recurrir al original; no modificar archivos ahora |

Hojas para revisión humana:

- [Hoja 1 · R01–R12](evidencias_B02_recursos/contactos_01.jpg): control, datos y energía.
- [Hoja 2 · R13–R24](evidencias_B02_recursos/contactos_02.jpg): instalaciones y recursos de portada.
- [Hoja 3 · R25–R36](evidencias_B02_recursos/contactos_03.jpg): sectores y primeros originales.
- [Hoja 4 · R37–R48](evidencias_B02_recursos/contactos_04.jpg): originales técnicos y plano.
- [Hoja 5 · R49–R55](evidencias_B02_recursos/contactos_05.jpg): originales de obra y sectores.

El vínculo R ↔ ruta original ↔ hoja/posición está en el JSON. Las miniaturas son para identificación: sus dimensiones no sustituyen a la resolución de origen. No se atribuye calidad final al material por su apariencia en la hoja.

## 9. Vacíos gráficos detectados

| Necesidad respaldada por D03 | Situación observada | Alternativa o insumo pendiente |
|---|---|---|
| Experiencia acreditada H06/INF-06/ENE-06/DIG-W06/PE | LIB no aporta imágenes auténticas autorizadas de las seis referencias | Expedientes y recursos propios; bloque general/neutral conforme reglas de D03; no rellenar X01–X03 con fotos de terceros |
| Tres fundadores SB-02 | No hay retratos propios en LIB | Retratos autorizados o composición tipográfica neutra; fotos del sitio existente requieren su propia validación |
| Relaciones técnicas C03/INF-05/ENE-05/DIG-W05 | Fotos sueltas no muestran una arquitectura integrada; E08/D07 ausentes | Diagramas específicos basados en relaciones correctas en fase autorizada; no crearlos ahora |
| Diagnóstico/acústica y amplitud INF-03 | No hay recurso específico de acústica; planta/foto no cubre todos los ámbitos | No exigir foto a cada ámbito; documentación real si añade comprensión |
| Descarbonización y eficiencia hídrica ENE-03 | No hay gráfico específico verificable ni caso técnico auténtico | Texto/tipografía o recurso propio posterior; gráficos DEMO no se reconvierten en datos reales |
| Integración/OT y control energético DIG-W03 | D05/D07 pendientes; no hay arquitectura/protocolos documentados en imágenes | Esquemas propios cuando se autorice; evitar atribuciones técnicas solo por fotos de pantallas |
| Seis sectores SEC-02 | Cinco imágenes preparadas con otra agrupación; no cubren uniformemente todos los contextos | D03 prefiere iconografía uniforme; no crear nuevas categorías para usar todas las fotos |
| Resultados de estudios en futuras fichas | Tres gráficos sintéticos, sin muestras anonimizadas de los dos softwares | Recabar SVG/PNG, tablas, unidades, metodología y permiso reales; no bloquear el diseño corporativo por su ausencia |
| Contacto CO-01–04 | Ningún vacío gráfico obligatorio | Página sustentada en formulario y correo; no requiere fotografía |

**INFERIDO.** El recurso más escaso no es la fotografía genérica, sino la documentación auténtica y los diagramas que expliquen relaciones. Una biblioteca extensa no justifica aumentar el número de imágenes ni crear secciones adicionales.

## 10. Recomendaciones para B02.1 y B02.2

La numeración de pasos siguientes es orientativa: no presupone un alcance nuevo autorizado. **No se han iniciado B02.1, B02.2, el diseño de páginas ni G1.**

1. **RECOMENDACIÓN para B02.1:** usar el contrato común G1 de D04 §8 y D05 §8 y la identidad recuperada por B01 para preparar la especificación del sistema visual. Mantener D03 como única fuente editorial. Separar IDs editoriales de IDs de biblioteca; revisar candidatos y licencias por recurso sin copiar instrucciones del README a producción.
2. **RECOMENDACIÓN para B02.1:** seleccionar solo recursos que aporten a una función de §6. Registrar permiso, autor, fuente, licencia, tratamiento y alternativa textual por imagen elegida. No adoptar automáticamente `READY`, `alt_es`, paletas de gráficos DEMO o clasificaciones sectoriales antiguas.
3. **RECOMENDACIÓN para B02.2:** preparar el paquete de diseño G1 aprobado en alcance: nueve wireframes completos desktop/móvil, tres maquetas completas y módulos singulares de las seis restantes, catálogo y estados. Mostrar alternativas cuando falten evidencia/retratos/medios. Ninguna maqueta debe simular proyectos realizados.
4. **RECOMENDACIÓN para B02.2:** comprobar recortes y texto en móvil, nitidez y legibilidad de gráficos/plano, contraste sobre fotos, y coherencia entre tres capacidades. Los diagramas conceptuales deberán explicar relaciones reales; las fotografías no los sustituyen.
5. **RECOMENDACIÓN de cierre posterior:** someter el conjunto a revisión global y aprobación expresa de dirección registrada; separar aprobación visual de permisos y preparación para publicar. No integrar imágenes ni refactorizar por el mero cierre de esta preparación documental.

### Validación y cierre de esta ejecución

**VERIFICADO.** D04 y D05 se armonizaron exclusivamente en §8; se preservaron sus demás apartados. Se contrastaron las 55 rutas, hashes, hojas de contactos y correspondencias de miniatura. Las siete entradas sin imagen se excluyen del inventario de archivos existentes y se registran expresamente como pendientes. El control de integridad compara la copia inicial, incluidos cambios previos del usuario, con la final; su detalle se guarda en [validación de ejecución](evidencias_B02_recursos/validacion_ejecucion.json) y el [diff documental](evidencias_B02_recursos/cambios_documentales.diff).

**PENDIENTES:** revisión independiente de licencias y condiciones comerciales, selección humana de candidatos, detalles 1:1/fotogramas MPO si fueran necesarios, recursos auténticos de referencias/equipo, diagramas y muestras de estudios. Ninguno de estos pendientes autoriza acciones productivas en esta intervención.
