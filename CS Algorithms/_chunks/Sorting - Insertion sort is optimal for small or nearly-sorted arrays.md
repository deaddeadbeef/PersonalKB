---
id: chunk-csa-025
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 3"
topic: "sorting"
claim: "Insertion sort runs in Θ(n) on nearly-sorted input and Θ(n²) on reverse-sorted input, making it the practical choice for small arrays or as a final pass in hybrid sorts"
confidence: verified
supports:
  - "[[Sorting Overview]]"
  - "[[Insertion Sort]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Insertion sort is optimal for small or nearly-sorted arrays

## Context

Insertion sort builds a sorted prefix incrementally: for each element, shift it left past all larger elements until it reaches its correct position. On already-sorted input every element is already in place, so each insertion requires zero shifts — Θ(n) total. On reverse-sorted input every insertion scans the entire prefix — Θ(n²). The number of comparisons equals the number of inversions in the input, so performance degrades gracefully as disorder increases. Insertion sort is in-place (O(1) extra space) and stable. Its low overhead on small inputs (no recursive call stack, simple inner loop) makes it the standard base case in hybrid sorts like Timsort and introsort, which switch from quicksort/merge sort to insertion sort once the subarray is smaller than ~16 elements.

## Why It Matters

Insertion sort illustrates how input structure affects algorithm performance — a point Cormen returns to repeatedly. It is theoretically dominated by merge sort and quicksort at large n, but practically superior at small n because of low constant factors and zero overhead. Understanding when to prefer it over asymptotically better alternatives is a key engineering judgement.

## QnA Seeds

- Q: On what type of input does insertion sort run in Θ(n), and why?
- Q: How is the running time of insertion sort related to the number of inversions in the input?
- Q: Why is insertion sort used as the base case in hybrid sorting algorithms like Timsort?
