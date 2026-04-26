---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Maximum Subarray Problem and Kadane's Algorithm"
authors: [Jon Bentley]
year: 1984
---

## Summary

The maximum subarray problem asks for the contiguous subarray within a one-dimensional array of numbers that has the largest sum. This classic problem, popularized by Jon Bentley in his "Programming Pearls" column, admits solutions at multiple complexity levels, making it an ideal case study in algorithm design. The brute-force approach examines all O(n²) subarrays in O(n²) time (or O(n³) without prefix sums). A divide-and-conquer approach achieves O(n log n): split the array in half, recursively find the maximum subarray in each half, and find the maximum subarray crossing the midpoint in O(n), then take the overall maximum. Kadane's algorithm achieves the optimal O(n) time using dynamic programming. It maintains a running variable current_max representing the maximum subarray sum ending at the current position: at each step, current_max = max(A[i], current_max + A[i]). This captures the key insight—either extend the previous maximum subarray by including A[i], or start a new subarray at A[i]. A global variable best_max tracks the overall maximum seen. The algorithm requires O(1) space and a single pass through the array. Originally described by Jay Kadane in response to a problem posed by Ulf Grenander (for a 2D maximum subarray in image processing), the 1D solution reduces a quadratic problem to linear time. The 2D extension—finding the maximum-sum subrectangle in an m×n matrix—can be solved in O(m²n) by fixing two rows and applying Kadane's algorithm to column prefix sums between them. Applications include financial analysis (maximum profit over consecutive days), bioinformatics (finding regions of high activity in genomic sequences), and image processing (maximum brightness region).

## Key Claims

1. Kadane's algorithm solves the maximum subarray problem in O(n) time and O(1) space with a single pass, which is optimal since every element must be examined.
2. The DP recurrence current_max = max(A[i], current_max + A[i]) captures the core decision: extend the current subarray or start fresh at position i.
3. The divide-and-conquer solution in O(n log n) illustrates the paradigm cleanly but is suboptimal compared to Kadane's linear scan.
4. The 2D maximum subrectangle problem reduces to O(n) applications of Kadane's algorithm over O(m²) row-pair combinations, yielding O(m²n) time for an m×n matrix.
5. The problem serves as a canonical example of how different algorithmic paradigms (brute force, divide and conquer, dynamic programming) yield progressively better solutions to the same problem.

## Atomic Facts

1. Kadane's algorithm initializes current_max = A[0] and best_max = A[0], then iterates from index 1 to n−1, updating both variables at each step.
2. For all-negative arrays, Kadane's algorithm correctly returns the largest (least negative) single element, provided the implementation uses max(A[i], current_max + A[i]) rather than max(0, current_max + A[i]).
3. The divide-and-conquer solution has recurrence T(n) = 2T(n/2) + O(n), resolving to O(n log n) by the Master Theorem (Case 2).
4. To recover the actual subarray (not just the sum), track the start and end indices, resetting start when a new subarray begins (when A[i] > current_max + A[i]).
5. The 2D extension computes prefix sums over columns for each pair of rows (top, bottom), then applies 1D Kadane on the resulting 1D array of column sums.
6. A variant allowing at most one deletion (removing one element from the subarray) can be solved in O(n) time using two passes: left-to-right and right-to-left maximum subarray values.

## Significance

The maximum subarray problem is one of the most celebrated examples in algorithm pedagogy, demonstrating how problem analysis and the right paradigm choice can yield order-of-magnitude improvements. Kadane's algorithm shows the power of dynamic programming in transforming a seemingly quadratic problem into a linear-time solution. In finance, it models the maximum profit from buying and selling a stock (on consecutive-day returns); in bioinformatics, it identifies regions of biological significance in sequence data. The problem's scalability from 1D to 2D and its connections to other DP problems make it a versatile teaching tool and a practical algorithm in signal processing and data analysis.

## Chunks Extracted

chunk-algo-181 through chunk-algo-184
