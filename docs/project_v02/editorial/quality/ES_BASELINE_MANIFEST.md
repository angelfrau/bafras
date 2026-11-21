# Manifiesto del baseline editorial ES

Fecha: 06/11/2026. Intervención CONTENT-ES-01 / A6 V2.
Rama: `feat/contingut-v2`. HEAD: `fca65e8ba7d75317be150e3f428be67d87825d34`.
Los datos permanecen sin consolidar mediante commits. No es un release, tag,
aprobación editorial ni permiso de publicación.

## Autoridad e inventario

Copy: [D03 V1.22](../../03_contenido_editorial_V1_22_baseline_G1.md), incluidas
03.K, 03.K.2, 03.SEC.CAT-01/02, 03.CO-02 y 03.G1-01/02 según su ámbito.
[D04 V2.4](../../04_arquitectura_software_V2_4_handoff_G1.md) gobierna contratos
WEB y [D05 V4.12](../../05_sistema_visual_V4_12_baseline_G1.md) composición.
[DEC-05 y registro G1](../../WEB_G1_CLOSE_DECISIONES.md) conservan sus decisiones pendientes.
Los mockups no gobiernan el copy. Se conserva la selección aplicada en A1–A5.

| Archivo en content/es/pages | Bloques | Revisión |
|---|---:|---|
| automatizacion_control.yaml | 7 | draft |
| capacidades.yaml | 5 | draft |
| contacto.yaml | 4 | draft |
| infraestructuras.yaml | 7 | draft |
| inicio.yaml | 7 | draft |
| proyectos_experiencia.yaml | 4 | draft |
| sectores.yaml | 5 | draft |
| sistemas_energeticos.yaml | 7 | draft |
| sobre_bafras.yaml | 5 | draft |

Total: nueve páginas, 51 bloques. Catálogos: `entities/sectors.yaml`, seis
sectores canónicos y tres ejemplos por sector; `entities/people.yaml`, Murti,
Àngel y Amin en ese orden, todos draft y sin verificación/autorización afirmada.
No existen catálogos common, experiences o resources; no se crean para completar
el inventario. PE conserva tres agrupaciones sin experiencias confirmadas.

## Huellas de los once YAML

SHA-256 calculado sobre bytes, no sobre una reserialización YAML. Los once
archivos son idénticos a los del preflight A6; no hubo normalización masiva.

| Ruta relativa a content/es | SHA-256 |
|---|---|
| [entities/people.yaml](../../../../content/es/entities/people.yaml) | `791226abf439067bddfe876d3924eedff2d4cf37e3d99548012327d976b26758` |
| [entities/sectors.yaml](../../../../content/es/entities/sectors.yaml) | `9a3ee52727f6ddbeb730052580cac74f6685538475f6f4392e2f91621fa1bcfd` |
| [pages/automatizacion_control.yaml](../../../../content/es/pages/automatizacion_control.yaml) | `12b5d3a0de0267ceea18cc21801e2fc58cde2bcacf92ff74bbd4ed1a7ac9be8a` |
| [pages/capacidades.yaml](../../../../content/es/pages/capacidades.yaml) | `c87c64f1324cd57041eb889919dae2732abea349259dfec3a94e59fbc7ffd83a` |
| [pages/contacto.yaml](../../../../content/es/pages/contacto.yaml) | `1d04dab1400de87b1ccfe4ebf3f6182a5016833a47d6736c6c193bb4a6e86c41` |
| [pages/infraestructuras.yaml](../../../../content/es/pages/infraestructuras.yaml) | `074f3578a99a0bcd4df715acf469b57882c444ca3a05740c836a10e1b1252613` |
| [pages/inicio.yaml](../../../../content/es/pages/inicio.yaml) | `5f9b0f1411ea6b04a8e6205614125e9bb8bf8f47cc2b115ea7d62a5cd65e9713` |
| [pages/proyectos_experiencia.yaml](../../../../content/es/pages/proyectos_experiencia.yaml) | `0b4b85c38db36649ec6c5db4a96723f3881a4f1e019b1feb1310f5c65cf11549` |
| [pages/sectores.yaml](../../../../content/es/pages/sectores.yaml) | `2ffe51d3b51ce387f113298e73f0f675d9a2fa40e2bb0a3d9d154270465eb765` |
| [pages/sistemas_energeticos.yaml](../../../../content/es/pages/sistemas_energeticos.yaml) | `ce1e88e274a379d61a07c40d73a17318007e99201feb347a6237a97b6e6cb312` |
| [pages/sobre_bafras.yaml](../../../../content/es/pages/sobre_bafras.yaml) | `828337905fe9d81830410f646b7495cd84a348c8a5583768c1b3914cbdf543e9` |

