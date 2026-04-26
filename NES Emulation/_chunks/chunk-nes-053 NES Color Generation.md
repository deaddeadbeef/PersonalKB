---
tags: [chunk, nes-emulation, palette]
source: "[[raw-nes-021]]"
up: "[[PPU Rendering Pipeline]]"
---

# Chunk NES 053 — NES Color Generation

The NES PPU generates NTSC composite video rather than RGB. Each of 64 palette entries encodes a hue (12 possible phase angles at 30-degree increments) and brightness level (4 levels). The TV decoder converts this analog signal to visible color. Since modern displays use RGB, emulators must approximate — no single correct NES palette exists because real hardware looked different on every TV. Common approaches include empirically measured palettes (FCEUX, Nestopia) and mathematically generated NTSC-model palettes. PPUMASK emphasis bits 5-7 tint the entire screen, creating up to 512 effective color combinations.
