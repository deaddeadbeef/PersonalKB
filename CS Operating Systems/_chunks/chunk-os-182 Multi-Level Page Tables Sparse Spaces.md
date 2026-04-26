---
id: chunk-csos-182
type: chunk
source: "[[raw-os-033]]"
source_loc: "TLB and Address Translation"
topic: "memory"
claim: "Multi-level page tables save memory by not allocating table pages for unmapped regions, trading additional TLB miss cost for dramatically reduced memory consumption"
confidence: verified
supports:
  - "[[TLB and Page Tables]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Multi-level page tables save memory for sparse spaces

## Context

x86-64 uses a 4-level hierarchy (PML4, PDPT, PD, PT), each level indexed by 9 bits with a 12-bit offset, supporting 48-bit virtual addresses (256 TB). Unmapped regions require no page table pages at any level, saving enormous memory for sparse address spaces. Hugepages (2 MB or 1 GB) increase TLB reach: one 2 MB entry covers 512 standard 4 KB entries. Linux supports optional 5-level tables (PML5, kernel 4.14+) for 57-bit addressing (128 PB).

## Why It Matters

A flat page table for 48-bit addresses would require 512 GB of memory per process. Multi-level tables make virtual memory practical by allocating proportionally to actual usage. Hugepages complement this by improving TLB coverage for large working sets.

## QnA Seeds

- Q: How does a multi-level page table avoid allocating entries for unmapped memory?
- Q: How large is the x86-64 virtual address space with 4-level page tables?
- Q: How do hugepages improve TLB coverage?
