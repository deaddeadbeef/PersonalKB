---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
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

## How To Read This Chapter

Read this chapter for cartridge hardware and bank switching. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: PRG/CHR mapping, nametable mirroring, mapper IRQs, battery-backed RAM, and board-specific edge cases. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
