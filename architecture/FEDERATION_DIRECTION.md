# Federation Direction — The Commons Without a Distributed Database

Federation in the first decade should be intentionally modest.

## Goal

Independent WorldOS instances should be able to help one another observe the public world better while remaining operationally independent.

## Safe exchange candidates

- source manifests;
- adapter identifiers/versions;
- schema versions;
- coverage manifests;
- source health/freshness metadata;
- content hashes;
- latest-observed timestamps;
- explicitly redistributable preserved artifacts;
- bundle signatures/checksums;
- origin metadata.

## Not required

- distributed consensus;
- peer-to-peer query routing;
- mandatory corpus replication;
- globally unique belief state;
- shared source trust scores;
- shared interpretations;
- automatic ingestion of unreviewed community content.

## Import flow

```text
Receive bundle
   ↓
Validate schema/checksum
   ↓
Preview origin + changes + conflicts
   ↓
Operator selects entries
   ↓
Import catalog definitions
   ↓
Local WorldOS observes sources independently
```

## Powerful consequence

The community can disagree about politics, importance, or interpretation and still collaborate on the infrastructure needed to preserve public source material.
