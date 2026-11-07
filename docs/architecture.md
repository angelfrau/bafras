# BAFRAS WEB V2 — Arquitectura del repositorio

**Estado:** implantada en WEB-G2-00 (04/11/2026), rama `feat/contingut-v2`. Esta es la referencia operativa del código. El
contexto de producto y los contratos de alto nivel están en D04 V2.4 (`docs/project_v02/04_arquitectura_software_V2_4_handoff_G1.md`).
La autoridad editorial es D03 V1.22 y sus adendas; la visual, D05 V4.12 y las nueve maquetas aprobadas.

## 1. Árbol

```text
bafras/
├── pyproject.toml            único punto de empaquetado, dependencias, CLI y pytest
├── README.md · CNAME · .gitignore · .gitattributes
├── config/                   locales.yaml (DEC-14), routes.yaml (DEC-16), site.yaml (contacto, D04 §13), composition.yaml (imágenes y variantes, D05)
├── content/                  contenido editorial localizado (CONTENT-ES-01)      → content/README.md
├── src/bafras_web/
│   ├── __init__.py           versión (desde los metadatos instalados)
│   ├── __main__.py           python -m bafras_web
│   ├── cli.py                punto de entrada bafras-web (composición)
│   ├── editorial/            dominio editorial (vacío: CONTENT-ES-01)
│   ├── localization/         idiomas, traducciones y vigencia · locales.py (idiomas admitidos y publicados)
│   ├── site/                 páginas, rutas, navegación, publicación · routes.py (URL y alternativas de idioma)
│   ├── media/                recursos y su publicabilidad
│   ├── application/          casos de uso · configuration.py (carga y validación de config/)
│   ├── adapters/             yaml_files.py (cargador YAML único), filesystem.py · Jinja2 y dist/ pendientes
│   └── templates/            plantillas Jinja2 (package-data)                    → templates/README.md
├── assets/                   fuentes publicables: images/ (hoy); css/, js/, documents/ (cuando existan)
├── media-library/            originales, manifiestos de procedencia y generadores: NUNCA se publica entera
├── tests/                    unit/ · integration/ · contracts/ · e2e/ (cuando exista build)
├── docs/                     architecture.md (este), project_v02/ (paquete G1), audits/ (histórico)
└── dist/                     salida del build: generada, ignorada por Git
```

Solo existen las carpetas con contenido real. `assets/css`, `assets/js`, `assets/documents`, `templates/*` y
`tests/e2e` se crean con su primer archivo.

## 2. Responsabilidades

| Paquete | Responsable | Responsabilidad |
|---|---|---|
| `editorial` | CONTENT-ES-01 | Modelos Pydantic v2 de páginas, secciones tipadas, entidades, CTA y SEO editorial; validación semántica; ID estables; versión del esquema; detección de cambios |
| `localization` | CONTENT-ES-01 | Idiomas, correspondencia de unidades entre idiomas, estados de traducción (`pending`, `translated`, `reviewed`, `approved`) y vigencia respecto al español. Reutiliza `editorial`; no hay un segundo modelo |
| `site` | WEB | Rutas localizadas (`routes.py`), resolución de destinos editoriales a URL (`links.py`, único lugar donde se construye un `href`), elegibilidad preview/release (`publication.py`), composición por página (`composition.py`: imagen por hueco `media` y variantes, autoridad D05) y contacto público (`settings.py`); previstos: canonical/hreflang |
| `media` | WEB | `assets.py`: contrato de lectura del manifiesto `media-library/manifests/media-manifest.yaml` (sin duplicarlo) y `resolve_image` (estado READY, alt por idioma sin inferencias, dimensiones, crédito, derechos «declarados»). No lee archivos: build_output verifica los derivados con sus metadatos MEDIA |
| `application` | WEB (excepto `editorial.py`: CONTENT) | Casos de uso: `configuration.py` (carga tipada), `editorial.py` (`inspect_editorial`, CONTENT), `build.py` (coordinación de página/sitio), `presentation.py` (contexto derivado tipado y componentes). Sin reglas editoriales |
| `adapters` | WEB (excepto `editorial_files.py`: CONTENT) | Implementados: `yaml_files.py`, el **único** cargador YAML (SafeLoader estricto que rechaza claves duplicadas; CONTENT lo reutiliza para `content/`), `filesystem.py` (raíz y estructura del proyecto) `editorial_files.py` (descubrimiento acotado de `content/<idioma>/`, CONTENT) `jinja.py` (`render_html(template_name, context, *, environment=None) -> str`: plantillas del paquete, autoescape HTML, `StrictUndefined`; no conoce modelos editoriales) `build_output.py` (derivados y salida preparada), `site_integrity.py` (HTML físico) y escritura/copia/staging en `filesystem.py` |
| `templates` | WEB | `layouts/`, `partials/`, `components/` (uno por tipo de sección), `pages/sections.html` (composición general de secciones) |
| `cli` | WEB (los equipos registran sus comandos) | Composición; sin reglas de dominio |

