---
tags: [cs-ds, chunk]
id: chunk-ds-005
source: "[[raw-ds-003]]"
supports: ["[[Circular Buffers]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Circular buffers use modular arithmetic for O(1) fixed-size queue ops

## Context
Fixed-size queues need efficient enqueue and dequeue without shifting.

## Claim
Circular buffers wrap around a fixed-size array using modular arithmetic (index mod capacity), providing O(1) enqueue and dequeue with excellent cache locality.

## Why It Matters
Ideal for streaming, kernel I/O, and producer-consumer patterns where fixed capacity is acceptable.

## QnA Seeds
- Q: How does wrap-around work? -> A: Next index = (current + 1) mod capacity.
- Q: How to distinguish full from empty? -> A: Maintain a count field, or sacrifice one slot.
