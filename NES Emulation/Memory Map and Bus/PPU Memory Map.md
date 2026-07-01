---
tags: [nes, wiki]
up: "[[Memory Map and Bus Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# PPU Memory Map

> **The PPU's separate 16 KB address space containing pattern tables (tile graphics), nametables (screen layout), and palette RAM.**

## 🎯 Intuition
**The Core Idea:** The PPU has its own private address bus and memory, completely separate from the CPU — it maps tile graphics from the cartridge, screen layout in VRAM, and color palettes into a 16 KB space with its own mirroring rules.
**Analogy:** If the CPU memory map is the town's postal system, the PPU memory map is a separate postal system for the art studio. The pattern tables are the tile catalog (shipped in from the cartridge warehouse), the nametables are the canvas grid showing which tile goes where, and the palette is the paint rack with 32 color slots.
**Why It Matters:** Your emulator needs a completely separate address decoder for the PPU bus. Nametable mirroring varies per cartridge (controlled by hardware), and palette mirroring has its own special rules — errors here cause garbled graphics or wrong colors.

---

## ⚙️ Core Mechanics
### How It Works
The PPU addresses a 14-bit (16 KB) address space. Pattern tables come from the cartridge's CHR ROM/RAM, nametables use 2 KB of internal VRAM with mirroring controlled by the cartridge, and 32 bytes of palette RAM determine colors.

### Key Specifications

**PPU Address Space**

| Range | Size | Content |
|-------|------|---------|
| 0x0000-0x0FFF | 4 KB | Pattern table 0 (CHR ROM/RAM) |
| 0x1000-0x1FFF | 4 KB | Pattern table 1 (CHR ROM/RAM) |
| 0x2000-0x23FF | 1 KB | Nametable 0 |
| 0x2400-0x27FF | 1 KB | Nametable 1 |
| 0x2800-0x2BFF | 1 KB | Nametable 2 |
| 0x2C00-0x2FFF | 1 KB | Nametable 3 |
| 0x3000-0x3EFF | - | Mirror of 0x2000-0x2EFF |
| 0x3F00-0x3F1F | 32 bytes | Palette RAM |
| 0x3F20-0x3FFF | - | Mirrors of palette |

### Key Facts
- **Pattern Tables:** Supplied by the cartridge (CHR ROM or CHR RAM); each holds 256 tiles of 16 bytes each (8x8 pixels, 2 bits per pixel); mappers can bank-switch these to access much more tile data
- **Nametable Mirroring:** Only 2 KB of physical VRAM exists for 4 logical nametables; the cartridge controls mirroring via hardware:
  - **Horizontal:** Two unique screens, one above the other
  - **Vertical:** Two unique screens, side by side
  - **Single-screen:** All four nametables point to the same 1 KB
  - **Four-screen:** Cartridge provides 2 KB extra (rare)
- **Palette RAM (32 bytes at 0x3F00-0x3F1F):**
  - 0x3F00: Universal background color
  - 0x3F01-0x3F03: Background palette 0
  - 0x3F05-0x3F07: Background palette 1
  - 0x3F09-0x3F0B: Background palette 2
  - 0x3F0D-0x3F0F: Background palette 3
  - 0x3F11-0x3F13: Sprite palette 0-3 (similarly)
  - Addresses 0x3F10, 0x3F14, 0x3F18, 0x3F1C mirror 0x3F00, 0x3F04, 0x3F08, 0x3F0C

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Palette Mirroring Quirk:** The "sprite" palette entries at 0x3F10, 0x3F14, 0x3F18, and 0x3F1C are mirrors of the corresponding "background" entries (0x3F00, 0x3F04, 0x3F08, 0x3F0C). This is because those entries represent the "transparent" color for each palette, which is always the universal background color. Writing to 0x3F10 changes 0x3F00 and vice versa.

**Nametable Mirroring Is Cartridge-Controlled:** The NES console provides 2 KB of VRAM, but the cartridge's hardware wiring determines how the four logical nametable addresses map to physical VRAM pages. This means mirroring mode can even change dynamically (some mappers switch mirroring mid-frame).

**Address Wrapping:** PPU addresses above 0x3FFF wrap around (the PPU only has a 14-bit address bus). Access to 0x4000 is the same as 0x0000.

### Common Emulation Pitfalls
1. **Wrong palette mirroring** — If 0x3F10 and 0x3F00 don't alias each other, background colors will be wrong in many games (the universal background color won't update correctly)
2. **Hardcoding nametable mirroring** — Mirroring mode depends on the cartridge, not the console. You must read the iNES header to determine the initial mode and support mapper-controlled dynamic changes
3. **Forgetting 0x3000-0x3EFF nametable mirror** — This range mirrors 0x2000-0x2EFF; games rarely access it directly, but test ROMs check it

### Reference Implementations
OxideNES ppu.rs implements `ppu_read()`/`ppu_write()` with `mirror_vram_addr()` for nametable mirroring and `mirror_palette_addr()` for palette mirroring. Direct palette table access optimizes the critical rendering path.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. How many physical bytes of VRAM does the NES have for nametables, and how many logical nametable addresses exist?
2. What happens when you write a color value to PPU address 0x3F10?
3. Why are pattern tables supplied by the cartridge rather than built into the console?

### Core Problems
1. **Implement `ppu_read()`/`ppu_write()`:** Write the PPU bus routing function that handles pattern table access (from cartridge), nametable access (with configurable mirroring), and palette access (with palette-specific mirroring).
2. **Nametable mirroring:** Implement all four mirroring modes (Horizontal, Vertical, SingleScreen, FourScreen) as a function that maps a nametable address (0x2000-0x2FFF) to a physical VRAM offset (0-2047).

### Challenge
**Dynamic mirroring:** A game using MMC3 switches nametable mirroring from Vertical to Horizontal mid-frame. Explain what visual effect this produces and implement a mirroring mode switch that takes effect at the correct scanline. What does the screen look like if the switch happens at scanline 120?

---

*See also:* [[CPU Memory Map]], [[OAM DMA]], [[Backgrounds and Nametables]], [[Memory Map and Bus Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