## 3. Reglas de dependencia

Comprobadas automáticamente en `tests/contracts/test_architecture.py`:

| Capa | Puede importar (interno) | Prohibido |
|---|---|---|
| `media` | — | `yaml`, `jinja2` |
| `editorial` | `media` | `yaml`, `jinja2`, `os`, `pathlib`, `shutil`, `io` |
| `localization` | `editorial`, `media` | `yaml`, `jinja2` |
| `site` | `editorial`, `localization`, `media` | `yaml`, `jinja2` |
| `adapters` | `editorial`, `localization`, `site`, `media` | `application`, `cli` |
| `application` | todas las anteriores y `adapters` | `cli` |
| `cli` | cualquiera | — |

No se permiten ciclos entre capas. Un ciclo se resuelve revisando responsabilidades, no creando `shared/` o `utils/`.

## 4. Empaquetado y entorno

- Paquete único `bafras-web` (layout `src/`, setuptools). Python ≥ 3.11 (verificado con 3.12.10).
- Ejecución: `pydantic>=2.12,<3`, `PyYAML>=6.0.2,<7`, `Jinja2>=3.1.6,<4`. Desarrollo (`[dev]`): `pytest>=9.1,<10`.
- Instalación, desde la raíz:
  ```bash
  python -m venv .venv
  .venv/Scripts/python -m pip install -e ".[dev]"     # Windows; en Linux/macOS: .venv/bin/python
  ```
- Pruebas: `.venv/Scripts/python -m pytest`.
- El paquete solo es importable si está instalado. Que la raíz del repositorio esté en `sys.path` no basta, y hay una prueba que lo comprueba.

## 5. CLI

Implementado:

| Comando | Función |
|---|---|
| `bafras-web --version` | Versión instalada |
| `bafras-web doctor [--project DIR]` | Dependencias instaladas, plantillas del paquete, estructura obligatoria y validación de `config/locales.yaml` y `config/routes.yaml`; código de salida 1 si hay algún problema |
| `bafras-web build --locale L (--page P \| --all) --mode preview\|release [--project DIR]` | Página individual o catálogo SITE completo. Preview no indexable en `build/preview/`; release protegido por G4 y estados editoriales, sin salida. Build individual conserva su alias histórico. |

Previstos. Su contrato está aquí, pero no se registran hasta que ejecuten operaciones reales:

| Comando | Responsable | Contrato |
|---|---|---|
| `content validate` | CONTENT-ES-01 | Carga YAML, validación Pydantic por archivo y validación transversal; errores con `archivo:línea`; salida ≠ 0 si hay errores |
| `content status` | CONTENT-ES-01 | Estado editorial y de traducción por idioma y unidad |
| `content diff` | CONTENT-ES-01 | Cambios en el contenido español que afectan a traducciones |

**Cómo añadir comandos:** escribir `_register_<grupo>(subparsers)` en `cli.py`, que crea los subcomandos y asigna
`handler`, e incluirla en `_REGISTRARS`. El handler llama a casos de uso de `application`. Si `cli.py` crece, se
convierte en el paquete `bafras_web/cli/`, sin cambiar el punto de entrada.

## 6. Flujo de generación

```
config/*.yaml + content/<idioma>/**.yaml
  → adapters (único cargador YAML; claves duplicadas = error)
  → editorial / localization / site / media (modelos Pydantic v2 y validación transversal)
  → application (bundle y referencias tipadas → contexto derivado; política por modo)
  → adapters (Jinja2, autoescape; staging e integridad) → build/preview/ + assets usados
```

Las plantillas nunca leen YAML. «Publicable» es un valor calculado, no un campo editable.
La salida pública `dist/` requiere implementar y aprobar el cierre release; no se genera en preview.

## 6 bis. Preview de una página (WEB-V01-B)

```bash
.venv/Scripts/python -m bafras_web build --locale es --page inicio --mode preview
.venv/Scripts/python -m http.server 8000 -d build/preview      # abrir http://localhost:8000/es/inicio/
```

- La salida es autónoma: `build/preview/<idioma>/<página>/index.html` y, junto a ella, `build/preview/assets/…` (solo
  CSS, JS e imágenes que la página usa, copiados desde `assets/`). Las URL de recursos son absolutas respecto a esa
  raíz (`/assets/…`), así que se sirve por HTTP; `file://` no es un modo soportado.
- Contenido: bundle editorial (incluido `content/<idioma>/common.yaml` para cabecera y pie), `SiteRouting`,
  `config/site.yaml` (contacto), `config/composition.yaml` (imágenes y variantes) y el manifiesto de medios.
