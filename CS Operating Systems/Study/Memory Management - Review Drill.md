---
tags:
  - csos
  - csos/study
  - csos/memory
up: "[[OS Study Index]]"
---
# Memory Management — Review Drill

Active-recall drill for virtual memory, paging mechanics, TLBs, segmentation, and page replacement algorithms.

**Canon pages:** [[Address Spaces]] · [[Virtual Memory and Paging]] · [[Page Replacement Algorithms]] · [[Segmentation]] · [[Memory Management Overview]]

---

## How to Use

Answer each question without referring to the canonical pages. When you cannot answer, mark it and open the relevant page, then try again from scratch.

---

## Core Recall

**Address Spaces**

Q: What problem does a virtual address space solve?
A: Without address spaces, programs would reference physical addresses directly — two programs could overwrite each other's memory, a single crash would corrupt all others, and memory layout would be fixed at compile time. Virtual address spaces give each process the illusion of exclusive access to a large, contiguous memory region. The OS and MMU translate virtual addresses to physical addresses invisibly.

Q: What is the difference between internal and external fragmentation?
A: **External fragmentation**: free memory exists but is split into small, non-contiguous holes that individually cannot satisfy a large allocation request. **Internal fragmentation**: allocated blocks are larger than requested — the excess inside a block is wasted. Fixed-size paging eliminates external fragmentation (any free frame satisfies any virtual page request) at the cost of some internal fragmentation within the last page of a region.

---

**Virtual Memory and Paging**

Q: Describe the virtual-to-physical address translation path.
A: The CPU generates a virtual address VA = (VPN, offset). The MMU uses VPN as an index into the process's page table to find the PFN (physical frame number). Physical address = (PFN << page_size_bits) | offset. If the PTE is marked "not present", a page fault trap fires and the OS brings the page in from disk (or zeroes it for anonymous memory).

Q: What are the five important flags in a page table entry (PTE)?
A: **Present (P)** — page is in physical memory. **Read/Write (R/W)** — write permission. **User/Supervisor (U/S)** — accessible from user mode. **Dirty (D)** — page has been written; must be written back before eviction. **Accessed (A)** — page was recently referenced; used by replacement algorithms (clock/LRU approximations).

Q: Why do modern CPUs use multi-level page tables?
A: A flat page table for a 48-bit virtual address space at 4 KiB granularity would require $2^{36}$ ≈ 64 billion entries — impractical in RAM. A 4-level x86-64 page table (PML4 → PDP → PD → PT, each 512 entries, only populated for mapped regions) is sparse: most virtual address space is unmapped, so most subtrees are absent and consume no memory.

Q: What is demand paging, and what does it enable?
A: Pages are not loaded into RAM until first accessed. On the first access to an unmapped page, a page fault fires; the OS loads the page from disk or allocates a zeroed frame. This enables: (1) address spaces larger than physical RAM, (2) fast process startup (only load touched pages), and (3) memory-mapped files (lazily load file content on access).

---

**Translation Lookaside Buffer (TLB)**

Q: What is a TLB and why is it essential?
A: The TLB is a small, fully-associative hardware cache of recent virtual-to-physical address translations. Without it, every memory access would require 4+ memory reads to walk the page table — making paging prohibitively slow. With a TLB, most translations are resolved in a single cycle. Typical TLBs: 64–1024 entries; hit rate > 99% for common workloads due to spatial/temporal locality.

Q: What is a TLB shootdown and when does it occur?
A: When the OS modifies a page table entry (e.g., remaps or unmaps a page), it must invalidate the corresponding TLB entry on every CPU that might have cached it. On a multiprocessor, this requires sending an inter-processor interrupt (IPI) to all other CPUs to flush their TLBs — an expensive operation. This is why large-page mappings (2 MiB or 1 GiB pages) are desirable: fewer TLB entries needed, fewer shootdowns.

---

**Page Replacement Algorithms**

Q: State the five replacement policies (OPT, FIFO, LRU, Clock, NRU) and their key property.
A: **OPT**: evict the page not needed for the longest future time; optimal fault rate but requires future knowledge — used only as a benchmark. **FIFO**: evict the longest-resident page; simple, no hardware support; suffers Bélády's anomaly (more frames → more faults on some reference strings). **LRU**: evict the least recently used page; good OPT approximation; exact implementation expensive (requires hardware timestamp on every access). **Clock**: circular list with accessed bit; evict first page with bit=0, clearing bit=1 pages on the sweep — $O(1)$ approximation of LRU. **NRU**: classify pages by (R, M) bits into four classes; evict from lowest class — cheapest, slightly worse than clock.

