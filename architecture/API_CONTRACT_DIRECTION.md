# API Contract Direction — One Generic Connector

WorldOS should expose one stable contract rather than building bespoke integrations for every consumer.

## Principle

An external consumer should need only:

```text
WORLDOS_BASE_URL
WORLDOS_API_KEY (when required)
```

It should not import backend internals.

## Initial `/v1` read/query resources

```text
GET /v1/sources
GET /v1/sources/{source_id}
GET /v1/sources/{source_id}/observations
GET /v1/sources/{source_id}/versions
GET /v1/observations/{observation_id}
GET /v1/versions/{version_id}
GET /v1/versions/{version_id}/segments
GET /v1/segments/{segment_id}
GET /v1/search?q=...
GET /v1/catalog
GET /v1/coverage
GET /v1/health
```

## Mutation/admin surface

Administrative writes may exist, but keep them logically distinct from the stable generic read/query connector. Mutation auth should never force tenant semantics into core records.

## Response rule

Any endpoint returning content should include or link to enough identity to recover:

```text
Source
→ SourceObservation/SourceVersion
→ StoredArtifact/Segment
→ ProcessRun where derived
```

## Versioning promise

Once `/v1` is declared stable:
- additive changes are preferred;
- breaking changes require a new major namespace or explicit compatibility strategy;
- clients should not rely on undocumented fields;
- pagination/error envelopes should be consistent.

## Client packages

Provide thin clients that merely encode the public HTTP contract:
- Python;
- TypeScript.

They should not contain hidden intelligence or privileged endpoints.
