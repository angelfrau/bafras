# EXPERIENCE · Especificación de integración WEB

Fecha: 09/11/2026 · CONTENT-EXPERIENCE-02 V3 + LOCALIZATION-EXPERIENCE-01 V2 + CONTENT-EXPERIENCE-03 V2 · Rama `feat/contingut-v2`, base
`9209efc` (cambios sin commit).
- Contenido: [addenda D03 EXPERIENCE](../../addenda/D03_ADDENDA_EXPERIENCE.md).
- Composición: [addenda D05 EXPERIENCE](../../addenda/D05_ADDENDA_EXPERIENCE.md).
- Interfaz general: [CONTENT_TO_WEB_HANDOFF](CONTENT_TO_WEB_HANDOFF.md).

**Estado: CONTENT cerrado para WEB-EXPERIENCE-03.** Siete referencias en tres ámbitos, completas en es, ca, en y
de, en draft, con redacción pública afirmativa y sin descargos visibles (§5).

## 1. Reparto

**Resuelto por CONTENT:**
- contenido y correcciones factuales;
- localización completa;
- modelo `Experience` (`role`, `key_figures`, `links`);
- entidades y relaciones con profesionales;
- magnitudes con su alcance;
- atribución pública «Profesional · Rol» y referencias destacadas explícitas;
- pruebas de paridad y de invariantes.

**Pendiente de WEB:**
- reproducir la maqueta C04-PE (anclas por ámbito, composición asimétrica, tarjetas destacadas y complementarias);
- fichas individuales y su routing;
- fotografías: selección, conversión HEIC → WebP, registro en el manifiesto y composición;
- responsive y QA visual.

`templates/components/experience_index.html` ya muestra las siete referencias, pero como paneles genéricos (§10).

## 2. Modelos reales

`bafras_web.editorial`:

| Modelo | Campos usados por WEB |
|---|---|
| `ExperienceIndexSection` (`kind="experience_index"`, `id="pe-02"`) | `title`, `introduction`, `groups` |
| `ExperienceGroup` | `id` (`infrastructure`, `automation`, `energy`), `title`, `introduction`, `entries` |
| `ExperienceEntry` | `id` (= `experience_ref`), `experience_ref`, `emphasis` (`featured` / `complementary`) |
| `Experience` | `id`, `kind`, `title`, `attribution`, `person_refs`, `role`, `summary`, `key_figures`, `context`, `systems`, `phases`, `intervention`, `deliverables`, `results` (`text` + `evidence_refs`), `links` (solo `ExternalLink`), `review`, `verification` |
| `Person` | `public_name`, `qualification`, `specialty` |

Los textos son cadenas planas, que WEB debe escapar. Las listas vacías y `None` significan «sin dato»: el módulo
se omite.

## 3. Consumo verificado

```python
from pathlib import Path
from bafras_web.adapters.filesystem import ProjectPaths, find_project_root
from bafras_web.application.editorial import EditorialLoadRequest, inspect_editorial
from bafras_web.editorial.integrity import build_editorial_bundle

paths = ProjectPaths(find_project_root(Path.cwd()))
for locale in ("es", "ca", "en", "de"):
    bundle = build_editorial_bundle(inspect_editorial(paths, EditorialLoadRequest(locale=locale, policy="COMPLETE")))
    index = next(s for s in bundle.get_page("proyectos_experiencia").sections if s.kind == "experience_index")
    for group in index.groups:                                   # orden editorial de ámbitos
        for entry in group.entries:                              # orden editorial de referencias
            ref = bundle.get_experience(entry.experience_ref)
            person = bundle.get_person(ref.person_refs[0])
            print(locale, group.id, entry.emphasis, ref.title, "|", person.public_name, "|", ref.role,
                  [f.text for f in ref.key_figures], [(l.label, str(l.target.url)) for l in ref.links])
```

Lo he ejecutado tal cual: 28 líneas (7 referencias × 4 idiomas), con 3 destacadas por idioma.

## 4. Identificadores, orden y jerarquía

| Ámbito (`group.id`) | Referencias, en orden | Profesional | Destacada (`emphasis`) |
|---|---|---|---|
| `infrastructure` | `four-seasons-formentor`, `montesion`, `the-n-residences-ibiza` | `angel` | `four-seasons-formentor` |
| `automation` | `dogger-bank-a`, `vineyard-wind-1` | `amin` | `dogger-bank-a` |
| `energy` | `uib-transicion-energetica`, `edge-ai-investigacion` | `murti` | `uib-transicion-energetica` |

La jerarquía es un **campo explícito** (`emphasis`), no una convención de orden. Los identificadores son estables
en los cuatro idiomas y sirven de anclas (ámbito) y de identidad de ficha (referencia).

## 5. Política editorial y datos de tarjeta y de ficha

**Política definitiva (addenda D03 EXPERIENCE §8, D05 EXPERIENCE §7).** Sin descargos visibles: ni nota general
junto al índice, ni aviso por tarjeta, ni notas de alcance en la ficha. WEB no debe añadir textos propios de
aclaración. PE-01 no tiene `attribution` (`None`).

