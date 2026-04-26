---
id: chunk-csa-033
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 3"
topic: "sorting"
claim: "Selection sort finds the minimum of the unsorted suffix on each of n−1 passes, performing exactly Θ(n²) comparisons regardless of input order"
confidence: verified
supports:
  - "[[Sorting Overview]]"
  - "[[Selection Sort]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Selection sort scans for the minimum n−1 times giving unconditional Θ(n²)

## Context

Selection sort maintains a sorted prefix. In pass i (from 1 to n−1): scan A[i..n] to find the minimum element; swap it into position A[i]. After n−1 passes, the array is sorted.

**Comparison count**: pass i scans n−i elements, performing n−i−1 comparisons. Total: Σᵢ₌₁ⁿ⁻¹ (n−i) = n(n−1)/2 = Θ(n²). This count is **independent of the input** — selection sort makes exactly the same number of comparisons on a sorted array as on a reverse-sorted one.

**Swap count**: exactly n−1 swaps (one per pass), regardless of input. This is fewer swaps than insertion sort in the worst case.

**Properties**: in-place (O(1) extra space), not stable (swapping disrupts relative order of equal elements), unconditionally Θ(n²) — no best-case improvement.

## Why It Matters

Selection sort's unconditional Θ(n²) contrasts with insertion sort, which achieves Θ(n) on nearly-sorted input. This illustrates that a simple scan-and-place approach gains nothing from pre-existing order. For applications where swaps are expensive but comparisons are cheap, selection sort's n−1 swaps can be an advantage over insertion sort's potential Θ(n²) swaps.

## QnA Seeds

- Q: Why does selection sort perform the same number of comparisons regardless of whether the input is sorted or reverse-sorted?
- Q: Compare selection sort and insertion sort on: comparisons, swaps, stability, and adaptivity.
- Q: Under what conditions might you prefer selection sort over insertion sort?
