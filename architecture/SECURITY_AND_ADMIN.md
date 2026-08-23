# Security and Administration

WorldOS is public-source software, but its administrative surface still needs protection.

## Separate concerns

### Read/query access
May be public or token-protected according to operator configuration.

### Administrative mutation
Should require operator authentication for actions such as:
- add/disable sources;
- import catalogs/bundles;
- trigger observations;
- rotate API keys;
- alter preservation policy;
- change schedules.

## Do not let security become tenancy

Security controls should protect an instance. They should not introduce workspace membership or source-level organizational ACL semantics into the core data model.

## Secrets

- never commit secrets;
- use environment variables/secret stores;
- document rotation;
- GCP reference deployments may use Secret Manager.

## Source safety

URL fetching should include SSRF-aware protections appropriate to a self-hosted fetcher. Operators should be able to restrict private-network targets and dangerous schemes.

## Content safety

Preserved content is untrusted input. Frontend rendering should not execute arbitrary retrieved HTML/JS.
