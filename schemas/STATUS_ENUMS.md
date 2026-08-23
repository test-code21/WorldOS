# Status Enums — Suggested Semantic Vocabulary

These names are directional and should be finalized with implementation tests.

## Retrieval status

- `success`
- `failed`
- `skipped`
- `cancelled`

## Observation outcome detail

- `content_obtained`
- `not_modified`
- `redirected`
- `http_error`
- `timeout`
- `dns_error`
- `blocked`
- `parser_error`
- `storage_error`
- `policy_skip`

## Source operational health

- `healthy`
- `stale`
- `retrieval_failing`
- `disabled`
- `never_observed`
- `storage_error`
- `parser_error`

## Important

These are operational labels only. Do not add epistemic labels such as `trustworthy`, `misinformation`, or `propaganda` to the core status vocabulary.
