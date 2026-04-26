---
tags: [cs-ds, heaps]
up: "[[Heaps and Priority Queues Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Priority Queue ADT

> **One-line summary**: The priority queue is an abstract data type that supports inserting elements with associated priorities and extracting the element with the highest (or lowest) priority, with implementation choice critically affecting the performance of graph, scheduling, and compression algorithms.

## 🎯 Intuition
**The Core Idea:** A container where elements jump the line based on urgency, not arrival order — the most urgent item is always served first.
**Analogy:** An emergency room waiting area — patients aren't seen first-come-first-served; the one with the most critical condition is treated next, regardless of when they arrived.
**Why It Matters:** The priority queue ADT is the interface behind Dijkstra, Prim, Huffman, A*, OS schedulers, and event simulation. Choosing the right implementation (binary heap vs. Fibonacci heap vs. d-ary heap) can make or break an algorithm's practical speed.

---

## ⚙️ Core Mechanics
### How It Works
A **priority queue** is defined by its interface, not its implementation. The core operations are:
- **insert(key, priority)**: add an element.
- **extract-min** (or extract-max): remove and return the element with the smallest (or largest) priority.
- **peek**: return the minimum without removal.
- **decrease-key(handle, new_priority)** *(optional)*: lower the priority of an element already in the queue.
- **merge** *(optional)*: combine two priority queues into one.

The choice of underlying data structure determines the asymptotic cost of each operation:
- **Dijkstra's shortest path**: 1 insert and 1 extract-min per vertex, 1 decrease-key per edge relaxation. Binary heap → $O((V + E)$ log V); Fibonacci heap → $O(E + V \log V)$.
- **Prim's MST**: identical operation profile → identical improvement.
- **Huffman coding**: n − 1 extract-min and n − 1 insert → $O(n \log n)$ with any logarithmic heap.

Beyond graph algorithms, priority queues appear in event-driven simulation, OS schedulers, k-way merge, best-first search (A*, beam search), and median maintenance.

### Key Operations

| Implementation | Insert | Extract-min | Decrease-key | Merge | Peek |
|---|---|---|---|---|---|
| Unsorted array | $O(1)$ | $O(n)$ | $O(1)$* | $O(n)$ | $O(n)$ |
| Sorted array | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| Binary heap | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ | $O(1)$ |
| d-ary heap | $O(log_d n)$ | $O(d log_d n)$ | $O(log_d n)$ | $O(n)$ | $O(1)$ |
| Binomial heap | $O(\log n)$† | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$‡ |
| Fibonacci heap | $O(1)$* | $O(\log n)$* | $O(1)$* | $O(1)$* | $O(1)$ |

*Amortised. †$O(1)$ amortised with lazy insert. ‡$O(1)$ if min pointer maintained.

### Key Facts
- Core operations: insert, extract-min (or extract-max), peek; optional: decrease-key, merge.
- Decrease-key cost dominates the complexity of Dijkstra and Prim on dense graphs.
- An unsorted array gives $O(1)$ insert but $O(n)$ extract-min; a sorted array reverses this.
- Binary heap: $O(\log n)$ insert, extract-min, and decrease-key — most common practical choice.
- Fibonacci heap: $O(1)$ amortised insert, merge, and decrease-key; $O(\log n)$ extract-min.
- Binomial heap: $O(\log n)$ merge, insert, and extract-min; useful when merges are frequent.
- Priority queues are required by Dijkstra, Prim, Huffman, A*, event simulation, and k-way merge.
- In practice, binary heaps or d-ary heaps outperform Fibonacci heaps due to lower constants and better cache behaviour.

---

## 🔬 Deep Dive
### Formal Properties / Proofs
- **Lower bound**: comparison-based priority queues require $\Omega(\log n)$ for either insert or extract-min (otherwise sorting could be done in o(n log n) via n inserts + n extracts).
- **Dijkstra's complexity derivation**: V extract-min at $O(\log V)$ each + E decrease-key at $O(\log V)$ each = $O((V + E)$ log V) with a binary heap. With Fibonacci heap, decrease-key drops to $O(1)$ amortised → $O(E + V \log V)$.
- **Equivalence to sorting**: a priority queue that achieves $O(1)$ insert and $O(1)$ extract-min would imply $O(n)$ comparison sorting, violating the $\Omega(n \log n)$ bound.

### Edge Cases and Pitfalls
- **Decrease-key without handles**: if the implementation doesn't expose element handles (e.g., Python's `heapq`), decrease-key requires an $O(n)$ search or a separate index map.
- **Max-heap vs. min-heap confusion**: many libraries default to one variant; wrapping keys with negation is the standard workaround.
- **Empty-queue extract**: attempting extract-min on an empty queue — guard with a size check or exception.
- **Merge cost**: binary heaps require $O(n)$ to merge; if merges are frequent, switch to binomial or Fibonacci heaps.

### Real-World Usage
- **Dijkstra's algorithm**: the canonical priority-queue client; heap choice determines practical speed.
- **Prim's MST**: identical pattern to Dijkstra.
- **Huffman coding**: repeated extract-min + insert to build the optimal prefix-free code tree.
- **A* search**: priority queue keyed by f(n) = g(n) + h(n); drives game AI pathfinding and robot navigation.
- **OS process scheduling**: priority-based schedulers (e.g., multi-level feedback queues) use heap-backed priority queues.
- **Event-driven simulation**: discrete-event simulators (network emulators, physics engines) extract the next-timestamp event.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Which priority-queue implementation would you choose for an algorithm that performs 1,000 inserts, 10 extract-mins, and no decrease-keys? Why?
2. True or false: a Fibonacci heap is always faster than a binary heap for Dijkstra's algorithm in practice.
3. If you need to merge two priority queues frequently, which implementation should you avoid? Why?

### Core Problems
1. **Last Stone Weight** (LeetCode 1046): model the problem as a max-priority-queue. Extract the two heaviest stones, smash them, and re-insert the remainder. Analyse the total number of operations.
2. **Task Scheduler** (LeetCode 621): use a max-heap to greedily pick the most-frequent task first, combined with a cooldown queue. Prove the greedy strategy is optimal.

### Challenge
1. **Design a priority queue with $O(1)$ peek, $O(\log n)$ insert, $O(\log n)$ extract-min, AND $O(1)$ merge**: explain why this combination is impossible with a single comparison-based structure. Then design a two-structure hybrid (e.g., leftist heap or skew heap) that achieves $O(1)$ merge and $O(\log n)$ for the rest. Prove the bounds.

---

*See also:* [[Binary Heaps]] | [[Binomial Heaps]] | [[Fibonacci Heaps]] | [[Heap Applications and d-ary Heaps]] | **CS Algorithms:** [[Dijkstra's Algorithm]], [[Huffman Coding]]

## Supporting Chunks

*Pending chunk extraction.*

## References

→ Sources Index
