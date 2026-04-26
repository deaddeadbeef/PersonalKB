---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Memory Management: Segmentation"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Memory Management: Segmentation

## Summary
Segmentation divides a process's address space into variable-sized logical units (segments) corresponding to meaningful program structures like code, data, stack, and heap. Each segment has its own base address and limit, enabling fine-grained protection and sharing at the logical level. While segmentation was once a primary memory management scheme, modern systems have largely replaced it with paging or use segmentation in a vestigial capacity (as in x86-64), because segmentation causes external fragmentation and complicates memory allocation.

## Key Claims
- Segmentation provides a two-dimensional address space where each address is a (segment number, offset) pair, matching the programmer's logical view of memory more naturally than the flat address space of pure paging
- Each segment table entry contains the segment's base physical address and its limit (length), enabling the hardware to perform bounds checking on every memory access—an offset exceeding the limit triggers a segmentation fault
- Segmentation enables fine-grained protection and sharing: a shared library can be mapped as a single segment in multiple processes' segment tables with read-execute permissions, without duplicating it in physical memory
- External fragmentation is the primary weakness of pure segmentation—as segments of varying sizes are allocated and freed, memory becomes riddled with small unusable gaps that may require compaction (an expensive operation)
- Intel x86 processors from the 8086 through the Pentium used segmentation extensively; x86-64 (AMD64) effectively flattened the segment model by setting all segment bases to 0, making segmentation vestigial except for thread-local storage via FS/GS segment registers

## Atomic Facts
1. A segment table maps segment numbers to (base, limit) pairs; on each memory reference, the hardware adds the offset to the base and verifies that the offset is less than the limit—violation causes a segmentation fault (SIGSEGV on Unix)
2. In segmented memory, external fragmentation occurs because freed segments leave variably-sized holes; algorithms like first-fit, best-fit, and worst-fit attempt to minimize fragmentation but none eliminate it completely
3. Segmented paging (used in Intel 386–Pentium) combines both schemes: a logical address is first translated through a segment table to a linear address, which is then translated through a page table to a physical address
4. The Multics operating system (1960s) was a pioneering user of segmentation, supporting up to 2^18 segments of up to 2^18 words each, with per-segment access control lists enabling fine-grained security
5. In x86-64 long mode, the CS, DS, ES, and SS segment base addresses are forced to zero and limits are ignored; only FS and GS retain functional base addresses, used by operating systems to point to per-CPU or per-thread data structures
6. Compaction—relocating all segments to eliminate external fragmentation—requires updating all base addresses and is extremely expensive (O(n) memory copies), making it infeasible as a routine operation during normal system execution

## Significance
Segmentation represents an important historical approach to memory management that prioritized logical structure and protection over allocation efficiency. Understanding segmentation explains why modern architectures retained vestigial segment registers, why the term "segmentation fault" persists in everyday programming, and why paging ultimately won as the dominant memory management mechanism—its fixed-size pages eliminate external fragmentation entirely.

## Chunks Extracted
*Pending*
