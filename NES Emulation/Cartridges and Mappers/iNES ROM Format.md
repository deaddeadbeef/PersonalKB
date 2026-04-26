---
tags: [nes, wiki]
up: "[[Cartridges and Mappers Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# iNES ROM Format

> **The 16-byte header format that describes a ROM's hardware configuration — the first thing an emulator parses when loading any game.**

## 🎯 Intuition
**The Core Idea:** A 16-byte header prepended to raw ROM data describes the cartridge's hardware configuration — mapper, ROM sizes, mirroring, and battery.
**Analogy:** Like a shipping label telling the emulator what's inside the package — which mapper to use, how much PRG and CHR to expect, and how memory is arranged.
**Why It Matters:** Parsing the iNES header is the first step in loading any game. Dirty (corrupted) headers are one of the most common sources of emulation bugs, making robust detection essential.

---

## ⚙️ Core Mechanics
### How It Works
Every iNES ROM file begins with a 16-byte header followed by optional trainer data (512 bytes), PRG ROM data, and CHR ROM data. The header encodes the mapper number, ROM sizes, mirroring mode, and other hardware flags. The emulator reads this header to determine how to configure the virtual cartridge.

### Key Specifications

| Offset | Size | Content |
|--------|------|---------|
| 0–3 | 4 | Magic: 'N', 'E', 'S', 0x1A |
| 4 | 1 | PRG ROM size in 16 KB units |
| 5 | 1 | CHR ROM size in 8 KB units (0 = CHR RAM) |
| 6 | 1 | Flags 6: mapper low, mirroring, battery, trainer |
| 7 | 1 | Flags 7: mapper high, NES 2.0 indicator |
| 8–15 | 8 | Extended flags (NES 2.0) or padding |

### Key Flag Bits (Byte 6)

| Bit | Meaning |
|-----|---------|
| 0 | Mirroring: 0=horizontal, 1=vertical |
| 1 | Battery-backed SRAM at 0x6000–0x7FFF |
| 2 | 512-byte trainer at 0x7000–0x71FF |
| 3 | Four-screen VRAM (ignore bit 0) |
| 4–7 | Mapper number low nibble |

### Key Facts
- The magic bytes 'N', 'E', 'S', 0x1A must be present — reject files without them
- CHR ROM size of 0 means the cartridge uses CHR RAM (writable pattern tables)
- The mapper number is split across two bytes: low nibble in byte 6 (bits 4–7), high nibble in byte 7 (bits 4–7)
- Byte 7 bits 2–3 = 0b10 identifies the NES 2.0 extended format

---

## 🔬 Deep Dive
### Dirty Headers
Many early ROM dumps have corrupted headers (e.g., "DiskDude!" watermark in bytes 7–15). These corrupted bytes can produce incorrect mapper numbers when the high nibble from byte 7 is used. OxideNES detects dirty headers and falls back to using only the lower nibble of the mapper number. The ROM database provides verified corrections.

### NES 2.0 Extensions
The NES 2.0 extended format (identifiable by bits 2–3 of byte 7 = 0b10) adds:
- Submapper number for disambiguating mapper variants
- Extended PRG/CHR ROM sizes beyond the original 8-bit limits
- Extended mapper number (12-bit, supporting mappers 0–4095)
- Explicit SRAM/CHR RAM size specification

### Mapper Number Extraction
```
mapper_low  = (flags6 >> 4) & 0x0F   // byte 6, bits 4-7
mapper_high = (flags7 >> 4) & 0x0F   // byte 7, bits 4-7 (if not dirty)
mapper_id   = mapper_high << 4 | mapper_low
```
For NES 2.0, byte 8 bits 0–3 provide an additional 4 bits for the mapper number (total 12 bits).

### Reference Implementations
cartridge.rs `new()` validates magic bytes, detects dirty headers, extracts mapper ID and ROM sizes, then instantiates the appropriate mapper. `new_with_romdb()` cross-references CRC32 hash against the ROM database for header corrections.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What are the 4 magic bytes at the start of every iNES file?
2. How do you determine the PRG ROM size in bytes from the header?
3. What does CHR ROM size = 0 mean for the cartridge?

### Core Problems
1. **Header Parser:** Write a function that reads 16 bytes and extracts: mapper ID, PRG ROM size (bytes), CHR ROM size (bytes), mirroring mode, battery flag, and trainer flag. Validate the magic bytes and return an error for invalid files.
2. **Dirty Header Detection:** Implement a heuristic to detect dirty headers. If bytes 8–15 contain non-zero ASCII characters (like "DiskDude!"), flag the header as dirty and use only the lower nibble for the mapper number.

### Challenge
**Full ROM Loader:** Implement a complete iNES ROM loader that parses the header, handles optional trainer data, splits the file into PRG and CHR ROM segments, detects dirty headers, and supports both iNES 1.0 and NES 2.0 formats. Verify with test ROMs that have known dirty headers.

---

*See also:* [[Common Mappers]], [[Bank Switching Explained]], [[Cartridges and Mappers Overview]]

## References
→ [[Sources Index]]
