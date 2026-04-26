---
tags: [cs-ds, chunk]
id: chunk-ds-109
source: "[[raw-ds-039]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Write amplification in LSM trees ranges from 10x to 30x

## Context
LSM trees rewrite data during compaction amplifying the total bytes written.

## Claim
Leveled compaction rewrites each key approximately 10-30 times as it migrates through levels. Write amplification = total bytes written to disk divided by bytes written by user.

## Why It Matters
Primary cost concern for SSDs where write endurance is limited. WiscKey and other designs aim to reduce write amp.

## QnA Seeds
- Q: Why so high? -> A: Each level compaction rewrites all overlapping SSTables merging with next level.
- Q: How does WiscKey reduce it? -> A: Separate keys from values. Only keys in LSM so less data rewritten.
