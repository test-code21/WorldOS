# Portability Doctrine

## Goal

WorldOS should be deployable outside the creator's infrastructure without architectural surgery.

## Portability requirements

- PostgreSQL schema, not Cloud-SQL-specific domain semantics;
- artifact storage interface, not GCS URIs baked into records;
- scheduler semantics that can map to multiple runtimes;
- standard HTTP API;
- environment-based configuration;
- exportable catalogs;
- documented backup formats;
- no requirement for private AiBC services.

## Reference vs requirement

GCP may be the best documented hosted path while local/self-hosted deployment remains first-class.

## Test

If replacing GCS with local filesystem or an S3-compatible implementation would require changing `SourceVersion` semantics, the abstraction is leaking.
