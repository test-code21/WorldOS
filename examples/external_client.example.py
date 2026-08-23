"""Illustrative Sprint 006+ usage; endpoint/client names are directional until /v1 freezes."""

from worldos_client import WorldOS

client = WorldOS(
    base_url="https://worldos.example.com",
    api_key="YOUR_KEY",
)

results = client.search("public infrastructure")
for result in results.items:
    print(result.text)
    print(result.provenance.source_url)
    print(result.provenance.source_version_id)
