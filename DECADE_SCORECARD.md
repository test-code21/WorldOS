# Decade Scorecard

Use this to judge whether each sprint has actually crossed a capability threshold.

| Sprint | Capability question | Pass condition |
|---|---|---|
| 001 | Can WorldOS prove what it observed? | Durable Source → Observation → Version → Artifact lineage survives restart and repeat observations. |
| 002 | Can an operator change the source set without code changes? | Validated manifests round-trip import/export and normal additions require no deploy. |
| 003 | Can WorldOS distinguish unchanged, changed, failed, and never-checked states? | Timeline and scheduler preserve all four without overwriting history. |
| 004 | Can a consumer point to a precise part of a precise version? | Stable segment locators and reproducible segmentation exist. |
| 005 | Can a user find material without losing provenance? | Every result resolves directly to source/version/segment context. |
| 006 | Can unrelated software consume WorldOS? | Separate client uses only base URL + auth + `/v1` contract. |
| 007 | Can we see global coverage and gaps honestly? | Every target jurisdiction has explicit coverage status and health visibility. |
| 008 | Can two instances help each other without merging? | One exports a reviewed bundle; another selectively imports and observes independently. |
| 009 | Can an unfamiliar operator deploy and integrate it? | Clean-room deployment + external site integration passes documented smoke tests. |
| 010 | Is WorldOS useful before analysis, and composable after it? | 1.0 core stands alone; downstream demo uses only public API and visibly begins outside WorldOS. |
