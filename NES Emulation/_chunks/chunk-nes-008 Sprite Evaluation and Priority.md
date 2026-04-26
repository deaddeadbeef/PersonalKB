---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[Sprites and OAM]]"
---

# Chunk NES 008 — Sprite Evaluation and Priority

Each visible scanline, the PPU evaluates all 64 OAM sprites for the NEXT scanline. Up to 8 sprites are selected (the overflow flag is set if more exist). Selected sprite pixels are fetched from pattern tables into per-sprite shift registers. The pixel multiplexer resolves priority: sprite-0 hit detection fires when an opaque sprite-0 pixel overlaps an opaque background pixel. Sprite-vs-sprite priority follows OAM order (sprite 0 highest, sprite 63 lowest). Each sprite's attribute bit controls whether it renders in front of or behind the background layer.
