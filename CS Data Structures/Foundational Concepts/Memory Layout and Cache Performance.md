---
tags: [cs-ds, foundational]
up: "[[Foundational Concepts Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
created: 2025-07-14
---
# Memory Layout and Cache Performance

> **One-line summary**: Real-world data-structure performance depends as much on memory layout and cache behavior as on asymptotic complexity, because a cache miss can cost 100× more than a cache hit.

## 🎯 Intuition
(2-min read. No jargon. Build mental picture.)

**The Core Idea:** How data is physically arranged in memory matters as much as the algorithm — because the CPU fetches data in chunks, and scattered data is punishingly slow to access.

**Analogy:** Imagine you're a librarian fulfilling reading requests. Your desk (L1 cache) holds 5 books. A nearby cart (L2 cache) holds 50. The library shelves (main memory) hold millions, but walking to them takes 100× longer than grabbing a book from your desk. If a reader requests pages from one book, you grab it once and keep flipping — fast. But if they request one page each from 100 different books scattered across the building, you're walking back and forth constantly. That's the difference between an array (one book, sequential pages) and a linked list (100 scattered books). Same number of pages read, wildly different time.

**Why It Matters:** Two algorithms with identical Big-O can differ by 10–100× in real speed. The difference is almost always cache behavior. Understanding the memory hierarchy is what separates textbook analysis from production-grade engineering.

---

## ⚙️ Core Mechanics
(Textbook level. Definitions, operations, complexity.)

### How It Works

Modern CPUs do not access main memory directly for every read. Instead, a hierarchy of caches — **L1** (~1–4 cycles, 32–64 KB), **L2** (~10 cycles, 256 KB–1 MB), and **L3** (~30–50 cycles, 4–64 MB shared) — sits between the processor and DRAM (~100–300 cycles). Data moves in fixed-size **cache lines**, typically **64 bytes**. When the CPU requests one byte, it fetches the entire 64-byte line, so neighboring bytes come "for free."

This is the hardware basis of **spatial locality**: accessing elements stored contiguously in memory is dramatically faster than chasing scattered pointers.

**Temporal locality** is the complementary principle: data accessed recently is likely to be accessed again soon, so the cache retains it.

Together, spatial and temporal locality explain why arrays dominate linked lists in practice for sequential access. An array of 4-byte integers fits 16 elements per cache line; iterating over *n* elements triggers roughly *n*/16 cache misses. A singly linked list with nodes scattered across the heap may trigger one cache miss **per node** — the same $O(n)$ traversal, but 10–100× slower in wall-clock time.

These effects reshape data-structure selection. B-trees outperform binary search trees not because of better Big-O, but because each node packs many keys into a cache-line-sized block, minimizing misses during search. Hash tables with open addressing (probing contiguous slots) outperform chaining (pointer-linked buckets) on modern CPUs for the same reason. Structure-of-Arrays (SoA) layouts often beat Array-of-Structures (AoS) when only a subset of fields is accessed, because they pack the hot fields contiguously.

### Key Operations

| Structure             | Traversal Big-O | Cache Misses (approx.) | Relative Wall-Clock |
|-----------------------|-----------------|------------------------|---------------------|
| Array                 | $O(n)$            | n / 16                 | 1× (baseline)       |
| Linked List (scattered)| $O(n)$           | ~n                     | 10–100×             |
| B-Tree search         | $O(\log n)$        | log_B(n), B ~ 16–32   | Fast                |
| BST search (pointer)  | $O(\log n)$        | ~log₂(n)              | Slower per level    |
| Hash (open addressing)| $O(1)$ avg        | 1–3 lines probed       | Fast                |
| Hash (chaining)       | $O(1)$ avg        | 1 + chain pointer hops | Slower              |

### Key Facts

- A typical **cache line is 64 bytes**; all data-structure analysis should account for how many useful elements fit in one line.
- **L1 cache hit**: ~1 ns; **DRAM access**: ~60–100 ns — a 60–100× penalty per miss.
- Arrays deliver excellent spatial locality; linked lists, trees with per-node allocation, and hash tables with chaining deliver poor spatial locality.
- **Prefetching** (hardware and software) can partially hide latency for predictable access patterns (arrays, sequential scans) but cannot help with pointer chasing.
- B-trees with branching factor tuned to cache-line size (e.g., 16–32 keys per node) minimize cache misses for search.
- **False sharing** occurs when two threads modify different variables that share a cache line, causing expensive coherence traffic.
- Structure-of-Arrays (SoA) vs. Array-of-Structures (AoS) is a critical layout decision in performance-sensitive systems (games, scientific computing).
- The "same Big-O, vastly different speed" phenomenon is the strongest argument for profiling beyond complexity analysis.

---

## 🔬 Deep Dive
(Proofs, edge cases, real-world tradeoffs)

### Formal Properties

- **Cache complexity model (Ideal Cache)**: The external memory model (Aggarwal & Vitter, 1988) formalizes cache performance. Memory is divided into blocks of size *B*. Scanning *n* elements costs $\Theta(n/B)$ I/Os. Sorting costs $\Theta((n/B)$ log_{M/B}(n/B)) I/Os, where *M* is cache size. This explains why merge sort (sequential access) often beats quicksort (random pivoting) on very large datasets despite similar comparison counts.
- **Cache-oblivious algorithms**: Algorithms designed without knowing *B* or *M* that still achieve optimal cache behavior. The van Emde Boas layout for static binary trees achieves $O(log_B n)$ cache misses per search — matching B-trees without knowing the cache line size.
- **TLB (Translation Lookaside Buffer)**: Virtual-to-physical address translation uses a small cache (TLB). Large data structures that span many pages cause TLB misses, adding another latency layer beyond L1/L2/L3. Huge pages (2 MB or 1 GB) can mitigate this.
- **Bandwidth vs. latency**: Prefetching and out-of-order execution can partially hide memory *latency*, but total *bandwidth* is fixed. Structures with high bytes-per-useful-datum ratios (e.g., pointer-heavy trees) waste bandwidth on pointer data.

