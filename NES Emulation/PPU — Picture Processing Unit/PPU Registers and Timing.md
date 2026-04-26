---
tags: [nes, wiki]
up: "[[PPU — Picture Processing Unit Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# PPU Registers and Timing

> **The 8 memory-mapped PPU registers at 0x2000-0x2007 and their critical timing-sensitive side effects that drive NES graphics.**

## 🎯 Intuition
**The Core Idea:** The CPU controls the PPU through just 8 registers — but these registers have complex side effects, shared internal state (the write toggle and read buffer), and timing-sensitive behaviors that make them far trickier than they appear.
**Analogy:** The PPU registers are like a control panel for the artist with hidden gotchas: reading the status display (PPUSTATUS) resets a switch, the data readout (PPUDATA) always shows yesterday's value, and two dials (PPUSCROLL and PPUADDR) share a hidden flip-flop that alternates between "setting the first half" and "setting the second half."
**Why It Matters:** Nearly every visual bug in an NES emulator traces back to incorrect register behavior — missing the PPUSTATUS read side effects, forgetting the PPUDATA read buffer, or mishandling the scroll/address write toggle.

---

## ⚙️ Core Mechanics
### How It Works
The CPU accesses the PPU through 8 registers mapped at 0x2000-0x2007, mirrored every 8 bytes through 0x3FFF (1023 mirrors). Several registers have critical side effects on read or write.

### Key Specifications

**CPU-Accessible PPU Registers**

| Address | Register | R/W | Description |
|---------|----------|-----|-------------|
| 0x2000 | PPUCTRL | W | NMI enable, sprite size, pattern table select, increment mode |
| 0x2001 | PPUMASK | W | Color emphasis, sprite/background enable, left-column clip |
| 0x2002 | PPUSTATUS | R | Vblank flag, sprite 0 hit, sprite overflow |
| 0x2003 | OAMADDR | W | OAM write address |
| 0x2004 | OAMDATA | R/W | OAM data read/write |
| 0x2005 | PPUSCROLL | W(x2) | Fine scroll position (two writes via toggle) |
| 0x2006 | PPUADDR | W(x2) | VRAM address (two writes via toggle) |
| 0x2007 | PPUDATA | R/W | VRAM data with auto-increment |

### Key Facts
- These 8 registers are mirrored every 8 bytes from 0x2000 to 0x3FFF (1023 mirrors)
- PPUSCROLL and PPUADDR share an internal write toggle (w) — each requires two sequential writes
- Reading PPUSTATUS resets the write toggle
- PPUDATA reads are buffered (delayed by one read) except for palette addresses

---

## 🔬 Deep Dive
### Hardware Behavior Details
**PPUSTATUS Read Side Effects (0x2002):**
- Clears the vblank flag (bit 7)
- Resets the write toggle (w)
- Reading one cycle before NMI suppresses the NMI entirely

**PPUDATA Read Buffer:** Reads from PPUDATA return the **previous** value in an internal buffer (delayed by one read), except for palette reads (0x3F00-0x3FFF) which return immediately while still updating the buffer with the nametable byte "behind" the palette address.

**Odd Frame Skip:** On NTSC, odd frames skip the last dot of the pre-render scanline when rendering is enabled, making odd frames 89,341 dots vs even frames' 89,342 dots. This is the PPU's way of maintaining precise color burst phase alternation.

**PPUCTRL Increment Mode:** Bit 2 of PPUCTRL selects whether PPUADDR auto-increments by 1 (horizontal) or 32 (vertical) after each PPUDATA access. Vertical increment (+32) is used for column-wise VRAM updates.

### Common Emulation Pitfalls
1. **Not clearing vblank on PPUSTATUS read** — If the vblank flag stays set after reading 0x2002, games that poll PPUSTATUS in a loop will never exit the loop (or exit immediately every time)
2. **Forgetting the PPUDATA read buffer** — The first PPUDATA read after setting PPUADDR returns stale buffer data. Games expect to discard the first read — if your emulator returns the correct value immediately, the game reads wrong data on subsequent reads
3. **Ignoring the shared write toggle** — PPUSCROLL and PPUADDR share the w toggle. If a game writes to PPUSCROLL once, then reads PPUSTATUS (resetting w), then writes to PPUADDR, the toggle state must be correct or scroll values will be corrupted

### Reference Implementations
OxideNES `ppu.rs` implements all register behaviors in `cpu_read()` and `cpu_write()` methods. The PPUDATA read buffer, PPUSTATUS side effects, and scroll toggle are all accurately emulated.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What three things happen when the CPU reads address 0x2002?
2. Why does the first read from PPUDATA after setting PPUADDR return "garbage"?
3. If a game writes to PPUSCROLL once and then reads PPUSTATUS, what happens to the write toggle?

### Core Problems
1. **Implement PPUSTATUS read:** Write the 0x2002 read handler that returns the current status byte, clears the vblank flag, and resets the write toggle — all in one operation.
2. **Implement PPUDATA read/write:** Write the 0x2007 handler that manages the internal read buffer (buffered reads for non-palette, immediate for palette), and auto-increments the VRAM address by 1 or 32 based on PPUCTRL.

### Challenge
**NMI suppression race:** A game reads PPUSTATUS on the exact dot when VBlank begins (scanline 241, dot 1). Does the read return the vblank flag as set or clear? Does NMI fire or get suppressed? Implement the cycle-exact interaction between PPUSTATUS read, vblank flag set, and NMI edge detection. Test against the `vbl_nmi_timing` test ROM expectations.

---

*See also:* [[PPU Rendering Pipeline]], [[PPU Scrolling]], [[Backgrounds and Nametables]], [[Sprites and OAM]], [[PPU — Picture Processing Unit Overview]]

## References
→ [[Sources Index]]
