---
tags: [nes, hub]
up: "[[NES Emulation]]"
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

## References

→ [[Sources Index]]
