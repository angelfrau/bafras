"""El paquete se usa instalado, no por estar la raíz del repositorio en sys.path."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from importlib.metadata import distribution, entry_points, requires
from pathlib import Path

import bafras_web
from bafras_web.adapters.filesystem import templates_dir

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_distribution_metadata():
    dist = distribution("bafras-web")
    assert dist.version == bafras_web.__version__
    runtime = {req.split(">")[0].split("<")[0].split("=")[0].strip().lower() for req in requires("bafras-web") if "extra ==" not in req}
    assert runtime == {"pydantic", "pyyaml", "jinja2"}


def test_package_is_imported_from_src_layout():
    assert Path(bafras_web.__file__).resolve().parent == REPO_ROOT / "src" / "bafras_web"


def test_import_works_only_through_installation(tmp_path):
    """En modo aislado (-I: sin directorio actual ni PYTHONPATH) solo queda site-packages."""
    probe = "import bafras_web, sys; print(bafras_web.__file__); print(sys.path[0])"
    result = _run_outside_repo([sys.executable, "-I", "-X", "utf8", "-c", probe], tmp_path)
    assert result.returncode == 0, result.stderr
    module_file, first_path = result.stdout.splitlines()
    assert Path(module_file).resolve() == REPO_ROOT / "src" / "bafras_web" / "__init__.py"
    assert Path(first_path).resolve() != REPO_ROOT


def test_runtime_dependencies_import():
    import jinja2
    import pydantic
    import yaml

    assert pydantic.VERSION.startswith("2.")
    assert jinja2.__version__ and yaml.__version__


def test_console_script_entry_point():
    (script,) = [ep for ep in entry_points(group="console_scripts") if ep.name == "bafras-web"]
    assert script.value == "bafras_web.cli:main"


def test_templates_are_package_data():
    assert templates_dir().is_dir()


def _run_outside_repo(args: list[str], tmp_path: Path) -> subprocess.CompletedProcess[str]:
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(args, cwd=tmp_path, env=env, capture_output=True, text=True, encoding="utf-8", check=False)


def test_console_script_runs_from_another_directory(tmp_path):
    exe = shutil.which("bafras-web", path=str(Path(sys.executable).parent))
    assert exe, "bafras-web no está instalado en el entorno de este intérprete"
    result = _run_outside_repo([exe, "--version"], tmp_path)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == f"bafras-web {bafras_web.__version__}"


def test_module_execution_and_doctor_from_another_directory(tmp_path):
    result = _run_outside_repo([sys.executable, "-I", "-X", "utf8", "-m", "bafras_web", "doctor", "--project", str(REPO_ROOT)], tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Resultado: correcto" in result.stdout


def test_redirected_output_is_utf8(tmp_path):
    """Sin -X utf8 ni PYTHONIOENCODING: el CLI garantiza UTF-8 al redirigir la salida."""
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "PYTHONIOENCODING", "PYTHONUTF8")}
    result = subprocess.run(
        [sys.executable, "-I", "-m", "bafras_web", "doctor", "--project", str(REPO_ROOT)],
        cwd=tmp_path, env=env, capture_output=True, check=False,
    )
    assert result.returncode == 0
    assert "configuración".encode("utf-8") in result.stdout
