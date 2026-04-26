---
tags: [cs-ds, chunk]
id: chunk-ds-141
source: "[[raw-ds-003]]"
supports: ["[[Circular Buffers]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Power-of-two buffer size makes modular arithmetic a single bitmask

## Context
Circular buffers compute indices using modulo: index mod capacity.

## Claim
When capacity is a power of two, modulo becomes a bitwise AND with capacity-1 which is a single CPU instruction. This eliminates the expensive division instruction from every enqueue and dequeue.

## Why It Matters
Ubiquitous micro-optimization in kernel ring buffers, network drivers, and lock-free queues.

## QnA Seeds
- Q: Why power of two? -> A: index AND (capacity-1) equals index mod capacity but is much faster.
- Q: How much faster? -> A: Bitwise AND is 1 cycle. Division is 20-40 cycles on most architectures.
