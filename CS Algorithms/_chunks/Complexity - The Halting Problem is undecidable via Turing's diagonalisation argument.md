---
id: chunk-csa-022
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 10"
topic: "complexity"
claim: "The Halting Problem is undecidable — Turing proved in 1936 via diagonalisation that no algorithm can decide whether an arbitrary program halts"
confidence: verified
supports:
  - "[[NP Completeness]]"
  - "[[P vs NP]]"
  - "[[Halting Problem]]"
tags:
  - csa
  - csa/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Complexity — The Halting Problem is undecidable via Turing's diagonalisation argument

## Context

The Halting Problem: given a program P and input I, does P halt on I? Turing (1936) proved no algorithm H can solve this for all (P, I). The diagonalisation argument: suppose H exists. Construct a program D that calls H on itself — if H says D halts, D loops forever; if H says D loops, D halts. D's behaviour contradicts H's answer on input D, so H cannot exist. Undecidability is strictly harder than NP-completeness: an NP-complete problem at least has a deterministic algorithm (exponential), whereas the Halting Problem has no algorithm at all.

## Why It Matters

The Halting Problem establishes the fundamental limits of computation — not all well-posed questions have algorithmic answers. This is relevant to practical software engineering (you cannot write a general bug-detector), to formal verification (some program properties are undecidable), and to complexity theory (undecidability is the ceiling above which even exponential algorithms fail).

## QnA Seeds

- Q: How does Turing's diagonalisation argument prove the Halting Problem undecidable?
- Q: Is undecidability the same as NP-hardness?
- Q: What practical implications does the Halting Problem have for software tools?
