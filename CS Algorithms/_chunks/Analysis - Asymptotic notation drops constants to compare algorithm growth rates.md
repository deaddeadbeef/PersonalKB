---
id: chunk-csa-003
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapters 1–2"
topic: "analysis"
claim: "Asymptotic notation drops constants and lower-order terms to isolate the growth rate that determines scalability"
confidence: verified
supports:
  - "[[Asymptotic Notation]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Asymptotic notation drops constants to compare algorithm growth rates

## Context

For a function f(n) = 50n + 125, asymptotic analysis drops the constant 125 (lower-order term) and the coefficient 50, yielding Θ(n). The formal definition: f(n) = Θ(g(n)) if there exist positive constants c₁, c₂, n₀ such that c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀. O (upper bound) and Ω (lower bound) are the one-sided variants. Constants depend on implementation and hardware; order of growth depends only on the algorithm.

## Why It Matters

Asymptotic notation is the shared language for comparing algorithms independent of machine, language, or programmer. Without it, every benchmark would be implementation-specific. The notation makes statements like "merge sort is Θ(n lg n) in all cases" universal facts rather than machine-dependent measurements.

## QnA Seeds

- Q: What is the formal definition of Θ-notation?
- Q: Why is the 50 coefficient dropped in Θ(50n) = Θ(n)?
- Q: What is the difference between O and Θ?
