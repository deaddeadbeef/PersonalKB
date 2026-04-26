---
tags: [cs-ds, raw]
id: raw-ds-021
source: "Open Data Structures (Morin, Ch. 4)"
up: "[[CS Data Structures]]"
---

# Memory Allocation and Garbage Collection

## Key Ideas
- Stack allocation: LIFO, automatic, O(1) alloc/free via pointer bump
- Heap allocation: malloc/free, fragmentation risk, O(1) amortized with free lists
- Internal vs external fragmentation trade-offs
- Reference counting: immediate cleanup, but circular reference problem
- Mark-and-sweep: handles cycles, but stop-the-world pauses
- Generational GC: most objects die young (weak generational hypothesis)
- Compacting collectors: eliminate fragmentation, enable pointer bumping
- Arena allocation: batch alloc/free, ideal for phase-based programs
- Memory pools: fixed-size blocks, zero fragmentation, O(1) alloc/free
- RAII vs GC: deterministic vs automatic lifetime management
