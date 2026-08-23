# Sprint 001 — The First Memory

## Story

WorldOS becomes real when it can make one narrow statement reliably:

> At this time, WorldOS attempted to observe this configured public source; this is what it successfully preserved, and this is the distinct source version that observation corresponds to.

The feature looks small because the visible action is "fetch a page." The actual product is **durable provenance**.

## Immediate user value

An operator gets a trustworthy memory of a public source instead of a browser bookmark. They can revisit exactly what their WorldOS instance observed even after restart, and repeated checks do not confuse "looked again" with "content changed."

## Capability added

```text
Source
  ↓
SourceObservation
  ↓
SourceVersion
  ↓
StoredArtifact
```

## Implementation scope

### Backend/domain
- Source, SourceObservation, SourceVersion, StoredArtifact;
- URL and supplied-text capture paths;
- content hashing;
- source-scoped version deduplication;
- explicit preservation mode;
- local artifact store abstraction;
- database migrations;
- health endpoint.

### Frontend
- Sources list;
- add/configure source;
- observe-now action;
- Source detail;
- Observation detail;
- Version detail;
- preserved-text preview where permitted.

### Operations
- local Docker/reference start path;
- environment template;
- durable PostgreSQL volume;
- durable artifact volume;
- visible failures.

## Key invariant

Five checks of unchanged content create five Observations and one SourceVersion.

## Demo story

1. Add one controlled public/test URL.
2. Observe it.
3. Restart WorldOS.
4. Open the preserved record.
5. Observe again unchanged.
6. Show Observation 2 pointing to the same Version.
7. Change the test source.
8. Observe again.
9. Show Version 2 while Version 1 remains intact.

## Acceptance gates

- [ ] Successful observation persists across restart.
- [ ] Same source/content does not create duplicate SourceVersions.
- [ ] Repeated checks remain individually recorded.
- [ ] Changed content creates a new immutable historical version.
- [ ] Failed retrieval creates a failed Observation and no phantom Version.
- [ ] Storage backend does not leak cloud-specific semantics into domain records.
- [ ] Preservation mode is explicit.
- [ ] Fresh clone can run from documentation.
- [ ] No tenant/workspace layer exists.
- [ ] No interpretive source labels exist.

## Non-goals

No segmentation, search, scheduler fleet, source discovery, translation, entity resolution, trust scoring, or stable external connector yet.

## Why Sprint 002 depends on this

A source registry is meaningless until a configured source can be observed and remembered correctly.

## Detailed execution

See `plans/SPRINT_001_BUILD_PLAN.md`.
