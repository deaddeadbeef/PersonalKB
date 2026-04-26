---
id: chunk-csa-057
type: chunk
source: "[[Princeton Algorithms 4e - Online Reference]]"
source_loc: "Section 2.1 — Elementary Sorts"
topic: "sorting"
claim: "Selection sort performs exactly n−1 swaps regardless of the input order, making it optimal for situations where writing data is expensive relative to reading or comparing"
confidence: verified
supports:
  - "[[Selection Sort]]"
  - "[[Sorting Overview]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Selection sort minimizes the number of writes by guaranteeing exactly n−1 swaps regardless of input order

## Context

Sedgewick and Wayne highlight selection sort's defining characteristic: it scans the remaining unsorted suffix to find the minimum and then performs **exactly one swap** to place it. This pattern repeats n−1 times, giving exactly n−1 swaps for any input.

**Contrast with other sorts**:

| Algorithm | Swaps (worst case) | Swaps (best case) |
|-----------|-------------------|------------------|
| Selection sort | n−1 | n−1 |
| Insertion sort | Θ(n²) | 0 |
| Merge sort | N/A (uses copies) | N/A |
| Quicksort | Θ(n²) | Ω(n lg n) |

**When this matters**: in hardware or storage systems where writes are significantly more expensive than reads — flash memory with limited write cycles, tape storage, EEPROMs — minimising swaps/writes is a practical goal. Selection sort's exactly n−1 write operations is the minimum possible for a sorting algorithm that must move every out-of-place element.

**Caveats**: the low swap count comes at the cost of being non-adaptive (Θ(n²) comparisons always) and not stable. In most software contexts the write savings do not compensate for the comparison overhead.

## QnA Seeds

- Q: How many swaps does selection sort perform in the worst case, and why?
- Q: When would selection sort's low write count be a practical advantage over insertion sort?
- Q: Which of selection sort and insertion sort performs fewer writes in the worst case, and by how much?
