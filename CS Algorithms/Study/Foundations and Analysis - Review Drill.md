---
tags:
  - csa
  - csa/study
  - csa/analysis
up: "[[Algorithms Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Foundations and Analysis — Review Drill

Active-recall drill for the core vocabulary, proof machinery, and analysis tools used throughout CS Algorithms.

**Canon pages:** [[Algorithm Definition]] · [[Asymptotic Notation]] · [[Loop Invariant]] · [[Comparison Sort Lower Bound]] · [[Dynamic Programming]] · [[Recurrence Relations]] · [[Master Theorem]]

---

## How to Use

Answer each question aloud or in writing before revealing the answer. The goal is retrieval, not re-reading.

---

## Core Recall

**Algorithms and Correctness**

Q: What three properties does a well-defined algorithm require?
A: Input specification, a finite sequence of unambiguous steps, and guaranteed termination that produces correct output.

Q: What is the correctness spectrum for algorithms, and where do exact vs approximation algorithms sit?
A: Exact algorithms always return the optimal solution. Approximation algorithms return a solution within a provable factor of optimal and run in polynomial time. Heuristics have no formal guarantee.

Q: What does the RAM model assume, and why does it matter for analysis?
A: Each basic operation (comparison, arithmetic, memory access) costs unit time. It abstracts away hardware specifics and lets asymptotic analysis compare algorithms independently of constant factors.

---

**Asymptotic Notation**

Q: Define $\Theta(f(n)$) precisely.
A: T(n) = $\Theta(f(n)$) iff there exist positive constants c₁, c₂, n₀ such that c₁·f(n) ≤ T(n) ≤ c₂·f(n) for all n ≥ n₀. Θ is a tight bound — both upper and lower.

Q: What is the difference between $O(f(n)$) and $\Theta(f(n)$)?
A: O is an upper bound (T(n) ≤ c·f(n) for large n). Θ is a tight bound — both O and Ω. Saying an algorithm is $O(n²)$ does not mean it *is* $\Theta(n²)$; it could be $\Theta(n)$.

Q: State the asymptotic hierarchy from slowest to fastest growth.
A: 1 < lg n < n < n lg n < n² < n³ < 2ⁿ < n!

Q: Why do constants and lower-order terms get dropped in asymptotic notation?
A: For sufficiently large n, the dominant term dwarfs constants and lower-order terms. Asymptotic analysis compares growth rates, not absolute values for specific hardware.

Q: When is algorithm choice more important than hardware speed?
A: When n is large enough that the difference in growth rate dominates. An $O(n \lg n)$ algorithm will outperform an $O(n²)$ algorithm on fast hardware once n crosses a crossover point that depends only on the constants.

---

**Loop Invariants**

Q: What are the three parts of a loop invariant proof?
A: **Initialization** — the invariant holds before the first iteration. **Maintenance** — if the invariant holds before iteration i, it holds before iteration i+1. **Termination** — when the loop ends, the invariant (combined with the termination condition) gives the desired result.

Q: What does a *strong* loop invariant couple together?
A: The loop variable (e.g., i) and a measurable correctness property of the data structure (e.g., "A[1..i] is sorted"). This prevents the invariant from being trivially true without saying anything useful.

Q: For insertion sort, state the loop invariant.
A: After iteration i, A[1..i] is a sorted permutation of the original A[1..i].

---

**Recurrence Relations and the Master Theorem**

Q: Write the general divide-and-conquer recurrence.
A: T(n) = a·T(n/b) + f(n), where a ≥ 1 is the number of subproblems, b > 1 is the size-reduction factor, and f(n) is the cost to divide/combine.

Q: What is the Master Theorem's "watershed exponent"?
A: E = log_b(a). It represents the "rate" at which work at the leaves grows relative to the work at the root.

Q: State the three Master Theorem cases and their results.
A: Let E = log_b(a).
- **Case 1**: f(n) = $O(n^(E−ε)$) for some ε > 0 → T(n) = $\Theta(n^E)$. Leaves dominate.
- **Case 2**: f(n) = $\Theta(n^E)$ → T(n) = $\Theta(n^E · \lg n)$. Equal work at every level.
- **Case 3**: f(n) = $\Omega(n^(E+ε)$) for some ε > 0 and regularity condition → T(n) = $\Theta(f(n)$). Root dominates.

Q: Apply the Master Theorem to merge sort: T(n) = 2T(n/2) + $\Theta(n)$.
A: a=2, b=2, E=log₂(2)=1. f(n)=$\Theta(n)$=$\Theta(n¹)$. Case 2 applies → T(n) = $\Theta(n \lg n)$.

Q: Apply the Master Theorem to binary search: T(n) = T(n/2) + $\Theta(1)$.
A: a=1, b=2, E=log₂(1)=0. f(n)=$\Theta(1)$=$\Theta(n⁰)$. Case 2 applies → T(n) = $\Theta(\lg n)$.

