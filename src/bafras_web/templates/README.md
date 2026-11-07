# Plantillas Jinja2 (equipo WEB)

Se distribuyen con el paquete (`package-data`) y las renderiza `bafras_web.adapters`.

- `layouts/`: estructura de documento (`<html>`, `<head>`, cuerpo).
- `partials/`: cabecera, pie, metadatos y fragmentos comunes.
- `components/`: componentes explícitos por kind/purpose, sin descubrimiento dinámico.
- `pages/`: sections.html compone las nueve páginas en orden editorial.

Las plantillas reciben modelos CONTENT originales y un PageContext tipado con destinos ya resueltos: nunca leen YAML ni contienen textos editoriales, salvo
etiquetas de interfaz procedentes de `content/<idioma>/`. Las nueve maquetas aprobadas son referencia visual y no
se copian como archivos monolíticos. Las subcarpetas se crean con su primer archivo real. Ver `docs/architecture.md`.
