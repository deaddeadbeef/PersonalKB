---
id: chunk-csa-052
type: chunk
source: "[[MIT OCW 6006 - Introduction to Algorithms]]"
source_loc: "Lecture 14 — Cryptography"
topic: "cryptography"
claim: "A PRNG's security depends entirely on the seed being unpredictable: using a low-entropy value such as the current timestamp, process ID, or a fixed constant allows an attacker to enumerate all possible seeds and recover the keystream"
confidence: verified
supports:
  - "[[Random Number Generation]]"
tags:
  - csa
  - csa/cryptography
  - chunk
up: "[[CS Algorithms]]"
---
# Cryptography — PRNG security requires a high-entropy seed not a low-entropy value such as a timestamp

## Context

A pseudorandom number generator (PRNG) is a deterministic algorithm: given the same seed, it always produces the same output sequence. Security therefore reduces entirely to seed unpredictability. An adversary who can enumerate or predict the seed can regenerate the full pseudorandom output, breaking any cipher that relies on it.

**Low-entropy seed sources and their weaknesses**:
- **Current timestamp**: An attacker who knows approximately when a session was established can try all timestamps within a small window — often only thousands of values.
- **Process or session ID**: Typically a small integer with limited range. An attacker can enumerate the space quickly.
- **Fixed constant or hardcoded seed**: trivially known to any observer.
- **Combination of low-entropy sources**: combining two small-range values multiplies their cardinalities — but the product may still be small enough for exhaustive search.

**What high entropy looks like**: cryptographic PRNGs gather entropy from hardware events — interrupt timing, disk seek latency, network packet arrival jitter — which are difficult for an external attacker to observe or predict. A 128-bit seed from such a source has 2¹²⁸ possible values — computationally infeasible to enumerate.

## Why It Matters

The mathematical soundness of a PRNG algorithm provides no practical security if the seed is predictable. Algorithm correctness and implementation security are orthogonal concerns: a provably sound algorithm with a weak seed is broken. This chunk extends the Cormen PRBG chunk (chunk-csa-036) by specifying concretely what "unpredictable seed" means and what constitutes a failure.

## QnA Seeds

- Q: Why is using the current timestamp as a PRNG seed a security vulnerability?
- Q: What makes a seed "high entropy" for cryptographic purposes?
- Q: How would an attacker exploit a PRNG seeded with the process ID?
- Q: Why can a mathematically correct PRNG be broken in practice?
