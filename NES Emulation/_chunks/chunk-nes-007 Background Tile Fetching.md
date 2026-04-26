---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[Backgrounds and Nametables]]"
---

# Chunk NES 007 — Background Tile Fetching

During visible scanlines, the PPU fetches background data in 8-cycle groups: (1) nametable byte identifying the tile index, (2) attribute byte for palette selection, (3) pattern table low byte containing bit-plane 0, (4) pattern table high byte containing bit-plane 1. Two 16-bit shift registers hold pattern data for the current and next tile. The fine X scroll register selects which bit position produces the current pixel. At the end of each 8-cycle group, coarse X scroll increments; at the end of each scanline, Y scroll increments. This fetch-and-shift architecture renders backgrounds autonomously.
