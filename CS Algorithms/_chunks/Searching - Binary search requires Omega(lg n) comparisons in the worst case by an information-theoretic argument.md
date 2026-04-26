---
id: chunk-csa-044
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 3 — Sorting and Searching"
topic: "searching"
claim: "Binary search is optimal: any comparison-based algorithm for searching a sorted array requires Omega(lg n) comparisons in the worst case, by an information-theoretic argument"
confidence: verified
supports:
  - "[[Binary Search]]"
tags:
  - csa
  - csa/searching
  - chunk
up: "[[CS Algorithms]]"
---
# Searching — Binary search requires Omega(lg n) comparisons in the worst case by an information-theoretic argument

## Context

The Ω(lg n) lower bound for searching a sorted array follows from a simple information-theoretic argument. The search problem has n+1 distinct outcomes: the target is at position 1, 2, …, n, or absent. Each three-way comparison (less than, equal, greater than) partitions the remaining possibilities into at most three groups. After k comparisons, at most 3^k outcomes have been distinguished. To distinguish all n+1 outcomes, we need 3^k ≥ n+1, so k ≥ log₃(n+1) = Ω(lg n).

For binary comparisons (less-or-equal / greater), the argument gives 2^k ≥ n+1, so k ≥ ⌈lg(n+1)⌉ — exactly the number of comparisons binary search uses in the worst case.

**Interpretation**: Every comparison yields at most one bit of information. Distinguishing among n+1 outcomes requires at least lg(n+1) bits. Binary search is information-theoretically optimal — it extracts the maximum possible information from each comparison by always halving the search space.

## Why It Matters

This lower bound establishes that binary search cannot be improved upon (within the comparison model) — no clever comparison-based algorithm can search a sorted array in o(lg n) worst-case comparisons. The argument also illustrates the information-theoretic lower bound technique, which applies more broadly: sorting Ω(n lg n) uses the same structure (decision tree over n! permutations).

## QnA Seeds

- Q: Why does searching a sorted array require at least Ω(lg n) comparisons?
- Q: What does the information-theoretic argument say about the number of outcomes that k comparisons can distinguish?
- Q: In what sense is binary search optimal for searching a sorted array?
- Q: How does the lower bound argument for binary search relate to the Ω(n lg n) sorting lower bound?
