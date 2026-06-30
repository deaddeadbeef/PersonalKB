---
tags: [study, nes-emulation, architecture]
up: "[[NES Emulation Study Index]]"
confidence: policy
---
# Review Drill — Emulator Architecture

Test your understanding of OxideNES design and features.

## Questions

**Q1:** What is the PPU-to-CPU cycle ratio and how is it implemented?
> 3:1. The bus clock() method calls ppu.tick() three times, then cpu.tick() once (unless DMA-stalled), then apu.tick() once. This interleaving ensures PPU state is always current for CPU register reads.

**Q2:** List the 7 stages of the CRT simulation pipeline in order.
> (1) Bilinear upscale, (2) phosphor persistence, (3) gamma correction LUT, (4) scanlines + vignette, (5) barrel distortion, (6) shadow mask, (7) glass reflections + chromatic aberration.

**Q3:** How does the save state system handle version compatibility?
> States encode a version number from semver. If the format changes, old states are rejected with a mismatch error. States use serde/bincode compressed with zstd. 10 slots per ROM stored by CRC32.

**Q4:** Describe the rewind system's implementation.
> A ring buffer (default 300 entries) stores compressed state snapshots every 2 frames. Holding rewind pops states in reverse order. ~3.6 MB total memory. Disabled during netplay.

**Q5:** How does netplay maintain synchronization?
> Lockstep peer-to-peer: both run identical emulation exchanging inputs each frame via UDP. ROM CRC32 verified at connection. Input delay (default 2 frames) hides latency. RAM CRC32 checksums every 60 frames detect desync.

**Q6:** What zero-allocation strategy does OxideNES use?
> All large buffers (frame, rewind ring, audio) pre-allocated at startup. No heap allocation during emulation frames. Rust ownership enforces this at compile time. Prevents GC-like pauses.

**Q7:** Name the key Rust crates OxideNES depends on and their purposes.
> minifb (windowing), cpal (audio output), gilrs (gamepad input), mlua (Lua scripting), serde/bincode (serialization), socket2 (UDP netplay), ringbuf (rewind buffer), blip_buf (audio resampling), crc32fast (ROM hashing), semver (version checking).

**Q8:** What is the main.rs vs core split in OxideNES?
> Core (bus, cpu, ppu, apu, mapper) handles pure emulation. main.rs (~7,572 lines) wraps it with window, CRT pipeline, input, audio, save states, rewind, netplay, Lua, achievements, and config. This keeps the core testable and platform-independent.

## References
- [[NES Emulation/Sources/Sources Index|NES Emulation Sources Index]]
