# BAFRAS WEB V2

Generador estático de la web corporativa de BAFRAS Engineering: contenido YAML validado con Pydantic v2 y HTML
generado con Jinja2. Sin backend, base de datos ni CMS.

**Estado:** base de arquitectura implantada (WEB-G2-00). Aún no hay contenido ni build: los desarrollan CONTENT-ES-01 y
las fases siguientes. La web publicada (`main`) es el sitio anterior.

## Puesta en marcha

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"   # Linux/macOS: .venv/bin/python
.venv/Scripts/bafras-web doctor                    # comprueba dependencias y estructura
.venv/Scripts/python -m pytest                     # pruebas
```

## Estructura

| Ruta | Contenido |
|---|---|
| `src/bafras_web/` | Paquete Python: `editorial`, `localization`, `site`, `media`, `application`, `adapters`, `templates`, `cli` |
| `config/` | Configuración técnica del sitio |
| `content/` | Contenido editorial por idioma (`es`, `ca`, `en`, `de`) |
| `assets/` | Recursos publicables (imágenes; CSS, JS y documentos cuando existan) |
| `media-library/` | Originales, procedencia, licencias y atribución. No se publica |
| `docs/project_v02/` | Documentación aprobada: D02–D05, acta G1, maquetas y auditorías |
| `dist/` | Salida generada; no se versiona |

Arquitectura, reglas de dependencia, CLI y reparto entre equipos: [docs/architecture.md](docs/architecture.md).
