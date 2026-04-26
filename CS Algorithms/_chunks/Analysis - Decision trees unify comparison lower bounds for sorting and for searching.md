---
id: chunk-csa-055
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 3 — Insertion Sort, Merge Sort, Binary Search"
topic: "analysis"
claim: "Decision trees provide a single framework that establishes Ω(lg n) as the lower bound for comparison-based searching and Ω(n lg n) as the lower bound for comparison-based sorting, by counting leaves against tree height"
confidence: verified
supports:
  - "[[Comparison Sort Lower Bound]]"
  - "[[Binary Search]]"
tags:
  - csa
  - csa/analysis
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Decision trees unify comparison lower bounds for sorting and for searching

## Context

MIT 6.006 Lecture 3 frames binary search and comparison sorting within the same decision-tree model, showing the lower bound argument is structurally identical in both cases.

**The shared model**: Any algorithm that determines its answer solely through pairwise comparisons can be represented as a binary decision tree. Each internal node is a comparison; each branch is its outcome; each leaf is a distinct answer. A correct algorithm must have at least as many leaves as there are possible answers.

| Problem | Possible answers | Min leaves | Tree height lower bound |
|---------|-----------------|-----------|------------------------|
| Search in sorted array of n | n + 1 (target at position 1…n, or absent) | n + 1 | ≥ lg(n+1) = Ω(lg n) |
| Sort n distinct elements | n! permutations | n! | ≥ lg(n!) = Ω(n lg n) |

The argument is the same: the binary tree of height h can have at most 2ʰ leaves; requiring at least L leaves forces h ≥ lg L.

**Consequence**: Binary search is optimal (it achieves O(lg n)), and any comparison sort achieving Θ(n lg n) (merge sort, heapsort) is optimal. You cannot improve on these bounds without abandoning the comparison model.

## QnA Seeds

- Q: How does the decision-tree argument extend from sorting to searching?
- Q: Why does searching in a sorted array of n elements require Ω(lg n) comparisons?
- Q: What does the decision-tree lower bound tell us about the optimality of binary search and merge sort?
