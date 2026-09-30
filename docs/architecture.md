# Architecture

## Current Architecture - V0.5

```text
HTML
  ↓
CSS + Vanilla JS
  ↓
Static site
  ↓
GitHub Pages
```

Python se usa solo como tooling de desarrollo y validacion. No sirve contenido en produccion y no genera todavia el HTML.

## Responsibilities

`index.html`
: Documento principal, contenido comercial y estructura de las paginas virtuales actuales.

`css/`
: Estilos extraidos del HTML. `tokens.css` contiene variables existentes, `base.css` base global, `components.css` componentes reutilizados y `pages.css` reglas de paginas o secciones concretas.

`js/`
: JavaScript vanilla extraido del HTML. `router.js` contiene hash routing y metadata de rutas, `site.js` comportamiento global de UI e imagenes dinamicas, y `form.js` envio del formulario.

`assets/`
: Imagenes y recursos visuales organizados por uso real.

`tools/`
: Tooling local. Actualmente contiene `validate.py`.

`tests/`
: Baseline minima de tests estructurales.

`docs/`
: Documentacion tecnica y notas de evolucion.

## Current Constraints

- El contenido permanece mayoritariamente hardcoded en `index.html`.
- El hash router sigue siendo el mecanismo de navegacion.
- No hay build step.
- No hay i18n real.
- No hay paginas generadas.
- No hay backend.
- No hay framework frontend.
- No se han cambiado las URLs ni el modelo de despliegue.

## Future Direction

Una V1 potencial puede evolucionar hacia:

```text
structured content
  +
templates
  +
Python static build
  +
real routes
  +
i18n
```

Esa direccion queda diferida por diseno. V0.5 se limita a establecer una base estructural pequena y verificable.
