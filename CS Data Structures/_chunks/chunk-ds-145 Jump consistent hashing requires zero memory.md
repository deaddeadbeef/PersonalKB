---
tags: [cs-ds, chunk]
id: chunk-ds-145
source: "[[raw-ds-018]]"
supports: ["[[Consistent Hashing]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Jump consistent hashing requires zero memory for balanced distribution

## Context
Ring-based consistent hashing stores virtual node positions on the ring.

## Claim
Jump consistent hashing uses a mathematical formula with zero storage to map keys to N buckets. It achieves perfect balance and moves only 1/N keys on resize. But it only supports appending or removing the last bucket.

## Why It Matters
Ideal for systems where buckets are numbered sequentially like sharded databases with sequential shard IDs.

## QnA Seeds
- Q: Why zero memory? -> A: Bucket computed from hash using a deterministic pseudorandom jump formula.
- Q: Main limitation? -> A: Cannot remove arbitrary buckets. Only add/remove at the end.
