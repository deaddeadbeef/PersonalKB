---
tags:
  - csa
  - csa/study
up: "[[Algorithms Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Algorithm Complexity Cheatsheet

Compiled quick-reference for time and space complexities across all domains in the CS Algorithms knowledge base. Use for rapid review, algorithm selection, and exam preparation.

---

## Asymptotic Growth Ordering

From slowest to fastest growth — a $\Theta(f)$ algorithm is faster than a $\Theta(g)$ algorithm for large n when f appears earlier in this list:

```
1  <  lg n  <  √n  <  n  <  n lg n  <  n²  <  n³  <  2ⁿ  <  n!
```

*Remember:* n lg n is barely above linear. n² is a factor of lg n worse than n lg n. 2ⁿ and n! are qualitatively different — they grow faster than any polynomial.

---

## Master Theorem — Quick Reference

For divide-and-conquer recurrences of the form **T(n) = a·T(n/b) + f(n)** (a ≥ 1, b > 1):

Let **E = log_b(a)** (the watershed exponent).

| Case | Condition | Result | Intuition |
|------|-----------|--------|-----------|
| **1** | f(n) = $O(n^(E−ε)$) for some ε > 0 | T(n) = $\Theta(n^E)$ | Leaves dominate |
| **2** | f(n) = $\Theta(n^E)$ | T(n) = $\Theta(n^E · \lg n)$ | Every level contributes equally |
| **3** | f(n) = $\Omega(n^(E+ε)$) + regularity | T(n) = $\Theta(f(n)$) | Root dominates |

**Common recurrences:**

| Recurrence | a | b | E | Case | Result |
|-----------|---|---|---|------|--------|
| Merge sort: T(n) = 2T(n/2) + $\Theta(n)$ | 2 | 2 | 1 | 2 | **$\Theta(n \lg n)$** |
| Binary search: T(n) = T(n/2) + $\Theta(1)$ | 1 | 2 | 0 | 2 | **$\Theta(\lg n)$** |
| Strassen: T(n) = 7T(n/2) + $\Theta(n²)$ | 7 | 2 | lg₂7 ≈ 2.81 | 1 | **$\Theta(n^\lg 7)$ ≈ $\Theta(n^2.81)$** |
| T(n) = 8T(n/2) + $\Theta(n²)$ | 8 | 2 | 3 | 1 | **$\Theta(n³)$** |
| T(n) = 2T(n/2) + $\Theta(n²)$ | 2 | 2 | 1 | 3 | **$\Theta(n²)$** |
| T(n) = T(n−1) + $\Theta(1)$ | — | — | — | — | **$\Theta(n)$** (arithmetic; not MT) |

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Adaptive | Notes |
|-----------|------|---------|-------|-------|--------|---------|-------|
| **Merge sort** | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $O(n)$ | ✅ | ❌ | Optimal comparison sort |
| **Quicksort** | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n²)$ | $O(\lg n)$ avg | ❌ | ❌ | In-practice fastest; random pivot |
| **Insertion sort** | $\Theta(n)$ | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ | ✅ | ✅ | Best for nearly-sorted; $\Theta(inversions + n)$ |
| **Selection sort** | $\Theta(n²)$ | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ | ❌ | ❌ | Exactly n−1 writes; good for write-costly media |
| **Counting sort** | $\Theta(n+k)$ | $\Theta(n+k)$ | $\Theta(n+k)$ | $O(k)$ | ✅ | ❌ | Integer keys in [0, k]; not comparison-based |
| **Radix sort** | $\Theta(d(n+k)$) | $\Theta(d(n+k)$) | $\Theta(d(n+k)$) | $O(n+k)$ | ✅ | ❌ | d = digits; k = alphabet; subroutine must be stable |

**Lower bound:** Any comparison sort requires $\Omega(n \lg n)$ comparisons (decision tree: n! leaves → height ≥ lg(n!)). Merge sort achieves this — it is asymptotically optimal.

