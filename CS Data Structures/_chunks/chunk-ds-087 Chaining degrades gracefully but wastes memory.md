---
tags: [cs-ds, chunk]
id: chunk-ds-087
source: "[[raw-ds-007]]"
supports: ["[[Collision Resolution Strategies]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Chaining degrades gracefully but wastes memory on pointer overhead

## Context
Hash collision resolution must handle keys mapping to the same bucket.

## Claim
Separate chaining stores colliding keys in linked lists per bucket. Performance degrades linearly with load factor but continues working for any load. Pointer overhead of 8 bytes per entry can double memory usage.

## Why It Matters
Simplest collision strategy. Default in Java HashMap. Predictable worst-case behavior.

## QnA Seeds
- Q: What is the expected chain length? -> A: alpha = n/m the load factor.
- Q: When does chaining beat open addressing? -> A: High load factors and when deletion is frequent.
