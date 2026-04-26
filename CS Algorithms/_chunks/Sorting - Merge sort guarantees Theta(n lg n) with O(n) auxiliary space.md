---
id: chunk-csa-009
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 3"
topic: "sorting"
claim: "Merge sort guarantees Theta(n lg n) in all cases using a divide-and-conquer recurrence, at the cost of O(n) auxiliary space"
confidence: verified
supports:
  - "[[Merge Sort]]"
  - "[[Sorting Overview]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Merge sort achieves guaranteed Theta(n lg n) with O(n) auxiliary space

## Context

Merge sort recursively splits the array in half, sorts each half, then merges the two sorted halves in Θ(n) time. The recurrence T(n) = 2T(n/2) + Θ(n) solves to Θ(n lg n). The key insight is that the merge step is linear: scan both sorted halves from the left, picking the smaller element each time. This requires O(n) auxiliary space (the output array for the merge). There are no bad inputs — merge sort is Θ(n lg n) in the best, average, and worst cases.

## Why It Matters

Merge sort is the canonical example of divide-and-conquer and the textbook demonstration that recursion can yield efficient algorithms. Its guaranteed worst case makes it preferable to quicksort when worst-case performance matters (e.g., real-time systems). It is also stable, making it the reference implementation for the "guaranteed performance" row in the sort-choice table.

## QnA Seeds

- Q: What is the recurrence relation for merge sort and how does it solve to Θ(n lg n)?
- Q: Why does merge sort need O(n) extra space?
- Q: When should you prefer merge sort over quicksort?
