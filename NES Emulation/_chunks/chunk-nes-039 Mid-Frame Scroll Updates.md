---
tags: [chunk, nes-emulation, scrolling]
source: "[[raw-nes-012]]"
up: "[[PPU Scrolling]]"
---

# Chunk NES 039 — Mid-Frame Scroll Updates

During rendering, the PPU copies scroll components from t to v at precise cycle positions. At cycle 257 of each visible scanline, horizontal bits (coarse X and nametable horizontal) copy from t to v, resetting horizontal scroll each line. During cycles 280-304 of the pre-render scanline, vertical bits copy, setting the frame's starting vertical position. Every 8 cycles, coarse X increments with nametable toggle at wrap. At cycle 256, fine Y increments (0-7), then coarse Y increments. Games create fixed status bars by writing new scroll values after sprite-0 hit detection, exploiting the t-to-v copy timing.
