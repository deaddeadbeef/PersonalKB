---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "TLB and Address Translation"
authors: Silberschatz, Galvin, Gagne; Tanenbaum, Bos
year: 2018
---

# TLB and Address Translation

## Summary

The Translation Lookaside Buffer (TLB) is a small, fast hardware cache that stores recent virtual-to-physical address translations, accelerating the address translation process that occurs on every memory access. Without the TLB, each memory reference would require traversing the multi-level page table in memory—a four-level page table walk on x86-64 requires four additional memory accesses before the actual data can be read, making every memory operation five times slower.

On a TLB hit, the MMU (Memory Management Unit) obtains the physical frame number directly from the TLB entry in a single cycle, appends the page offset, and accesses physical memory. On a TLB miss, the hardware page table walker (on x86) or software TLB miss handler (on MIPS, RISC-V) traverses the page table hierarchy to find the mapping. If the page is present, the translation is loaded into the TLB and the access is retried. If the page is not present (page fault), the OS is invoked to handle the fault (load from swap, allocate a new frame, or signal SIGSEGV). Modern x86 processors typically have a split L1 TLB (separate for instruction and data) with 64–128 entries and a unified L2 TLB with 512–2048 entries. TLB hit rates typically exceed 99% due to spatial and temporal locality.

Context switches present a TLB management challenge. When the OS switches from one process to another, the TLB entries from the previous process are invalid for the new process (different page tables). The naive approach is to flush the entire TLB on each context switch, but this is expensive—refilling hundreds of entries requires hundreds of memory accesses. Address Space Identifiers (ASIDs) solve this by tagging each TLB entry with a process identifier, allowing entries from multiple processes to coexist. Only entries with the current process's ASID are considered for hits.

Multi-level page tables reduce memory consumption by not allocating page table pages for unmapped regions. x86-64 uses a four-level hierarchy: PML4 (Page Map Level 4) → PDPT (Page Directory Pointer Table) → PD (Page Directory) → PT (Page Table), each indexed by 9 bits of the virtual address, with a 12-bit page offset. Inverted page tables (used in IBM PowerPC) maintain one entry per physical frame rather than per virtual page, reducing table size but requiring hash-based lookup.

## Key Claims

- The TLB caches recent virtual-to-physical translations, reducing multi-level page table walks from 4 memory accesses (on x86-64) to a single-cycle lookup for over 99% of memory references
- TLB misses are handled by hardware page table walkers (x86) or software miss handlers (MIPS), with the former being faster but less flexible than the latter
- ASIDs tag TLB entries with process identifiers, allowing TLB entries from multiple processes to coexist and eliminating the need for full TLB flushes on every context switch
- Multi-level page tables trade additional memory accesses on TLB misses for dramatically reduced memory consumption by not allocating table pages for unmapped virtual address ranges
- Inverted page tables maintain one entry per physical frame rather than per virtual page, scaling with physical rather than virtual memory size but requiring hash-based lookup

## Atomic Facts

1. x86-64 uses a 4-level page table (PML4 → PDPT → PD → PT) with 9 bits per level and a 12-bit offset, supporting 48-bit virtual addresses (256 TB) and 52-bit physical addresses (4 PB)
2. Intel processors since Westmere support 8-bit ASIDs (called PCIDs—Process Context Identifiers), allowing up to 256 processes to retain TLB entries simultaneously
3. A typical L1 dTLB has 64 entries with 4-way set associativity and 1-cycle access time; an L2 TLB has 1024–2048 entries with 6–8 cycle access time
4. Hugepages (2 MB or 1 GB on x86-64) increase TLB reach by mapping larger regions per entry; a single 2 MB hugepage TLB entry covers the same range as 512 standard 4 KB entries
5. Linux can use 5-level page tables (PML5, enabled in kernel 4.14+) to extend the virtual address space to 57 bits (128 PB), used by systems with very large memory
6. The inverted page table hashes the virtual page number and ASID to find the corresponding physical frame entry, using chaining for hash collisions, with O(1) average lookup

## Significance

The TLB is arguably the most critical cache in the entire memory hierarchy—its performance directly determines the overhead of virtual memory, which is the foundation of process isolation and memory protection. Understanding TLB behavior is essential for performance engineering (hugepages, NUMA-aware allocation), security analysis (TLB-based side channels like Meltdown), and OS kernel development (TLB shootdowns for multiprocessor consistency). The design tradeoffs between multi-level and inverted page tables illustrate fundamental space-time tradeoffs in systems design.

## Chunks Extracted

*Pending*
