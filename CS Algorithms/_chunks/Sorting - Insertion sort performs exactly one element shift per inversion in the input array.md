---
id: chunk-csa-059
type: chunk
source: "[[Princeton Algorithms 4e - Online Reference]]"
source_loc: "Section 2.1 — Elementary Sorts"
topic: "sorting"
claim: "Insertion sort performs exactly one element shift (array write) for each inversion in the input, so the total work is directly proportional to the inversion count of the array"
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
# Sorting — Insertion sort performs exactly one element shift per inversion in the input array

## Context

Sedgewick and Wayne state this precisely: **insertion sort makes exactly as many comparisons (and shifts) as there are inversions in the input array, plus at most n−1 additional comparisons** (one per outer-loop iteration, to detect the stop condition).

**Why exactly one shift per inversion**: when the inner while-loop shifts A[j] right to A[j+1], it eliminates exactly one inversion — the pair (j, j+1) where A[j] > key. No other inversions are created (the key moves left past each element it is smaller than, resolving one inversion per step). Therefore:

```
total shifts = number of inversions in original array
```

**Counting inversions**: a pair (i, j) with i < j but A[i] > A[j] is an inversion. The number of inversions ranges from 0 (sorted) to n(n−1)/2 (reverse sorted). The average over all permutations is n(n−1)/4.

**Complexity derived directly**:

| Input state | Inversions | Insertion sort shifts |
|-------------|-----------|----------------------|
| Sorted | 0 | 0 → Θ(n) total work |
| Nearly sorted (max k per element) | ≤ kn | ≤ kn → O(kn) total work |
| Random | ≈ n(n−1)/4 | ≈ n²/4 → Θ(n²) total work |
| Reverse sorted | n(n−1)/2 | n(n−1)/2 → Θ(n²) total work |

## QnA Seeds

- Q: What is an inversion, and how many inversions does a sorted / reverse-sorted array have?
- Q: Why does insertion sort perform exactly one shift per inversion?
- Q: What is the average number of inversions over all permutations of n elements?
