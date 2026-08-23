# WorldOS — Current Decisions Log

These are current architecture decisions for the first decade. They remain subordinate to the canonical founding documents.

## Product boundary

- WorldOS is a generic, open-source, public-source substrate.
- It is narrower than SourceLedger.
- It does not own private organizational source permissions, source grants, or tenant/workspace governance.
- Core data models should not grow `tenant_id` merely in anticipation of a hosted SaaS product.

## Source acquisition

- Systematic/autonomous source discovery is out of scope for the decade.
- WorldOS will use explicitly configured sources.
- The reference project should build a high-quality curated source catalog with coverage across a UN-member-state baseline.
- Coverage gaps should be visible rather than hidden.

## Linguistic analysis

- MultilingualOS is not a WorldOS dependency.
- WorldOS may preserve source-declared or mechanically detected language metadata.
- Cross-language semantic normalization, translation, and interpretation belong downstream.
- The generic WorldOS API is the integration boundary.

## External integration

- One generic, stable API should be sufficient for IntelOS, websites, scripts, universities, or other users.
- No IntelOS-specific, MultilingualOS-specific, or AiBC-only connector should be required in core.

## Self-hosting

- The public repository is the canonical implementation.
- The generic install should be polished, reliable, low-maintenance, and deployable on a user's own systems.
- GCP is the preferred reference cloud, not a core dependency.
- A later hosted `worldos.austincanty.com` should run the same public product.

## Federation

- Federation belongs in the first decade in lightweight form.
- Initial federation means sharing safe knowledge about observation machinery: source manifests, adapter declarations, hashes, coverage metadata, schemas, and explicitly redistributable artifacts.
- It does not mean mandatory corpus replication, distributed consensus, or shared analytical judgments.

## Decade ending

- Sprint 009 proves self-hosted WorldOS can power an external website/app.
- Sprint 010 stabilizes the core and demonstrates external intelligence layered on top.
- MultilingualOS may appear in Sprint 010 only as a separate downstream teaser/consumer.
