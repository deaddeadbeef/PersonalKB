---
id: chunk-csa-058
type: chunk
source: "[[Princeton Algorithms 4e - Online Reference]]"
source_loc: "Section 2.1 — Elementary Sorts"
topic: "sorting"
claim: "Selection sort is non-adaptive: it makes the same n(n−1)/2 comparisons whether the input is already sorted, reverse-sorted, or randomly permuted, because it always scans the full remaining suffix to find the minimum"
confidence: verified
supports:
  - "[[Selection Sort]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Selection sort is non-adaptive and performs identical comparison work on sorted or random inputs

## Context

Sedgewick and Wayne describe non-adaptivity as a defining weakness of selection sort. The algorithm's inner loop scans from position i+1 to n to find the minimum regardless of what the data looks like:

```
for i = 1 to n−1:
    min_idx = i
    for j = i+1 to n:          // always runs n−i times
        if A[j] < A[min_idx]:
            min_idx = j
    swap A[i] with A[min_idx]
```

There is no early exit. The inner loop cannot short-circuit even if `A[i]` is already the minimum — it must verify that claim by inspecting every remaining element. Comparisons sum to:

```
(n−1) + (n−2) + … + 1 = n(n−1)/2 = Θ(n²)
```

always. This stands in direct contrast to insertion sort:

| Input | Insertion sort comparisons | Selection sort comparisons |
|-------|--------------------------|--------------------------|
| Already sorted | n−1 = Θ(n) | n(n−1)/2 = Θ(n²) |
| Nearly sorted (k displacements) | O(kn) | n(n−1)/2 = Θ(n²) |
| Random | Θ(n²) | Θ(n²) |
| Reverse sorted | Θ(n²) | Θ(n²) |

Non-adaptivity makes selection sort especially wasteful on nearly-sorted inputs that arrive frequently in practice (log files, timestamps, sequential updates).

## QnA Seeds

- Q: What does it mean for a sorting algorithm to be non-adaptive, and why is selection sort non-adaptive?
- Q: How do the comparison counts of selection sort and insertion sort differ on an already-sorted array?
- Q: Can selection sort terminate early if it detects the array is sorted? Why or why not?
