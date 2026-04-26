---
tags: [cs-ds, chunk]
id: chunk-ds-139
source: "[[raw-ds-021]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Arena allocation frees all memory in one shot for phase-based programs

## Context
Individual malloc/free calls have overhead and risk memory leaks.

## Claim
Arena allocation pre-allocates a large memory block. Objects are allocated by bumping a pointer. At phase end the entire arena is freed in O(1). No individual frees needed.

## Why It Matters
Used in compilers (per-compilation-unit arena), web servers (per-request arena), and game engines (per-frame arena).

## QnA Seeds
- Q: What is the allocation cost? -> A: O(1) pointer bump. No free list search needed.
- Q: Main limitation? -> A: Cannot free individual objects. Only bulk free of entire arena.
