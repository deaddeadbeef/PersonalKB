---
tags: [cs-ds, chunk]
id: chunk-ds-101
source: "[[raw-ds-023]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Read-Copy-Update lets readers proceed with zero synchronization

## Context
Reader-writer locks still block readers during writes.

## Claim
RCU allows readers to access shared data with zero locks or atomic operations. Writers create a new version and wait for all pre-existing readers to finish before freeing old version. Readers always see a consistent snapshot.

## Why It Matters
Linux kernel uses RCU for routing tables, file system caches, and module lists where reads vastly outnumber writes.

## QnA Seeds
- Q: How do readers synchronize? -> A: They dont. They read current pointer which always points to valid data.
- Q: How is old version freed? -> A: Writer waits for a grace period ensuring no reader holds old reference.
