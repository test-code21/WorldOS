# Sprint 007 — The World Shelf

## Story

The machinery has earned enough stability that the project can invest heavily in **what sources are configured**.

WorldOS earns its name through transparent breadth, not through autonomous crawling.

## Immediate user value

A fresh reference installation can begin with a serious, reviewable public-source catalog instead of an empty database, while operators can still replace or extend that catalog.

## Capability added

```text
Global reference catalog
  ↓
Coverage manifest
  ↓
WorldOS Registry
  ↓
Chronicle + Library + API
```

## Implementation scope

### Reference catalog
Build curated source bundles spanning a UN-member-state baseline and useful public source classes.

Possible source classes include:
- government portals;
- legislation/regulation repositories;
- public notices;
- statistical agencies;
- central banks/public economic institutions;
- major public institutions;
- open-data portals;
- official press/publication feeds.

The exact source-class baseline should be documented and may vary where institutions differ.

### Coverage instrumentation
For every target jurisdiction show:
- configured sources;
- source classes represented;
- declared languages;
- latest successful observation;
- failing/stale sources;
- known gaps.

### Contribution tooling
- manifest CI validation;
- adapter smoke tests;
- duplicate checking;
- contribution template;
- reviewer guidance.

### Frontend
- global coverage dashboard;
- filterable jurisdiction list;
- explicit zero/partial coverage states;
- drill-down into source health.

## Demo story

Open the coverage screen and choose several very different jurisdictions. Show what WorldOS is configured to observe, what is healthy, what is missing, and when each source was last successfully seen.

## Acceptance gates

- [ ] Every target UN member state has explicit coverage status.
- [ ] Missing/weak coverage is visible.
- [ ] Catalog additions still use generic manifest mechanisms.
- [ ] No autonomous discovery is required.
- [ ] No country receives privileged schema treatment.
- [ ] Coverage metrics measure collection, not truth/quality of a society.

## Non-goals

No claim of exhaustive national representation; no random-web crawling; no preferred-media/trust ranking.

## Why Sprint 008 depends on this

Once source curation becomes labor-intensive and global, community collaboration becomes materially valuable.
