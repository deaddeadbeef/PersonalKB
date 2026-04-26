---
tags: [chunk, nes-emulation, ines]
source: "[[raw-nes-019]]"
up: "[[iNES ROM Format]]"
---

# Chunk NES 075 — iNES Header Format

The iNES header is 16 bytes: bytes 0-3 are the magic number     (NES plus MS-DOS EOF). Byte 4 gives PRG ROM size in 16 KB units. Byte 5 gives CHR ROM size in 8 KB units (0 means CHR RAM). Flags 6 encodes the mapper low nibble, mirroring type, battery-backed RAM flag, and trainer presence. Flags 7 has the mapper high nibble, NES 2.0 identifier, and VS/PlayChoice flags. The mapper number is formed by combining the upper nibbles of flags 6 and 7. NES 2.0 extends the format with submapper numbers, larger ROM sizes, and timing mode selection.
