# Self-Hosting Doctrine

WorldOS should be designed so an unfamiliar operator can run it without becoming a WorldOS developer.

## Product promise

A fresh operator should be able to:

1. clone/download the repository;
2. configure required environment values;
3. start the stack;
4. complete first-run setup;
5. import a source catalog;
6. begin observations;
7. inspect health;
8. back up data;
9. upgrade safely;
10. connect an external client through the public API.

## Core portability

The domain layer should not require GCP-specific concepts.

Reference implementations may include:

- local filesystem object storage;
- Google Cloud Storage;
- PostgreSQL locally or Cloud SQL remotely.

## "Low maintenance" means

- idempotent scheduled work;
- explicit retry/backoff;
- no silent failed jobs;
- visible stale/failing sources;
- safe migrations;
- documented backup/restore;
- health endpoints;
- useful logs;
- one place to inspect operational state;
- predictable upgrade steps.

It does **not** mean promising zero failures. It means failures are contained, visible, recoverable, and documented.

## Hosted reference instance

A future hosted WorldOS should deploy the same canonical code. Hosted convenience may add surrounding infrastructure, but core capabilities should not be withheld from self-hosters.
