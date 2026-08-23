# WorldOS — Decade Map

The decade tells one continuous engineering story. Each sprint earns the next.

| Sprint | Story | New capability | Why it is useful immediately |
|---|---|---|---|
| 001 | The First Memory | Durable observation + preservation | A public source can be remembered reliably. |
| 002 | The Registry | Declarative source manifests | Operators add supported sources without editing code. |
| 003 | The Chronicle | Repeated observation + versions + diffs | We can show how a source changed over time without interpreting the change. |
| 004 | The Addressable Document | Segments + locators + process lineage | Machines can retrieve exact parts of preserved documents. |
| 005 | The Library | Search + filters + provenance | The accumulated record becomes practically useful. |
| 006 | The Connector | Stable `/v1` API + generic clients | Any external application can use WorldOS without knowing internals. |
| 007 | The World Shelf | Curated global reference catalog + coverage view | The generic machinery gets serious geographic breadth. |
| 008 | The Commons | Community bundles + safe federation metadata | Independent instances improve one another without forced corpus replication. |
| 009 | Bring Your Own WorldOS | Hardened self-hosting + external-site proof | A third party can deploy it and connect their own software. |
| 010 | Beyond the Boundary | 1.0 stabilization + external intelligence demo | We prove that powerful analysis can be layered on top without bloating WorldOS. |

## Why this order

- We cannot version what we cannot preserve.
- A registry is useful only after a source can actually be observed.
- Longitudinal history should exist before search hides temporal differences.
- Segmentation should mature before the public API freezes resource shapes.
- Search should mature before the connector becomes a compatibility promise.
- Global catalog work should wait until collection health can be measured honestly.
- Federation should wait until manifests and adapters have stable semantics.
- Self-hosting should be marketed only after upgrades, backups, diagnostics, and migrations are boring.
- Intelligence should be demonstrated only after WorldOS's stopping point is unmistakable.

## End-state sentence

At the end of Sprint 010, an operator should be able to clone WorldOS, deploy it, load a curated source catalog, let it observe those sources over time, inspect and search the preserved record, expose that record through one stable API, import community source knowledge safely, and hand the returned evidence to any external analytical or language system they choose.
