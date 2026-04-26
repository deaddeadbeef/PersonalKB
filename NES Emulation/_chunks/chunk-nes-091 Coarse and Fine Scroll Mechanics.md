---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-012]]"
up: "[[PPU Scrolling]]"
---

# Chunk NES 091 — Coarse and Fine Scroll Mechanics

Scroll position has two components: coarse scroll (which 8x8 tile) and fine scroll (which pixel within that tile, 0-7). Horizontal: coarse X occupies 5 bits of the v register (0-31 tile columns), fine X is the separate 3-bit x register. Vertical: coarse Y occupies 5 bits (0-29 tile rows, with 30-31 as special cases), fine Y occupies 3 bits of v. During rendering, fine X selects the bit position in the shift registers for the current pixel. Every 8 pixels, coarse X increments and wraps at 31, toggling the horizontal nametable bit. At scanline end, fine Y increments 0-7 then coarse Y increments.
