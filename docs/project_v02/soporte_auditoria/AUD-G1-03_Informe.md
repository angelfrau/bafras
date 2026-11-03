# AUD-G1-03 — Informe de intervención y evidencias

**Fecha:** 03/11/2026. **Fuentes:** D03 V1.21, D04 V2.3, D05 V4.11; nueve prototipos aprobados; AUD-G1-02. **Equipo funcional:** producto, marca, UX, marketing B2B, ingeniería, frontend/accesibilidad y SEO/i18n. No se han modificado los documentos maestros.

## Dictamen

**G1 NO cerrado.** Se ha profundizado en la inspección editorial y estática, pero el entorno bloquea incluso la navegación a una URL `data:` en Chromium (`ERR_BLOCKED_BY_ADMINISTRATOR`). Por tanto no existen pruebas visuales de responsive, interacción, teclado ni WCAG ejecutadas en navegador. Se adjunta un runner reproducible para ejecutar fuera de este entorno.

## Evidencia realizada

- **Navegación:** inspección estática de los nueve HTML integrados; rutas internas y anclas contrastadas en `AUD-G1-03_Auditoria_Estatica.csv`. La cabecera de ensayo es compartida, pero siguen presentes cabeceras/nav originales en parte de las maquetas. No se afirma que el shell productivo esté completamente integrado.
- **Responsive:** 0/36 pruebas de viewport certificadas. Intento nuevo de Chromium sobre `data:` también bloqueado. El script `ejecutar_qa_browser_local.py` está preparado para ejecutar 36 capturas y medir overflow en un entorno sin restricciones.
- **Componentes:** se conserva el catálogo de 13 familias de AUD-G1-02; es una especificación, no una implementación reutilizable. Requiere aceptación por dirección y aplicación en G2.
- **Editorial:** cotejo ampliado de **212 fragmentos candidatos** de D03 frente al texto visible extraído de los nueve HTML: **134 coincidencias normalizadas** y **78 fragmentos que requieren clasificación humana**. El cotejo incluye anotaciones internas, rótulos, enlaces y textos compuestos, de modo que estos últimos **no equivalen automáticamente a errores de copy**. Se entregan todos los fragmentos en CSV; no se ha sustituido el texto aprobado por heurísticas.

## Incidencias y criterios de cierre

| ID | Estado tras intervención | Evidencia requerida para cerrar |
|---|---|---|
| G1-001 navegación | **Parcial**: contrato y rutas; shell de ensayo conserva elementos duplicados | Renderizar las nueve páginas, comprobar menú desktop/móvil/teclado y eliminar navegación duplicada en templates productivos |
| G1-002 responsive | **Abierta, bloqueo técnico** | 36 capturas 320/390/768/1440, ausencia de overflow y revisión visual documentada |
| G1-003 componentes | **Resuelta documentalmente, pendiente aprobación** | Aceptación del catálogo de AUD-G1-02; implementar y probar componentes en G2 |
| G1-004 fidelidad editorial | **Parcial, revisión pendiente** | Clasificar cada fila no coincidente como nota interna, rótulo/CTA, falso negativo o divergencia real; corregir únicamente divergencias reales |

## Advertencias editoriales y de publicación

- Las fichas de proyectos son provisionales hasta verificar experiencia, atribución y permisos. No activar ejemplos de PDF ni resultados simulados.
- La operatividad de `info@bafras.com`, el formulario y los textos legales requiere validación de publicación, no se deduce de la maqueta.
- Las traducciones CA/EN/DE no están aprobadas.

## Próximo paso imprescindible

Ejecutar `python ejecutar_qa_browser_local.py` con `playwright` y Chromium instalados, revisar sus capturas, clasificar el CSV editorial y decidir el cierre. No se recomienda aprobar G1 basándose únicamente en comprobaciones estáticas.
