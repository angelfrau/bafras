"""B1.1 adds Pydantic contracts and reuses the sole YAML parser."""

import ast
from pathlib import Path

import pytest
from pydantic import BaseModel

import bafras_web
from bafras_web.adapters.editorial_files import EditorialSource
from bafras_web.application.editorial import EditorialLoadRequest
from bafras_web.editorial.inspection import EditorialDiagnostic, EditorialDocument, EditorialInspection, IntegrityResult

PACKAGE = Path(bafras_web.__file__).parent
FILES = ("editorial/inspection.py", "editorial/integrity.py", "adapters/editorial_files.py", "application/editorial.py")


@pytest.mark.parametrize("model", [EditorialDiagnostic, EditorialDocument, EditorialInspection, IntegrityResult, EditorialSource, EditorialLoadRequest])
def test_new_data_contracts_are_pydantic_and_share_configuration(model):
    assert issubclass(model, BaseModel)
    assert model.model_config["strict"] and model.model_config["frozen"]
    assert model.model_config["extra"] == "forbid"


@pytest.mark.parametrize("name", FILES)
def test_no_new_parser_data_containers_or_rendering(name):
    tree = ast.parse((PACKAGE / name).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert not any(alias.name.split(".")[0] in {"yaml", "jinja2", "dataclasses", "attrs", "requests"} for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert (node.module or "").split(".")[0] not in {"yaml", "jinja2", "dataclasses", "attrs", "requests"}
            assert not any(alias.name in {"NamedTuple", "dataclass"} for alias in node.names)
        elif isinstance(node, ast.ClassDef):
            # No plain class is being used to pass untyped data between layers.
            assert any(isinstance(base, ast.Name) and base.id == "EditorialModel" for base in node.bases)
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            assert "03_contenido_editorial" not in node.value


def test_request_rejects_coercions_and_unknown_properties():
    from pydantic import ValidationError

    for data in ({"locale": 1, "policy": "COMPLETE"}, {"locale": "es", "policy": "PREVIEW"},
                 {"locale": "es", "policy": "COMPLETE", "content_root": "/tmp"}):
        with pytest.raises(ValidationError):
            EditorialLoadRequest.model_validate(data)
