---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# PPU — Picture Processing Unit Overview

The Ricoh 2C02 (NTSC) is the NES's dedicated graphics processor. It renders 256x240 pixels at ~60 Hz by racing the electron beam across 262 scanlines of 341 dots each. The PPU has its own 14-bit address bus, separate from the CPU, accessing pattern tables and nametables through the cartridge.

## Pages

- [[PPU Rendering Pipeline]] — The scanline-by-scanline rendering process
- [[Backgrounds and Nametables]] — Tile-based background rendering and scrolling
- [[Sprites and OAM]] — Sprite evaluation, priority, and the 8-sprite limit
- [[PPU Scrolling]] — The complex dual-register scroll mechanism
- [[PPU Registers and Timing]] — PPUCTRL, PPUMASK, PPUSTATUS, and cycle-accurate timing

## Key Facts

- **341 dots × 262 scanlines** = 89,342 PPU cycles per frame (NTSC)
- **Runs at 3x CPU speed** — 5.369 MHz
- **Two rendering layers:** background tiles + sprites
- **52 unique colors** in the NES master palette
- **Sprite 0 hit** flag enables mid-frame raster effects

## OxideNES Implementation

`ppu.rs` (781 lines): The `tick()` method is the single hottest function in the emulator, called 5.37 million times per second. Uses unsafe bounds elimination on pixel writes and direct palette access for performance.

## How To Read This Chapter

Read this chapter for background and sprite rendering. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: nametable fetches, pattern tables, palettes, OAM evaluation, scrolling registers, vblank/NMI timing, and sprite-zero hit behavior. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