Q: What is Bélády's anomaly, and which policy is immune to it?
A: Bélády's anomaly: adding more physical frames can *increase* the number of page faults for the FIFO policy on certain reference strings. FIFO is not a "stack algorithm" — it doesn't guarantee that a superset of frames will contain at least the same pages. LRU and OPT are **stack algorithms** (the set of pages in k frames is always a subset of the set in k+1 frames) and are therefore immune.

Q: Describe the clock algorithm step by step.
A: Frames are arranged in a circular list with a "clock hand" pointer. On a page fault: (1) inspect the page at the hand's position. (2) If the accessed bit is 1: clear it, advance the hand (second chance given). (3) If the accessed bit is 0: evict this page and load the faulting page here, advance the hand. Hardware sets the accessed bit on every reference. Worst case: one full revolution around the clock before finding a victim.

Q: What is thrashing, and what causes it?
A: Thrashing occurs when a process (or the system) spends more time handling page faults than doing useful work. Cause: the sum of working sets of all running processes exceeds physical RAM. The OS keeps evicting pages that are immediately needed again. Fix: reduce the degree of multiprogramming (suspend some processes) or add RAM.

---

**Segmentation**

Q: How does segmentation differ from paging?
A: Segmentation divides a process's address space into **variable-size**, logically meaningful regions (code segment, data segment, stack segment). Each segment has its own base and limit register; the hardware checks each access against the limit. Paging uses **fixed-size** pages with no logical significance. Segmentation suffers external fragmentation; paging does not. Modern x86-64 effectively disables segmentation in 64-bit mode (flat model), relying entirely on paging.

---

## Compare and Contrast

**Page Replacement Policies**

| Policy | Approximates | Belady immune? | Hardware needed | Cost |
|--------|-------------|---------------|-----------------|------|
| OPT | — (optimal) | Yes | No (theoretical) | Impossible |
| FIFO | — | No | None | $O(1)$ |
| LRU | OPT closely | Yes | Full timestamp | Expensive |
| Clock | LRU approx | No | Accessed bit | $O(1)$ |
| NRU | LRU approx | — | R + M bits | Very cheap |

**Paging vs Segmentation**

| Property | Paging | Segmentation |
|----------|--------|-------------|
| Unit size | Fixed (e.g., 4 KiB) | Variable |
| External fragmentation | None | Yes |
| Internal fragmentation | Small (last page) | None |
| Logical structure | None — opaque pages | Matches program structure |
| Protection | Per-page bits | Per-segment (finer intent) |
| Modern use | Universal | x86-64: flat/disabled |

---

## Common Mistakes

1. **Confusing present bit with dirty bit** — the present bit (P) says the page is in RAM now; the dirty bit (D) says the page has been written and differs from disk. A page can be present and clean, present and dirty, or not present.

2. **LRU is not free** — exact LRU requires hardware to timestamp every memory access — impractical at CPU speeds. The clock algorithm is the standard approximation. Saying "the OS uses LRU" usually means "the OS uses a clock approximation".

3. **Bélády's anomaly scope** — it only affects FIFO (and similar non-stack policies). LRU and OPT cannot exhibit it. Don't claim it applies universally.

4. **TLB and context switch** — on a process context switch, the TLB is typically flushed (or tagged with an ASID to avoid flushing). Students often forget that switching address spaces invalidates all cached translations.

5. **Multi-level page tables** — higher levels of the page table must themselves be walked on every TLB miss. A 4-level miss requires 4 memory accesses before the physical address is known. The TLB eliminates this overhead for hot pages.

---

## Links Back

- [[Address Spaces]] — virtual address space concept; fragmentation types
- [[Virtual Memory and Paging]] — paging mechanics; PTE flags; demand paging; multi-level tables
- [[Page Replacement Algorithms]] — OPT, FIFO, LRU, Clock, NRU; Bélády's anomaly; thrashing
- [[Segmentation]] — variable-size regions; base/limit registers; comparison with paging
- [[Memory Management Overview]] — hub for the entire domain