Q: Apply the Master Theorem to T(n) = 8T(n/2) + $\Theta(n²)$.
A: a=8, b=2, E=log₂(8)=3. f(n)=$\Theta(n²)$. Since 2 < 3, f(n)=$O(n^(3−1)$). Case 1 → T(n) = $\Theta(n³)$.

---

**Dynamic Programming**

Q: What two structural properties must a problem have for dynamic programming to apply?
A: **Optimal substructure** — an optimal solution contains optimal solutions to its sub-problems. **Overlapping subproblems** — the same sub-problem recurs multiple times in the recursion tree.

Q: What is the difference between top-down (memoization) and bottom-up (tabulation) DP?
A: Top-down: recursive; cache results to avoid recomputation. Bottom-up: iterative; fill a table in dependency order so each entry is available when needed. Bottom-up avoids recursion overhead and is often more cache-friendly.

Q: Give an example of a DP problem and state its sub-problem definition.
A: **Longest Common Subsequence**: LCS(i, j) = length of LCS of A[1..i] and B[1..j]. Recurrence: if A[i]=B[j], LCS(i,j) = LCS(i−1,j−1)+1; else max(LCS(i−1,j), LCS(i,j−1)). See [[LCS - Longest Common Subsequence]].

---

**Comparison Sort Lower Bound**

Q: What is the decision tree lower bound for comparison sorts, and what is the intuition?
A: Any comparison sort must make $\Omega(n \lg n)$ comparisons in the worst case. Intuition: the decision tree has at least n! leaves (one per permutation). A binary tree with n! leaves has height ≥ lg(n!) = $\Omega(n \lg n)$.

Q: What is the exact expansion of lg(n!)?
A: lg(n!) = n lg n − $O(n)$. More precisely, n lg n − n/ln 2 + $O(\lg n)$. This means the lower bound is tight to the leading term — no comparison sort can do better than n lg n − $O(n)$ comparisons.

Q: Which comparison sort achieves the lower bound, and what does this mean?
A: Merge sort achieves $\Theta(n \lg n)$ in all cases. It is leading-coefficient optimal — you cannot improve the n lg n term with any comparison sort.

Q: Does the decision tree argument apply to searching? What does it give?
A: Yes. Searching in a sorted array needs ≥ n+1 leaves → height ≥ lg(n+1) = $\Omega(\lg n)$. Binary search achieves $O(\lg n)$ and is therefore optimal.

---

## Compare and Contrast

**O vs Θ vs Ω**

| Notation | Meaning | Typical use |
|----------|---------|-------------|
| $O(f(n)$) | Upper bound (≤ c·f(n) for large n) | Worst-case guarantee |
| $\Omega(f(n)$) | Lower bound (≥ c·f(n) for large n) | Best case or impossibility proof |
| $\Theta(f(n)$) | Tight bound (both O and Ω) | Exact characterisation |

**Divide-and-Conquer vs Dynamic Programming**

| Property | D&C | DP |
|----------|-----|---|
| Subproblem overlap | Independent subproblems | Overlapping subproblems |
| Caching | Not needed | Essential |
| Order | Top-down | Usually bottom-up |
| Examples | Merge sort, binary search | LCS, edit distance, shortest paths |

**Memoization vs Tabulation**

| Aspect | Memoization | Tabulation |
|--------|------------|-----------|
| Direction | Top-down | Bottom-up |
| Recursion | Yes | No |
| Space | Can skip unreachable states | Fills entire table |
| Overhead | Call-stack depth | Iteration order must respect dependencies |

---

## Common Mistakes

1. **O and Θ confusion** — "insertion sort is $O(n²)$" is correct but weak; "insertion sort is $\Theta(n²)$ in the worst case" is more precise. Saying "binary search is $\Theta(n)$" is false.

2. **Master Theorem case 2 gap** — the $\Theta(n^E · \lg n)$ result surprises people. Remember: when f(n) and $n^{E}$ are *equal* in growth, every level of the recursion contributes equally and you accumulate a log factor.

3. **Loop invariant termination step** — most proofs write initialization and maintenance but skip termination, which is where the invariant actually proves the algorithm's result.

4. **DP requires optimal substructure** — DP fails if locally optimal sub-problem solutions do not combine into globally optimal solutions. Always verify optimal substructure before applying DP.

5. **Lower bound scope** — the $\Omega(n \lg n)$ comparison-sort lower bound applies only to comparison sorts. Counting sort and radix sort bypass it by exploiting non-comparison structure.

---

## Links Back

- [[Algorithm Definition]] — correctness spectrum, RAM model
- [[Asymptotic Notation]] — formal definitions, hierarchy
- [[Loop Invariant]] — initialization/maintenance/termination structure
- [[Comparison Sort Lower Bound]] — decision tree argument, exact lg(n!) bound
- [[Dynamic Programming]] — optimal substructure, overlapping subproblems
- [[Recurrence Relations]] — divide-and-conquer recurrences
- [[Master Theorem]] — three-case reference card

## References

- [[CS Algorithms/CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index]]
