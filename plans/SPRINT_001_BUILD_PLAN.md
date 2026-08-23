# Sprint 001 Build Plan — The First Memory

This is the implementation starting line.

## Objective

From a clean deployment, an operator can configure one public URL or supplied public text, observe it, preserve the selected representation, inspect the resulting Source/Observation/Version/Artifact records in the UI, restart the stack, and retrieve the same record. Repeating the same observation creates a new Observation but not a duplicate Version.

## Workstream A — Repository reconnaissance

Before coding:

- identify existing backend/frontend languages and frameworks;
- identify current database/migration tooling;
- identify current deployment files;
- identify lint/test/CI conventions;
- document what is retained vs changed.

**Do not replace the stack merely because this roadmap lists preferences.**

## Workstream B — Domain model

Implement minimal records:

### Source
Required semantics:
- stable ID;
- canonical URL or supplied-text identity;
- name;
- adapter type;
- preservation mode;
- enabled;
- timestamps.

### SourceObservation
Required semantics:
- one row per attempt;
- attempted/completed times;
- outcome/status;
- resolved location;
- response status where applicable;
- hashes when content exists;
- optional pointer to SourceVersion;
- error information that is useful but does not leak secrets.

### SourceVersion
Required semantics:
- source-scoped uniqueness by documented content identity;
- first-observed time;
- preserved artifact pointer(s);
- immutable historical meaning after creation.

### StoredArtifact
Required semantics:
- storage backend;
- opaque storage key;
- media type;
- byte size where known;
- hash;
- preservation mode/context.

## Workstream C — Capture pipeline

Implement a narrow adapter interface, even if only two adapters exist:

```text
HtmlUrlAdapter
SuppliedTextAdapter
```

Suggested pipeline:

```text
request observation
   ↓
create Observation(attempted)
   ↓
adapter retrieves material
   ↓
policy chooses artifacts to preserve
   ↓
compute hashes
   ↓
look up existing SourceVersion for same Source/content identity
   ↓
create Version + Artifact(s) only if new
   ↓
attach Observation to Version
   ↓
mark Observation complete
```

Failure path:

```text
create Observation
   ↓
fetch/parser/storage failure
   ↓
record failed outcome
   ↓
no phantom SourceVersion
```

## Workstream D — Storage abstraction

Create an interface with no GCP concepts in domain records.

Minimum backend:
- local filesystem.

Preferred additional backend in Sprint 001 if straightforward:
- Google Cloud Storage.

The DB stores an artifact key/backend identifier, not a hard-wired public GCS URL.

## Workstream E — Database/migrations

Requirements:
- first migration is deterministic;
- unique constraints enforce version identity;
- foreign keys protect lineage;
- deletion behavior does not cascade away historical evidence accidentally;
- timestamps are UTC;
- IDs do not depend on row-number semantics exposed publicly.

## Workstream F — API/internal service

Sprint 001 does **not** freeze `/v1`.

It does need enough endpoints/services for the frontend and tests:
- create/configure Source;
- trigger observation;
- list/get Sources;
- list/get Observations;
- list/get Versions;
- retrieve preserved artifact safely;
- health.

Mark internal/unstable API status clearly until Sprint 006.

## Workstream G — Frontend

Build the beginning of the real interface, not a throwaway admin page.

### Sources page
- source name;
- URL/identity;
- preservation mode;
- latest observation status;
- latest version time;
- observe-now action.

### Source detail
- identity/configuration;
- observation history;
- versions;
- latest artifact metadata.

### Observation detail
- attempted/completed;
- status;
- resolved URL;
- hashes;
- matching/new version link;
- error detail when failed.

### Version detail
- first observed;
- hashes;
- artifact metadata;
- preserved text preview where policy allows.

## Workstream H — Reliability

Tests must cover:

1. first successful observation creates Version;
2. identical second observation creates Observation but reuses Version;
3. changed content creates a second Version;
4. failed request creates failed Observation and no Version;
5. DB restart preserves records;
6. app restart preserves records;
7. artifact retrieval survives restart;
8. duplicate/retried completion does not create duplicate Version;
9. storage failure is visible;
10. dangerous/unapproved URL schemes are rejected.

## Workstream I — Local deployment

A fresh clone should have one documented path:

```text
copy env example
start services
run migrations automatically or via one documented command
open UI
add source
observe source
```

Avoid a README requiring ten undocumented manual fixes.

## Workstream J — Documentation

Ship:
- architecture diagram;
- object semantics;
- environment variable reference;
- preservation-mode explanation;
- local setup;
- first observation tutorial;
- troubleshooting.

## Demo script

1. Start clean WorldOS.
2. Add a controlled public/test source.
3. Trigger observation.
4. Open the Observation and Version in UI.
5. Restart the stack.
6. Show the same records/artifact.
7. Trigger again unchanged.
8. Show Observation 2 → Version 1.
9. Change controlled content.
10. Trigger again.
11. Show Observation 3 → Version 2.

## Exit gates

Sprint 001 is complete only when:

- [ ] Source/Observation/Version/Artifact semantics are documented.
- [ ] Observation and Version are distinct in schema and UI.
- [ ] repeat observations are idempotent with respect to version creation.
- [ ] failures are preserved as failures.
- [ ] preserved artifacts survive restart.
- [ ] local deployment works from a clean clone.
- [ ] there is no tenant/workspace layer.
- [ ] there is no source-trust interpretation.
- [ ] tests prove the invariants.
- [ ] the frontend tells the same provenance story as the database.

## What Sprint 001 intentionally leaves ugly/unfinished

- no segmentation;
- no full search;
- no global catalog;
- no scheduler beyond manual/limited triggering if desired;
- no stable external `/v1` contract;
- no federation;
- no intelligence.

The sprint is successful because its tiny capability is *dependable*.
