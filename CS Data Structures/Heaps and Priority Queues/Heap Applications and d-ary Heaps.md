---
tags: [cs-ds, heaps]
up: "[[Heaps and Priority Queues Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Heap Applications and d-ary Heaps

> **One-line summary**: d-ary heaps generalise binary heaps by allowing each node up to *d* children, trading shallower height for wider comparisons, while heap-based applications — heapsort, k-way merge, median maintenance, top-k selection, and event simulation — demonstrate the priority queue's central role across computing.

## 🎯 Intuition
**The Core Idea:** Widen the heap to make "going up" faster (fewer levels) at the cost of "going down" being slower (more children to compare) — then pick the branching factor that matches your workload.
**Analogy:** A company org chart — a flat org (high *d*) means promotions (decrease-key) are fast because there are fewer layers, but finding the weakest performer at each level (extract-min) requires comparing more direct reports.
**Why It Matters:** d-ary heaps with d = 4 often beat binary heaps in practice due to cache-line alignment, and heap applications (heapsort, k-way merge, median, top-k, event simulation) are ubiquitous interview and systems-design patterns.

---

## ⚙️ Core Mechanics
### How It Works
A **d-ary heap** is a complete d-ary tree stored implicitly in an array (generalising the binary heap where d = 2). The node at index *i* (zero-based) has children at indices di + 1 through di + d and its parent at ⌊(i − 1) / d⌋.

**Trade-off**: increasing *d* reduces tree height to log_d n, which directly benefits **decrease-key** ($O(log_d n)$). However, **extract-min** must compare up to *d* children at each level during sift-down, costing $O(d · log_d n)$. The optimal *d* depends on the operation mix — for Dijkstra on dense graphs, d = E/V balances the two.

**Heap-based applications:**
- **Heapsort**: build a max-heap in $O(n)$, repeatedly extract the maximum → $O(n \log n)$ in-place, not stable.
- **k-way merge**: min-heap of *k* stream heads; extract global minimum, replace from same stream → $O(n \log k)$.
- **Median maintenance**: max-heap (lower half) + min-heap (upper half), rebalance after each insertion → $O(\log n)$ per element.
- **Top-k selection**: min-heap of size *k*; for each incoming element, replace root if larger → $O(n \log k)$.
- **Event-driven simulation**: priority queue keyed by timestamp; extract next event in $O(\log n)$, insert consequences.

### Key Operations

| Application / Operation | Time | Space | Notes |
|---|---|---|---|
| d-ary insert (sift-up) | $O(log_d n)$ | $O(1)$ | Shallower than binary for d > 2 |
| d-ary extract-min (sift-down) | $O(d log_d n)$ | $O(1)$ | d comparisons per level |
| d-ary decrease-key | $O(log_d n)$ | $O(1)$ | Key advantage for large d |
| Heapsort | $O(n \log n)$ | $O(1)$ | In-place; build-heap $O(n)$ |
| k-way merge | $O(n \log k)$ | $O(k)$ | Heap of k stream heads |
| Median maintenance | $O(n \log n)$ total | $O(n)$ | Two heaps of ~n/2 elements |
| Top-k selection | $O(n \log k)$ | $O(k)$ | Min-heap of size k |
| Event simulation (per event) | $O(\log n)$ | $O(n)$ | Insert + extract-min |

### Key Facts
- A d-ary heap has height ⌈log_d n⌉; children of index *i*: di+1 … di+d.
- Decrease-key benefits from shallower height: $O(log_d n)$; extract-min costs $O(d log_d n)$.
- Optimal *d* for Dijkstra: d = E/V, yielding $O(E log_{E/V} V)$.
- d = 4 is a common practical sweet spot, aligning node width with cache-line size.
- Heapsort: in-place, $O(n \log n)$ worst-case, not stable, poor cache locality.
- k-way merge via min-heap: $O(n \log k)$ for *n* total elements across *k* sorted streams.
- Median maintenance: max-heap (lower half) + min-heap (upper half), $O(\log n)$ per insertion.
- Top-k via size-k min-heap: $O(n \log k)$ for streaming selection.

---

## 🔬 Deep Dive
### Formal Properties / Proofs
- **Optimal d derivation**: Dijkstra performs $O(V)$ extract-min operations at cost $O(d log_d V)$ each, and $O(E)$ decrease-key operations at cost $O(log_d V)$ each. Total = $O(V · d log_d V + E · log_d V)$. Minimising over *d* gives d = max(2, E/V), yielding $O(E log_{E/V} V)$.
- **Build-heap for d-ary**: same bottom-up analysis as binary; total work is $O(n · Σ (h · d^h)$ / $d^{h+1}$) = $O(n · d / (d − 1)$²) = $O(n)$ for constant *d*.
- **k-way merge correctness**: the heap invariant ensures the global minimum is always at the root; replacing it with the next element from the same stream and sifting down costs $O(\log k)$.

### Edge Cases and Pitfalls
- **d = 1 degeneracy**: a 1-ary heap is a sorted linked list — extract-min is $O(1)$ but insert is $O(n)$. Always use d ≥ 2.
- **Heapsort cache misses**: despite $O(n \log n)$ guarantees, the access pattern in heapsort jumps between parent and child indices, causing ~2× more cache misses than mergesort.
- **Top-k on tiny k**: when k is very small (e.g., k = 1), a simple linear scan beats a heap.
- **Median maintenance rebalance**: if the two heaps differ in size by more than 1, move the root of the larger heap to the smaller.

### Real-World Usage
- **Dijkstra's algorithm**: d-ary heap with d = 4 is the fastest practical implementation for most graph densities.
- **External sorting**: k-way merge with a heap is the standard pattern in database engines (e.g., PostgreSQL merge joins).
- **Stream processing**: top-k and median maintenance power real-time analytics dashboards.
- **Game engines / physics engines**: event-driven simulation queues schedule collision checks and animation frames.
- **Operating systems**: timer wheels and schedulers often use 4-ary or 8-ary heaps for cache efficiency.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. For a 4-ary heap with 15 elements, what is the height of the tree?
2. Given a stream of integers `[5, 15, 1, 3, 8, 7, 2]`, show the state of a size-3 min-heap used for top-3 selection after processing each element.
3. Why is heapsort not stable? Give a concrete 3-element counterexample.

### Core Problems
1. **Running Median** (LeetCode 295): implement `addNum(int num)` and `findMedian()` using two heaps. Analyse the time complexity per operation.
2. **k-way Merge of Sorted Arrays**: given *k* sorted arrays of varying lengths totalling *n* elements, merge them into a single sorted array. Implement and prove $O(n \log k)$.

### Challenge
1. **Optimal d for Dijkstra (empirical)**: implement Dijkstra's algorithm with a configurable d-ary heap. Run it on random sparse (E ≈ 2V) and dense (E ≈ V²) graphs for V = 10,000. Measure wall-clock time for d ∈ {2, 4, 8, 16, 32}. Plot results and explain why the empirical optimum may differ from the theoretical d = E/V.

---

*See also:* [[Binary Heaps]] | [[Priority Queue ADT]] | [[Fibonacci Heaps]] | [[Binomial Heaps]] | **CS Algorithms:** [[Dijkstra's Algorithm]], [[Huffman Coding]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-104 D-ary heaps optimize for cache and reduce height|D-ary heaps optimize for cache and reduce height]]
- [[CS Data Structures/_chunks/chunk-ds-088 Heapsort is On log n worst-case and in-place|Heapsort is O(n log n) worst-case and in-place]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
