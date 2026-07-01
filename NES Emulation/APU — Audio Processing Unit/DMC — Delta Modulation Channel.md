---
tags: [nes, wiki]
up: "[[APU — Audio Processing Unit Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# DMC — Delta Modulation Channel

> **The sample-playback channel that reads 1-bit delta-encoded PCM audio from ROM, stealing CPU cycles to fetch each byte.**

## 🎯 Intuition
**The Core Idea:** The DMC is the NES's sampler — it plays pre-recorded audio by reading bytes from ROM and interpreting each bit as "output level goes slightly up" or "slightly down," producing rough but recognizable reproductions of drums, voices, and sound effects.
**Analogy:** The DMC is like a DJ's turntable playing a vinyl record, but the record only stores "move the needle up a tiny bit" or "move it down a tiny bit" for each moment. The DJ (DMC) has to physically walk over to the record shelf (ROM) to grab each groove of the record, and while walking, the main performer (CPU) has to stop and wait. This "cycle stealing" is the DMC's most notorious behavior.
**Why It Matters:** DMC cycle stealing is one of the hardest APU behaviors to emulate accurately. It inserts unpredictable CPU stalls that affect timing of everything else — PPU sync, controller reads, and other APU timing. Many test ROMs specifically target DMC DMA interactions.

---

## ⚙️ Core Mechanics
### How It Works
1. DMC reads a byte from memory (ROM) at a specified address
2. Each bit shifts the output level up or down by 2 (out of 0-127 range)
3. Bit = 1: output += 2 (clamped at 127)
4. Bit = 0: output -= 2 (clamped at 0)
5. 8 bits per byte at configurable rate = 4.2 kHz to 33.1 kHz

### Key Specifications

**DMC Registers**

| Register | Address | Function |
|----------|---------|----------|
| DMC Freq | 0x4010 | IRQ enable, loop flag, rate index |
| DMC Raw | 0x4011 | Direct 7-bit output load |
| DMC Addr | 0x4012 | Sample start address (0xC000 + value × 64) |
| DMC Len | 0x4013 | Sample length (value × 16 + 1 bytes) |

### Key Facts
- **DMA Cycle Stealing:** When the DMC needs a new sample byte, it halts the CPU for approximately 4 cycles to perform a read from the CPU bus — this stall is called "DMC DMA"
- **Sample Address Range:** Samples always start in the 0xC000-0xFFFF range (PRG ROM upper region)
- **Use in Games:**
  - Super Mario Bros. 3: Drum samples and sound effects
  - Mega Man series: Impact and explosion sounds
  - Ninja Gaiden: Voice samples and percussion

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Cycle Stealing Details:** The DMC DMA stall is not a simple 4-cycle halt. The exact number of stolen cycles depends on what the CPU is doing when the DMA occurs:
- If the CPU is on a read cycle: 4 cycles stolen
- If on a write cycle: 3 cycles stolen
- If during OAM DMA: interaction is complex — both DMA controllers compete for the bus

**Sample Looping:** When the loop flag is set, the sample restarts from the beginning address when it reaches the end. When the loop flag is clear and the sample ends, the DMC can optionally fire an IRQ.

**Address Wrapping:** The sample address auto-increments after each byte read. When it reaches 0xFFFF, it wraps to 0x8000 (not 0x0000), staying within the PRG ROM address space.

**Direct Load (0x4011):** Writing to 0x4011 directly sets the 7-bit output level. This is used for raw PCM playback (by writing rapid values from the CPU) and causes an audible pop if the change is large.

### Common Emulation Pitfalls
1. **Ignoring cycle stealing** — If the DMC reads don't halt the CPU, timing-sensitive code (like sprite 0 hit polling) will be off by 3-4 cycles per sample byte, causing visual glitches in games with active DMC playback
2. **Wrong sample address formula** — The starting address is `0xC000 + (value × 64)`, not `value × 64`. Forgetting the 0xC000 base reads from the wrong ROM region and produces garbage audio
3. **Not clamping output** — The output level must be clamped to the 0-127 range. Without clamping, values wrap around and produce harsh distortion

### Reference Implementations
The OxideNES `Dmc` struct in `apu.rs` tracks sample address, remaining length, shift register, and output level. DMC DMA stall is tracked in `bus.rs` with accurate cycle stealing counted against the CPU.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does the DMC need to steal CPU cycles instead of reading ROM through its own bus?
2. What is the maximum sample length in bytes, and at the highest rate, how long does it play?
3. How does writing directly to 0x4011 differ from normal DMC playback?

### Core Problems
1. **Implement the DMC output unit:** Write the bit-by-bit output processing: shift register feeds one bit per output cycle, adjusting the 7-bit output level by ±2 with clamping. When all 8 bits are consumed, request a new byte.
2. **Implement DMA cycle stealing:** When the DMC's sample buffer is empty, insert a CPU stall of the appropriate cycle count (3-4 depending on current CPU phase) and perform the read from the sample address.

### Challenge
**DMC + OAM DMA interaction:** OAM DMA is in progress (CPU halted, DMA controller reading page 0x02) when the DMC simultaneously needs a sample byte from 0xC000. What happens? Which DMA gets bus priority? How many total extra cycles are inserted? Implement the interaction and verify against known test ROM behavior (e.g., `dmc_dma_during_read4`).

---

*See also:* [[Pulse Channels]], [[Triangle and Noise Channels]], [[APU Frame Sequencer]], [[APU — Audio Processing Unit Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
