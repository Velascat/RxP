# RxP — Runtime eXecution Protocol

RxP is the **Runtime eXecution Protocol**. It defines normalized contracts for runtime invocation
and runtime results produced by execution systems.

## What RxP is not

RxP is not:

- CxRP
- OperationsCenter
- SwitchBoard
- SourceRegistry
- ExecutorRuntime
- a scheduler
- a runner
- a subprocess library
- a package manager
- an agent framework

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
ExecutorRuntime consumes RxP RuntimeInvocation.
ExecutorRuntime produces RxP RuntimeResult.
OperationsCenter maps RxP RuntimeResult back to CxRP ExecutionResult.
