---
tags: [csa, csa/techniques]
up: "[[Techniques Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Amortized Analysis for Algorithms

> **One-line summary**: Amortized analysis determines the average cost per operation over a worst-case sequence of operations, proving that expensive operations are rare enough to keep the average cost low.

## 🎯 Intuition
**The Core Idea:** Some operations are occasionally expensive but make future operations cheaper — amortized analysis averages the cost fairly over the sequence.
**Analogy:** A prepaid highway toll. Most trips are free (you've pre-paid), but once a year you pay a large lump sum. The amortized cost per trip is the yearly fee divided by the number of trips — much less than the occasional big payment suggests.
**Why It Matters:** Without amortized analysis, data structures like dynamic arrays, splay trees, and Union-Find would appear to have poor worst-case bounds. Amortized analysis reveals their true efficiency.

---

## ⚙️ Core Mechanics
### Three Methods

#### 1. Aggregate Method
Compute the total cost of n operations, then divide by n.

**Example — Dynamic Array (vector push_back):**
- Most insertions cost $O(1)$.
- When the array is full, it doubles in size: copy all n elements → $O(n)$.
- Total cost for n insertions: 1 + 1 + 1 + 2 + 1 + 1 + 1 + 4 + … = n + (1 + 2 + 4 + … + n) ≤ n + 2n = 3n.
- Amortized cost per insertion: **3n / n = $O(1)$**.

#### 2. Accounting (Banker's) Method
Assign each operation an amortized cost (possibly higher than actual). Store the excess as "credit" on data structure elements. When an expensive operation occurs, pay with stored credits.

**Example — Dynamic Array:**
- Charge each insertion $3 (amortized cost).
- Actual cost for a normal insertion: $1. Save $2 as credit on the new element.
- When doubling occurs (n elements copied at $1 each): the n/2 newest elements each have $2 credit → total credits = $n, which covers the $n copy cost.

#### 3. Potential Method
Define a potential function Φ mapping the state of the data structure to a non-negative real number. The amortized cost of operation i is:
```
ĉᵢ = cᵢ + Φ(Dᵢ) − Φ(Dᵢ₋₁)
```
where cᵢ is the actual cost.

**Example — Dynamic Array:** Let Φ(D) = 2·size − capacity.
- Normal insertion: cᵢ = 1, Φ increases by 2 (size grows by 1). ĉ = 1 + 2 = 3.
- Doubling insertion: cᵢ = 1 + old_capacity. New capacity = 2 × old_capacity, size = old_capacity + 1.
  - Φ_after − Φ_before = (2(old_cap+1) − 2·old_cap) − (2·old_cap − old_cap) = 2 − old_cap.
  - ĉ = (1 + old_cap) + (2 − old_cap) = 3.
- Amortized cost is always **3 = $O(1)$**.

### Pseudocode — Dynamic Array Insert
```
function insert(arr, element):
    if arr.size == arr.capacity:
        new_arr = allocate(2 * arr.capacity)
        copy arr → new_arr             // O(n) actual cost
        arr = new_arr
    arr[arr.size] = element
    arr.size += 1
```

### Complexity

| Data Structure | Operation | Worst Case | Amortized |
|---------------|-----------|------------|-----------|
| Dynamic Array | push_back | $O(n)$ | $O(1)$ |
| Multipop Stack | multipop(k) | $O(k)$ | $O(1)$ |
| Binary Counter | increment | $O(\log n)$ | $O(1)$ |
| Union-Find | find + union | $O(\log n)$ | $O(α(n)$) ≈ $O(1)$ |
| Splay Tree | access | $O(n)$ | $O(\log n)$ |

### Key Facts
- Amortized analysis is about **worst-case sequences**, not probabilistic analysis. It guarantees performance — no randomness assumptions.
- The three methods always yield the same amortized bound; they differ in ease of application.
- Amortized ≠ average-case. Average-case assumes a distribution over inputs; amortized considers any sequence of operations.
- The potential method is the most general and powerful, but the aggregate method is simplest when applicable.

---

## 🔬 Deep Dive
### Multipop Stack Analysis
A stack supporting push, pop, and multipop(k) (pop k elements at once).
- **Aggregate:** In n operations, each element is pushed at most once and popped at most once. Total pops ≤ n. Total cost of all operations ≤ 2n. Amortized = $O(1)$.
- **Accounting:** Charge push $2 (pay $1 for the push, bank $1). When an element is popped (individually or via multipop), use the banked $1. Multipop of k costs k × $1, all paid by credits.
- **Potential:** Φ = number of elements on the stack. Each push: ĉ = 1 + 1 = 2. Each pop: ĉ = 1 − 1 = 0. Multipop(k): ĉ = k − k = 0.

### Binary Counter Increment
A binary counter represented as an array of bits, incremented by 1.
- Worst case: all bits flip (e.g., 0111...1 → 1000...0) → $O(\log n)$ flips.
- **Aggregate:** Bit 0 flips every increment, bit 1 flips every 2nd, bit 2 every 4th… Total flips for n increments: n + n/2 + n/4 + … < 2n. Amortized: $O(1)$.
- **Potential:** Φ = number of 1-bits. An increment that flips t bits from 1 to 0 and one bit from 0 to 1 has actual cost t + 1 and ΔΦ = 1 − t. Amortized: (t + 1) + (1 − t) = 2 = $O(1)$.

### Edge Cases and Pitfalls
- **Φ must be non-negative** (or at least Φ_n ≥ Φ_0) for the total amortized cost to be an upper bound on total actual cost.
- **Starting potential must be accounted for** — if Φ(D₀) > 0, subtract it or ensure Φ is defined so Φ(D₀) = 0.
- **Amortized bounds don't apply to single operations** — you can't claim a single dynamic-array insert is $O(1)$; only that any sequence of n inserts costs $O(n)$ total.
- **Confusing with average-case** — amortized is deterministic, not probabilistic.

### Comparison with Alternatives
- **Worst-case analysis** — overly pessimistic for data structures with occasional expensive operations.
- **Average-case analysis** — assumes a probability distribution; may not reflect adversarial inputs.
- **Smoothed analysis** — adds small random perturbations to worst-case inputs; useful for algorithms like Simplex.
- Amortized is the **right tool** when operations on a data structure have variable costs but the expensive ones are guaranteed to be infrequent by the structure's own invariants.

### Real-World Usage
- **std::vector / ArrayList** — the push_back / add guarantee of amortized $O(1)$ is why dynamic arrays are the default container.
- **Hash table resizing** — amortized $O(1)$ insert despite occasional $O(n)$ rehash.
- **Union-Find** — near-constant amortized time via path compression + union by rank underpins Kruskal's MST efficiency.
- **Splay trees** — used in caches and network routers; amortized $O(\log n)$ operations without explicit balancing.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between amortized analysis and average-case analysis?
2. For a dynamic array that triples (instead of doubles) its capacity, what is the amortized cost per insertion? Derive using the aggregate method.
3. In the accounting method for the multipop stack, how much do you charge per push?

### Core Problems
1. **Binary Counter** — Prove the amortized cost of increment is $O(1)$ using all three methods. Extend to decrement: does the $O(1)$ amortized bound still hold? (Hint: it doesn't — show a counter-example sequence.)
2. **Dynamic Table with Deletions** — A table that doubles on insert when full and halves when less than 1/4 full. Prove amortized $O(1)$ per operation using the potential Φ = |2·size − capacity|.

### Challenge
- **Splay Tree Amortized Analysis:** Using the potential function Φ = Σ log(size of subtree rooted at v), prove that the amortized cost of a splay operation is $O(\log n)$. This is the Access Lemma — work through it step by step.

---

*See also:* [[Two Pointers and Sliding Window]] · [[Divide and Conquer Overview]] · [[Greedy Algorithms Overview]] | **CS Data Structures:** [[Dynamic Arrays]] · [[Union-Find (Disjoint Sets)]] · [[Splay Trees]]

## References
-> [[Sources Index]]
