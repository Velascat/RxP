## Summary

<!-- One or two sentences describing what this PR does and why. -->

## Changes

<!-- Bullet list of what changed. -->

-

## Contract Impact

<!-- Check all that apply. -->

- [ ] No contract change (refactor, docs, tests, tooling only)
- [ ] Additive within current schema version (new optional field or enum value)
- [ ] Breaking change — introduces new `schemas/vX.Y/` revision
- [ ] Vocabulary change (`runtime_status` or `runtime_kind` enums)
- [ ] Validation helper change

If this is a contract change, list the affected contracts:

- [ ] `RuntimeInvocation`
- [ ] `RuntimeResult`
- [ ] `ArtifactDescriptor`

## Boundary Check

- [ ] No subprocess execution or runner logic introduced (belongs in CoreRunner)
- [ ] No CxRP-shaped fields leaked into RxP types (lane, policy, contract refs stay in CxRP)
- [ ] No source-resolution logic introduced (belongs in SourceRegistry)

## Downstream Consumers

<!-- Note any expected impact on CoreRunner, OperationsCenter, etc. -->

## Testing

- [ ] Tests pass: `PYTHONPATH=. .venv/bin/python -m pytest tests/ -v`
- [ ] Schemas updated under `schemas/vX.Y/` (if contract changed)
- [ ] Examples updated under `examples/vX.Y/` (if contract changed)
- [ ] Spec updated in `docs/spec/` (if normative behavior changed)

## Related Issues

<!-- Closes #N or References #N -->

## Notes for Reviewer

<!-- Anything non-obvious: migration considerations, deferred follow-ups, design trade-offs. -->
