---
tags: [nes, wiki]
up: "[[NES Hardware Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# NES Console Architecture

> **The NES is a three-chip system built around separate CPU and PPU buses, with the cartridge bridging both worlds.**

## 🎯 Intuition
**The Core Idea:** The console centers on three major pieces of hardware: the Ricoh 2A03, the Ricoh 2C02, and the cartridge, all connected through two distinct buses.
**Analogy:** Think of three departments connected by two hallways: one hallway serves CPU-side traffic, the other serves graphics traffic, and the cartridge has doors to both.
**Why It Matters:** This is the blueprint every emulator must reproduce, because most NES behavior follows directly from who can see which memory over which bus.

---

## ⚙️ Core Mechanics
### How It Works
The NES is built around three main chips communicating via shared buses:
1. **Ricoh 2A03** — CPU (6502 core) + APU (sound) on one die
2. **Ricoh 2C02** — PPU (graphics) with its own address bus
3. **Cartridge** — External ROM/RAM connected to both CPU and PPU buses

### Key Specifications
A single 21.477272 MHz master clock divides:
- **CPU:** Master / 12 = 1.789773 MHz (NTSC)
- **PPU:** Master / 4 = 5.369318 MHz (3x CPU speed)

This 3:1 PPU:CPU ratio is fundamental to emulation timing.

The CPU and PPU have **separate address buses**:
- **CPU bus** (16-bit): Addresses 0x0000-0xFFFF — RAM, PPU registers, APU, cartridge PRG ROM
- **PPU bus** (14-bit): Addresses 0x0000-0x3FFF — Pattern tables, nametables, palettes

The cartridge sits on both buses simultaneously, providing PRG ROM to the CPU and CHR ROM/RAM to the PPU.

### Key Facts
- The APU is integrated into the Ricoh 2A03.
- The PPU has its own address bus rather than sharing the CPU's full address space.
- Cartridge hardware participates in both program and graphics memory access.
- The 3:1 PPU:CPU timing relationship is structural, not incidental.

---

## 🔬 Deep Dive
### Bus Separation
The separate CPU and PPU buses are one of the NES's defining architectural features. CPU-side traffic covers system RAM, memory-mapped PPU registers, APU state, and cartridge PRG ROM. PPU-side traffic covers pattern tables, nametables, and palettes. That split is why the cartridge can expose both PRG ROM and CHR ROM/RAM using different interfaces to the same physical board.

### Clocking
The entire system derives from a single 21.477272 MHz master clock. Dividing by 12 gives the NTSC CPU frequency of 1.789773 MHz, while dividing by 4 gives the PPU frequency of 5.369318 MHz. That fixed relationship produces the familiar 3x graphics clock.

### OxideNES Implementation
In OxideNES, the Bus struct (`bus.rs`, 351 lines) serves as the central memory arbitration layer, owning instances of CPU, PPU, APU, Cartridge, and Joypads. The `cpu_read` and `cpu_write` methods implement the full CPU memory map with proper mirroring. That makes `bus.rs` the concrete code embodiment of the console's architectural split between devices and address spaces.

### Reference Implementations
The most direct implementation reference is OxideNES's `bus.rs`, where the Bus mediates CPU-visible memory, enforces mapping rules, and models the mirrored regions that make the NES memory map behave like real hardware.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Which bus does a PPU pattern-table fetch use?
2. Why does the cartridge need access to both the CPU bus and the PPU bus?
3. What frequency do you get by dividing the 21.477272 MHz master clock by 4?

### Core Problems
1. Trace how a CPU-side PRG ROM read differs from a PPU-side CHR read in terms of which bus and address space are involved.
2. Explain why memory mirroring belongs in the Bus layer instead of in the CPU core itself.

### Challenge
Design a minimal emulator architecture that preserves the NES's separate CPU and PPU buses without overcomplicating ownership between CPU, PPU, APU, cartridge, and controller state.

---

*See also:* [[NES Technical Specifications]], [[NES History and Legacy]], [[NES vs Other 8-bit Consoles]], [[NES Hardware Overview]]

## References
→ [[Sources Index]]
