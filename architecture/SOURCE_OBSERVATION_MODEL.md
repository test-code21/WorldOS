# Source Observation and Versioning Model

This is one of the decade's most important foundations.

## Why Observation is separate from Version

If WorldOS checks a source every day for a month and the source changes twice, there should be roughly thirty observations but only three distinct versions.

Without `SourceObservation`, the system cannot distinguish:

- checked and unchanged;
- not checked;
- checked and failed;
- checked and changed.

That ambiguity becomes unacceptable in a longitudinal record.

## State examples

### Successful, unchanged

```text
Observation O2
  source = S1
  status = success
  hash = H1
  source_version = V1
```

### Successful, changed

```text
Observation O3
  source = S1
  status = success
  hash = H2
  source_version = V2 (new)
```

### Failed

```text
Observation O4
  source = S1
  status = failed
  error = timeout
  source_version = null
```

### Not checked

No observation exists for that period. Do not synthesize an "unchanged" state.

## Version identity

Version identity should be content-derived and source-scoped. Never reuse a SourceVersion from another Source only because hashes match.

## Redirects

Record the configured canonical source separately from the resolved location observed during a request. Redirect history is operational evidence, not a reason to silently rewrite source identity.

## Deletion/removal

A 404/410 or other disappearance should be recorded as an observation outcome. It should not delete historical SourceVersions.

## Diff semantics

Diffs are mechanical comparisons between preserved versions. Core labels should be neutral:

- added text;
- removed text;
- moved/reordered structure where detectable.

Avoid interpretive labels such as correction, retraction, lie, improvement, or contradiction.
