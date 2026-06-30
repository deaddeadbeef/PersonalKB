---
id: au-ch-01
type: book-chapter
chapter: 1
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 3
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# AU — Chapter 01: What Are Algorithms and Why Should You Care?

## Summary

Cormen opens by establishing what distinguishes a computer algorithm from a vague human procedure: the algorithm must be precise enough that a machine can execute it without interpretation. Two properties matter above all — **correctness** (the algorithm produces a valid answer for every input in its problem specification) and **efficiency** (it uses computational resources economically). The chapter frames correctness as a spectrum: some problems allow probabilistic correctness (Miller-Rabin primality testing can be wrong, but the error probability is drivable below any threshold); others allow **approximation** (a result within a provable factor of optimal counts as correct by redefinition). Efficiency is captured through **order of growth**: a 1000× faster machine running an $O(n²)$ sort still loses to a slow machine running $O(n \lg n)$ once n reaches 10 million. This motivates the book's central thesis — algorithm choice is as consequential as hardware choice.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Algorithm | Finite, precise, machine-executable steps producing a solution |
| Correctness | Produces right answer for every valid input |
| Approximation algorithm | Guaranteed solution within factor α of optimal |
| Order of growth | Dominant term of running-time function; constants dropped |
| lg n | log₂ n; grows very slowly; basis of efficient algorithm comparisons |

## Chunk Candidates

- [x] [[Analysis - Algorithm correctness exists on a spectrum from exact to probabilistic to approximation]]
- [x] [[Analysis - Algorithm choice matters as much as hardware at large n]]
- [x] [[Analysis - Asymptotic notation drops constants to compare algorithm growth rates]]

## Wiki Pages Seeded

- [[Algorithm Definition]] — definition, precision requirement, correctness spectrum
- [[Asymptotic Notation]] — order of growth, why constants are dropped

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
