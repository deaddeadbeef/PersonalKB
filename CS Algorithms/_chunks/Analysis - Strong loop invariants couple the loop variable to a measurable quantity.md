---
id: chunk-csa-038
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 1 — Recursion"
topic: "analysis"
claim: "Strong loop invariants name the loop variable explicitly and couple it to a measurable quantity that tracks progress toward termination"
confidence: verified
supports:
  - "[[Loop Invariant]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Strong loop invariants couple the loop variable to a measurable quantity

## Context

Erickson distinguishes weak from strong loop invariants. A weak invariant states only that some property holds; a strong invariant additionally names the loop counter (or index variable) explicitly and ties the invariant to a concrete, measurable quantity — such as "after k iterations, the first k elements of A are sorted." This coupling serves two purposes: it makes maintenance proofs mechanical (incrementing k by 1 extends the sorted prefix by one element), and it makes the termination argument immediate (when k = n the invariant implies the full array is sorted). Without naming the counter, the invariant can be vacuously satisfied by an algorithm that does nothing.

## Why It Matters

Strong loop invariants are the difference between a proof sketch and a proof. In competitive and exam settings, a grader can confirm a strong invariant simply by substituting concrete values of the loop variable. They also make off-by-one errors in the algorithm immediately visible — if the invariant requires A[1..k] to be sorted after iteration k and the loop starts at k=0 rather than k=1, the initialization check fails and the bug surfaces before any testing.

## QnA Seeds

- Q: What distinguishes a strong loop invariant from a weak one?
- Q: Why is naming the loop variable in the invariant useful for the maintenance proof?
- Q: How does a strong loop invariant make termination arguments easier?
