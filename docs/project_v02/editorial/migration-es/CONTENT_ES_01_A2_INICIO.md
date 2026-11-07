# CONTENT-ES-01 / A2 — Primera migración editorial de Inicio

Fecha: 05/11/2026. Continuación de A1 autorizada mediante «continua».
Alcance realizado: contenido textual real de Inicio y pruebas de integración.
No se declara A2 completa en medios ni se inicia la migración de las otras páginas.

## Baseline

- Rama: `feat/contingut-v2`.
- HEAD inicial: `fca65e8ba7d75317be150e3f428be67d87825d34`.
- Los cambios de A1 permanecían sin commit. Se preservan íntegramente.
- DEC-14/16 implementadas: fuente ES, español sin prefijo e ID WEB `inicio`.
- `media/` sigue sin contrato MediaRef. No se modifica ni se inventa otro.

## Archivos añadidos

| Archivo | Responsabilidad |
|---|---|
| `content/es/pages/inicio.yaml` | Contenido real de H01–H07; IDs estables, acciones semánticas y pendientes |
| `tests/integration/test_inicio_content.py` | Carga con adaptador existente, validación A1, paridad D03 y contratos WEB |
| Este informe | Alcance, trazabilidad y condiciones pendientes |

No se modifican archivos de A1, módulos WEB, configuración, manifiestos,
dependencias, CLI ni pruebas existentes. Sin cambio de rama, commit o push.

## Trazabilidad de contenido

Fuente: `03_contenido_editorial_V1_22_baseline_G1.md`, Parte A, H01–H07,
con las reglas de autoridad y exclusión de notas de 03.G1-01/02.
No se trasladan textos adicionales de los prototipos ni fixtures sintéticos.

| D03 | Sección YAML | Contenido migrado |
|---|---|---|
| H01 | h01 / hero | Eyebrow, H1, subtítulo, párrafo y dos CTA |
| H02 | h02 / cards / capabilities | H2, introducción, tres capacidades con descripción, tres ejemplos y enlace; acción al índice |
| H03 | h03 / item_list / needs | H2, introducción y cuatro necesidades con título, descripción y destino propio |
| H04 | h04 / process / workflow | H2, introducción, cuatro pasos, cierre de alcance y enlace |
| H05 | h05 / cards / sector_preview | H2, introducción, cuatro grupos propuestos y enlace único; aprobación pendiente |
| H06 | h06 / text | H2, párrafo general de experiencia y enlace; sin cartera ficticia |
| H07 | h07 / text | H2, párrafo, CTA específico y microcopy de colaboración |

Los rótulos documentales «Tarjeta», «Situación» y «Paso» identifican estructuras;
no se copian como prefijos de título. La numeración se deriva del orden.
La puntuación del texto público se conserva, incluidos puntos finales de ejemplos,
etiquetas H05 y enlaces H03. No se corrige por criterio de estilo.

El documento queda en estado `draft`: no se presupone que una migración
estructural apruebe pendientes editoriales o habilite publicación.

## Contrato de carga utilizado

El YAML contiene el PageContent existente salvo `locale`, aportado por el contexto:

```python
raw = load_yaml(paths.content / "es" / "pages" / "inicio.yaml")
page = PageContent.model_validate({**raw, "locale": routing.locales.default_locale})
```

Las pruebas reutilizan `adapters/yaml_files.load_yaml` y
`application/configuration.load_site_routing`; no crean un cargador de producción
ni cambian su perfil de interpretación YAML. La comprobación de forma y tipos
la realiza el dominio A1. El contexto contrasta idioma, nombre de archivo e ID
con la configuración existente. No hay fallback.

Los 14 enlaces contienen page_id, sin URL ni slug. Su existencia se contrasta
con el registro WEB. Que una ruta esté configurada no demuestra que su contenido
editorial ya exista, esté aprobado o sea publicable.

No se añade common.yaml: las acciones de esta página son locales y las de H01/H07
tienen copy diferente. La extracción de textos realmente compartidos se hará con
evidencia de reutilización al migrar más páginas. No hay referencias comunes rotas.

## Pendientes preservados

| Selector | Motivo | Fuente |
|---|---|---|
| seo.title | approval_required | DEC-05 |
| seo.description | approval_required | DEC-05 |
| sections/h05/items | approval_required | D03 H05 / DEC-15 |
| sections/h01/media | integration_pending | D05, R24 |
| sections/h02/items/infrastructure/media | integration_pending | D05, R23 |
| sections/h02/items/energy/media | integration_pending | D05, R22 |
| sections/h02/items/automation/media | integration_pending | D05, R21 |
| sections/h03/media | integration_pending | D05, R03 |

Los Rxx se conservan exclusivamente como procedencia documental interna.
No se convierten en IDs del manifiesto ni se publica una equivalencia supuesta.
No se inventan alt, pies, derechos o rutas. Los campos media siguen siendo None.

## Verificación

`tests/integration/test_inicio_content.py` contiene 12 pruebas:

- Una comparación completa de textos públicos por cada bloque H01–H07.
  El oráculo lee D03 en pruebas y excluye instrucciones y notas internas.
  Compara multiconjuntos de textos para detectar omisiones, repeticiones y añadidos.
- Identidad, locale, orden de secciones y reconstrucción JSON.
- Los 14 enlaces y sus destinos de capacidad/necesidad.
- SEO, H05 y cinco referencias de medios pendientes explícitos.
- Orden e IDs semánticos de tarjetas, necesidades, pasos y grupos.
  Reordenar tarjetas conserva contenido e identidad.
- Ausencia de cartera ficticia y paneles extra de maqueta; CTA específico H07.

El test no certifica layout, HTML, accesibilidad, derechos, salida release ni
disponibilidad editorial de las páginas destino. Es extracción documental de
pruebas: la aplicación futura no debe generar el sitio leyendo Markdown maestro.

Comando específico:

```powershell
.venv/Scripts/python.exe -B -m pytest tests/integration/test_inicio_content.py -q
```

Resultado específico: 12 pruebas aprobadas. Suite completa: 232 pruebas aprobadas,
sin regresiones. Se utilizó un temporal nuevo y la excepción safe.directory
limitada al proceso, como en A1; no cambió la configuración Git persistente.

## Siguiente integración

1. WEB proporciona MediaRef y confirma correspondencias visual/manifiesto.
2. Se amplían los campos de medios con ese contrato y pruebas de alt/contexto,
   sin introducir un catálogo paralelo.
3. Editorial confirma SEO y las etiquetas H05.
4. Se acuerdan API de carga, declaración de esquema y validación transversal
   con application; no se modifican esos contratos compartidos unilateralmente.
5. Se migran las siguientes páginas y el contenido común con paridad documental.

Este incremento deja la parte textual de Inicio revisable y validada. Los
pendientes de integración y aprobación impiden presentarla como página terminada
o lista para publicación.
