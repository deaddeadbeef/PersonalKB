---
tags: [cs-ds, chunk]
id: chunk-ds-104
source: "[[raw-ds-029]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# D-ary heaps optimize for cache and reduce height to log_d n

## Context
Binary heaps have height log2 n but each sift-down compares 2 children.

## Claim
D-ary heaps use d children per node reducing height to log_d n. For d=4 this matches cache line size (4 children fit in one line) and reduces extract-min comparisons despite more comparisons per level.

## Why It Matters
4-ary heaps often outperform binary heaps in practice due to cache effects especially for Dijkstra.

## QnA Seeds
- Q: Why d=4? -> A: Four 8-byte keys fit in a 32-byte half cache line enabling single fetch comparison.
- Q: Trade-off of larger d? -> A: Shorter height but more children to compare per sift-down step.
