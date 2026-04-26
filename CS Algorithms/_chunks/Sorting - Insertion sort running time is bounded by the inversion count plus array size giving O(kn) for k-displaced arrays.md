---
id: chunk-csa-060
type: chunk
source: "[[Princeton Algorithms 4e - Online Reference]]"
source_loc: "Section 2.1 — Elementary Sorts"
topic: "sorting"
claim: "The insertion sort running time equals Θ(inversions + n), so on a k-sorted array where each element is at most k positions from its final place the algorithm runs in O(kn), far below the Θ(n²) worst case"
confidence: verified
supports:
  - "[[Insertion Sort]]"
  - "[[Inversions]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Insertion sort running time is bounded by the inversion count plus array size giving O(kn) for k-displaced arrays

## Context

Sedgewick and Wayne's near-sortedness argument formalises insertion sort's adaptivity:

**Total work = Θ(inversions + n)**

- The `+n` term accounts for the n−1 outer-loop iterations (each at minimum does one comparison to confirm the current element is in place).
- The `inversions` term accounts for every shift, as derived in the companion chunk.

**k-sorted arrays** (each element displaced by at most k positions from its sorted position):

- Each element can create at most k inversions with earlier elements.
- Total inversions ≤ kn.
- Therefore running time = Θ(kn + n) = **O(kn)**.

When k is a small constant (e.g., k = 5, meaning data is nearly sorted from a merge of sorted streams), insertion sort runs in O(n) effectively. This is why Timsort and introsort use insertion sort as their base case for small subarrays — and why insertion sort is the natural finisher after a coarse radix pass.

**Lower bound on comparison sorts for k-sorted arrays**: any comparison sort still requires Ω(n) time (must at least read each element), and insertion sort's O(kn) matches this up to the small displacement constant k.

## QnA Seeds

- Q: What is the exact expression for insertion sort's running time in terms of inversions and n?
- Q: If every element is at most k positions from its sorted position, what is insertion sort's running time?
- Q: Why is insertion sort used as the base case in hybrid sorts like Timsort?