| Elemento visual | Fuente |
|---|---|
| Tipo de referencia | `entry.emphasis` → «Referencia destacada / complementaria». Texto de interfaz por idioma, **todavía no** en CommonContent: hay que acordarlo con CONTENT |
| Atribución pública | «`experience.attribution` · `experience.role`» (p. ej. «Àngel Frau Salom · Técnico de instalaciones»). `attribution` es el nombre completo; equivale a `person.public_name` |
| Clasificación (opcional) | `experience.kind`: `founder_previous` → «Experiencia profesional del equipo»; `bafras_project` → «Proyecto BAFRAS». Etiqueta de clasificación, no descargo; recomendada solo si la página mezcla ambos tipos |
| Título · texto de tarjeta | `title` · `summary` |
| Magnitudes | `key_figures`, con la frase completa (máximo dos en tarjeta) |
| Ficha | `context`, `systems`, `phases`, `intervention`, `deliverables`, `results`, `links` (externos) |

**Contrato de campos (sin cambios de modelo):**
- `kind`: clasificador interno, idéntico en los cuatro idiomas (hoy todas `founder_previous`).
- `emphasis`: jerarquía explícita, `featured` (una por ámbito) o `complementary`. No derivarla del orden.
- `intervention`: solo `uib-transicion-energetica` tiene contenido (`work`, afirmativo); en las demás es `[]` y el
  módulo se omite.
- `role`, `summary`, `attribution`: presentes en las siete referencias y los cuatro idiomas.
- Opcionales con datos parciales: `key_figures` (6 de 7), `systems`, `phases`, `context`, `deliverables`,
  `results`, `links` (UIB y Edge AI).

## 6. Medios: inventario de `assets/images/experience/`

Inventario de solo lectura (09/11/2026). Son trabajo del usuario sin commit; no se ha modificado, movido,
renombrado ni convertido nada. La identificación se basa en el **nombre que el usuario dio al archivo**,
contrastado con el contenido visible; la similitud visual sola no se ha considerado confirmación. Ningún JPG/WebP
tiene GPS ni fecha de captura útil en EXIF (las cuatro fechas EXIF presentes son del 09/11/2026, de exportación).

| Ruta real (bajo `assets/images/experience/`) | Formato · px | Proyecto candidato | Identificación | Conversión |
|---|---|---|---|---|
| `Infraestructura y Instalaciones/formentor_1.jpg`, `formentor_2.jpg` | JPG · 1200×800 | `four-seasons-formentor` | Confirmada (nombre; complejo hotelero en costa arbolada) | WebP |
| `Infraestructura y Instalaciones/montesion_1.jpg`, `montesion_2.jpg` | JPG | `montesion` | Confirmada (nombre). Son **renders** arquitectónicos, no fotografías de obra | WebP |
| `Infraestructura y Instalaciones/ibiza_1.jpg`, `ibiza_2.jpg` | JPG | `the-n-residences-ibiza` | Probable: el nombre indica Ibiza, no el complejo | WebP |
| `Sistemas Energéticos/CAMPUS-UIB-2026.webp` | WebP · 1280×960 | `uib-transicion-energetica` | Confirmada (nombre; campus con marquesinas FV) | Ya web |
| `Sistemas Energéticos/8de8083c-f2ed-4352-844a-2994315f750f.JPG` | JPG · 1200×1600 | `uib-transicion-energetica` | Probable (cubierta FV; sin nombre ni metadatos) | WebP |
| `Sistemas Energéticos/Dogger Bank 1.jpg` | JPG · 640×479 | `dogger-bank-a` | Confirmada (nombre). Resolución insuficiente para destacada | WebP; no apta en gran formato |
| `Sistemas Energéticos/dogger bank 2.jpg` | JPG | `dogger-bank-a` | Confirmada (nombre) | WebP |
| `Sistemas Energéticos/amin dogger bank.jpg` | JPG | `dogger-bank-a` | Confirmada (nombre). Aparece una persona | WebP; confirmar consentimiento |
| `Sistemas Energéticos/amin vineayrd.jpg` | JPG | `vineyard-wind-1` | Confirmada (nombre). Aparece una persona | WebP; confirmar consentimiento |
| `Sistemas Energéticos/vinneyatrd turbina.jpg` | JPG | `vineyard-wind-1` | Confirmada (nombre, con errata) | WebP |
| `Sistemas Energéticos/IMG_0255…IMG_1122` (28 HEIC) | HEIC | — | No identificada (no visualizable sin conversión) | HEIC → WebP antes de valorar |
| `Automatización y Control/instrumentación 1 valvula.HEIC` | HEIC | ámbito `automation` | No identificada (proyecto) | HEIC → WebP |
| — | — | `edge-ai-investigacion` | Sin imágenes | Composición tipográfica |

