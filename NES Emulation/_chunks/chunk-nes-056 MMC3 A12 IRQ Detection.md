---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-022]]"
up: "[[Advanced Mappers]]"
---

# Chunk NES 056 — MMC3 A12 IRQ Detection

MMC3's scanline counter monitors PPU address line A12 for rising edges to count scanlines. When A12 transitions low-to-high (during pattern table address switches between background and sprite fetches), the counter decrements or reloads. A minimum low period filters glitches from sprite fetch patterns. When the counter transitions from 1 to 0 and IRQs are enabled (), an IRQ fires. Writing to  sets the reload value;  forces a reload;  disables and acknowledges IRQ;  enables IRQ. OxideNES calls the mapper's ppu_tick() every PPU cycle to track A12 transitions accurately.
