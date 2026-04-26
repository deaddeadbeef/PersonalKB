---
tags: [cs-ds, chunk]
id: chunk-ds-143
source: "[[raw-ds-006]]"
supports: ["[[B-Trees and B-Plus Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# B-tree minimum fill factor of 50pct bounds space waste

## Context
B-tree nodes can have between ceil(m/2) and m children.

## Claim
The minimum occupancy guarantee means every non-root node is at least half full. This bounds space utilization at 50 percent minimum with typical utilization around 67-69 percent for random insertions.

## Why It Matters
Predictable space usage is critical for database storage planning and SSD wear management.

## QnA Seeds
- Q: Why 50 percent minimum? -> A: Nodes split at m keys into two nodes of ceil(m/2) keys each.
- Q: Actual utilization? -> A: Random insertions give about 69 percent due to splits creating half-full nodes.
