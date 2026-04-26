---
tags: [raw, nes-emulation, nametable]
source: "NESdev nametable reference + OxideNES ppu.rs"
---

# Raw NES 017 — Nametables and Mirroring

The NES PPU's background rendering system is built around nametables — 960-byte data structures that define which tiles appear on screen. Understanding nametables and their mirroring modes is essential for NES emulation.

## Nametable Structure

Each nametable is 1024 bytes total:
- **960 bytes (30 rows × 32 columns):** Tile index bytes. Each byte selects one of 256 tiles from the active pattern table (selected by PPUCTRL bit 4). The tile grid maps directly to screen pixels: row 0 = top 8 pixel rows, column 0 = leftmost 8 pixels.
- **64 bytes (attribute table):** Palette selection for 2×2 tile groups. Each byte covers a 4×4 tile area (32×32 pixels). The byte is divided into four 2-bit fields: bits 0-1 = top-left 2×2 group, bits 2-3 = top-right, bits 4-5 = bottom-left, bits 6-7 = bottom-right. Each 2-bit value selects one of 4 background palettes.

## Logical Nametable Space

The PPU addresses four logical nametables in a 2×2 grid:
- Nametable 0 at  (top-left)
- Nametable 1 at  (top-right)
- Nametable 2 at  (bottom-left)
- Nametable 3 at  (bottom-right)

This creates a 512×480 pixel virtual playfield (2×2 screens). Scrolling wraps around this space. However, the NES only has 2 KB of VRAM — enough for two physical nametables. The other two must be mirrored or provided by the cartridge.

## Mirroring Modes

**Vertical mirroring:** Nametables 0 and 2 share physical memory, as do 1 and 3. This gives two side-by-side unique screens — ideal for horizontal scrolling games (Super Mario Bros.). VRAM layout: [] A [] B [] A [] B.

**Horizontal mirroring:** Nametables 0 and 1 share, as do 2 and 3. Two vertically stacked unique screens — ideal for vertical scrolling (Ice Climber). VRAM layout: [] A [] A [] B [] B.

**Single-screen:** All four nametables map to the same physical memory. Used by some mappers (AxROM/Mapper 7) that dynamically select between two physical banks. Only one unique screen at a time.

**Four-screen:** The cartridge provides an extra 2 KB of RAM, giving all four nametables unique memory. Rare — used by a handful of games. Full 512×480 scrolling without mirroring artifacts.

## Mirroring in OxideNES

The mapper provides a mirror_mode() method returning an enum: Vertical, Horizontal, SingleLower, SingleUpper, FourScreen. The PPU calls a mirror_nametable_addr(addr) function that applies the appropriate mapping before each VRAM access. Some mappers (MMC1, MMC3) can change mirroring mode dynamically via register writes, enabling games to switch scrolling direction mid-play.

## Attribute Table Details

The attribute table's 2×2 tile granularity for palette selection is a significant constraint on NES graphics. It means color can only change every 16×16 pixels in the background. Games work around this with careful tile design, sprite overlays for extra color detail, and palette cycling effects. The attribute table is at the end of each nametable (, , , ).