- Fuente tipográfica: Inter con alternativas del sistema; no se distribuye ningún archivo de fuente todavía.

## 7. Política de publicación

- Producción = archivos estáticos de `dist/`, sin backend ni base de datos.
- `media-library/` y `docs/` nunca se publican. De `assets/` solo se copia lo referenciado y autorizado.
- El modo `release` excluye borradores, referencias sin verificar, recursos sin derechos acreditados y traducciones no publicadas.
- `CNAME` (`bafras.com`) se conserva en la raíz. El build lo copiará a `dist/` cuando se defina el despliegue (DEC-11).
- `main` es producción y no se modifica desde esta rama.

## 8. Límites entre WEB y CONTENT-ES-01

**CONTENT-ES-01 implementa:**
- `editorial/` y `localization/` (excepto `localization/locales.py`, el contrato de configuración de idiomas que mantiene WEB);
- `application/editorial.py` y `adapters/editorial_files.py` (API de carga editorial; ver `docs/project_v02/editorial/handoff/CONTENT_TO_WEB_HANDOFF.md`);
- la carga de `content/` con `adapters/yaml_files.load_yaml` (no se crea otro cargador);
- `content/es/`;
- los comandos `content *`;
- sus pruebas en `tests/{unit,contracts,integration}`.

**El equipo WEB mantiene:**
- `site/`, `media/`, `application/` (salvo `editorial.py`);
- el resto de `adapters/`;
- `templates/`, `assets/`, `config/`;
- `build`, `cli.py` y `pyproject.toml`.

Las dependencias nuevas requieren un cambio revisado de `pyproject.toml`.

## 9. Decisiones superadas

- **`docs/audits/04-target-project-structure.md`:** propuesta de contenido en JSON bajo `src/content/`. Sustituida por YAML en `content/` y `config/`.
- **`docs/audits/07-incremental-migration-plan.md` y WEB-00:** convivencia con el sitio heredado. Sustituida por la retirada completa del legacy en esta rama.
- **D04 §3 y D03 §3.1:** el prefijo `/es/` para el español queda sustituido por DEC-16 (§11): el español va sin prefijo. Los slugs de D03 §3.1 se mantienen.
- **D04 §4 (`Page.slug`):** el slug no forma parte de la página; vive solo en `config/routes.yaml`.
- **D04 §5:** árbol lógico adaptado:
  - `content/` se separa de `config/`;
  - el paquete interno se divide en las capas de §2, no en `build.py`, `models.py`, `content.py`, `routes.py` y `seo.py`;
  - los originales están en `media-library/`;
  - los descargables van a `assets/documents/`.
  - D04 no se modifica, porque su §5 se declara «objetivo lógico, adaptable».

## 10. Legacy retirado (recuperable desde Git)

Se retiraron en WEB-G2-00:
- la SPA `index.html`;
- `css/` (`tokens`, `base`, `components`, `pages`);
- `js/` (`router`, `site`, `form`);
- `tools/validate.py`;
- `tests/test_structure.py`;
- `docs/visual-system-v1.md`.

Se recuperan con `git show efa5b6f:<ruta>`; el sitio publicado sigue en `main`. Hay dos valores del CSS heredado que no figuran en D05:
- gris claro de marca `#E6E6E6`;
- contenedor de `1180px`.

El resto de la paleta (`#0E2B25`, `#1A7A5A`, `#4F7B6E`, `#2A2A2A`, `#ECE8DD`, `#F7F5F0`, `#D8D2C3`, `#4A5550`) está en D05.

`js/form.js` enviaba el formulario a FormSubmit con un mensaje de éxito no aprobado. No es base para V2. CONTACT-R1 descarta formulario y proveedor para Release 1.0; DEC-11 conserva hosting/dominio pendientes.

## 11. Idiomas y rutas: DEC-14 y DEC-16 (dirección técnica, 04/11/2026)

**DEC-14 · Internacionalización**
- El español (`es`) es el idioma fuente y el predeterminado (`config/locales.yaml: default_locale`).
- Idiomas previstos: `es`, `ca`, `en`, `de`. Solo se publica `es` (`published: true`). El idioma por defecto debe estar publicado.
- Todos los idiomas comparten plantillas, componentes, lógica y estructura funcional. Se localizan el contenido editorial, los metadatos SEO, los textos alternativos y los slugs.
- No hay fallback: un idioma o una página sin traducción publicada no se generan ni se enlazan. Que la traducción de una página esté completa y aprobada lo determinará el contenido (CONTENT-ES-01); la configuración solo declara el idioma.

