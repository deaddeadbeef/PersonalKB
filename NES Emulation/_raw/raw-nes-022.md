---
tags: [raw, nes-emulation, mmc3]
source: "OxideNES mapper.rs MMC3 implementation"
---

# Raw NES 022 — MMC3 Mapper Deep Dive

MMC3 (Mapper 4) is the most popular complex mapper on the NES, used by over 250 games including Super Mario Bros. 3, Kirby's Adventure, and Mega Man 3-6. OxideNES's implementation is one of the most detailed in mapper.rs.

## Register Architecture

MMC3 uses two registers at $8000-$9FFF for bank select:
- **$8000 (Bank Select):** Bits 0-2 specify which of 8 bank registers to update. Bit 6 swaps PRG bank layout. Bit 7 swaps CHR bank layout.
- **$8001 (Bank Data):** The value written here goes into the bank register specified by $8000 bits 0-2.

The 8 bank registers (R0-R7) control:
- R0-R1: 2 KB CHR banks (at $0000/$0800 or $1000/$1800 depending on CHR mode)
- R2-R5: 1 KB CHR banks (filling remaining CHR space)
- R6-R7: 8 KB PRG banks (at $8000/$A000 or $C000/$A000 depending on PRG mode)

## PRG Banking Modes

**Mode 0 (bit 6 = 0):** R6 at $8000, R7 at $A000, second-to-last bank fixed at $C000, last bank fixed at $E000.
**Mode 1 (bit 6 = 1):** Second-to-last bank fixed at $8000, R7 at $A000, R6 at $C000, last bank fixed at $E000.

This swappable layout lets games choose whether the fixed bank (containing interrupt handlers) is at the top or bottom of the address range.

## CHR Banking Modes

**Mode 0 (bit 7 = 0):** R0-R1 (2 KB each) at $0000-$0FFF, R2-R5 (1 KB each) at $1000-$1FFF.
**Mode 1 (bit 7 = 1):** R2-R5 (1 KB each) at $0000-$0FFF, R0-R1 (2 KB each) at $1000-$1FFF.

This determines whether the 2 KB banks cover the background pattern table or the sprite pattern table — important for the scanline counter's A12 monitoring.

## Scanline Counter (IRQ)

MMC3's scanline counter is its most complex and critical feature. It monitors PPU address line A12 (bit 12 of the PPU address bus) to detect scanline transitions:

1. **Counter Reload:** Writing any value to $C000 sets the reload value. Writing to $C001 forces a reload on the next rising A12 edge.
2. **Operation:** When A12 transitions from 0 to 1 (rising edge), if the counter is zero OR the reload flag is set, the counter reloads from the value at $C000. Otherwise, the counter decrements.
3. **IRQ firing:** When the counter transitions from 1 to 0 AND IRQs are enabled ($E001), an IRQ is fired.
4. **Enable/Disable:** Writing to $E000 disables IRQ and acknowledges pending IRQ. Writing to $E001 enables IRQ.

## A12 Detection in OxideNES

The scanline counter relies on detecting A12 rising edges accurately. OxideNES monitors the PPU address bus and detects when bit 12 goes from low to high. A minimum number of consecutive low cycles must occur before a rising edge is recognized (to filter glitches from sprite fetches). This is implemented in the mapper's `ppu_tick()` method, called every PPU cycle.

## Mirroring Control

MMC3 supports dynamic mirroring: writing to $A000 sets horizontal (bit 0 = 0) or vertical (bit 0 = 1) mirroring. Writing to $A001 enables/disables PRG RAM at $6000-$7FFF and optionally write-protects it. This allows games to change scrolling direction dynamically.

## Common MMC3 Uses

- **Split-screen status bars:** Set the IRQ counter to fire at the scanline where the status bar ends, then change scroll registers in the IRQ handler.
- **Animated backgrounds:** Swap CHR banks each frame to animate background tiles without CPU involvement.
- **Large worlds:** Use PRG banking to address up to 512 KB of game code and data.
