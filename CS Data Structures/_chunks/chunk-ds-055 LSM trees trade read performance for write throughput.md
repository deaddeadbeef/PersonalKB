---
tags: [cs-ds, chunk]
id: chunk-ds-055
source: "[[raw-ds-039]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# LSM trees trade read performance for optimal write throughput

## Context
B-trees optimize for reads; what about write-heavy workloads?

## Claim
LSM trees buffer writes in a memory table, flush as immutable sorted runs to disk, and merge runs via compaction. This converts random writes to sequential I/O, achieving near-optimal write throughput.

## Why It Matters
Powers RocksDB, LevelDB, Cassandra, and all modern write-optimized storage engines.

## QnA Seeds
- Q: Why faster writes than B-tree? -> A: Sequential disk writes (flush/compact) vs random page updates.
- Q: Main read penalty? -> A: May check multiple levels — mitigated by Bloom filters.
