"""Recursos (responsable: equipo WEB).

Responsabilidad:
Identificación de recursos, referencias editoriales a medios, catálogo de recursos
publicables a partir de media-library/manifests/media-manifest.yaml (sin duplicarlo),
comprobación de existencia y de permisos de publicación, URLs de assets.

Dependencias (comprobadas en tests/contracts/test_architecture.py):
No puede importar: yaml, jinja2 ni ningún otro subpaquete de bafras_web.
La lectura del manifiesto la realiza un adaptador.
"""
