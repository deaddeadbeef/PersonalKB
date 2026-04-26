---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[PPU Rendering Pipeline]]"
---

# Chunk NES 010 — Frame Buffer and Display Output

OxideNES renders each pixel via a render_pixel() method called every PPU cycle during visible scanlines. Background and sprite data are composed using a priority multiplexer that resolves layering based on sprite priority bits and transparency. The final pixel color is looked up from palette RAM using the NES master palette. The frame buffer is a flat RGBA array of 256x240x4 bytes passed to the minifb display backend. Nametable mirroring (horizontal, vertical, four-screen, single-screen) is configured by the cartridge mapper through a mirror_nametable_addr() method.
