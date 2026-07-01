---
tags: [cs-ds, hash-based, probabilistic]
up: "[[Hash-Based Structures Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, practice]
---

# Cuckoo Filters

> **One-line summary** A cuckoo filter is a probabilistic membership structure like a Bloom filter, but it stores compact fingerprints in cuckoo-hash tables so deletion is practical.

## Intuition

Bloom filters answer "is this item possibly in the set?" with no false negatives and some false positives, but ordinary Bloom filters do not support deletion safely. Cuckoo filters solve that by storing short fingerprints in buckets. Each fingerprint has two possible bucket locations, and insertion may evict existing fingerprints along a cuckoo-hashing chain.

If lookup finds the fingerprint in either candidate bucket, the item is probably present. If not, it is definitely absent, assuming the structure has not exceeded its load limits.

## Core Mechanics

- Store a short fingerprint rather than the full key.
- Compute two candidate buckets for each item.
- Insert into either bucket, evicting and relocating fingerprints when needed.
- Delete by removing the matching fingerprint from one candidate bucket.
- False positives remain possible because fingerprints can collide.

## Why It Matters

Cuckoo filters are useful when membership tests need deletion, compact memory use, and fast lookup. They appear in storage engines, caching systems, network filters, and deduplication pipelines where a Bloom filter's lack of deletion would be operationally awkward.

## Practice

1. Explain why Bloom filters cannot naively delete items.
2. Describe why fingerprint collisions create false positives.
3. Compare cuckoo filters with Bloom filters for a workload with frequent deletions.

## References

- [[CS Data Structures/Hash-Based Structures/Bloom Filters and Probabilistic Structures]]
- [[CS Data Structures/Hash-Based Structures/Cuckoo Hashing]]
- [[CS Data Structures/Hash-Based Structures/Count-Min Sketch]]
