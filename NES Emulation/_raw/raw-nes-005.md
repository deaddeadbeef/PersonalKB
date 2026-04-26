---
tags: [raw, nes-emulation, mapper]
source: "OxideNES mapper.rs + NESdev mapper docs"
---

# Raw NES 005 — Mapper System and Bank Switching

The NES mapper system in OxideNES is implemented in `mapper.rs` (~3,213 lines — the largest source file). The mapper sits between the bus and the cartridge ROM, translating CPU/PPU addresses to physical ROM/RAM offsets. OxideNES supports 20 mappers covering the vast majority of the NES library.

## Why Mappers Exist

The NES CPU can only address 32 KB of PRG ROM ($8000-$FFFF) and the PPU can only address 8 KB of CHR ROM ($0000-$1FFF) directly. Games larger than these limits use mappers — custom hardware on the cartridge PCB that dynamically remaps (banks) different sections of the full ROM into the CPU/PPU address windows. This is called bank switching.

## Mapper Interface

OxideNES defines a `Mapper` trait with methods: `cpu_read(addr)`, `cpu_write(addr, val)`, `ppu_read(addr)`, `ppu_write(addr, val)`, `mirror_mode()`, and optional `irq_tick()`. Each mapper implements this trait. The `Cartridge` struct holds the mapper instance and delegates all ROM/RAM access through it.

## NROM (Mapper 0)

The simplest mapper — no bank switching. PRG ROM is either 16 KB (mirrored at $8000 and $C000) or 32 KB. CHR ROM is a fixed 8 KB. Used by games like Super Mario Bros., Donkey Kong, and Ice Climber.

## MMC1 (Mapper 1)

A serial-load shift register mapper. Writes to $8000-$FFFF load bits one at a time into a 5-bit shift register (5 writes to load a full value). Registers control: mirroring mode, PRG bank mode (32 KB or 16 KB switching), CHR bank mode (8 KB or 4 KB switching), PRG bank select, and CHR bank select. Can support up to 512 KB PRG and 128 KB CHR. Used by Legend of Zelda, Metroid, Mega Man 2.

## UxROM (Mapper 2)

Simple switchable PRG with fixed last bank. Writing to $8000-$FFFF selects which 16 KB PRG bank appears at $8000; the last 16 KB bank is always at $C000. CHR RAM only (8 KB). Used by Mega Man, Castlevania, Contra.

## MMC3 (Mapper 4)

The most complex common mapper. Features: 8 bankable registers for fine-grained PRG/CHR switching, scanline counter for IRQ (used for split-screen effects and raster tricks), and PRG RAM protection bits. The scanline counter decrements each time the PPU fetches from the background pattern table address transitions (A12 rising edge). When it hits zero, an IRQ fires. OxideNES tracks A12 transitions in the PPU to accurately clock this counter. Used by Super Mario Bros. 3, Kirby's Adventure, many others.

## Advanced Mappers

OxideNES also implements: MMC5 (Mapper 5) with its expansion audio and ExRAM, MMC2/MMC4 (Mappers 9/10) with latch-triggered CHR switching for Punch-Out!!, VRC6 (Mapper 24/26) and VRC7 (Mapper 85) with Konami's expansion audio chips, Sunsoft FME-7 (Mapper 69), and several simpler mappers (3, 7, 11, 34, 66, 71, 79, 206). Each mapper is implemented as a separate struct implementing the Mapper trait.

## Save RAM

Mappers that support battery-backed RAM (e.g., MMC1, MMC3) expose an 8 KB window at $6000-$7FFF. OxideNES persists save RAM to disk in the config directory, loading it when the ROM is loaded and saving on emulator exit. This provides persistent game saves for games like Zelda and Final Fantasy.
