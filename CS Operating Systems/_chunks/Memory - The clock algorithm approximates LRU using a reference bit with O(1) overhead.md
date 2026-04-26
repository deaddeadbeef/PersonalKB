---
id: chunk-csos-020
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 3"
topic: "memory"
claim: "The clock (second-chance) algorithm approximates LRU by sweeping a circular list of frames and evicting the first frame with its accessed bit clear, clearing set bits as it passes them"
confidence: verified
supports:
  - "[[Page Replacement Algorithms]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — The clock algorithm approximates LRU using a reference bit with O(1) overhead

## Context

The clock algorithm uses the hardware-maintained accessed (reference) bit in each page-table entry. Frames form a circular list; a pointer (the "clock hand") sweeps them. On a page fault: if the current frame's bit is 1 (recently accessed), clear it and advance. If the bit is 0, evict this frame. In the worst case the hand makes a full revolution and evicts the frame it just gave a second chance to. Hardware resets the bit on each access, naturally tracking recency without software timestamps.

## Why It Matters

The clock algorithm delivers near-LRU performance with O(1) work per replacement (amortised) and no per-access software overhead — only the hardware bit is touched. This makes it practical for real OSes. BSD Unix and early Windows used variants of it. Linux uses a more sophisticated version (active/inactive lists split, with an additional referenced bit from page-table PTE walking), but the core idea is the same.

## QnA Seeds

- Q: What is the clock algorithm's "second chance" rule?
- Q: What bit in the page-table entry does the clock algorithm use?
- Q: Why is clock preferred over exact LRU in production systems?
