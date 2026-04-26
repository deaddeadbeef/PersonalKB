---
tags: [raw, nes-emulation, expansion-audio]
source: "OxideNES mapper.rs expansion audio + NESdev"
---

# Raw NES 024 — Expansion Audio Hardware

Several NES cartridges contained additional audio hardware that expanded the console's sound capabilities beyond the built-in APU. These expansion audio chips produced additional channels mixed with the standard APU output. OxideNES implements the most significant expansion audio chips.

## Konami VRC6 (Mappers 24/26)

The VRC6 adds three channels to the NES audio:
- **Two pulse channels:** Unlike the APU's pulse channels with only 4 duty cycles, VRC6 pulses offer 8 duty cycle settings (6.25%, 12.5%, 18.75%, 25%, 31.25%, 37.5%, 43.75%, 50%), and each channel has direct 4-bit volume control (16 levels) — no envelope or sweep units needed.
- **One sawtooth channel:** A unique waveform generator that produces a sawtooth wave using an accumulator that adds a fixed value every 2 CPU cycles. When the accumulator overflows, it resets, creating the sawtooth shape. The accumulator rate (and thus pitch) is controlled by a 12-bit frequency register.

Used by: Castlevania III (Japanese version), Madara, Esper Dream 2.

OxideNES implementation: The VRC6 channels are embedded in the Mapper 24/26 struct. Each tick of the CPU clock updates the VRC6 channel state. Audio output is mixed with the main APU output by summing samples before the final DAC conversion.

## Konami VRC7 (Mapper 85)

The VRC7 contains a YM2413-derivative FM synthesis chip providing 6 FM channels. This is the most powerful expansion audio on the NES:
- 6 independently controllable channels
- 15 built-in instrument patches + 1 user-defined custom patch
- 2-operator FM synthesis per channel (modulator → carrier)
- ADSR envelope per operator
- Vibrato and tremolo effects

Used by: Lagrange Point (the only game to use VRC7).

OxideNES implements a simplified FM synthesis model for VRC7. The 15 instrument patches are stored as ROM data matching the YM2413 register format. FM synthesis computes: output = sin(carrier_freq × t + modulation_index × sin(mod_freq × t)), with the envelope shaping amplitude over time.

## Sunsoft 5B / FME-7 (Mapper 69)

Contains a YM2149-compatible PSG (Programmable Sound Generator) providing 3 square wave channels:
- 3 channels with 12-bit period registers
- 4-bit volume per channel or hardware envelope
- Noise generator (shared across channels)

Used by: Gimmick! (one of the most impressive NES soundtracks).

## Namco 163 (Mapper 19)

A unique wavetable synthesis chip supporting up to 8 channels:
- Each channel plays from a 4-bit wavetable stored in 128 bytes of internal RAM
- Wave length is configurable per channel (allowing different waveform complexity)
- More active channels = lower update rate per channel (they share time-division multiplexing)
- 4 channels at full quality is typical; 8 channels halves the sample rate

Used by: Rolling Thunder, Megami Tensei II, King of Kings.

## Mixing with APU

On real hardware, expansion audio is mixed with the APU output on the cartridge connector's audio pin. The mixing ratios vary by expansion chip and cartridge design. OxideNES uses configurable mixing levels, defaulting to balanced ratios determined by community research. The expansion audio samples are generated at the CPU clock rate alongside APU samples and summed before downsampling via blip_buf.
