"""Localización (responsable: CONTENT-ES-01).

Responsabilidad:
Idiomas admitidos, correspondencia entre unidades editoriales de distintos idiomas,
estados de traducción, revisión y vigencia respecto al contenido español. Reutiliza
los contratos de bafras_web.editorial; no define un segundo modelo editorial.

Dependencias (comprobadas en tests/contracts/test_architecture.py):
Puede importar: bafras_web.editorial, bafras_web.media.
No puede importar: yaml, jinja2, bafras_web.site, application, adapters, cli.
"""
