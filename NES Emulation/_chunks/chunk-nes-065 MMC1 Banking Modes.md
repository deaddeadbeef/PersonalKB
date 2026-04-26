---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-026]]"
up: "[[Common Mappers]]"
---

# Chunk NES 065 — MMC1 Banking Modes

MMC1 supports multiple PRG and CHR banking modes controlled by its Control register. PRG modes 0 and 1 switch a full 32 KB bank at -. Mode 2 fixes the first bank at  and switches the bank at . Mode 3 (default, most common) switches  while fixing the last bank at  — keeping interrupt handlers at a stable address. CHR mode 0 switches a single 8 KB bank; mode 1 independently switches two 4 KB banks. This flexibility supports up to 512 KB PRG and 128 KB CHR. Games include Legend of Zelda, Metroid, and Mega Man 2.
