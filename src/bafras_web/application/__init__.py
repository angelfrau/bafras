"""Aplicación (responsable: equipo WEB).

Responsabilidad:
Casos de uso que coordinan dominio y adaptadores: cargar y validar el sitio, preparar
páginas, determinar el contenido publicable y orquestar la construcción estática.
No contiene reglas de validación editorial.

Dependencias (comprobadas en tests/contracts/test_architecture.py):
Puede importar: editorial, localization, site, media, adapters.
No puede importar: bafras_web.cli.
"""
