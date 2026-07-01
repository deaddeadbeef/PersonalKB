---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# NES Hardware Overview

The Nintendo Entertainment System (1983 in Japan as Famicom, 1985 in North America) defined console gaming for a generation. Understanding its hardware is the foundation for building an accurate emulator.

## Pages

- [[NES Console Architecture]] — CPU, PPU, APU integration and system design
- [[NES Technical Specifications]] — Clock speeds, memory sizes, video output
- [[NES History and Legacy]] — From Famicom to worldwide phenomenon
- [[NES vs Other 8-bit Consoles]] — Comparison with Master System, C64, ZX Spectrum

## Key Facts

- **CPU:** Ricoh 2A03 (modified MOS 6502) at 1.789773 MHz (NTSC)
- **PPU:** Ricoh 2C02, 256x240 resolution, 52 colors, 64 sprites
- **APU:** 5 channels integrated into CPU die
- **RAM:** 2 KB CPU RAM + 2 KB VRAM + 256 bytes OAM
- **Cartridge:** Up to 512 KB PRG ROM + 256 KB CHR ROM (with mappers)

## How To Read This Chapter

Read this chapter for the full console as a timed system. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: CPU/PPU/APU clocks, shared cartridge lines, RAM limits, DMA pauses, video output, and regional differences. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
