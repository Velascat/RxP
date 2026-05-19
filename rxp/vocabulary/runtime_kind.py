# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 ProtocolWarden
RUNTIME_KINDS = (
    "subprocess",
    "http",
    "http_async",
    "container",
    "manual",
    "unknown",
)
"""Recognized runtime_kind values.

- ``subprocess``: local subprocess (process-group safe).
- ``http``: synchronous HTTP request/response (one round-trip; no polling).
- ``http_async``: async-shaped HTTP — kickoff returns 202 + run_id, runner
  polls a status URL until a terminal status. Sync from the caller's POV.
- ``container``: containerized runtime (placeholder).
- ``manual``: caller-supplied dispatcher (used for out-of-process services
  whose transport CoreRunner does not own).
- ``unknown``: catch-all for anything else.
"""
