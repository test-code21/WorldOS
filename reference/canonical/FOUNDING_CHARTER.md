# WorldOS — Founding Charter

## 1. Purpose

WorldOS is a generic open-source system whose purpose is to make the world's publicly available information machine-readable while preserving enough source context for other systems to reason over it later.

Its founding sentence is:

> **WorldOS records what a source communicates and preserves enough context to let another system reason about it later.**

WorldOS does not exist to publish a preferred interpretation of the world.

It exists to create a durable, structured, provenance-preserving public-information substrate.

## 2. Global by construction

WorldOS has no preferred country.

No country is a reference country in the core architecture.

No region, government, culture, language, publisher, media institution, or political perspective is privileged by the founding design.

Country-specific applications may be built on top of WorldOS, but they are consumers of the generic system rather than defining examples embedded into the core.

## 3. Public first

The canonical WorldOS implementation is public and generic from the beginning.

AiBC should not first build a private proprietary WorldOS and later publish a reduced community edition.

The open implementation is the real implementation.

Private, customer-specific, or commercial deployments may later be created from the same generic core.

## 4. What WorldOS preserves

WorldOS should preserve, where available:

- the source;
- source location/URL;
- retrieval time;
- publication time when available;
- publisher or originating institution when available;
- author/speaker when available;
- language;
- textual content;
- source-local context;
- stable identifiers;
- revisions or observed source versions;
- machine-readable structural metadata derived from the source.

The system should retain the ability to connect structured records back to the source material from which they originated.

## 5. What WorldOS does not publish

WorldOS is not founded to publish:

- country goodness/badness scores;
- government trustworthiness rankings;
- media trust scores;
- political ideology scores;
- truth scores;
- cultural judgments;
- safety verdicts;
- geopolitical recommendations;
- preferred narratives;
- or final beliefs about contested events.

Those are possible outputs of downstream analytical systems, and responsibility for them belongs to those systems and their operators.

## 6. Open public machinery

A central WorldOS principle is:

> **We keep the private world private.**
>
> **We build the public-world machinery in public.**

WorldOS is an appropriate first open-source AiBC product precisely because its domain is the public information environment.

## 7. Relationship to intelligence

WorldOS is infrastructure for intelligence, not the final intelligence.

A downstream stack may look like:

```text
PUBLIC WORLD
    ↓
WORLDOS
    ↓
INTEL OS
    ↓
MODEL OS / MODEL RUN
    ↓
ANALYSIS FOR A SPECIFIC PURPOSE
```

WorldOS makes information available.

Other systems decide what question to ask of it and how to interpret the returned material.

## 8. Long-term direction

WorldOS begins with text.

It may eventually incorporate additional public modalities and data types when they become useful.

The founding architecture should not assume that today's textual interface is the final boundary of the project.

But new modalities must earn their complexity.

The first mission is simple:

> **Make public text machine-readable without destroying provenance.**
