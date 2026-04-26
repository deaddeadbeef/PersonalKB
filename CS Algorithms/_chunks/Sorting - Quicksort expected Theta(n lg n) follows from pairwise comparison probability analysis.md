---
id: chunk-csa-042
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 7 — Quicksort, Randomisation"
topic: "sorting"
claim: "Quicksort's expected Theta(n lg n) running time can be derived by summing over all pairs of elements the probability that those two elements are compared during the execution"
confidence: verified
supports:
  - "[[Quicksort]]"
tags:
  - csa
  - csa/sorting
  - chunk
up: "[[CS Algorithms]]"
---
# Sorting — Quicksort expected Theta(n lg n) follows from pairwise comparison probability analysis

## Context

The standard probabilistic analysis of randomised quicksort uses **indicator random variables** and **linearity of expectation**. Let X_{ij} = 1 if elements i and j (in sorted order) are ever compared during the algorithm's execution, and 0 otherwise. The total number of comparisons is X = Σ_{i<j} X_{ij}, and E[X] = Σ_{i<j} Pr[X_{ij} = 1].

**Key observation**: Elements i and j are compared if and only if one of them is chosen as the pivot before any element strictly between them (in sorted order) is chosen. This is because: once an element between i and j is chosen as a pivot, i and j end up in different subproblems and can never be compared. The elements i, j, and those between them are equally likely to be chosen first (uniform random pivot selection), so:

```
Pr[i and j are compared] = 2 / (j - i + 1)
```

Summing over all pairs: E[X] = Σ_{i<j} 2/(j−i+1) = Σ_{k=1}^{n} (n−k+1) · 2/(k+1) ≈ 2n · H(n) = Θ(n lg n), where H(n) is the n-th harmonic number.

## Why It Matters

This analysis gives a clean, information-theoretic reason why randomised quicksort runs in Θ(n lg n) on average for *any* input — not just random permutations. It demonstrates the power of probabilistic analysis: linearity of expectation allows summing over independent-looking random events even when the comparisons are not independent. This is a template argument reusable for other randomised algorithms.

## QnA Seeds

- Q: What is the probability that elements in positions i and j (sorted) are compared in randomised quicksort?
- Q: How does the pairwise comparison argument give E[comparisons] = Θ(n lg n)?
- Q: Why does choosing a pivot strictly between two elements prevent those elements from being compared?
- Q: How does linearity of expectation simplify the expected-comparisons calculation?
