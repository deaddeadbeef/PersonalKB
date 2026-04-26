---
id: chunk-csos-184
type: chunk
source: "[[raw-os-034]]"
source_loc: "Log-Structured File Systems"
topic: "file-systems"
claim: "Garbage collection is the fundamental LFS challenge: dead blocks from overwritten files accumulate, requiring a cleaner to copy live data and reclaim segments"
confidence: verified
supports:
  - "[[Log-Structured File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — LFS garbage collection copies live data to reclaim space

## Context

Since data is never updated in place, old versions of blocks scatter throughout the log as dead data. A cleaner periodically identifies segments with high dead-block ratios, copies live blocks to the log head, and reclaims the space. Segment summary blocks record which inodes each block belongs to, enabling live-block identification. The cost-benefit policy selects segments by both dead-ratio and age for efficient cleaning.

## Why It Matters

Garbage collection determines LFS viability. Aggressive cleaning wastes bandwidth; insufficient cleaning causes space exhaustion. This same tradeoff appears in flash firmware, garbage-collected languages, and any system using log-structured storage.

## QnA Seeds

- Q: Why does LFS need garbage collection?
- Q: How does the cleaner identify which blocks in a segment are still live?
- Q: What policy does LFS use to select segments for cleaning?
