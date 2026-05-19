---
name: Feature Request
about: Propose a new field, enum value, contract, or schema revision
labels: enhancement
assignees: ''
---

## Summary

A one-sentence description of the proposal.

## Problem It Solves

What can downstream systems (CoreRunner / OperationsCenter) not currently express or validate?

## Proposed Change

What you want added or changed. Include a sketch:

```json
{
  "schema_version": "0.1",
  "contract_kind": "...",
  "...": "..."
}
```

## Change Class

- [ ] New optional field (additive within current version)
- [ ] New enum value (additive within current version)
- [ ] New contract kind
- [ ] Breaking change — requires new `schemas/vX.Y/`

## Affected Contract

- [ ] `RuntimeInvocation`
- [ ] `RuntimeResult`
- [ ] `ArtifactDescriptor`
- [ ] Vocabulary (`runtime_status` / `runtime_kind`)

## Downstream Consumers

Which systems need this, and how will they use it?

- CoreRunner: 
- OperationsCenter: 

## Alternatives Considered

Other shapes you thought about and why you ruled them out.

## Scope Check

Confirm this belongs in RxP (runtime contract layer) rather than:

- [ ] CoreRunner (subprocess execution mechanics)
- [ ] SourceRegistry (source / fork resolution)
- [ ] OperationsCenter (planning / dispatch / observability)
- [ ] CxRP (request-side contracts: lane, policy, contract refs)

## Additional Context

Prior discussion links, related issues, or use-case background.
