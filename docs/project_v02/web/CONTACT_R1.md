# CONTACT-R1 · Contacto definitivo de Release 1.0

Decisión autorizada por el responsable BAFRAS en WEB-V03 R2, §7; 07/11/2026.

Release 1.0 utiliza exclusivamente correo electrónico y teléfono como canales directos.
No hay formulario, backend ni proveedor de formularios pendiente para esta versión.
`config/site.yaml` sigue siendo la autoridad de los datos: `info@bafras.com`,
`+34 610 903 179` y su representación E.164 validada. No se duplican en plantillas.

Esta decisión posterior sustituye únicamente el alcance funcional de formulario de D03 CO-02,
D04 §13 y D05 §47 para la página española. D03 conserva la autoridad del texto reutilizado,
D04 las fronteras y D05 los tokens y patrones. No modifica el resto de sus especificaciones
ni declara superados sus gates. La comprobación operativa del correo y teléfono sigue pendiente
para publicación. No implica envío de mensajes de prueba ni contratación de servicios.

Intervención editorial explícita, limitada a `content/es/pages/contacto.yaml`:

- CO-01, CO-03 y CO-04 conservan títulos y párrafos.
- CO-02 pasa de `form` a `text`, mantiene «Envíanos tu consulta.» y convierte la ayuda aprobada
  del mensaje en un párrafo `consultation-guidance`, sin reescribirla.
- Se retiran campos, obligatoriedad, etiqueta del botón y mensajes de envío, pertenecientes a la
  funcionalidad eliminada. El pendiente `sections/co-02/privacy_text` deja de tener objeto y se retira;
  los requisitos legales generales del sitio siguen vigentes.
- CO-03 mantiene las etiquetas y destinos tipados `ContactLink`; el dato visible procede de configuración,
  por lo que se eliminan los valores duplicados del YAML español.
- La referencia editorial incorpora `CONTACT-R1 / WEB-V03 R2`; revisión `draft` sin cambios.

Se conservan nueve páginas y 51 secciones. El sitio español utiliza 15 combinaciones kind/purpose.
El modelo editorial `ContactFormSection` permanece porque los borradores CA/EN/DE y las pruebas del
contrato histórico lo utilizan; el pipeline español no contiene ni omite artificialmente una sección form.
No existe un componente de envío en la presentación activa.

CA/EN/DE no se modifican: Contacto y su pendiente de privacidad conservan el contrato anterior y requieren
una adaptación editorial revisada antes de publicarse. Los tests comparan íntegramente las otras páginas
y delimitan expresamente esta diferencia autorizada; no se aplica fallback ni conversión durante la carga.

La composición española reutiliza secciones de texto y una variante `direct_contact` con canales destacados
en dos columnas en escritorio y orden vertical en móvil. Se retiran los estilos y la plantilla exclusivos
del formulario, sin cambios visuales intencionados en las otras ocho páginas.
