---
id: chunk-csos-018
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 3"
topic: "memory"
claim: "The TLB caches recent virtual-to-physical page translations in hardware, making the two-level memory access of paging affordable by hitting cache ~99% of the time"
confidence: verified
supports:
  - "[[Virtual Memory and Paging]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — TLBs cache recent address translations to make paging affordable

## Context

Without a TLB, every memory access requires two: one to look up the page table entry, one for the actual data. For a 4-level page table, it would be five accesses. The TLB (Translation Lookaside Buffer) is a small, fully-associative hardware cache (typically 32–2048 entries) that stores recent VPN→PFN mappings. On a TLB hit, the physical address is available in 1–2 cycles. On a miss, the hardware or OS walks the page table (taking tens of cycles) and reloads the TLB.

## Why It Matters

The TLB works because of **locality**: a process repeatedly accesses the same few pages (spatial and temporal locality). Hit rates of 98–99% are typical, making the effective cost of address translation almost zero. Context switches invalidate (or ASID-partition) the TLB, causing a cold-start penalty — one reason why context-switch frequency must be managed carefully.

## QnA Seeds

- Q: What is the purpose of the TLB?
- Q: What happens on a TLB miss?
- Q: Why does context switching hurt TLB performance?
