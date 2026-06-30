---
id: mos-ch-12
type: book-chapter
chapter: 12
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 2
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 12: Operating System Design

## Summary

The final chapter steps back from mechanisms to discuss OS design philosophy. Tanenbaum argues that the most important design principle is the separation of **mechanism** (what the system can do) from **policy** (decisions about when and how to use those mechanisms). This separation allows policy to change — for different workloads, users, or domains — without rewriting the underlying mechanism. Other principles discussed include simplicity (systems that are easy to reason about have fewer bugs), correctness over performance (get it right first; optimise later with measurement), and portability (abstracting hardware dependencies into a narrow HAL-like layer). The chapter examines why OS design is hard: conflicting goals (security vs convenience, performance vs safety), legacy constraints, and emergent complexity from interactions among independently correct subsystems. It closes with advice on measurement, avoiding premature optimisation, and thinking carefully about which layer should own each responsibility.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Mechanism vs policy | Mechanism: capability; policy: decision about using it — keep them separate |
| Simplicity | Fewer mechanisms, well understood, is better than many ad-hoc special cases |
| Correctness first | A fast wrong system is worse than a slow correct one |
| Layering | Assign each responsibility to exactly one layer; avoid cross-layer coupling |
| Measurement | Optimise based on profiling data, not intuition |

## Chunk Candidates

- [x] [[Design - Separating mechanism from policy lets policy evolve without rewriting mechanisms]]
- [x] [[Design - OS design requires balancing conflicting goals across security performance and portability]]

## Wiki Pages Seeded

- [[OS Design Principles]] — goals, trade-offs, simplicity, correctness, portability
- [[Mechanism vs Policy]] — separation principle; flexibility argument

## References

See [[Sources Index#Tanenbaum 2015]].
