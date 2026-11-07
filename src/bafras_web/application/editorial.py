"""Load all documents of one locale; WEB configuration remains authoritative."""

from pydantic import TypeAdapter, ValidationError

from bafras_web.adapters import yaml_files
from bafras_web.adapters.editorial_files import discover_editorial_sources, editorial_path_for_reading
from bafras_web.adapters.filesystem import ProjectPaths
from bafras_web.adapters.yaml_files import YamlFileError
from bafras_web.editorial.entities import DownloadableResource, Experience, Person, Sector
from bafras_web.editorial.inspection import (
    CATALOG_FILES, CompletenessPolicy, DiagnosticCode, DocumentKind, DocumentValue,
    EditorialDiagnostic, EditorialDocument, EditorialInspection,
)
from bafras_web.editorial.integrity import assess_integrity
from bafras_web.editorial.pages import CommonContent, PageContent
from bafras_web.editorial.primitives import EditorialModel, PublicText

from .configuration import load_site_routing


class EditorialLoadRequest(EditorialModel):
    locale: PublicText
    policy: CompletenessPolicy


def inspect_editorial(paths: ProjectPaths, request: EditorialLoadRequest) -> EditorialInspection:
    routing = load_site_routing(paths)  # Preserve ConfigurationError, not an empty registry.
    if request.locale not in routing.locales.codes:
        return EditorialInspection(locale=request.locale, policy=request.policy, expected_page_ids=(), documents=(), diagnostics=(
            EditorialDiagnostic(code="LOCALE_UNKNOWN", severity="error", message="Idioma no configurado"),
        ))
    locale = request.locale
    expected = tuple(sorted(routing.routes.pages))
    specs: dict[str, tuple[DocumentKind, str]] = {
        f"{locale}/pages/{pid}.yaml": ("page", f"page/{pid}") for pid in expected
    }
    specs.update({f"{locale}/{file}": (kind, "common" if kind == "common" else f"catalog/{kind}") for kind, file in CATALOG_FILES.items()})
    documents: dict[str, EditorialDocument] = {
        source: EditorialDocument(document_id=id, kind=kind, source=source, required=kind == "page", state="ABSENT")
        for source, (kind, id) in specs.items()
    }
    diagnostics: list[EditorialDiagnostic] = []
    for discovered in discover_editorial_sources(paths.content, locale, tuple(specs)):
        kind, id = specs.get(discovered.source, ("unexpected", f"unexpected/{discovered.source}"))
        source = discovered.source

        def diagnostic(code: DiagnosticCode, message: str, selector: str | None = None) -> None:
            diagnostics.append(EditorialDiagnostic(code=code, severity="error", message=message,
                                                   document_id=id, source=source, selector=selector))

        if kind == "unexpected" and discovered.error and not source.lower().endswith((".yaml", ".yml")):
            # A directory access failure is not an extra editorial document.
            diagnostics.append(EditorialDiagnostic(code="DOCUMENT_READ_ERROR", severity="error",
                message="No se pudo examinar el directorio editorial", source=source))
            continue
        documents[source] = EditorialDocument(document_id=id, kind=kind, source=source, required=kind == "page", state="INVALID")
        if kind == "unexpected":
            diagnostic("DOCUMENT_UNEXPECTED", "Origen fuera del contrato editorial")
            if discovered.error:
                diagnostic("DOCUMENT_READ_ERROR", "Error de acceso o contención durante descubrimiento")
            continue
        if discovered.error:
            diagnostic("DOCUMENT_READ_ERROR", "Origen no legible, no regular o fuera del idioma permitido")
            continue
        try:
            path = editorial_path_for_reading(paths.content, locale, discovered)
        except (OSError, RuntimeError):
            diagnostic("DOCUMENT_READ_ERROR", "El origen no pudo leerse tras el descubrimiento")
            continue
        try:
            raw = yaml_files.load_yaml(path)
        except YamlFileError as error:
            code = "DOCUMENT_READ_ERROR" if isinstance(error.__context__, OSError) else "YAML_ERROR"
            diagnostic(code, "Error de lectura o sintaxis YAML")
            continue
        except UnicodeError:
            diagnostic("YAML_ERROR", "Entrada YAML no interpretable")
            continue
        except TypeError as error:
            # The existing loader's duplicate-key set can see unhashable YAML
            # keys. Other TypeErrors are programming errors, not content errors.
            if error.args not in tuple((f"unhashable type: '{kind}'",) for kind in ("list", "dict", "set")):
                raise
            diagnostic("YAML_ERROR", "Clave YAML no interpretable")
            continue
        except OSError:
            diagnostic("DOCUMENT_READ_ERROR", "No se pudo leer el documento editorial")
            continue
        if (kind in ("page", "common") and not isinstance(raw, dict)) or (kind not in ("page", "common") and not isinstance(raw, list)):
            diagnostic("DOCUMENT_ROOT_INVALID", "Raíz YAML incompatible con el contrato documental")
            continue
        if kind == "page":
            if "locale" in raw and raw["locale"] != locale:
                diagnostic("DOCUMENT_LOCALE_MISMATCH", "El idioma declarado no coincide con el contexto", "locale")
                continue
            if "page_id" in raw and raw["page_id"] != id.removeprefix("page/"):
                diagnostic("DOCUMENT_ID_MISMATCH", "La página declarada no coincide con el archivo esperado", "page_id")
                continue
        try:
            value: DocumentValue
            if kind == "page":
                value = PageContent.model_validate({**raw, "locale": locale})
            elif kind == "common":
                value = CommonContent.model_validate(raw)
            else:
                adapter = {
                    "people": TypeAdapter(list[Person]), "sectors": TypeAdapter(list[Sector]),
                    "experiences": TypeAdapter(list[Experience]), "resources": TypeAdapter(list[DownloadableResource]),
                }[kind]
                value = tuple(adapter.validate_python(raw, strict=True))
            documents[source] = EditorialDocument(document_id=id, kind=kind, source=source, required=kind == "page", state="VALID", value=value)
        except ValidationError as error:
            for issue in error.errors(include_input=False, include_context=False):
                code = "DUPLICATE_ENTITY_ID" if issue["type"] == "duplicate_entity_id" else "DOCUMENT_INVALID"
                # Keep locations, not input values, OS paths or exception reprs.
                selector = ".".join("".join(c if c.isalnum() or c in "_-" else "~" for c in str(part)) for part in issue["loc"])
                diagnostic(code, "Documento incompatible con su modelo tipado", selector)
    report = assess_integrity(tuple(documents.values()), expected)
    finalized = tuple(EditorialDocument(
        document_id=d.document_id, kind=d.kind, source=d.source,
        required=d.kind == "page" or d.kind in report.required_catalogs,
        state=d.state, value=d.value,
    ) for d in documents.values())
    for doc in finalized:
        if doc.required and doc.state == "ABSENT":
            diagnostics.append(EditorialDiagnostic(
                code="DOCUMENT_MISSING", severity="error" if request.policy == "COMPLETE" else "warning",
                message="Documento editorial requerido ausente", document_id=doc.document_id, source=doc.source,
            ))
    return EditorialInspection(locale=locale, policy=request.policy, expected_page_ids=expected,
                               documents=finalized, diagnostics=(*diagnostics, *report.diagnostics))
