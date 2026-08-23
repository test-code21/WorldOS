# Frontend Information Architecture

The frontend should make provenance and longitudinal observation intuitive rather than decorating the backend.

## Primary navigation by the mature decade

### Dashboard
- overall source count;
- recent observations;
- recent new versions;
- failing/stale sources;
- coverage snapshot;
- scheduler health.

### Catalog
- configured sources;
- filters by jurisdiction/source class/status;
- import/export;
- source enable/disable;
- preservation mode visibility.

### Source Detail
- canonical identity;
- configured URL;
- source class/jurisdiction metadata;
- latest observation;
- latest successful version;
- preservation mode;
- health history;
- observation timeline.

### Timeline
- successful unchanged observations;
- new-version observations;
- failures;
- redirects;
- gaps where no observation occurred.

### Version Viewer
- preserved artifact metadata;
- normalized/extracted representation where available;
- segments;
- direct provenance breadcrumb;
- compare-to-previous action.

### Diff Viewer
- mechanical added/removed text;
- no interpretive labels.

### Search / Library
- query;
- source/jurisdiction/time/source-class filters;
- historical/current toggle;
- provenance-first result cards;
- jump to exact segment.

### Coverage
- target jurisdiction list;
- source counts by class;
- health/freshness;
- explicit gaps.

### Commons
- community bundle preview/import/export;
- origin metadata;
- conflict resolution.

### API Explorer
- base URL;
- auth guidance;
- OpenAPI-linked examples;
- live read-only calls where safe.

### System Health / Settings
- database/storage connectivity;
- worker/scheduler status;
- failed jobs;
- backup status hooks;
- version/migration information;
- API key administration.

## Design principle

A user should always be able to answer:

> Where did this text come from, when did WorldOS observe it, and what version am I looking at?
