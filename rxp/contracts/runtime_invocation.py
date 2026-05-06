from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from rxp.vocabulary.runtime_kind import RUNTIME_KINDS


class RuntimeInvocation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["0.1"] = "0.1"
    contract_kind: Literal["runtime_invocation"] = "runtime_invocation"
    invocation_id: str = Field(min_length=1)
    runtime_name: str = Field(min_length=1)
    runtime_kind: Literal[*RUNTIME_KINDS]
    working_directory: str = Field(min_length=1)
    command: list[str] = Field(min_length=1)
    environment: dict[str, str] = Field(default_factory=dict)
    timeout_seconds: int | None = Field(default=None, gt=0)
    input_payload_path: str | None = None
    output_result_path: str | None = None
    artifact_directory: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)
