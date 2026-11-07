# CONTENT-I18N-02 · Auditoría multilingüe y cierre técnico del subsistema editorial

## 1. Contexto de ejecución

- **Fecha:** 07/11/2026.
- **Rama:** `feat/contingut-v2`.
- **HEAD:** `fca65e8ba7d75317be150e3f428be67d87825d34`.
- **Entorno:** Python 3.12.10 (`.venv`), pydantic 2.14.2, PyYAML 6.0.3.
- **Sin commits:** no se ha ejecutado `add`, `commit`, `stash`, `reset`, `clean` ni cambio de rama.
- **Documento para el equipo WEB:** [CONTENT_TO_WEB_HANDOFF](../handoff/CONTENT_TO_WEB_HANDOFF.md).

## 2. Estado Git inicial

- **Modificado:** `src/bafras_web/editorial/__init__.py`, ahora API pública A1.
- **Sin seguimiento:**
  - los 44 YAML de `content/{es,ca,en,de}/`;
  - 9 módulos editoriales (`editorial/*.py`, `adapters/editorial_files.py`, `application/editorial.py`);
  - 12 archivos de prueba;
  - 13 documentos CONTENT, incluido `docs/project_v02/README.md`.

Es trabajo de CONTENT A1–A6 e I18N-01 no confirmado. Se ha preservado íntegramente: esta intervención no
modifica ninguno de esos archivos.

## 3. Inventario real

| Idioma | Páginas | Catálogos | Total | UTF-8 sin BOM | Claves duplicadas | Finales de línea |
|---|---:|---:|---:|---|---|---|
| es | 9 | 2 | 11 | sí | 0 | CRLF en 10 archivos, LF en `inicio.yaml` (bytes del manifiesto A6) |
| ca | 9 | 2 | 11 | sí | 0 | LF |
| en | 9 | 2 | 11 | sí | 0 | LF |
| de | 9 | 2 | 11 | sí | 0 | LF |

- Hay exactamente los 44 archivos esperados, sin YAML extra.
- No existen `common.yaml`, `experiences.yaml` ni `resources.yaml` en ningún idioma, como en el baseline A6.

**Documentos de referencia:**
- Localizados: D03, D04, D05, decisiones G1/DEC-05, informes A1–A6 y B1.0/B1.1, `LOCALIZATION_CONTRACT.md`,
  `TERMINOLOGY_ES.md` y `ES_BASELINE_MANIFEST.md`.
- **No localizado: informe I18N-01.** No impide ninguna comprobación técnica. Sí impide documentar la
  procedencia y el método de las traducciones.

## 4. Baseline español

- Los 11 SHA-256 coinciden con [ES_BASELINE_MANIFEST](ES_BASELINE_MANIFEST.md).
- La huella del bundle ES (`725e0f2326f9e723…`) coincide con la registrada, en ambas políticas.
- El baseline ES no ha cambiado; no se ha modificado ni el contenido ni el manifiesto.

## 5. Resultados por idioma

| Control | es | ca | en | de |
|---|---|---|---|---|
| YAML válidos (loader estricto) | 11/11 | 11/11 | 11/11 | 11/11 |
| Pydantic (`PageContent`, `list[Sector]`, `list[Person]`) | 11/11 | 11/11 | 11/11 | 11/11 |
| Paridad estructural | Referencia | 0 diferencias | 0 diferencias | 0 diferencias |
| Referencias resueltas / incorrectas | 73 / 0 | 73 / 0 | 73 / 0 | 73 / 0 |
| INCREMENTAL: completo / bundle | sí / sí | sí / sí | sí / sí | sí / sí |
| COMPLETE: completo / bundle | sí / sí | sí / sí | sí / sí | sí / sí |
| Bundle: páginas / bloques / sectores / personas | 9 / 51 / 6 / 3 | 9 / 51 / 6 / 3 | 9 / 51 / 6 / 3 | 9 / 51 / 6 / 3 |
| Errores | 0 | 0 | 0 | 0 |
| Avisos | 6 (`ENTITY_PENDING_UNCHECKED`) | 6 | 6 | 6 |
| Info | 22 `EDITORIAL_PENDING` + 2 `EXTERNAL_CONTACT_UNCHECKED` | igual | igual | igual |
| Revisión | 9 draft | 9 draft | 9 draft | 9 draft |
| Huella del bundle (SHA-256, 16 caracteres) | `725e0f2326f9e723` | `9d2c0f86c93e772f` | `d7959a95c75dce24` | `538ffc5eb055c998` |

Los diagnósticos de ca/en/de coinciden uno a uno con los de es (código, severidad, documento, selector y
motivo). La huella de cada idioma es idéntica en INCREMENTAL y COMPLETE.

## 6. Paridad estructural

