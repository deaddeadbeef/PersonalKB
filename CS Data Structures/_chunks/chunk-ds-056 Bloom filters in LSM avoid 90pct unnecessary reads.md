---
tags: [cs-ds, chunk]
id: chunk-ds-056
source: "[[raw-ds-039]]"
supports: ["[[B-Trees and B-Plus Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Bloom filters in LSM trees avoid 90pct of unnecessary disk reads

## Context
LSM trees may have the same key in multiple levels requiring multi-level search.

## Claim
Attaching a Bloom filter to each SSTable allows skipping levels that do not contain the query key avoiding roughly 90 percent of unnecessary disk reads.

## Why It Matters
Makes LSM read performance acceptable. Without Bloom filters LSM reads would be impractically slow.

## QnA Seeds
- Q: Where is the Bloom filter stored? -> A: In the SSTable metadata block loaded into memory.
- Q: What is the false positive cost? -> A: Occasional unnecessary disk read but no correctness impact.
