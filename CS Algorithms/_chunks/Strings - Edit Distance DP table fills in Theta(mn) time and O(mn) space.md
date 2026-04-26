---
id: chunk-csa-029
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 7"
topic: "strings"
claim: "Filling the edit distance DP table row by row takes Θ(mn) time and O(mn) space; the optimal edit sequence is recovered by backtracking through the table"
confidence: verified
supports:
  - "[[Edit Distance]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — Edit Distance DP table fills in Θ(mn) time and O(mn) space

## Context

The (m+1) × (n+1) cost table is filled left-to-right, top-to-bottom. Each cell requires O(1) work (evaluate at most three cases, take the minimum). Total cells: (m+1)(n+1) = Θ(mn). Space: Θ(mn) to store the full table; this can be reduced to O(n) if only the final cost is needed (keep two rows), but backtracking then requires re-computation.

**Backtracking** to recover the edit sequence: start at cost[m, n] and at each cell follow the pointer recorded during fill (which case was optimal). This traces the sequence of operations in O(m+n) time.

For spell-checking or diff tools, the full table is usually stored so the edit sequence can be retrieved. For applications that only need the distance (e.g., database similarity ranking), the two-row optimisation is practical.

## Why It Matters

The Θ(mn) complexity directly bounds the practical utility: on strings of length 1000 each, the table has one million entries — feasible. On genome sequences of length 10⁶, a naïve implementation is 10¹² entries — infeasible without approximations or banded DP. Knowing the complexity governs which application contexts are tractable.

## QnA Seeds

- Q: What is the time and space complexity of the edit distance DP algorithm, and why?
- Q: How do you recover the actual sequence of edit operations from the filled table?
- Q: In what situation can you reduce the space to O(n), and what capability do you lose?
