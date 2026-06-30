---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
confidence: verified
---
# Techniques Overview

Some algorithmic ideas are not tied to a single problem domain — they are cross-cutting **techniques** that appear in sorting, searching, graphs, strings, and beyond. This hub collects patterns and analytical tools that sharpen your ability to design and reason about algorithms across every domain.

---

## Learn in This Order

1. [[Two Pointers and Sliding Window]] — scan-based patterns for arrays and strings; $O(n)$ solutions to subset, subarray, and interval problems
2. [[Amortized Analysis for Algorithms]] — averaging expensive operations over cheap ones; aggregate, accounting, and potential methods

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Two Pointers and Sliding Window]] | Converging/parallel pointer patterns; fixed/variable window; $O(n)$ array techniques |
| [[Amortized Analysis for Algorithms]] | Aggregate, accounting, and potential methods for averaged operation cost |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Two pointers vs sliding window? | Two pointers use two indices moving towards each other or in the same direction; sliding window is a specialised two-pointer pattern focused on contiguous subarrays/substrings. |
| Amortized vs average-case? | Amortized analysis guarantees the average cost over a worst-case sequence of operations. Average-case analysis assumes a distribution over inputs. Amortized bounds are stronger. |
| Where does amortized analysis apply? | Dynamic arrays (doubling), splay trees (rotations), union-find (path compression), hash-table resizing — any structure with occasional expensive operations. |

---

## How to Navigate

- **Solving array/string problems?** Start with [[Two Pointers and Sliding Window]].
- **Analysing data structure operations?** [[Amortized Analysis for Algorithms]] provides the tools.

---

## Related Domains

- **[[Foundations and Analysis Overview]]** — asymptotic analysis and recurrences complement the amortized perspective.
- **[[Sorting Overview]]** — two-pointer patterns underpin partition-based algorithms like quicksort.
- **[[Strings Overview]]** — sliding window drives many substring search and matching algorithms.

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
