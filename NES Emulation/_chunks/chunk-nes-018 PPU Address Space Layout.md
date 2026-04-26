---
tags: [chunk, nes-emulation, memory]
source: "[[raw-nes-004]]"
up: "[[PPU Memory Map]]"
---

# Chunk NES 018 — PPU Address Space Layout

The PPU has its own 16 KB address space accessed via PPUADDR/PPUDATA. - holds two 4 KB pattern tables (tile graphics), usually mapped to CHR ROM or CHR RAM on the cartridge. - contains four logical nametables (tile maps) with only 2 KB physical VRAM — mirroring fills the gap. - mirrors -. - holds 32 bytes of palette RAM: 16 background colors and 16 sprite colors. - mirrors the palette. The mapper controls pattern table banking and nametable mirroring configuration.
