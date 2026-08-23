# Release Gates

## Every sprint

Before merging the sprint milestone:

- all stated acceptance gates pass;
- migrations are tested from the previous sprint state;
- docs match actual commands;
- demo path is reproducible;
- no critical provenance invariant is weakened;
- frontend surfaces the capability;
- operational failures are visible;
- out-of-scope additions are called out rather than smuggled in.

## Sprint 006 API gate

Do not label `/v1` stable until:
- resource IDs are stable;
- pagination is chosen;
- error envelope is chosen;
- timestamps are normalized;
- provenance response pattern is agreed;
- auth model for self-hosted read access is documented.

## Sprint 009 self-hosting gate

Require a clean-room test performed from documentation by someone/process that did not build the environment.

## Sprint 010 1.0 gate

Require:
- migration history review;
- backup/restore rehearsal;
- API compatibility review;
- provenance validation suite;
- license/source-catalog distribution review;
- security review of fetcher/admin surface;
- complete architecture docs.
