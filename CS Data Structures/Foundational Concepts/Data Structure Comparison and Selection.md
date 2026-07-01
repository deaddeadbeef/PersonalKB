---
tags: [cs-ds, foundational]
up: "[[Foundational Concepts Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
created: 2025-07-14
---
# Data Structure Comparison and Selection

> **One-line summary**: Selecting the right data structure requires identifying the dominant operations in your workload and then choosing the structure whose complexity, memory, and cache profile best match those operations.

## 🎯 Intuition
(2-min read. No jargon. Build mental picture.)

**The Core Idea:** There's no "best" data structure — only the best one *for your specific workload*.

**Analogy:** Choosing a data structure is like choosing a vehicle. Need to haul lumber? Pick a truck (array — great capacity, can't weave through traffic). Need to dart through city traffic? Pick a motorcycle (linked list — nimble insertions, bad at carrying heavy loads). Need something balanced? Pick an SUV (balanced BST — decent at everything, best at nothing). And if you're only going two blocks, just walk (small *n* — use a flat array and linear scan, overhead of fancier structures isn't worth it). The vehicle you choose depends entirely on the trip, not on which vehicle has the best spec sheet.

**Why It Matters:** Picking the wrong data structure is one of the most expensive mistakes in software architecture. It forces workarounds, tanks performance, and resists refactoring. A disciplined selection framework — operations first, then complexity, then cache and memory, then profile — prevents this.

---

## ⚙️ Core Mechanics
(Textbook level. Definitions, operations, complexity.)

### How It Works

The selection process begins with a simple question: **what operations does your code perform most often?** If you need constant-time key lookup, a hash table wins. If you need sorted iteration and range queries, a balanced BST or B-tree is appropriate. If you need fast append and positional access, a dynamic array is the default. Framing the question around operations — not data — prevents premature commitment.

A **comparison matrix** makes the trade-offs visible:
- **Arrays**: $O(1)$ access, excellent cache performance, but $O(n)$ insertion.
- **Linked lists**: $O(1)$ insertion at known positions, but $O(n)$ search and poor locality.
- **Balanced BSTs** (AVL, red-black): $O(\log n)$ for search, insert, and delete with sorted-order traversal, but each node is a separate allocation with pointer overhead.
- **Hash tables**: $O(1)$ average for insert, delete, and lookup, but no ordering and $O(n)$ worst-case without careful collision handling.
- **Heaps**: $O(1)$ find-min/max and $O(\log n)$ insert/extract, but no efficient arbitrary search.

Context determines the right answer. A 50-element collection rarely needs anything beyond a flat array — linear scan at that size is faster than tree or hash overhead. A real-time system may reject amortized $O(1)$ in favor of worst-case $O(\log n)$ because occasional spikes are unacceptable. A memory-constrained embedded device may choose a sorted array over a hash table to avoid load-factor waste. **Profiling** is the final arbiter: theoretical complexity guides the shortlist, but measured performance on your hardware with your data makes the decision.

### Key Operations

| Structure         | Search     | Insert     | Delete     | Min/Max    | Ordered Iter | Cache    |
|-------------------|------------|------------|------------|------------|--------------|----------|
| Dynamic Array     | $O(n)$       | $O(n)$*      | $O(n)$       | $O(n)$       | No           | Excellent|
| Sorted Array      | $O(\log n)$   | $O(n)$       | $O(n)$       | $O(1)$       | Yes          | Excellent|
| Linked List       | $O(n)$       | $O(1)$^      | $O(1)$^      | $O(n)$       | No           | Poor     |
| Hash Table        | $O(1)$ avg   | $O(1)$ avg   | $O(1)$ avg   | $O(n)$       | No           | Moderate |
| Balanced BST      | $O(\log n)$   | $O(\log n)$   | $O(\log n)$   | $O(\log n)$   | Yes          | Moderate |
| Binary Heap       | $O(n)$       | $O(\log n)$   | $O(\log n)$   | $O(1)$       | No           | Good     |
| B-Tree            | $O(\log n)$   | $O(\log n)$   | $O(\log n)$   | $O(\log n)$   | Yes          | Excellent|

*\*$O(1)$ amortized at end.  ^At a known position; finding the position is $O(n)$.* 

### Key Facts

- **Start with operations**: list the top 2–3 operations by frequency; choose the structure that optimizes those.
- Hash tables are the default for unordered key-value workloads; balanced BSTs for ordered workloads.
- For small *n* (< ~100), a simple array with linear scan often beats theoretically superior structures due to cache effects and low overhead.
- Heaps are optimal when you only need the min or max, not arbitrary search.
- **Sorted arrays** with binary search are a strong read-heavy alternative to BSTs: $O(\log n)$ search, zero pointer overhead, cache-friendly.
- When multiple operations matter equally, balanced BSTs ($O(\log n)$ across the board) are the safest general-purpose choice.
- Real-time constraints disqualify amortized structures (dynamic arrays, splay trees) in favor of worst-case guarantees (red-black trees, B-trees).
- Hybrid structures (e.g., hash map + doubly linked list for LRU cache) are common when no single structure covers all required operations.

---

## 🔬 Deep Dive
(Proofs, edge cases, real-world tradeoffs)

### Formal Properties

- **No free lunch theorem (informally)**: No single data structure achieves optimal complexity for all operations simultaneously. This can be formalized via cell-probe lower bounds — e.g., any data structure supporting $O(\log n)$ predecessor queries requires $\Omega(\log n)$ update time.
- **Space-time tradeoffs**: Augmenting a BST with parent pointers, subtree sizes, or order statistics uses $O(n)$ extra space but enables $O(\log n)$ rank queries. Every augmentation trades space for time.
- **Amortized vs. worst-case selection criterion**: If your application can tolerate occasional latency spikes (web servers with retry logic), amortized structures are fine. If it cannot (audio rendering, flight control), worst-case bounds are mandatory.
- **Entropy-based lower bounds**: For search over *n* sorted items, information theory gives $\Omega(\log n)$ comparisons. Hash tables beat this by using hashing instead of comparisons — they operate in a different computational model.

### Edge Cases and Pitfalls

- **Small-n trap**: Developers often over-engineer with hash maps or trees when a flat array of 20 elements with linear scan would be faster and simpler. Profile before optimizing.
- **Hash table worst case**: Without a good hash function or collision strategy, hash tables degrade to $O(n)$. Java's `HashMap` mitigates this by converting long chains to red-black trees (since Java 8).
- **Memory fragmentation**: Pointer-based structures (linked lists, trees) with per-node allocation can fragment the heap, increasing allocator overhead and GC pressure.
- **Iterator invalidation**: Dynamic arrays invalidate iterators on resize; linked lists don't. This is a correctness constraint that may override performance considerations.
- **Concurrency characteristics**: `ConcurrentHashMap` uses lock striping; `ConcurrentSkipListMap` is lock-free with $O(\log n)$. The choice depends on contention patterns, not just sequential complexity.

### Real-World Usage

- **Redis**: Uses hash tables for key-value storage, skip lists for sorted sets, and ziplist (compact arrays) for small collections — a textbook example of workload-driven selection.
- **Linux kernel**: Uses red-black trees for process scheduling (CFS), radix trees for page cache, and hash tables for dentry cache — each chosen for its dominant operation pattern.
- **Database indexes**: B+ trees for range queries and ordered scans; hash indexes for exact-match lookups; bitmap indexes for low-cardinality columns. The query planner selects the index type based on query patterns.
- **Google's Swiss Table (Abseil `flat_hash_map`)**: Open-addressing hash table optimized for cache performance with SIMD-accelerated probing — chosen over chaining for modern CPU architectures.

---

## 🏋️ Practice

### Warm-Up (5 min)
1. Your application reads 10,000 records by key and occasionally inserts a new one. Which data structure do you choose, and why?
2. A colleague proposes using a balanced BST for a collection that's built once and never modified. What simpler structure would you suggest?
3. Name a scenario where a linked list is genuinely better than a dynamic array. What specific property makes it win?

### Core Problems
1. **LRU Cache Design** — Design an LRU (Least Recently Used) cache with $O(1)$ `get` and $O(1)$ `put`. Identify which data structures you need to combine and why no single structure suffices. (Expected approach: hash map for $O(1)$ key lookup + doubly linked list for $O(1)$ eviction and reordering. Explain why a heap won't work here.)
2. **Selection Framework Application** — You're building a system that maintains a leaderboard of the top 100 scores out of millions of entries. Insertions are frequent; reads always request the top-K sorted. Compare at least three candidate structures (sorted array, balanced BST, min-heap) with complexity analysis for your workload, and select the best one with justification. (Expected approach: min-heap of size 100 — $O(\log 100)$ = $O(1)$ per insertion, $O(100 \log 100)$ to extract sorted top-K.)

### Challenge
**Multi-Dimensional Selection** — Design a data structure that supports the following operations efficiently: (1) insert a (key, value, priority) triple, (2) lookup by key in $O(1)$ average, (3) extract-min by priority in $O(\log n)$, and (4) delete by key in $O(\log n)$. No single standard structure handles all four. Propose a composite structure, analyze each operation's complexity, and discuss the space overhead.

---

*See also:* [[Abstract Data Types]] | [[Asymptotic Analysis and Big-O Notation]] | [[Memory Layout and Cache Performance]] | [[Pointer-Based vs Array-Based Structures]] | [[CS Data Structures/Hash-Based Structures/Hash Tables and Hash Functions|Hash Tables]] | **CS Algorithms:** [[CS Data Structures/Foundational Concepts/Data Structure Comparison and Selection|Algorithm Selection and Design]] | [[CS Algorithms/Sorting/Sorting Overview|Sorting Algorithm Selection]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-004 DLL plus hash map gives O1 LRU cache operations|DLL plus hash map gives O(1) LRU cache operations]]
- [[CS Data Structures/_chunks/chunk-ds-010 Hash tables achieve expected O1 via load factor management|Hash tables achieve expected O(1) via load-factor management]]
- [[CS Data Structures/_chunks/chunk-ds-061 Cache locality makes arrays 10-100x faster for iteration|Cache locality makes arrays much faster for iteration]]
- [[CS Data Structures/_chunks/chunk-ds-154 Fibonacci heaps rarely used despite optimal theory|Fibonacci heaps illustrate theory-vs-practice trade-offs]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
