---
id: chunk-csa-179
type: chunk
source: "[[Bloom 1970 - Bloom Filters]]"
source_loc: "Practical Space"
topic: "data-structures"
claim: "A Bloom filter at 10 bits per element (roughly 1.2 bytes) achieves approximately 1 percent false positive rate, orders of magnitude less than storing actual elements"
confidence: verified
supports:
  - "[[Bloom Filter]]"
  - "[[Space-Efficient Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Bloom filter 10 bits per element for 1 percent false positive rate

## Context

At 10 bits per element (~1.2 bytes), a Bloom filter achieves approximately 1% false positive rate. This is orders of magnitude less space than storing actual elements or their hashes. In Google Chrome, a locally stored Bloom filter checks URLs against known malicious sites, avoiding network round-trips for safe URLs. In LSM-tree databases (LevelDB, RocksDB, Cassandra), per-SSTable Bloom filters prevent unnecessary disk reads by quickly ruling out absent keys during point lookups. The false positive rate degrades gracefully as more elements are inserted.

## Why It Matters

The practical space-to-accuracy tradeoff makes Bloom filters indispensable in systems design—knowing the concrete numbers (10 bits = 1% FPR) enables quick engineering decisions.

## QnA Seeds

- Q: How much space does a Bloom filter need per element for 1% false positive rate?
- Q: How do LSM-tree databases use Bloom filters to optimize reads?
- Q: How does Chrome use Bloom filters for safe browsing?
