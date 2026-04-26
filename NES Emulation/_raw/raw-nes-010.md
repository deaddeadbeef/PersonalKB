---
tags: [raw, nes-emulation, savestate]
source: "OxideNES main.rs save/rewind implementation"
---

# Raw NES 010 — Save States and Rewind System

OxideNES implements both save states (manual snapshots) and a rewind system (continuous state recording) that allow the player to save and restore the complete emulation state.

## Save State Format

A save state captures the entire emulation state via serde serialization:
- CPU: All registers (A, X, Y, SP, PC, P), cycle counter, interrupt flags
- PPU: VRAM (2 KB), OAM (256 bytes), palette RAM (32 bytes), scroll registers (v, t, x, w), scanline/cycle position, all control/mask/status flags
- APU: All channel state (timers, counters, envelope, sweep), frame sequencer position, output buffer
- Bus: Internal RAM (2 KB), controller latch state, DMA state
- Mapper: Bank registers, IRQ counter, PRG/CHR RAM (if any) — each mapper implements Serialize/Deserialize
- Cartridge RAM: Full battery-backed RAM contents (8 KB when present)

The state is serialized using serde with bincode format for compact binary representation. Typical save state size is 10-15 KB depending on the mapper (larger for mappers with extra RAM like MMC5). States are compressed with zstd before writing to disk.

## Save State Slots

OxideNES provides 10 save state slots (0-9) accessed via keyboard shortcuts (Shift+F1-F10 to save, F1-F10 to load). Slots are stored as files in ~/.nes-emulator/states/<rom-crc32>/slot-N.state. Quick save/load (without selecting a slot) uses slot 0 by default.

## Rewind Implementation

The rewind system works by automatically saving a compressed state snapshot every N frames (default: every 2 frames). A ring buffer holds the last M snapshots (default: 300, giving ~10 seconds of rewind at 60 FPS). When the user holds the rewind key, the emulator pops states from the ring buffer, replacing the current state and rendering each frame in reverse.

The ring buffer uses the ingbuf crate for efficient circular buffer operations. Total rewind memory usage is approximately 300 × 12 KB = ~3.6 MB — negligible on modern systems. The snapshot interval and buffer size are configurable in the emulator settings.

## State Compatibility

Save states encode a version number. If the emulator version changes in a way that alters the serialization format, old save states are rejected with a version mismatch error rather than loading corrupt state. The version is derived from the emulator's semver version using the semver crate.

## Edge Cases

- Loading a state mid-DMA correctly restores the DMA transfer state
- PPU mid-scanline state is fully captured, enabling frame-perfect save/load
- Mapper IRQ counter state is preserved, preventing IRQ timing glitches after load
- Rewind during netplay is disabled to prevent desync — only single-player mode supports rewind
- Achievement state is independent of save states (see raw-nes-009)
