# BAFRAS_Website_Visual_Assets_V1 — Guía de integración

> **Integración en el repositorio (WEB-00 FINAL, 03/11/2026).** El paquete ya está incorporado y la estructura de abajo describe la entrega original. En el repositorio:
> - `assets/images/…` — los 29 WebP derivados, en las rutas exactas de `relative_path` del manifiesto (versionados).
> - `media-library/manifests/`, `reports/`, `README.md` — procedencia, licencias y atribución (versionados).
> - `media-library/originals/<ID>/source.json` — metadatos y SHA-1 del original (versionado).
> - `media-library/originals/<ID>/<ID>_original.*` — originales de Wikimedia Commons (≈95 MB). **Solo en local**, excluidos de Git por `.gitignore`. Se recuperan desde `original_download_url` y se comprueban con `commons.sha1` de `source.json`. Hay copia en `../_respaldo_WEB-00_20261103/`.
> - `media-library/generators/demo_graphics.py` — una única copia del generador de los gráficos sintéticos E01, E07 y D06; antes había tres copias idénticas.
> - `media-library/originals/team/` (retratos originales) y `originals/diagrams/` (diagrama de visión, fuente del WebP de `assets/images/home/vision/`; probablemente el H02 «PENDING_ORIGINAL») — propios y versionados.
>
> Comprobación de originales: `python -c "import hashlib,json,glob,os; [print(os.path.basename(d), hashlib.sha1(open(glob.glob(d+'/*_original.*')[0],'rb').read()).hexdigest()==json.load(open(d+'/source.json',encoding='utf-8'))['commons']['sha1']) for d in sorted(glob.glob('media-library/originals/[A-Z]*[0-9]')) if glob.glob(d+'/*_original.*')]"`


Biblioteca gráfica inicial de la web corporativa de BAFRAS Engineering. Está pensada para que Codex o el equipo de desarrollo la incorporen **sin tener que volver a investigar, renombrar ni clasificar**.

```
BAFRAS_Website_Visual_Assets_V1/
├── assets/images/        ← se copia tal cual al repositorio web
├── originals/<ID>/       ← <ID>_original.<ext> sin modificar + source.json (nombre original en Commons, metadatos, SHA-1 y recorte aplicado)
├── manifests/
│   ├── media-manifest.yaml   ← fuente de verdad (36 entradas, una por recurso)
│   ├── assets-inventory.csv  ← la misma información para Excel (UTF-8, separador «;»)
│   └── attribution.md        ← créditos obligatorios y voluntarios
├── reports/
│   ├── acquisition-report.md
│   ├── missing-assets.md
│   └── contact-sheet.pdf
└── README.md
```

## 1. Copiar las imágenes al repositorio

Copia la carpeta `assets/images/` en la raíz pública del proyecto conservando las rutas:

```bash
rsync -av BAFRAS_Website_Visual_Assets_V1/assets/images/ <repo>/assets/images/
```

Las rutas del manifiesto (`relative_path`) son relativas a la raíz del sitio, por ejemplo `assets/images/home/hero/home-hero-engineering.webp`. **No incluyas `originals/` en el repositorio web**: es material de archivo y pesa unos 100 MB.

## 2. Interpretar el manifiesto

Cada entrada de `manifests/media-manifest.yaml` incluye: `id`, `filename`, `relative_path`, `page`, `section`, `role`, `priority`, `target_aspect_ratio`, `status`, la fuente y la licencia (`source_url`, `author`, `license`, `license_url`, `attribution_required`, `attribution_text`), las dimensiones (`original_dimensions`, `output_dimensions`, `output_size_bytes`), `alt_es`, `replacement_required` y `notes`.

| Estado | Significado | ¿Se publica? |
|---|---|---|
| `READY` | Descargado, procesado y con licencia verificada | Sí |
| `PENDING_LICENSE` | Identificado, con derechos sin verificar | No |
| `PENDING_ORIGINAL` | Requiere material auténtico del equipo | No |
| `NEEDS_CREATION` | Requiere elaboración técnica interna | No |
| `NOT_FOUND` | No se encontró un recurso adecuado | No |

## 3. Identificar los recursos READY

```python
import yaml
m = yaml.safe_load(open("manifests/media-manifest.yaml"))
ready = {a["id"]: a for a in m["assets"] if a["status"] == "READY"}
```

Solo existen como archivo en `assets/images/` los recursos READY (29). Los demás (H02, E08, D07, D05, X01–X03) **no tienen archivo**: el componente debe mostrar un placeholder o, mejor, ocultar el bloque.

