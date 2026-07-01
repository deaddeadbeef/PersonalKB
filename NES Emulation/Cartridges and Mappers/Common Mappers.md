---
tags: [nes, wiki]
up: "[[Cartridges and Mappers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Common Mappers

> **Five mapper types that cover ~85% of all licensed NES games, from the trivial NROM to the versatile MMC3.**

## 🎯 Intuition
**The Core Idea:** Five mapper types cover ~85% of all NES games — mastering these five gets you from "hello world" to running most of the NES library.
**Analogy:** Think of transmissions — NROM is a fixed-gear bike, UxROM/CNROM are manual transmissions, MMC1 is an automatic, and MMC3 is a sport automatic with paddle shifters.
**Why It Matters:** Implement these five mappers and you can run most NES games. They're ordered from trivial (NROM) to complex (MMC3), making them ideal for incremental emulator development.

---

## ⚙️ Core Mechanics
### How It Works
Each mapper intercepts CPU reads/writes to the cartridge address space (0x8000–0xFFFF for PRG, 0x0000–0x1FFF for CHR on the PPU bus). Depending on the mapper, writes configure internal bank registers that control which ROM segments appear in the CPU/PPU address windows.

### Key Specifications

| Mapper | Name | PRG | CHR | Bank Switching | Notable Games |
|--------|------|-----|-----|---------------|---------------|
| 0 | NROM | 16 or 32 KB (no switching) | 8 KB (no switching) | None | Super Mario Bros., Donkey Kong, Ice Climber |
| 1 | MMC1 | Up to 256 KB / 16 KB banks | Up to 128 KB / 4 KB banks | Serial shift register (5 writes) | The Legend of Zelda, Metroid, Mega Man 2 |
| 2 | UxROM | Up to 256 KB / 16 KB switchable + 16 KB fixed | 8 KB CHR RAM | Single write selects PRG bank | Castlevania, Contra, Duck Tales |
| 3 | CNROM | 16 or 32 KB (no switching) | Up to 32 KB / 8 KB banks | Single write selects CHR bank | Gradius, Solomon's Key |
| 4 | MMC3 | Up to 512 KB / 8 KB banks | Up to 256 KB / 1 KB+2 KB banks | Flexible bank register system | Super Mario Bros. 3, Kirby's Adventure, Mega Man 3–6 |

### Key Facts
- NROM is the simplest possible mapper: ROM is directly wired to CPU/PPU buses with no switching logic
- MMC1 uses a serial shift register — you write 5 bits one at a time to configure banks, mirroring, and SRAM
- UxROM has a fixed last 16 KB bank and a single switchable 16 KB bank; CHR is RAM, not ROM
- CNROM switches CHR banks while keeping PRG fixed — the opposite of UxROM
- MMC3 is the most common advanced mapper (~24% of licensed NES games), featuring a scanline counter IRQ and flexible bank switching
- MMC1 supports switchable mirroring and SRAM battery saves

---

## 🔬 Deep Dive
### Mapper 0 — NROM
The simplest possible mapper. ROM is directly wired to CPU/PPU buses. 16 KB PRG ROMs are mirrored at both 0x8000 and 0xC000. No writes are meaningful.

### Mapper 1 — MMC1
Uses a serial shift register: the game writes 5 bits one at a time (bit 0 of each write, shifting in from the top). After 5 writes, the accumulated value configures one of four internal registers depending on the target address range:
- **0x8000–0x9FFF:** Control (mirroring, PRG mode, CHR mode)
- **0xA000–0xBFFF:** CHR bank 0
- **0xC000–0xDFFF:** CHR bank 1
- **0xE000–0xFFFF:** PRG bank + SRAM enable
Writing with bit 7 set resets the shift register.

### Mapper 2 — UxROM
Single write to anywhere in 0x8000–0xFFFF selects the 16 KB PRG bank mapped to 0x8000–0xBFFF. The last 16 KB bank is always fixed at 0xC000–0xFFFF. Uses CHR RAM (not ROM), so the PPU pattern tables are writable.

### Mapper 3 — CNROM
Single write to 0x8000–0xFFFF selects the 8 KB CHR bank. PRG ROM is not switched — always either 16 KB (mirrored) or 32 KB direct.

### Mapper 4 — MMC3
The most complex of the common mappers. Features:
- 8 bank registers configurable via writes to 0x8000/0x8001
- Two PRG banking modes (0xC000 fixed vs. 0x8000 fixed)
- 1 KB and 2 KB CHR bank granularity with two arrangement modes
- Scanline counter IRQ: counts PPU A12 rising edges, fires IRQ at configurable scanline — critical for scroll-split effects in games like Super Mario Bros. 3

### Reference Implementations
Each mapper is a separate struct in mapper.rs implementing the Mapper trait. The MapperEnum uses Rust enum dispatch (not dynamic dispatch) for zero-cost abstraction.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Which mapper requires no bank switching logic at all, and how does it handle 16 KB PRG ROMs?
2. How many writes does it take to configure an MMC1 register, and what happens if bit 7 is set?
3. What percentage of licensed NES games does MMC3 cover?

### Core Problems
1. **Implement NROM:** Write a complete Mapper 0 implementation. Handle both 16 KB (mirrored) and 32 KB PRG ROM configurations. Verify that reads from 0x8000 and 0xC000 return the same data for a 16 KB ROM.
2. **MMC1 Shift Register:** Implement the MMC1 serial shift register. Write 5 consecutive values (0, 1, 0, 1, 1) and verify the assembled register value. Then verify that writing with bit 7 set resets the register.

### Challenge
**MMC3 Scanline Counter:** Implement the MMC3 IRQ scanline counter. The counter decrements on each PPU A12 rising edge (approximately once per scanline during rendering). When it reaches zero, reload from the latch and fire an IRQ. Test with a scenario that sets the counter to 40 and verifies the IRQ fires on scanline 40.

---

*See also:* [[Advanced Mappers]], [[Bank Switching Explained]], [[iNES ROM Format]], [[Cartridges and Mappers Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
