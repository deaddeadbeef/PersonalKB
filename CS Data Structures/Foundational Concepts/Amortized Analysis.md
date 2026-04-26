---
tags: [cs-ds, foundational]
up: "[[Foundational Concepts Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
created: 2025-07-14
---
# Amortized Analysis

> **One-line summary**: Amortized analysis determines the average cost per operation over a worst-case sequence of operations, proving that expensive operations are rare enough to keep the per-operation average low.

## 🎯 Intuition
(2-min read. No jargon. Build mental picture.)

**The Core Idea:** Some operations are occasionally expensive, but if you spread the cost over many operations, each one is cheap on average — and this holds for *every* possible sequence, not just the "lucky" ones.

**Analogy:** Imagine you drive a car that costs $0.10/mile in gas — except every 1,000 miles, you need an oil change that costs $100. If you only look at the oil-change mile, driving looks absurdly expensive. But over 1,000 miles, you've spent $100 + $100 = $200 total, or $0.20/mile. The oil change is "amortized" across all the miles. Amortized analysis is like computing your *true cost per mile* rather than panicking at the mechanic's bill.

**Why It Matters:** Without amortized analysis, you'd reject some of the most efficient data structures in computing (dynamic arrays, hash tables, splay trees) because their occasional worst-case operations look scary. Amortized reasoning shows these structures are, in fact, excellent over sustained use.

---

## ⚙️ Core Mechanics
(Textbook level. Definitions, operations, complexity.)

### How It Works

Standard worst-case analysis can be overly pessimistic when a costly operation can only occur after many cheap ones. Amortized analysis addresses this by spreading the cost across the entire sequence. The key distinction: amortized cost is **not** average-case (which assumes a probability distribution over inputs). It is a **worst-case guarantee** over any valid sequence of *n* operations—no randomness assumed.

Three techniques formalize this:

1. **Aggregate method**: Compute the total cost of *n* operations and divide by *n*. Simplest but requires you to compute total cost directly.

