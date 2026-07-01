---
tags:
  - csa
  - csa/study
  - csa/sorting
up: "[[Algorithms Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Sorting and Searching — Review Drill

Active-recall drill covering comparison sorts, non-comparison sorts, the sorting lower bound, inversion analysis, and binary search.

**Canon pages:** [[Sorting Overview]] · [[Merge Sort]] · [[Quicksort]] · [[Counting Sort]] · [[Radix Sort]] · [[Selection Sort]] · [[Insertion Sort]] · [[Inversions]] · [[Binary Search]]

---

## How to Use

Answer each question without referring to the canonical pages. When you cannot answer, mark it and check [[Sorting Overview]] or the specific algorithm page, then try again from scratch.

---

## Core Recall

**Sorting Lower Bound**

Q: State the comparison sort lower bound and the argument that proves it.
A: Any comparison sort requires $\Omega(n \lg n)$ comparisons in the worst case. Proof: model the algorithm as a binary decision tree where each internal node is a comparison and each leaf is a permutation. The tree needs ≥ n! leaves, so height ≥ lg(n!) = $\Omega(n \lg n)$. See [[Comparison Sort Lower Bound]].

Q: Which comparison sorts are asymptotically optimal?
A: Merge sort is optimal — it achieves $\Theta(n \lg n)$ in all cases. Heapsort also achieves $\Theta(n \lg n)$ but is not in-place like merge sort's conceptual form. Quicksort achieves expected $\Theta(n \lg n)$ but has a $\Theta(n²)$ worst case.

Q: How do counting sort and radix sort bypass the $\Omega(n \lg n)$ lower bound?
A: They are not comparison sorts — they exploit numeric structure of the keys (bounded integer range for counting sort; digit structure for radix sort) rather than comparing pairs of elements. The lower bound proof applies only to algorithms that determine order exclusively by comparisons.

---

**Merge Sort**

Q: State merge sort's time and space complexity in all cases.
A: $\Theta(n \lg n)$ in all cases (best, average, worst). Space: $O(n)$ auxiliary — the merge step requires a temporary array of size n.

Q: Why is merge sort's $\Theta(n \lg n)$ guarantee valuable compared to quicksort?
A: Merge sort has no bad inputs — it always runs in $\Theta(n \lg n)$ regardless of the input. Quicksort's worst case is $\Theta(n²)$ on adversarial or sorted inputs. For applications requiring a worst-case guarantee, merge sort is safer.

Q: Is merge sort stable?
A: Yes. During the merge step, when two elements are equal, the left-side element is taken first, preserving relative order.

---

**Quicksort**

Q: What is quicksort's worst case, and what input triggers it?
A: $\Theta(n²)$. Triggered when the pivot is always the minimum or maximum of the subarray — e.g., a sorted or reverse-sorted array with first-element pivoting. Every partition produces one empty subarray and one of size n−1.

Q: What is quicksort's expected time complexity and why?
A: $\Theta(n \lg n)$ with random pivot selection. The analysis shows that any two elements are compared at most once and compared only when one of them is chosen as a pivot. The expected number of comparisons is 2n ln n ≈ 1.39 n lg n.

Q: Why is quicksort typically fastest in practice despite the same asymptotic bound as merge sort?
A: In-place partitioning gives excellent cache locality. No auxiliary memory allocation. Small constant factor in the inner loop. Combines well with insertion sort for small subarrays (introsort/Timsort).

---

**Counting Sort**

Q: What condition must hold for counting sort to be applicable?
A: The keys must be integers in a bounded range [0, k]. The algorithm requires $O(k)$ auxiliary space and runs in $\Theta(n + k)$ time. If k = $O(n)$, this is $\Theta(n)$.

Q: Why must counting sort's right-to-left pass scan the input from right to left?
A: To preserve stability. Scanning right-to-left ensures that among equal keys, the one appearing last in the input is placed last in the output — maintaining relative order of equal elements. Scanning left-to-right reverses that order.

Q: Is counting sort stable? Does it sort in place?
A: Stable: yes (with the right-to-left pass). In-place: no — it uses an auxiliary output array and a count array.

---

**Radix Sort**

Q: What does "LSD-first" mean for radix sort, and why does it work?
A: Least Significant Digit first — process the least significant digit first, then the next, up to the most significant digit. Correctness relies on the subroutine sort being **stable**: equal keys on a higher digit retain the order established by previous (lower digit) passes.

Q: What is radix sort's time complexity?
A: $\Theta(d(n + k)$) where d is the number of digits and k is the alphabet size (radix). For fixed k and d = $O(log_k n)$, this is $\Theta(n log_k n)$. For large k and small d, this can beat comparison sorts.

Q: Is radix sort stable?
A: Radix sort itself is stable if and only if the per-digit subroutine sort (typically counting sort) is stable.

---

**Selection Sort**

Q: What is selection sort's comparison count and swap count?
A: Comparisons: always $\Theta(n²)$ — unconditional. Swaps: exactly n−1, regardless of input order. It cannot short-circuit on sorted input.

Q: Why might selection sort be preferred over insertion sort in some contexts?
A: Selection sort makes exactly n−1 swaps (writes). In systems where writes are significantly more expensive than reads — flash memory, EEPROM, write-audited storage — minimising write count justifies the extra comparison cost.

Q: Is selection sort adaptive?
A: No. It always makes $\Theta(n²)$ comparisons on any input. A sorted input yields zero time savings compared to a random input.

---

**Insertion Sort**

Q: State the exact relationship between insertion sort's running time and inversions.
A: Insertion sort performs **exactly one element shift per inversion** in the input, plus at most n−1 comparisons for loop-exit checks. Total running time: $\Theta(inversions + n)$.

