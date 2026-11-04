"""Adaptadores técnicos.

Responsabilidad:
Implementaciones concretas: lectura YAML (único cargador del proyecto, responsable:
CONTENT-ES-01), renderizado Jinja2 y escritura de dist/ (equipo WEB), sistema de
archivos del proyecto (filesystem.py).

Dependencias (comprobadas en tests/contracts/test_architecture.py):
Puede importar: editorial, localization, site, media.
No puede importar: bafras_web.application, bafras_web.cli.
"""
