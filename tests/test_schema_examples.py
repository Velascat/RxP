import json
from pathlib import Path

from rxp.validation.json_schema import validate_payload


def test_all_examples_validate() -> None:
    for path in Path("examples/v0.1").glob("*.json"):
        payload = json.loads(path.read_text())
        validate_payload(payload)
