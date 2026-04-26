---
tags: [cs-ds, chunk]
id: chunk-ds-066
source: "[[raw-ds-007]]"
supports: ["[[Hash Tables and Hash Functions]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Universal hashing eliminates adversarial worst-case input

## Context
A fixed hash function can always be defeated by an adversary who knows it.

## Claim
Universal hashing randomly selects a hash function from a family at runtime. For any fixed input set the expected number of collisions is n/m making adversarial attacks impossible.

## Why It Matters
Prevents hash-flooding DoS attacks and gives provable expected O(1) performance.

## QnA Seeds
- Q: What is a universal hash family? -> A: For any two distinct keys probability of collision is at most 1/m.
- Q: Real-world example? -> A: SipHash used in Python and Rust hash maps to prevent HashDoS.
