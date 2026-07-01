---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# Memory Map and Bus Overview

The NES CPU sees a 64 KB address space (0x0000-0xFFFF) shared between RAM, PPU registers, APU registers, and cartridge ROM. The PPU has its own separate 16 KB address space. Understanding the memory map is essential for emulating how all components communicate.

## Pages

- [[CPU Memory Map]] — Complete CPU address space layout
- [[PPU Memory Map]] — VRAM, pattern tables, palettes
- [[OAM DMA]] — The 513-cycle sprite transfer mechanism

## Key Facts

- **CPU bus:** 16-bit addressing, 0x0000-0xFFFF
- **PPU bus:** 14-bit addressing, 0x0000-0x3FFF
- **Extensive mirroring** saves address decode logic
- **DMA** is the only bulk data transfer mechanism

## OxideNES Implementation

us.rs (351 lines): The Bus struct is the central arbitration layer, implementing cpu_read()/cpu_write() with proper address mapping and mirroring. Game Genie intercepts reads transparently.

## How To Read This Chapter

Read this chapter for CPU and PPU address routing. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: RAM mirroring, register side effects, DMA, open bus behavior, mapper delegation, and read/write ordering. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
