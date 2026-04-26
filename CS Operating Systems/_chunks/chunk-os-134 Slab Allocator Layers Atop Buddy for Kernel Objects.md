---
id: chunk-csos-134
type: chunk
source: "Silberschatz, Galvin, Gagne; Tanenbaum, Bos (2018/2015)"
source_loc: "Memory Allocation: Buddy System"
topic: "memory"
claim: "The slab allocator layers atop the buddy system to efficiently manage small, frequently-allocated kernel objects — SLUB (the current Linux default) replaced SLAB with simpler design and better NUMA scalability"
confidence: verified
supports:
  - "[[Memory Management Overview]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Slab allocator layers atop buddy for efficient kernel object allocation

## Context

The buddy system's minimum allocation is a full page (4 KB), but kernel objects like task_struct, inode, and dentry are much smaller and allocated millions of times. The slab allocator pre-allocates caches of objects at specific sizes, carving buddy-allocated pages into same-sized object slots. This eliminates per-object buddy overhead and reduces fragmentation. Linux has shipped three slab implementations: SLAB (the original, with cache coloring to reduce cache line conflicts), SLUB (the current default, simpler with better NUMA behavior and less metadata overhead), and SLOB (a minimal ~2 KB first-fit allocator for embedded systems with <16 MB RAM). kmalloc() allocates from SLUB caches in power-of-two sizes from 8 to 8192 bytes.

## Why It Matters

The buddy + slab layered design is a fundamental OS pattern: a coarse-grained allocator for large units topped by a specialized cache for fine-grained frequent allocations. The same pattern appears in user-space allocators (malloc's arenas + thread caches) and database buffer managers.

## QnA Seeds

- Q: Why can't the buddy allocator efficiently handle small kernel object allocations directly?
- Q: What are the three Linux slab implementations and when is each used?
- Q: How does SLUB improve over SLAB for modern multicore systems?
