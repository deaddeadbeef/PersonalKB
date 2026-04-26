---
id: chunk-csa-002
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 1"
topic: "analysis"
claim: "Algorithm choice matters as much as hardware — O(n lg n) beats O(n squared) even on a 1000x slower machine at large n"
confidence: verified
supports:
  - "[[Algorithm Definition]]"
  - "[[Asymptotic Notation]]"
tags:
  - csa
  - csa/analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Analysis — Algorithm choice matters as much as hardware

## Context

Cormen's concrete example: Computer A runs 1,000,000,000 operations per second and runs an O(n²) sort; Computer B runs 10,000,000 operations per second and runs an O(n lg n) sort (merge sort). For n = 10,000,000 (10 million elements), Computer A takes roughly 55 seconds; Computer B takes roughly 23 seconds. The slow machine with the better algorithm wins decisively, and the gap widens as n grows.

## Why It Matters

This is the central justification for studying asymptotic analysis. Hardware improvements are bounded by physics and economics; algorithm improvements can yield order-of-magnitude gains on any hardware. It also explains why the book focuses on order-of-growth rather than exact operation counts.

## QnA Seeds

- Q: Why do we drop constants in asymptotic analysis?
- Q: At what input size does algorithm choice overtake hardware speed?
- Q: What does it mean to say algorithms are a "technology" on par with hardware?
