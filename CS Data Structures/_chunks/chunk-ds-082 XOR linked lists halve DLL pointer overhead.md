---
tags: [cs-ds, chunk]
id: chunk-ds-082
source: "[[raw-ds-002]]"
supports: ["[[Doubly Linked Lists and Circular Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# XOR linked lists halve DLL pointer overhead using bitwise tricks

## Context
DLLs store both prev and next pointers doubling overhead versus SLLs.

## Claim
XOR linked lists store prev XOR next in a single pointer field. Given either neighbor the other is recovered via XOR. This halves pointer overhead while preserving bidirectional traversal.

## Why It Matters
Historical curiosity demonstrating space optimization. Rarely used today due to GC incompatibility and debugging difficulty.

## QnA Seeds
- Q: How to traverse forward? -> A: next = stored_value XOR prev_address.
- Q: Why not widely used? -> A: Incompatible with garbage collectors and makes debugging very hard.
