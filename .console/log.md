# Log

_Chronological continuity log. Decisions, stop points, what changed and why._
_Not a task tracker — that's backlog.md. Keep entries concise and dated._

## Recent Decisions

_Log significant choices here so they survive context resets._

| Decision | Rationale | Date |
|----------|-----------|------|
| [what was decided] | [why] | [date] |

## Stop Points

_Where did you leave off? What should be verified next session?_

- [what to pick up next]

## Notes

_Free-form scratch. Clear periodically — old entries can be deleted once no longer relevant._

---

- DC4 README sections (2026-05-08, on `fix/dc4-readme-sections`): Custodian DC4 (native) flagged the README missing both Quick start and Architecture H2s. Quick start gives pip install + RuntimeInvocation example; Architecture frames RxP as a contract layer (three Pydantic models + vocabularies + schemas) consumed by ExecutorRuntime, distinguishes from CxRP, and points at the existing CxRP vs RxP / v0.1 scope / Example lifecycle sections.

## 2026-05-08 — M1: CHANGELOG.md stub (Keep-a-Changelog format)

Added a minimal CHANGELOG.md so M1 (and M5 format check) pass.

## 2026-05-08 — CI regression guard

Added .github/workflows/custodian-audit.yml + .hooks/pre-push.
Both run `custodian-multi --fail-on-findings`. CI is the source of
truth; pre-push catches regressions before they hit GitHub.

