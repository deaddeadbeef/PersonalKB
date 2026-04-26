---
id: mos-ch-03
type: book-chapter
chapter: 3
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 6
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
---
# MOS — Chapter 03: Memory Management

## Summary

Memory management begins with the simplest model — a single process with absolute addresses — and builds toward the full virtual memory system used by modern hardware. The address space abstraction decouples logical addresses from physical ones; base-and-limit registers provide the first level of protection. Paging divides both spaces into fixed-size units, eliminating external fragmentation and enabling partial loading; the page table maps virtual page numbers to physical frame numbers. TLBs cache hot translations to make the two-level lookup affordable. Page replacement policies (OPT, FIFO, LRU, clock) govern which frame to evict on a page fault. Segmentation offers variable-size regions with independent protection and sharing attributes; combining it with paging (as in x86 protected mode) provides the richest memory model.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Address space | Set of memory addresses a process can legally reference |
| Page table | Per-process mapping from virtual page to physical frame |
| TLB | Hardware cache for recent page-table lookups; reduces two-level overhead |
| Demand paging | Pages loaded only when referenced; saves physical memory |
| Page fault | Trap on access to a non-present page; triggers OS handler |
| Clock algorithm | Approximate LRU using a reference bit; practical page replacement |

## Chunk Candidates

- [x] [[Memory - Address spaces decouple logical and physical memory for protection and flexibility]]
- [x] [[Memory - Paging maps fixed-size virtual pages to physical frames eliminating external fragmentation]]
- [x] [[Memory - TLBs cache recent address translations to make paging affordable]]
- [x] [[Memory - Page replacement policies decide which frame to evict on a page fault]]
- [x] [[Memory - The clock algorithm approximates LRU using a reference bit with O(1) overhead]]
- [x] [[Memory - Segmentation provides variable-size regions with independent protection attributes]]

## Wiki Pages Seeded

- [[Address Spaces]] — logical vs physical, base/limit, protection
- [[Virtual Memory and Paging]] — page tables, demand paging, page faults
- [[Page Replacement Algorithms]] — OPT, FIFO, LRU, clock
- [[Segmentation]] — segment tables, combining with paging

## References

See [[Sources Index#Tanenbaum 2015]].
