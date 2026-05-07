# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Velascat
import json
from pathlib import Path
from typing import Any

from jsonschema import ValidationError, validate

from rxp.vocabulary.contract_kind import CONTRACT_KINDS

_ROOT = Path(__file__).resolve().parents[2]
_SUPPORTED_SCHEMA_VERSIONS = {"0.1"}


def schema_path_for(contract_kind: str, schema_version: str = "0.1") -> Path:
    if contract_kind not in CONTRACT_KINDS:
        raise ValidationError(f"Unsupported contract kind: {contract_kind}")
    if schema_version not in _SUPPORTED_SCHEMA_VERSIONS:
        raise ValidationError(f"Unsupported schema version: {schema_version}")

    path = _ROOT / "schemas" / f"v{schema_version}" / f"{contract_kind}.schema.json"
    if not path.exists():
        raise ValidationError(
            f"Schema file not found for {contract_kind} v{schema_version}: {path}"
        )
    return path


def validate_payload(payload: dict[str, Any]) -> None:
    contract_kind = payload.get("contract_kind")
    schema_version = payload.get("schema_version", "0.1")

    schema_file = schema_path_for(contract_kind=contract_kind, schema_version=schema_version)
    schema = json.loads(schema_file.read_text())
    validate(instance=payload, schema=schema)