Desde la raíz del checkout pueden recalcularse con PowerShell:

```powershell
Get-ChildItem -LiteralPath content/es/pages,content/es/entities -Filter *.yaml | Get-FileHash -Algorithm SHA256
.venv/Scripts/python.exe -B -m pytest -q
```

Para reproducir el estado editorial, usar ProjectPaths sobre la raíz,
inspect_editorial con locale es y cada política INCREMENTAL/COMPLETE,
assess_integrity con report_resolved=True y build_editorial_bundle. Son las
API existentes; no se añade ningún CLI o sistema de snapshots.

## Estado observado

| Comprobación | INCREMENTAL | COMPLETE |
|---|---:|---:|
| Páginas registradas / válidas | 9 / 9 | 9 / 9 |
| Ausentes / documentos inválidos | 0 / 0 | 0 / 0 |
| Referencias internas y de catálogo resueltas | 73 | 73 |
| Referencias incorrectas | 0 | 0 |
| Contactos externos no verificados | 2 info | 2 info |
| Pendientes de página | 22 info | 22 info |
| Pendientes de entidades no resueltos por B1.1 | 6 warning | 6 warning |
| Errores de selector / estructurales | 0 / 0 | 0 / 0 |
| documents_complete / can_build_bundle | true / true | true / true |

Bundle construido en ambas políticas: nueve páginas, seis sectores, tres
personas, cero experiencias y cero recursos. Catálogos requeridos: people y
sectors. La suite baseline y la suite final A6 dan **544 passed**, sin skips
ni xfail. Se usaron temporales nuevos fuera del repositorio y safe.directory
solo de proceso para las comprobaciones Git del entorno de ejecución.

Serialización de modelos determinista, con model_dump(mode="json"), claves
ordenadas, ensure_ascii=False y separadores compactos JSON; listas en su orden
editorial. Huella del bundle completo vigente (renovada en WEB-EXPERIENCE-04 V3, 21/11/2026: solo tres textos de
interfaz nuevos en common.yaml, experience-portfolio, experience-previous-work e image-adapted; ningún dato de
páginas ni de experiencias cambia):

`2625f97eb90c70b89d9fb08dfb7e3adbc9f63d68a778bc720b68857d412e82a1`

Huella WEB-EXPERIENCE-03 V2, histórica: `5c111f90bbf1f4c81cdffe698358e4096dac9c3c9da6d3567ccd3068ae6054f2`.

Huella CONTENT-EXPERIENCE-03 V2, histórica: `ab2bf9cb43912c643b0ae3ae4c5d0a862c9bfe76b65e42aaeae8f4d1814909ce`.

Huella LOCALIZATION-EXPERIENCE-01 V2, histórica: `aa08128085d56acf6d719f4b317b57612f78ea866bdb54ee698302176491e5a8`.

Huella CONTENT-EXPERIENCE-02 V3, histórica: `68aa97d688ffa89c2e6195108f91001c44bead32a368f6c0f7e83748992f4666`.

