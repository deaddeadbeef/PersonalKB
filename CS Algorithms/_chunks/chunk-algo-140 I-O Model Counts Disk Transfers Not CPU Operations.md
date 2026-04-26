---
id: chunk-algo-140
type: chunk
source: "[[raw-algo-025]]"
source_loc: "B-Trees - Atomic Facts and Significance"
topic: "data-structures"
claim: "The I/O (external memory) model counts disk block transfers rather than CPU operations; B-tree nodes are sized to one disk page (4-16 KB) so each access is one I/O, and a height-3 tree with branching factor 500 indexes 125 million keys in 3 reads."
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
# I-O Model Counts Disk Transfers Not CPU Operations

## Context

Each block transfer moves B bytes (disk page size). With B=8 KB and 8-byte key-pointer pairs, a node holds ~500 entries giving branching factor ~500. Height 3 indexes 500^3 = 125M keys with 3 I/O ops. This model explains why B-trees beat binary search trees (O(log2 n) I/O) despite higher CPU cost per node, and why LSM-trees are preferred for write-heavy workloads (optimized for sequential writes). The framework extends to cache-oblivious algorithms and SSD-optimized structures.

## Why It Matters

The I/O model explains B-tree design. Without understanding that disk access—not CPU time—is the bottleneck, B-tree design choices appear arbitrary. This model is fundamental to database and storage system engineering.

## QnA Seeds

- Q: What does the I/O model measure?
- Q: Why do B-trees beat BSTs in the I/O model?
- Q: How many keys can a height-3 tree with branching 500 index?