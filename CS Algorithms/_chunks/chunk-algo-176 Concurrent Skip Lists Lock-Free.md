---
id: chunk-csa-176
type: chunk
source: "[[Pugh 1990 - Skip Lists]]"
source_loc: "Concurrency"
topic: "data-structures"
claim: "Concurrent skip lists are easier to implement than concurrent balanced trees because modifications affect only local pointers at each level, enabling lock-free CAS-based implementations"
confidence: verified
supports:
  - "[[Skip List]]"
  - "[[Concurrent Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Concurrent skip lists easier than concurrent balanced trees

## Context

In balanced trees, rotations during rebalancing move nodes between subtrees, requiring complex locking protocols (hand-over-hand locking) to prevent concurrent access violations. Skip list modifications affect only local pointers at each level—no global structural changes—making fine-grained locking straightforward. Lock-free implementations use compare-and-swap (CAS) operations, avoiding locks entirely. This concurrency advantage led to skip list adoption in Java's ConcurrentSkipListMap and in LevelDB/RocksDB's MemTable indexing.

## Why It Matters

In multi-threaded systems, the ease of implementing concurrent skip lists is often the deciding factor over balanced trees, making this a critical practical consideration.

## QnA Seeds

- Q: Why are tree rotations problematic for concurrent balanced tree implementations?
- Q: How do lock-free skip lists use CAS operations?
- Q: What production systems use concurrent skip lists?
