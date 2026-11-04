from __future__ import annotations

import pytest

from bafras_web.adapters.yaml_files import YamlFileError, load_yaml


def _write(tmp_path, text):
    path = tmp_path / "doc.yaml"
    path.write_text(text, encoding="utf-8")
    return path


def test_loads_mappings_and_sequences(tmp_path):
    data = load_yaml(_write(tmp_path, "a: 1\nb:\n  - x\n  - {c: ''}\n"))
    assert data == {"a": 1, "b": ["x", {"c": ""}]}


def test_rejects_duplicate_keys_with_line(tmp_path):
    with pytest.raises(YamlFileError, match=r"clave duplicada 'es' \(línea 3\)"):
        load_yaml(_write(tmp_path, "pages:\n  es: a\n  es: b\n"))


def test_rejects_duplicate_keys_in_flow_mappings(tmp_path):
    with pytest.raises(YamlFileError, match="clave duplicada"):
        load_yaml(_write(tmp_path, "slugs: {es: a, es: b}\n"))


def test_reports_syntax_errors(tmp_path):
    with pytest.raises(YamlFileError):
        load_yaml(_write(tmp_path, "a: [1, 2\n"))


def test_reports_missing_file(tmp_path):
    with pytest.raises(YamlFileError, match="no se puede leer"):
        load_yaml(tmp_path / "missing.yaml")


def test_does_not_construct_python_objects(tmp_path):
    with pytest.raises(YamlFileError):
        load_yaml(_write(tmp_path, "x: !!python/object/apply:os.system ['echo']\n"))
