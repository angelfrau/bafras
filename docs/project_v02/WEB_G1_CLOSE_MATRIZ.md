# BAFRAS WEB — WEB-G1-CLOSE · Matriz de incidencias
**Fecha:** 03/11/2026 · **Vigencia:** esta matriz es el **registro de estado vigente** de las incidencias. `WEB_G1_REVIEW_01_INCIDENCIAS.csv` conserva la evidencia, la descripción y la acción originales. Su columna `estado` queda como histórica (estado al cierre de REVIEW-01) y no se ha modificado, para no duplicar fuentes de estado.

**Estados:** `RESOLVED` resuelta con evidencia · `PARTIAL` parcialmente resuelta · `OPEN` abierta, con autoridad suficiente para resolverla en su fase · `DEFERRED` diferida a una fase posterior por una regla documental explícita (no está resuelta) · `ACCEPTED_EXCEPTION` excepción con autorización documentada (**ninguna hoy**: las excepciones propuestas siguen en `BLOCKED_DECISION` hasta que se firme el acta) · `BLOCKED_DECISION` requiere decisión de dirección (ver `WEB_G1_CLOSE_DECISIONES.md`).

**Tipo de bloqueo:** `GOB` gobierno/gate · `IMPL` impide construir correctamente el sistema · `INTEG` impide cerrar una página o funcionalidad · `PUBL` permite desarrollar, pero no desplegar · `DOC` documental, sin efecto en el código · `—` ninguno.

## Resumen
- 71 incidencias: 61 de REVIEW-01 y 10 nuevas (WGR-091…100).
- Estados: RESOLVED 9 · PARTIAL 5 · OPEN 19 · DEFERRED 15 · BLOCKED_DECISION 23 · ACCEPTED_EXCEPTION 0.
- No resueltas por severidad: **P0 8** · P1 27 · P2 27.
- Las 8 P0 no resueltas: 3 bloquean el **inicio** (WGR-090 acta, WGR-050 diagramas, WGR-092 control de versiones) y 5 son **solo de publicación** (WGR-080…084). Las de publicación no se convierten en P0 de desarrollo.
- No resueltas por bloqueo: GOB 7 · IMPL 22 · INTEG 15 · PUBL 12 · DOC 4 · ninguno 2.
- Cambios de estado frente a REVIEW-01: WGR-009 y WGR-012 pasan de ACEPTADA a **RESOLVED**, porque ya las cubre una regla documental de D03 y no hacía falta excepción. WGR-041 y WGR-086 pasan a **DEFERRED** (por D04 §8 G5 y 03.SEC.CAT-01). WGR-070/071/073/074 pasan a **DEFERRED** (por D04 §14). WGR-080…085 pasan a **DEFERRED** (gate G4). Las decisiones abiertas pasan a **BLOCKED_DECISION**.
- Severidades revisadas: se mantienen. WGR-002 sube en urgencia por WGR-091, pero no en severidad: D03 sigue siendo vinculante para el contenido.

## Incidencias nuevas
- **WGR-091** (P1, BLOCKED_DECISION): D02 (`02_posicionamiento.md`, 2347 líneas) estaba disponible el 02/11 (B01 L5, L36) y ha desaparecido; no hay copia en Git.
- **WGR-092** (P0, PARTIAL): Documentación G1, biblioteca de medios y trabajo de septiembre sin control de versiones (única copia local).
- **WGR-093** (P1, BLOCKED_DECISION): `origin/main` en 4af79e0 (local 04c92c8); ramas remotas `contratos-menores` y `presupuesto-pdf` sin inspeccionar; fuente de GitHub Pages sin verificar.
- **WGR-094** (P2, OPEN): Finales de línea sin normalizar (`autocrlf=true`, sin `.gitattributes`).
- **WGR-095** (P2, RESOLVED): La matriz responsive reducida persistía en D04 §13, D05 §48 (L1691) y briefing L11.
- **WGR-096** (P2, DEFERRED): Los ID de imagen D01–D07 colisionan con los documentos D01–D05 (`originals/D02/D02_original.jpg`).
- **WGR-097** (P2, OPEN): Residuo rastreado `assets/images/misc/a` (2 bytes, sin referencias).
- **WGR-098** (P2, DEFERRED): Imágenes de Commons con personas identificables (R04, R05): además de la licencia, valorar el derecho de imagen.
- **WGR-099** (P2, BLOCKED_DECISION): Originales de imagen (96 MB, hasta 13 MB por archivo) sin política de versionado.
- **WGR-100** (P2, PARTIAL): `.gitignore` sin entornos ni `.env`; sin decisión sobre `dist/`.

