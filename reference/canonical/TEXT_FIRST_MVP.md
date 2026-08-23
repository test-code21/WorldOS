# WorldOS — Text-First MVP

## 1. Wedge

WorldOS begins with **current textual public sources**.

This is intentionally narrow and unusually powerful.

Text is one of humanity's richest information media per bit and is already the dominant representation for:

- government publications;
- laws and regulations;
- public notices;
- company releases;
- journalism;
- research;
- reports;
- event pages;
- institutional websites;
- transcripts;
- blogs;
- and much of the public web.

Modern language models are especially well suited to processing this medium.

WorldOS should exploit that alignment before expanding into more expensive modalities.

## 2. MVP objective

A useful first release should demonstrate:

> **Given a public textual source, WorldOS can preserve it, structure it, retain provenance, make it retrievable, and expose it to downstream systems without pretending to decide what the world means.**

## 3. Minimal object set

### Source
Where material came from.

Possible fields:

- `source_id`
- `canonical_url`
- `retrieved_at`
- `publisher_name` when available
- `author_or_speaker` when available
- `publication_time` when available
- `language`
- `content_type`

### SourceVersion
What WorldOS observed at a specific retrieval point.

- `source_version_id`
- `source_id`
- `retrieved_at`
- `content_hash`
- `raw_content_uri`

### Segment
Addressable portion of preserved source text.

- `segment_id`
- `source_version_id`
- `sequence`
- `text`
- source-local locator where available

### DerivedMetadata
Machine-produced structure used for retrieval.

Examples may include:

- detected language;
- extracted dates;
- named entity candidates;
- geographic references;
- headings;
- numbers;
- document structure.

Every derived field should retain lineage to its source version and, where relevant, the transformation that produced it.

## 4. First capabilities

### Ingest a URL or supplied public text

### Preserve original textual material

### Detect whether the observed source changed

### Segment source content

### Extract basic metadata

### Create machine-readable structured output

### Search/query preserved material

### Return source context alongside results

### Expose an API suitable for IntelOS or other consumers

## 5. What v1 should not attempt

The MVP should not need to:

- rate countries;
- rate governments;
- rank media trustworthiness;
- decide geopolitical disputes;
- classify universal truth;
- produce ideological scores;
- maintain a canonical worldview;
- predict conflicts;
- judge cultures;
- personalize travel decisions;
- ingest every modality;
- or become a general-purpose web search engine.

## 6. Coverage philosophy

The architecture should be globally generic.

Coverage may be uneven during development, but the system itself should not encode that one recognized country is more deserving of representation than another.

As collectors mature, WorldOS can increase the breadth and freshness of public textual coverage.

## 7. Success condition

WorldOS v1 succeeds when another system can ask:

> **Give me the relevant preserved public material about this subject, with enough provenance and context that I can decide how to analyze it.**

And WorldOS can answer without inventing a final judgment.
