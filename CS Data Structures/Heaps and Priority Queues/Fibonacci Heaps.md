---
tags: [cs-ds, heaps]
up: "[[Heaps and Priority Queues Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Fibonacci Heaps

> **One-line summary**: Fibonacci heaps achieve $O(1)$ amortised insert, merge, and decrease-key through lazy consolidation and cascading cuts, providing the theoretically optimal priority-queue bounds that underpin the best-known complexities for Dijkstra's and Prim's algorithms.

## 🎯 Intuition
**The Core Idea:** Be as lazy as possible — don't clean up the heap structure until you absolutely have to (during extract-min), and when cutting nodes, limit the damage with a "two-strikes" rule.
**Analogy:** A messy desk where you toss new papers onto the pile ($O(1)$ insert) and only sort through everything when the boss asks for the most urgent document (extract-min triggers consolidation).
**Why It Matters:** Fibonacci heaps give Dijkstra's algorithm its best-known complexity of $O(E + V \log V)$, making them the theoretical gold standard against which all priority queues are measured.

---

## ⚙️ Core Mechanics
### How It Works
Introduced by Fredman and Tarjan (1987), the **Fibonacci heap** is a collection of heap-ordered trees with extremely relaxed structural constraints. Unlike binomial heaps, Fibonacci heaps impose **no limit** on the number of trees of each degree, and trees need not be binomial in shape.

**Key operations:**
- **Insert**: add a new single-node tree to the root list and update the minimum pointer — $O(1)$ actual and amortised.
- **Merge**: concatenate the root lists of two heaps and pick the smaller minimum — $O(1)$.
- **Extract-min**: remove the minimum root, promote its children to the root list, then perform **consolidation** — iterate over all root-list trees, linking trees of equal degree until no two trees share the same degree. Amortised $O(\log n)$.
- **Decrease-key**: cut the decreased node from its parent and add it to the root list — $O(1)$ actual work. **Cascading cuts** prevent trees from becoming too unbalanced: if a node loses a second child (tracked by a *mark* bit), it is also cut from its parent, and the process repeats upward. Amortised $O(1)$.

A key result is that the maximum degree of any node is $O(\log n)$, because a node of degree *k* heads a subtree of at least F_{k+2} ≥ $\varphi^{k}$ nodes (where φ is the golden ratio) — hence the name "Fibonacci heap."

### Key Operations

| Operation | Actual (worst) | Amortised | Notes |
|---|---|---|---|
| Find-min | $O(1)$ | $O(1)$ | Direct pointer to minimum root |
| Insert | $O(1)$ | $O(1)$ | Add node to root list |
| Merge | $O(1)$ | $O(1)$ | Concatenate root lists |
| Extract-min | $O(n)$ | $O(\log n)$ | Consolidation phase links root trees |
| Decrease-key | $O(\log n)$* | $O(1)$ | *Cascading cuts may fire $O(\log n)$ times |
| Delete | $O(n)$ | $O(\log n)$ | Decrease-key to −∞, then extract-min |

### Key Facts
- Introduced by Fredman and Tarjan (1987) to optimise graph algorithms.
- Insert, merge, and decrease-key are all $O(1)$ amortised; extract-min is $O(\log n)$ amortised.
- Lazy consolidation defers tree linking until extract-min, batching the structural work.
- Maximum node degree is $O(\log n)$, bounded via Fibonacci number analysis (hence the name).
- Cascading cuts ensure decrease-key remains $O(1)$ amortised; marked nodes track child loss.
- Dijkstra with Fibonacci heap: $O(E + V \log V)$; Prim with Fibonacci heap: $O(E + V \log V)$.
- Pointer-heavy structure and poor cache locality make it slower in practice than d-ary or pairing heaps.
- Pairing heaps, rank-pairing heaps, and strict Fibonacci heaps are practical or theoretical successors.

---

## 🔬 Deep Dive
### Formal Properties / Proofs
- **Potential function**: Φ = t + 2m, where *t* = number of root-list trees and *m* = number of marked nodes. Insert increases Φ by 1 (amortised cost $O(1)$). Extract-min reduces root-list trees during consolidation; the potential drop pays for the linking work. Decrease-key with *c* cascading cuts costs $O(c)$ actual work but decreases Φ by at least c − 2, giving $O(1)$ amortised.
- **Degree bound**: a node of degree *k* has had *k* children linked to it over time; cascading cuts guarantee each child was of degree ≥ i − 2 when linked as the *i*-th child. By induction, the subtree has ≥ F_{k+2} nodes, so k = $O(log_φ n)$ = $O(\log n)$.
- **Why Fibonacci numbers**: the minimum subtree sizes follow the Fibonacci sequence because of the "lose at most one child" invariant from cascading cuts.

### Edge Cases and Pitfalls
- **Constant factors**: pointer manipulation overhead makes Fibonacci heaps 2–10× slower than binary heaps for typical input sizes.
- **Cache locality**: root-list and child-list traversals scatter across memory, causing frequent cache misses.
- **Implementation complexity**: correct handling of mark bits, cascading cuts, and circular doubly-linked lists is error-prone.
- **Worst-case extract-min**: $O(n)$ actual time when the root list has degenerated (all singletons) — the amortised bound holds only over sequences.

### Real-World Usage
- **Dijkstra's algorithm**: Fibonacci heap gives the theoretically optimal $O(E + V \log V)$.
- **Prim's MST**: identical operation profile to Dijkstra, same asymptotic benefit.
- **Theoretical benchmark**: even when practitioners use simpler heaps, Fibonacci heaps set the lower bar for priority-queue design.
- **Practical alternatives**: pairing heaps (simpler, competitive empirically), rank-pairing heaps, Brodal queues (worst-case optimal), strict Fibonacci heaps.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can't you simply unmark all nodes instead of using cascading cuts? What invariant would break?
2. What is the maximum degree of any node in a Fibonacci heap of 100 elements? (Use the φ bound.)
3. True or false: merging two Fibonacci heaps of size *n* each takes $O(n)$ time.

### Core Problems
1. **Amortised analysis**: using the potential Φ = t + 2m, prove that a sequence of *n* inserts followed by one extract-min costs $O(n)$ total. Show the potential bookkeeping step by step.
2. **Dijkstra comparison**: implement Dijkstra's algorithm using (a) a binary heap and (b) a simulated Fibonacci heap (e.g., using a library). Compare actual running times on a dense random graph with V = 10,000 and E = V². Explain any discrepancy between theory and practice.

### Challenge
1. **Design a strict Fibonacci heap**: starting from the standard Fibonacci heap, redesign the data structure so that extract-min and decrease-key both run in $O(\log n)$ and $O(1)$ **worst-case** (not just amortised). Outline the key modifications (eager consolidation, deficit counters). Compare trade-offs with the original lazy design.

---

*See also:* [[Binomial Heaps]] | [[Priority Queue ADT]] | [[Binary Heaps]] | [[Heap Applications and d-ary Heaps]] | **CS Algorithms:** [[Dijkstra's Algorithm]], [[Huffman Coding]]

## Supporting Chunks

*Pending chunk extraction.*

## References

→ Sources Index
