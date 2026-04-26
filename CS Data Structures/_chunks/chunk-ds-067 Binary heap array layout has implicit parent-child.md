---
tags: [cs-ds, chunk]
id: chunk-ds-067
source: "[[raw-ds-008]]"
supports: ["[[Binary Heaps and Heapsort]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Binary heap array layout has implicit parent-child via index arithmetic

## Context
Trees normally require explicit pointers between nodes.

## Claim
A binary heap stored in an array uses index arithmetic: parent of i is floor(i/2) and children are 2i and 2i+1. No pointers needed giving perfect cache utilization and zero memory overhead.

## Why It Matters
Most space-efficient tree representation. This is why heaps are the default priority queue implementation.

## QnA Seeds
- Q: How to find parent of node i? -> A: floor(i/2) in 1-indexed array.
- Q: Why better than pointer-based tree? -> A: Zero pointer overhead and contiguous memory for cache efficiency.
