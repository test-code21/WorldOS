# Test Strategy

## Test layers

### Unit tests
- hashing/canonicalization functions;
- manifest validation;
- adapter behavior with fixtures;
- preservation policy decisions;
- diff/segmentation pure functions.

### Integration tests
- DB constraints/migrations;
- artifact store + DB lineage;
- observation/version deduplication;
- scheduler retry behavior;
- API resource provenance.

### End-to-end tests
- clean deployment;
- add source;
- observe;
- view timeline;
- search;
- use `/v1` from a separate client;
- import community bundle;
- upgrade and restore.

### Golden-source fixtures
Maintain stable local fixtures that simulate:
- unchanged HTML;
- changed HTML;
- redirects;
- 404/410;
- timeout;
- malformed HTML;
- dynamic noise;
- multiple languages without requiring semantic interpretation.

## Regression priority

Any bug that could silently:
- collapse two different versions;
- invent a version without a successful observation;
- detach a segment from provenance;
- delete history during migration;
should receive a permanent regression test.
