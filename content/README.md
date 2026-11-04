# content/ — contenido editorial localizado (CONTENT-ES-01)

Fuente operativa del contenido de la web, validada por `bafras_web.editorial` y `bafras_web.localization` mediante el
único cargador YAML del proyecto (`bafras_web.adapters`). El texto español procede de D03 V1.22 y sus adendas
(`docs/project_v02/`); las maquetas no son fuente editorial.

- `es/`: idioma de origen, con la estructura completa de las páginas.
- `ca/`, `en/`, `de/`: traducciones; se crean cuando haya contenido.
- El nombre de archivo y los identificadores son estables y se comparten entre idiomas. Los slugs localizados viven en
  `config/routes.yaml`.

Ver `docs/architecture.md`, apartado «Contrato con CONTENT-ES-01».
