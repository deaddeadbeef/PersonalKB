---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Virtual Memory Concepts"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Virtual Memory Concepts

## Summary
Virtual memory creates the illusion that each process has a large, contiguous, private address space by mapping virtual addresses to physical addresses through page tables managed by the OS and hardware MMU. The Translation Lookaside Buffer (TLB) caches recent translations to make this indirection nearly free in the common case. Demand paging loads pages from disk only when accessed, enabling the system to run programs whose total memory requirements exceed physical RAM and supporting multiprogramming by isolating processes from each other.

## Key Claims
- Virtual memory solves three fundamental problems simultaneously: it provides each process with an isolated address space (protection), it decouples the programmer's view of memory from physical layout (abstraction), and it enables efficient use of limited physical RAM (multiplexing)
- The page table translates virtual page numbers to physical frame numbers; a single-level page table for a 64-bit address space would be impractically large, necessitating multi-level page tables or inverted page tables
- The TLB is the single most performance-critical cache in the memory hierarchy—a TLB miss triggers a page table walk costing 10–100 cycles, while a TLB hit adds zero to one cycle to memory access latency
- Demand paging defers loading a page until the first access causes a page fault; the page fault handler loads the page from disk, updates the page table, and restarts the faulting instruction transparently
- Copy-on-write (COW) allows fork() to share all pages between parent and child as read-only; pages are duplicated only when either process writes, making fork() nearly free and enabling patterns like fork+exec efficiently

## Atomic Facts
1. A typical page size is 4 KB on x86 systems; huge pages (2 MB or 1 GB on x86-64) reduce TLB pressure for large-memory workloads like databases and scientific applications by covering more address space per TLB entry
2. x86-64 uses a four-level page table (PML4→PDPT→PD→PT) with 9 bits per level plus a 12-bit offset, mapping 48-bit virtual addresses; Linux 5.x added optional five-level paging (PML5) extending to 57-bit virtual addresses
3. Each page table entry (PTE) contains the physical frame number plus control bits: present/absent, read/write permission, user/supervisor, dirty (page has been written), accessed (page has been read), and no-execute (NX) for security
4. A TLB typically holds 64–1024 entries with a hit rate above 99% for most workloads; TLB misses are handled in hardware on x86 (hardware page table walker) but in software on some RISC architectures (MIPS, older SPARC)
5. Memory-mapped files (mmap) map a file's contents directly into a process's virtual address space, allowing file I/O through load/store instructions; the OS handles page faults by reading file blocks on demand and writing dirty pages back
6. The working set of a process at time t with window Δ is the set of pages referenced during the interval (t−Δ, t); maintaining each process's working set in memory is the key to avoiding thrashing

## Significance
Virtual memory is arguably the most important abstraction in modern computing—it enables process isolation (security), memory overcommit (efficiency), and position-independent code (flexibility). Without virtual memory, every program would need to manage physical addresses, multiprogramming would require manual partitioning, and security boundaries between processes would be nearly impossible to enforce.

## Chunks Extracted
*Pending*
