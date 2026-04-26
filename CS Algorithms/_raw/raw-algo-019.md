---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Amortized Analysis: Aggregate, Accounting, and Potential Methods"
authors: "Robert Endre Tarjan"
year: 1985
---

# Amortized Analysis

## Summary
Amortized analysis determines the average cost per operation over a worst-case sequence of operations, providing tighter bounds than worst-case per-operation analysis when expensive operations are infrequent. Three techniques formalize this: the aggregate method (total cost divided by number of operations), the accounting method (assign amortized "charges" to each operation, banking surplus credit for future expensive operations), and the potential method (define a potential function on the data structure state, where amortized cost = actual cost + change in potential). Unlike average-case analysis, amortized analysis makes no probabilistic assumptions—it guarantees bounds for any operation sequence.

## Key Claims
- The aggregate method computes the total cost of n operations and divides by n; for dynamic array doubling, n appends cost at most 3n total work, giving O(1) amortized cost per append
- The accounting method assigns each operation an amortized cost that may differ from actual cost; the invariant is that total amortized cost ≥ total actual cost, ensured by maintaining non-negative "credit" stored in the data structure
- The potential method defines Φ(D_i) on data structure state D_i, with amortized cost ĉ_i = c_i + Φ(D_i) − Φ(D_{i-1}); if Φ(D_n) ≥ Φ(D_0), then Σĉ_i ≥ Σc_i, proving the amortized bound over any sequence
- Dynamic arrays (e.g., std::vector, Python list, Java ArrayList) achieve O(1) amortized append by doubling capacity when full; the potential Φ = 2n − capacity shows each append has amortized cost 3 (1 for the insertion + 2 banked for future copying)
- Union-find with union by rank and path compression achieves O(α(n)) amortized time per operation, where α is the inverse Ackermann function, proved by Tarjan using a sophisticated potential argument

## Atomic Facts
1. For a dynamic array starting at capacity 1, the sequence of n appends triggers doublings at sizes 1, 2, 4, 8, ..., 2^⌊log n⌋; total copying cost is 1 + 2 + 4 + ... + 2^⌊log n⌋ = 2^{⌊log n⌋+1} − 1 < 2n, so total cost including insertions is < 3n
2. The binary counter example: incrementing an n-bit counter starting from 0, each increment flips O(1) amortized bits because bit i flips every 2^i increments; total flips over n increments = Σ_{i=0}^{⌊log n⌋} ⌊n/2^i⌋ < 2n
3. Splay trees achieve O(log n) amortized time per operation using the potential Φ = Σ log(size(v)) over all nodes v (the access lemma); individual operations may take O(n) but any sequence of m operations on an n-node tree takes O((m + n) log n)
4. The inverse Ackermann function α(n) grows so slowly that α(2^{2^{2^{65536}}}) = 4; for all practical purposes, α(n) ≤ 4, making union-find operations effectively O(1)
5. Multi-pop stack: a sequence of n push, pop, and multi-pop operations costs O(n) total because each element is pushed at most once and popped at most once; amortized cost per operation is O(1) via the accounting method with $2 charged per push ($1 for push, $1 banked for future pop)
6. Fibonacci heaps use the potential Φ = t + 2m (t = trees, m = marked nodes) to prove O(1) amortized insert, O(1) amortized decrease-key, and O(log n) amortized extract-min; the cascading cut mechanism ensures at most O(log n) trees after consolidation

## Significance
Amortized analysis is an indispensable tool for understanding data structures whose individual operations vary widely in cost but whose sequences are efficient. Without amortized analysis, dynamic arrays would appear to have O(n) worst-case append (due to resizing), hash tables would appear to have O(n) worst-case insert (due to rehashing), and splay trees would appear to have O(n) worst-case search. The potential method in particular is the key technique behind the analysis of Fibonacci heaps, splay trees, and union-find—three of the most important advanced data structures. Mastery of amortized analysis separates superficial understanding of data structure costs from deep algorithmic literacy.

## Chunks Extracted
*Pending*
