"""Sitio (responsable: equipo WEB).

Responsabilidad:
Registro de páginas, rutas localizadas, navegación, resolución de enlaces internos,
política de publicación, canonical/hreflang y metadatos técnicos de publicación
(los metadatos SEO editoriales pertenecen a bafras_web.editorial). No es un router
HTTP: el sitio publicado es estático.

Dependencias (comprobadas en tests/contracts/test_architecture.py):
Puede importar: bafras_web.editorial, bafras_web.localization, bafras_web.media.
No puede importar: yaml, jinja2, bafras_web.application, adapters, cli.
"""
