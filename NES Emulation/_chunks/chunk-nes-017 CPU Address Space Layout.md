---
tags: [chunk, nes-emulation, memory]
source: "[[raw-nes-004]]"
up: "[[CPU Memory Map]]"
---

# Chunk NES 017 — CPU Address Space Layout

The NES CPU addresses 64 KB: - is 2 KB internal RAM mirrored through . - holds PPU registers mirrored through . - maps APU registers.  is OAM DMA.  is APU status. - are controller ports (also APU frame counter on  write). - is normally unused. - is cartridge space controlled by the mapper, containing PRG ROM, PRG RAM, and expansion hardware. The bus decodes each address and routes reads/writes to the appropriate subsystem.
