---
tags: [cs-ds, chunk]
id: chunk-ds-137
source: "[[raw-ds-039]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Memtables use skip lists or red-black trees for sorted writes

## Context
LSM trees need a sorted in-memory buffer for incoming writes.

## Claim
The memtable is typically implemented as a skip list (LevelDB) or red-black tree (RocksDB option) providing O(log n) sorted insertion. When full it is flushed as an immutable SSTable to disk.

## Why It Matters
Memtable structure determines write throughput. Skip lists are preferred for their lock-free concurrent insertion.

## QnA Seeds
- Q: Why skip list over red-black? -> A: Lock-free concurrent writes without complex locking.
- Q: When is memtable flushed? -> A: When it reaches a size threshold (typically 64MB-256MB).
