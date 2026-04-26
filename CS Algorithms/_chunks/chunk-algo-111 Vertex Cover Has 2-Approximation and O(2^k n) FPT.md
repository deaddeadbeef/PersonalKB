---
id: chunk-algo-111
type: chunk
source: "[[raw-algo-018]]"
source_loc: "NP-Completeness Theory - Atomic Facts"
topic: "complexity"
claim: "Vertex Cover is NP-complete but admits a 2-approximation (both endpoints of any maximal matching) and a fixed-parameter tractable algorithm in O(2^k * n) for cover size k, showing NP-hardness does not preclude practical solutions."
confidence: verified
supports:
  - "[[NP-Completeness]]"
  - "[[Approximation Algorithms]]"
tags:
  - cs-algorithms
  - cs-algorithms/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Vertex Cover Has 2-Approximation and O(2^k n) FPT

## Context

The 2-approximation works because a maximal matching has size at most the minimum cover (each edge needs at least one endpoint covered). Taking both endpoints at most doubles the optimal. The FPT algorithm branches on each uncovered edge: include one endpoint or the other, creating a search tree of depth k with branching factor 2. For k=30, 2^30 ~ 10^9 is tractable. These exemplify the two main NP-coping strategies: approximation with provable ratios and parameterized tractability.

## Why It Matters

Vertex Cover is the poster child for NP-complete problems that remain practically solvable. The 2-approximation is the simplest approximation algorithm to teach, and the FPT algorithm introduces parameterized complexity.

## QnA Seeds

- Q: How does the maximal matching 2-approximation for Vertex Cover work?
- Q: What is the FPT algorithm for Vertex Cover?
- Q: Why does NP-completeness not preclude efficient Vertex Cover solutions?