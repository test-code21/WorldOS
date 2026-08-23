# Sprint 006 — The Connector

## Story

WorldOS becomes infrastructure when software that has never seen its database can use it through one stable contract.

This is the **one generic connector**. IntelOS, a university project, a personal site, or an unknown future consumer should all use the same interface.

## Immediate user value

An operator can give another developer only a base URL and credentials. That developer can query the public-source record without installing or importing WorldOS internals.

## Capability added

```text
Any external app
     ↓ HTTP/OpenAPI
WorldOS /v1
     ↓
public-source records + provenance
```

## Implementation scope

### Stable read/query API
- Sources;
- Observations;
- Versions;
- Segments;
- Search;
- Catalog;
- Coverage;
- Health.

### Contract foundations
- `/v1` namespace;
- OpenAPI spec;
- stable opaque IDs;
- consistent pagination;
- consistent errors;
- UTC timestamps;
- provenance envelopes/links;
- documented rate-limit hooks;
- read-access configuration suitable for self-hosting.

### Thin clients
- Python client;
- TypeScript client;
- clients contain no private endpoints or hidden intelligence.

### Frontend
- API explorer;
- credential setup guidance;
- example requests;
- link from UI resource to corresponding API endpoint.

## Demo story

A separate repository receives only:

```text
WORLDOS_BASE_URL
WORLDOS_API_KEY
```

It searches, opens one Segment, retrieves its SourceVersion and Source, and displays provenance.

## Acceptance gates

- [ ] External consumer imports no backend code.
- [ ] `/v1` contract is documented and tested.
- [ ] Every content response preserves recoverable provenance.
- [ ] Python and TypeScript examples work against a clean instance.
- [ ] No IntelOS-specific logic exists.
- [ ] No MultilingualOS-specific logic exists.
- [ ] API compatibility policy is published.

## Non-goals

No bespoke connector zoo. No separate privileged API for our own intelligence stack.

## Why Sprint 007 depends on this

Once coverage becomes global, external consumers need a stable way to benefit without coupling to catalog internals.
