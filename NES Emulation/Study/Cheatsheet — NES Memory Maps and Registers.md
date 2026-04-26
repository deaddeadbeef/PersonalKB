---
tags: [study, nes-emulation, cheatsheet]
up: "[[NES Emulation Study Index]]"
---

# Cheatsheet — NES Memory Maps and Registers

Quick reference for NES address spaces and register layouts.

## CPU Address Space (-)

| Range | Size | Device |
|-------|------|--------|
| - | 2 KB | Internal RAM (mirrored to ) |
| - | 8 bytes | PPU registers (mirrored to ) |
| - | 20 bytes | APU registers |
|  | 1 byte | OAM DMA |
|  | 1 byte | APU status |
|  | 1 byte | Controller 1 + strobe |
|  | 1 byte | Controller 2 / APU frame counter |
| - | ~8 KB | Expansion (mapper-dependent) |
| - | 8 KB | PRG RAM / SRAM (battery-backed) |
| - | 32 KB | PRG ROM (mapper-banked) |

## PPU Address Space (-)

| Range | Size | Content |
|-------|------|---------|
| - | 4 KB | Pattern Table 0 (left) |
| - | 4 KB | Pattern Table 1 (right) |
| - | 1 KB | Nametable 0 |
| - | 1 KB | Nametable 1 |
| - | 1 KB | Nametable 2 |
| - | 1 KB | Nametable 3 |
| - | 16 bytes | Background palettes |
| - | 16 bytes | Sprite palettes |

## PPU Registers

| Addr | Name | R/W | Key Bits |
|------|------|-----|----------|
|  | PPUCTRL | W | NMI enable, sprite size, pattern table select, VRAM increment |
|  | PPUMASK | W | Render enable (BG/sprite), color emphasis, grayscale |
|  | PPUSTATUS | R | VBlank (bit 7), sprite-0 hit (bit 6), overflow (bit 5) |
|  | OAMADDR | W | OAM address |
|  | OAMDATA | R/W | OAM data |
|  | PPUSCROLL | W×2 | Scroll X (1st write), Scroll Y (2nd write) |
|  | PPUADDR | W×2 | VRAM address high (1st), low (2nd) |
|  | PPUDATA | R/W | VRAM data (auto-increments address) |

## Interrupt Vectors

| Vector | Address | Source |
|--------|---------|--------|
| NMI | - | PPU VBlank (edge-triggered) |
| RESET | - | Power-on / reset button |
| IRQ/BRK | - | Mapper IRQ or BRK instruction |

## Timing Constants (NTSC)

| Parameter | Value |
|-----------|-------|
| Master clock | 21.477272 MHz |
| CPU clock | 1.789773 MHz (master / 12) |
| PPU clock | 5.369318 MHz (master / 4) |
| PPU:CPU ratio | 3:1 |
| Scanlines/frame | 262 |
| PPU cycles/scanline | 341 |
| Frame rate | ~60.0988 FPS |
| CPU cycles/frame | ~29,780.67 |

## OAM Entry (4 bytes per sprite, 64 sprites)

| Byte | Content |
|------|---------|
| 0 | Y position (top - 1) |
| 1 | Tile index (8x16: bit 0 = pattern table) |
| 2 | Attributes: palette (0-1), priority (5), H-flip (6), V-flip (7) |
| 3 | X position |
