---
tags: [chunk, nes-emulation, pattern]
source: "[[raw-nes-018]]"
up: "[[PPU Rendering Pipeline]]"
---

# Chunk NES 051 — Tile Encoding and Pattern Tables

The PPU's two 4 KB pattern tables (- and -) each contain 256 tiles of 8x8 pixels, 16 bytes per tile. Each tile uses 2-bit planar encoding: bytes 0-7 hold bit-plane 0 (low bit of each pixel) and bytes 8-15 hold bit-plane 1 (high bit). The color for pixel (x,y) is computed by combining both planes: color = (high_plane[y] >> (7-x)) AND 1 shifted left 1 OR (low_plane[y] >> (7-x)) AND 1. This yields a 2-bit value (0-3). Color 0 is transparent for sprites. The attribute table or OAM attribute selects which 4-color palette is used.
