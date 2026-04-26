---
id: chunk-csa-151
type: chunk
source: "[[Vazirani 2003 - Approximation Algorithms]]"
source_loc: "Set Cover"
topic: "approximation"
claim: "Greedy set cover achieves an H(n) approximation ratio where H(n) is ln(n) and this is essentially tight unless P equals NP"
confidence: verified
supports:
  - "[[Approximation Algorithms]]"
  - "[[Set Cover Problem]]"
tags:
  - csa
  - csa/approximation
  - chunk
up: "[[CS Algorithms]]"
---
# Approximation — Greedy set cover achieves O(log n) ratio and is tight

## Context

The greedy algorithm for set cover repeatedly picks the set covering the most uncovered elements. It achieves an approximation ratio of H(n) = 1 + 1/2 + ... + 1/n which is approximately ln(n). This is essentially the best possible: no polynomial-time algorithm can achieve o(log n) approximation unless P = NP. The proof of the ratio analyzes how uncovered elements decrease geometrically with each greedy choice, and the inapproximability result follows from the PCP theorem.

## Why It Matters

Set cover is the prototypical problem where logarithmic approximation is both achievable and provably optimal (under standard assumptions), illustrating the limits of efficient approximation.

## QnA Seeds

- Q: What is the greedy strategy for set cover and what ratio does it achieve?
- Q: Why is the O(log n) approximation ratio for set cover essentially tight?
- Q: How does the harmonic number H(n) arise in the greedy set cover analysis?
