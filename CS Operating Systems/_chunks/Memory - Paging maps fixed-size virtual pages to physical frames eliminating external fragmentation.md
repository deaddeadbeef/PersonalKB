---
id: chunk-csos-017
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 3"
topic: "memory"
claim: "Paging divides both the virtual address space and physical RAM into fixed-size units (pages/frames), eliminating external fragmentation and allowing non-contiguous physical allocation"
confidence: verified
supports:
  - "[[Virtual Memory and Paging]]"
  - "[[Address Spaces]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Paging maps fixed-size virtual pages to physical frames eliminating external fragmentation

## Context

Contiguous physical allocation creates external fragmentation — unusable holes between allocations. Paging solves this by breaking both virtual and physical space into fixed-size units (4 KiB typically). Any virtual page can map to any physical frame — frames do not need to be contiguous. The page table records these mappings. Internal fragmentation (last page partially used) exists but is bounded by one page per allocation.

## Why It Matters

Paging is the universal foundation of modern virtual memory. Without it, running 50 applications simultaneously while each believes it has a large contiguous address space would be impossible. Paging also enables demand paging (load pages only when accessed), copy-on-write (share pages until written), and memory-mapped files. The entire virtual memory system — TLBs, multi-level page tables, swap — sits on top of this basic mapping.

## QnA Seeds

- Q: What problem does paging solve that contiguous allocation cannot?
- Q: What is the difference between a page and a frame?
- Q: Why does paging produce internal but not external fragmentation?
