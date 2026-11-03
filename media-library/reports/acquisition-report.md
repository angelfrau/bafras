# Informe de adquisición — BAFRAS_Website_Visual_Assets_V1

Fecha: 2026-11-02

## Cifras

| Concepto | Nº |
|---|---|
| Recursos solicitados | 36 |
| Recursos obtenidos y procesados (READY) | 29 |
|  · fotografías de Wikimedia Commons | 26 |
|  · gráficos demostrativos generados (datos sintéticos) | 3 |
| Listos para uso público | 29 |
| Pendientes de licencia (PENDING_LICENSE) | 0 |
| Requieren material propio (PENDING_ORIGINAL) | 4 |
| Requieren creación técnica (NEEDS_CREATION) | 2 |
| No encontrados (NOT_FOUND) | 1 |

Por prioridad: P1 READY 19/20; P2 READY 10/13. Los P1 que faltan son H02 (recuperación del repositorio).

Licencias de los recursos READY: CC BY-SA 4.0: 12, Public domain: 5, CC BY 2.0: 3, CC BY-SA 3.0: 3, Propio (BAFRAS Engineering): 3, CC BY 3.0: 1, CC0: 1, CC BY 4.0: 1.

## Fuentes utilizadas

- **Wikimedia Commons** (26 fotografías). Para cada archivo se consultaron, mediante la API oficial, el autor, la licencia, la URL de la licencia, si exige atribución, las restricciones y el SHA-1 del original. Ese SHA-1 se ha comprobado contra el archivo descargado.
- **Gráficos generados** (3): E01, E07 y D06, creados con datos sintéticos y con un sello visible. Están permitidos expresamente por el encargo para E01 y E07 («demostración expresamente identificada»). D06 sigue el mismo criterio.
- **Openverse, Pexels, Unsplash y Pixabay**: no se usaron. Desde el entorno de trabajo esos servidores no eran accesibles, y la API de Openverse no respondió desde el navegador local. Commons ofrece además una trazabilidad de licencia superior.

## Criterios de selección

1. Pertinencia técnica: equipos e instalaciones reales de cada disciplina, sin renders, sin IA y sin escenas corporativas genéricas.
2. Licencia compatible con uso comercial y modificación (CC0, dominio público, CC BY, CC BY-SA). Se descartaron GFDL, GPL, FAL y licencias dudosas.
3. Resolución de origen igual o superior a la de salida, sin ampliar nunca.
4. Sin marcas de agua ni fechas impresas, o recortadas cuando la licencia lo permite (I08).
5. Ningún logotipo protagonista. Se descartó una fotografía de oficinas con logotipos corporativos en la cubierta, y se recortaron un rótulo hotelero (S01) y una pancarta publicitaria (E05).
6. Coherencia visual: iluminación natural o técnica realista, sin filtros de color. H03 e I04 proceden de la misma sala técnica.
7. Ninguna imagen se asocia a proyectos de BAFRAS. Las de hoteles o edificios identificables (S01, S04) llevan una nota para no vincularlas a clientes.

## Procesamiento

- Se conserva el original sin modificar en `originals/<ID>/`, junto con `source.json` (metadatos de Commons y caja de recorte aplicada).
- Recorte al formato objetivo (16:9 en el hero, 4:3 en capacidades y 16:10 en sectores) con punto focal elegido manualmente. Redimensionado Lanczos y WebP con calidad 82 (88 en los gráficos).
- Dimensiones de salida: hero 1920×1080, capacidades 1600×1200, sectores 1600×1000. Peso total de `assets/images/`: ~5 MB.

## Problemas encontrados

- El entorno de trabajo en la nube no tenía acceso a los bancos de imágenes. La descarga se hizo con el navegador integrado del equipo local (carpeta Descargas › «bafras imagenes»), y la subida al entorno de proceso fue lenta. Siete originales (I04, I07, I08, S01, S02, S03 y S05) se procesaron a partir de copias de trabajo de 3200 px generadas en el equipo local, y sus originales completos se añadieron al ZIP directamente en ese equipo.
- Las búsquedas en Commons para obra en curso, instrumentación, redes industriales y dashboards dieron pocos resultados pertinentes. D05 queda NOT_FOUND, e I07 y D02 son aceptables pero mejorables.
- No existen dashboards energéticos reales con licencia libre que sean pertinentes, de ahí la demostración generada (E07).

## Recomendaciones de sustitución futura

1. **Prioridad alta:** I07 (obra), D02 (instrumentación), I01 (sala eléctrica) y E07/D06 (capturas reales anonimizadas de plataformas propias).
2. Hacer una sesión fotográfica en un proyecto propio o de un cliente que lo autorice (sala técnica de hotel, cubierta FV, armario de control). Con 10–12 fotos bien hechas se sustituye la mayoría de las imágenes provisionales.
3. Encargar E08, D07 y la revisión de H02 como una familia de diagramas SVG con la misma línea gráfica.
4. Mantener los nombres de archivo: la sustitución consiste solo en reemplazar el archivo y actualizar el manifiesto.
