---
tags: [nes, wiki]
up: "[[PPU — Picture Processing Unit Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Sprites and OAM

> **The PPU's sprite system: 64 sprites stored in 256 bytes of OAM, with per-scanline evaluation, an 8-sprite limit, and the critical sprite 0 hit detection.**

## 🎯 Intuition
**The Core Idea:** Sprites are the movable objects layered on top of (or behind) the background — the PPU stores 64 of them in dedicated OAM memory and evaluates each scanline to find which sprites are visible, subject to a hard limit of 8 per scanline.
**Analogy:** If the background is the artist's painted canvas, sprites are cutout stickers placed on top. OAM is a filing cabinet of 64 sticker descriptions (position, which sticker design, colors, layering). Each scanline, the artist quickly flips through all 64 entries to find which stickers appear on this line — but can only place 8 stickers per line. If there are more, some go invisible (and games make them flicker by rotating the filing order each frame).
**Why It Matters:** Sprite evaluation timing, the 8-sprite limit, and sprite 0 hit are among the most timing-sensitive PPU behaviors. Sprite 0 hit is the primary mechanism for screen splits in countless games.

---

## ⚙️ Core Mechanics
### How It Works
OAM is 256 bytes of dedicated PPU memory holding 64 sprites (4 bytes each). Each scanline, the PPU evaluates all 64 entries to find up to 8 sprites visible on that line, then fetches their pattern data.

### Key Specifications

**OAM Entry Format (4 bytes per sprite)**

| Byte | Content |
|------|---------|
| 0 | Y position (top of sprite, actual = value + 1) |
| 1 | Tile index (pattern table lookup) |
| 2 | Attributes: palette (bits 0-1), priority (bit 5), flip H (bit 6), flip V (bit 7) |
| 3 | X position (left of sprite) |

**Sprite Sizes** (selected by PPUCTRL bit 5):
- **8×8 mode:** Sprites use a single tile from the selected pattern table
- **8×16 mode:** Sprites use two vertically stacked tiles; tile index bit 0 selects the pattern table, allowing sprites to use tiles from either table

### Key Facts
- **Sprite Rendering Pipeline:**
  1. Evaluation phase (dots 257-320): PPU scans all 64 OAM entries, finding up to 8 sprites on the current scanline
  2. Fetch phase: Load pattern data for selected sprites
  3. Output: Each pixel, check if any sprite has an opaque pixel at this position
- **8-Sprite Limit:** The NES can only display 8 sprites per scanline; when more are found, the overflow flag is set (PPUSTATUS bit 5) and additional sprites are invisible; games handle this with **sprite cycling** — rotating sprite priority each frame to distribute flickering evenly
- **Sprite Zero Hit:** When sprite 0's opaque pixel overlaps a background opaque pixel, the sprite 0 hit flag (PPUSTATUS bit 6) is set; games poll this flag to time mid-frame effects like screen splits
- **OAM DMA:** Writing to CPU address 0x4014 triggers DMA that copies 256 bytes from CPU memory to OAM, taking 513 or 514 CPU cycles — the standard way to update sprites each frame

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Sprite Evaluation Bug:** The NES's sprite overflow detection has a hardware bug — when searching for the 9th sprite, the evaluation logic incorrectly increments both the sprite index and the byte offset within each OAM entry, causing it to check the wrong bytes of subsequent sprites. This means the overflow flag is unreliable (it can both miss overflows and report false positives).

**Sprite 0 Hit Restrictions:** Sprite 0 hit cannot trigger at X=255 (the rightmost pixel), and it cannot trigger if either background or sprite rendering is disabled via PPUMASK. It also cannot trigger during the left 8 pixels if left-column clipping is enabled.

**Y Position Off-By-One:** The Y value in OAM represents the scanline *above* where the sprite first appears. A Y value of 0 means the sprite starts on scanline 1. A Y value of 0xEF is the last visible position for an 8×8 sprite (scanlines 240-247 are off-screen). Setting Y to 0xEF+ effectively hides the sprite.

### Common Emulation Pitfalls
1. **Sprite 0 hit timing too early or late** — The hit flag must be set at the exact pixel/dot where the overlap occurs, not at the end of the scanline. Super Mario Bros. and many other games poll this in a tight loop for screen splits
2. **Not implementing the sprite overflow bug** — If you implement "correct" overflow detection (finding the true 9th sprite), test ROMs will fail and a few games that exploit the buggy behavior will break
3. **Forgetting the Y+1 offset** — Every sprite appears one scanline lower than its OAM Y value. If you display at Y exactly, all sprites will be one pixel too high

### Reference Implementations
OxideNES `ppu.rs` scans all 64 OAM entries at cycle 257 of each visible scanline. The `Bus` handles DMA via `dma_active()`/`dma_tick()` with cycle-accurate timing including the dummy cycle on odd CPU cycles.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does the NES limit sprites to 8 per scanline, and how do games work around this limitation?
2. What is the difference between sprite priority bit 5=0 and bit 5=1 in the OAM attribute byte?
3. How does 8×16 sprite mode differ from 8×8 mode in terms of tile index interpretation?

### Core Problems
1. **Implement sprite evaluation:** Write the per-scanline evaluation that scans all 64 OAM entries, determines which sprites are in range (accounting for sprite height and the Y+1 offset), and selects the first 8 with overflow flag handling.
2. **Implement sprite pixel output:** For a given screen X position, check all evaluated sprites (in priority order) for an opaque pixel, apply horizontal flip if needed, and resolve priority against the background pixel.

### Challenge
**Sprite overflow bug replication:** Implement the hardware-accurate sprite overflow evaluation bug where the byte offset within each OAM entry increments along with the sprite index when searching past the 8th sprite. Construct a test case with 9 sprites on one scanline and verify that your buggy evaluation produces the same false result as real hardware (checking bytes at offsets 0, 1, 2, 3 of successive sprites instead of always offset 0 for Y comparison).

---

*See also:* [[PPU Rendering Pipeline]], [[Backgrounds and Nametables]], [[PPU Registers and Timing]], [[OAM DMA]], [[PPU — Picture Processing Unit Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
