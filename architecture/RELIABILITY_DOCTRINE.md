# Reliability Doctrine

WorldOS is a longitudinal system. Silent data loss is more damaging than a visible temporary failure.

## Reliability priorities

1. **No silent loss of historical versions.**
2. **No silent scheduler failure.**
3. **Idempotent repeated jobs where practical.**
4. **Explicit failed-observation records.**
5. **Recoverable artifact/database relationships.**
6. **Safe migrations.**
7. **Tested backup/restore.**
8. **Observable stale sources.**

## Failure philosophy

A failed fetch is data about the observation process. Preserve it as an operational record rather than hiding it.

## Health categories

Keep health operational, not epistemic. Examples:
- healthy;
- stale;
- retrieval_failing;
- disabled;
- never_observed;
- storage_error;
- parser_error.

Do not use "untrustworthy" or "bad source" as health labels.

## Long-running deployment test

By Sprint 009, WorldOS should survive:
- restarts;
- temporary source outages;
- temporary network loss;
- worker restarts;
- duplicate job delivery;
- version upgrades;
- backup/restore rehearsal.
