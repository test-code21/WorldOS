# Build Order and Dependency Rules

## Hard dependencies

```text
001 First Memory
  ↓
002 Registry
  ↓
003 Chronicle
  ↓
004 Addressable Document
  ↓
005 Library
  ↓
006 Connector
  ↓
007 World Shelf
  ↓
008 Commons
  ↓
009 Bring Your Own WorldOS
  ↓
010 Beyond the Boundary
```

## Allowed overlap

Some work can begin early without violating the sequence:

- frontend design system can start during Sprint 001;
- source research for Sprint 007 can happen in parallel, but catalog completion should not drive core schema prematurely;
- API shape sketches can begin before Sprint 006, but `/v1` stability must not be promised before internal objects settle;
- deployment automation can improve throughout the decade, while Sprint 009 is the clean-room proof;
- federation ideas can be documented early, but exchange formats should not freeze before Sprint 002/006 semantics stabilize.

## Rule for pulling future work forward

A future-sprint feature may be implemented early only if it:

1. is required by an earlier invariant;
2. does not prematurely freeze unstable semantics;
3. does not expand WorldOS jurisdiction;
4. is covered by tests and documentation;
5. does not add hidden dependencies on AiBC systems.