Huella anterior (WEB-V01-B / WEB-V03), histórica: `1ec660a628e614dbe9623a8fa9834a3705ab478d6a7af1af283117b8cf3514a9`.

> **Renovación WEB-V01-B (07/11/2026).** Se añade `content/es/common.yaml` (CommonContent: navegación
> aprobada en D03, denominación y textos de interfaz de las maquetas aprobadas; SHA-256
> `70cfa0f1bb12040c4f00f7c9746574c13f0268736f3efcaef85f07de285f4564`). Los once YAML de la tabla anterior
> no cambian (bytes verificados), ni páginas, bloques, referencias o pendientes. El bundle incluye ahora
> `common`, por lo que cambia su huella. Huella A6 anterior, histórica:
> `725e0f2326f9e723253c698fac34afe70ea49bb9b659edad1c8fbc4e55ab0df8`. `common.yaml` existe solo en `es`
> (traducción pendiente; sin fallback).

El [informe A6](CONTENT_ES_01_A6.md) registra también la comparación de copy y
metadatos protegidos y la verificación de los cinco informes movidos y tres
rutas de entrega conservadas.

## Pendientes y límites

Los 22 pendientes de página conservan campo, motivo y fuente: SEO de
Inicio/Capacidades/INF/ENE, selección H05, medios aprobados todavía sin MediaRef,
descripción SEO de PE, referencias PE pendientes y privacidad de Contacto.
Los seis avisos de persona conservan grafía pública/consentimiento y biografía
por confirmar. B1.1 no resuelve selectores de entidades; no se oculta ese límite.
info@bafras.com y +34 610 903 179 son datos aprobados, sin prueba de operatividad.

La revisión humana conjunta sigue pendiente y los nueve documentos permanecen
draft. Las seis candidatas PE no son referencias publicadas ni cartera BAFRAS.
No hay habilitación legal, derechos de imágenes, backend, traducciones, HTML
o autorización de publicación derivados de este manifiesto.

## Vigencia y localización

Este baseline debe renovarse si cambia cualquier byte de los once YAML, un
contrato de dominio/loader/integridad relevante, el registro WEB o una decisión
aprobada de D03 que afecte al contenido. Un cambio T3 equivalente sigue
requiriendo actualizar las huellas de bytes y registrar equivalencia. Un
cambio documental de ruta exige revisar sus enlaces, aunque no altere el copy.

No alterar los hashes a mano para aceptar diferencias. Revalidar paridad,
referencias, pendientes y bundle, y dejar constancia de la nueva revisión.
Para una entrega a IA externa usar el
[contrato de localización](../localization/LOCALIZATION_CONTRACT.md) y el
[glosario ES](../localization/TERMINOLOGY_ES.md). No se han generado traducciones.



## CONTACT-R1 / WEB-V03 R2 — 07/11/2026

La política aprobada de Release 1.0 utiliza solo correo/teléfono. Contacto ES conserva cuatro
secciones; CO-02 es ahora texto con la ayuda aprobada, se retiran controles/mensajes de envío y
el pendiente privacy_text del formulario. CO-03 usa datos de SITE y etiquetas/destinos CONTENT.
La tabla y la huella del bundle vigentes se actualizan; las observaciones A6 anteriores son históricas.
CA/EN/DE mantienen el contrato anterior y requieren adaptación revisada de Contacto.
Los otros diez YAML de la tabla y common.yaml no cambian. Revisión draft intacta.
Decisión y alcance exactos: [CONTACT-R1](../../web/CONTACT_R1.md).

## CONTENT-EXPERIENCE-02 V3 — 09/11/2026

Autoridad: EXPERIENCE-01 V2 y [addenda D03 EXPERIENCE](../../addenda/D03_ADDENDA_EXPERIENCE.md).

