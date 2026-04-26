---
id: chunk-csa-149
type: chunk
source: "[[Vazirani 2003 - Approximation Algorithms]]"
source_loc: "Vertex Cover"
topic: "approximation"
claim: "Vertex cover has a simple 2-approximation in O(V+E): repeatedly pick any uncovered edge and add both endpoints"
confidence: verified
supports:
  - "[[Approximation Algorithms]]"
  - "[[Vertex Cover]]"
tags:
  - csa
  - csa/approximation
  - chunk
up: "[[CS Algorithms]]"
---
# Approximation — Vertex cover 2-approximation adds both endpoints of uncovered edges

## Context

The 2-approximation for vertex cover works by repeatedly selecting any uncovered edge and adding both endpoints to the cover. Since the optimal solution must include at least one endpoint of every selected edge, and the algorithm adds exactly two per edge, the cover is at most twice the minimum. This runs in O(V + E) time. Achieving a ratio better than 2 - e remains a major open problem, connected to the Unique Games Conjecture—making this simple algorithm remarkably close to the best possible polynomial-time guarantee.

## Why It Matters

This is the simplest meaningful approximation algorithm and illustrates the core proof technique: bounding the algorithm's output and OPT through a shared quantity (the matching).

## QnA Seeds

- Q: Why does the edge-picking vertex cover algorithm guarantee a 2-approximation ratio?
- Q: What is the relationship between vertex cover approximation and the Unique Games Conjecture?
- Q: What shared quantity bounds both the algorithm's output and OPT in this proof?
