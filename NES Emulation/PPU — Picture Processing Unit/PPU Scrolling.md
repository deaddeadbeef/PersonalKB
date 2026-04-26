---
tags: [nes, wiki]
up: "[[PPU — Picture Processing Unit Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# PPU Scrolling

> **The Loopy register mechanism (v, t, x, w) that enables hardware scrolling across a 512×480 virtual space using a dual-register pipeline.**

## 🎯 Intuition
**The Core Idea:** PPU scrolling uses two 15-bit address registers (v and t) plus a 3-bit fine X register — the CPU writes the desired scroll position into t, and the PPU copies it to v at specific moments during rendering, creating smooth pixel-level scrolling across up to four nametables.
**Analogy:** Imagine the PPU's canvas is much larger than the screen — a 512×480 pixel mural. The screen is a 256×240 camera viewport. The t register is where you tell the camera "I want to look here next," and v is where the camera is actually pointed right now. At the start of each scanline, the camera's horizontal aim snaps to t's horizontal position; at the start of each frame, the vertical aim snaps too. The 3-bit fine X is like sub-pixel camera nudging for ultra-smooth horizontal panning.
**Why It Matters:** Scrolling is arguably the most complex PPU behavior to emulate correctly. The shared write toggle, the interaction between PPUSCROLL and PPUADDR, and the precise timing of t→v copies are responsible for more emulation bugs than almost any other feature.

---

## ⚙️ Core Mechanics
### How It Works
The NES screen is 256×240 but games often have worlds much larger. The PPU supports hardware scrolling across a 512×480 virtual space (4 nametables) using an intricate dual-register mechanism.

### Key Specifications

**The Loopy Registers**

| Register | Name | Purpose |
|----------|------|---------|
| **v** | Current VRAM address | Address used during rendering |
| **t** | Temporary VRAM address | Holds scroll position being set up |
| **x** | Fine X scroll | 3-bit (0-7) fine horizontal offset |
| **w** | Write toggle | Alternates between first/second write |

### Key Facts
- **Scroll Setup (CPU side):**
  - First PPUSCROLL write: Sets coarse X in t, fine X in x
  - Second PPUSCROLL write: Sets coarse Y and fine Y in t
  - PPUADDR writes also modify t (they share the same internal register)
- **Scroll Application (PPU side):**
  - Dot 257: Copy horizontal bits from t to v (X scroll reset each scanline)
  - Dots 280-304 of pre-render: Copy vertical bits from t to v (Y scroll reset for new frame)
  - Each tile fetch: v is used as the VRAM address and incremented
- **Split Scrolling:** Games achieve split-screen effects by:
  1. Setting scroll for the top portion
  2. Waiting for sprite 0 hit (or mapper IRQ at a specific scanline)
  3. Writing new scroll values to PPUSCROLL for the bottom portion
  - Used in Super Mario Bros. (status bar), Zelda II (top/bottom split), and many others

---

## 🔬 Deep Dive
### Hardware Behavior Details
**The v Register as a VRAM Address:** During rendering, the v register doubles as the VRAM address for tile fetches. Its bits encode: fine Y (3 bits), nametable select (2 bits), coarse Y (5 bits), coarse X (5 bits). The PPU increments coarse X after each tile fetch and fine/coarse Y at the end of each scanline.

**PPUSCROLL and PPUADDR Interaction:** Both registers write to the same internal t register through the same w toggle. Writing PPUADDR after PPUSCROLL (or vice versa) overwrites parts of t. Games must be careful about write order — and emulators must model this shared state exactly.

**Coarse Y Overflow:** When coarse Y increments past 29 (the last tile row), it wraps to 0 and toggles the vertical nametable bit. If coarse Y is set to 30 or 31 (via direct PPUADDR write), the PPU reads from the attribute table area as if it were tile data — a known quirk some games exploit.

### Common Emulation Pitfalls
1. **Not implementing the t→v horizontal copy at dot 257** — Without this, the X scroll position won't reset each scanline, causing horizontal scrolling to look completely wrong (each scanline scrolls further than the last)
2. **Missing the t→v vertical copy on pre-render scanline** — Without this, the Y scroll won't reset for the new frame, and vertical scrolling will drift or the screen will show the wrong vertical position
3. **PPUADDR corrupting scroll state** — PPUADDR writes modify t, which is also the scroll register. If a game writes PPUADDR during vblank for VRAM updates and then writes PPUSCROLL, the order matters. Incorrect toggle state handling here is one of the most common emulation bugs

### Reference Implementations
OxideNES `ppu.rs` implements the full Loopy register mechanism with `increment_scroll_x()`, `increment_scroll_y()`, `transfer_address_x()`, and `transfer_address_y()` methods at the correct cycle timings.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between the v and t registers, and when does v get its value from t?
2. Why does the PPU reset horizontal scroll every scanline but vertical scroll only once per frame?
3. How does a game like Super Mario Bros. keep the status bar stationary while the gameplay area scrolls?

### Core Problems
1. **Implement the Loopy register writes:** Write handlers for PPUSCROLL (0x2005) and PPUADDR (0x2006) that correctly update the t register and x register, alternating via the w toggle. Include PPUSTATUS reads resetting w.
2. **Implement scroll increment:** Write `increment_scroll_x()` that advances coarse X with nametable toggle on overflow, and `increment_scroll_y()` that advances fine Y, then coarse Y with nametable toggle and the coarse Y=29→0 wrap behavior.

### Challenge
**Split scroll implementation:** Implement a split-scroll effect where the top 48 pixels (6 tile rows) display a fixed status bar and the remaining 192 pixels scroll horizontally. Use sprite 0 hit to detect the split point. Write the exact sequence of PPUSCROLL writes in the NMI handler (before rendering) and in the sprite 0 hit polling loop (mid-frame). Account for the fact that PPUADDR writes during vblank may have already modified t.

---

*See also:* [[PPU Registers and Timing]], [[PPU Rendering Pipeline]], [[Backgrounds and Nametables]], [[Sprites and OAM]], [[PPU — Picture Processing Unit Overview]]

## References
→ [[Sources Index]]
