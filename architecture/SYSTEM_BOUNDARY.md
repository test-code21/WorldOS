# System Boundary — WorldOS vs Adjacent Systems

## WorldOS owns

- explicitly configured public sources;
- source identity and operational metadata;
- retrieval attempts/observations;
- preserved source versions;
- stored artifacts or references according to policy;
- mechanical document structure;
- source-local segments;
- longitudinal version history;
- provenance-preserved search;
- source health and coverage status;
- generic API access to its records;
- source catalog import/export;
- lightweight community/federation bundles.

## WorldOS does not own

### SourceLedger territory
- organizational tenants/workspaces;
- employees/members/roles;
- private source grants;
- per-user/provider permissions;
- Google Drive/Dropbox/SharePoint source governance;
- client-specific knowledge boundaries;
- private organizational context.

### IntelOS territory
- deciding which systems to query for a user's question;
- cross-system retrieval orchestration;
- relevance strategy across public and private corpora;
- analytical workflow orchestration.

### ModelOS territory
- selecting analytical models;
- running interpretive model workflows;
- scoring or judging source claims.

### MultilingualOS territory
- translation as interpretation layer;
- cross-language semantic normalization;
- language-learning or culturally aware linguistic interpretation.

## Anti-drift test

Before adding a core table or endpoint, finish this sentence:

> WorldOS needs this because it helps an operator **observe, preserve, structure, retrieve, or expose public source material**.

If the sentence instead ends with "decide," "judge," "recommend," "understand the organization," or "govern a private user's access," the feature probably belongs elsewhere.

## Administration is not tenancy

WorldOS may need:

- an instance administrator;
- credentials for protected source retrieval where legally/configurationally appropriate;
- API keys/tokens;
- operator settings;
- local access control around administrative mutation.

That does not justify a workspace/tenant business model in the core schema.
