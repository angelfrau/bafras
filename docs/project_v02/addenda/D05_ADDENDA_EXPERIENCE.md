# D05 · Addenda EXPERIENCE — Composición de Proyectos y experiencia con referencias reales

**Fecha:** 09/11/2026 · **Intervención:** CONTENT-EXPERIENCE-02 V3 · **Base:** D05 V4.12 §13.8 (`ExperienceCard`)
y composición aprobada C04-PE V1 (`maquetas_aprobadas/C04_PE_V1_BAFRAS.zip`: `proyectos-experiencia.html`,
`plantilla-ficha-proyecto.html`). **Estado:** propuesta de concreción visual dentro de la composición aprobada. No
reabre la estética ni define rutas o contratos de software.

## 1. Página índice

1. **Hero:** como en la maqueta (eyebrow, H1, entradilla, enlace «Explorar referencias» al índice), con el texto
   de D03 PE-01. ~~La nota de atribución se muestra como aviso visible junto al índice~~ (retirada en §7: PE-01 ya no tiene nota).
2. **Navegación interna:** fila de anclas a los tres ámbitos, en el orden de PE-02. Con teclado y en móvil, la
   fila puede desplazarse horizontalmente sin cortar las etiquetas.
3. **Ámbito:** cabecera en dos columnas (índice «01 / ÁMBITO» + título | introducción), seguida de la rejilla de
   referencias. Los tres ámbitos tienen la misma jerarquía; el tercero, con dos referencias, mantiene la rejilla.
4. **Referencia destacada:** ocupa la columna ancha de la rejilla, con imagen superior, tipo de referencia,
   etiqueta de atribución, título, texto de tarjeta, hasta dos magnitudes y acceso a la ficha.
5. **Referencia complementaria:** tarjeta sin imagen (o con miniatura solo si existe material autorizado), con la
   misma secuencia de textos y el acceso a la ficha.
6. **Cierre:** PE-03 como bloque editorial y PE-04 como banda de cierre con los dos CTA aprobados.

## 2. Jerarquía de la tarjeta

| Orden | Elemento | Tratamiento |
|---|---|---|
| 1 | Tipo («Referencia destacada / complementaria») | Etiqueta pequeña en mayúsculas; color de texto con contraste AA sobre el fondo de la tarjeta |
| 2 | Clasificación («Experiencia profesional del equipo») | Opcional (§7): etiqueta de clasificación derivada de `kind`, no un descargo |
| 3 | Título | H3 dentro del ámbito (H2) |
| 4 | Texto de tarjeta | Párrafo de lectura, sin truncar |
| 5 | Magnitudes | Lista breve (máximo dos en la tarjeta; todas en la ficha). Sin cifras grandes decorativas que sugieran resultados propios |
| 6 | Profesional y rol | Línea secundaria |
| 7 | Acceso a la ficha | Enlace de texto con flecha decorativa |

La maqueta muestra marcas internas («pendiente de acreditación», «Ficha y atribución pendientes», «Material técnico
autorizado, cuando exista»). **No se muestran**: eran avisos de prototipo.

## 3. Fotografías

- Solo material autorizado, con la confirmación del usuario de EXPERIENCE-01 V2. Se publican derivados web (WebP,
  recorte 16:10 en destacadas), nunca archivos originales HEIC o JPG de cámara.
- Ningún metadato interno de imagen es visible: ni nombre de archivo, ni EXIF, ni códigos `IMG_xxxx`, ni rutas.
  El texto alternativo describe el contenido técnico de la foto, y el crédito, si lo hay, sigue las reglas de MEDIA.
- Una fotografía de un proyecto previo no se rotula como obra de BAFRAS.
- Sin fotografía, la tarjeta destacada conserva su composición tipográfica: no se reserva un hueco vacío ni se
  muestra un marcador.

## 4. Ficha individual (plantilla aprobada)

Orden de la plantilla:
1. Hero: título, etiqueta de atribución y texto de tarjeta.
2. Contexto, junto a la ficha técnica (tipo, profesional y rol, ámbito, magnitudes).
3. Sistemas.
4. Intervención (fases).
5. Entregables y evidencias.
6. Resultados.
7. Enlaces externos.
8. Retorno al índice y CTA de cierre.

**Los módulos sin datos se omiten**, sin títulos vacíos. Los campos «Período y ubicación» y «Organización» no
aparecen mientras no haya datos publicables.

## 5. Responsive y accesibilidad

- **≥ 1024 px:** rejilla con la destacada a doble anchura y las complementarias apiladas o en una segunda columna.
- **< 760 px:** una columna, en el orden editorial; la destacada conserva la imagen en 16:10.
- **Verificación:** 320, 375, 390, 768, 1024, 1440 px y zoom 200 %. Sin desbordamiento horizontal, sin texto
  cortado y con el foco visible en anclas, tarjetas y enlaces de ficha.
- Los enlaces externos (DOI, noticia institucional) se distinguen como externos sin depender solo del color.

## 6. Precisiones LOCALIZATION-EXPERIENCE-01 V2 (09/11/2026)

- **Destacadas aprobadas:** Four Seasons Formentor, Dogger Bank A y Transición energética UIB, una por ámbito y
  las primeras de cada uno. No hay que reinterpretarlas por posición: el dato (`emphasis`) es explícito.
- **Atribución:** la referencia ya no repite «no es un proyecto contratado por BAFRAS». Por eso la etiqueta de
  atribución de la tarjeta (§2, fila 2) y la nota general junto al índice (§1.1) son **obligatorias** y no pueden
  ocultarse en ningún ancho ni idioma. *(Sustituido por §7.)*
- **Magnitudes:** se muestran con su frase completa («capacidad nominal del parque», «en el programa»), nunca como
  cifra destacada aislada.
- **Enlaces de ficha:** «Ver noticia institucional» y «Consultar publicación científica» (y sus equivalentes en
  ca, en y de), marcados como externos.

## 7. Precisiones CONTENT-EXPERIENCE-03 V2 (09/11/2026)

Sustituye la precisión «Atribución» de §6 y la nota de §1.1 (addenda D03 EXPERIENCE §8).
- **Sin descargos visibles:** ni nota general junto al índice ni aviso por tarjeta o ficha. PE-01 ya no tiene
  `attribution`.
- **Atribución pública:** línea «Profesional · Rol» (`attribution` · `role`), en tarjeta (§2, fila 6) y en la ficha
  técnica (§4.2).
- **Clasificación por `kind`:** «Experiencia profesional del equipo» / «Proyecto BAFRAS» es una etiqueta de
  clasificación **opcional**, recomendada solo si la página llega a mezclar ambos tipos. No es obligatoria ni debe
  redactarse como aviso.
- **Intervención:** solo UIB conserva un módulo de intervención; en las demás referencias el campo está vacío y el
  módulo se omite (§4).
