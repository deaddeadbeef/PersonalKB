---
tags: [raw, nes-emulation, pattern-table]
source: "NESdev CHR reference + OxideNES ppu.rs"
---

# Raw NES 018 — Pattern Tables and Tile Encoding

Pattern tables store the tile graphics data that the PPU uses to render both backgrounds and sprites. Understanding the bit-plane encoding format is fundamental to NES graphics emulation.

## Pattern Table Layout

The PPU has two 4 KB pattern tables:
- Pattern Table 0 at - (left)
- Pattern Table 1 at - (right)

PPUCTRL selects which table is used for backgrounds (bit 4) and which for 8x8 sprites (bit 3). For 8x16 sprites, the tile index itself selects the table (bit 0).

Each pattern table contains 256 tiles (16 × 16 grid). Each tile is 8×8 pixels and occupies 16 bytes.

## Tile Encoding (2-Bit Planar)

Each tile's 16 bytes are split into two bit-planes of 8 bytes each:
- **Bytes 0-7 (low plane):** Bit 0 of each pixel's color
- **Bytes 8-15 (high plane):** Bit 1 of each pixel's color

For pixel (x, y) in a tile: color = ((high_plane[y] >> (7-x)) & 1) << 1 | ((low_plane[y] >> (7-x)) & 1)

This gives a 2-bit color value (0-3) per pixel. Color 0 is always transparent (for sprites) or the background color. Colors 1-3 are looked up from the palette selected by the attribute table (backgrounds) or OAM attribute (sprites).

## Example Tile

For a tile at  (tile index 1 in pattern table 0):
`
Address  Data     Pixels (binary)
    %01000001  .#.....#  (low plane row 0)
    %11000010  ##....#.  (low plane row 1)
...
    %01000001  .#.....#  (high plane row 0)
    %00000010  .....#.   (high plane row 1)
`

Combining: pixel (1,0) has low=1, high=1 → color 3. pixel (7,0) has low=1, high=1 → color 3. This two-plane encoding was common in 8-bit era hardware — it allows efficient hardware implementation using shift registers.

## CHR ROM vs CHR RAM

Tiles can be stored in:
- **CHR ROM:** Read-only tiles burned into the cartridge chip. The mapper bank-switches different sections into the PPU's pattern table windows. Most NES games use CHR ROM.
- **CHR RAM:** 8 KB of writable memory on the cartridge. The CPU writes tile data through the PPU registers. Used by games like Mapper 2 titles (Mega Man, Castlevania). Allows dynamically generated or modified tiles.

## OxideNES Implementation

Pattern data is accessed through the mapper, which handles bank switching. The PPU reads pattern bytes during background and sprite fetch cycles. For performance, OxideNES caches decoded tile rows — when the PPU fetches a tile's two bytes, it immediately combines them into the 8-pixel color values rather than doing per-pixel bit extraction during rendering. This shift-register approach matches the real hardware and is computationally efficient.

## Color Palettes

The NES has a fixed master palette of 64 colors (though some are duplicates). The PPU maintains 8 palettes of 4 colors each (4 background + 4 sprite palettes) in palette RAM (-). Each palette entry is a 6-bit index into the master palette. The NES color space is unique — it's based on NTSC signal generation rather than RGB, producing characteristic colors that differ from simple RGB approximations.
