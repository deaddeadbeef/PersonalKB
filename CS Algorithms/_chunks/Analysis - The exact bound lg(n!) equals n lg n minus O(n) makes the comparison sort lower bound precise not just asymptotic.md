---
id: chunk-csa-056
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 3 — Insertion Sort, Merge Sort, Binary Search"
topic: "analysis"
claim: "The exact expansion lg(n!) = n lg n − O(n) sharpens the comparison sort lower bound to a precise leading term, confirming that the Ω(n lg n) bound is tight and not merely an order-of-magnitude statement"
confidence: verified
supports:
  - "[[Comparison Sort Lower Bound]]"
tags:
  - csa
  - csa/analysis
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — The exact bound lg(n!) equals n lg n minus O(n) makes the comparison sort lower bound precise not just asymptotic

## Context

The decision-tree argument gives h ≥ lg(n!). The Ω(n lg n) lower bound follows from Stirling's approximation, but the MIT 6.006 treatment goes further: it derives the exact leading term.

**Derivation via logarithm telescoping**:

```
lg(n!) = lg(n) + lg(n−1) + … + lg(1)
       ≥ lg(n) + lg(n−1) + … + lg(n/2)          (drop the lower half)
       ≥ (n/2) · lg(n/2)                          (n/2 terms each ≥ lg(n/2))
       = (n/2)(lg n − 1)
       = (n/2) lg n − n/2
       = Ω(n lg n)
```

**Sharper form (Stirling)**:

```
lg(n!) = n lg n − n/ln 2 + O(lg n)
       = n lg n − O(n)
```

So the lower bound is precisely n lg n − O(n), not just Ω(n lg n). This means:

- The leading coefficient of the lower bound is 1 (in lg n terms).
- Merge sort, which uses exactly n lg n − O(n) comparisons in the worst case, achieves this leading coefficient and is therefore optimal — not merely asymptotically optimal but leading-coefficient optimal.
- Any comparison sort using fewer than (1 − ε) n lg n comparisons for constant ε > 0 is impossible.

## QnA Seeds

- Q: What is the exact value of lg(n!) to leading order, and what does it imply for comparison sorts?
- Q: How do you derive Ω(n lg n) from lg(n!) without Stirling's approximation?
- Q: In what sense is merge sort not just asymptotically optimal but leading-coefficient optimal?
