# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 ProtocolWarden
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from rxp.contracts.artifact_descriptor import ArtifactDescriptor
from rxp.contracts.runtime_invocation import RuntimeInvocation
from rxp.contracts.runtime_result import RuntimeResult
from rxp.validation.json_schema import schema_path_for
from rxp.vocabulary.contract_kind import CONTRACT_KINDS
from rxp.vocabulary.runtime_kind import RUNTIME_KINDS
from rxp.vocabulary.runtime_status import RUNTIME_STATUSES


def test_runtime_status_values_match_schema_enum() -> None:
    schema = json.loads(Path("schemas/v0.1/runtime_result.schema.json").read_text())
    assert tuple(schema["properties"]["status"]["enum"]) == RUNTIME_STATUSES


def test_runtime_kind_values_match_schema_enum() -> None:
    invocation_schema = json.loads(Path("schemas/v0.1/runtime_invocation.schema.json").read_text())
    result_schema = json.loads(Path("schemas/v0.1/runtime_result.schema.json").read_text())
    assert tuple(invocation_schema["properties"]["runtime_kind"]["enum"]) == RUNTIME_KINDS
    assert tuple(result_schema["properties"]["runtime_kind"]["enum"]) == RUNTIME_KINDS


def test_http_async_runtime_kind_accepted() -> None:
    """``http_async`` is a valid runtime_kind for both invocation and result."""
    assert "http_async" in RUNTIME_KINDS
    invocation = RuntimeInvocation(
        invocation_id="inv-1",
        runtime_name="archon-workflow",
        runtime_kind="http_async",
        working_directory="/tmp",
        command=["unused"],
    )
    assert invocation.runtime_kind == "http_async"

    result = RuntimeResult(
        invocation_id="inv-1",
        runtime_name="archon-workflow",
        runtime_kind="http_async",
        status="succeeded",
        started_at="2026-05-07T10:00:00Z",
        finished_at="2026-05-07T10:01:00Z",
    )
    assert result.runtime_kind == "http_async"


def test_contract_kind_values_map_to_schema_files() -> None:
    for contract_kind in CONTRACT_KINDS:
        assert schema_path_for(contract_kind).exists()


def test_typed_model_defaults() -> None:
    invocation = RuntimeInvocation(
        invocation_id="inv-1",
        runtime_name="rt",
        runtime_kind="subprocess",
        working_directory="/tmp",
        command=["echo"],
    )
    assert invocation.schema_version == "0.1"
    assert invocation.environment == {}
    assert invocation.metadata == {}

    result = RuntimeResult(
        invocation_id="inv-1",
        runtime_name="rt",
        runtime_kind="subprocess",
        status="pending",
        started_at="2026-05-06T10:00:00Z",
        finished_at="2026-05-06T10:00:00Z",
    )
    assert result.schema_version == "0.1"
    assert result.metadata == {}
    assert result.artifacts == []

    artifact = ArtifactDescriptor(artifact_id="a1", path="/tmp/a", kind="log")
    assert artifact.description == ""
    assert artifact.metadata == {}


@pytest.mark.parametrize(
    ("field", "value"),
    [("invocation_id", ""), ("runtime_name", "")],
)
def test_rejects_empty_invocation_fields(field: str, value: str) -> None:
    kwargs = {
        "invocation_id": "inv-1",
        "runtime_name": "rt",
        "runtime_kind": "subprocess",
        "working_directory": "/tmp",
        "command": ["echo"],
    }
    kwargs[field] = value
    with pytest.raises(ValidationError):
        RuntimeInvocation(**kwargs)


def test_rejects_empty_artifact_path() -> None:
    with pytest.raises(ValidationError):
        ArtifactDescriptor(artifact_id="a1", path="", kind="log")
