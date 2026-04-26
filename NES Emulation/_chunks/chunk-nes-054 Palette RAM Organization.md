---
tags: [chunk, nes-emulation, palette]
source: "[[raw-nes-021]]"
up: "[[PPU Registers and Timing]]"
---

# Chunk NES 054 — Palette RAM Organization

The PPU's 32 bytes of palette RAM (-) hold 8 palettes of 4 colors each: 4 background palettes (-) and 4 sprite palettes (-). Address  is the universal background color shared across all background palettes. Mirror quirks:  reads/writes actually access ; addresses , ,  are writable but reading returns the universal background color. Each entry is a 6-bit index into the NES master palette. PPUMASK bit 0 enables grayscale mode, ANDing all lookups with  to strip hue information, producing 4-shade grayscale output.
