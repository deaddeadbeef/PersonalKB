---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-018]]"
up: "[[PPU Rendering Pipeline]]"
---

# Chunk NES 116 — NES Master Palette

The NES has a fixed master palette of 64 color entries, though several produce identical or near-identical colors, giving approximately 52-54 unique colors. The palette is based on NTSC signal parameters rather than RGB values. Entries  and  in each row produce voltage levels below NTSC black — displaying them can cause issues on real televisions. Each palette RAM entry is a 6-bit index into this master palette. The master palette cannot be modified by software. OxideNES stores the master palette as a pre-computed 64-entry RGB lookup table, with the specific RGB values selectable between several community-standard palette files.
