---
tags: [chunk, nes-emulation, nametable]
source: "[[raw-nes-017]]"
up: "[[Backgrounds and Nametables]]"
---

# Chunk NES 050 — Nametable Mirroring Modes

The PPU addresses four logical nametables in a 2x2 grid (, , , ) forming a 512x480 virtual playfield, but only 2 KB VRAM exists for two physical nametables. Vertical mirroring pairs 0-with-2 and 1-with-3, giving two side-by-side screens for horizontal scrolling games. Horizontal mirroring pairs 0-with-1 and 2-with-3, giving two stacked screens for vertical scrolling. Single-screen maps all four to one physical bank. Four-screen requires extra cartridge RAM for all unique nametables. The mapper provides a mirror_mode() method; some mappers like MMC1 can change mirroring dynamically.
