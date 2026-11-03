# BAFRAS.com

## Purpose

Web corporativa de BAFRAS Engineering.

## Architecture

El sitio actual es una web estatica desplegable directamente en GitHub Pages:

- HTML estatico en `index.html`.
- CSS modular en `css/`.
- JavaScript vanilla en `js/`.
- Hash routing temporal para paginas virtuales.
- Assets visuales en `assets/images/`.
- Python solo como tooling de desarrollo y validacion.

No existe backend, framework frontend, build system ni generacion de HTML en esta version.

## Project Structure

```text
.
├── index.html
├── assets/
│   └── images/
├── css/
│   ├── tokens.css
│   ├── base.css
│   ├── components.css
│   └── pages.css
├── js/
│   ├── site.js
│   ├── router.js
│   └── form.js
├── tools/
│   └── validate.py
├── tests/
│   └── test_structure.py
├── media-library/        # fuentes de imagen no publicables: manifiestos, originales, generadores
├── docs/
│   └── project_v02/      # documentación vigente V2 (D02–D05, acta G1, maquetas, auditorías)
├── CNAME
├── pyproject.toml
└── README.md
```

## Local Development

Desde la raiz del repositorio:

```bash
python -m http.server 8000
```

Abrir `http://localhost:8000/`.

## Validation

```bash
python tools/validate.py
```

El validador comprueba estructura minima, carga CSS/JS, referencias de assets, rutas hash, formulario y ausencia de referencias legacy a `/images/` en archivos operativos.

## Tests

```bash
python -m pytest
```

## Content Editing

En V0.5 gran parte del contenido comercial todavia vive directamente en `index.html`. No hay todavia content system, JSON/YAML de contenido ni plantillas.

## Visual Assets

- `assets/images/`: imágenes publicables optimizadas para web: `brand/` (logos, símbolos, favicon, avatar), `team/` (retratos usados por el sitio), `home/`, `capabilities/`, `sectors/` (derivados WebP de la biblioteca V1, en las rutas `relative_path` de `media-library/manifests/media-manifest.yaml`) y `experience/` (fotografías propias pendientes de autorización).
- `media-library/`: fuentes no publicables. Contiene `manifests/` (procedencia, licencia, autor y atribución), `reports/`, `originals/<ID>/source.json`, `originals/team/` y `originals/diagrams/` (originales propios) y `generators/` (gráficos sintéticos). Los originales de terceros (`originals/<ID>/<ID>_original.*`) se guardan solo en local y se recuperan y verifican según `media-library/README.md`.
- Los documentos descargables, como los catálogos PDF sectoriales, irán en `assets/downloads/` cuando existan (D03 03.SEC.CAT-01; D04 §11).
- Para sustituir una fotografía: actualizar el derivado y su entrada del manifiesto, manteniendo el identificador estable.

## Deployment

El despliegue observado sigue siendo compatible con GitHub Pages desde la raiz del repositorio. `CNAME` se mantiene intacto para `bafras.com`.

## Architectural Direction

Futuros pasos podran incluir contenido estructurado, templates, generacion estatica, i18n, rutas reales y automatizacion SEO. Esas capacidades son futuras, no funcionalidad existente en V0.5.
