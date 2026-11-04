"""Dominio editorial (responsable: CONTENT-ES-01).

Responsabilidad:
Modelos Pydantic v2 de páginas, secciones tipadas, entidades compartidas, CTA y
metadatos editoriales; validación semántica; identificadores estables; versión del
esquema; detección de cambios editoriales.

Dependencias (comprobadas en tests/contracts/test_architecture.py):
Puede importar: bafras_web.media.
No puede importar: yaml, jinja2, sistema de archivos (os, pathlib, shutil, io),
bafras_web.localization, site, application, adapters, cli.
"""
