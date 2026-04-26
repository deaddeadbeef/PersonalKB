---
tags: [cs-algorithms, raw]
source_type: journal_paper
source_title: "Quicksort"
authors: "C.A.R. Hoare"
year: 1962
---

# Quicksort Analysis

## Summary
Quicksort is a divide-and-conquer sorting algorithm that partitions an array around a pivot element, recursively sorting the resulting subarrays. It achieves an average-case time complexity of O(n log n) but degrades to O(n²) in the worst case when pivot selection is poor. The randomized variant eliminates adversarial worst-case inputs by selecting pivots uniformly at random, making O(n²) behavior extremely unlikely in practice.

## Key Claims
- Quicksort's average-case running time is O(n log n) with a small constant factor, making it one of the fastest general-purpose comparison sorts in practice
- The worst-case O(n²) behavior occurs when the pivot consistently produces maximally unbalanced partitions (e.g., already sorted input with first-element pivot)
- Randomized quicksort achieves expected O(n log n) time regardless of input distribution, with the expectation taken over random pivot choices
- Quicksort is an in-place algorithm requiring only O(log n) auxiliary stack space on average, compared to mergesort's O(n) extra space
- Despite being unstable (equal elements may be reordered), quicksort typically outperforms mergesort on arrays due to better cache locality and lower constant factors

## Atomic Facts
1. Hoare's original partition scheme uses two converging pointers and performs approximately n/2 swaps on average per partition call, compared to Lomuto's scheme which performs up to n swaps
2. The average number of comparisons made by quicksort is approximately 2n ln n ≈ 1.39n log₂ n, which is only 39% more than the information-theoretic lower bound of n log₂ n
3. Median-of-three pivot selection reduces the expected number of comparisons to approximately 1.188n log₂ n and eliminates the sorted-input worst case
4. The probability that randomized quicksort exceeds 4n ln n comparisons on any input of size n is at most 1/n, by a Chernoff bound argument
5. Quicksort's cache performance is superior because it accesses elements sequentially within each partition call, resulting in O(n/B · log(n/M)) cache misses in the external memory model (where B is block size and M is cache size)
6. Introsort (used in C++ std::sort) switches from quicksort to heapsort after O(log n) recursion depth, guaranteeing O(n log n) worst case while retaining quicksort's practical speed

## Significance
Quicksort remains the most widely used sorting algorithm in practice, forming the basis of standard library sort implementations in C, C++, Java (for primitives), and many other languages. Hoare's 1962 paper introduced not just the algorithm but also the partition subroutine that became fundamental to selection algorithms (quickselect) and the study of randomized algorithms. The analysis of quicksort's average case using indicator random variables is a canonical example in probabilistic analysis of algorithms.

## Chunks Extracted
*Pending*
