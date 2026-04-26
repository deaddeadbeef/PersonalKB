---
tags: [cs-ds, chunk]
id: chunk-ds-051
source: "[[raw-ds-036]]"
supports: ["[[Bloom Filters and Probabilistic Structures]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Cuckoo filters support deletion unlike Bloom filters

## Context
Bloom filters cannot delete elements without risk of false negatives.

## Claim
Cuckoo filters store fingerprints in a cuckoo hash table, supporting O(1) insertion, lookup, and deletion while achieving better space efficiency than Bloom filters at low false-positive rates.

## Why It Matters
Used in RocksDB and networking where approximate membership with deletion is needed.

## QnA Seeds
- Q: How is deletion possible? -> A: Remove the fingerprint from its bucket — deterministic location.
- Q: Space vs Bloom? -> A: Cuckoo filter beats Bloom below 3% FP rate; Bloom wins above.
