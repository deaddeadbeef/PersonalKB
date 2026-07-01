---
id: au-ch-03
type: book-chapter
chapter: 3
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 5
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# AU — Chapter 03: Algorithms for Sorting and Searching

## Summary

The book's most algorithm-dense chapter covers one search and four sort algorithms. **Binary search** on a sorted array eliminates half the search space per comparison, yielding $O(\lg n)$ worst case — a fundamental result. **Selection sort** always runs in $\Theta(n²)$ by scanning for the minimum n−1 times. **Insertion sort** builds a sorted prefix incrementally; it is $\Theta(n)$ on nearly-sorted inputs and $\Theta(n²)$ on reversed inputs, making it the practical choice for small arrays. **Merge sort** is the first divide-and-conquer sort: recursively sort two halves, then merge in $\Theta(n)$ time; the result is $\Theta(n \lg n)$ in *all cases*, at the cost of $O(n)$ auxiliary space. **Quicksort** partitions around a pivot so the pivot lands in its final position; worst case is $\Theta(n²)$ on adversarial inputs, but with randomised pivot selection the expected time is $\Theta(n \lg n)$ and the constant factors make it fastest in practice on random data.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Binary search | Halve search space per step; $O(\lg n)$; requires sorted array |
| Selection sort | Find minimum, swap to front; always $\Theta(n²)$ |
| Insertion sort | Build sorted prefix; $\Theta(n)$ best, $\Theta(n²)$ worst |
| Merge sort | Divide-and-conquer; $\Theta(n \lg n)$ all cases; $O(n)$ auxiliary space |
| Quicksort | Partition around pivot; expected $\Theta(n \lg n)$; $\Theta(n²)$ worst case |
| Randomised quicksort | Random pivot eliminates adversarial inputs |
| In-place | Quicksort/insertion sort $O(1)$ extra space; merge sort needs $O(n)$ |

## Algorithm Complexity Summary

| Algorithm | Best | Worst | Space |
|-----------|------|-------|-------|
| Binary search | $\Theta(1)$ | $O(\lg n)$ | $O(1)$ |
| Selection sort | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ |
| Insertion sort | $\Theta(n)$ | $\Theta(n²)$ | $O(1)$ |
| Merge sort | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $O(n)$ |
| Quicksort | $\Theta(n \lg n)$ | $\Theta(n²)$ | $O(\lg n)$ |

## Chunk Candidates

- [x] [[Sorting - Binary search halves the search space each step for O(lg n) worst case]]
- [x] [[Sorting - Selection sort scans for the minimum n-1 times giving unconditional Theta(n squared)]]
- [x] [[Sorting - Merge sort guarantees Theta(n lg n) with O(n) auxiliary space]]
- [x] [[Sorting - Quicksort is fastest in practice but has Theta(n squared) worst case]]
- [x] [[Sorting - Insertion sort is optimal for small or nearly-sorted arrays]]

## Wiki Pages Seeded

- [[Binary Search]] — algorithm and loop-invariant proof
- [[Merge Sort]] — divide-and-conquer analysis
- [[Quicksort]] — partition, pivot, worst-case analysis
- [[Sorting Overview]] — comparison table

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
