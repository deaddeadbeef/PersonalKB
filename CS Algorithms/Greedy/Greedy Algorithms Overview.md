---
tags: [csa, csa/greedy]
up: "[[CS Algorithms/CS Algorithms|CS Algorithms Index]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Greedy Algorithms Overview

> **One-line summary**: Greedy algorithms build solutions incrementally, always choosing the locally optimal option at each step, and succeed when local optima guarantee a global optimum.

## 🎯 Intuition
**The Core Idea:** At every decision point, pick the choice that looks best right now and never reconsider.
**Analogy:** Imagine you're collecting coins scattered on a path — a greedy approach grabs the largest coin within reach at every step rather than planning a route to maximize the total haul.
**Why It Matters:** Greedy algorithms often run in $O(n \log n)$ or better, making them the first strategy to consider for optimization problems where the greedy-choice property and optimal substructure hold.

---

## ⚙️ Core Mechanics
### When Greedy Works
A problem is amenable to a greedy approach when two properties hold:
1. **Greedy-choice property** — a globally optimal solution can be assembled by making locally optimal choices.
2. **Optimal substructure** — an optimal solution to the problem contains optimal solutions to its sub-problems.

### General Strategy
1. Cast the problem as one where you make a choice and are left with a single sub-problem.
2. Prove the greedy choice is safe (always part of some optimal solution).
3. Show optimal substructure.
4. Implement: sort or organize input, iterate and choose greedily.

### Pseudocode (Generic Greedy)
```
function GreedySolve(candidates):
    solution = ∅
    sort candidates by greedy criterion
    for each c in candidates:
        if solution ∪ {c} is feasible:
            solution = solution ∪ {c}
    return solution
```

### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | $O(n)$ | $O(1)$ |
| Average | $O(n \log n)$ | $O(1)$–$O(n)$ |
| Worst | $O(n \log n)$ | $O(n)$ |

(Dominated by the initial sort in most formulations.)

### Key Facts
- Greedy does **not** work for all optimization problems — the 0/1 Knapsack is a classic counter-example.
- A correct greedy proof requires showing the greedy-choice property, not just intuition.
- Many scheduling, graph, and compression problems have elegant greedy solutions (Huffman coding, Dijkstra, Kruskal).

---

## 🔬 Deep Dive
### Proving Greedy Correctness
The standard technique is an **exchange argument**:
1. Assume an optimal solution O that differs from the greedy solution G.
2. Find the first point of divergence.
3. Show you can "exchange" the non-greedy choice in O for the greedy one without worsening the objective.
4. By induction, G is optimal.

### Edge Cases and Pitfalls
- **Ties in the greedy criterion** — breaking ties inconsistently can mask bugs in correctness proofs.
- **Problem variants that break greedy** — e.g., the 0/1 Knapsack looks similar to Fractional Knapsack but cannot be solved greedily.
- **Floating-point comparisons** when sorting by ratios (value/weight).

### Comparison with Alternatives
- **Dynamic Programming** — use DP when overlapping sub-problems exist and greedy fails (e.g., 0/1 Knapsack).
- **Backtracking** — use when the feasibility check is complex and you need to explore branches.
- Greedy is preferable whenever a valid proof exists because it's simpler and faster.

### Real-World Usage
- **Huffman coding** — used in gzip, JPEG, MP3.
- **Dijkstra's shortest path** — routing in maps and networking.
- **Job scheduling** — minimizing lateness in operating-system schedulers.
- **Prim's / Kruskal's MST** — network design, clustering.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does greedy fail for the 0/1 Knapsack but succeed for Fractional Knapsack?
2. State the two properties required for a greedy solution to be correct.
3. What proof technique is most commonly used for greedy correctness?

### Core Problems
1. **Activity Selection** — Given n activities with start/end times, select the maximum non-overlapping set. *Expected approach:* sort by finish time, greedily pick earliest-finishing compatible activity. → [[Activity Selection Problem]]
2. **Minimum number of coins** — Given denominations {1, 5, 10, 25}, make change for a value V using the fewest coins. *Expected approach:* always pick the largest denomination that fits.

### Challenge
- **Prove or disprove:** For an arbitrary set of coin denominations, the greedy coin-change algorithm always yields the minimum number of coins. Construct a counter-example and explain which property fails.

---

*See also:* [[Activity Selection Problem]] · [[Fractional Knapsack]] · [[CS Algorithms/Analysis/Dynamic Programming|Dynamic Programming Overview]] | **CS Data Structures:** [[Priority Queues and Heaps]] · [[CS Data Structures/Linear Structures/Arrays and Dynamic Arrays|Sorted Arrays]]

## References
-> [[CS Algorithms/Sources/Sources Index|Sources Index]]
