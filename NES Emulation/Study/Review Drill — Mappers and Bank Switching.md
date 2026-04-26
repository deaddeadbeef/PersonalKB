---
tags: [study, nes-emulation, mapper]
up: "[[NES Emulation Study Index]]"
---

# Review Drill — Mappers and Bank Switching

Test your understanding of NES cartridge mapper hardware.

## Questions

**Q1:** Why do NES games need mappers?
> The CPU can only address 32 KB PRG ROM and the PPU 8 KB CHR. Games exceeding these limits use mapper hardware on the cartridge to dynamically remap (bank-switch) different ROM sections into the address windows.

**Q2:** Describe NROM (Mapper 0).
> No bank switching. 16 KB or 32 KB PRG ROM (16 KB is mirrored), 8 KB CHR ROM. The simplest mapper — used by Super Mario Bros., Donkey Kong.

**Q3:** How does MMC1's serial register interface work?
> Five consecutive writes to - load one bit each into a 5-bit shift register. On the fifth write, the value transfers to an internal register selected by address bits 14-13. Writing with bit 7 set resets the shift register.

**Q4:** Explain MMC3's scanline counter mechanism.
> Monitors PPU address line A12. On each rising edge (background-to-sprite pattern table switch), the counter decrements or reloads. When it hits zero with IRQs enabled, an IRQ fires. Used for split-screen status bars.

**Q5:** What is the difference between CHR ROM and CHR RAM?
> CHR ROM: read-only tiles burned into the cartridge, bank-switched by the mapper. CHR RAM: 8 KB writable memory populated by CPU through PPU registers, enabling dynamically generated tiles. iNES header byte 5 = 0 indicates CHR RAM.

**Q6:** How does MMC3 detect scanlines via A12?
> PPU address bit 12 goes high when fetching from pattern table - and low for -. During rendering, the PPU alternates between background and sprite fetches from different tables, causing A12 transitions that the mapper counts.

**Q7:** What makes MMC5 the most complex NES mapper?
> Per-tile attribute mode (bypassing 2x2 palette restriction), 1 KB ExRAM, advanced 8 KB PRG banking up to 1 MB, expansion audio (2 pulse + PCM), and 8x16 sprite mode control.

**Q8:** How does OxideNES persist battery-backed save RAM?
> Saves to ~/.nes-emulator/saves/<rom-crc32>.sav on emulator exit, loads on ROM open. The 8 KB SRAM at - is also included in save state snapshots.
