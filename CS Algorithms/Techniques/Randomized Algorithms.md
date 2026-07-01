---
tags: [cs-algorithms, techniques, randomized]
up: "[[Techniques Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, practice]
---

# Randomized Algorithms

> **One-line summary** Randomized algorithms use random choices to simplify design, improve expected performance, or trade deterministic guarantees for high-probability guarantees.

## Intuition

Randomness is useful when a fixed adversarial input can force a deterministic algorithm into bad behavior. By making part of the execution unpredictable, the algorithm can often avoid worst-case structure without needing to recognize that structure explicitly.

The classic example is randomized quicksort: choosing a pivot randomly makes the expected running time $O(n log n)$ regardless of the input order. Hash tables use related reasoning: a good randomized or universal hash function makes collisions unlikely enough that expected lookup cost stays constant.

## Core Patterns

- **Random sampling:** inspect a small random subset to estimate a property of a large input.
- **Randomized pivoting:** choose pivots or split points randomly to avoid bad deterministic choices.
- **Hash randomization:** choose hash functions from a family to limit adversarial collisions.
- **Monte Carlo algorithms:** run fast with a small probability of error.
- **Las Vegas algorithms:** always return a correct answer, but running time is random.

## Why It Matters

Randomization often turns brittle worst-case behavior into robust expected behavior. It is central to hashing, randomized quicksort, skip lists, randomized graph algorithms, streaming sketches, primality testing, and load balancing.

## Practice

1. Explain why randomized pivot selection protects quicksort from already-sorted input.
2. Compare Monte Carlo and Las Vegas guarantees.
3. Describe why a randomized hash function can be safer than a fixed hash function under adversarial input.

## References

- [[CS Algorithms/Sources/Sources Index]]
- [[CS Algorithms/Sorting/Quicksort]]
- [[CS Data Structures/Hash-Based Structures/Universal and Perfect Hashing]]
