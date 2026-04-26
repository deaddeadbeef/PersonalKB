---
id: chunk-csa-023
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 2"
topic: "analysis"
claim: "Divide-and-conquer algorithms split a problem of size n into subproblems, recurse, and combine; their running time is captured by a recurrence relation T(n) = aT(n/b) + f(n)"
confidence: verified
supports:
  - "[[Merge Sort]]"
  - "[[Recurrence Relations]]"
  - "[[Master Theorem]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Divide-and-conquer running time is expressed as a recurrence relation

## Context

In a divide-and-conquer algorithm the input of size n is split into a subproblems each of size n/b, solved recursively, and the results combined in f(n) time. The running time satisfies the recurrence T(n) = aT(n/b) + f(n). For merge sort, a = 2, b = 2, f(n) = Θ(n), which gives T(n) = 2T(n/2) + Θ(n) — solved by the Master Theorem or by induction to yield T(n) = Θ(n lg n). Recurrences are the standard vocabulary for analysing recursive algorithms; they make the cost structure visible and amenable to formal solution.

## Why It Matters

Recurrence relations make recursive algorithm analysis tractable: rather than reasoning about all recursive calls simultaneously, you write down the relationship between problem sizes and solve it. The same framework applies to binary search (T(n) = T(n/2) + Θ(1) → O(lg n)), merge sort, quicksort expected case, and many other divide-and-conquer algorithms. Understanding recurrences is a prerequisite for analysing any recursive algorithm.

## QnA Seeds

- Q: Write the recurrence relation for merge sort and explain each term.
- Q: How does the divide-and-conquer paradigm differ from dynamic programming?
- Q: What does the combining step contribute to the total running time of a divide-and-conquer algorithm?
