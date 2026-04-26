---
tags: [raw, nes-emulation, mmc1]
source: "OxideNES mapper.rs MMC1 + NESdev"
---

# Raw NES 026 — MMC1 Mapper Deep Dive

MMC1 (Mapper 1) is the second most popular NES mapper after NROM, used by ~400 games including The Legend of Zelda, Metroid, and Mega Man 2. Its unique serial-load interface makes it a fascinating emulation target.

## Serial Register Interface

Unlike most mappers that decode address bits and data bus directly, MMC1 uses a 5-bit serial shift register loaded one bit at a time. To write a 5-bit value:
1. Write bit 0 to any address in - (bit 0 of data byte)
2. Write bit 1 the same way
3. Write bit 2
4. Write bit 3
5. Write bit 4 — on this fifth write, the 5-bit value is transferred to the internal register selected by address bits 13-14

Writing with bit 7 set at any point resets the shift register and sets the PRG mode to fixed-last-bank (mode 3).

## Internal Registers

The four internal registers (selected by address bits 14-13 of the write address):

**Control (-):**
- Bits 0-1: Mirroring (0=single-lower, 1=single-upper, 2=vertical, 3=horizontal)
- Bits 2-3: PRG bank mode (0,1=switch 32KB at ; 2=fix first, switch last; 3=fix last, switch first)
- Bit 4: CHR bank mode (0=switch 8KB; 1=switch two 4KB banks)

**CHR Bank 0 (-):** Selects CHR bank for - (4KB mode) or - (8KB mode)
**CHR Bank 1 (-):** Selects CHR bank for - (4KB mode only)
**PRG Bank (-):** Bits 0-3 select PRG bank. Bit 4 enables/disables PRG RAM at -.

## Banking Behavior

**PRG Mode 0,1 (32 KB):** The 5-bit bank value (ignoring bit 0) selects a 32 KB bank at -. Supports up to 512 KB PRG ROM.
**PRG Mode 2:** First bank (-) fixed to bank 0. Last bank (-) switchable.
**PRG Mode 3:** First bank (-) switchable. Last bank (-) fixed to last bank. This is the default and most common mode.

**CHR Mode 0 (8 KB):** A single bank register selects an 8 KB CHR bank (bit 0 ignored).
**CHR Mode 1 (4 KB):** Two independent bank registers select 4 KB banks.

## OxideNES Implementation Details

The MMC1 struct stores: shift_register (5-bit), write_count (0-4), control register, chr_bank0, chr_bank1, prg_bank, and prg_ram. Each write to - calls write_serial() which: checks bit 7 (reset), shifts in bit 0 of the data byte, increments write_count, and on the fifth write, transfers to the appropriate internal register based on the address.

Key edge case: consecutive writes on consecutive CPU cycles should be ignored (the second write is "eaten" by the shift register logic). OxideNES tracks the last write cycle to implement this behavior, which is important for a small number of games that rely on it.

## Battery-Backed RAM

Many MMC1 games (Zelda, Final Fantasy, Metroid) use battery-backed SRAM at - for game saves. OxideNES persists this to ~/.nes-emulator/saves/<crc32>.sav, loading on ROM open and saving on emulator exit. The PRG bank register bit 4 can disable this RAM, though most games leave it enabled.
