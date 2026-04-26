---
tags: [chunk, nes-emulation, sprites]
source: "[[raw-nes-014]]"
up: "[[Sprites and OAM]]"
---

# Chunk NES 042 — OAM Entry Format

Each of the 64 sprites in OAM uses 4 bytes. Byte 0 is Y position (top edge minus 1; values - hide 8x8 sprites off-screen). Byte 1 is the tile index: for 8x8 sprites it selects from the PPUCTRL-chosen pattern table; for 8x16 sprites, bit 0 selects the pattern table and bits 7-1 give the top tile number. Byte 2 holds attributes: bits 0-1 select the sprite palette, bit 5 sets priority (front or behind background), bit 6 enables horizontal flip, bit 7 enables vertical flip. Byte 3 is the X position with no wrapping — sprites clip at the right edge.
