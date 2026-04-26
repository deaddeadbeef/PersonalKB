---
tags: [raw, nes-emulation, sprites]
source: "NESdev sprite rendering + OxideNES ppu.rs"
---

# Raw NES 014 — Sprite Rendering and OAM

The NES PPU supports 64 sprites stored in Object Attribute Memory (OAM), a dedicated 256-byte RAM internal to the PPU. Each sprite entry is 4 bytes.

## OAM Entry Format

Each of the 64 sprites uses 4 consecutive bytes:
- **Byte 0 — Y position:** Top edge of sprite minus 1 (sprite at Y=0 is placed at scanline 1). Values 0xEF-0xFF hide 8x8 sprites off-screen bottom.
- **Byte 1 — Tile index:** For 8x8 sprites, this is the tile number in the pattern table selected by PPUCTRL bit 3. For 8x16 sprites, bit 0 selects the pattern table (0=0x0000, 1=0x1000), and bits 7-1 give the top tile number (bottom tile is top+1).
- **Byte 2 — Attributes:** Bits 0-1 = palette (from sprite palettes 0x3F10-0x3F1F), bit 5 = priority (0=in front of background, 1=behind background), bit 6 = horizontal flip, bit 7 = vertical flip.
- **Byte 3 — X position:** Left edge of sprite. No wrapping — sprites at X positions that go off the right edge are clipped.

## Sprite Evaluation (per scanline)

During each visible scanline, the PPU evaluates which sprites are on the NEXT scanline:
1. Clear secondary OAM (32 bytes, holds up to 8 sprites)
2. Iterate through all 64 primary OAM entries
3. For each sprite, check if the next scanline falls within its Y range (Y+1 to Y+8 or Y+16)
4. If yes and fewer than 8 sprites found, copy the 4-byte entry to secondary OAM
5. If 8 sprites already found and another is in range, set the sprite overflow flag in PPUSTATUS
6. The sprite overflow flag has a hardware bug: after finding 8 sprites, the evaluation incorrectly increments both the sprite index AND the byte offset within each sprite entry, causing it to miss some sprites and false-trigger on others

## Sprite Pixel Fetch

After evaluation, the PPU fetches pattern data for the (up to) 8 selected sprites. For each sprite, it reads the pattern table low and high bytes for the appropriate tile row (accounting for vertical flip). These are stored in shift registers alongside the sprite's X position, attributes, and priority.

## Sprite-0 Hit

The sprite-0 hit flag in PPUSTATUS is set when: an opaque pixel of sprite 0 overlaps with an opaque pixel of the background, rendering is enabled for both backgrounds and sprites, the pixel is not at X=255, and (if left-side clipping is enabled) the pixel is not in X=0-7. This flag is widely used for timing mid-frame scroll changes. The exact cycle of the hit depends on the sprite's X position and the background pixel pattern.

## Sprite Priority

Sprite priority has two levels: sprite-vs-background (per-sprite attribute bit) and sprite-vs-sprite (sprite 0 has highest priority, sprite 63 lowest). When multiple sprites overlap, the lowest-numbered sprite's pixel wins. Background priority means the sprite pixel is only visible where the background pixel is transparent (color 0 of any palette).

## OAM Corruption and DMA

Direct access to OAM through 0x2003/0x2004 is unreliable during rendering (reading returns internal values, writing corrupts evaluation). Games use OAM DMA (0x4014) to bulk-write OAM from CPU RAM. OxideNES supports both access methods but games that rely on 0x2003/0x2004 during rendering may not render correctly, matching real hardware behavior.