Observaciones:
- Las imágenes de Dogger Bank A y Vineyard Wind 1 están en `Sistemas Energéticos/`, aunque las referencias son del
  ámbito `automation`: la carpeta no determina el ámbito.
- `assets/images/experience/mep/` (6 JPG versionados) aparece borrada en el árbol de trabajo: el usuario la ha
  reorganizado en `Infraestructura y Instalaciones/`. No se ha restaurado.
- `IMG_4155–4158.jpg` del inventario anterior ya no existen. Las HEIC suman unos 63 MB.

`Experience` no tiene campo de medios: la selección es composición D05. WEB debe:
- añadir un hueco por referencia en `config/composition.yaml`, con el patrón de selector
  `experiences/<id>/media` en `site/composition.py`;
- generar los derivados WebP sin metadatos y registrarlos en el manifiesto;
- confirmar el consentimiento de las fotos con personas y no rotular ninguna como obra de BAFRAS;
- dejar sin imagen las referencias sin material (Edge AI) con su composición tipográfica, sin hueco vacío.

## 7. Enlaces y routing

- **Enlaces externos:** `experience.links` (`ExternalLink` https). Etiquetas aprobadas en español: «Ver noticia
  institucional» y «Consultar publicación científica»; traducidas en ca, en y de. Hoy `site.links.resolve_links`
  recibe una página o el contenido común: WEB debe incluir las experiencias referenciadas.
- **Fichas:** D04 §3 las prevé como rutas adicionales, pero `config/routes.yaml` no las tiene. Opciones:
  - (a) ruta por referencia bajo `proyectos_experiencia`;
  - (b) ficha como bloque ampliado dentro de la página.

  La decisión es de WEB/D04. CONTENT no crea rutas ni slugs.

## 8. Localización

| Idioma | Referencias | Ámbitos | Traducción | Validación | Paridad |
|---|---:|---:|---|---|---|
| es | 7 | 3 | Fuente | Bundle válido (INCREMENTAL y COMPLETE) | Referencia |
| ca | 7 | 3 | Completa (draft) | Bundle válido | Estructural completa |
| en | 7 | 3 | Completa (draft) | Bundle válido | Estructural completa |
| de | 7 | 3 | Completa (draft) | Bundle válido | Estructural completa |

**Invariantes comprobados por pruebas:**
- IDs, orden, `emphasis`, `person_refs` y `kind`;
- valores numéricos de las magnitudes, normalizando el separador del idioma;
- URL, DOI, evidencias y estados;
- número de fases, sistemas e intervenciones;
- nombres oficiales sin traducir.

**Equivalencia semántica:** la he revisado manualmente referencia por referencia. Corregí tres defectos durante
la traducción:
- DE: nota de Formentor y redacción en pasado de The N Residences;
- EN: «commissioning» duplicado;
- CA: «direcció d'obra», que se podía confundir con la dirección facultativa.

CONTENT-EXPERIENCE-03 V2 retira en los cuatro idiomas las mismas notas (5 `intervention/scope` y la nota de
PE-01) y reduce `attribution` al nombre. Paridad estructural intacta.

Antes de publicar se recomienda una revisión lingüística humana nativa; no bloquea a WEB.

## 9. Criterios de aceptación WEB

1. Composición según la addenda D05: anclas por ámbito, una destacada por ámbito tomada de `emphasis` y
   complementarias sin hueco vacío.
2. Atribución «Profesional · Rol» en cada tarjeta y ficha; sin nota general ni descargos añadidos por WEB.
3. Magnitudes con su frase completa; sin cifras aisladas.
4. Ningún texto de la maqueta («pendiente de acreditación», «Material técnico autorizado…»).
5. Enlaces externos resueltos con `site.links` e identificados como externos.
6. Fichas: los módulos sin datos se omiten.
7. Imágenes en WebP, con alt descriptivo y sin metadatos visibles.
8. Responsive a 320/375/390/768/1024/1440 px y zoom 200 %.
9. Los cuatro idiomas muestran sus propias referencias, sin fallback al español.
10. `emphasis` controla la jerarquía; `kind` solo se muestra como clasificación opcional.

## 10. Problemas de presentación detectados (renderer actual)

> **Resuelto en WEB-EXPERIENCE-03 V2** ([informe](../../web/WEB_EXPERIENCE_03_INFORME.md)): tarjetas con
> «Profesional · Rol», `emphasis`, magnitudes e imagen; anclas por ámbito; siete fichas con una plantilla; imágenes
> X01–X11. Lo siguiente describe el estado anterior.

`templates/components/experience_index.html` no genera notas propias: todas las notas retiradas procedían de
CONTENT. Pendiente de WEB:
- imprime `attribution` sola, sin `role`: falta la línea «Profesional · Rol»;
- ignora `emphasis` (todas las tarjetas iguales), `key_figures` y `links`;
- vuelca en la tarjeta `context`, `intervention`, `systems`, `phases`, `deliverables` y `results` (contenido de
  ficha), sin títulos de módulo;
- no hay anclas por ámbito, ni fichas, ni imágenes.
