---
tags: [cs-ds, chunk]
id: chunk-ds-001
source: "[[raw-ds-001]]"
supports: ["[[Arrays and Dynamic Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Dynamic arrays achieve amortized O(1) append via geometric resizing

## Context
Dynamic arrays double capacity when full, copying all elements in O(n).

## Claim
Geometric resizing (typically 2x) achieves amortized O(1) append because n appends cost at most 3n total, despite individual resizes costing O(n).

## Why It Matters
This makes dynamic arrays practical for growable collections -- the most common use case in programming.

## QnA Seeds
- Q: Why is dynamic array append amortized O(1)? -> A: Doubling means each element is copied at most O(log n) times total.
- Q: What growth factor do most implementations use? -> A: 2x (Java ArrayList, C++ vector) or 1.5x.
