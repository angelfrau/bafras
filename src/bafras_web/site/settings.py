"""Datos públicos de contacto del sitio (D04 §13), validados desde config/site.yaml."""

from __future__ import annotations

import re
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, StringConstraints, model_validator


class SiteContact(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    email: Annotated[str, StringConstraints(pattern=r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$")]
    phone_display: Annotated[str, StringConstraints(pattern=r"^\+[0-9 ]+$")]
    phone_e164: Annotated[str, StringConstraints(pattern=r"^\+[1-9][0-9]{6,14}$")]

    @model_validator(mode="after")
    def _phone_consistent(self) -> SiteContact:
        if re.sub(r"\s", "", self.phone_display) != self.phone_e164:
            raise ValueError("phone_display y phone_e164 no corresponden al mismo número")
        return self


class SiteSettings(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    schema_version: Literal[1]
    contact: SiteContact
