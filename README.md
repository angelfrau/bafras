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
├── docs/
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

Los assets estan organizados bajo `assets/images/` por uso: marca, home, experiencia, equipo y miscelanea. No se optimizan ni convierten imagenes en este pase.

## Deployment

El despliegue observado sigue siendo compatible con GitHub Pages desde la raiz del repositorio. `CNAME` se mantiene intacto para `bafras.com`.

## Architectural Direction

Futuros pasos podran incluir contenido estructurado, templates, generacion estatica, i18n, rutas reales y automatizacion SEO. Esas capacidades son futuras, no funcionalidad existente en V0.5.
