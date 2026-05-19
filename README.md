# RxP — Runtime eXecution Protocol

RxP is the **Runtime eXecution Protocol**. It defines normalized contracts for runtime invocation
and runtime results produced by execution systems.

## What RxP is

- `RuntimeInvocation` — normalized request shape for execution systems
- `RuntimeResult` — normalized response shape (status, exit code, artifacts)
- `ArtifactDescriptor` — typed descriptor for files produced during execution
- `runtime_kind` and `runtime_status` vocabularies
- JSON Schemas for cross-language validation
- Example payloads for interoperable integration

## What RxP is not

RxP is not:

- CxRP
- OperationsCenter
- SwitchBoard
- SourceRegistry
- CoreRunner
- a scheduler
- a runner
- a subprocess library
- a package manager
- an agent framework

## Quick start

```bash
pip install -e .
```

```python
from rxp import RuntimeInvocation, RuntimeResult
inv = RuntimeInvocation(runtime_kind="subprocess", argv=["echo", "hello"])
# Hand the invocation to CoreRunner; receive a RuntimeResult.
```

JSON Schemas live under `rxp/schemas/` for non-Python consumers.

## Architecture

RxP is a contract layer — three Pydantic models (`RuntimeInvocation`, `RuntimeResult`, `ArtifactDescriptor`) plus their `runtime_kind` / `runtime_status` enum vocabularies and JSON Schemas. CoreRunner consumes the contract; CxRP describes work routing *to* a runtime, RxP describes the request/response *with* the runtime. See **CxRP vs RxP** below for the split, **v0.1 scope** for what's frozen, and **Example lifecycle** for an end-to-end walkthrough.

## CxRP vs RxP

```text
CxRP = what should happen and how it routes through the system
RxP  = how a runtime is invoked and what runtime result came back
```

## v0.1 scope

- runtime invocation
- runtime result
- artifact descriptor
- runtime status vocabulary
- runtime kind vocabulary
- JSON Schema validation
- examples

## Example lifecycle

OperationsCenter maps CxRP ExecutionRequest to RxP RuntimeInvocation.
CoreRunner consumes RxP RuntimeInvocation.
CoreRunner produces RxP RuntimeResult.
OperationsCenter maps RxP RuntimeResult back to CxRP ExecutionResult.
