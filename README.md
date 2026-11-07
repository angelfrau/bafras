# BAFRAS WEB V2

Generador estático de la web corporativa de BAFRAS Engineering: contenido YAML validado con Pydantic v2 y HTML
generado con Jinja2. Sin backend, base de datos ni CMS.

**Estado:** nueve páginas españolas completas en preview, con contenido tipado, imágenes y navegación.
WEB-V03 consolida el motor y Contacto directo por correo/teléfono. Release permanece protegido;
no se ha desplegado ni modificado `main`.

## Puesta en marcha

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"   # Linux/macOS: .venv/bin/python
.venv/Scripts/bafras-web doctor                    # comprueba dependencias y estructura
.venv/Scripts/python -m pytest                     # pruebas
.venv/Scripts/python -m bafras_web build --locale es --all --mode preview
.venv/Scripts/python -m http.server 8000 --bind 127.0.0.1 --directory build/preview
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
| `build/preview/` | Sitio local no indexable; se sirve por HTTP, no se publica |
| `scripts/capture_site.py` | QA HTTP y 18 capturas completas desde el routing |
| `artifacts/web-v03/visual-review/es/` | PNG/manifest generados localmente; fuera del commit |

Arquitectura, reglas de dependencia, CLI y reparto entre equipos: [docs/architecture.md](docs/architecture.md).

El build individual sigue disponible con `--page inicio` en lugar de `--all`; conserva el alias
`build/preview/es/inicio/index.html`. Cada build sustituye preview por su selección: termina con `--all`
para disponer del sitio completo. Contacto R1: [decisión y alcance editorial](docs/project_v02/web/CONTACT_R1.md).

QA visual opcional, sin dependencias nuevas en el runtime:

```powershell
.venv/Scripts/python -m pip install --target build/qa-tools playwright
$env:PYTHONPATH = "$PWD/build/qa-tools"
.venv/Scripts/python scripts/capture_site.py --browser "C:/Program Files/Google/Chrome/Application/chrome.exe"
```

El script sirve el build por loopback y cierra el servidor al terminar. Requiere Chrome/Chromium local
y permisos para ejecutarlo. No descarga un navegador. El manifest incluye huellas del build y las fuentes.
