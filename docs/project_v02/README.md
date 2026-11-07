# Documentación BAFRAS WEB V2

Índice operativo actualizado en WEB-V03 R2, 07/11/2026. CONTENT mantiene el baseline ES y sus
contratos editoriales; WEB conserva arquitectura, rutas, diseño e integración.
El contenido sigue en revisión draft: este índice no autoriza publicación.

## Fuentes estables y responsabilidades

| Ámbito / responsable | Documentos |
|---|---|
| Copy / CONTENT y dirección | [D03 V1.22 y addenda](03_contenido_editorial_V1_22_baseline_G1.md), [posicionamiento](02_posicionamiento.md) |
| Arquitectura / WEB | [D04 V2.4](04_arquitectura_software_V2_4_handoff_G1.md), [arquitectura del repositorio](../architecture.md), [briefing](01_Briefing_Tecnico_Desarrollo.md) |
| Diseño / WEB y dirección | [D05 V4.12](05_sistema_visual_V4_12_baseline_G1.md), [inventario de maquetas](00_Inventario_Artefactos.md), [control del paquete](99_Manifest_SHA256.md) |
| Decisiones / dirección y responsables de cada ámbito | [Registro WEB-G1](WEB_G1_CLOSE_DECISIONES.md), [matriz de cierre](WEB_G1_CLOSE_MATRIZ.md), [acta propuesta](02_Acta_Propuesta_Cierre_G1.md) |
| QA WEB | [Auditoría G1](WEB_G1_REVIEW_01_INFORME.md), [incidencias](WEB_G1_REVIEW_01_INCIDENCIAS.csv), [trazabilidad](WEB_G1_REVIEW_01_TRAZABILIDAD.md), [plan WEB](WEB_G1_REVIEW_01_PLAN_IMPLEMENTACION.md), [cierre](WEB_G1_CLOSE_INFORME.md) |
| Repositorio y medios / WEB | [Baseline WEB-00](WEB_00_BASELINE.md), [auditoría WEB-00](WEB_00_AUDITORIA_REPOSITORIO.md), [plan de saneamiento](WEB_00_PLAN_SANEAMIENTO.md), [B01](BAFRAS_WEB_B01_AUDITORIA_REPOSITORIO.md), [inventario visual B02](B02_PREP_01_INVENTARIO_RECURSOS_VISUALES.md) |
| Cierre del sitio / WEB | [WEB-V02 R2](web/WEB_V02_R2_INFORME.md), [WEB-V03 R2](web/WEB_V03_R2_INFORME.md), [Contacto R1](web/CONTACT_R1.md) |
| Integración CONTENT → WEB / WEB | [WEB-01: auditoría de integración](web/WEB_01_INFORME.md), [plan ejecutable WEB-V01-A](web/WEB_V01_A_PLAN.md) |

D03 gobierna copy; D04 contratos WEB; D05 composición. Las aprobaciones
posteriores prevalecen solo en su ámbito. Maquetas y YAML no sustituyen D03.
Los maestros, maquetas, soporte y evidencias permanecen en sus rutas anteriores.
No se crean carpetas architecture, web o decisions vacías ni se mueve material
de otro equipo para imponer simetría al árbol.

## Flujo editorial e historial A1–A6

| Carpeta | Documentos y uso |
|---|---|
| editorial/foundation | [A1: modelos](editorial/foundation/CONTENT_ES_01_A1.md), [B1.0: contrato de carga](editorial/foundation/CONTENT_ES_01_B1_0.md), [B1.1: inspección e integridad](editorial/foundation/CONTENT_ES_01_B1_1.md) |
| editorial/migration-es y rutas de entrega conservadas | [A2: Inicio](editorial/migration-es/CONTENT_ES_01_A2_INICIO.md), [A3: Capacidades](CONTENT_ES_01_A3.md), [A4: especialidades](CONTENT_ES_01_A4.md), [A5: cierre ES](CONTENT_ES_01_A5.md) |
| editorial/quality | [A2.1: paridad y pendientes](editorial/quality/CONTENT_ES_01_A2_1.md), [A6: consolidación](editorial/quality/CONTENT_ES_01_A6.md), [manifiesto ES reproducible](editorial/quality/ES_BASELINE_MANIFEST.md) |
| editorial/localization | [Contrato para la IA externa](editorial/localization/LOCALIZATION_CONTRACT.md), [terminología española](editorial/localization/TERMINOLOGY_ES.md) |
| editorial/quality · editorial/handoff | [CONTENT-I18N-02: auditoría multilingüe](editorial/quality/CONTENT_I18N_02.md), [handoff CONTENT → WEB](editorial/handoff/CONTENT_TO_WEB_HANDOFF.md) |

Cinco informes se han movido sin cambiar sus bytes. A3, A4 y A5 conservan su
ruta raíz porque ya tienen enlaces absolutos de entrega en la conversación,
fuera del control de actualización del repositorio. Las rutas
citadas dentro de sus baselines y ejemplos son referencias históricas, no
enlaces operativos actuales. El [mapa de movimientos A6](editorial/quality/CONTENT_ES_01_A6.md#reorganización-documental)
permite localizar cada nombre anterior. No hay copias duplicadas ni redirecciones.

## Convención futura

Crear informes CONTENT directamente en su carpeta de flujo, con nombre
`CONTENT_ES_01_<fase>.md`; mantener referencias relativas desde el documento.
Los maestros conservan nombre y ubicación. No crear carpetas por cada fase ni
carpetas sin documentos. Un cambio de ruta requiere inventario de consumidores,
comprobación de colisiones y actualización de enlaces controlados. Los informes
históricos no se reescriben para presentar un estado posterior.

La siguiente entrega a una IA de traducción parte de los once YAML identificados
en el manifiesto y del contrato de localización. No se han generado traducciones
ni herramientas de importación, exportación o rendering.
