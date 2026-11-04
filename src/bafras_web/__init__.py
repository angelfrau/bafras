"""BAFRAS WEB V2: generación estática de la web corporativa de BAFRAS Engineering.

Arquitectura y reglas de dependencia: docs/architecture.md.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bafras-web")
except PackageNotFoundError:  # código fuente sin instalar
    __version__ = "0+unknown"
