---
tags: [cs-ds, chunk]
id: chunk-ds-008
source: "[[raw-ds-005]]"
supports: ["[[Red-Black Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Red-Black trees need at most 3 rotations per mutation

## Context
Balancing after insert/delete is the bottleneck for self-balancing BSTs.

## Claim
Red-Black insertions require at most 2 rotations and deletions at most 3, making them efficient for write-heavy workloads and preferred in standard libraries.

## Why It Matters
This bounded rotation count is why Java TreeMap, C++ std::map, and Linux CFS use Red-Black trees.

## QnA Seeds
- Q: Why RB preferred over AVL for libraries? -> A: Fewer rotations per mutation (max 3 vs O(log n)).
- Q: What are the five RB properties? -> A: Root black, NIL black, red children are black, equal black-height, each node red or black.
