---
tags: [cs-ds, chunk]
id: chunk-ds-112
source: "[[raw-ds-003]]"
supports: ["[[Stacks and Queues]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Deque with circular buffer gives O1 push and pop at both ends

## Context
Arrays give O(1) at one end but O(n) at the other.

## Claim
A double-ended queue implemented with a circular buffer and two pointers gives O(1) amortized push and pop at both front and back with excellent cache performance.

## Why It Matters
Python collections.deque, Java ArrayDeque, and C++ std::deque all use this approach.

## QnA Seeds
- Q: How does front push work? -> A: Decrement front pointer modulo capacity then write.
- Q: When to resize? -> A: When front and back pointers collide indicating the buffer is full.