2. **Accounting (banker's) method**: Assign each operation an amortized "charge." Cheap operations overpay and bank credit, which expensive operations later spend. The charges must ensure that accumulated credit never goes negative.

3. **Potential method**: Define a potential function Φ on the data structure's state. The amortized cost of operation *i* is its actual cost plus the change in potential: `â_i = c_i + Φ_i − Φ_{i−1}`. If Φ rises during cheap operations and drops during expensive ones, the amortized cost smooths out.

**Canonical example — dynamic array**: Appending to a full array triggers a doubling reallocation costing $O(n)$, but this happens only every *n* insertions. By the aggregate method, *n* insertions cost at most 1 + 2 + 4 + ... + n = $O(n)$ total for copying, plus $O(n)$ for the insertions themselves—giving **$O(1)$ amortized** per `push_back`.

**Splay trees**: Despite individual operations costing up to $O(n)$, any sequence of *m* operations on an *n*-node splay tree costs $O(m \log n)$ total, yielding **$O(\log n)$ amortized**.

### Key Operations

| Data Structure      | Operation      | Worst-Case | Amortized |
|---------------------|----------------|------------|-----------|
| Dynamic Array       | append         | $O(n)$       | $O(1)$      |
| Dynamic Array       | delete last    | $O(1)$       | $O(1)$      |
| Splay Tree          | search/insert  | $O(n)$       | $O(\log n)$  |
| Fibonacci Heap      | insert         | $O(1)$       | $O(1)$      |
| Fibonacci Heap      | decrease-key   | $O(n)$       | $O(1)$      |
| Fibonacci Heap      | extract-min    | $O(n)$       | $O(\log n)$  |
| Multipop Stack      | multipop(k)    | $O(k)$       | $O(1)$      |

### Key Facts

- Amortized ≠ average-case: amortized bounds hold for **every** sequence, with no probabilistic assumption.
- The aggregate method is simplest but requires you to compute total cost directly; it offers less insight into individual operations.
- The accounting method is intuitive: "save coins during cheap ops, spend them during expensive ops."
- The potential method is the most general and is required for complex proofs (e.g., splay trees, Fibonacci heaps).
- Dynamic array doubling gives $O(1)$ amortized append; growing by a fixed increment gives only $O(n)$ amortized.
- Fibonacci heaps achieve $O(1)$ amortized insert and decrease-key via the potential method, enabling faster Dijkstra's algorithm.
- Amortized analysis is **not suitable** when you need hard per-operation guarantees (e.g., real-time systems); in such cases, worst-case per-operation bounds are required.
- A common pitfall is confusing amortized $O(1)$ with "always $O(1)$"—individual operations can still spike.

---

## 🔬 Deep Dive
(Proofs, edge cases, real-world tradeoffs)

### Formal Properties

- **Potential method for dynamic arrays**: Let Φ = 2·size − capacity. After a normal append, size increases by 1 so Φ increases by 2; actual cost is 1; amortized cost = 1 + 2 = 3. On a doubling resize with old capacity *c*: actual cost = c + 1 (copy + insert), new capacity = 2c, new size = c + 1, so Φ drops from 2c − c = c to 2(c+1) − 2c = 2. Change in Φ = 2 − c. Amortized cost = (c + 1) + (2 − c) = 3. Every operation amortizes to exactly 3 — constant.
- **Telescoping sum guarantee**: For any sequence of *n* operations, Σ â_i = Σ c_i + Φ_n − Φ_0. If Φ_n ≥ Φ_0 (which we ensure by design), then total amortized cost ≥ total actual cost. The amortized bound is therefore a valid upper bound on real cost.
- **Splay tree access lemma**: Using Φ = Σ log(size of subtree rooted at each node), Sleator and Tarjan proved the $O(\log n)$ amortized bound, along with the *dynamic optimality conjecture* (still open).
- **Growth factor tradeoff**: Doubling (factor 2) wastes up to 50% memory; factor 1.5 (used by some `std::vector` implementations) reduces waste but increases amortized constant.

### Edge Cases and Pitfalls

- **Real-time systems**: Amortized $O(1)$ means *some* operations are $O(n)$. If your system has hard per-operation deadlines (audio processing, robotics), you need worst-case bounds. Use structures with deamortized guarantees (e.g., real-time queues, balanced BSTs instead of splay trees).
- **Shrinking policy**: Naïve halving at half-capacity causes thrashing if operations alternate between push and pop at the boundary. The standard fix: shrink at 1/4 capacity (or don't shrink at all).
- **Multi-structure interactions**: Amortized analysis applies to one data structure's operation sequence. If an expensive operation on structure A triggers an expensive operation on structure B, you cannot simply add their amortized costs — you need a combined analysis.
- **Memory allocation costs**: The $O(n)$ resize cost assumes allocation is $O(1)$. In practice, memory allocation itself can vary; large allocations may trigger OS page faults or garbage collection pauses not captured by the model.

### Real-World Usage

- **C++ `std::vector`**, **Java `ArrayList`**, **Python `list`**, **Go slices**: All use amortized doubling for dynamic growth. This is the single most common application of amortized analysis in production code.
- **Hash table resizing**: When load factor exceeds a threshold (e.g., 0.75), the table doubles and rehashes all entries. The $O(n)$ rehash amortizes to $O(1)$ per insertion over the table's lifetime.
- **Splay trees in caching**: Used in some kernel memory allocators and as the basis for link-cut trees in network flow algorithms.
- **Fibonacci heaps in Dijkstra's**: Achieve $O(V \log V + E)$ for shortest paths (vs. $O((V+E)$ log V) with binary heaps) — the improvement comes entirely from $O(1)$ amortized decrease-key.

---

## 🏋️ Practice

### Warm-Up (5 min)
1. A dynamic array performs 1,000 appends starting from capacity 1 with doubling. How many total element copies occur? What is the amortized cost per append?
2. Why is amortized $O(1)$ *not* the same as average-case $O(1)$? Describe a scenario where the distinction matters.
3. You have a "multipop" stack where `multipop(k)` pops up to *k* elements. Explain intuitively why a sequence of *n* pushes and multipops has $O(n)$ total cost.

### Core Problems
1. **Accounting Method for a Binary Counter** — A *k*-bit binary counter increments by flipping bits. The worst case flips all *k* bits. Use the accounting method to prove that *n* increments cost $O(n)$ total. (Expected approach: charge $2 per increment — $1 to flip the bit to 1, $1 saved to later flip it back to 0. Each bit flip from 1→0 is paid by saved credit.)
2. **Potential Method for Stack with Multipop** — Define a potential function for a stack supporting `push`, `pop`, and `multipop(k)`. Prove that all three operations have $O(1)$ amortized cost. (Expected approach: Φ = number of elements in the stack. Push increases Φ by 1; multipop(k) decreases Φ by k with actual cost k, so amortized cost = k + (−k) + constant = $O(1)$.)

### Challenge
**Design a Deamortized Dynamic Array** — Construct a dynamic array variant where *every* append is worst-case $O(1)$, not just amortized $O(1)$. Hint: incrementally copy elements to a new larger array in the background, a few per regular append, so the resize is complete before the old array fills up. Specify the copy schedule and prove the worst-case bound.

---

*See also:* [[Asymptotic Analysis and Big-O Notation]] | [[Dynamic Arrays]] | [[Splay Trees]] | [[Fibonacci Heaps]] | [[Abstract Data Types]] | **CS Algorithms:** [[Dijkstra's Algorithm]] | [[Graph Algorithm Complexity]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-120 Aggregate method proves amortized bounds by averaging|Aggregate method proves amortized bounds by averaging over sequences]]
- [[CS Data Structures/_chunks/chunk-ds-080 Accounting method assigns credits for amortized analysis|Accounting method assigns credits for amortized analysis]]
- [[CS Data Structures/_chunks/chunk-ds-079 Potential method proves amortized bounds|Potential method proves amortized bounds via virtual savings]]
- [[CS Data Structures/_chunks/chunk-ds-001 Dynamic arrays achieve amortized O1 append via geometric resizing|Dynamic arrays achieve amortized O(1) append via geometric resizing]]
- [[CS Data Structures/_chunks/chunk-ds-036 Fibonacci heaps achieve O1 amortized decrease-key|Fibonacci heaps achieve O(1) amortized decrease-key]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
