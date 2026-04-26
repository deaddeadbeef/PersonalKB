---
tags:
  - csa
  - csa/sorting
confidence: verified
up: "[[CS Algorithms]]"
---
# Sorting Overview

Given an array A of n elements with a total order (≤), rearrange A so that A[1] ≤ A[2] ≤ … ≤ A[n].

---

## Comparison Sort Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Selection sort | $\Theta(n²)$ | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ | No | Simple; no early exit |
| Insertion sort | $\Theta(n)$ | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ | Yes | Fast for small / nearly-sorted |
| Merge sort | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $O(n)$ | Yes | Guaranteed; aux space required |
| Quicksort | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n²)$ | $O(\lg n)$ | No | Fastest in practice; randomise pivot |
| Heap sort | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $O(1)$ | No | *(Beyond AU scope — broader-context / future expansion)* |

## Non-Comparison Sort Algorithms

| Algorithm | Time | Space | Stable | Requirement |
|-----------|------|-------|--------|-------------|
| Counting sort | $\Theta(m+n)$ | $\Theta(m+n)$ | Yes | Keys in 0..m−1 |
| Radix sort | $\Theta(d(m+n)$) | $\Theta(m+n)$ | Yes | Keys decompose into d digits base m |

---

## Lower Bound

Any **comparison sort** requires $\Omega(n \lg n)$ comparisons in the worst case.
Proof via decision-tree argument → see [[Comparison Sort Lower Bound]].

Non-comparison sorts bypass this bound by exploiting key structure.

---

## Choosing a Sort

| Situation | Recommendation |
|-----------|---------------|
| n < ~50 | Insertion sort |
| Worst-case guarantee needed | Merge sort |
| Large n, random data, maximum speed | Quicksort (randomised pivot) |
| Integer keys in known range m = $O(n)$ | Counting sort |
| Multi-field / digit-decomposable keys | Radix sort |
| In-place + $O(n \lg n)$ guaranteed | Heap sort *(beyond AU scope)* |

---

## Detailed Pages

[[Merge Sort]] · [[Quicksort]] · [[Counting Sort]] · [[Radix Sort]] · [[Binary Search]] · [[Comparison Sort Lower Bound]] · [[Selection Sort]] · [[Insertion Sort]] · [[Inversions]]

> **Note:** [[Binary Search]] is grouped here because it operates on **sorted** arrays — its correctness and analysis are tightly coupled to the sorting algorithms on this page. It is a searching technique, not a sort, but belongs in this hub by dependency.

## Supporting Chunks

- [[Sorting - The Omega(n lg n) lower bound applies to all comparison sorts]]
- [[Sorting - Merge sort guarantees Theta(n lg n) with O(n) auxiliary space]]
- [[Sorting - Quicksort is fastest in practice but has Theta(n squared) worst case]]
- [[Sorting - Counting sort achieves linear time by exploiting bounded integer keys]]
- [[Sorting - Radix sort applies stable counting sort digit-by-digit]]
- [[Sorting - Selection sort scans for the minimum n-1 times giving unconditional Theta(n squared)]]
- [[Sorting - Insertion sort is optimal for small or nearly-sorted arrays]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Sources Index]]. Chapters 3–4.
