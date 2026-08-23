# Observability Plan

## Operator needs to know

- Is the application healthy?
- Is PostgreSQL reachable?
- Is artifact storage reachable?
- Is the scheduler/worker alive?
- Which sources are failing?
- Which sources are stale?
- What was the last successful observation?
- Are jobs backing up?
- Did a migration complete?

## Metrics worth exposing

- observations attempted/succeeded/failed;
- new versions created;
- unchanged observations;
- observation latency;
- artifact bytes written;
- per-adapter failure counts;
- stale-source count;
- scheduler queue depth where applicable.

Keep observability about system behavior, not source truth/reliability.
