---
id: chunk-csa-152
type: chunk
source: "[[Vazirani 2003 - Approximation Algorithms]]"
source_loc: "PTAS and FPTAS"
topic: "approximation"
claim: "An FPTAS is polynomial in both n and 1/e achieving (1+e)-approximation, while a PTAS may be exponential in 1/e; the knapsack FPTAS runs in O(n squared over e)"
confidence: verified
supports:
  - "[[Approximation Algorithms]]"
  - "[[Knapsack Problem]]"
tags:
  - csa
  - csa/approximation
  - chunk
up: "[[CS Algorithms]]"
---
# Approximation — FPTAS vs PTAS and knapsack FPTAS in O(n squared over epsilon)

## Context

A Polynomial-Time Approximation Scheme (PTAS) achieves a (1+e)-approximation for any fixed e > 0, with running time polynomial in n but potentially exponential in 1/e. A Fully Polynomial-Time Approximation Scheme (FPTAS) is polynomial in both n and 1/e, making it practical for any desired accuracy. The knapsack FPTAS works by scaling and rounding item values to reduce the state space, then applying exact DP on the reduced instance, achieving O(n^2/e) time. This distinction is practically significant: a PTAS with O(n^(1/e)) time is useless for small e.

## Why It Matters

The PTAS/FPTAS distinction determines whether an approximation scheme is practically useful, and the knapsack FPTAS shows that near-optimal solutions to an NP-hard problem can be computed efficiently.

## QnA Seeds

- Q: What distinguishes an FPTAS from a PTAS in terms of running time?
- Q: How does the knapsack FPTAS achieve O(n^2/e) time?
- Q: Why is a PTAS with O(n^(1/e)) time impractical for small epsilon?
