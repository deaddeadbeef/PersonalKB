---
tags: [chunk, nes-emulation, ppu]
source: "[[raw-nes-002]]"
up: "[[PPU — Picture Processing Unit Overview]]"
---

# Chunk NES 082 — PPU Frame Structure Overview

The NES PPU renders 256x240 pixel frames at approximately 60.1 FPS for NTSC. Each frame consists of 262 scanlines with 341 PPU cycles per scanline. The PPU operates autonomously — once configured by the CPU through register writes, it fetches tile and sprite data from VRAM and pattern tables, composites the image through a priority multiplexer, and signals the CPU via NMI when vertical blank begins. This hardware-driven rendering pipeline frees the CPU to focus on game logic during the approximately 20 VBlank scanlines available each frame.
