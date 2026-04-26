---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Binary Search and Its Variants"
authors: "Jon Bentley"
year: 1986
---

# Binary Search and Variants

## Summary
Binary search is a fundamental algorithm for locating elements in a sorted array with O(log n) time complexity, making at most ⌈log₂ n⌉ + 1 comparisons. Despite its apparent simplicity, correct implementation is notoriously difficult—Bentley famously noted that only about 10% of professional programmers can write a bug-free binary search. The comparison-based lower bound proof establishes that Ω(log n) is optimal for searching in a sorted array, and numerous practical variants (lower_bound, upper_bound, interpolation search) extend the basic idea to solve a wide range of problems.

## Key Claims
- Binary search requires exactly ⌊log₂ n⌋ + 1 comparisons in the worst case, which is optimal among comparison-based search algorithms on sorted arrays
- The lower bound proof uses a decision tree argument: any comparison-based algorithm must distinguish among n+1 outcomes (n elements plus "not found"), requiring a tree of height at least ⌈log₂(n+1)⌉
- Lower_bound (first element ≥ target) and upper_bound (first element > target) variants are more useful in practice than exact-match binary search, enabling range queries and counting
- Interpolation search achieves O(log log n) expected time on uniformly distributed data by estimating the target's position proportionally, but degrades to O(n) on adversarial inputs
- Binary search on the answer (parametric search) transforms optimization problems into decision problems, applicable whenever the feasibility function is monotonic

## Atomic Facts
1. For an array of n = 1,000,000 elements, binary search makes at most 20 comparisons (⌊log₂ 1,000,000⌋ + 1 = 20), compared to 1,000,000 for linear search in the worst case
2. The classic off-by-one bug in binary search (using mid = (low + high) / 2) causes integer overflow for arrays larger than 2³⁰ elements; the fix is mid = low + (high − low) / 2
3. C++ STL std::lower_bound performs exactly ⌈log₂(n) + 1⌉ comparisons and is implemented using a branchless variant on modern compilers for better branch prediction
4. Interpolation search on n uniformly distributed keys performs O(log log n) comparisons on average, proved by Perl, Itai, and Avni (1978); for n = 10⁹, this is roughly 5 comparisons vs 30 for binary search
5. Exponential search (galloping) finds the range in O(log k) where k is the position of the target, then applies binary search; total cost is O(log k), which is superior when the target is near the beginning
6. Fractional cascading allows binary search across k sorted lists sharing elements in O(log n + k) total time instead of O(k log n), with applications in computational geometry range trees

## Significance
Binary search is arguably the most important algorithm in computer science after sorting. Its principle—halving the search space with each step—underlies everything from database index lookups (B-trees perform multi-way binary search) to debugging (git bisect), numerical methods (bisection method for root-finding), and competitive programming (binary search on the answer). The lower bound proof for comparison-based searching is one of the simplest and most elegant information-theoretic arguments, serving as a gateway to understanding computational complexity.

## Chunks Extracted
*Pending*