Q: What is an inversion?
A: A pair of indices (i, j) with i < j but A[i] > A[j] — a pair of elements that appear in the wrong relative order.

Q: Why is insertion sort optimal for nearly-sorted input?
A: If every element is at most k positions from its final position, the array has ≤ kn inversions, so insertion sort runs in $O(kn)$. For small constant k this is effectively $O(n)$. It matches the information-theoretic lower bound for this input class.

Q: Is insertion sort stable and adaptive?
A: Yes to both. Stable because equal elements are never swapped past each other (the while condition is strict: `A[j] > key`). Adaptive because fewer inversions → fewer shifts.

---

**Inversions**

Q: What is the maximum number of inversions for an array of n distinct elements?
A: n(n−1)/2 — achieved when the array is in reverse sorted order.

Q: What is the expected number of inversions in a random permutation of n elements?
A: n(n−1)/4.

Q: Describe the $O(n \lg n)$ algorithm for counting inversions.
A: A merge-sort-based divide-and-conquer: count inversions within the left half, within the right half, and cross-inversions (pairs with left element > right element) during the merge step. Cross-inversions are counted in $O(n)$ per merge; total $\Theta(n \lg n)$.

---

**Binary Search**

Q: State binary search's worst-case complexity and the lower bound that matches it.
A: $O(\lg n)$ worst case. The comparison-based search lower bound is $\Omega(\lg n)$ (decision tree with n+1 leaves). Binary search is therefore optimal among comparison-based searches.

Q: State the loop invariant for binary search.
A: After each iteration, if the target exists in A, it lies within A[lo..hi]. At termination (lo > hi), the target is absent.

Q: Is binary search applicable to unsorted arrays?
A: No. Binary search requires the array to be sorted; it relies on the sorted order to halve the search space at each step.

---

## Compare and Contrast

**All Sorting Algorithms at a Glance**

| Algorithm | Best | Average | Worst | Space | Stable | Adaptive |
|-----------|------|---------|-------|-------|--------|---------|
| Merge Sort | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ | $O(n)$ | ✅ | ❌ |
| Quicksort | $\Omega(n \lg n)$ | $\Theta(n \lg n)$ | $\Theta(n²)$ | $O(\lg n)$ avg | ❌ | ❌ |
| Counting Sort | $\Theta(n+k)$ | $\Theta(n+k)$ | $\Theta(n+k)$ | $O(k)$ | ✅ | ❌ |
| Radix Sort | $\Theta(d(n+k)$) | $\Theta(d(n+k)$) | $\Theta(d(n+k)$) | $O(n+k)$ | ✅ | ❌ |
| Selection Sort | $\Theta(n²)$ | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ | ❌ | ❌ |
| Insertion Sort | $\Theta(n)$ | $\Theta(n²)$ | $\Theta(n²)$ | $O(1)$ | ✅ | ✅ |

**Insertion Sort vs Selection Sort**

| Property | Insertion Sort | Selection Sort |
|----------|---------------|---------------|
| Sorted input | $\Theta(n)$ | $\Theta(n²)$ |
| Worst case | $\Theta(n²)$ | $\Theta(n²)$ |
| Swaps worst case | $\Theta(n²)$ | n−1 |
| Stable | Yes | No |
| Adaptive | Yes | No |

Key contrast: insertion sort adapts to order (inversions-sensitive), selection sort does not; selection sort minimises writes, insertion sort can require many.

**Comparison Sorts vs Non-Comparison Sorts**

| Criterion | Comparison sorts | Non-comparison sorts |
|-----------|-----------------|---------------------|
| Lower bound | $\Omega(n \lg n)$ | N/A — bypassed |
| Requirements | Only need `<` operator | Require integer / structured keys |
| Universality | Sort any comparable type | Restricted to specific key types |
| Stability | Depends on algorithm | Counting sort: yes; radix: conditional |

---

## Common Mistakes

1. **Forgetting the stability requirement in radix sort** — radix sort only works correctly if the per-digit subroutine is stable. Using an unstable sort (e.g., selection sort) as the digit subroutine breaks the algorithm.

2. **Quicksort worst case** — students often assume random pivot is always safe. It prevents adversarial sorted inputs but not every bad case. Introsort (quicksort + heapsort fallback) guarantees $O(n \lg n)$ worst case.

3. **Confusing counting sort with radix sort** — counting sort is a single-pass sort for bounded integers; radix sort uses counting sort as a digit-level subroutine across d passes.

4. **Inversion count vs comparison count** — insertion sort's shift count equals inversions; its comparison count is inversions + (n−1) for the loop-exit checks. These are related but not identical.

5. **Selection sort on sorted input** — selection sort does NOT terminate early on a sorted input. Its comparison count is always n(n−1)/2.

6. **Binary search on unsorted arrays** — binary search requires a sorted array; applying it to unsorted data produces incorrect results without any error signal.

---

## Links Back

- [[Sorting Overview]] — algorithm comparison table and selection guide
- [[Merge Sort]] — divide-and-conquer; $\Theta(n \lg n)$ all cases
- [[Quicksort]] — partition-based; expected $\Theta(n \lg n)$; $\Theta(n²)$ worst case
- [[Counting Sort]] — linear-time stable sort for bounded integers
- [[Radix Sort]] — LSD-first digit-by-digit sort
- [[Selection Sort]] — unconditional $\Theta(n²)$; minimal writes
- [[Insertion Sort]] — inversion-optimal; excellent for nearly-sorted data
- [[Inversions]] — inversion count definition, sortedness metric, merge-sort counter
- [[Binary Search]] — $O(\lg n)$ search on sorted arrays; optimal comparison search
- [[Comparison Sort Lower Bound]] — $\Omega(n \lg n)$ decision-tree proof

## References

- [[CS Algorithms/CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index]]
