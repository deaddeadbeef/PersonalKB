---
id: chunk-csos-097
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4 — ext4 and Linux File Systems"
topic: "file-systems"
claim: "Delayed allocation (allocate-on-flush) defers physical block allocation until data is actually written to disk, enabling the allocator to see the full size of pending writes and make better contiguous allocation decisions"
confidence: verified
supports:
  - "[[File System Implementation]]"
  - "[[Journaling File Systems]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Delayed allocation defers block assignment until flush for better contiguity

## Context

Traditional file systems allocate physical blocks immediately when a process calls write(), even though the data may sit in the page cache for seconds before being flushed to disk. ext4's delayed allocation postpones the block allocation decision until writeback time. By then, the allocator can see the total amount of data being written and allocate a single contiguous extent rather than many small, scattered block runs. This dramatically reduces fragmentation and improves sequential read performance on subsequent access.

## Why It Matters

Delayed allocation is a classic example of "lazy evaluation" applied to systems software — deferring a decision until more information is available leads to better outcomes. The tradeoff is a small risk window: data written to the page cache but not yet allocated could be lost on crash before flush, which ext4 mitigates with journal-based metadata consistency and periodic sync.

## QnA Seeds

- Q: What is delayed allocation and how does it differ from immediate allocation?
- Q: Why does deferring block allocation reduce fragmentation?
- Q: What crash-safety risk does delayed allocation introduce?
