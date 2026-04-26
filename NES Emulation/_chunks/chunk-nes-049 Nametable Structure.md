---
tags: [chunk, nes-emulation, nametable]
source: "[[raw-nes-017]]"
up: "[[Backgrounds and Nametables]]"
---

# Chunk NES 049 — Nametable Structure

Each nametable is 1024 bytes: 960 bytes of tile indices (30 rows x 32 columns, each byte selecting one of 256 tiles from the active pattern table) plus 64 bytes of attribute table. The attribute table provides palette selection at 2x2 tile granularity: each byte covers a 4x4 tile area with four 2-bit fields (top-left, top-right, bottom-left, bottom-right 2x2 groups). This coarse 16x16-pixel palette granularity is a major NES graphics constraint. Games work around it with careful tile design, sprite overlays for extra color detail, and palette cycling effects.
