# Sprint 005 — The Library

## Story

WorldOS has memory, history, and addressable documents. Sprint 005 makes the accumulated public record **findable**.

## Immediate user value

A human or machine can search across configured public sources and inspect every hit in its original provenance context.

## Capability added

```text
query
  ↓
index
  ↓
Segment hits
  ↓
SourceVersion + Source context
```

## Implementation scope

### Search
- segment full-text index;
- title/source/publisher-like identity filters where captured;
- jurisdiction filter;
- source-class filter;
- observation/publication-time filters where available;
- historical/current-version filter;
- language field filter when source-declared or mechanically detected.

### Mechanical metadata
Optional, lineage-preserved fields such as:
- headings;
- extracted date strings;
- numeric strings;
- detected language;
- links.

### Ranking
Ranking should optimize textual/retrieval relevance without hidden source-trust weighting.

### Frontend
- search box;
- filters;
- provenance-first result cards;
- jump to exact segment;
- show historical-version status prominently.

## Demo story

Search a corpus containing multiple versions and multiple jurisdictions. Open a result and land on the exact preserved segment in the exact historical version.

## Acceptance gates

- [ ] Every result resolves to source/version/segment lineage.
- [ ] Historical search is possible.
- [ ] Search does not silently collapse all history to latest.
- [ ] Ranking contains no hidden trustworthiness preference.
- [ ] Index can be rebuilt from canonical records without losing provenance.

## Non-goals

No web discovery, semantic world model, cross-language interpretation, or final analytical answer generation.

## Why Sprint 006 depends on this

The connector should expose a useful, settled retrieval surface rather than freezing an API around immature internals.
