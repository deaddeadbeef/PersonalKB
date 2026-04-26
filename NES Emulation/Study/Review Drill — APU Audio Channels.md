---
tags: [study, nes-emulation, apu]
up: "[[NES Emulation Study Index]]"
---

# Review Drill — APU Audio Channels

Test your understanding of the NES Audio Processing Unit.

## Questions

**Q1:** List all five APU channels and their waveform types.
> Pulse 1 (square, 4 duty cycles), Pulse 2 (square, 4 duty cycles), Triangle (32-step triangle wave), Noise (LFSR pseudo-random), DMC (1-bit delta-encoded samples).

**Q2:** What is the hardware quirk difference between Pulse 1 and Pulse 2 sweep units?
> Pulse 1 uses ones complement for sweep negation, Pulse 2 uses twos complement. This gives slightly different minimum period values and must be emulated faithfully.

**Q3:** How does the noise channel's short mode differ from long mode?
> Long mode taps LFSR bits 0 and 1, producing white noise with period 32,767. Short mode taps bits 0 and 6, producing metallic/tonal buzzing with period 93. Short mode is used for metallic percussion effects.

**Q4:** How does DMC playback stall the CPU?
> Each DMC DMA byte fetch stalls the CPU 1-4 cycles depending on CPU state. DMC DMA can interrupt OAM DMA, causing a glitch byte in OAM.

**Q5:** Describe the two frame sequencer modes.
> 4-step mode: quarter frames (envelope+linear) at all 4 steps, half frames (length+sweep) at steps 2 and 4, optional IRQ at step 4. 5-step mode: same clocking over 5 steps with no IRQ.

**Q6:** How does the APU mix channels?
> Non-linear mixing via lookup tables: pulse_out indexed by pulse1+pulse2 sum, tnd_out indexed by 3*triangle + 2*noise + DMC. This means louder channels slightly suppress quieter ones.

**Q7:** How does OxideNES handle sample rate conversion from 1.79 MHz to 44.1/48 kHz?
> Uses blip_buf for band-limited synthesis. The APU writes amplitude deltas at NES timestamps; blip_buf renders these to PCM at the host rate, preventing aliasing artifacts.

**Q8:** Name two NES expansion audio chips and their capabilities.
> VRC6: 2 enhanced pulse channels (8 duty cycles) + sawtooth. VRC7: 6-channel FM synthesis with YM2413 derivative, 15 instrument patches. Also: Namco 163 (wavetable), Sunsoft 5B (3 PSG channels).
