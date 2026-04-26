---
id: chunk-algo-137
type: chunk
source: "[[raw-algo-025]]"
source_loc: "B-Trees - Key Claims and Atomic Facts"
topic: "data-structures"
claim: "B-trees of minimum degree t achieve O(log_t n) disk accesses per operation; with t=1001, a tree of height 2 stores over 1 billion keys requiring at most 3 disk reads for any search."
confidence: verified
supports:
  - "[[B-Trees]]"
  - "[[External Memory Algorithms]]"
tags:
  - cs-algorithms
  - cs-algorithms/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# B-Tree Search Uses O(log_t n) Disk Accesses

## Context

Each node has t-1 to 2t-1 sorted keys (root may have fewer). A height-h B-tree stores >= 2t^h - 1 keys. For t=1001 and h=2: root + 2002 level-1 nodes + ~2M level-2 nodes = over 1 billion keys, searched with 3 I/O operations. CPU time per node is O(t) linear or O(log t) with binary search, giving O(t*log_t n) total. Node size is tuned to disk page size (4-16 KB) so each read fetches one complete node.

## Why It Matters

B-trees are the dominant index structure in databases and file systems because they minimize disk I/O. Understanding height analysis is essential for database internals and storage design.

## QnA Seeds

- Q: How many disk accesses does a B-tree search require?
- Q: How many keys can height-2 B-tree with t=1001 store?
- Q: Why match node size to disk page size?