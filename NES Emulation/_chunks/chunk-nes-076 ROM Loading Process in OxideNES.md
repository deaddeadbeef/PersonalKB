---
tags: [chunk, nes-emulation, ines]
source: "[[raw-nes-019]]"
up: "[[iNES ROM Format]]"
---

# Chunk NES 076 — ROM Loading Process in OxideNES

OxideNES loads ROMs through a defined sequence: validate the 16-byte header magic number, extract mapper number from flags 6 and 7, determine mirroring mode, skip the 512-byte trainer if present (flags 6 bit 2), read PRG ROM data (header byte 4 times 16384 bytes), read CHR ROM or allocate 8 KB CHR RAM if size is zero, compute CRC32 of the full ROM for save state and netplay verification, instantiate the appropriate mapper struct, and load battery-backed RAM from disk if the battery flag is set. Unsupported mapper numbers fall back to NROM (Mapper 0) with a logged warning.
