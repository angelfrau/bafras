"""Real A5 representation gaps; additive contracts preserve A1 consumers."""

import pytest

from bafras_web.editorial.pages import PageContent
from bafras_web.editorial.pending import resolve_pending_selector, validate_pending_fields
from bafras_web.editorial.sections import ContactChannel, FormField


def test_approved_contact_data_is_bound_to_its_channel():
    channel = ContactChannel.model_validate({
        "id": "email", "label": "Correo electrónico", "value": "info@bafras.com",
        "target": {"kind": "contact", "channel": "email"},
    })
    assert channel.value == "info@bafras.com" and channel.target.channel == "email"
    assert ContactChannel(id="phone", label="Teléfono", target={"kind": "contact", "channel": "phone"}).value is None


def test_approved_form_optionality_is_editorial_data():
    assert FormField.model_validate({"id": "company", "label": "Empresa u organización", "required": False}).required is False
    assert FormField.model_validate({"id": "name", "label": "Nombre *", "required": True}).required is True
    assert FormField(id="legacy", label="Campo anterior").required is None


@pytest.mark.parametrize("section,field,status", [
    ({"id": "co-02", "kind": "form", "title": "Envíanos tu consulta.", "fields": [{"id": "name", "label": "Nombre *"}],
      "submit_label": "Enviar consulta.", "messages": {"success": "Enviado", "error": "Error"}}, "privacy_text", "none"),
    ({"id": "pe-02", "kind": "experience_index", "title": "Referencias",
      "groups": [{"id": "infrastructure", "title": "Infraestructuras e instalaciones"}]}, "groups", "collection"),
])
def test_missing_approved_content_has_an_explicit_pending_target(section, field, status):
    selector = f"sections/{section['id']}/{field}"
    page = PageContent.model_validate({
        "page_id": "contacto" if field == "privacy_text" else "proyectos_experiencia", "locale": "es",
        "review": {"status": "draft"}, "seo": {},
        "sections": [{"id": "hero", "kind": "hero", "title": "Cabecera"}, section],
        "pending": [{"field": selector, "reason_code": "source_missing"}],
    })
    assert resolve_pending_selector(page, selector).status == status
    assert validate_pending_fields(page) == []
    assert resolve_pending_selector(page, f"sections/hero/{field}").status == "field_not_allowed"
