# Sprint 008 — The Commons

## Story

WorldOS becomes more useful when communities can share the work of finding and maintaining public source definitions without being forced into one central corpus.

Federation starts as **shared observation knowledge**, not a distributed database.

## Immediate user value

An operator can import a reviewed source bundle created by another community, compare it with their local catalog, select what they want, and then observe those sources locally.

## Capability added

```text
Instance A
  ↓ export safe bundle
Community artifact
  ↓ preview/validate/select
Instance B
  ↓ observe independently
Local corpus B
```

## Implementation scope

### Community bundle
- bundle/schema version;
- origin metadata;
- source manifests;
- adapter declarations;
- coverage metadata;
- optional latest hashes/observation timestamps;
- redistributability flags;
- checksum/signature support where useful.

### Import safety
- dry-run validation;
- origin display;
- conflict detection;
- selective import;
- local override behavior;
- no auto-enable unless operator chooses policy.

### Frontend
- Commons/bundles screen;
- bundle preview;
- differences/conflicts;
- source selection;
- origin/provenance display.

## Demo story

Instance A exports a country/source-class bundle. Instance B imports only selected definitions and then captures the sources itself. No source content needs to be replicated between them.

## Acceptance gates

- [ ] No mandatory corpus replication.
- [ ] Imported records retain bundle origin metadata.
- [ ] Operator approves what enters local catalog.
- [ ] Redistributable content is explicitly distinguished from metadata/manifests.
- [ ] Federation transfers no analytical judgments.
- [ ] Instances remain fully functional if the other disappears.

## Non-goals

No consensus network, peer-to-peer global query engine, blockchain, or universal shared state.

## Why Sprint 009 depends on this

The strongest proof of an open-source commons is that truly independent installations can operate and still benefit from shared artifacts.
