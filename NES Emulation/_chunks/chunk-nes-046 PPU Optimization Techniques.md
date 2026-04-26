---
tags: [chunk, nes-emulation, performance]
source: "[[raw-nes-015]]"
up: "[[Performance Optimization in OxideNES]]"
---

# Chunk NES 046 — PPU Optimization Techniques

OxideNES optimizes PPU rendering with dirty tile tracking: only nametable entries changed since the last frame are re-rendered, dramatically reducing work for games with mostly static backgrounds. Sprite evaluation results are cached when OAM has not been written since the previous frame. The PPU's 16-bit background shift registers use native integer shifts rather than bit-by-bit simulation. When both background and sprite rendering are disabled (PPUMASK bits 3-4 clear), the PPU skips all rendering logic, only updating timing and VBlank state. The frame buffer uses cache-friendly sequential RGBA layout for efficient blitting.
