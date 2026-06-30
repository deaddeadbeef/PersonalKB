---
id: au-ch-02
type: book-chapter
chapter: 2
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 5
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# AU — Chapter 02: How to Describe and Evaluate Computer Algorithms

## Summary

Chapter 2 builds the notational and proof vocabulary used throughout the rest of the book. Cormen introduces the **RAM model**: a single processor, one unit cost per basic operation, uniform memory access — the standard abstraction that makes complexity analysis machine-independent. He formalises the three asymptotic notations (Θ for tight bounds, O for upper bounds, Ω for lower bounds) using worked examples from linear-search variants, showing how to count operations and extract the dominant term. The chapter then introduces **loop invariants** — a three-part proof technique (initialization, maintenance, termination) for proving algorithm correctness, analogous to mathematical induction. It closes with two design paradigms: **divide-and-conquer** (split, recurse, combine; running time captured by a recurrence relation) and **dynamic programming** (exploit overlapping subproblems by storing results in a table).

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| RAM model | One unit per basic op; uniform memory cost; machine-independent analysis |
| Θ-notation | Tight bound: both upper and lower bounded by c·g(n) for large n |
| O-notation | Upper bound: f(n) ≤ c·g(n) for large n |
| Ω-notation | Lower bound: f(n) ≥ c·g(n) for large n |
| Loop invariant | Property true before loop, maintained each step, implies correctness at termination |
| Recurrence relation | Running-time formula expressed in terms of smaller input sizes |
| Divide-and-conquer | Split → recurse → combine; e.g., T(n) = 2T(n/2) + $\Theta(n)$ for merge sort |
| Dynamic programming | Bottom-up table of overlapping subproblem solutions to avoid recomputation |

## Chunk Candidates

- [x] [[Analysis - The RAM model treats each basic operation as unit cost]]
- [x] [[Analysis - Asymptotic notation drops constants to compare algorithm growth rates]]
- [x] [[Analysis - Loop invariants provide a three-part correctness proof structure]]
- [x] [[Analysis - Divide-and-conquer running time is expressed as a recurrence relation]]
- [x] [[Analysis - Dynamic programming solves problems with overlapping subproblems by memoising a table]]

## Wiki Pages Seeded

- [[Asymptotic Notation]] — formal definitions and intuition
- [[Loop Invariant]] — three-part proof structure

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
