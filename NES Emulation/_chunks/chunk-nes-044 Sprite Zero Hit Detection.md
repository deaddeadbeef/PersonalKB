---
tags: [chunk, nes-emulation, sprites]
source: "[[raw-nes-014]]"
up: "[[Sprites and OAM]]"
---

# Chunk NES 044 — Sprite Zero Hit Detection

The sprite-0 hit flag in PPUSTATUS is set when an opaque sprite-0 pixel overlaps an opaque background pixel, provided: both background and sprite rendering are enabled, the pixel is not at X=255, and left-side clipping does not mask the pixel (X=0-7 when clipping is on). The exact PPU cycle of the hit depends on the sprite's X position and background pixel pattern. Games widely use sprite-0 hit for timing mid-frame scroll changes — placing sprite 0 at the boundary between a fixed status bar and scrolling playfield, then polling PPUSTATUS in a tight loop until the hit is detected.
