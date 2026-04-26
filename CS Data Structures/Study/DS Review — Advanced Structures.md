---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
---

# DS Review — Advanced Structures

## Quick-Fire Questions

1. How do skip lists achieve $O(\log n)$ without rotations?
2. What is path compression in Union-Find? Why is it important?
3. When would you use a segment tree vs a Fenwick tree?
4. How does a Fenwick tree use the lowest set bit?
5. What is a k-d tree and when does it degrade?

## Compare and Contrast

| Structure | Build | Query | Update | Space | Best For |
|-----------|-------|-------|--------|-------|----------|
| Segment Tree | $O(n)$ | $O(\log n)$ | $O(\log n)$ | $O(4n)$ | General range queries |
| Fenwick Tree | $O(n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ | Prefix sums |
| Skip List | $O(n \log n)$ | $O(\log n)$* | $O(\log n)$* | $O(n)$* | Sorted set, concurrency |
| Union-Find | $O(n)$ | $O(alpha(n)$)* | $O(alpha(n)$)* | $O(n)$ | Dynamic connectivity |

*Expected/amortized