### Edge Cases and Pitfalls

- **False sharing in multithreaded code**: Two threads writing to adjacent struct fields that share a cache line cause constant cache-line invalidations across cores. Fix: pad structs to cache-line boundaries (`alignas(64)` in C++, `@Contended` in Java).
- **NUMA effects**: On multi-socket systems, accessing memory attached to a remote socket can cost 2–3× more than local memory. Data structure placement must be NUMA-aware for large-scale systems.
- **Garbage collector interaction**: Languages with GC (Java, Go, C#) may compact or relocate objects, disrupting carefully planned memory layouts. Generational GC promotes objects to different heap regions, scattering what was once contiguous.
- **Huge arrays and page faults**: Allocating a multi-GB array may not trigger physical allocation until first access (lazy allocation). The first scan incurs page faults — thousands of µs per fault — making the first pass much slower than subsequent passes.
- **AoS vs SoA tradeoff**: AoS is more natural for object-oriented code and better when you access all fields together. SoA wins when you iterate over one field across many objects (e.g., updating only positions in a game entity system).

### Real-World Usage

- **Game engines (Unity DOTS / ECS)**: Entity Component Systems store components in SoA layout for cache-friendly iteration. This can yield 10–50× speedups over traditional OOP with scattered heap objects.
- **Database columnar storage (Apache Parquet, ClickHouse)**: Storing each column contiguously rather than each row enables massive scan speedups when queries touch only a few columns. This is SoA applied to databases.
- **Linux kernel slab allocator**: Allocates same-sized objects from contiguous slabs, improving cache behavior for frequently allocated kernel structures (inodes, dentries).
- **Google's Abseil `flat_hash_map`**: Uses open addressing with SIMD-accelerated probing on contiguous memory, specifically designed for modern cache hierarchies. Benchmarks show 2–5× faster than `std::unordered_map` (which uses chaining).
- **HPC and scientific computing**: Libraries like BLAS achieve near-peak FLOPS by tiling matrix operations to fit in L1/L2 cache, making memory layout the primary optimization target.

---

## 🏋️ Practice

### Warm-Up (5 min)
1. A cache line is 64 bytes. How many 4-byte integers fit in one line? How many 8-byte pointers? Why does this ratio matter for linked list vs. array performance?
2. You have two $O(n)$ algorithms: one iterates an array, the other traverses a scattered linked list. Estimate the wall-clock speed difference on modern hardware and explain why.
3. What is false sharing? Give a concrete scenario with two threads and explain why padding fixes it.

### Core Problems
1. **AoS vs SoA Comparison** — You have 1,000,000 game entities, each with `position (x,y,z)` (12 bytes), `velocity (vx,vy,vz)` (12 bytes), `health` (4 bytes), and `name` (64 bytes). Your hot loop updates only position and velocity. Calculate cache misses per entity for AoS vs. SoA layout, and estimate the speedup. (Expected approach: AoS struct = 92 bytes, spans ~2 cache lines. SoA: position + velocity = 24 bytes per entity, ~2.67 entities per line. SoA accesses ~1/4 the cache lines.)
2. **B-Tree Branching Factor** — Derive the optimal branching factor for a B-tree node that must fit in a single 64-byte cache line, given 8-byte keys and 8-byte child pointers. How many keys per node? Compare the search depth to a binary BST for n = 1,000,000 elements. (Expected approach: Each entry = key + pointer = 16 bytes, plus one extra pointer. ~3 keys fit per 64-byte node. Compare log₃(10⁶) ≈ 12.6 vs log₂(10⁶) ≈ 20, but with far fewer cache misses per level.)

### Challenge
**Cache-Oblivious Search Structure** — Research and explain the van Emde Boas memory layout for a static binary search tree. Why does it achieve $O(log_B n)$ cache misses per search without knowing B? Implement a static search tree in this layout for a sorted array of 1,000,000 integers and benchmark it against a naive in-order layout binary search.

---

*See also:* [[Pointer-Based vs Array-Based Structures]] | [[Asymptotic Analysis and Big-O Notation]] | [[CS Data Structures/Trees/B-Trees and B-Plus Trees|B-Trees]] | [[CS Data Structures/Hash-Based Structures/Hash Tables and Hash Functions|Hash Tables]] | [[Data Structure Comparison and Selection]] | **CS Algorithms:** [[CS Data Structures/Advanced Structures/Cache-Oblivious Structures|Cache-Oblivious Algorithms]] | [[CS Data Structures/Advanced Structures/External Memory Structures|External Memory Algorithms]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-061 Cache locality makes arrays 10-100x faster for iteration|Cache locality makes arrays much faster for iteration]]
- [[CS Data Structures/_chunks/chunk-ds-128 Sequential scan is always On over B cache transfers|Sequential scans use O(n/B) cache transfers]]
- [[CS Data Structures/_chunks/chunk-ds-160 Memory wall means layout matters more than algorithm|The memory wall makes layout matter]]
- [[CS Data Structures/_chunks/chunk-ds-023 Cache-oblivious structures optimize for all cache levels|Cache-oblivious structures optimize across cache levels]]
- [[CS Data Structures/_chunks/chunk-ds-151 Memory alignment affects struct layout and padding|Memory alignment affects struct layout and padding]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