**DEC-16 · Rutas y selector de idioma**
- `config/routes.yaml` es la única fuente de URL. Cada página tiene un identificador estable independiente del idioma, que también nombra `content/<idioma>/pages/<id>.yaml`, y un slug (un segmento) por idioma. La URL encadena los segmentos de las páginas padre.
- Prefijos: el español no lleva ninguno (`/`, `/capacidades/`…); `ca`, `en` y `de` usan `/ca/`, `/en/` y `/de/`.
- `SiteRouting.url(page_id, idioma)` devuelve `None` si el idioma no está publicado o la página no tiene slug en él. `SiteRouting.alternates(page_id)` devuelve solo las equivalencias publicadas: es la base del selector de idioma y de `hreflang`. Nunca se genera un enlace a una traducción inexistente.
- Validaciones:
  - identificadores `^[a-z][a-z0-9_]*$`;
  - slugs en ASCII, minúsculas y guiones simples;
  - una sola página raíz (slug vacío);
  - padres existentes y sin ciclos;
  - slug obligatorio en el idioma por defecto;
  - solo idiomas declarados;
  - una página hija solo se traduce si su padre lo está;
  - URL únicas por idioma;
  - el español no puede usar como primer segmento `ca`, `en`, `de` ni `assets`;
  - claves YAML duplicadas = error.

| `page_id` | URL española (D03 V1.22 §3.1, sin `/es/`) |
|---|---|
| `inicio` | `/` |
| `capacidades` | `/capacidades/` |
| `infraestructuras` | `/capacidades/infraestructuras-instalaciones/` |
| `sistemas_energeticos` | `/capacidades/sistemas-energeticos/` |
| `automatizacion_control` | `/capacidades/automatizacion-control/` |
| `sectores` | `/sectores/` |
| `proyectos_experiencia` | `/proyectos-experiencia/` |
| `sobre_bafras` | `/sobre-bafras/` |
| `contacto` | `/contacto/` |

La coincidencia con D03 se comprueba en `tests/integration/test_site_config.py`, que lee la tabla del propio D03. La maqueta de Inicio usaba variantes (`/infraestructuras-e-instalaciones/`, `/proyectos-y-experiencia/`) que no son fuente de rutas.

Fuera de este alcance: páginas legales, 404, fichas individuales de proyectos y la redirección de las rutas hash del sitio anterior. Se añadirán a `routes.yaml` cuando tengan contenido y decisión.


## WEB-V03 R2 · Generación española y responsabilidades

`application/build.py` reutiliza `render_page` para build individual y `build_site`; carga una sola vez
el bundle, routing, configuración y manifiesto en `BuildInputs` por ejecución. La selección procede
de SITE. `application/presentation.py` prepara el contexto Jinja tipado, navegación y entidades originales,
con un mapeo explícito `(kind, purpose)`. No lee archivos. `site/composition.py` valida selectores y variantes.
`adapters/build_output.py` verifica archivos MEDIA y materializa URL/HTML/assets ya resueltos; no decide páginas.
`adapters/site_integrity.py` comprueba HTML y destinos físicos; `adapters/filesystem.py` prepara un
hermano temporal y promueve con backup/recuperación. No se garantiza atomicidad absoluta de directorios.

`--all` genera las nueve rutas públicas bajo `build/preview/`, con `/` en `index.html`.
`--page` conserva además el alias histórico `<locale>/<page_id>/index.html` y devuelve ese archivo.
Cada ejecución sustituye el árbol preview por su selección validada y sus assets actuales; para navegar
el sitio completo debe usarse `--all`. Los enlaces a páginas conocidas fuera de una selección individual
se permiten expresamente; la comprobación completa no permite destinos ausentes.

MEDIA separa `publication_authorization` de la licencia de origen y exige referencia documental a la
autorización declarada. El estado READY no concede permiso por sí solo. DEC-10 / WEB-V02 R2 autoriza
los nueve activos asignados por D05, sin habilitar los demás ni levantar otros bloqueos de release.
Contacto R1 utiliza exclusivamente correo/teléfono: sin formulario, campos ni estados de envío.
El cambio editorial español y la adaptación pendiente de CA/EN/DE se documentan en
[CONTACT-R1](project_v02/web/CONTACT_R1.md). No hay proveedor de formulario pendiente para R1.

El build conserva las APIs `render_page`, `build_page`, `build_site`, `BuildRequest` y `BuildError`.
El adaptador devuelve sus errores propios y APPLICATION los contextualiza como BuildError.
El staging y la política preview/release permanecen protegidos por las pruebas de regresión.

QA independiente: `python scripts/capture_site.py --browser <Chrome/Chromium>` utiliza Playwright
solo en el entorno de QA, obtiene las páginas de SITE y sirve el build por HTTP loopback.
Entrega 9 PNG desktop 1440×900 y 9 mobile 390×844, DPR 1, fullPage, junto con manifest y huellas
en `artifacts/web-v03/visual-review/es/` (ignorado por Git). `--baseline-root <árbol anterior>` permite
verificar igualdad visual fuera del cambio aprobado de Contacto. No hay dependencias QA en el runtime.
