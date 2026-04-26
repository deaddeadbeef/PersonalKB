---
tags: [cs-ds, chunk]
id: chunk-ds-069
source: "[[raw-ds-009]]"
supports: ["[[Bloom Filters and Probabilistic Structures]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Count-Min Sketch estimates frequency with bounded error in sublinear space

## Context
Exact frequency counting requires O(n) space for n distinct items.

## Claim
Count-Min Sketch uses d hash functions and w counters per row. Frequency estimate is the minimum across d rows giving at most epsilon*N overcount with probability 1-delta using O(1/epsilon * log(1/delta)) space.

## Why It Matters
Powers real-time analytics: heavy hitter detection, network traffic monitoring, database query optimization.

## QnA Seeds
- Q: Why take minimum? -> A: Each row may overcount due to collisions but minimum gives tightest bound.
- Q: Can it undercount? -> A: Never. It can only overcount due to hash collisions.
