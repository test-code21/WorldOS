# Migration Policy

WorldOS's value grows with history, so schema migrations must treat old observations as valuable evidence.

## Rules

- migrations are version-controlled;
- no destructive migration without explicit backup/rollback plan;
- provenance IDs should remain stable across upgrades;
- stored artifacts should not be renamed/rekeyed casually;
- data backfills must be distinguishable from original observation times;
- derived data may be regenerated if process/version lineage makes that explicit;
- source observations and source versions should not be recomputed from scratch in ways that falsify historical timing.

## Upgrade test

Each sprint should include an upgrade test from the previous released schema, not only a clean-install test.
