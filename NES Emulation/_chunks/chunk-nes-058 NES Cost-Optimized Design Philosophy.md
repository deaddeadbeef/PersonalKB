---
tags: [chunk, nes-emulation, history]
source: "[[raw-nes-023]]"
up: "[[NES Console Architecture]]"
---

# Chunk NES 058 — NES Cost-Optimized Design Philosophy

The NES was designed for maximum capability per dollar. The Ricoh 2A03 combined a 6502 CPU core with PSG audio on one chip, eliminating a separate sound chip. The dedicated PPU (Ricoh 2C02) handled scrolling, sprites, and backgrounds in hardware, freeing the CPU from pixel work. Only 2 KB RAM and 2 KB VRAM kept onboard costs minimal. The revolutionary cartridge bus exposed raw address and data lines, allowing mapper hardware to extend capability without console revisions. This meant a 1983 console could run increasingly sophisticated games throughout its 12-year commercial lifespan.
