---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-022]]"
up: "[[Advanced Mappers]]"
---

# Chunk NES 055 — MMC3 Bank Register Architecture

MMC3 uses a bank select register () and bank data register () to control 8 internal bank registers (R0-R7). R0-R1 select 2 KB CHR banks, R2-R5 select 1 KB CHR banks, and R6-R7 select 8 KB PRG banks. Bit 6 of the select register swaps PRG layout: mode 0 places R6 at  with the second-to-last bank fixed at ; mode 1 reverses this. Bit 7 swaps CHR layout, controlling whether 2 KB banks cover background or sprite pattern tables. This flexibility lets games optimize bank arrangement for their specific graphics and code organization needs.
