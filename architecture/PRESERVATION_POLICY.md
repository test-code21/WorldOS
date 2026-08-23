# Preservation Policy Architecture

WorldOS must separate **ability to retrieve** from **right/choice to preserve or redistribute**.

## Preservation modes

### `full`
Preserve the retrieved representation needed for faithful later inspection, subject to operator policy and applicable rights.

### `extracted_text`
Preserve a text representation while omitting or separately treating full raw bytes.

### `metadata_only`
Preserve observation metadata, hashes when appropriate, headers/identifiers, and descriptive metadata without storing full content.

### `reference_only`
Preserve source identity/location and observation facts but no source body.

## Required property

Every Source should have an explicit preservation mode or inherit one from documented instance policy. "Publicly reachable" must never silently mean "freely redistributable."

## Redistribution is separate

Later federation/export should use an explicit redistributability field. Storage permission and redistribution permission are not the same concept.

## Hashing

Document exactly what is hashed:

- raw bytes;
- extracted canonical text;
- or both.

Prefer retaining both hashes when feasible because they answer different questions.

## Source disappearance

Historical records should remain referentially intact when the live source disappears, subject to applicable legal/ethical requirements and operator policy.
