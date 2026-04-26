---
id: chunk-csa-053
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 13 — Approximation Algorithms"
topic: "complexity"
claim: "The standard approximation-ratio proof template bounds the algorithm's output and OPT independently through the same intermediate structural quantity, avoiding the need to know OPT directly"
confidence: verified
supports:
  - "[[Approximation Algorithms]]"
tags:
  - csa
  - csa/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Complexity — Approximation proof template bounds algorithm output and OPT through a shared intermediate quantity

## Context

Proving an approximation ratio α is hard because OPT is unknown (if we could compute OPT efficiently, we would not need an approximation algorithm). Erickson's treatment identifies the standard template used in most ratio proofs:

1. **Identify an intermediate bound** B — a structural property of the problem instance (e.g., a matching, a fractional relaxation, a lower bound on OPT).
2. **Show OPT ≥ B** — the optimal solution cannot be better than the bound implies.
3. **Show ALG ≤ α · B** — the algorithm's output is at most α times that bound.
4. **Conclude ALG ≤ α · OPT** — by transitivity through B.

This template avoids examining OPT directly. The skill in designing approximation algorithms is finding the right intermediate B.

**Vertex cover example (instantiation)**: B = |matching M| selected during the greedy run. OPT ≥ |M| because any cover must hit every matching edge. ALG = 2|M| because both endpoints of each selected edge are added. Therefore ALG ≤ 2 · OPT. □

The template applies equally to maximisation problems, where the inequality directions reverse.

## QnA Seeds

- Q: Why can't an approximation-ratio proof directly compare the algorithm's output to OPT?
- Q: What three steps define the standard approximation proof template?
- Q: Apply the template to the 2-approximation for vertex cover: what is the intermediate bound B?
