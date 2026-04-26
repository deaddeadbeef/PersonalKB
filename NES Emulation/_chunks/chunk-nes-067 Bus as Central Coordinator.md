---
tags: [chunk, nes-emulation, module]
source: "[[raw-nes-027]]"
up: "[[OxideNES Module Architecture]]"
---

# Chunk NES 067 — Bus as Central Coordinator

The Bus struct owns CPU, PPU, APU, and Cartridge (with mapper), serving as central interconnect. All CPU memory access routes through bus.read(addr) and bus.write(addr, val), which decode addresses and dispatch to the appropriate subsystem. PPU VRAM access goes through the cartridge mapper for nametable mirroring and CHR banking. The bus clock() method maintains the 3:1 PPU-to-CPU timing ratio — three ppu.tick() calls per one cpu.tick(), plus apu.tick() at CPU rate. This architecture isolates each subsystem behind well-defined interfaces while maintaining the precise timing relationships required for accurate emulation.
