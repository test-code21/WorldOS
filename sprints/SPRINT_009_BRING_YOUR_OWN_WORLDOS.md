# Sprint 009 — Bring Your Own WorldOS

## Story

Sprint 009 proves the generic promise under hostile conditions: **someone who is not us should be able to run WorldOS and connect their own product to it.**

The goal is not another deployment guide written by the person who already knows all the hidden steps. The goal is a clean-room success.

## Immediate user value

A developer or organization can deploy WorldOS, maintain it with little intervention, and use it as infrastructure for their own website/application.

## Capability added

```text
Third-party infrastructure
  └── WorldOS
        ↑ /v1
External website/app
```

## Implementation scope

### Deployment hardening
- polished Docker/Compose path;
- polished GCP reference path;
- environment diagnostics;
- first-run setup;
- database migrations/upgrades;
- backup/restore;
- artifact backup guidance;
- restart recovery;
- scheduler/worker supervision;
- API key administration.

### Operator experience
- setup checklist/wizard;
- system health page;
- stale/failing source remediation;
- version/build information;
- upgrade instructions;
- troubleshooting decision tree.

### External integration proof
Build a **separate repository/site**, not a WorldOS frontend route, that uses only `/v1` and a normal client library to display:
- configured public sources;
- recent observed changes;
- search results;
- source provenance.

## Demo story

1. New machine/project starts from repository docs.
2. Operator deploys WorldOS.
3. Imports a source bundle.
4. Waits/triggers observations.
5. Generates an API key.
6. Separate site connects using only base URL + key.
7. Restart/upgrade is performed.
8. Site continues working.

## Acceptance gates

- [ ] Clean-room deployment succeeds from docs.
- [ ] No private AiBC service is required.
- [ ] External app imports no backend internals.
- [ ] Backup and restore have been rehearsed.
- [ ] Upgrade from prior sprint release is tested.
- [ ] Failures are diagnosable from UI/logs/docs.
- [ ] A normal operator can run WorldOS without continuous developer babysitting.

## Non-goals

No hosted SaaS tenancy, billing system, customer workspaces, or custom intelligence stack bundled into WorldOS.

## Why Sprint 010 depends on this

Only after independent operation is proven can the decade credibly end by showing WorldOS as a substrate other intelligence systems choose to consume.
