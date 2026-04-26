---
tags: [cs-ds, chunk]
id: chunk-ds-024
source: "[[raw-ds-023]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Lock-free guarantees system-wide progress without deadlock

## Context
Lock-based concurrency can deadlock or have priority inversion.

## Claim
Lock-free data structures guarantee at least one thread makes progress in any bounded number of steps, eliminating deadlock by design using CAS operations.

## Why It Matters
Critical for real-time systems and high-throughput servers.

## QnA Seeds
- Q: Lock-free vs wait-free? -> A: Lock-free: one thread progresses. Wait-free: every thread in bounded steps.
- Q: What hardware primitive enables lock-free? -> A: Compare-and-Swap CAS.
