---
tags:
  - csos
  - csos/memory
confidence: verified
freshness: stable
up: "[[CS Operating Systems/Memory/Memory Management Overview|Memory Management Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Segmentation

> **One-line summary**: Segmentation divides a program's address space into variable-size logical units (code, data, stack) with independent protection — matching program structure rather than fixed page sizes.

## 🎯 Intuition
**The Core Idea:** Segmentation slices memory along the lines that programmers think in — "this is my code," "this is my stack," "this is shared data" — rather than arbitrary fixed-size blocks.
**Analogy:** Think of a filing cabinet where each drawer (segment) can be any size and has its own lock (protection bits). One drawer holds recipes (code, read-only), another holds notes (data, read-write), another is shared with a colleague (shared segment). The drawback: drawers of different sizes leave awkward gaps in the cabinet (external fragmentation).
**Why It Matters:** Segmentation was the first hardware scheme that let the OS enforce fine-grained permissions per logical region. Though largely superseded by paging, its concepts survive in modern executable formats (ELF sections) and CPU segment registers.

---

## ⚙️ Core Mechanics
### How It Works
**Segmentation** divides a program's address space into variable-size **segments** — logical units such as code, data, stack, and shared library — each with independent base, limit, and protection attributes. Unlike paging (fixed-size), segments match program structure.

#### Segment Table
Each process has a **segment table**: one entry per segment containing:
- **Base**: starting physical address.
- **Limit**: segment length.
- **Protection bits**: read, write, execute permissions.

A logical address is a pair (segment number, offset). The MMU validates `offset < limit`, then forms physical address = base + offset.

### Key Concepts

| Segment Table Field | Purpose |
|--------------------|---------|
| Base | Starting physical address of the segment |
| Limit | Length of the segment (maximum valid offset) |
| Protection bits | Read / Write / Execute permissions |

| Address Translation Step | Action |
|-------------------------|--------|
| 1. Extract segment number | Index into segment table |
| 2. Bounds check | Verify offset < limit |
| 3. Form physical address | base + offset |

### Key Facts
- **Sharing**: two processes can share a read-only code segment by pointing to the same physical pages.
- **Protection granularity**: code segment can be read+execute only; stack can be read+write only.
- **Natural fit for compiler output**: each ELF section (.text, .data, .bss) maps cleanly to a segment.
- **External fragmentation**: variable-size segments leave oddly-sized holes in physical memory that are difficult to fill.
- **Compaction cost**: moving segments to consolidate free space is expensive.

---

## 🔬 Deep Dive
### Combining Segmentation with Paging
x86 protected mode (IA-32) combines both: the segmented address is first translated to a "linear address" by segment registers, then paged by the page table. x86-64 has largely abandoned segmentation (most segment registers set to base 0), relying purely on paging.

MULTICS (1969) was the original example of combined segment+page addressing.

### Implementation Details
- **IA-32 segment registers**: CS (code), DS (data), SS (stack), ES/FS/GS (extra). Each holds a selector that indexes into the GDT (Global Descriptor Table) or LDT (Local Descriptor Table). The descriptor contains base, limit, privilege level (DPL), and type.
- **x86-64 flat model**: Segmentation is effectively disabled — CS, DS, SS, ES all have base=0 and limit=max. Only FS and GS retain non-zero bases, used for thread-local storage (TLS) and per-CPU data in the kernel.
- **ELF segments vs sections**: An ELF executable has *sections* (.text, .data, .bss, .rodata) grouped into *segments* (PT_LOAD) for the OS loader. The OS maps each segment with appropriate permissions (read+execute for text, read+write for data).
- **Fragmentation management**: First-fit, best-fit, and worst-fit are allocation strategies for segments. Buddy allocation is used by some systems as a compromise. External fragmentation eventually requires compaction — copying all segments to one end of memory — which is expensive and requires pausing processes.

### Edge Cases and Pitfalls
- **External fragmentation** is the fatal flaw: after many allocations and deallocations, free memory becomes scattered into small, unusable holes. Paging solves this completely (every frame is the same size).
- **Segment limit overflow**: Accessing beyond a segment's limit triggers a hardware fault — this is how stack overflow detection worked in segmented systems.
- **Cross-segment pointers**: A pointer to another segment requires the segment number + offset — more complex than flat addresses. This is why modern OSes prefer flat address spaces with paging.

### Real-World Systems
- **MULTICS (1969)**: Full segmentation + paging; each segment independently paged. Deeply influential but complex.
- **Intel IA-32**: Hardware segmentation with GDT/LDT; Linux and Windows used flat segments (base=0) to effectively disable segmentation while using paging.
- **x86-64**: Segmentation vestigial; FS/GS bases used only for TLS. Paging is the sole memory management mechanism.
- **ARM**: Never had segmentation — went directly to paging-based memory management.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. How does a segmented address (segment number, offset) get translated to a physical address?
2. What is external fragmentation, and why does segmentation cause it while paging does not?
3. Why has x86-64 effectively abandoned segmentation?

### Core Problems
1. **Segment translation**: A process has three segments: Seg 0 (base=0x1000, limit=0x400), Seg 1 (base=0x3000, limit=0x600), Seg 2 (base=0x5000, limit=0x200). Translate: (a) logical address (Seg 1, offset 0x100), (b) logical address (Seg 0, offset 0x500) — what happens? (c) logical address (Seg 2, offset 0x1FF).
2. **Fragmentation analysis**: A system has 64 KiB of memory. Five segments are allocated: A(10 KiB), B(8 KiB), C(15 KiB), D(12 KiB), E(5 KiB). Then B and D are freed. (a) Draw the memory layout. (b) Can a 16 KiB segment F be loaded? (c) What is the total free memory? (d) What is the external fragmentation ratio?

### Challenge
MULTICS used combined segmentation + paging: each segment was independently paged, so logical addresses were (segment, page, offset). Design the address translation hardware for this scheme: (a) Draw the translation path from logical address to physical address. (b) How many memory accesses does a single translation require (worst case, no TLB)? (c) Why did this complexity ultimately lose to flat paging? (d) Argue whether the MULTICS approach has any advantages for modern fine-grained memory protection (e.g., capability-based systems like CHERI).

---

*See also:* [[Virtual Memory and Paging]], [[Address Spaces]]

## Supporting Chunks

- [[Memory - Segmentation provides variable-size regions with independent protection attributes]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 3.
