# WorldOS — Architecture Doctrine

## 1. Product position

WorldOS is a generic open-source public-information capability.

For AiBC, it should also be architected as a reusable GCP-native capability/plugin that can be deployed into or alongside a client's SourceLedger foundation.

This should be considered a broader AiBC pattern:

> **Build generic capability once, then deploy it into governed client infrastructure.**

## 2. Separation of responsibilities

### WorldOS
Publicly available external information.

### SourceLedger
Governed private/client sources, permissions, provenance, source grants, organizational context.

### IntelOS
Retrieval/orchestration across available intelligence systems.

### ModelOS
Selection and execution of model-based analytical runs.

The systems should compose rather than duplicate one another.

## 3. Canonical flow

```text
PUBLIC TEXTUAL SOURCE
        ↓
DISCOVERY / INPUT
        ↓
CAPTURE
        ↓
SOURCE PRESERVATION
        ↓
NORMALIZATION
        ↓
STRUCTURING / INDEXING
        ↓
PROVENANCE-PRESERVED WORLDOS RECORD
        ↓
API / QUERY SURFACE
        ↓
INTEL OS / OTHER CONSUMER
        ↓
MODEL OS / ANALYSIS IF DESIRED
```

WorldOS ends before the final analytical judgment.

## 4. Public core

The open-source core should contain everything necessary to perform WorldOS's essential function.

Likely responsibilities include:

- source intake;
- fetch/capture;
- textual preservation;
- document versioning;
- metadata extraction;
- segmentation;
- normalization;
- indexing;
- entity/place references where technically useful;
- provenance/lineage;
- query APIs;
- export;
- operational health;
- tests and evaluations.

## 5. GCP reference architecture

AiBC's official hosted/reference deployment should be Google Cloud-native where practical.

Potential services include:

- **Cloud Run** — application and ingestion services;
- **Cloud SQL / PostgreSQL** — canonical structured records;
- **Cloud Storage** — preserved source content;
- **IAM** — service identity;
- **Secret Manager** — credentials;
- **Pub/Sub / Tasks / Scheduler** — asynchronous and recurring collection where justified;
- **Vertex AI / Gemini** — optional language-model-assisted extraction or normalization.

The public code should remain modular enough to run locally or be adapted to other environments where reasonable.

## 6. Model use inside WorldOS

Language models may assist WorldOS with transformations that make information machine-readable.

Their outputs must remain derived artifacts with lineage to the source.

A model assisting with:

- segmentation;
- metadata extraction;
- entity candidate extraction;
- schema normalization;
- language translation for indexing;
- structured representations;

does not thereby grant WorldOS authority to publish broad judgments about the underlying subject.

## 7. SourceLedger deployment

In a client environment:

```text
CLIENT GCP
   │
   ├── SOURCELEDGER
   │      ├── identity
   │      ├── permissions
   │      ├── private sources
   │      └── governed context
   │
   └── WORLDOS
          ├── public information substrate
          └── public-world retrieval
```

Authorized applications can then reason across both public and private material without forcing either system to abandon its jurisdiction.

## 8. Genericity test

Before merging a core feature, ask:

> **Would this make sense for any recognized country, region, or public source without knowing anything about the original creator's personal interests?**

If not, it likely belongs in a downstream application rather than WorldOS core.
