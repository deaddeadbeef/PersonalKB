---
tags: [cs-ds, chunk]
id: chunk-ds-072
source: "[[raw-ds-011]]"
supports: ["[[Skip Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Skip lists support lock-free concurrent operations naturally

## Context
Balanced BSTs require complex concurrent rebalancing.

## Claim
Skip lists support lock-free insertion because adding a node only requires local pointer updates at each level and failed CAS can be retried without global restructuring.

## Why It Matters
Java ConcurrentSkipListMap and Redis sorted sets chose skip lists specifically for concurrency.

## QnA Seeds
- Q: Why easier to make concurrent than BSTs? -> A: No rotations needed so local CAS suffices.
- Q: What about deletion? -> A: Mark node logically deleted then physically unlink lazily.
