---
tags: [cs-ds, chunk]
id: chunk-ds-004
source: "[[raw-ds-002]]"
supports: ["[[Doubly Linked Lists and Circular Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# DLL plus hash map gives O(1) LRU cache operations

## Context
LRU caches need O(1) access and O(1) eviction of least recently used item.

## Claim
Combining a DLL (O(1) move-to-front and remove-from-tail) with a hash map (O(1) key lookup) gives O(1) get and put for LRU caches.

## Why It Matters
This is the standard LRU cache implementation across databases, operating systems, and web servers.

## QnA Seeds
- Q: Why DLL for LRU instead of array? -> A: DLL supports O(1) removal at any position and O(1) front insertion.
- Q: What role does the hash map play? -> A: Maps keys to DLL nodes for O(1) lookup, avoiding O(n) traversal.
