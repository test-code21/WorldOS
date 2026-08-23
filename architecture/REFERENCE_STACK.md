# Reference Stack Direction

These are implementation preferences, not immutable doctrine. Existing repository choices should be inspected before replacing anything.

## Backend

**Python + FastAPI** is preferred because WorldOS is text-heavy, Python has strong parsing/data tooling, and FastAPI naturally exposes OpenAPI.

## Frontend

**Next.js / React** is preferred for a polished operator/research interface and straightforward API consumption.

## Database

**PostgreSQL** is preferred for durable relational provenance, migrations, full-text capability, and broad self-hosting support.

## Artifact storage

Use an abstraction such as:

```text
ArtifactStore
  put(...)
  get(...)
  exists(...)
  delete_if_policy_allows(...)
```

Reference backends:
- local filesystem;
- Google Cloud Storage.

An S3-compatible backend may be added if it remains generic and maintainable.

## Scheduling/background work

Choose the simplest portable mechanism that can provide:
- scheduled observations;
- retries;
- idempotency;
- visibility.

GCP deployments may map this to Cloud Run jobs/Tasks/Scheduler/Pub/Sub where justified, but core semantics should not depend on them.

## Local deployment

Docker Compose should be the primary reference path unless the repository already provides an equally portable alternative.

## GCP deployment

Preferred mapping where practical:
- Cloud Run — web/API/worker services;
- Cloud SQL for PostgreSQL;
- Cloud Storage for artifacts;
- Secret Manager for secrets;
- Scheduler/Tasks/Pub/Sub only when operationally justified.
