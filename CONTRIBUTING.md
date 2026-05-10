# Contributing to RxP

RxP is the **Runtime eXecution Protocol** — a contract-only specification for how a runtime is invoked and what runtime result came back. It is the runtime-side counterpart to CxRP (which describes *what should happen and how it routes*).

## Before You Start

- Check open issues to avoid duplicate work
- For any contract change (new field, enum value, schema revision), open an issue first to discuss the impact on downstream consumers
- All contributions must pass the test suite before merging

## Development Setup

```bash
git clone https://github.com/ProtocolWarden/RxP.git
cd RxP
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Requires `python3 >= 3.11`.

## Running Tests

```bash
PYTHONPATH=. .venv/bin/python -m pytest tests/ -v
```

## Project Structure

```
rxp/contracts/      # Python contract models (RuntimeInvocation, RuntimeResult, ArtifactDescriptor)
rxp/vocabulary/     # canonical enums (runtime_status, runtime_kind)
rxp/validation/     # schema loading and validation helpers
rxp/schemas/v0.1/   # JSON Schemas (active)
examples/v0.1/      # minimal interoperable example payloads
docs/spec/          # versioned normative summaries
tests/              # contract + schema validation tests
```

## What Belongs Here

RxP is the **contract layer only**. It must not contain:

- Subprocess execution or runner logic (belongs in ExecutorRuntime)
- Source/fork resolution (belongs in SourceRegistry)
- Routing or lane-selection logic (belongs in SwitchBoard)
- Planning, scheduling, watchers, or queue systems
- Model/provider integrations or adapter implementations

If a feature requires reaching outside contract definitions and validation, it belongs in another repo.

## CxRP vs RxP Boundary

```text
CxRP = what should happen and how it routes through the system
RxP  = how a runtime is invoked and what runtime result came back
```

OperationsCenter typically maps a CxRP `ExecutionRequest` to an RxP `RuntimeInvocation`. Keep the boundary clean: don't add CxRP-shaped fields (lane, policy, contract refs) into RxP types.

## Versioning

- New optional fields or enum values within the current `vX.Y` are additive
- Breaking changes ship as a new `schemas/vX.Y+1/` directory; the previous version is frozen
- Vocabulary enum changes (`runtime_status`, `runtime_kind`) require an issue discussion before opening a PR

## Pull Request Checklist

- [ ] Tests pass (`pytest -v`)
- [ ] Schemas updated under `schemas/vX.Y/` (if contract changed)
- [ ] Examples updated under `examples/vX.Y/` (if contract changed)
- [ ] Spec updated in `docs/spec/` (if normative behavior changed)
- [ ] Downstream impact noted (ExecutorRuntime, OperationsCenter)

## Code Style

- Type hints required on public functions
- Prefer dataclasses or frozen dataclasses for contract types
- No `from foo import *`
- Docstrings on public types; comments only when the *why* is non-obvious
