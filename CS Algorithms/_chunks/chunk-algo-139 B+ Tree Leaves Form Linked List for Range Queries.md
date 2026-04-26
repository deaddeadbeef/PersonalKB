---
id: chunk-algo-139
type: chunk
source: "[[raw-algo-025]]"
source_loc: "B-Trees - Key Claims"
topic: "data-structures"
claim: "B+ trees store all data in leaf nodes linked as a doubly-linked list, with internal nodes holding only keys and child pointers; range queries traverse consecutive leaves sequentially after one O(log_t n) descent."
confidence: verified
supports:
  - "[[B-Trees]]"
  - "[[B+ Trees]]"
tags:
  - cs-algorithms
  - cs-algorithms/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# B+ Tree Leaves Form Linked List for Range Queries

## Context

Internal nodes store only separator keys and child pointers (no data), maximizing branching factor and minimizing height. All data resides in leaves linked to siblings. A range query 'keys 50 to 100' descends to key 50 in O(log_t n), then follows leaf pointers sequentially—cache-friendly and I/O-efficient. B+ trees are the dominant index in MySQL InnoDB, PostgreSQL, NTFS, HFS+, and ext4. Leaf-only data storage also simplifies concurrent access.

## Why It Matters

B+ trees are the most widely deployed index structure in production systems. The separation of routing from data and the linked-list leaf structure are the key design decisions enabling efficient range queries.

## QnA Seeds

- Q: How do B+ trees differ from B-trees in data layout?
- Q: How do B+ trees answer range queries efficiently?
- Q: Why store only keys in internal nodes?