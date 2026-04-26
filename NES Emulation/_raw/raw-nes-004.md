---
tags: [raw, nes-emulation, memory, bus]
source: "OxideNES bus.rs + NESdev memory map"
---

# Raw NES 004 — Bus Architecture and Memory Map

The NES bus system in OxideNES is implemented in `bus.rs` (~351 lines). The bus serves as the central interconnect between CPU, PPU, APU, cartridge, and controller I/O. All CPU memory accesses go through the bus, which decodes addresses and routes reads/writes to the appropriate subsystem.

## CPU Address Space ($0000-$FFFF)

The NES CPU sees a 64 KB address space divided into regions:
- **$0000-$07FF:** 2 KB internal RAM, mirrored every 2 KB through $1FFF (address AND 0x07FF)
- **$2000-$2007:** PPU registers, mirrored every 8 bytes through $3FFF (address AND 0x2007)
- **$4000-$4013:** APU registers (pulse, triangle, noise, DMC)
- **$4014:** OAM DMA register — writing a byte N copies 256 bytes from CPU page $NN00-$NNFF to OAM, stalling CPU 513-514 cycles
- **$4015:** APU status (read: channel status, write: channel enable)
- **$4016-$4017:** Controller ports (read: shift register, write: strobe) + APU frame counter ($4017 write)
- **$4018-$401F:** Normally unused (test mode registers)
- **$4020-$FFFF:** Cartridge space (mapper-controlled PRG ROM/RAM)

## PPU Address Space ($0000-$3FFF)

The PPU has its own 16 KB address space accessed via PPUADDR/PPUDATA:
- **$0000-$1FFF:** Pattern tables (8 KB, usually CHR ROM/RAM on cartridge)
- **$2000-$2FFF:** Nametables (4 logical, 2 physical KB of VRAM with mirroring)
- **$3000-$3EFF:** Mirror of $2000-$2EFF
- **$3F00-$3F1F:** Palette RAM (32 bytes: 16 background + 16 sprite colors)
- **$3F20-$3FFF:** Mirror of palette RAM

## Mirroring

Nametable mirroring is determined by the cartridge/mapper: horizontal mirroring (vertical scrolling games), vertical mirroring (horizontal scrolling games), single-screen (mapper selects which), or four-screen (cartridge provides extra VRAM). OxideNES configures mirroring via the Cartridge struct which provides a `mirror_nametable_addr()` method called by the PPU for every nametable access.

## OAM DMA Implementation

OAM DMA ($4014) is a critical performance feature. Writing to this register triggers a 256-byte bulk copy from CPU address space to PPU OAM. In OxideNES, the bus handles this by: (1) reading the page byte, (2) performing 256 consecutive reads from $XX00-$XXFF, (3) writing each byte to OAM via PPU, (4) adding 513 cycles (514 if starting on an odd CPU cycle) to the CPU's stall counter. This matches the real hardware's DMA controller behavior including the alignment penalty.

## Controller I/O

Controllers are accessed at $4016 (controller 1) and $4017 (controller 2, shared with APU frame counter). Writing 1 then 0 to $4016 strobes both controllers, latching the current button state. Each subsequent read returns one bit of the button state: A, B, Select, Start, Up, Down, Left, Right. OxideNES supports standard NES pads via `gilrs` (gamepad library) and keyboard mapping, with configurable rebinding stored in the config file.

## Bus Timing

The bus runs at the master clock rate. For NTSC: CPU ticks every 12 master cycles, PPU every 4 master cycles (3 PPU ticks per CPU tick). OxideNES uses this 3:1 ratio — for each `cpu.tick()`, `ppu.tick()` is called 3 times. The bus orchestrates this in its main `clock()` method, also ticking the APU at the CPU rate and handling DMA stalls.
