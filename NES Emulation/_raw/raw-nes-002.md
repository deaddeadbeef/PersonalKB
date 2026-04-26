---
tags: [raw, nes-emulation, ppu]
source: "OxideNES ppu.rs + NESdev PPU reference"
---

# Raw NES 002 — PPU Rendering Pipeline

The NES Picture Processing Unit (PPU) in OxideNES is implemented in `ppu.rs` (~781 lines). It renders 256×240 pixel frames at ~60.1 FPS (NTSC). The PPU operates on a scanline-by-scanline basis with 341 PPU cycles per scanline and 262 scanlines per frame (including pre-render and vblank lines).

## Scanline Types

- **Pre-render scanline (-1/261):** Clears sprite overflow and sprite-0 hit flags. Reloads vertical scroll bits from the t register. Fetches tile data for the first visible scanline.
- **Visible scanlines (0-239):** Active rendering. Each scanline fetches background tiles (nametable byte, attribute byte, pattern low/high) in 8-cycle groups, evaluates sprites for the NEXT scanline, and outputs pixels via multiplexer logic.
- **Post-render scanline (240):** Idle — PPU does nothing but the frame is complete.
- **VBlank scanlines (241-260):** VBlank flag is set at cycle 1 of scanline 241, triggering NMI if enabled. CPU uses this time for game logic and VRAM updates.

## Background Rendering

Every 8 cycles during visible scanlines, the PPU fetches: (1) nametable byte identifying the tile, (2) attribute byte for palette selection, (3) pattern table low byte, (4) pattern table high byte. Two shift registers hold 16 bits of pattern data (current + next tile). The fine X scroll selects which bit of the shift register becomes the pixel. At the end of each tile fetch, the coarse X scroll increments; at the end of each scanline, the Y scroll increments.

## Sprite Rendering

During each visible scanline, the PPU evaluates up to 64 sprites in OAM for the NEXT scanline. Up to 8 sprites per scanline are selected (setting overflow flag if more exist). Sprite pixels are fetched from pattern tables and held in per-sprite shift registers. The multiplexer resolves priority: sprite-0 hit detection occurs when an opaque sprite-0 pixel overlaps an opaque background pixel. Sprite priority (front/behind background) is per-sprite via an OAM attribute bit.

## PPU Registers

Key memory-mapped registers at $2000-$2007: PPUCTRL ($2000) controls NMI enable, sprite size, background/sprite pattern table selection, and VRAM increment direction. PPUMASK ($2001) controls rendering enable and color emphasis. PPUSTATUS ($2002) returns vblank, sprite-0 hit, and overflow flags (reading clears vblank and resets the w latch). PPUADDR/PPUDATA ($2006/$2007) provide VRAM access. OAMADDR/OAMDATA ($2003/$2004) access OAM. PPUSCROLL ($2005) sets scroll position.

## OxideNES Implementation Notes

The PPU uses a `render_pixel()` method called each cycle during visible scanlines. Background and sprite data are composed using the priority multiplexer. The frame buffer is a flat `[u8; 256 * 240 * 4]` RGBA array passed to the display backend (minifb). Nametable mirroring (horizontal, vertical, four-screen, single-screen) is configured by the cartridge mapper.
