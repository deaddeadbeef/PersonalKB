---
tags: [chunk, nes-emulation, testing]
source: "[[raw-nes-028]]"
up: "[[Emulator Architecture Overview]]"
---

# Chunk NES 070 — PPU and APU Test ROM Suites

Blargg's test ROM suites validate PPU and APU accuracy. sprite_hit_tests checks sprite-0 hit detection under edge cases including X=255, rendering disabled, and left-side clipping. vbl_nmi_timing tests exact VBlank and NMI cycle timing plus the PPUSTATUS read suppression quirk. scroll_tests validates loopy register mechanics. sprite_overflow_tests verifies the hardware overflow detection bug. APU tests cover channel behavior, frame sequencer timing in both modes, and DMC DMA stall cycles. MMC3-specific tests validate scanline counter A12 detection. OxideNES prioritizes passing tests that affect commercial game compatibility over obscure edge-case-only tests.
