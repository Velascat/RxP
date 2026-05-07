# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Velascat
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ArtifactDescriptor(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["0.1"] = "0.1"
    contract_kind: Literal["artifact_descriptor"] = "artifact_descriptor"
    artifact_id: str = Field(min_length=1)
    path: str = Field(min_length=1)
    kind: str = Field(min_length=1)
    description: str = ""
    metadata: dict[str, str] = Field(default_factory=dict)
