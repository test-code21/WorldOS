# Core Domain Model

The model should stay small enough that provenance is easy to explain.

## 1. Source

Stable identity of a configured public source.

Core concerns:
- canonical location;
- human-readable name;
- source class;
- declared jurisdiction metadata where known;
- configured adapter;
- preservation mode;
- enabled state;
- scheduling policy later.

A Source is not "the truth" and is not an institution rating.

## 2. SourceObservation

One attempt to observe one Source at one moment.

It records operational facts such as:
- attempt time;
- completion time;
- request/result status;
- resolved URL;
- HTTP status where applicable;
- retrieval error category;
- observed hash when content was obtained;
- which SourceVersion it matched/created.

**Invariant:** an observation exists even if no new version exists.

## 3. SourceVersion

A distinct observed content state for a Source.

Typical identity rule:

```text
(source_id, normalized-preservation-hash) → unique SourceVersion
```

The exact hash input must be documented and stable.

## 4. StoredArtifact

Pointer to preserved bytes/text or an external reference, depending on preservation policy.

The domain model must not assume every public URL is legally redistributable.

## 5. Segment

Introduced in Sprint 004. An addressable slice of one SourceVersion.

Examples:
- heading;
- paragraph;
- list item;
- table block;
- section.

A Segment never floats free of its SourceVersion.

## 6. ProcessRun

Introduced when transformations need explicit lineage.

Records:
- process name;
- process version;
- configuration hash;
- input SourceVersion/artifact;
- output set;
- run time/status.

This supports deterministic segmentation and later mechanical metadata without implying analytical authority.

## 7. DerivedField

Optional mechanical structure tied to a ProcessRun and source location.

Examples:
- detected language;
- extracted publication-date string;
- heading level;
- numeric string;
- source link.

Derived fields must never silently replace originals.

## Relationship map

```text
Source
  ├── SourceObservation ───────┐
  │                            │ points to
  └── SourceVersion <──────────┘
         ├── StoredArtifact
         ├── Segment
         └── ProcessRun
                └── DerivedField(s)
```

## Intentionally absent

- Tenant
- Workspace
- Member
- PermissionGrant
- TruthScore
- TrustScore
- Ideology
- Assessment
- WorldModel
- EntityGraph
- Translation
