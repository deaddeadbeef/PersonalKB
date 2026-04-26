---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Page Replacement Algorithms"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Page Replacement Algorithms

## Summary
When a page fault occurs and no free physical frames are available, the OS must select a victim page to evict. The choice of page replacement algorithm directly affects the page fault rate and overall system performance. The optimal algorithm (Belady's OPT) provides a theoretical lower bound but requires future knowledge; practical algorithms like LRU, Clock, and Working Set approximate optimality using hardware-supported reference and dirty bits.

## Key Claims
- Belady's optimal algorithm (OPT) replaces the page that will not be used for the longest time in the future; it is unrealizable in practice but serves as the benchmark against which all practical algorithms are measured
- FIFO replacement is simple but suffers from Belady's anomaly—the counterintuitive phenomenon where increasing the number of physical frames can actually increase the page fault rate for certain reference strings
- True LRU replacement requires either a hardware counter per page or a stack data structure updated on every memory reference, making it too expensive for direct implementation; practical systems approximate LRU using reference bits
- The Clock algorithm (second-chance) arranges pages in a circular buffer and inspects the reference bit; pages with the bit set get a "second chance" (bit cleared, pointer advances), while pages with the bit clear are evicted—this approximates LRU at near-FIFO cost
- Thrashing occurs when the total working set of all active processes exceeds physical memory, causing the system to spend more time paging than executing; the solution is to reduce the degree of multiprogramming

## Atomic Facts
1. Belady's anomaly was demonstrated with FIFO and the reference string 1,2,3,4,1,2,5,1,2,3,4,5: with 3 frames there are 9 page faults, but with 4 frames there are 10 page faults—more memory causes more faults
2. Stack algorithms (including LRU and OPT) are immune to Belady's anomaly because the set of pages in memory with n frames is always a subset of the set with n+1 frames
3. The Not Recently Used (NRU) algorithm classifies pages into four categories using the referenced (R) and modified (M) bits: class 0 (R=0,M=0), class 1 (R=0,M=1), class 2 (R=1,M=0), class 3 (R=1,M=1), and evicts a random page from the lowest non-empty class
4. The working set model defines W(t,τ) as the set of pages referenced in the last τ time units; pages not in the working set are candidates for eviction, and processes should not run unless their working set fits in memory
5. Linux uses a variant of the two-list LRU strategy with active and inactive lists; pages start on the inactive list and are promoted to the active list on second access, approximating LRU-2 behavior
6. The dirty bit (modified bit) affects replacement cost: evicting a clean page requires no disk write (just discard it), while evicting a dirty page requires writing it to disk first, so algorithms prefer to evict clean pages when possible

## Significance
Page replacement algorithms illustrate a fundamental pattern in systems design: the tension between theoretical optimality and practical implementability. Belady's anomaly demonstrates that intuitive assumptions about resource allocation can be wrong, and the working set model provides the conceptual framework for understanding thrashing—a phenomenon that has plagued systems from 1960s mainframes to modern cloud instances running memory-hungry containers.

## Chunks Extracted
*Pending*