- **Método:** comparación recursiva de cada árbol YAML con el de es.
  - Comprueba tipo, claves y su orden, cardinalidad y todos los valores escalares, salvo los campos
    traducibles del [contrato de localización](../localization/LOCALIZATION_CONTRACT.md).
  - Campos traducibles: `text`, `title`, `description`, `eyebrow`, `subtitle`, `attribution`, `label`,
    `submit_label`, `success`, `error`, `privacy_text`, `help`, `placeholder`, `qualification`, `specialty`.
  - Todo lo demás es protegido: `id`, `kind`, `purpose`, referencias, `review`, `pending`, `required`,
    `ContactChannel.value`, `public_name`…
- **Resultado:** 473 campos traducibles por idioma y 0 diferencias protegidas o estructurales.
- **Contraprueba:** se alteraron un `id`, un `status`, la cardinalidad y un selector de pendiente, y el
  comparador detectó los cuatro cambios.
- **Excepciones aplicadas:** ninguna. El contrato no autoriza diferencias estructurales.

**Comprobaciones lingüísticas** (sin retraducir):
- **Truncamientos:** ninguno. La razón de longitud está entre 0,5 y 1,8 en todos los textos de más de
  25 caracteres.
- **Variables o placeholders:** no hay en el baseline.
- **Tokens técnicos:** se conservan. Las diferencias detectadas son flexiones correctas (`APIs`, `PLCs`,
  `OT-Integration`, `DDC-Controller`) o equivalentes de glosario (ACS → *domestic hot water* /
  *Trinkwarmwasser*).
- **Textos idénticos a es:** siglas (PLC/DDC, SCADA/HMI, BMS, API, EMS, PPC, BESS) y palabras coincidentes
  en catalán («Verificar», «Analítica», «fotovoltaica», «Enviar consulta.», «SOBRE BAFRAS») o en inglés
  («Interfaces.»). Son correctos.

## 7. Integridad referencial y pendientes

En cada idioma:
- 73 referencias resueltas: 58 enlaces internos (página o sección), 6 `sector_refs`, 3 `person_refs` y
  6 acciones contextuales de sector;
- 2 `ContactLink` de forma válida, sin comprobar su operatividad;
- 0 `REFERENCE_UNKNOWN`, `REFERENCE_SECTION_UNKNOWN`, `PENDING_SELECTOR_INVALID` o `RESOURCE_SECTOR_MISMATCH`;
- catálogos requeridos: `people` y `sectors`.

**Pendientes:**
- 22 de página, con selectores idénticos a es;
- 6 de persona, que siguen como aviso porque B1.1 no resuelve selectores de entidad. Es una limitación
  conocida, no un defecto.

No se ha cambiado ningún estado draft, ni cerrado ningún pendiente, ni modificado ninguna regla de integridad.

## 8. Diagnóstico del loader y la aplicación

1. **Idioma:** `EditorialLoadRequest.locale` explícito. Se valida contra `config/locales.yaml`; si no está,
   `LOCALE_UNKNOWN` sin descubrir ni leer archivos.
2. **Rutas:** se esperan `content/<idioma>/pages/<page_id>.yaml` para cada `page_id` de `config/routes.yaml`,
   más los catálogos de `CATALOG_FILES`. El descubrimiento se limita a `<idioma>/`, `pages/` y `entities/`,
   con control de contención (enlaces simbólicos, carreras).
3. **Catálogos:** del mismo idioma. Son obligatorios solo si alguna referencia los usa.
4. **Páginas:** se leen con el `SafeLoader` estricto (`adapters/yaml_files.py`, el único del proyecto). El
   idioma lo aporta el contexto; se rechaza un `locale` o `page_id` declarado que no coincida.
5. **Bundle:** `build_editorial_bundle` solo procede si `can_build_bundle` es verdadero, y recalcula la
   integridad.
6. **Errores:** los problemas de contenido se devuelven como diagnósticos y no se lanzan. La configuración
   inválida lanza `ConfigurationError`, y un bundle no elegible lanza `ValueError`.
7. **Interfaces:** se documentan en el handoff, §6.
8. **Idioma por defecto:** no hay ninguno implícito en la carga.
9. **Fallback:** no existe (comprobado con un archivo ausente en cada idioma traducido).
10. **Determinismo:** documentos y diagnósticos se ordenan, y no hay estado de módulo ni caché. Las cargas
    intercaladas es → ca → en → de → es → de → ca → en → es producen huellas estables por idioma y objetos
    no compartidos.

**Conclusión:** el soporte multilingüe ya existía mediante la parametrización `locale`. No hace falta ninguna
ampliación ni API nueva.

## 9. Correcciones realizadas

**Ninguna en código ni en datos.** No hay defectos D1–D5.

