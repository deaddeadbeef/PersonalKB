---
id: chunk-csa-034
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapters 2, 5, 6, 7"
topic: "analysis"
claim: "Dynamic programming solves problems with optimal substructure and overlapping subproblems by filling a memoisation table bottom-up, converting exponential recursion to polynomial time"
confidence: verified
supports:
  - "[[Dynamic Programming]]"
  - "[[LCS - Longest Common Subsequence]]"
  - "[[Edit Distance]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Dynamic programming solves problems with overlapping subproblems by memoising a table

## Context

Dynamic programming (DP) applies when a problem has two properties:

1. **Optimal substructure**: an optimal solution to the problem contains optimal solutions to subproblems. This allows a correct recurrence to be written.
2. **Overlapping subproblems**: the same subproblems arise repeatedly in the naive recursive decomposition. Simply memoising their answers avoids redundant computation.

**Bottom-up tabulation** (the standard form in Algorithms Unlocked): define the subproblem space, establish an ordering so that each subproblem is solved after its dependencies, fill a table in that order. The final answer is one table entry.

**Contrast with divide-and-conquer**: D&C also uses optimal substructure, but subproblems are *disjoint* — each piece of the input appears in exactly one subproblem. DP's gain comes specifically from reusing solutions to *shared* subproblems.

**Running time**: (number of distinct subproblems) × (time per subproblem), once overlap is eliminated. For 1D problems (e.g., rod cutting) this is typically Θ(n²); for 2D prefix-pair problems (e.g., LCS, edit distance) it is Θ(mn).

## Why It Matters

DP is one of the two most broadly applicable algorithm design paradigms (alongside greedy methods). Recognising whether a new problem has the two DP properties — and formulating the correct recurrence — is the core skill. The same pattern appears across sorting (bottom-up merge sort argument), string problems (LCS, edit distance), graph problems (Floyd-Warshall, DAG shortest paths), and combinatorial optimisation.

## QnA Seeds

- Q: What two properties must a problem have for dynamic programming to apply?
- Q: What is the difference between top-down memoisation and bottom-up tabulation?
- Q: How does dynamic programming differ from divide-and-conquer?
