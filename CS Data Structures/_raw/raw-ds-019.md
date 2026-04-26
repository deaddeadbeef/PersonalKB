---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Amortized Analysis Methods"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Amortized Analysis Methods

## Summary

Amortized analysis determines the average cost per operation over a worst-case sequence. Three methods: aggregate (total cost / operations), accounting (charge more for cheap ops), potential (define potential function). Dynamic array doubling is the canonical example: occasional O(n) resize amortizes to O(1) per append.

## Key Claims

1. Amortized cost averages over worst-case sequences, not random inputs
2. Aggregate method: total cost divided by number of operations
3. Accounting method: overcharge cheap operations to pay for expensive ones
4. Potential method: define potential function tracking stored credit
5. Dynamic array doubling achieves amortized O(1) append

## Atomic Facts

1. Dynamic array: n appends cost at most 3n total (amortized O(1))
2. Splay tree: O(log n) amortized via potential method
3. Fibonacci heap decrease-key: O(1) amortized via cascading cuts
4. Union-Find: O(alpha(n)) amortized via path compression
5. Amortized != average case: amortized is worst-case over sequences
6. Individual operations can still be expensive (O(n) resize)

## Significance

Amortized analysis is essential for understanding data structures that have occasional expensive operations but excellent overall performance.

## Chunks Extracted

*Pending*
