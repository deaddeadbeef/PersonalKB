---
tags: [cs-ds, chunk]
id: chunk-ds-065
source: "[[raw-ds-006]]"
supports: ["[[B-Trees and B-Plus Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# B-plus trees link leaves for O(k) range scans after O(logm n) seek

## Context
B-trees store data in internal and leaf nodes making range scans require tree traversal.

## Claim
B+ trees store all data in leaves and link leaves in a doubly-linked list. After seeking to the start key in O(log_m n) the rest of the range is a sequential leaf scan in O(k).

## Why It Matters
This is why every major RDBMS uses B+ tree indices. Range queries are the most common database operation.

## QnA Seeds
- Q: How do B+ leaves differ from B-tree? -> A: B+ internal nodes are keys only. All data lives in leaves.
- Q: Why linked leaves? -> A: Sequential scan of sorted data without returning to parent nodes.
