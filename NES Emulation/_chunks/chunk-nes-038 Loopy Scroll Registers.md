---
tags: [chunk, nes-emulation, scrolling]
source: "[[raw-nes-012]]"
up: "[[PPU Scrolling]]"
---

# Chunk NES 038 — Loopy Scroll Registers

The PPU uses four internal registers for scrolling: v (15-bit current VRAM address tracking render position), t (15-bit temporary address holding programmed scroll), x (3-bit fine horizontal scroll, 0-7 pixels), and w (1-bit write toggle for sequential register writes). The v/t layout encodes coarse X (5 bits, tile column), coarse Y (5 bits, tile row), nametable select (2 bits), and fine Y (3 bits, pixel row). Games set scroll via PPUSCROLL () two-write sequence. PPUADDR () also modifies t, enabling mid-frame scroll tricks. This dual-purpose sharing of the t register is key to advanced NES visual effects.
