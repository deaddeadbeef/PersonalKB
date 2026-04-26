---
tags: [raw, nes-emulation, ines]
source: "NESdev iNES format spec + OxideNES main.rs"
---

# Raw NES 019 — iNES ROM Format

The iNES file format (.nes extension) is the de facto standard for distributing NES ROM images. OxideNES parses this format to load games, extracting the PRG ROM, CHR ROM/RAM, mapper configuration, and mirroring mode.

## Header Format (16 bytes)

| Offset | Size | Content |
|--------|------|---------|
| 0-3 | 4 | Magic number: $4E    ("NES" + MS-DOS EOF) |
| 4 | 1 | PRG ROM size in 16 KB units |
| 5 | 1 | CHR ROM size in 8 KB units (0 = uses CHR RAM) |
| 6 | 1 | Flags 6: Mapper low nibble, mirroring, battery, trainer |
| 7 | 1 | Flags 7: Mapper high nibble, NES 2.0 identifier, VS/PlayChoice |
| 8 | 1 | PRG RAM size in 8 KB units (0 infers 8 KB) |
| 9 | 1 | Flags 9: TV system (NTSC/PAL) |
| 10 | 1 | Flags 10: TV system, PRG RAM presence (unofficial) |
| 11-15 | 5 | Padding (should be zero) |

## Flags 6 Detail

- Bit 0: Mirroring (0=horizontal, 1=vertical)
- Bit 1: Battery-backed PRG RAM at -
- Bit 2: 512-byte trainer at - (precedes PRG data)
- Bit 3: Four-screen VRAM (ignore bit 0 mirroring)
- Bits 4-7: Lower nibble of mapper number

## Flags 7 Detail

- Bits 0-1: VS Unisystem / PlayChoice-10
- Bits 2-3: If equal to 2, flags 8-15 are NES 2.0 format
- Bits 4-7: Upper nibble of mapper number

## ROM Data Layout

After the 16-byte header (and optional 512-byte trainer):
1. PRG ROM: header[4] × 16384 bytes
2. CHR ROM: header[5] × 8192 bytes (omitted if header[5] = 0, indicating CHR RAM)

## NES 2.0 Extensions

NES 2.0 extends the header for larger ROMs and more mapper information:
- Extended mapper number (12 bits instead of 8)
- Submapper number (4 bits) for variants within a mapper
- Extended PRG/CHR ROM sizes (using exponent+multiplier format for sizes > 4 MB)
- PRG/CHR RAM and non-volatile RAM sizes
- CPU/PPU timing mode (NTSC, PAL, Multi-region, Dendy)
- Miscellaneous ROM metadata

OxideNES detects NES 2.0 via bits 2-3 of flags 7 and parses extended fields when present, falling back to iNES 1.0 interpretation otherwise.

## OxideNES ROM Loading

The ROM loading process in OxideNES:
1. Read and validate the 16-byte header (check magic number)
2. Extract mapper number from flags 6 and 7
3. Determine mirroring mode from flags 6
4. Skip trainer if present (bit 2 of flags 6)
5. Read PRG ROM into a Vec<u8>
6. Read CHR ROM (or allocate 8 KB CHR RAM if size = 0)
7. Compute CRC32 of the full ROM for save state/netplay verification
8. Instantiate the appropriate mapper struct based on mapper number
9. Load battery-backed RAM from disk if the battery flag is set

If the mapper number is not supported, OxideNES logs an error and falls back to NROM (Mapper 0), which may or may not work depending on the game.
