---
id: chunk-csa-024
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 3"
topic: "searching"
claim: "Binary search on a sorted array eliminates half the remaining elements per comparison, giving O(lg n) worst-case time using O(1) extra space"
confidence: verified
supports:
  - "[[Binary Search]]"
tags:
  - csa
  - csa/searching
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Binary search halves the search space each step for O(lg n) worst case

## Context

Given a sorted array, binary search compares the target value against the middle element. If equal, the search succeeds; if smaller, recurse on the left half; if larger, recurse on the right half. Each comparison halves the search space, giving the recurrence T(n) = T(n/2) + Θ(1), which solves to T(n) = O(lg n). A 1-billion-element sorted array requires at most 30 comparisons. The algorithm requires O(1) extra space (iterative version) and is correct by a loop invariant: the target, if present, lies within the current subarray.

## Why It Matters

Binary search is one of the most fundamental algorithms in computer science — the canonical example of halving the search space. It underpins dictionary lookups, sorted-array queries, and is the basis for more complex data structures (B-trees, binary search trees). Its O(lg n) complexity makes it practical for any sorted dataset regardless of size; but it requires the array to be sorted, so it is typically paired with an efficient sort.

## QnA Seeds

- Q: What precondition does binary search require, and why?
- Q: Write a loop invariant that proves binary search correct.
- Q: What is the worst-case number of comparisons to search a sorted array of 1 million elements?
