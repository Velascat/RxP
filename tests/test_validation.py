# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 ProtocolWarden
import json

import pytest
from jsonschema import ValidationError

from rxp.validation.json_schema import validate_payload


def _base_invocation() -> dict:
    return json.loads(
        """{
        \"schema_version\": \"0.1\",
        \"contract_kind\": \"runtime_invocation\",
        \"invocation_id\": \"inv-001\",
        \"runtime_name\": \"runtime\",
        \"runtime_kind\": \"subprocess\",
        \"working_directory\": \"/tmp\",
        \"command\": [\"echo\"],
        \"environment\": {},
        \"timeout_seconds\": 1,
        \"input_payload_path\": null,
        \"output_result_path\": null,
        \"artifact_directory\": null,
        \"metadata\": {}
    }"""
    )


def test_invalid_contract_kind_fails() -> None:
    payload = _base_invocation()
    payload["contract_kind"] = "nope"
    with pytest.raises(ValidationError):
        validate_payload(payload)


def test_invalid_schema_version_fails() -> None:
    payload = _base_invocation()
    payload["schema_version"] = "9.9"
    with pytest.raises(ValidationError):
        validate_payload(payload)


def test_missing_required_field_fails() -> None:
    payload = _base_invocation()
    payload.pop("runtime_name")
    with pytest.raises(ValidationError):
        validate_payload(payload)


def test_invalid_runtime_status_fails() -> None:
    payload = json.loads(open("examples/v0.1/runtime_result.succeeded.json").read())
    payload["status"] = "orchestrating"
    with pytest.raises(ValidationError):
        validate_payload(payload)


def test_invalid_runtime_kind_fails() -> None:
    payload = _base_invocation()
    payload["runtime_kind"] = "archon"
    with pytest.raises(ValidationError):
        validate_payload(payload)


def test_empty_command_fails() -> None:
    payload = _base_invocation()
    payload["command"] = []
    with pytest.raises(ValidationError):
        validate_payload(payload)


def test_non_positive_timeout_fails() -> None:
    payload = _base_invocation()
    payload["timeout_seconds"] = 0
    with pytest.raises(ValidationError):
        validate_payload(payload)
