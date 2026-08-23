# Sprint 002 — The Registry

## Story

Sprint 001 can remember a source that someone configured manually. Sprint 002 turns source configuration into a **portable public artifact**.

The operator should no longer need to edit application code to tell WorldOS what to observe.

## Immediate user value

A researcher, civic technologist, developer, or institution can maintain a version-controlled list of public sources, move it between WorldOS installations, review changes, and share it with collaborators.

## Capability added

```text
Source Manifest
   ↓ validate
Catalog Import
   ↓
Configured Sources
   ↕
Catalog Export
```

## Implementation scope

### Manifest/schema
- versioned YAML/JSON source-manifest format;
- stable source IDs;
- canonical URL;
- name/source class;
- jurisdiction reference;
- declared languages where known;
- adapter;
- preservation mode;
- cadence suggestion;
- enabled state.

### Import/export
- dry-run validation;
- duplicate detection;
- conflict preview;
- create/update behavior;
- export normalized manifest;
- audit metadata for catalog changes.

### Frontend
- Catalog page;
- import preview;
- validation errors;
- source enable/disable;
- export action;
- source configuration editor constrained by schema.

## Demo story

1. Start a fresh instance.
2. Import one manifest containing sources from multiple jurisdictions.
3. Review validation output.
4. Enable/disable entries.
5. Observe selected sources using Sprint 001 machinery.
6. Export the catalog.
7. Import the exported catalog into another fresh instance.

## Acceptance gates

- [ ] Manifest round-trip is stable.
- [ ] Invalid manifests fail with actionable messages.
- [ ] Normal source additions require no code deploy.
- [ ] Catalog changes preserve origin/audit information.
- [ ] Source metadata does not contain trust or ideology ratings.
- [ ] Unknown future manifest fields fail/round-trip according to documented compatibility policy.

## Non-goals

No global catalog completion, automatic discovery, federation, semantic topic ontology, or popularity ranking.

## Why Sprint 003 depends on this

Longitudinal observation is most useful when the set of watched sources is declarative, reviewable, and schedulable.
