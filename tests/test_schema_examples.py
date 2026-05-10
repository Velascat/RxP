# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 ProtocolWarden
import json
from pathlib import Path

from rxp.validation.json_schema import validate_payload


def test_all_examples_validate() -> None:
    paths = list(Path("examples/v0.1").glob("*.json"))
    assert paths, "no example payloads found under examples/v0.1/"
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        validate_payload(payload)
