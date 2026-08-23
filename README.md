# WorldOS — The First Decade

**Status:** Implementation roadmap and architectural operating package  
**Purpose:** Turn the WorldOS founding doctrine into ten buildable, demonstrable sprints without allowing the project to drift into SourceLedger, IntelOS, ModelOS, MultilingualOS, or autonomous web discovery.

## Founding sentence

> **WorldOS records what a source communicates and preserves enough context to let another system reason about it later.**

## What this package is

This is not merely a roadmap. It is the working bridge between the canonical WorldOS source documents and implementation.

It contains:

- the ten-sprint narrative;
- explicit system boundaries;
- a core domain model;
- source observation/versioning invariants;
- a self-hosting doctrine;
- a portable reference stack;
- frontend information architecture;
- the generic API/connector contract direction;
- curated-source-catalog rules;
- lightweight federation rules;
- reliability, migration, backup, and upgrade expectations;
- schemas and example manifests;
- acceptance gates for every sprint;
- a detailed Sprint 001 build plan;
- coding-agent handoff instructions;
- canonical source documents bundled for reference.

## The central design decision

WorldOS is intentionally narrower than SourceLedger.

**WorldOS:** public-source observation, preservation, versioning, mechanical structure, retrieval, and a generic API.

**SourceLedger:** private/client sources, identities, permissions, source grants, provider connections, tenant/workspace governance, and organizational context.

Therefore the WorldOS core should not acquire `tenant_id`, private Drive/Dropbox connectors, workspace roles, per-source ACLs, or organizational knowledge semantics.

## The decade in one line each

1. **The First Memory** — observe one public source and preserve what was seen.
2. **The Registry** — define what should be observed declaratively.
3. **The Chronicle** — preserve repeated observations and change over time without interpretation.
4. **The Addressable Document** — make preserved material structurally addressable.
5. **The Library** — make the preserved record searchable with provenance.
6. **The Connector** — expose one stable generic API for any external consumer.
7. **The World Shelf** — curate a serious global reference catalog without autonomous discovery.
8. **The Commons** — let independent WorldOS instances share safe community artifacts.
9. **Bring Your Own WorldOS** — prove third-party self-hosting and site/app integration.
10. **Beyond the Boundary** — stabilize WorldOS and demonstrate intelligence layered *outside* the core.

## Start here

1. Read `START_HERE.md`.
2. Read `architecture/SYSTEM_BOUNDARY.md` and `architecture/CORE_DOMAIN_MODEL.md`.
3. Read `DECADE_MAP.md`.
4. If implementing now, read `plans/SPRINT_001_BUILD_PLAN.md` and `sprints/SPRINT_001_FIRST_MEMORY.md`.
5. Coding agents should also read `CLAUDE_HANDOFF.md`.

## Governing implementation rule

> **Build WorldOS as though `worldos.austincanty.com` will someday be just one ordinary deployment of the public repository.**

The public repository is the product. A hosted reference instance may come later, but it should not become a secret superior fork.
