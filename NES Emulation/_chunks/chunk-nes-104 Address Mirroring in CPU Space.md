---
tags: [chunk, nes-emulation, memory]
source: "[[raw-nes-004]]"
up: "[[CPU Memory Map]]"
---

# Chunk NES 104 — Address Mirroring in CPU Space

The NES CPU address space features extensive mirroring to simplify hardware design. The 2 KB internal RAM (-) mirrors every 2 KB through  — addresses are decoded with addr AND . The 8 PPU registers (-) mirror every 8 bytes through  — decoded with addr AND . This mirroring means writing to  is identical to writing to , and reading  is identical to reading . OxideNES applies these masks in the bus read/write methods before dispatching to subsystems. Games occasionally use mirrored addresses intentionally.
