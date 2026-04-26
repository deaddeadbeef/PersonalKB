---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Counting Sort, Radix Sort, and Non-Comparison Sorting"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

Comparison-based sorting algorithms have a proven lower bound of Ω(n log n) in the worst case, derived from the decision tree model: any comparison sort must make at least ⌈log₂(n!)⌉ comparisons. Non-comparison sorts bypass this bound by exploiting structure in the keys. Counting sort operates on integer keys in range [0, k], counting occurrences of each value and computing prefix sums to place elements directly into their sorted positions in O(n + k) time. It is stable—equal elements maintain their relative order—which is essential when used as a subroutine. Radix sort exploits this stability by sorting d-digit numbers digit by digit, from least significant digit (LSD) to most significant digit (MSD), using counting sort on each digit. LSD radix sort processes all elements uniformly and runs in O(d(n + k)) time where k is the base. MSD radix sort recursively partitions elements by the most significant digit first, enabling early termination for strings of varying length but requiring careful handling of recursion and bucket management. The choice between comparison and non-comparison sorts depends on data characteristics: when keys are integers in a bounded range or fixed-length strings, radix sort achieves linear time; when keys are arbitrary or the range k is much larger than n, comparison sorts remain preferable. Bucket sort, another non-comparison approach, distributes elements into buckets assuming uniform distribution, achieving O(n) expected time.

## Key Claims

1. The Ω(n log n) lower bound for comparison-based sorting is information-theoretic: the decision tree must have at least n! leaves, requiring height ≥ log₂(n!) = Θ(n log n).
2. Counting sort achieves O(n + k) time for integer keys in range [0, k] and is stable, making it the ideal subroutine for radix sort.
3. LSD radix sort achieves O(d(n + k)) time by applying a stable sort on each digit from least to most significant, where d is the number of digits and k is the radix.
4. For n integers in range [0, n^c − 1], choosing base n yields radix sort time O(cn), which is linear when c is constant.
5. Non-comparison sorts are not universally superior: they require assumptions about key structure (bounded integers, fixed-length strings) and degrade when these assumptions are violated.

## Atomic Facts

1. Counting sort uses an auxiliary array C[0..k] where C[i] counts elements equal to i, then computes prefix sums so C[i] gives the final position of value i.
2. Stability in counting sort is achieved by iterating the input array from right to left when placing elements into the output array.
3. LSD radix sort processes digits from position 0 (least significant) to position d−1 (most significant); correctness relies on the stability of the per-digit sort.
4. MSD radix sort recursively partitions into buckets by the most significant digit, similar to quicksort's partitioning but with k-way splits.
5. Bucket sort distributes n elements into n buckets assuming uniform distribution over [0, 1), sorts each bucket with insertion sort, achieving O(n) expected time.
6. The decision tree model assumes only binary comparisons between elements; any algorithm using richer operations (indexing, arithmetic) can potentially beat Ω(n log n).

## Significance

Non-comparison sorting algorithms demonstrate that algorithmic lower bounds depend on the computational model: the Ω(n log n) barrier is not fundamental but conditional on using only comparisons. Counting sort and radix sort are critical in practice for sorting integers, strings, and fixed-format records. Radix sort is used in database systems for sorting integer keys, in suffix array construction algorithms, and in GPU-accelerated sorting where its regular memory access patterns outperform comparison sorts. Understanding when non-comparison sorts apply is essential for algorithm design and system performance optimization.

## Chunks Extracted

*Pending*