## Matriz

| ID | Sev. | Bloqueo | Estado | Fase | Responsable | Autoridad | Depende de | Criterio de cierre |
|---|---|---|---|---|---|---|---|---|
| WGR-001 | P1 | DOC | RESOLVED | G1 | Arquitectura documental | D03 L2; D04 L2; D05 L2 | — | Cabeceras D03/D04/D05 muestran V1.22/V2.4/V4.12 y remiten a la vigencia correcta |
| WGR-002 | P1 | GOB | BLOCKED_DECISION | Antes de WEB-01 (D02) / G4 (D01) | Dirección + Editorial | D04 §1; D03 L17 | DEC-03; WGR-091 | D02 y D01 accesibles desde project_v02 con versión identificada y hash en manifiesto |
| WGR-003 | P2 | DOC | PARTIAL | G2-00 | Responsable de auditorías G1 | D04 §14 (nota) | — | Artefactos incorporados con hash o retirados de la lista de evidencias disponibles |
| WGR-004 | P2 | DOC | RESOLVED | G1 | Arquitectura documental | B02_PREP L45–46 | — | Comprobador de enlaces: 0 rotos en project_v02 |
| WGR-005 | P2 | DOC | RESOLVED | G1 | Arquitectura documental | D03 L33; D05 L6 | — | Notas de vigencia presentes en D03 y D05; ninguna decisión alterada |
| WGR-006 | P1 | DOC | RESOLVED | G1 | Arquitectura documental + QA | D05 §12.5; CA-C02-10 | WGR-095 | Los cuatro documentos citan 320/375/390/768/1024/1440 + zoom 200 % |
| WGR-007 | P2 | DOC | RESOLVED | G1 | Arquitectura documental | 99_Manifest (recalculado en G1-CLOSE) | — | sha256sum -c del manifiesto: todas las entradas OK |
| WGR-008 | P2 | DOC | DEFERRED | G2-01 | Arquitectura | D04 §1 | WGR-096 | Identificadores únicos sin ambigüedad documento/decisión |
| WGR-009 | P2 | DOC | RESOLVED | — | Arquitectura documental | D03 L31, L36: el histórico no es instrucción | — | Registrado como histórico; sin contradicción material |
| WGR-010 | P2 | IMPL | PARTIAL | G2-01 | Arquitectura + Editorial | D03 L36; TRAZABILIDAD | WGR-030 | Contenido ES estructurado con IDs H01…CO-04 validado por Pydantic y cotejado con D03 |
| WGR-011 | P2 | DOC | RESOLVED | G1 | Arquitectura documental | D04 §1 (Astro excluido) | — | Nota presente en D03; D04 sin alternativas activas |
| WGR-012 | P2 | DOC | RESOLVED | — | Diseño | D03 03.G1-01: el texto de prototipo no se copia | — | El title productivo procede de D03 L767 |
| WGR-020 | P1 | INTEG | BLOCKED_DECISION | Antes de G3-01a | Editorial (propietario D03) | Adenda 03.CO-02; 03.K.2 | DEC-04 | Adenda D03 con un único texto de éxito y de error |
| WGR-021 | P1 | INTEG | BLOCKED_DECISION | Antes de G3-01a | Editorial | Adenda 03.CO-02 | DEC-04 | Un único texto CO-01 y ayuda CO-02 en D03 |
| WGR-022 | P1 | INTEG | BLOCKED_DECISION | Antes de G3-01a | Editorial + Dirección | Adenda 03.CO-02 | DEC-04 | Copy CO-03 aprobado en D03 y coherente con correo + teléfono |
| WGR-023 | P1 | INTEG | BLOCKED_DECISION | Antes de G3-02 | Editorial | D03 L868; 03.K §2 | DEC-06 | Dos etiquetas únicas en D03 usadas en Inicio, especialidades, PE y fichas |
| WGR-024 | P1 | INTEG | OPEN | G3-02 | Desarrollo + Fundadores | 03.K §1 (prevalece sobre la maqueta, 03.G1-01) | — | SB-02 renderizado cumple 03.K; especialidades confirmadas por escrito |
| WGR-025 | P2 | INTEG | BLOCKED_DECISION | Antes de G3-01a | Editorial | D03 H05 | DEC-15 | D03 sin marca «pendiente de cotejo» en H05 |
| WGR-026 | P1 | PUBL | BLOCKED_DECISION | Antes de G3-02 / G4 | Dirección + Editorial | 03.K §2 | DEC-07 | Variante aprobada y probada en build con 0 referencias publicadas |
| WGR-027 | P2 | INTEG | OPEN | G3-01/G3-02 | Desarrollo + QA | D03 03.G1-01 | — | Prueba de paridad: dist contiene solo cadenas D03 + catálogo aprobado de etiquetas de interfaz |
| WGR-028 | P2 | INTEG | OPEN | G3-02 | Frontend | D03 C03; D05 L1283 | — | C03 renderizado con la etiqueta y sin rótulos internos |
| WGR-030 | P1 | IMPL | OPEN | G2-01 | Arquitectura | D04 §4 | G1-CLOSE INFORME §5 | Modelos Pydantic v2 + tests que cargan las nueve páginas ES |
| WGR-031 | P1 | IMPL | BLOCKED_DECISION | G2-00 | Arquitectura + SEO | D04 §3; D03 L1080 | DEC-16 | Registro de rutas aprobado y validado por test de build |
| WGR-032 | P1 | PUBL | BLOCKED_DECISION | Antes de G4-01 | Dirección | D04 §3 | DEC-14 | Decisión registrada; selector y sitemap acordes |
| WGR-033 | P1 | INTEG | BLOCKED_DECISION | Antes de cerrar G3-01b | Dirección + Operaciones | D04 §7, §9; 03.K.2 | DEC-11 | Proveedor elegido, credenciales solo en servidor, prueba E2E superada |
| WGR-034 | P1 | IMPL | OPEN | G2-01 | Arquitectura | D04 §4 Media; 03.K §5 | G1-CLOSE INFORME §7 | Validación Pydantic de créditos + test con imagen CC BY-SA |
| WGR-035 | P2 | IMPL | OPEN | G2-01 | Arquitectura | D04 §5 | DEC-12; WGR-099 | Assets publicables versionados, con hash y sin originales en dist |
| WGR-036 | P1 | IMPL | PARTIAL | Antes de WEB-01 | Usuario + Arquitectura | D04 §8 G2; WEB_00_BASELINE | DEC-13 | Árbol limpio o rama de baseline; plan de rollback aprobado |
| WGR-037 | P2 | IMPL | OPEN | WEB-01/G2-01 | Desarrollo | D04 §8 G2 | — | Build en entorno limpio idéntico byte a byte en dos ejecuciones |
| WGR-038 | P2 | IMPL | OPEN | WEB-02/G2-01 | Desarrollo | D03 V1.22 (terminología «Capacidades») | — | Suite nueva verde sobre dist; sin aserciones de copy antiguo |
| WGR-039 | P2 | PUBL | BLOCKED_DECISION | Antes de G4-01 | Dirección + Operaciones | D04 §9 | DEC-11 | Canonical, redirecciones y HTTPS verificados en staging |
| WGR-040 | P1 | INTEG | BLOCKED_DECISION | Antes de G3-01a | Editorial + SEO | D03 §4 (L1111) | DEC-05 | Registro SEO de nueve páginas sin duplicados |
| WGR-041 | P2 | — | DEFERRED | G5 (posterior al lanzamiento) | Responsables de estudios | D04 §8 G5: no bloquea el sitio | — | Paquete real validado en G5 |
| WGR-050 | P0 | GOB | BLOCKED_DECISION | G1 (acta) | Dirección + Diseño | D05 §8.5 (L66), L576 frente a L1049/L1218/L1250 | DEC-02 | Acta G1 firmada con la excepción o diagramas aprobados |
| WGR-051 | P1 | IMPL | BLOCKED_DECISION | G1 (acta) → G2-02 | Diseño + Frontend | D05 §8.1, §8.7 | DEC-09 | Tokens aprobados; plantillas sin valores fuera de tokens |
| WGR-052 | P1 | IMPL | BLOCKED_DECISION | G1 (acta) → G2-02 | Diseño | WCAG 2.2 AA (D03 §5; D04 §8 G4) | DEC-08 | Prueba automática de contraste sin fallos sobre fondos sólidos en dist |
| WGR-053 | P2 | IMPL | OPEN | G2-02 | Frontend | D05 tokens | WGR-052 | Sin colores fuera de tokens; test de contraste verde |
| WGR-054 | P1 | INTEG | OPEN | G2-02 | Diseño + Frontend | D05 §12; AUD-G1-02 | — | Pie aprobado e implementado una sola vez |
| WGR-055 | P2 | IMPL | OPEN | G2-02 | Diseño | D05 §12.3 / VIS-020 | — | Cabecera única conforme a CA-01…CA-07 |
| WGR-056 | P1 | INTEG | OPEN | Antes de cerrar G3-01b | Diseño + Editorial | AUD-G1-02 (formulario); 03.K §3 | DEC-04 | Estados aprobados y probados con lector de pantalla |
| WGR-057 | P2 | IMPL | OPEN | G2-02 | Diseño + Frontend | D03 §5; D05 | — | Migas presentes en INF/ENE/DIG/CAP y fichas, accesibles |
| WGR-058 | P2 | IMPL | OPEN | G2-02 | Frontend | D03 §5 (skip link) | — | Skip link operativo en todas las páginas de dist |
| WGR-059 | P2 | IMPL | OPEN | G2-02 (tokens) / G3-02 | Frontend + QA | D05 §12.5 | WGR-051 | 0 px de desbordamiento a 320 px en dist |
| WGR-060 | P1 | IMPL | BLOCKED_DECISION | Antes de G2-02 | Dirección + Diseño | D05 §8.1 | DEC-10 | Logo maestro identificado con hash |
| WGR-061 | P1 | PUBL | BLOCKED_DECISION | G2-02 | Diseño + Legal | attribution.md; 03.K §5 | DEC-10 | Créditos visibles conformes a cada licencia |
| WGR-062 | P2 | IMPL | OPEN | G2-02 | Diseño | D04 §3 | DEC-14 | Regla aplicada y probada |
| WGR-063 | P2 | GOB | BLOCKED_DECISION | G1 (acta) → G2-02 | Diseño + Arquitectura | D05 §8.2 | DEC-09 | Catálogo + complemento aceptados y cubiertos por plantillas |
| WGR-070 | P1 | INTEG | DEFERRED | G2-02/G3-01 | Frontend + QA | D04 §14 (criterios diferidos) | — | Cero enlaces rotos en dist; menú operable por teclado; Escape cierra |
| WGR-071 | P1 | INTEG | DEFERRED | G3/G4 | QA | D04 §14; D05 §12.5 | WGR-059 | Matriz completa en dist con capturas archivadas y revisión humana |
| WGR-072 | P1 | GOB | BLOCKED_DECISION | G1 (acta) | Dirección | D04 §8 G1 | DEC-01 | Acta firmada |
| WGR-073 | P1 | INTEG | DEFERRED | G3-01/G3-02 | QA + Editorial | D03 03.G1-01; D04 §14 | DEC-04; DEC-05 | Test de paridad sin diferencias no justificadas |
| WGR-074 | P2 | PUBL | DEFERRED | G4-01 | QA | D04 §8 G4 | — | Checklist WCAG 2.2 AA documentado |
| WGR-075 | P2 | DOC | OPEN | G2-00 | Arquitectura documental | D04 §8 G0 | — | Baseline G0 referenciado con hash |
| WGR-080 | P0 | PUBL | DEFERRED | G4-01 | Fundadores + Editorial | 03.K §2 | DEC-07 | Ficha mínima 03.K §2 completa o referencia excluida |
| WGR-081 | P0 | PUBL | DEFERRED | G4-01 | Fundadores | 03.K §1 | — | Datos y consentimientos registrados |
| WGR-082 | P0 | PUBL | DEFERRED | G3-01b (E2E) / G4-01 | Operaciones + Desarrollo | Adenda 03.CO-02; 03.K.2 | DEC-11 | Criterios 03.K.2 superados |
| WGR-083 | P0 | PUBL | DEFERRED | G4-01 | Dirección + Legal | 03.K §4 | — | Páginas legales reales enlazadas desde pie y formulario |
| WGR-084 | P0 | PUBL | DEFERRED | G4-01 | Legal + Dirección + Ingeniería | 03.K §5; attribution.md | DEC-03; DEC-10 | Registro de derechos por imagen y servicios aprobados |
| WGR-085 | P1 | PUBL | DEFERRED | G4-01 o posterior | Editorial + revisores | D04 §3 | DEC-14 | Traducciones revisadas por humano o fuera de alcance |
| WGR-086 | P2 | — | DEFERRED | Posterior | Dirección | D03 03.SEC.CAT-01: sin PDF no hay CTA | — | Build con 0 catálogos sin controles vacíos |
| WGR-090 | P0 | GOB | BLOCKED_DECISION | G1 | Dirección | D04 §8, §14 | DEC-01; DEC-02; DEC-08; DEC-09 | Acta firmada con fecha y responsable |
| WGR-091 | P1 | GOB | BLOCKED_DECISION | Antes de WEB-01 | — | B01 L5/L36 | DEC-03 | D02 reincorporado o retirado formalmente |
| WGR-092 | P0 | GOB | PARTIAL | Antes de WEB-01 | — | WEB_00_AUDITORIA §6 R2 | DEC-13 | Commits A–C ejecutados y verificados (respaldo externo ya creado) |
| WGR-093 | P1 | IMPL | BLOCKED_DECISION | Antes de WEB-01 | — | `git ls-remote` | DEC-13 | `fetch` hecho, contenido inspeccionado, fuente de Pages documentada |
| WGR-094 | P2 | IMPL | OPEN | WEB-01 | — | `git ls-files --eol` | — | `.gitattributes` en commit aislado, sin diffs de archivo completo |
| WGR-095 | P2 | DOC | RESOLVED | G1 | — | D05 §12.5 | — | Corregido en G1-CLOSE |
| WGR-096 | P2 | DOC | DEFERRED | G2-01 | — | assets-inventory.csv | WGR-008 | Contrato de asset con prefijo inequívoco y tabla de correspondencia |
| WGR-097 | P2 | IMPL | OPEN | Commit D | — | grep sin resultados | DEC-13 | `git rm` autorizado |
| WGR-098 | P2 | PUBL | DEFERRED | G4-01 | — | evidencias_B02_recursos/contactos_01.jpg | DEC-10 | Decisión de uso o sustitución registrada |
| WGR-099 | P2 | IMPL | BLOCKED_DECISION | Commit C | — | WEB_00_PLAN_SANEAMIENTO §1 | DEC-12 | Política aplicada |
| WGR-100 | P2 | IMPL | PARTIAL | WEB-01 | — | `.gitignore` | — | Entradas añadidas (hecho); `dist/` decidido con el método de despliegue |
