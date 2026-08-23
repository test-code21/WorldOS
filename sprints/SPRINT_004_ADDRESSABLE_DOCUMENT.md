# Sprint 004 — The Addressable Document

## Story

A preserved document is still too coarse for reliable machine use. Sprint 004 lets WorldOS point **inside a specific historical version**.

## Immediate user value

A consumer can cite/retrieve "this paragraph from this version of this source" instead of receiving a whole page blob.

## Capability added

```text
SourceVersion
  ├── Segment 1: heading
  ├── Segment 2: paragraph
  ├── Segment 3: list item
  └── Segment 4: table block
```

## Implementation scope

### Process lineage
- `ProcessRun` for segmentation/normalization;
- process name/version/configuration hash;
- reproducible or versioned outputs.

### Segmentation
- headings;
- paragraphs;
- lists;
- sections;
- source-local locators where possible;
- table blocks only where deterministic/reliable;
- extracted links.

### Normalization
- character/encoding normalization;
- whitespace handling;
- preserve original artifact separately;
- normalized text is explicitly derived.

### Frontend
- structured version viewer;
- segment anchors;
- copy segment ID/link;
- provenance breadcrumb;
- toggle original/derived representations where appropriate.

## Demo story

Request Segment 14 from Version X and recover:
- exact text;
- sequence;
- locator;
- segment type;
- source/version identity;
- process run used to create it.

## Acceptance gates

- [ ] Every segment has exactly one parent SourceVersion.
- [ ] Reprocessing never silently mutates historical segment meaning without version/process lineage.
- [ ] Original preserved artifact remains available according to preservation policy.
- [ ] Parser failure does not make SourceVersion disappear.
- [ ] Segment IDs are stable for the produced processing run.

## Non-goals

No entity graph, topic model, translation, summary, contradiction analysis, or opinion classification.

## Why Sprint 005 depends on this

Search should return addressable evidence, not floating snippets detached from a historical source state.
