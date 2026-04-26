---
tags: [raw, nes-emulation, apu]
source: "OxideNES apu.rs + NESdev APU reference"
---

# Raw NES 003 — APU Channels and Frame Sequencer

The NES Audio Processing Unit (APU) in OxideNES is implemented in `apu.rs` (~973 lines). It generates audio through five channels: two pulse (square wave) channels, one triangle channel, one noise channel, and one DMC (delta modulation) channel. Audio output is mixed and sent to the host via the `cpal` audio library.

## Pulse Channels (1 and 2)

Each pulse channel generates a square wave with selectable duty cycle (12.5%, 25%, 50%, 75%). Key components: an 11-bit timer (period), a length counter for automatic silencing, an envelope generator for volume control (constant or decaying), and a sweep unit that periodically adjusts the period up or down. Pulse 1's sweep uses one's complement for negation while Pulse 2 uses two's complement — a hardware quirk faithfully emulated. The duty cycle is implemented as an 8-step sequence where the number of high steps varies by duty setting.

## Triangle Channel

The triangle channel produces a triangle wave using a 32-step sequence (values 15,14,...,1,0,0,1,...,14,15). It has a linear counter (reloaded from a control register) and a length counter, both of which must be non-zero for output. Unlike pulse channels, it has no volume control — it's either on or off at full volume. At very low periods, the rapid cycling produces a buzzing sound often used for percussion effects in NES games.

## Noise Channel

The noise channel uses a 15-bit linear feedback shift register (LFSR) to produce pseudo-random noise. Two modes exist: long mode (period 32,767) taps bits 0 and 1, and short mode (period 93) taps bits 0 and 6, producing a more metallic/tonal sound. The LFSR is clocked by one of 16 timer periods selected via a 4-bit register. Like pulse channels, it has an envelope generator and length counter.

## DMC (Delta Modulation Channel)

The DMC plays 1-bit delta-encoded samples from memory. A sample address and length specify the data region in CPU address space ($C000-$FFFF). Each byte is read via DMA (stalling the CPU 1-4 cycles), then each bit shifts out: 1 increments the output level by 2, 0 decrements by 2, clamped to 0-127. DMC can trigger IRQ on completion and optionally loop.

## Frame Sequencer

The APU frame sequencer clocks the length counters, envelope generators, sweep units, and linear counter at specific intervals. In 4-step mode (240 Hz effective): quarter frame (envelope+linear) at steps 1-4, half frame (length+sweep) at steps 2 and 4, with optional IRQ at step 4. In 5-step mode: same clocking but over 5 steps with no IRQ, providing a slightly different timing feel. OxideNES implements this as a cycle counter that fires events at the hardware-accurate cycle positions.

## Mixing

The final audio output mixes all channels using the non-linear mixing formula from the NES hardware: pulse_out uses a lookup table indexed by pulse1+pulse2, and tnd_out uses a table indexed by 3×triangle + 2×noise + dmc. OxideNES uses blip_buf for band-limited synthesis, preventing aliasing artifacts when resampling from the NES's ~1.79 MHz sample rate to the host's 44.1/48 kHz.
