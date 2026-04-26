---
id: chunk-csos-131
type: chunk
source: "Silberschatz, Galvin, Gagne; Tanenbaum, Bos (2018/2015)"
source_loc: "Memory Allocation: Buddy System"
topic: "memory"
claim: "The buddy system restricts all allocation sizes to powers of two, enabling O(1) buddy address computation via a single bit-flip and efficient recursive coalescing of adjacent free blocks"
confidence: verified
supports:
  - "[[Memory Management Overview]]"
  - "[[Virtual Memory and Paging]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Buddy system restricts allocations to powers of two for O(1) coalescing

## Context

The buddy system partitions memory into blocks whose sizes are powers of two. When a process requests memory, the allocator finds the smallest power-of-two block satisfying the request. If none exists, a larger block is recursively split in half — each half being the other's "buddy." When a block is freed, its buddy's address is computed by flipping a single bit (the bit position corresponding to the block's order), making the merge check O(1). If the buddy is also free, the pair is coalesced into a block of the next larger size, and coalescing propagates upward as far as possible. A buddy pair is two blocks of equal size whose addresses differ by exactly one bit.

## Why It Matters

The buddy system's elegant address arithmetic — buddy address via bit-flip, split/merge via bit operations — makes it one of the fastest deterministic memory allocators. It has been the standard for physical page management in production kernels (Linux, Windows) for decades, forming the base layer of the memory allocation hierarchy.

## QnA Seeds

- Q: How is a buddy's address computed from the block's address and order?
- Q: What happens when a freed block's buddy is also free?
- Q: Why must allocation sizes be powers of two in the buddy system?
