---
tags: [nes, wiki]
up: "[[PPU — Picture Processing Unit Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Backgrounds and Nametables

> **How the PPU constructs the background layer from a grid of 8x8 tiles, nametable maps, attribute tables for palette selection, and pattern table graphics.**

## 🎯 Intuition
**The Core Idea:** The NES background is a mosaic — a 32×30 grid of 8×8 pixel tiles where each cell is just an index pointing to a tile graphic, and the attribute table assigns a color palette to each 2×2 group of tiles.
**Analogy:** The PPU is an artist working with a stamp collection. The nametable is the blueprint saying "put stamp #42 here, stamp #7 there." The pattern table is the actual stamp book. The attribute table is a color guide saying "this corner of the canvas uses the blue palette, that corner uses the red palette." The artist follows the blueprint, stamps each tile, and colors them according to the guide — line by line, 60 times per second.
**Why It Matters:** Background rendering is the foundation of NES graphics — every game uses it. Understanding the nametable/attribute/pattern table pipeline is essential for correctly displaying any game's visuals, and mirroring determines how scrolling works.

---

## ⚙️ Core Mechanics
### How It Works
The NES background is a grid of 8x8 pixel tiles:
- **32 × 30 tiles** = 256 × 240 pixels
- Each tile is an index (0-255) into a **pattern table** (CHR ROM/RAM)
- Tiles use 2 bits per pixel (4 colors from a 4-color palette)

### Key Specifications

**Nametable Layout**

| Address | Nametable |
|---------|-----------|
| 0x2000-0x23FF | Nametable 0 (top-left) |
| 0x2400-0x27FF | Nametable 1 (top-right) |
| 0x2800-0x2BFF | Nametable 2 (bottom-left) |
| 0x2C00-0x2FFF | Nametable 3 (bottom-right) |

**Nametable Mirroring** (NES has only 2 KB VRAM):
- **Horizontal mirroring** — NT0=NT1, NT2=NT3 (vertical scrolling games)
- **Vertical mirroring** — NT0=NT2, NT1=NT3 (horizontal scrolling games)
- **Four-screen** — Cartridge provides extra 2 KB (rare)

### Key Facts
- **Attribute Tables:** The last 64 bytes of each nametable form the attribute table, which assigns palettes to 2×2 tile groups (16×16 pixel areas); each byte controls a 4×4 tile area using 2-bit fields
- **Pattern Tables:** Two 4 KB tables at PPU 0x0000-0x1FFF:
  - 0x0000-0x0FFF — Pattern table 0 (usually background)
  - 0x1000-0x1FFF — Pattern table 1 (usually sprites)
- Each tile is 16 bytes: 8 bytes for bit plane 0 + 8 bytes for bit plane 1, combined to form 2-bit pixel values

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Attribute Table Resolution Limit:** Each attribute byte covers a 32×32 pixel (4×4 tile) area, but each 2-bit palette selector covers a 16×16 pixel (2×2 tile) area. This means the palette can only change every 16 pixels, creating the coarse color grid visible in many NES games. Games that need finer palette control must resort to mid-scanline register writes.

**Tile Fetching Pipeline:** During rendering, the PPU fetches tile data in a specific sequence: nametable byte (which tile), attribute byte (which palette), pattern table low byte, pattern table high byte — each taking 2 PPU cycles, for a total of 8 cycles (8 dots) per tile, exactly matching the 8-pixel tile width.

**Bit Plane Interleaving:** Each tile's two bit planes are stored sequentially (not interleaved): first all 8 bytes of plane 0, then all 8 bytes of plane 1. Pixel value = (plane1_bit << 1) | plane0_bit.

### Common Emulation Pitfalls
1. **Wrong attribute table decoding** — The 2-bit fields within each attribute byte must be extracted for the correct quadrant (top-left, top-right, bottom-left, bottom-right); getting the shift wrong makes palettes apply to the wrong tile groups
2. **Mirroring mode not matching cartridge** — If you hardcode Horizontal mirroring but the game uses Vertical, scrolling will visually repeat the wrong way and screen transitions will glitch
3. **Pattern table bit plane combination** — If you combine the two bit planes incorrectly (e.g., swapping plane 0 and plane 1), all tile graphics will appear corrupted

### Reference Implementations
OxideNES `ppu.rs` fetches nametable bytes, attribute bytes, and pattern data in the correct dot sequence. `mirror_vram_addr()` handles all mirroring modes (Horizontal, Vertical, FourScreen, SingleScreen).

---

## 🏋️ Practice
### Warm-Up (5 min)
1. How many bytes does a single nametable occupy, and what does each byte represent?
2. Why can the attribute table only assign palettes at 16×16 pixel granularity instead of per-tile?
3. What is the difference between CHR ROM and CHR RAM, and why does it matter for mappers?

### Core Problems
1. **Decode an attribute byte:** Given attribute byte 0xE4 at nametable offset 0x23C0, which palette indices apply to each of the four 2×2 tile groups it covers? Write the bit extraction logic.
2. **Render a single tile:** Given a tile index, pattern table base address, and attribute palette index, write a function that produces an 8×8 array of palette color indices (0-3 combined with the 2-bit attribute).

### Challenge
**Mid-scanline palette switch:** A game wants different palettes for the left and right halves of the screen, but the attribute table doesn't support per-tile palette control. Explain how a game could use timed writes to PPUADDR/PPUDATA during rendering to change palette RAM mid-scanline, and what visual artifacts would appear if the timing is off by 1 PPU dot.

---

*See also:* [[PPU Rendering Pipeline]], [[PPU Scrolling]], [[PPU Registers and Timing]], [[Sprites and OAM]], [[PPU — Picture Processing Unit Overview]]

## References
→ [[Sources Index]]
