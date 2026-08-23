# Preservation Mode Semantics

| Mode | Store full retrieved representation | Store extracted text | Store metadata/hash | Suitable for redistribution automatically? |
|---|---:|---:|---:|---:|
| `full` | Yes, subject to policy | Usually | Yes | No |
| `extracted_text` | Not necessarily | Yes | Yes | No |
| `metadata_only` | No | No | Yes | Possibly metadata only, subject to policy |
| `reference_only` | No | No | Minimal | Reference metadata only |

Redistributability must be represented separately from preservation mode.