## 4. Incorporar las imágenes en las páginas

Usa siempre `alt_es` del manifiesto como texto alternativo y respeta la relación de aspecto prevista:

```html
<img src="/assets/images/capabilities/energy/storage/energy-battery-storage.webp"
     alt="Sistema de almacenamiento en baterías en contenedores con equipos de potencia y climatización"
     width="1600" height="1200" loading="lazy" decoding="async">
```

- Hero (H01): 1920×1080, `fetchpriority="high"` y sin `loading="lazy"`.
- Tarjetas de capacidades (4:3): 1600×1200. Sectores (16:10): 1600×1000.
- Las variantes responsive (`srcset`) puede generarlas el sistema de construcción a partir de estos archivos.
- Si un componente necesita otro encuadre, usa `object-fit: cover` y `object-position`. No vuelvas a recortar los archivos.

## 5. Conservar los nombres estables

Los IDs (H01…X03), los nombres de archivo y las rutas son **contractuales**. No los renombres ni los muevas. Si el código necesita un alias, créalo en un mapa (`ID → ruta`) generado a partir del manifiesto.

## 6. Sustituir una imagen provisional por la definitiva

1. Prepara la imagen definitiva con el mismo formato (WebP), la misma relación de aspecto y dimensiones iguales o mayores.
2. Sobrescribe el archivo en la **misma ruta y con el mismo nombre**.
3. Guarda el original en `originals/<ID>/`.
4. Actualiza la entrada del manifiesto: `source_*`, `author`, `license`, `attribution_*`, `output_*`, `replacement_required: false` y `notes`. Si es material propio, `license: "Propio (BAFRAS Engineering)"`.
5. Si la imagen anterior exigía atribución, retira su crédito de la página de créditos.

El código de la web no cambia.

## 7. Gestionar los créditos

`manifests/attribution.md` contiene el texto de atribución de cada imagen y un bloque HTML listo para la página de créditos. Las imágenes CC BY y CC BY-SA **exigen** crédito visible (pie de imagen o página de créditos enlazada desde el pie y desde la imagen). Las de dominio público y CC0 no lo exigen. Los gráficos E01, E07 y D06 son propios y llevan el sello «DATOS SINTÉTICOS · GRÁFICO DEMOSTRATIVO», que **no debe recortarse ni ocultarse**.

## 8. Evitar publicar recursos no autorizados

- Publica solo entradas con `status: READY`.
- **X01, X02 y X03** (experiencia en la UIB, el Hotel Formentor y la eólica offshore) solo pueden publicarse con material autorizado, y siempre presentados como *experiencia profesional previa del equipo*. No los sustituyas por fotos genéricas.
- No asocies las imágenes de sector (S01 hotel, S04 ParcBIT) ni las de capacidades a clientes o proyectos de BAFRAS.
- Comprobación sugerida para CI:

```python
import yaml, os, sys
m = yaml.safe_load(open("manifests/media-manifest.yaml"))
bad = [a["id"] for a in m["assets"] if a["status"] != "READY" and os.path.exists(a["relative_path"])]
miss = [a["id"] for a in m["assets"] if a["status"] == "READY" and not os.path.exists(a["relative_path"])]
sys.exit(f"No READY publicados: {bad} / READY ausentes: {miss}" if bad or miss else 0)
```

## 9. Verificar imágenes rotas

```bash
# Que cada referencia del HTML exista en disco
grep -rhoE 'assets/images/[^"'"'"' )]+\.(webp|svg)' <repo>/src | sort -u | while read p; do [ -f "<repo>/$p" ] || echo "ROTA: $p"; done
# Que cada WebP se abra correctamente
python3 -c "import glob;from PIL import Image;[Image.open(f).verify() for f in glob.glob('assets/images/**/*.webp',recursive=True)];print('OK')"
```

## 10. Actualizar el inventario

El YAML es la fuente de verdad. Tras modificarlo, regenera el CSV para que no se desincronicen:

```python
import yaml, csv
m = yaml.safe_load(open("manifests/media-manifest.yaml"))
cols = ["id","filename","page","section","priority","status","relative_path","source_url","license","author","output_dimensions","original_dimensions","replacement_required","notes"]
with open("manifests/assets-inventory.csv","w",newline="",encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(cols)
    [w.writerow([a.get(c) for c in cols]) for a in m["assets"]]
```

No elimines filas de recursos que no se hayan conseguido: cambia su `status`.

---
Fecha de la adquisición: 2026-11-02. Esta tarea no ha modificado el repositorio web.
