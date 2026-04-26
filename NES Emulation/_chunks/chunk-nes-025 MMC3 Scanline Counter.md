---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Advanced Mappers]]"
---

# Chunk NES 025 — MMC3 Scanline Counter

MMC3 (Mapper 4) features a hardware scanline counter for IRQ generation, enabling split-screen effects. It monitors PPU address line A12: when A12 transitions from low to high (during background-to-sprite pattern table switches), the counter decrements. When it reaches zero, an IRQ fires. The CPU IRQ handler then changes scroll registers or bank settings mid-frame. OxideNES tracks A12 transitions in the PPU each cycle, feeding them to the mapper. Accurate A12 detection is critical — Super Mario Bros. 3 and Kirby's Adventure depend on exact IRQ timing for their status bar effects.
