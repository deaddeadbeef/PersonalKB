---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[PPU Registers and Timing]]"
---

# Chunk NES 009 — PPU Register Map

The PPU exposes 8 memory-mapped registers at - (mirrored through ). PPUCTRL () controls NMI enable, sprite size (8x8 or 8x16), pattern table selection, and VRAM increment direction. PPUMASK () enables/disables background and sprite rendering and controls color emphasis. PPUSTATUS () returns VBlank, sprite-0 hit, and overflow flags — reading it clears VBlank and resets the write latch. PPUSCROLL () sets the scroll position via two sequential writes. PPUADDR () and PPUDATA () provide VRAM read/write access. OAMADDR () and OAMDATA () access the sprite attribute memory.
