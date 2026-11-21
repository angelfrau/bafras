"""Activos de imagen: contrato del manifiesto existente y resolución a un recurso publicable en preview.

Fuente única: media-library/manifests/media-manifest.yaml (no se duplica). Este módulo no lee
archivos: la existencia e integridad física las comprueba la aplicación con el resultado.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator, model_validator

AssetId = Annotated[str, StringConstraints(pattern=r"^[A-Z][0-9]{2}$")]
_DIMENSIONS = re.compile(r"^(\d+)x(\d+)$")


class MediaError(ValueError):
    """Un activo no puede usarse; `problems` explica cada motivo."""

    def __init__(self, problems: list[str]) -> None:
        super().__init__("\n".join(problems))
        self.problems = problems


class MediaAsset(BaseModel):
    """Campos del manifiesto que usa WEB. El resto del registro (procedencia, original) se ignora aquí."""

    model_config = ConfigDict(extra="ignore", frozen=True)

    id: AssetId
    status: Literal["READY", "PENDING_LICENSE", "PENDING_ORIGINAL", "NEEDS_CREATION", "NOT_FOUND"]
    relative_path: str
    alt_es: str | None = None
    alt_ca: str | None = None
    alt_en: str | None = None
    alt_de: str | None = None
    output_dimensions: str | None = None
    output_size_bytes: int | None = None
    license: str | None = None
    license_url: str | None = None
    author: str | None = None
    source_url: str | None = None
    source_provider: str | None = None
    original_dimensions: str | None = None
    attribution_required: bool | None = None
    attribution_text: str | None = None  # registro completo de gestión (attribution.md); no es texto de interfaz
    publication_authorization: Literal["pending", "declared_by_bafras"] = "pending"
    authorization_ref: str | None = None
    output_sha256: Annotated[str, StringConstraints(pattern=r"^[a-f0-9]{64}$")] | None = None

    @model_validator(mode="after")
    def _authorization_trace(self) -> MediaAsset:
        if self.publication_authorization == "declared_by_bafras" and not self.authorization_ref:
            raise ValueError("la autorización declarada requiere referencia documental")
        return self

    @field_validator("relative_path")
    @classmethod
    def _safe_path(cls, value: str) -> str:
        parts = value.split("/")
        if not value.startswith("assets/images/") or "\\" in value or any(p in ("", ".", "..") for p in parts):
            raise ValueError(f"ruta de activo no segura: {value!r}")
        return value


class MediaManifest(BaseModel):
    model_config = ConfigDict(extra="ignore", frozen=True)

    assets: list[MediaAsset] = Field(min_length=1)

    @model_validator(mode="after")
    def _unique(self) -> MediaManifest:
        ids = [asset.id for asset in self.assets]
        if len(ids) != len(set(ids)):
            raise ValueError("identificadores de activo duplicados en el manifiesto")
        return self

    def get(self, asset_id: str) -> MediaAsset:
        for asset in self.assets:
            if asset.id == asset_id:
                return asset
        raise MediaError([f"{asset_id}: activo inexistente en el manifiesto"])


def media_publication_blockers(asset: MediaAsset) -> list[str]:
    """La declaración del titular se registra separada de la licencia de origen."""
    if asset.publication_authorization != "declared_by_bafras":
        return [f"imagen {asset.id}: autorización de publicación pendiente"]
    return []


@dataclass(frozen=True)
class ImageCredit:
    """Crédito visible exigido por la licencia (CC BY / BY-SA): autor, fuente y licencia enlazadas, y si se adaptó.

    WEB-EXPERIENCE-04: sustituye al volcado de `attribution_text` bajo la imagen. Ese texto es un registro de gestión
    (nombre de archivo, URL, transformaciones, en español) y sigue completo en el manifiesto y en attribution.md.
    La palabra «adaptada» es texto de interfaz por idioma (CommonContent `image-adapted`), no un dato de MEDIA.
    """

    author: str
    source_provider: str | None
    source_url: str | None
    license: str
    license_url: str | None
    adapted: bool


@dataclass(frozen=True)
class ResolvedImage:
    """Imagen lista para presentación. `rights` distingue lo declarado de lo verificado."""

    asset_id: str
    source_path: str  # relativa a la raíz del proyecto; también ruta bajo la raíz de salida
    url: str
    width: int
    height: int
    size_bytes: int
    alt: str
    credit: ImageCredit | None  # solo si la licencia exige atribución
    license: str | None
    rights: Literal["declared"]


def resolve_image(asset: MediaAsset, locale: str) -> ResolvedImage:
    """Activo READY con dimensiones, tamaño y texto alternativo en el idioma pedido; sin inferencias."""
    problems = []
    if asset.status != "READY":
        problems.append(f"{asset.id}: estado {asset.status}, no utilizable")
    # Descripción intrínseca por idioma (alt_<idioma>); sin fallback a otro idioma.
    alt = getattr(asset, f"alt_{locale}", None) if locale in ("es", "ca", "en", "de") else None
    if not alt:
        problems.append(f"{asset.id}: sin texto alternativo para {locale!r}")
    match = _DIMENSIONS.match(asset.output_dimensions or "")
    if match is None:
        problems.append(f"{asset.id}: dimensiones de salida ausentes o mal formadas")
    if asset.output_size_bytes is None:
        problems.append(f"{asset.id}: tamaño de salida ausente (necesario para verificar el archivo)")
    if asset.attribution_required and not asset.attribution_text:
        problems.append(f"{asset.id}: atribución obligatoria sin texto en el manifiesto")
    if asset.attribution_required and not (asset.author and asset.license):
        problems.append(f"{asset.id}: atribución obligatoria sin autor o licencia en el manifiesto")
    if problems:
        raise MediaError(problems)
    credit = None
    if asset.attribution_required:
        # Adaptación = el derivado no conserva las dimensiones del original (recorte/redimensionado registrados).
        adapted = bool(asset.original_dimensions) and asset.original_dimensions != asset.output_dimensions
        credit = ImageCredit(author=asset.author, source_provider=asset.source_provider, source_url=asset.source_url,
                             license=asset.license, license_url=asset.license_url, adapted=adapted)
    return ResolvedImage(
        asset_id=asset.id, source_path=asset.relative_path, url="/" + asset.relative_path,
        width=int(match.group(1)), height=int(match.group(2)), size_bytes=asset.output_size_bytes,
        alt=alt, credit=credit, license=asset.license, rights="declared",
    )