**Observaciones D6** (para la revisión editorial; no se corrigen):
1. La nota `scope` de `sistemas_energeticos/entregables` empieza en minúscula en es («viabilidad y
   planificación…»). en y ca (con artículo) también empiezan en minúscula; de empieza en mayúscula porque es un sustantivo. El origen está en el baseline ES, que
   no se modifica.
2. «dirección facultativa» se mantiene en español entre paréntesis en en y de (nota `scope` de
   Infraestructuras). Parece intencionado según el glosario; debe confirmarlo la revisión lingüística.
3. No hay registro de revisión humana ni informe I18N-01 de las traducciones (§3).

## 10. Pruebas añadidas

`tests/integration/test_multilingual_content.py`: 29 pruebas. No duplican listas del dominio ni guardan
traducciones como instantánea.

| Cobertura | Prueba |
|---|---|
| Idiomas configurados = idiomas de contenido | `test_configured_locales_are_the_content_locales` |
| Inventario frente a es | `test_inventory_matches_spanish_baseline` ×3 |
| Paridad estructural y valores protegidos | `test_structure_and_protected_values_match_spanish` ×3 |
| Las claves traducibles siguen usándose (detecta deriva del contrato) | `test_contract_translatable_keys_exist_in_content` |
| Integridad por idioma = perfil es (INCREMENTAL / COMPLETE) | `test_translated_inspection_has_spanish_integrity_profile` ×6 |
| El bundle procede del idioma pedido; páginas, secciones, pendientes, sectores y personas | `test_bundle_serves_the_requested_locale_files` ×3 |
| Aislamiento, carga intercalada y determinismo | `test_interleaved_loads_are_isolated_and_deterministic` |
| Compatibilidad es (huella del manifiesto, ambas políticas) | `test_spanish_bundle_matches_baseline_manifest` |
| Archivo ausente sin fallback (ambas políticas) | `test_missing_translated_page_never_falls_back_to_spanish` ×3 |
| Documento inválido | `test_invalid_translated_document_is_explicit` ×3 |
| Referencia rota | `test_broken_translated_reference_is_an_error` ×3 |
| Idioma no soportado con contenido en disco | `test_unsupported_locale_is_rejected_even_with_content_on_disk` |

Las pruebas negativas trabajan sobre copias en `tmp_path` y no escriben en el repositorio.

## 11. Regresión y compatibilidad

| Suite | Resultado |
|---|---|
| Inicial | **544 passed** (igual que A6) |
| Final | **573 passed**, 0 skip, 0 xfail |

**Consumidores de la API editorial:** solo las pruebas. Ni el CLI ni `site`/`media` la importan todavía. No
se ha cambiado ninguna firma.

## 12. Pendientes y riesgos

| Tipo | Elemento |
|---|---|
| **A · Bloqueante técnico** | Ninguno |
| **B · Dependencias WEB** | Componentes por `kind`/`purpose`; resolución de URLs y anclas con `SiteRouting`; slugs ca/en/de; contrato `MediaRef`; menú y pie sin `common.yaml`; gating draft/publicado; SEO técnico; selector de idioma; responsive; estados del formulario |
| **C · Editorial y publicación** | Las 9 páginas en draft en los 4 idiomas; revisión lingüística ca/en/de; SEO de 4 páginas (DEC-05); H05; privacidad; datos y consentimiento de personas; referencias PE; titular legal; operatividad de email y teléfono; derechos de medios |
| **Riesgo** | Trabajo CONTENT sin commit; traducciones sin trazabilidad de vigencia frente a es; procedencia de las traducciones no documentada |

## 13. Documentación generada

- [CONTENT_TO_WEB_HANDOFF](../handoff/CONTENT_TO_WEB_HANDOFF.md): contrato operativo para WEB, con ejemplo
  ejecutado literalmente.
- Este informe.
- Una entrada nueva en el [índice documental](../../README.md).

## 14. Dictamen

| Puerta | Dictamen | Fundamento |
|---|---|---|
| **GATE A — CONTENT technical readiness** | **GO** | 44/44 YAML válidos; Pydantic correcto en los 4 idiomas; paridad sin diferencias; 73 referencias resueltas y 0 incorrectas por idioma; bundles en ambas políticas; aislamiento sin fallback; baseline ES intacto; 573/573 |
| **GATE B — WEB handoff readiness** | **GO** | API real identificada y documentada; consumo demostrado con ejemplo ejecutado; 9 tipos de sección y 10 *purposes* con su matriz; 9 páginas inventariadas; responsabilidades y dependencias delimitadas |
| **Publicación** | **Pendiente** | Revisión humana y aprobación de textos y traducciones, SEO, privacidad, autorizaciones, medios y contactos (§12 C). No bloquea el desarrollo WEB |

**Condición recomendada antes de que WEB empiece:** confirmar en Git el trabajo CONTENT (A1–A6, I18N-01 y esta
intervención), para que WEB parta de un estado recuperable.
