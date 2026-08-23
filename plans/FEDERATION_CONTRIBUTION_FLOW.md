# Federation Contribution Flow

## Bundle producer

- exports selected catalog entries;
- includes bundle/schema version;
- includes origin identity;
- includes adapter requirements;
- includes optional latest hashes/health metadata;
- includes explicit redistributability flags for any content artifacts;
- signs/checksums bundle when supported.

## Bundle consumer

- validates bundle;
- previews source additions/changes;
- sees origin metadata;
- resolves conflicts;
- chooses what to import;
- observes imported sources locally.

## Principle

Federation should transfer **capability to observe**, not force trust in another instance's interpretation.
