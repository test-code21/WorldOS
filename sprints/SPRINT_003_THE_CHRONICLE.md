# Sprint 003 — The Chronicle

## Story

WorldOS stops being a collection of snapshots and becomes a **chronicle**.

It repeatedly checks configured sources and catalogs what happened without claiming why it happened.

## Immediate user value

An operator can answer:

- Did we check this source yesterday?
- Was it unchanged?
- When did the content first differ?
- What exact prior version did we preserve?
- Was the source unavailable for a period?

## Capability added

```text
Configured Source
   ↓ schedule
Observation 1 → Version A
Observation 2 → Version A
Observation 3 → failed
Observation 4 → Version B
```

## Implementation scope

### Scheduler
- per-source cadence;
- due-source selection;
- idempotent/retry-aware jobs;
- backoff;
- disabled source behavior;
- manual trigger remains available.

### Version chronology
- first/last observed timestamps;
- latest successful observation;
- latest distinct version;
- observation gaps remain visible.

### Mechanical diffs
- text diff between versions;
- added/removed lines/blocks;
- no semantic labels.

### Frontend
- observation timeline;
- version chronology;
- compare versions;
- failure history;
- stale/never-observed indicators.

### Operations
- worker/scheduler health;
- failure metrics;
- last-run visibility.

## Demo story

Use a controlled source observed four times:

- O1 → A
- O2 → A
- O3 → failed
- O4 → B

The UI must make all four states legible and show a mechanical A↔B diff.

## Acceptance gates

- [ ] "unchanged" and "not checked" are distinguishable.
- [ ] Failures preserve history.
- [ ] Old versions are never overwritten.
- [ ] Duplicate job delivery does not multiply versions.
- [ ] Source disappearance does not delete prior material.
- [ ] Diff is mechanical and provenance-linked.
- [ ] Core never labels a change correction, contradiction, deception, or improvement.

## Non-goals

No interpretation of why content changed; no claim that latest equals correct.

## Why Sprint 004 depends on this

Once history exists, document structure must attach to a precise version rather than to a mutable "current page."
