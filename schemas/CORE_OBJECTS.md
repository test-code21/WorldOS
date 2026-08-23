# Core Object Shapes — Directional, Not Yet Migration Code

These shapes document semantics before ORM details.

## Source

```json
{
  "source_id": "src_...",
  "name": "Example Ministry Notices",
  "canonical_url": "https://example.gov/notices",
  "source_class": "government_notice",
  "jurisdiction_ref": "...",
  "adapter": "html",
  "preservation_mode": "extracted_text",
  "enabled": true,
  "created_at": "..."
}
```

## SourceObservation

```json
{
  "observation_id": "obs_...",
  "source_id": "src_...",
  "attempted_at": "...",
  "completed_at": "...",
  "retrieval_status": "success",
  "http_status": 200,
  "resolved_url": "...",
  "raw_hash": "sha256:...",
  "text_hash": "sha256:...",
  "source_version_id": "ver_..."
}
```

## SourceVersion

```json
{
  "source_version_id": "ver_...",
  "source_id": "src_...",
  "first_observed_at": "...",
  "raw_hash": "sha256:...",
  "text_hash": "sha256:...",
  "raw_artifact_id": "art_...",
  "text_artifact_id": "art_..."
}
```

## Segment

```json
{
  "segment_id": "seg_...",
  "source_version_id": "ver_...",
  "sequence": 14,
  "segment_type": "paragraph",
  "locator": {"kind": "dom_path", "value": "main>section[2]>p[3]"},
  "text": "...",
  "process_run_id": "run_..."
}
```

## Rule

IDs should be opaque/stable enough that external clients do not infer database internals from them.
