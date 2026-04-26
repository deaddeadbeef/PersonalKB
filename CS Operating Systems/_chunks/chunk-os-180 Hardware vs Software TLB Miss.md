---
id: chunk-csos-180
type: chunk
source: "[[raw-os-033]]"
source_loc: "TLB and Address Translation"
topic: "memory"
claim: "TLB misses are handled by hardware page table walkers on x86 (faster, less flexible) or software miss handlers on MIPS/RISC-V (slower, more flexible)"
confidence: verified
supports:
  - "[[TLB and Page Tables]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Hardware vs software TLB miss handling

## Context

On a TLB miss, x86 hardware autonomously walks the page table hierarchy to find the mapping and loads it into the TLB. MIPS and RISC-V instead trap to an OS handler that performs the walk in software. Hardware walkers are faster but inflexible (fixed page table format); software handlers allow arbitrary page table structures. If the page is not present, both paths invoke the OS page fault handler.

## Why It Matters

This hardware/software split is a fundamental architecture decision with cascading effects. Hardware walkers dictate page table format (x86 four-level structure is fixed), while software handlers give OS designers freedom to use any translation scheme, including inverted page tables.

## QnA Seeds

- Q: What is the difference between hardware and software TLB miss handling?
- Q: Why are hardware page walkers faster but less flexible?
- Q: Which architectures use software TLB miss handlers?
