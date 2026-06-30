---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: plausible
---
# Cartridges and Mappers Overview

NES cartridges contain ROM chips and optional mapper hardware that extends the console's capabilities far beyond its base specifications. Mappers perform bank switching, allowing games to access much more memory than the CPU or PPU can directly address.

## Pages

- [[iNES ROM Format]] — The standard ROM file format for NES emulation
- [[Bank Switching Explained]] — How mappers extend memory beyond hardware limits
- [[Common Mappers]] — NROM, MMC1, UxROM, CNROM, MMC3 — the big five
- [[Advanced Mappers]] — MMC5, VRC6, Namco 163, and expansion audio
- [[Expansion Audio]] — Additional sound channels on cartridge hardware

## Key Facts

- **20 mappers** supported by OxideNES (covering ~95% of the NES library)
- **Bank switching** allows up to 512 KB PRG + 256 KB CHR (or more)
- **MMC3 (Mapper 4)** is the most common advanced mapper
- **Expansion audio** on VRC6, Namco 163, FME7, and VRC7 cartridges

## OxideNES Implementation

cartridge.rs (171 lines) handles ROM parsing with iNES header validation. mapper.rs (3,213 lines — the second largest file) implements all 20 mappers using enum dispatch for zero-cost abstraction.

## References

→ [[Sources Index]]
