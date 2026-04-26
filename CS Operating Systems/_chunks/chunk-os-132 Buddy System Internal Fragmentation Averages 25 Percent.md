---
id: chunk-csos-132
type: chunk
source: "Silberschatz, Galvin, Gagne; Tanenbaum, Bos (2018/2015)"
source_loc: "Memory Allocation: Buddy System"
topic: "memory"
claim: "The buddy system wastes approximately 25% of allocated memory on average due to internal fragmentation — requests are rounded up to the next power of two, so a 65 KB request receives a 128 KB block"
confidence: verified
supports:
  - "[[Memory Management Overview]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Internal fragmentation averages 25% from power-of-two rounding

## Context

The buddy system's power-of-two constraint means every allocation is rounded up to the next power of two. A request for 65 KB receives a 128 KB block, wasting 63 KB (49%). A request for 33 KB gets 64 KB, wasting 31 KB (48%). On average across a range of allocation sizes, internal fragmentation wastes approximately 25% of allocated memory. This is the primary disadvantage of the buddy system — external fragmentation is minimal (coalescing prevents it), but internal fragmentation is structurally inevitable.

## Why It Matters

This 25% overhead is why the buddy system is not used directly for small, variable-size allocations. Instead, Linux layers the slab allocator on top of the buddy allocator — the buddy handles coarse page-sized allocations while the slab carves pages into precisely-sized object caches, virtually eliminating internal fragmentation for common kernel objects.

## QnA Seeds

- Q: Why does the buddy system produce internal fragmentation?
- Q: What is the average internal fragmentation percentage for the buddy system?
- Q: How does the slab allocator mitigate the buddy system's internal fragmentation?
