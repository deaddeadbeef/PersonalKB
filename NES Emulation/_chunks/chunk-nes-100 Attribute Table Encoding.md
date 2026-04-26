---
tags: [chunk, nes-emulation, nametable]
source: "[[raw-nes-017]]"
up: "[[Backgrounds and Nametables]]"
---

# Chunk NES 100 — Attribute Table Encoding

The 64-byte attribute table at the end of each nametable assigns palettes to 2x2 tile groups. Each byte covers a 4x4 tile area (32x32 pixels) encoded as four 2-bit fields: bits 0-1 for the top-left 2x2 group, bits 2-3 for top-right, bits 4-5 for bottom-left, and bits 6-7 for bottom-right. Each 2-bit value selects one of four background palettes. This coarse granularity (16x16 pixel color regions) is a defining NES graphics constraint. Game artists designed tiles to minimize visible palette boundaries, and some games use sprites overlaid on backgrounds to add color detail beyond the attribute table limitation.
