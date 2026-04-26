---
tags: [chunk, nes-emulation, sprites]
source: "[[raw-nes-014]]"
up: "[[Sprites and OAM]]"
---

# Chunk NES 043 — Sprite Overflow Bug

The PPU's sprite overflow detection has a documented hardware bug. After finding 8 sprites for a scanline, the evaluation should continue checking remaining sprites to set the overflow flag. Instead, the hardware incorrectly increments both the sprite index AND the byte offset within each sprite entry simultaneously. This causes it to read bytes 1, 2, 3 of subsequent entries as Y coordinates, sometimes missing sprites that are in range and false-triggering on sprites that are not. OxideNES faithfully replicates this buggy behavior for hardware accuracy, though few games depend on the exact bug pattern.
