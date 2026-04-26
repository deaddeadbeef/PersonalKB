---
id: chunk-csa-040
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 12 — NP-Hardness"
topic: "complexity"
claim: "Rice's Theorem states that every non-trivial semantic property of programs is undecidable, generalising the Halting Problem to a broad class of questions about program behaviour"
confidence: verified
supports:
  - "[[Halting Problem]]"
tags:
  - csa
  - csa/complexity
  - chunk
up: "[[CS Algorithms]]"
---
# Complexity — Rice's Theorem shows all non-trivial semantic program properties are undecidable

## Context

A **semantic property** of a program is one that depends on what the program *computes* (its input-output behaviour) rather than its syntactic structure (how many lines it has, what variable names it uses). A semantic property is **non-trivial** if some programs have it and some do not — it is neither universally true nor universally false.

Rice's Theorem (1953) states: every non-trivial semantic property of programs is **undecidable**. No algorithm can, for all programs P, correctly determine whether P has the property.

**Examples of undecidable questions by Rice's Theorem:**
- Does program P ever output the number 42?
- Does program P sort its input correctly?
- Does program P terminate on all inputs? (The Halting Problem is a special case.)
- Does program P compute the same function as program Q?

**Proof sketch**: Assume a decider for property S exists. Use it to construct a decider for the Halting Problem (already proven undecidable) — contradiction. The construction works for any non-trivial S because one can wire the halting computation into a wrapper program.

## Why It Matters

Rice's Theorem explains why general-purpose program analysis tools (bug detectors, automated testers, equivalence checkers) cannot be sound and complete simultaneously. Any tool that tries to decide a non-trivial semantic property must either miss true positives (false negatives) or produce false alarms (false positives) — not due to engineering limitations, but due to mathematical necessity. The Halting Problem is simply one instance of this broader impossibility.

## QnA Seeds

- Q: What is Rice's Theorem and what does it generalise?
- Q: Give three examples of undecidable program properties that follow from Rice's Theorem.
- Q: Why must every non-trivial semantic property be undecidable according to Rice's proof?
- Q: What distinguishes a semantic property from a syntactic property of a program?
