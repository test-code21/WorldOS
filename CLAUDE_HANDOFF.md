# Coding-Agent Handoff

## Mission

Implement WorldOS from the public repository using this package as the working architecture bridge and the bundled canonical documents as ultimate doctrine.

## Before touching code

1. Inspect the existing repository structure and stack. Do not overwrite established choices without need.
2. Read `START_HERE.md`.
3. Read `architecture/SYSTEM_BOUNDARY.md`.
4. Read `architecture/CORE_DOMAIN_MODEL.md`.
5. Read the current sprint file.
6. For Sprint 001, also read `plans/SPRINT_001_BUILD_PLAN.md`.

## Prime directive

> WorldOS records what a source communicates and preserves enough context to let another system reason about it later.

## Five questions before adding a feature

1. Is this describing source material/context or interpreting the world?
2. Is this public-source infrastructure, or am I rebuilding SourceLedger?
3. Would it make sense in a generic deployment that knows nothing about AiBC or the creator?
4. Can every derived output be traced back to preserved input and processing lineage?
5. Does this preserve self-hosting portability?

## Do not introduce without explicit architecture change

- multi-tenant workspace architecture;
- `tenant_id` in core domain records;
- private Drive/Dropbox/SharePoint governance;
- per-source organizational ACLs;
- source trust/reliability/ideology scoring;
- autonomous source discovery;
- entity-resolution knowledge graph;
- multilingual semantic interpretation;
- country models or field-intelligence objects;
- hidden dependencies on private services.

## Definition of a completed sprint

A sprint is not complete because code compiles. It must include:

- working capability;
- automated tests for stated invariants;
- migrations if data structures changed;
- operator/user docs;
- a reproducible demo;
- frontend treatment for user-visible capability;
- health/diagnostics where relevant;
- updated API/schema docs;
- no unexplained deviation from current doctrine.

## Preferred implementation direction

Unless the existing repository already establishes a compatible stack:

- backend: Python + FastAPI;
- frontend: Next.js/React;
- database: PostgreSQL;
- artifact storage: backend abstraction with local filesystem and GCS-capable implementation;
- API: OpenAPI-first `/v1` contract when Sprint 006 is reached;
- local deployment: Docker Compose;
- reference cloud: GCP.

These are replaceable implementation choices. The architectural invariants are not.
