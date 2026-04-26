---
tags: [raw, nes-emulation, timing]
source: "NESdev timing + OxideNES bus.rs"
---

# Raw NES 020 — Master Clock and Timing System

Accurate timing is the foundation of NES emulation. The NES uses a master clock that drives all subsystems at fixed ratios, and OxideNES implements these relationships precisely.

## NTSC Master Clock

The NTSC NES master clock runs at 21.477272 MHz (21,477,272 Hz). This is derived from a crystal oscillator that produces a frequency exactly 6× the NTSC colorburst frequency (3.579545 MHz × 6).

## Clock Dividers

From the master clock, each subsystem derives its operating frequency:
- **CPU:** Master ÷ 12 = 1.789773 MHz (~1.79 MHz). Each CPU cycle is 12 master cycles.
- **PPU:** Master ÷ 4 = 5.369318 MHz (~5.37 MHz). Each PPU cycle is 4 master cycles.
- **Ratio:** 3 PPU cycles per 1 CPU cycle (12/4 = 3).
- **APU:** Clocked at the CPU rate. The frame sequencer further divides this for envelope/length counter clocking (~240 Hz quarter-frame, ~120 Hz half-frame).

## Frame Timing

One NTSC frame consists of 262 scanlines × 341 PPU cycles = 89,342 PPU cycles. At 3:1 ratio, this is 29,780.67 CPU cycles per frame. The fractional cycle is handled by the "odd frame skip" — on odd frames, the pre-render scanline is 340 cycles instead of 341, giving alternating frame lengths of 29,780 and 29,781 CPU cycles. This produces a frame rate of approximately 60.0988 FPS.

## PAL Timing

PAL NES uses a 26.601712 MHz master clock with CPU ÷ 16 and PPU ÷ 5 (3.2 PPU cycles per CPU cycle). PAL has 312 scanlines per frame, resulting in ~50.007 FPS. OxideNES supports PAL timing as a configuration option, though NTSC is the default since most NES games are NTSC.

## OxideNES Main Loop

The bus's clock() method implements the timing relationship:
`ust
pub fn clock(&mut self) {
    // PPU ticks 3 times per CPU tick
    self.ppu.tick();
    self.ppu.tick();
    self.ppu.tick();

    // CPU ticks once (unless stalled by DMA)
    if self.dma_cycles == 0 {
        self.cpu.tick(&mut self.bus);
    } else {
        self.dma_cycles -= 1;
    }

    // APU ticks at CPU rate
    self.apu.tick();
}
`

The outer loop calls clock() until ppu.frame_complete is set, then renders the frame and sleeps until the next frame boundary to maintain 60 FPS. Frame pacing uses std::time::Instant for high-resolution timing, with optional VSync support through minifb.

## Cycle Counting for Synchronization

The PPU and CPU need tight synchronization because they interact through shared registers. Critical timing points include:
- NMI is asserted at PPU cycle 1 of scanline 241 — the CPU must see this at the exact CPU cycle
- Sprite-0 hit timing depends on the exact PPU cycle the hit occurs
- Mid-frame PPU register writes must take effect at the correct cycle

OxideNES achieves this through the per-tick interleaving approach: for every CPU cycle, exactly 3 PPU cycles execute beforehand. This ensures the PPU state is always up-to-date when the CPU reads PPU registers.

## Audio Timing

The APU generates samples at the CPU clock rate (~1.79 MHz) but the host audio runs at 44,100 or 48,000 Hz. OxideNES uses lip_buf for band-limited downsampling: the APU writes amplitude deltas into the blip buffer at NES timestamps, and lip_buf renders these into PCM samples at the host rate. This prevents aliasing and produces clean audio. The audio buffer acts as the primary frame pacing mechanism — if audio gets ahead of emulation, the frame loop delays; if behind, frames are skipped.
