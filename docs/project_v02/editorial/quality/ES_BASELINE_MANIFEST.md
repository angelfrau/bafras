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
| [pages/proyectos_experiencia.yaml](../../../../content/es/pages/proyectos_experiencia.yaml) | `d93058a816c092450577d615d8d5580db374bc87387284e9dfd97758bdff4223` |
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
editorial. Huella del bundle completo vigente (renovada en WEB-V01-B, 07/11/2026):

`1ec660a628e614dbe9623a8fa9834a3705ab478d6a7af1af283117b8cf3514a9`

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
