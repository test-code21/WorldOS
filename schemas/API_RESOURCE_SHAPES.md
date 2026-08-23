# API Resource Shape Rules

## Provenance envelope

Content-bearing API responses should expose a compact provenance chain.

```json
{
  "data": {"...": "..."},
  "provenance": {
    "source_id": "src_...",
    "source_version_id": "ver_...",
    "segment_id": "seg_...",
    "observed_at": "...",
    "source_url": "https://..."
  }
}
```

Not every endpoint needs every field, but clients must be able to recover the chain without scraping UI URLs.

## Pagination

Use one consistent strategy across list/search endpoints. Cursor pagination is preferred if ordering/history semantics make offset pagination unstable.

## Errors

Return a consistent machine-readable envelope:

```json
{
  "error": {
    "code": "source_not_found",
    "message": "...",
    "request_id": "..."
  }
}
```

## Time

Return UTC ISO-8601 timestamps and document this globally.

## Content

Do not return a derived translation/summary in a field whose name implies original source text.
