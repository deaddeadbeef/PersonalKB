---
tags: [cs-ds, chunk]
id: chunk-ds-140
source: "[[raw-ds-023]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Epoch-based reclamation batches memory frees for lock-free structures

## Context
Lock-free structures cannot free memory while readers may hold references.

## Claim
Epoch-based reclamation tracks global and per-thread epochs. Memory retired in epoch e is safely freed only when all threads have advanced past e. This batches frees reducing overhead versus hazard pointers.

## Why It Matters
Used in Crossbeam (Rust) and many concurrent C++ libraries. Simpler than hazard pointers for most cases.

## QnA Seeds
- Q: When is memory safe to free? -> A: When all threads have observed an epoch after the one in which the memory was retired.
- Q: vs hazard pointers? -> A: Epoch is simpler but may delay freeing longer. Hazard pointers are more precise.
