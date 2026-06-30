---
tags: [csa, csa/divide-and-conquer]
up: "[[CS Algorithms|CS Algorithms Index]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Divide and Conquer Overview

> **One-line summary**: Divide and conquer solves problems by recursively breaking them into smaller, independent sub-problems, solving each, and combining the results.

## 🎯 Intuition
**The Core Idea:** Split the problem in half (or more), conquer each piece recursively, then stitch the answers back together.
**Analogy:** Sorting a deck of cards — split the deck into two halves, sort each half separately, then merge the two sorted halves into one. That's Merge Sort, the poster child of D&C.
**Why It Matters:** D&C is the backbone of algorithms like Merge Sort ($O(n \log n)$), Quick Sort, binary search, Strassen's matrix multiplication, and the FFT — some of the most important algorithms in computer science.

---

## ⚙️ Core Mechanics
### The Three Steps
1. **Divide** — Break the problem into sub-problems of the same type.
2. **Conquer** — Solve each sub-problem recursively; base cases are solved directly.
3. **Combine** — Merge sub-problem solutions into a solution for the original problem.

### Recurrence Relations
Most D&C algorithms produce a recurrence of the form:
```
T(n) = a·T(n/b) + f(n)
```
where `a` = number of sub-problems, `n/b` = size of each, and `f(n)` = cost of dividing + combining.

### Pseudocode (Generic D&C)
```
function DivideAndConquer(problem):
    if problem is small enough:
        return BaseSolve(problem)
    sub1, sub2, ... = Divide(problem)
    sol1 = DivideAndConquer(sub1)
    sol2 = DivideAndConquer(sub2)
    ...
    return Combine(sol1, sol2, ...)
```

### Complexity

| Algorithm | Recurrence | Time |
|-----------|-----------|------|
| Binary Search | T(n) = T(n/2) + $O(1)$ | $O(\log n)$ |
| Merge Sort | T(n) = 2T(n/2) + $O(n)$ | $O(n \log n)$ |
| Quick Sort (avg) | T(n) = 2T(n/2) + $O(n)$ | $O(n \log n)$ |
| Strassen | T(n) = 7T(n/2) + $O(n²)$ | $O(n^2.81)$ |
| Karatsuba | T(n) = 3T(n/2) + $O(n)$ | $O(n^1.585)$ |

### Key Facts
- The "combine" step is often where the real cleverness lies (e.g., the merge in Merge Sort, the linear-time combine in closest-pair).
- D&C naturally maps to parallel computation since sub-problems are independent.
- Tail-recursive D&C (like binary search) can be converted to iteration.
- Excessive recursion depth can blow the call stack; consider iterative or hybrid approaches for very large inputs.

---

## 🔬 Deep Dive
### Master Theorem (Quick Reference)
For T(n) = aT(n/b) + $\Theta(nᶜ)$:
- **Case 1:** If c < log_b(a), then T(n) = $\Theta(n^{log_b(a)})$.
- **Case 2:** If c = log_b(a), then T(n) = $\Theta(nᶜ \log n)$.
- **Case 3:** If c > log_b(a) and regularity condition holds, then T(n) = $\Theta(nᶜ)$.

See [[Master Theorem Applications]] for worked examples.

### Edge Cases and Pitfalls
- **Unbalanced splits** — Quick Sort degrades to $O(n²)$ when the pivot is always the smallest or largest element.
- **Not all problems divide cleanly** — sometimes sub-problems overlap (→ use DP instead).
- **Off-by-one in index arithmetic** — a common bug when implementing the divide step.
- **Stack overflow** — deep recursion on large inputs; consider increasing stack size or using an iterative approach.

### Comparison with Alternatives
- **Dynamic Programming** — use when sub-problems overlap; D&C recomputes them.
- **Greedy** — use when a locally optimal choice is globally optimal; D&C doesn't assume this.
- **Decrease and Conquer** — reduces the problem by a constant (e.g., insertion sort removes one element at a time), not a fraction.

### Real-World Usage
- **Merge Sort** — default sort in Java (TimSort is hybrid merge + insertion), Python (also TimSort).
- **Quick Sort** — default in C++ `std::sort`, often with intro-sort fallback.
- **FFT (Fast Fourier Transform)** — signal processing, polynomial multiplication, image compression.
- **Closest pair of points** — computational geometry in GIS and graphics.
- **Strassen's matrix multiply** — used in large-scale scientific computing libraries.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Identify the Divide, Conquer, and Combine steps for Merge Sort.
2. Write the recurrence for an algorithm that splits the input into 3 parts of size n/3 and does $O(n)$ combine work. What is its complexity?
3. Why is D&C not appropriate for the Fibonacci sequence?

### Core Problems
1. **Count Inversions** — Modify Merge Sort to count the number of inversions in an array in $O(n \log n)$. *Approach:* count cross-inversions during the merge step.
2. **Maximum Subarray (D&C version)** — Find the contiguous subarray with the largest sum using a divide-and-conquer approach in $O(n \log n)$.

### Challenge
- **Closest Pair of Points in 2D**: Implement the $O(n \log n)$ divide-and-conquer algorithm. Handle the "strip" merging step correctly and prove why checking only 7 points per strip element suffices.

---

*See also:* [[Master Theorem Applications]] · [[Merge Sort]] · [[Quicksort|Quick Sort]] · [[Greedy Algorithms Overview]] · [[Dynamic Programming|Dynamic Programming Overview]] | **CS Data Structures:** [[Arrays and Dynamic Arrays|Arrays]] · Recursion and Call Stack

## References
-> [[Sources Index]]
