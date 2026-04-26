---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-014]]"
up: "[[Sprites and OAM]]"
---

# Chunk NES 103 — 8x16 Sprite Mode

When PPUCTRL bit 5 is set, the PPU uses 8x16 sprites instead of the default 8x8. In this mode, the tile index byte in OAM has dual purpose: bit 0 selects the pattern table (0 for , 1 for ), and bits 7-1 specify the top tile number. The bottom tile is automatically the next sequential tile. This doubles sprite height, useful for character sprites in games like Super Mario Bros. 3. Vertical flipping swaps the top and bottom halves. The 8-per-scanline limit still applies, but each sprite covers more vertical space, allowing larger characters with fewer sprite slots.
