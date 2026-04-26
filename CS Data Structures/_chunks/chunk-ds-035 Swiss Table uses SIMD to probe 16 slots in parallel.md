---
tags: [cs-ds, chunk]
id: chunk-ds-035
source: "[[raw-ds-028]]"
supports: ["[[Hash Tables and Hash Functions]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Swiss Table uses SIMD to probe 16 slots in parallel

## Context
Traditional probing checks one slot at a time.

## Claim
Google's Swiss Table stores a metadata byte per slot and uses SIMD instructions to compare 16 metadata bytes in a single CPU instruction, dramatically reducing probe cost.

## Why It Matters
State-of-the-art hash table design — now the default in Abseil C++ and Rust hashbrown.

## QnA Seeds
- Q: What is the metadata byte? -> A: Top 7 bits of hash plus 1 control bit indicating empty/deleted/full.
- Q: Why 16 at once? -> A: SSE2 operates on 128-bit registers = 16 bytes simultaneously.
