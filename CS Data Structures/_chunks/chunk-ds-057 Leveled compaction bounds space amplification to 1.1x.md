---
tags: [cs-ds, chunk]
id: chunk-ds-057
source: "[[raw-ds-039]]"
supports: ["[[Hash Tables and Hash Functions]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Leveled compaction bounds space amplification to 1.1x

## Context
LSM compaction strategies trade between write read and space amplification.

## Claim
Leveled compaction limits each level to 10x the previous ensuring space amplification of at most 1.1x at the cost of higher write amplification of 10-30x versus size-tiered.

## Why It Matters
Critical design choice. Databases tune compaction strategy based on workload characteristics.

## QnA Seeds
- Q: Leveled vs size-tiered? -> A: Leveled: less space amp more write amp. Size-tiered: reverse.
- Q: Why 10x ratio between levels? -> A: Balances write and read amplification in practice.