- `pages/proyectos_experiencia.yaml`: PE-02 con siete entradas en tres ámbitos, título del ámbito `energy`
  «Sistemas energéticos e investigación» y retirada del pendiente `sections/pe-02/groups`. Huella anterior,
  histórica: `d93058a816c092450577d615d8d5580db374bc87387284e9dfd97758bdff4223`.
- Documento nuevo, solo en `es`: `entities/experiences.yaml`
  (`3c5807091f6ba71affb50f6defad180c07fed4e3f20a014d320c06f91bda4ea0`), con siete referencias `founder_previous`,
  en `draft`, verificadas y autorizadas con evidencia.
- Modelo `Experience`: campos opcionales `role`, `key_figures` y `links` (solo destinos externos).
- Los otros diez YAML de la tabla no cambian. El bundle incluye ahora `experiences` (catálogo requerido), de ahí la
  nueva huella. Pendientes de página: 20 (antes 21).
- CA/EN/DE no cambian: PE-02 sin entradas y sin `experiences.yaml`, pendiente de localización (P-EXP-06). Las
  pruebas multilingües comprueban exactamente esa divergencia.

## LOCALIZATION-EXPERIENCE-01 V2 — 09/11/2026

- `entities/experiences.yaml` (es) corregido: rol de Formentor, The N Residences en pasado y sin afirmar la
  entrega, diez competencias y «capacidad nominal» en Dogger Bank A y Vineyard Wind 1, atribución individual sin
  la frase repetida y etiquetas de enlace aprobadas. Huella vigente
  `57d51877b2a049e42781f8194e8dd7aca68d2675f34a747157368c6607604942`; anterior, histórica:
  `3c5807091f6ba71affb50f6defad180c07fed4e3f20a014d320c06f91bda4ea0`.
- `pages/proyectos_experiencia.yaml` (es) no cambia (`746eceb3…`). Los otros diez YAML de la tabla tampoco.
- Localización completa de las siete referencias; huellas fuera de la tabla ES, a título informativo:

| Archivo | SHA-256 |
|---|---|
| ca/entities/experiences.yaml | `c07691a056bf14bfc79163ae899089450d043755ede282f4f86ceed8a99d998c` |
| en/entities/experiences.yaml | `8074f8166607d6bdd61f47907cf2dfe5bce91b77c494b6684fe3ff2e2544bbf5` |
| de/entities/experiences.yaml | `46d33a2cdbc916f787abd9475e0863c0d199c8b611fd1ef351204962509e43ee` |
| ca/pages/proyectos_experiencia.yaml | `585eb03a08f618d90a3c0cacba9d1c2a62f02af3f39cae969f07f2856fc882cd` |
| en/pages/proyectos_experiencia.yaml | `6035296da80fef2b11ee5576fead8aec47e8bde1b3359bb27a0adbb1df304327` |
| de/pages/proyectos_experiencia.yaml | `6290121d3bf4df8b6004615f5ef70c52cf3b816ca2517ddfa432d7b7f21e6165` |

- La paridad estructural entre los cuatro idiomas es completa para las experiencias. Se retira la excepción de
  test de CONTENT-EXPERIENCE-02 y `common.yaml` sigue siendo la única excepción, solo en es.

## CONTENT-EXPERIENCE-03 V2 — 09/11/2026

Limpieza editorial: se retiran de la redacción pública las notas aclaratorias o defensivas (addenda D03
EXPERIENCE §8). No cambian IDs, orden, relaciones, `emphasis`, magnitudes, enlaces, profesionales ni estados.

- `entities/experiences.yaml` (es): se retiran los cinco párrafos `intervention/scope` (Formentor, The N
  Residences, Dogger Bank A, Vineyard Wind 1 y UIB) y `attribution` queda como el nombre completo del profesional
  (incluida la referencia 7). Huella vigente `96438aecb5c6553006aebc32c785fcd9fe571021206fe3b8d194344e289500ec`;
  anterior, histórica: `57d51877b2a049e42781f8194e8dd7aca68d2675f34a747157368c6607604942`.
