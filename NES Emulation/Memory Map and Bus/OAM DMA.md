---
tags: [nes, wiki]
up: "[[Memory Map and Bus Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# OAM DMA

> **A hardware-accelerated bulk transfer that copies 256 bytes of sprite data to the PPU's OAM, halting the CPU for 513-514 cycles.**

## 🎯 Intuition
**The Core Idea:** OAM DMA is a dedicated hardware shortcut that copies an entire page (256 bytes) of sprite data from CPU memory to the PPU's Object Attribute Memory in one atomic operation, freezing the CPU while it works.
**Analogy:** Imagine the postal system has a special express delivery service: instead of the CPU hand-carrying 256 letters one at a time to the PPU's sprite mailbox (which would take forever and mess up timing), it hands the entire mailbag to a courier (DMA) who delivers all 256 letters while the CPU takes a mandatory coffee break for exactly 513-514 cycles.
**Why It Matters:** Every NES game uses OAM DMA every frame — it's the standard way to update sprites. The exact cycle cost (513 vs 514 depending on CPU cycle parity) affects PPU synchronization, and getting this wrong causes sprite glitches or timing desync.

---

## ⚙️ Core Mechanics
### How It Works
1. CPU writes page number XX to register 0x4014
2. DMA copies 256 bytes from CPU address XX00-XXFF to OAM
3. CPU is **halted** for 513 or 514 cycles during transfer

### Key Specifications
- **513 cycles** on even CPU cycles (256 read-write pairs + 1 alignment cycle)
- **514 cycles** on odd CPU cycles (extra dummy cycle for alignment)
- Each byte: 1 read cycle + 1 write cycle = 2 cycles per byte
- Games typically use page 0x02 (RAM 0x0200-0x02FF) as a shadow OAM buffer

### Key Facts
- OAM DMA is triggered by writing to 0x4014 — the value written is the high byte of the source address
- The CPU is completely halted during DMA — no instructions execute
- Manually writing 256 bytes through OAMDATA (0x2004) one at a time would be much slower and would interfere with PPU timing
- DMA ensures all sprites are updated atomically during vblank

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Even/Odd Cycle Alignment:** The DMA controller needs to synchronize with the CPU's read/write cycle alternation. If DMA starts on an even CPU cycle, it takes 513 cycles (1 idle + 256 × 2). If it starts on an odd cycle, it takes 514 cycles (1 alignment + 1 idle + 256 × 2). This is because the DMA reads must occur on read cycles.

**DMA and DMC Conflict:** If the DMC (Delta Modulation Channel) requests a sample byte during OAM DMA, the DMC read takes priority, inserting additional stall cycles. This interaction is extremely timing-sensitive and only matters for cycle-exact emulation.

**OAMADDR Interaction:** The DMA writes to OAM starting at the current OAMADDR value. Most games set OAMADDR to 0 before triggering DMA, but if OAMADDR is non-zero, sprites will be shifted in OAM.

### Common Emulation Pitfalls
1. **Hardcoding 513 cycles** — If you always use 513 cycles instead of checking even/odd cycle parity, you'll be off by one cycle per frame. Over time this accumulates and desynchronizes PPU timing
2. **Not halting the CPU** — If the CPU continues executing during DMA, it will process instructions it shouldn't, corrupting game state and desynchronizing with the PPU
3. **Forgetting OAMADDR offset** — If you always start writing at OAM byte 0 instead of the current OAMADDR, sprites will be positioned incorrectly in games that use non-zero OAMADDR

### Reference Implementations
OxideNES bus.rs tracks DMA state with `dma_active()` and `dma_tick()`. The DMA state machine alternates between read and write cycles with proper even/odd cycle handling. The CPU's `tick` function yields control during DMA.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does OAM DMA exist instead of having games write sprites byte-by-byte through OAMDATA?
2. What determines whether DMA takes 513 or 514 cycles?
3. If the CPU writes 0x02 to 0x4014, what address range is copied and where does it go?

### Core Problems
1. **Implement the DMA state machine:** Write a DMA controller that alternates between read (from CPU bus) and write (to OAM) cycles, with proper initial alignment based on even/odd CPU cycle.
2. **Cycle accounting:** After OAM DMA completes, the CPU must resume at the correct cycle count. Implement the logic that adds 513 or 514 to the CPU's cycle counter and correctly advances the PPU by the same amount × 3.

### Challenge
**DMA + DMC conflict:** During OAM DMA, the DMC channel needs to fetch a sample byte from address 0xC000. What happens to the DMA transfer? How many total extra cycles does the DMC steal, and how does this affect the PPU timing for that frame? Implement the priority logic and verify the total cycle count.

---

*See also:* [[CPU Memory Map]], [[PPU Memory Map]], [[Sprites and OAM]], [[Memory Map and Bus Overview]]

## References
→ [[Sources Index]]
