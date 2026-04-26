---
id: chunk-csos-019
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 3"
topic: "memory"
claim: "Page replacement algorithms decide which physical frame to evict when memory is full; OPT is theoretically optimal but not implementable; practical choices include FIFO, LRU, and clock"
confidence: verified
supports:
  - "[[Page Replacement Algorithms]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Page replacement policies decide which frame to evict on a page fault

## Context

When a page fault occurs and all frames are in use, the OS must evict one. OPT evicts the page not used for the longest future time — optimal but requires future knowledge. FIFO is simple but suffers Bélády's anomaly. LRU evicts the page not used for the longest *past* time — approximates OPT well but requires per-page timestamps. The clock algorithm approximates LRU using a single "recently used" bit per frame, avoiding timestamps entirely.

## Why It Matters

Page replacement directly affects the page fault rate, which determines memory subsystem performance. A bad replacement policy under memory pressure (thrashing) causes the system to spend more time paging than executing. Linux's two-list (active/inactive) LRU approximation was tuned over years to handle the workload mix of servers and desktops without thrashing.

## QnA Seeds

- Q: Why is OPT not implementable in practice?
- Q: What is Bélády's anomaly in FIFO replacement?
- Q: How does the clock algorithm approximate LRU without timestamps?
