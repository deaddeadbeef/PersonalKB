---
id: chunk-csa-150
type: chunk
source: "[[Vazirani 2003 - Approximation Algorithms]]"
source_loc: "Metric TSP"
topic: "approximation"
claim: "Christofides algorithm achieves a 3/2-approximation for metric TSP by combining MST cost at most OPT with minimum perfect matching cost at most OPT/2"
confidence: verified
supports:
  - "[[Approximation Algorithms]]"
  - "[[Traveling Salesman Problem]]"
tags:
  - csa
  - csa/approximation
  - chunk
up: "[[CS Algorithms]]"
---
# Approximation — Christofides 3/2-approximation for metric TSP

## Context

Christofides' algorithm (1976) for TSP with triangle inequality: (1) compute an MST (cost <= OPT), (2) find a minimum-weight perfect matching on odd-degree MST vertices (cost <= OPT/2), (3) combine into an Eulerian circuit, (4) shortcut to a Hamiltonian tour. The total cost is at most 3/2 * OPT. This was the best known ratio for 45 years until Karlin, Klein, and Oveis Gharan achieved a slight improvement in 2021. General TSP without metric has no constant-factor approximation unless P = NP.

## Why It Matters

Christofides' algorithm is one of the most celebrated results in approximation algorithms and demonstrates how combining multiple algorithmic tools (MST, matching, Euler tour) yields strong guarantees.

## QnA Seeds

- Q: What are the four steps of Christofides' algorithm for metric TSP?
- Q: Why does the perfect matching on odd-degree vertices cost at most OPT/2?
- Q: Why can't general TSP (without triangle inequality) be approximated within any constant factor?
