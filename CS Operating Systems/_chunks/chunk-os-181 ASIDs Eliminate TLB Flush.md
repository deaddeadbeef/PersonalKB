---
id: chunk-csos-181
type: chunk
source: "[[raw-os-033]]"
source_loc: "TLB and Address Translation"
topic: "memory"
claim: "ASIDs tag TLB entries with process identifiers, allowing entries from multiple processes to coexist and eliminating costly full TLB flushes on context switches"
confidence: verified
supports:
  - "[[TLB and Page Tables]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — ASIDs eliminate TLB flushes on context switch

## Context

Without ASIDs, every context switch requires flushing the entire TLB because the new process has different page tables. Refilling hundreds of entries costs hundreds of memory accesses. ASIDs (called PCIDs on Intel, 8-bit since Westmere, supporting 256 concurrent processes) tag each TLB entry with a process identifier, so only entries matching the current ASID are considered for hits. Entries from inactive processes remain cached.

## Why It Matters

Context switches are frequent — hundreds to thousands per second. Without ASIDs, each switch would incur hundreds of TLB misses as the cache refills. ASIDs are why modern systems can switch between processes cheaply, making multitasking responsive.

## QnA Seeds

- Q: What problem do ASIDs solve for TLB management during context switches?
- Q: How many concurrent processes can Intel PCIDs support?
- Q: Why is flushing the TLB on every context switch expensive?