**Inversion relationship:** Insertion sort performs exactly one element shift per inversion. An array with I inversions → $\Theta(I + n)$ running time.

---

## Searching

| Algorithm | Time | Space | Requirement |
|-----------|------|-------|-------------|
| **Binary search** | $\Theta(\lg n)$ | $O(1)$ | Sorted array |
| **Linear search** | $\Theta(n)$ | $O(1)$ | None |
| **Hash table lookup** | $O(1)$ expected | $O(n)$ | Hash function; allows collisions |

**Lower bound:** Any comparison-based search in a sorted array requires $\Omega(\lg n)$ comparisons. Binary search is optimal.

---

## Graph Algorithms

n = vertices, m = edges. Assume adjacency list representation unless noted.

| Algorithm | Time | Space | Condition | Finds |
|-----------|------|-------|-----------|-------|
| **BFS / DFS** | $\Theta(n + m)$ | $O(n)$ | Any graph | Connectivity; tree |
| **Topological sort** (Kahn's) | $\Theta(n + m)$ | $O(n)$ | DAG only | Dependency order |
| **Dijkstra's** (binary heap) | $O((n + m)$ lg n) | $O(n)$ | Non-negative weights | SSSP |
| **Dijkstra's** (Fibonacci heap) | $O(m + n \lg n)$ | $O(n)$ | Non-negative weights | SSSP (theoretical) |
| **Bellman-Ford** | $\Theta(nm)$ | $O(n)$ | Any weights; no neg cycles for SSSP | SSSP; detects neg cycles |
| **Floyd-Warshall** | $\Theta(n³)$ | $\Theta(n²)$ | Any weights | APSP; detects neg cycles |
| **DAG shortest path** | $\Theta(n + m)$ | $O(n)$ | DAG only | SSSP (via topo order) |

**SSSP vs APSP selection guide:**

| Situation | Recommended algorithm |
|-----------|----------------------|
| Non-negative weights, single source | Dijkstra (binary heap) |
| Negative weights, single source | Bellman-Ford |
| DAG (any weights), single source | DAG relaxation in topo order |
| All pairs, dense graph | Floyd-Warshall |
| All pairs, sparse non-negative | Run Dijkstra from each vertex |

---

## String Algorithms (Dynamic Programming)

| Algorithm | Time | Space | Problem |
|-----------|------|-------|---------|
| **LCS** (Longest Common Subsequence) | $\Theta(mn)$ | $\Theta(mn)$ | Longest common subsequence of strings of length m, n |
| **Edit distance** (Levenshtein) | $\Theta(mn)$ | $\Theta(mn)$ | Min insert/delete/substitute operations |
| **KMP** string matching | $\Theta(n + p)$ | $O(p)$ | Find pattern of length p in text of length n |
| **Naïve string matching** | $O(nm)$ | $O(1)$ | Find pattern; no preprocessing |

**KMP advantage:** $O(n + p)$ vs naïve $O(nm)$ — the failure function precomputes a "restart table" that avoids re-examining text characters after a mismatch.

---

## Cryptography — Complexity Highlights

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| RSA key generation | expected $O(k² · M(k)$) | repeated Miller-Rabin tests to find two k-bit primes |
| RSA encrypt/decrypt | $O(k · M(k)$) | k-bit modulus; modular exponentiation; encryption often faster with small public exponent |
| Finite-field discrete log (best known) | sub-exponential | Number field sieve; basis of classical DH/DSA security (RSA security rests on integer factoring hardness, not discrete log) |
| Naïve modular exponentiation | $O(2^k · M(k)$) | k = exponent bits; repeated multiplication by the base is exponential in k; M(k) = cost of one modular multiply |
| Fast (square-and-multiply) | $O(k · M(k)$) | k squarings + ≤ k multiplications; one pass per exponent bit |

---

## Data Compression

| Algorithm | Time | Space | Compression type |
|-----------|------|-------|-----------------|
| **Huffman coding** | $O(n \lg n)$ | $O(n)$ | Optimal prefix-free variable-length code; greedy via priority queue |
| **Run-length encoding** | $O(n)$ | $O(1)$ extra | Lossless; best for long runs of identical symbols |
| **LZW** | $O(n)$ amortised | $O(dictionary)$ | Adaptive; no pre-known symbol frequencies needed |

**Huffman optimality:** Huffman produces the optimal prefix-free code — minimum expected bits per symbol. Proof: exchange argument shows any other assignment increases expected length.

---

## Complexity Theory — Key Results

| Result | Class | Status |
|--------|-------|--------|
| P ⊆ NP | — | True by definition |
| P = NP? | — | **Open problem** — the central question of complexity theory |
| NP-complete problems solvable in poly time | P | Only if P = NP |
| Halting problem | Undecidable | No algorithm can decide for all inputs |
| TSP, Satisfiability (SAT), Clique, Vertex Cover | NP-complete | Reduction chain from Cook-Levin theorem |
| Approximation ratio for vertex cover | 2 | Polynomial-time 2-approximation exists |
| Approximation for TSP (metric) | 3/2 (Christofides) | No PTAS unless P = NP |

**Complexity class ordering:**

```
P ⊆ NP ⊆ PSPACE ⊆ EXPTIME
```

Within NP: **NP-hard** = at least as hard as NP-complete; **NP-complete** = in NP AND NP-hard.

**Reduction principle:** To show problem X is NP-complete, show (1) X ∈ NP, and (2) some known NP-complete problem reduces to X in polynomial time. The canonical first NP-complete problem is **SAT** (Cook-Levin theorem). 3-SAT is NP-complete by reduction from SAT and serves as the common intermediate in most subsequent reduction chains.

---

## Dynamic Programming — Complexity Patterns

Most DP algorithms derive their complexity from the number of unique subproblems × work per subproblem:

| Problem | Subproblems | Per-subproblem | Total |
|---------|------------|----------------|-------|
| Fibonacci (memoised) | n | $O(1)$ | $O(n)$ |
| LCS(m, n) | m·n | $O(1)$ | $\Theta(mn)$ |
| Edit distance | m·n | $O(1)$ | $\Theta(mn)$ |
| Bellman-Ford | n·m (edges) | $O(1)$ per edge | $\Theta(nm)$ |
| Floyd-Warshall | n² pairs × n steps | $O(1)$ | $\Theta(n³)$ |
| Matrix chain (n matrices) | $O(n²)$ | $O(n)$ | $O(n³)$ |

---

## Quick-Pick Algorithm Selection

| Situation | Recommended |
|-----------|------------|
| Sort n comparable elements, worst-case guarantee | **Merge sort** $\Theta(n \lg n)$ |
| Sort n comparable elements, best average practice | **Quicksort** (random pivot) |
| Sort nearly-sorted array | **Insertion sort** $O(kn)$ for k-near-sorted |
| Sort n integers in [0, k], k = $O(n)$ | **Counting sort** $\Theta(n)$ |
| Search sorted array | **Binary search** $\Theta(\lg n)$ |
| SSSP, non-negative weights | **Dijkstra** $O((n+m)$ lg n) |
| SSSP, negative weights | **Bellman-Ford** $\Theta(nm)$ |
| All-pairs shortest paths | **Floyd-Warshall** $\Theta(n³)$ |
| Longest common subsequence | **LCS DP** $\Theta(mn)$ |
| Pattern match in text | **KMP** $\Theta(n+p)$ |
| Optimal variable-length code | **Huffman** $O(n \lg n)$ |
| Problem appears intractable | Check NP-completeness; consider approximation |

---

## Notes on Notation

- This vault uses **`lg`** for log base 2 throughout, following Cormen's *Algorithms Unlocked*.
- `n` = input size (number of elements, vertices, etc.) unless otherwise stated.
- `m` = number of edges in graph contexts.
- Θ = tight bound; O = upper bound; Ω = lower bound.
- Space complexity refers to auxiliary space beyond the input unless stated otherwise.

## References

- [[CS Algorithms/CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index]]
