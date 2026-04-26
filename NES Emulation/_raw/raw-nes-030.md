---
tags: [raw, nes-emulation, tas]
source: "OxideNES TAS features + TAS community practices"
---

# Raw NES 030 — Tool-Assisted Speedrunning Support

OxideNES includes features specifically designed for Tool-Assisted Speedrunning (TAS) — the practice of using emulator tools to create theoretically perfect gameplay through frame-by-frame input optimization.

## What is TAS?

A TAS is a carefully crafted input recording that, when played back on a deterministic emulator, produces optimal gameplay — fastest completion time, maximum score, or entertainment value. TASers use frame advance, save states, and input display to find frame-perfect strategies impossible for human players.

## Input Recording Format

OxideNES records inputs in a binary format:
- **Header (16 bytes):** Format version (2 bytes), ROM CRC32 (4 bytes), frame count (4 bytes), re-record count (4 bytes), flags (2 bytes)
- **Per-frame data (2 bytes per frame):** Player 1 input (1 byte) + Player 2 input (1 byte)

Total file size = 16 + (frame_count × 2) bytes. A typical 5-minute TAS (18,000 frames at 60 FPS) is ~36 KB.

## Frame Advance

The most critical TAS tool. Pressing the frame advance key (default: period key) advances the emulation by exactly one frame and pauses. This allows the TASer to examine each frame individually, test different inputs, and find the frame-perfect timing for jumps, attacks, and other actions.

## Re-recording

When a TASer loads a save state during recording, the input log is truncated to the save state's frame number, and new inputs overwrite from that point. The re-record counter increments. Competitive TAS typically involves thousands to tens of thousands of re-records as the TASer optimizes each section. OxideNES tracks re-records for metadata purposes.

## Input Display

An on-screen overlay shows the current controller state: a visual representation of the NES controller with buttons highlighted as they're pressed. This is essential for both creating and presenting TAS content. OxideNES renders this as a simple graphic overlay on the display output, after the CRT pipeline.

## Determinism Requirements

TAS replay correctness depends on perfect determinism — the same inputs must produce the same output every time. OxideNES ensures this by:
- No dependency on real-time clocks during emulation
- Fixed-point arithmetic where floating-point might introduce platform variance
- Deterministic initialization of all state (no uninitialized memory)
- Consistent instruction timing (no optimizations that change cycle counts)

## RAM Watch

TASers use memory monitoring to understand game state. OxideNES's Lua scripting enables this: scripts can read memory addresses every frame and display values on screen (player position, speed, boss HP, RNG state). The `emu.on_frame()` callback combined with `emu.read()` and `emu.draw_text()` creates a real-time RAM watch.

## Subframe Input

On real NES hardware, controller state can change between frames (between $4016 reads). Advanced TAS techniques exploit this for "subframe" inputs that are impossible on standard emulators. OxideNES does not currently support subframe input recording, which is consistent with most community emulators.

## Community Format Compatibility

The OxideNES input format is not directly compatible with other emulators' formats (FCEUX .fm2, BizHawk .bk2). A conversion tool could be written to translate between formats, but this is not currently implemented. The priority is internal consistency and deterministic replay.
