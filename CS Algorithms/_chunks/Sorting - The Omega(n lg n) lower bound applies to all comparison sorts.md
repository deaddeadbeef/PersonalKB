---
id: chunk-csa-006
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 4"
topic: "sorting"
claim: "Every comparison sort requires Omega(n lg n) comparisons in the worst case, proven by a decision-tree argument"
confidence: verified
supports:
  - "[[Comparison Sort Lower Bound]]"
  - "[[Sorting Overview]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — The Omega(n lg n) lower bound applies to all comparison sorts

## Context

A comparison sort determines the output permutation solely by comparing pairs of elements. Model it as a binary decision tree: each internal node is a comparison (a[i] ≤ a[j]?), each leaf is a possible sorted permutation. There are n! permutations of n elements, so the tree has at least n! leaves. A binary tree of height h has at most 2ʰ leaves, so h ≥ lg(n!). By Stirling's approximation, lg(n!) ≥ n lg n − n/ln 2 = Ω(n lg n). Merge sort achieves Θ(n lg n) in all cases, so the bound is tight — merge sort is an optimal comparison sort.

## Why It Matters

This result establishes that no comparison sort can asymptotically beat Θ(n lg n). It is a classical lower-bound proof demonstrating that you can prove things are impossible, not just hard. It also motivates counting sort and radix sort as the only route to linear-time sorting (by abandoning comparisons and exploiting key structure).

## QnA Seeds

- Q: Why can't we sort faster than O(n lg n) using comparisons?
- Q: What is the decision-tree model for comparison sorting?
- Q: Is merge sort optimal among comparison sorts?
