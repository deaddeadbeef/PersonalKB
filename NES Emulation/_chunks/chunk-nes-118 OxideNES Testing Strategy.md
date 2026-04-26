---
tags: [chunk, nes-emulation, testing]
source: "[[raw-nes-028]]"
up: "[[Emulator Architecture Overview]]"
---

# Chunk NES 118 — OxideNES Testing Strategy

OxideNES validates accuracy through multiple layers: automated regression runs nestest.nes comparing CPU execution logs against golden references on every build. PPU test ROMs produce specific screen patterns compared against reference screenshots. APU tests verify channel behavior and frame sequencer timing. A compatibility list of approximately 100 reference games is periodically tested for regressions. For timing-critical tests, the emulator logs PPU cycle and scanline positions alongside CPU execution for manual verification. The development philosophy prioritizes commercial game compatibility over passing every obscure edge-case test that no released game depends on.
