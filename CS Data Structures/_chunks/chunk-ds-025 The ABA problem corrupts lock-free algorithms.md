---
tags: [cs-ds, chunk]
id: chunk-ds-025
source: "[[raw-ds-023]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# The ABA problem corrupts lock-free algorithms without version counters

## Context
CAS checks if value equals expected then swaps but value can change and change back.

## Claim
The ABA problem occurs when a value changes from A to B to A between a threads read and CAS. The CAS succeeds but the data structure state has changed. Solved by version counters or hazard pointers.

## Why It Matters
Subtle correctness bug in lock-free code and one of the hardest concurrency issues.

## QnA Seeds
- Q: What is the ABA problem? -> A: Value reverts to original between read and CAS making CAS falsely succeed.
- Q: How to prevent ABA? -> A: Version counter tagged pointer or hazard pointers.
