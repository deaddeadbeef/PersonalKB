---
tags: [raw, nes-emulation, scrolling]
source: "NESdev PPU scrolling + OxideNES ppu.rs"
---

# Raw NES 012 — PPU Scrolling Mechanics

PPU scrolling is one of the most complex aspects of NES emulation. The NES achieves smooth scrolling through a set of internal registers (v, t, x, w) that control which portion of the nametable space is visible.

## The Loopy Registers

Named after the "loopy" document that first described them in detail, the PPU has four internal registers for scroll position:
- **v (current VRAM address, 15 bits):** The VRAM address currently being accessed/rendered from. During rendering, it tracks the current pixel position in nametable space.
- **t (temporary VRAM address, 15 bits):** Holds the scroll position set by the program. Copied to v at specific times during rendering.
- **x (fine X scroll, 3 bits):** Sub-tile horizontal scroll (0-7 pixels). Set by the first write to PPUSCROLL.
- **w (write toggle, 1 bit):** Tracks whether the next write to PPUSCROLL or PPUADDR is the first or second byte.

## v/t Register Layout

``
yyy NN YYYYY XXXXX

||| || ||||| +++++-- coarse X scroll (tile column, 0-31)
||| || +++++------- coarse Y scroll (tile row, 0-29)
||| ++------------ nametable select (0-3)
+++--------------- fine Y scroll (pixel row within tile, 0-7)
``

## Setting Scroll Position

Games set the scroll through two consecutive writes to PPUSCROLL (0x2005):
1. First write (w=0): Sets coarse X in t, fine X in x register. Toggles w to 1.
2. Second write (w=1): Sets coarse Y and fine Y in t. Toggles w to 0.

Alternatively, writing to PPUADDR (0x2006) also modifies t (and on the second write, copies t to v). This dual-purpose nature of the t register means games can set scroll position through PPUADDR writes — a technique used by some games for mid-screen scroll changes.

## During Rendering

At specific PPU cycle positions during each visible scanline:
- **Cycle 257:** Horizontal components of v are copied from t (coarse X and nametable horizontal bit). This resets horizontal scroll at the start of each scanline.
- **Cycles 280-304 (pre-render scanline only):** Vertical components of v are copied from t (coarse Y, fine Y, and nametable vertical bit). This sets the starting vertical scroll for the new frame.
- **Every 8 cycles:** Coarse X in v increments (wrapping from 31 to 0 and toggling horizontal nametable bit).
- **Cycle 256:** Y in v increments — fine Y goes 0-7, then coarse Y increments, wrapping from 29 to 0 (with nametable vertical bit toggle). Coarse Y values 30-31 don't wrap normally — 30 toggles the nametable bit, 31 doesn't.

## Split Scrolling

Many games change the scroll position mid-frame to create status bars (fixed HUD at top/bottom with scrolling playfield). This is done by writing to PPUSCROLL or PPUADDR during HBlank or via sprite-0 hit timing. Since writes to 0x2005/0x2006 only affect t, the change only takes effect when hardware copies t components to v at the appropriate times. The most common technique is the "split scroll": render a fixed status bar, detect sprite-0 hit, then write new scroll values.

## OxideNES Implementation

OxideNES implements the loopy registers as separate fields in the PPU struct. All cycle-accurate copies from t to v are implemented at the documented cycle positions. The scroll register write handling correctly interleaves with PPUADDR writes (both share the w toggle). This accuracy is critical — many games rely on exact scroll register behavior for visual effects.