---
tags: [cs-ds, memory-hierarchy]
up: "[[Advanced Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Cache-Oblivious Structures

> **One-line summary**: Data structures that achieve asymptotically optimal cache performance on any memory hierarchy without knowing cache size or block size parameters.

## 🎯 Intuition
**The Core Idea:** Design algorithms and data structures that automatically exploit every level of the memory hierarchy (L1, L2, L3, RAM, disk) without being tuned to any specific level's parameters.
**Analogy:** A cache-aware chef organizes ingredients in batches sized for their specific counter space. A cache-oblivious chef uses a recursive organizational principle (like nested containers) that works efficiently regardless of counter size, fridge capacity, or pantry dimensions — any kitchen automatically performs well.
**Why It Matters:** Real systems have multi-level caches with varying sizes and line widths. Writing code that's optimal at every level without explicit tuning simplifies development and ensures portability.

---

## ⚙️ Core Mechanics
### How It Works
Cache-oblivious design uses the **ideal cache model** for analysis:
- Memory has two levels: a cache of size `M` with block size `B`, and infinite main memory.
- The cache is **fully associative** with optimal (clairvoyant) replacement.
- Algorithms are analyzed in terms of `M` and `B` but **never use these values** at runtime.

**Key technique — Van Emde Boas layout** (for static trees):
- Recursively split a complete binary tree at the middle level.
- Store the top half, then recursively store each bottom subtree.
- This ensures that for any cache size, subtrees that fit in cache are stored contiguously.

**Key technique — Cache-oblivious B-trees:**
- Use a static structure with a "packed memory array" for ordered elements.
- Insertions and deletions are handled by local rebalancing within density-bounded regions.
- Searches use the van Emde Boas layout for optimal cache transfers.

### Key Operations

| Operation | Cache Transfers | Notes |
|-----------|----------------|-------|
| Search (CO B-tree) | $O(log_B N)$ | Optimal, matches B-tree |
| Insert/Delete (CO B-tree) | $O((log² N)$/B) amortized | Slightly worse than B-tree |
| Range query (k results) | $O(log_B N + k/B)$ | Optimal |
| Matrix transpose | $O(N²/(B√M)$) | Cache-oblivious blocked transpose |
| Merge sort (Funnel Sort) | $O((N/B)$ log_(M/B) (N/B)) | Optimal sorting bound |

### Key Facts
- **Tall cache assumption**: most results require `M = Ω(B²)` — the cache must hold at least B² elements. This holds for all real hardware.
- The van Emde Boas layout achieves optimal search with zero tuning parameters.
- **Funnel Sort** is the cache-oblivious optimal sorting algorithm — it matches the external-memory sorting lower bound.
- Cache-oblivious structures are also **self-tuning across hierarchy levels**: they're simultaneously optimal for L1, L2, L3, and disk.
- In practice, cache-oblivious structures often have higher constant factors than cache-aware structures tuned for a specific level.

---

## 🔬 Deep Dive
### Formal Properties
**Ideal cache model (Frigo et al., 1999):**
- Cache complexity `Q(N; M, B)` = number of block transfers between cache and main memory.
- A cache-oblivious algorithm achieves optimal `Q` without knowing `M` or `B`.
- The **optimal replacement** assumption can be simulated by LRU with a constant factor overhead (LRU is 2-competitive for block transfers).

**Search lower bound:** Any comparison-based search among N elements requires `Ω(log_B N)` cache transfers. The CO B-tree matches this.

**Sorting lower bound:** Sorting N elements requires `Ω((N/B) log_(M/B)(N/B))` transfers. Funnel Sort matches this.

**Scanning bound:** Reading N contiguous elements costs `Θ(N/B)` transfers — the baseline for sequential access.

### Edge Cases and Pitfalls
- **Constant factor overhead**: cache-oblivious structures typically have 2-5× larger constants than hand-tuned cache-aware structures. For performance-critical single-level optimization, B-trees may still win.
- **Dynamic operations**: the original CO B-tree has `O((log² N)/B)` amortized insert cost, which is suboptimal. Exponential-tree-based variants achieve `O(log_B N)` amortized but are extremely complex.
- **Implementation complexity**: recursive layouts are non-trivial to implement correctly. Index calculations in van Emde Boas layout require careful recursion or precomputed tables.
- **Pointer-based structures don't benefit**: linked lists and pointer-based trees inherently have poor cache behavior regardless of layout. CO design applies primarily to implicit/array-based structures.
- **Theoretical vs. practical**: some CO algorithms (like Funnel Sort) are asymptotically optimal but rarely faster than well-tuned cache-aware mergesort in practice due to high constants.

### Real-World Usage
- **COLA (Cache-Oblivious Lookahead Array)**: used in TokuDB (now Percona's TokuDB storage engine for MySQL) for write-optimized databases. Achieves excellent insertion performance.
- **Fractal tree indexes**: commercially used in Tokutek products — essentially cache-oblivious B-tree variants with buffering.
- **Scientific computing**: cache-oblivious matrix multiplication and FFT algorithms are used in FFTW (Fastest Fourier Transform in the West).
- **STXXL**: the C++ external memory library implements cache-oblivious algorithms for processing data larger than RAM.
- **Research influence**: the CO model has influenced CPU cache prefetching strategies and compiler-level loop tiling optimizations.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What does "cache-oblivious" mean — what parameters does the algorithm NOT know?
2. Why is the van Emde Boas tree layout better for searches than a standard BFS or DFS array layout of a binary tree?
3. What is the "tall cache assumption" and why is it needed?

### Core Problems
1. **Van Emde Boas Layout**: Given a complete binary tree of height h stored in an array, implement the recursive van Emde Boas layout. Write `layout(tree)` and `search(key)` functions. Measure cache misses using `perf stat` (or a simulator) versus BFS layout.
2. **Cache-Oblivious Matrix Transpose**: Implement a recursive divide-and-conquer matrix transpose that operates in `O(N²/B)` cache transfers. Compare wall-clock time against naive transpose for large matrices.

### Challenge
Implement a simplified **Cache-Oblivious B-tree** with search, insert, and range-query. Use a packed memory array with density thresholds [0.25, 0.75] for rebalancing. Benchmark against `std::map` (red-black tree) and a B+-tree with tuned node size on range query workloads.

---

*See also:* [[B-Trees and B+ Trees]] · [[External Memory Structures]] · [[LRU and LFU Caches]] | **CS Algorithms:** [[Divide and Conquer]] · [[External Sorting]]

## References
-> [[Sources Index]]
