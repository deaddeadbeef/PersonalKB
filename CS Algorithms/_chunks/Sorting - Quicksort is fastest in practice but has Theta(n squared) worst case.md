---
id: chunk-csa-010
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 3"
topic: "sorting"
claim: "Quicksort's average-case Theta(n lg n) and small constants make it the fastest comparison sort in practice despite a Theta(n squared) worst case"
confidence: verified
supports:
  - "[[Quicksort]]"
  - "[[Sorting Overview]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Quicksort is fastest in practice but has Theta(n squared) worst case

## Context

Quicksort partitions the array around a pivot: elements smaller go left, larger go right; the pivot lands in its final position. Recurse on each side. Worst case: Θ(n²) when pivots are always the minimum or maximum (e.g., already-sorted input with first-element pivot), producing unbalanced partitions. Average case: Θ(n lg n). Randomised quicksort picks a random pivot, making the probability of consistently bad splits negligible. In practice, quicksort's small constant factors (few writes compared to merge sort, good cache behaviour) make it the fastest comparison sort on random data.

## Why It Matters

Quicksort is the algorithm most commonly implemented in standard libraries (e.g., C's qsort, Java's Arrays.sort for primitives). Understanding its worst case is critical for security-sensitive applications — adversarial inputs can trigger Θ(n²) behaviour in non-randomised implementations, a vector for algorithmic complexity attacks.

## QnA Seeds

- Q: What input triggers quicksort's worst case?
- Q: How does randomised pivot selection eliminate the adversarial worst case?
- Q: Why is quicksort faster than merge sort in practice despite the same asymptotic average case?
