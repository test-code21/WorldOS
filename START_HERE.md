# Start Here

WorldOS should be built from the inside out: first establish what can be safely asserted about an observation, then make that observation durable, then make collections of observations useful.

## Three invariants to protect from Sprint 001 onward

### 1. Observation is not interpretation

WorldOS may say:

> This configured source was checked at time T. It returned content whose preserved form has hash H.

WorldOS should not silently transform that into:

> This is true, trustworthy, corrected, deceptive, important, or representative.

### 2. Observation is not version

A source can be checked repeatedly without changing. Therefore:

- `SourceObservation` records **that WorldOS looked**;
- `SourceVersion` records **a distinct observed content state**.

This lets WorldOS distinguish "unchanged" from "not checked."

### 3. Public information substrate is not private knowledge governance

WorldOS must resist feature pressure that recreates SourceLedger. Instance administration is allowed; tenant/workspace governance is not a core concern.

## What not to build early

Do not use early engineering energy on:

- automatic source discovery;
- a world ontology;
- entity resolution;
- multilingual semantic normalization;
- truth or trust scoring;
- topic interpretation;
- country models;
- field observations;
- multi-tenant SaaS architecture;
- custom AiBC-only integrations.

## The shortest accurate description

WorldOS is a self-hostable public-source memory and retrieval system with provenance.
