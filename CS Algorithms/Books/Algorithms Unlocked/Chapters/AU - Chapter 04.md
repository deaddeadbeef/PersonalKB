---
id: au-ch-04
type: book-chapter
chapter: 4
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 3
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# AU — Chapter 04: A Lower Bound for Sorting and How to Beat It

## Summary

Chapter 4 answers a fundamental question: is $\Theta(n \lg n)$ the best we can do for sorting? The answer depends on the rules. Any algorithm that determines sorted order **exclusively by comparing pairs of elements** must make $\Omega(n \lg n)$ comparisons in the worst case. The proof uses a **decision tree**: each internal node represents a comparison, each leaf a possible output permutation. An n-element sort has n! possible permutations (≥ n! leaves), and a binary tree of height h has at most 2ʰ leaves, so h ≥ lg(n!) = $\Omega(n \lg n)$. Merge sort achieves this bound exactly — it is optimal among comparison sorts. However, if we abandon comparison-based ordering and exploit the structure of integer keys, we can do better. **Counting sort** counts occurrences of each value in a range 0..m−1, computes prefix sums, and places each element in its final slot — $\Theta(m+n)$, linear when m = $O(n)$. Crucially, it is **stable** (equal keys preserve input order), which enables **radix sort**: process keys digit-by-digit, least-significant digit first, using counting sort at each pass. Total time $\Theta(d(m+n)$) where d is the number of digits.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Comparison sort | Sorted order determined only by key comparisons |
| Decision tree | Abstract binary tree of all comparison outcomes; leaves = permutations |
| $\Omega(n \lg n)$ lower bound | Every comparison sort needs ≥ cn lg n comparisons worst case |
| Counting sort | Count-based integer sort; $\Theta(m+n)$; stable; non-comparison-based |
| Stable sort | Equal keys come out in original input order |
| Radix sort | LSD-first digit passes using stable counting sort; $\Theta(d(m+n)$) |

## Chunk Candidates

- [x] [[Sorting - The Omega(n lg n) lower bound applies to all comparison sorts]]
- [x] [[Sorting - Counting sort achieves linear time by exploiting bounded integer keys]]
- [x] [[Sorting - Radix sort applies stable counting sort digit-by-digit]]

## Wiki Pages Seeded

- [[Comparison Sort Lower Bound]] — decision-tree proof
- [[Counting Sort]] — algorithm and stability
- [[Radix Sort]] — LSD-first algorithm

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
