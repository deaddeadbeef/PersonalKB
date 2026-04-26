---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[PPU Rendering Pipeline]]"
---

# Chunk NES 006 — PPU Scanline Types

The NES PPU processes 262 scanlines per NTSC frame with 341 PPU cycles each. Pre-render scanline (-1/261) clears sprite overflow and sprite-0 hit flags and reloads vertical scroll bits. Visible scanlines (0-239) perform active rendering: fetching background tiles, evaluating sprites, and outputting pixels. Post-render scanline (240) is idle. VBlank scanlines (241-260) set the VBlank flag at cycle 1 of scanline 241 and trigger NMI if enabled, giving the CPU time for game logic and VRAM updates. This totals 89,342 PPU cycles per frame.
