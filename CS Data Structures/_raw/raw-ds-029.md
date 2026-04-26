---
tags: [cs-ds, raw]
id: raw-ds-029
source: "Introduction to Algorithms (CLRS, Ch. 19)"
up: "[[CS Data Structures]]"
---

# Binomial and Fibonacci Heaps

## Key Ideas
- Binomial heap: collection of binomial trees satisfying heap property
- Binomial tree B_k: 2^k nodes, formed by linking two B_{k-1} trees
- Binomial heap operations: insert O(log n), extract-min O(log n), merge O(log n)
- Key advantage: O(log n) merge (vs O(n) for binary heap)
- Fibonacci heap: lazier version — delay consolidation
- Fib heap insert: O(1) — just add to root list
- Fib heap decrease-key: O(1) amortized — cut and cascade
- Fib heap extract-min: O(log n) amortized — consolidate during extraction
- Fib heap delete: O(log n) amortized — decrease to -infinity then extract
- Cascading cuts: maintain tree balance — mark nodes, cut if child lost twice
- Fibonacci numbers arise in the potential function analysis (hence the name)
- Practical reality: Fibonacci heaps rarely used due to high constant factors and complexity
- Pairing heap: simpler alternative with good empirical performance (O(log n) amortized conjectured for decrease-key)

## Application Impact
- Dijkstra's: O(V log V + E) with Fibonacci heap vs O((V+E) log V) with binary heap
- Prim's MST: same improvement
- In practice: binary heap + indexed priority queue usually wins
