---
id: chunk-csos-179
type: chunk
source: "[[raw-os-033]]"
source_loc: "TLB and Address Translation"
topic: "memory"
claim: "The TLB caches recent virtual-to-physical translations, reducing the four memory accesses needed for an x86-64 page table walk to a single-cycle lookup for over 99% of references"
confidence: verified
supports:
  - "[[TLB and Page Tables]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — TLB caches translations for single-cycle lookup

## Context

Without the TLB, every memory access on x86-64 would require a four-level page table walk (PML4, PDPT, PD, PT), costing four extra memory accesses. The TLB stores recent translations, delivering physical frame numbers in a single cycle on hits. Modern x86 CPUs have split L1 TLBs (64-128 entries, instruction/data) and unified L2 TLBs (512-2048 entries). Hit rates typically exceed 99% due to spatial and temporal locality.

## Why It Matters

The TLB is the most critical cache in the memory hierarchy — without it, virtual memory would impose a 5x slowdown on every memory access. Understanding TLB behavior is essential for performance engineering (hugepages, NUMA allocation) and security analysis (Meltdown).

## QnA Seeds

- Q: How many extra memory accesses does an x86-64 page walk require without TLB?
- Q: What TLB hit rates are typical and why?
- Q: What is the structure of L1 and L2 TLBs on modern x86 CPUs?
