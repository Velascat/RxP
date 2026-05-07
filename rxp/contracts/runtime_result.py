# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Velascat
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from rxp.contracts.artifact_descriptor import ArtifactDescriptor
from rxp.vocabulary.runtime_kind import RUNTIME_KINDS
from rxp.vocabulary.runtime_status import RUNTIME_STATUSES


class RuntimeResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["0.1"] = "0.1"
    contract_kind: Literal["runtime_result"] = "runtime_result"
    invocation_id: str = Field(min_length=1)
    runtime_name: str = Field(min_length=1)
    runtime_kind: Literal[*RUNTIME_KINDS]
    status: Literal[*RUNTIME_STATUSES]
    exit_code: int | None = None
    started_at: str
    finished_at: str
    stdout_path: str | None = None
    stderr_path: str | None = None
    artifacts: list[ArtifactDescriptor] = Field(default_factory=list)
    error_summary: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)