- `pages/proyectos_experiencia.yaml` (es): se retira `attribution` de PE-01 (nota general). Huella vigente
  `0b4b85c38db36649ec6c5db4a96723f3881a4f1e019b1feb1310f5c65cf11549` (tabla); anterior, histórica:
  `746eceb360c23b7503cf764d0afa1735ef2d2d473a8321cbfb0f96abcc7fd596`. Los otros diez YAML de la tabla no cambian.
- Mismas retiradas en ca, en y de; huellas informativas (las anteriores son las de LOCALIZATION-EXPERIENCE-01 V2):

| Archivo | SHA-256 |
|---|---|
| ca/entities/experiences.yaml | `156210cf4806dbb62b7c8c2e4331ad74064f2d671821e3fdbe8e144f7456e81b` |
| en/entities/experiences.yaml | `49d5aed9985739871ce9ec55c244cbb78f0fd21f68758ce5e30416029221cea7` |
| de/entities/experiences.yaml | `3280c45b90d49ac3751e070ebb75396be04212423ae0cd6b121c2fd8ead3de26` |
| ca/pages/proyectos_experiencia.yaml | `1f9ace453e72b2bc5c7b693f8ade62cea024f321f40e5a0ba097f5fe28e622cf` |
| en/pages/proyectos_experiencia.yaml | `063fe2a9009491d949fa361a33ff1ffa1cc507117fb811151759af26d689ac06` |
| de/pages/proyectos_experiencia.yaml | `4949171448af8fe1e9830752f9fe08d943585f14053ee2c67c62dc0ee74f4b94` |

## WEB-EXPERIENCE-03 V2 — 09/11/2026

Cambio WEB que toca CONTENT solo en interfaz y sincronización; ningún dato de las experiencias cambia.
- `common.yaml` (es): se añaden los `interface_messages` `language` y `experience-*` / `external-link` (textos de
  interfaz de la maqueta aprobada C04-PE V1 y de la addenda D05 EXPERIENCE). Navegación, marca y mensajes previos
  sin cambios. SHA-256 vigente `e58c70de0ace6a6fc7fb00f12aa45f3a80b26d6749e5056effe696923a9688e5`; anterior,
  histórica: `70cfa0f1bb12040c4f00f7c9746574c13f0268736f3efcaef85f07de285f4564`. El bundle incluye `common`, de ahí
  la nueva huella. Los once YAML de la tabla no cambian.
- ca/en/de: `common.yaml` traducido (draft) y `pages/contacto.yaml` sincronizado con CONTACT-R1 (9209efc): CO-02
  pasa de formulario a texto reutilizando su ayuda ya traducida, sin pendiente de privacidad y sin valores literales
  de contacto, igual que es. Huellas informativas:

| Archivo | SHA-256 |
|---|---|
| ca/common.yaml | `504862b2435e6c276a4b68f97822ade444a337f0394fd824547b7d3f4fa269e2` |
| en/common.yaml | `6918c0ed767c143ec11af01d086e1c95a49098181f6b6bae8aa86618144de78c` |
| de/common.yaml | `be2aaf2bedf71be2a457d68c74748a4e74bc5c8aa75ed230f57f4bf9ef48d0f5` |
| ca/pages/contacto.yaml | `f466681ae11deb97181552688f6465498574caed250aacf4c289b243aacc42f3` |
| en/pages/contacto.yaml | `a00a62bc866647ad279dde24f9220273487d8dedef17c57f5ea1a8300bd8e27f` |
| de/pages/contacto.yaml | `a2407c22777f775050b93efdf7cbe75c2506d8524b1efaa6bfac10ffe8993b50` |

- La paridad estructural es completa en los cuatro idiomas, incluido `common.yaml` y `contacto`; se retiran las
  dos excepciones de test (traducción pendiente de `common.yaml` y divergencia CONTACT-R1).
