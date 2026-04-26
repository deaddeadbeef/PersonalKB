---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
---
# Memory Management Overview

How the OS gives each process the illusion of private, contiguous memory while efficiently sharing physical RAM. Covers address spaces, the paging mechanism, TLBs, segmentation, and the page-replacement algorithms that govern virtual memory performance.

---

## Learn in This Order

1. [[Address Spaces]] — logical vs physical address; base/limit registers; memory protection
2. [[Virtual Memory and Paging]] — page tables; TLBs; demand paging; page faults; multi-level paging
3. [[Page Replacement Algorithms]] — OPT, FIFO, LRU, clock/second-chance; working-set model
4. [[Segmentation]] — variable-size segments; segment table; combining with paging

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Address Spaces]] | The abstraction of private memory; logical-to-physical translation |
| [[Virtual Memory and Paging]] | Page tables; TLBs; demand paging; page fault handling |
| [[Page Replacement Algorithms]] | OPT/FIFO/LRU/clock; Belady's anomaly; thrashing |
| [[Segmentation]] | Variable-size logical regions; protection and sharing; combined with paging |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Paging vs segmentation? | Paging = fixed-size pages (no external fragmentation, internal fragmentation possible). Segmentation = variable-size logical regions (no internal fragmentation, external fragmentation possible). Most systems page-within-segments or just page. |
| TLB hit vs miss? | TLB hit: address translation in ~1 cycle. TLB miss: walk the page table (dozens of cycles). TLBs make paging affordable in practice. |
| LRU vs clock algorithm? | True LRU is expensive to implement. The clock (second-chance) algorithm approximates LRU using a single reference bit per frame — practical and common in real OSes. |
| Demand paging vs prepaging? | Demand paging loads a page only when accessed (page fault). Prepaging speculatively loads pages expected to be needed soon. |

---

## How to Navigate

- **New to virtual memory?** [[Address Spaces]] → [[Virtual Memory and Paging]] is the core path.
- **Choosing a page-replacement policy?** [[Page Replacement Algorithms]] compares all major options.
- **Segmentation question (x86 history or protecting code/data)?** [[Segmentation]]

---

## Related Domains

- **[[Virtualization Overview]]** — hypervisors add another layer of address translation (nested paging); memory management is extended, not replaced.
- **[[Processes Overview]]** — each process has its own address space; the process model explains why isolation matters.
- **[[File Systems Overview]]** — memory-mapped files (mmap) bridge virtual memory and the file system.
