---
tags: [cs-ds, chunk]
id: chunk-ds-080
source: "[[raw-ds-019]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Accounting method assigns credits to operations for amortized analysis

## Context
Some operations are cheap and some expensive. We need to show the average is bounded.

## Claim
The accounting method charges each cheap operation a little extra (saving credits) and uses those credits to pay for occasional expensive operations. If no operation goes into debt the amortized bound holds.

## Why It Matters
Intuitive alternative to potential method. Used to prove dynamic array append is O(1) amortized.

## QnA Seeds
- Q: How does it differ from potential method? -> A: Credits are per-operation, potential is per-state. Equivalent power.
- Q: Example for dynamic array? -> A: Charge 3 per insert. 1 for the insert, 2 saved to pay for copying during resize.
