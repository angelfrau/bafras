"""WEB-V01-B: MEDIA contract, page composition, site contact, CommonContent layout and asset copy."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from bafras_web.adapters.filesystem import ProjectPaths, copy_file_atomically
from bafras_web.application.build import BuildError, BuildRequest, build_page, render_page
from bafras_web.application.configuration import load_media_manifest, load_site_composition, load_site_settings
from bafras_web.media.assets import MediaAsset, MediaError, resolve_image
from bafras_web.site.composition import SiteComposition, media_key
from bafras_web.site.settings import SiteContact

ROOT = Path(__file__).resolve().parents[2]
PATHS = ProjectPaths(ROOT)
PREVIEW = BuildRequest(locale="es", page_id="inicio", mode="preview")


def _asset(**changes):
    data = {"id": "H01", "status": "READY", "relative_path": "assets/images/home/hero/x.webp", "alt_es": "Descripción",
            "output_dimensions": "1920x1080", "output_size_bytes": 10, "license": "CC BY 2.0",
            "attribution_required": True, "attribution_text": "Crédito"}
    return MediaAsset.model_validate({**data, **changes})


# ---------- MEDIA ----------

def test_inicio_assets_resolve_from_the_real_manifest():
    manifest = load_media_manifest(PATHS)
    placed = load_site_composition(PATHS).for_page("inicio").media
    assert sorted(placed.values()) == ["D02", "H01", "H03", "H04", "H05"]
    for asset_id in placed.values():
        image = resolve_image(manifest.get(asset_id), "es")
        assert image.url == "/" + image.source_path and image.alt and image.width > 0 and image.rights == "declared"
        assert (ROOT / image.source_path).stat().st_size == image.size_bytes
        assert (image.credit is None) == (manifest.get(asset_id).attribution_required is False)


def test_public_domain_asset_has_no_mandatory_credit():
    assert resolve_image(load_media_manifest(PATHS).get("H04"), "es").credit is None


def test_unknown_asset_id_fails():
    with pytest.raises(MediaError, match="inexistente"):
        load_media_manifest(PATHS).get("Z99")


@pytest.mark.parametrize("path", ["../secret.webp", "assets/images/../../x.webp", "assets\\images\\x.webp", "/etc/x", "assets/other/x.webp"])
def test_unsafe_asset_paths_are_rejected(path):
    with pytest.raises(ValidationError):
        _asset(relative_path=path)


@pytest.mark.parametrize("changes, message", [
    ({"status": "PENDING_LICENSE"}, "no utilizable"),
    ({"alt_es": None}, "sin texto alternativo"),
    ({"output_dimensions": "grande"}, "dimensiones"),
    ({"output_size_bytes": None}, "tamaño"),
    ({"attribution_text": None}, "atribución obligatoria"),
])
def test_unusable_assets_are_explicit(changes, message):
    with pytest.raises(MediaError, match=message):
        resolve_image(_asset(**changes), "es")


def test_no_alternative_text_is_invented_for_other_locales():
    with pytest.raises(MediaError, match="'ca'"):
        resolve_image(_asset(), "ca")


# ---------- Composición y contacto ----------

def test_composition_is_strict():
    with pytest.raises(ValidationError):
        SiteComposition.model_validate({"schema_version": 1, "pages": {"inicio": {"variants": {"h07": "banda"}}}})
    with pytest.raises(ValidationError):
        SiteComposition.model_validate({"schema_version": 1, "pages": {"inicio": {"media": {"h01": "H01"}}}})
    assert media_key("sections/h02/items/energy/media") == ("h02", "energy")
    assert media_key("sections/h01/media") == ("h01", None)


def test_site_contact_comes_from_config_and_phone_must_match():
    contact = load_site_settings(PATHS).contact
    assert (contact.email, contact.phone_e164) == ("info@bafras.com", "+34610903179")
    with pytest.raises(ValidationError):
        SiteContact(email="info@bafras.com", phone_display="+34 610 903 170", phone_e164="+34610903179")


def test_contact_visible_data_and_links_use_site_configuration(project):
    _edit_yaml(project.site_file, lambda data: data["contact"].update({"email": "consultas@bafras.com"}))
    target = build_page(project, BuildRequest("es", "contacto", "preview"), build_root=project.root / "out")
    source = target.read_text(encoding="utf-8")
    assert source.count('href="mailto:consultas@bafras.com"') == 2  # bloque directo y footer
    assert "info@bafras.com" not in source
    assert not any(tag in source for tag in ("<form", "<fieldset", "<input", "<textarea"))


# ---------- Build sobre una copia del proyecto ----------

@pytest.fixture
def project(tmp_path):
    (tmp_path / "pyproject.toml").write_text("", encoding="utf-8")
    for name in ("config", "content", "assets"):
        shutil.copytree(ROOT / name, tmp_path / name)
    (tmp_path / "media-library" / "manifests").mkdir(parents=True)
    shutil.copyfile(PATHS.media_manifest, tmp_path / "media-library/manifests/media-manifest.yaml")
    return ProjectPaths(tmp_path)


def _edit_yaml(path: Path, change):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    change(data)
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def _problems(project, request=PREVIEW):
    with pytest.raises(BuildError) as info:
        build_page(project, request, build_root=project.root / "out")
    assert not (project.root / "out").exists()  # nada escrito ante un fallo
    return "\n".join(info.value.problems)


def test_placement_must_target_an_empty_media_slot(project):
    _edit_yaml(project.composition_file, lambda d: d["pages"]["inicio"]["media"].update({"sections/h04/media": "H01"}))
    assert "no es un hueco de imagen" in _problems(project)


def test_modified_image_file_is_detected(project):
    image = project.root / "assets/images/home/hero/home-hero-engineering.webp"
    image.write_bytes(image.read_bytes()[:-1])
    assert "no coincide con el tamaño" in _problems(project)


def test_missing_image_file_is_detected(project):
    (project.root / "assets/images/home/hero/home-hero-engineering.webp").unlink()
    assert "sin archivo" in _problems(project)


def test_same_size_image_corruption_is_detected_by_sha256(project):
    image = project.root / "assets/images/home/hero/home-hero-engineering.webp"
    data = image.read_bytes()
    image.write_bytes(bytes([data[0] ^ 1]) + data[1:])
    assert "SHA-256" in _problems(project)


@pytest.mark.parametrize("change, expected", [
    (lambda d: d["pages"]["inicio"]["variants"].update({"absent": "closing_band"}), "sección inexistente"),
    (lambda d: d["pages"]["inicio"]["variants"].update({"h01": "closing_band"}), "incompatible"),
    (lambda d: d["pages"].update({"absent": {}}), "página desconocida"),
])
def test_invalid_composition_fails_before_output(project, change, expected):
    _edit_yaml(project.composition_file, change)
    assert expected in _problems(project)


def test_missing_static_asset_is_detected_before_writing(project):
    (project.root / "assets/js/site.js").unlink()
    assert "recurso inexistente: assets/js/site.js" in _problems(project)


def test_layout_requires_approved_common_content(project):
    (project.content / "es" / "common.yaml").unlink()
    problems = _problems(project)
    assert "falta interface_messages 'skip-link'" in problems and "falta la acción de navegación a 'contacto'" in problems


def test_release_keeps_editorial_blockers_after_dec10_authorization():
    with pytest.raises(BuildError) as info:
        render_page(PATHS, BuildRequest(locale="es", page_id="inicio", mode="release"))
    rights = [p for p in info.value.problems if "derechos sin verificar" in p]
    assert not rights
    assert any("'draft'" in p for p in info.value.problems)
    assert all(manifest_asset.publication_authorization == "declared_by_bafras"
               for manifest_asset in load_media_manifest(PATHS).assets
               if manifest_asset.id in load_site_composition(PATHS).for_page("inicio").media.values())


def test_build_copies_only_used_assets_and_preserves_sources(project):
    sources = {p: p.read_bytes() for p in (project.root / "assets").rglob("*") if p.is_file()}
    target = build_page(project, PREVIEW, build_root=project.root / "out")
    copied = sorted(p.relative_to(project.root / "out" / "preview").as_posix()
                    for p in (project.root / "out" / "preview" / "assets").rglob("*") if p.is_file())
    assert len(copied) == 7 and "assets/css/site.css" in copied and "assets/js/site.js" in copied
    assert all(p.read_bytes() == data for p, data in sources.items())
    assert target.is_file()


def test_copy_does_not_rewrite_identical_targets(tmp_path):
    source, target = tmp_path / "a.bin", tmp_path / "out" / "a.bin"
    source.write_bytes(b"datos")
    copy_file_atomically(source, target)
    os.utime(target, (1, 1))
    copy_file_atomically(source, target)
    assert target.stat().st_mtime == 1 and target.read_bytes() == b"datos"
