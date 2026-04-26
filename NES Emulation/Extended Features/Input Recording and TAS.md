---
tags: [nes, wiki]
up: "[[Extended Features Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Input Recording and TAS

> **OxideNES records frame-perfect controller input for replay, TAS workflows, and cross-emulator export.**

## 🎯 Intuition
**The Core Idea:** Frame-perfect input capture enables replay, TAS, and cross-emulator sharing.
**Analogy:** A player piano roll — every press is timestamped for exact playback.
**Why It Matters:** It is the foundation for TAS speedrunning and deterministic testing.

---

## ⚙️ Core Mechanics
### How It Works
OxideNES records controller inputs frame-by-frame, enabling:
- **Replay:** Watch recorded gameplay
- **TAS creation:** Build tool-assisted speedruns using save states + recording
- **FM2 export:** Share recordings with FCEUX users

### Key Specifications

| Field | Size | Content |
|-------|------|---------|
| Magic | 4 bytes | "NREC" |
| Version | 1 byte | Format version |
| SHA-256 | 32 bytes | ROM hash for verification |
| Frames | 2 bytes each | P1 input byte + P2 input byte |

### Key Facts
- Each input byte packs 8 buttons: `A(0), B(1), Select(2), Start(3), Up(4), Down(5), Left(6), Right(7)`.
- Recordings are tied to a specific ROM via SHA-256 hash.
- Loading a recording for the wrong ROM is rejected, ensuring playback accuracy.
- Frame data is stored as compact 2-byte pairs.

### FM2 Export Format
FCEUX-compatible text format:
```

|0|RLDUTSBA|........|
```
Where each character is a button flag (letter = pressed, dot = released).

---

## 🔬 Deep Dive
### `recording.rs`
The OxideNES implementation lives in `recording.rs` (`372` lines).

### Recording Lifecycle
`InputRecording` manages lifecycle (`start/stop recording`, `start/stop playback`).

### ROM Binding
The implementation includes a minimal SHA-256 implementation for ROM hashing.

### Frame Storage
Frame data is stored as compact `2`-byte pairs.

### Reference Implementations
In OxideNES, `InputRecording` captures controller state frame-by-frame, writes `.nrec` data with a ROM SHA-256 binding, supports deterministic playback, and can export frames into FCEUX-compatible FM2 text.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Calculate the file size impact of storing a `10`-minute recording as `2` bytes per frame, ignoring the header.
- Explain why SHA-256 ROM binding matters for playback accuracy.
- Convert one `.nrec` frame conceptually into the FM2 button-string format.

### Core Problems
- Describe how `A(0), B(1), Select(2), Start(3), Up(4), Down(5), Left(6), Right(7)` fits into a single byte.
- Explain why compact `2`-byte frame pairs are a good fit for deterministic input playback.

### Challenge
- Propose a workflow that uses save states plus input recording to create and verify a simple TAS segment.

---

*See also:* [[Achievement System]], [[Lua Scripting Engine]], [[Netplay — UDP Multiplayer]], [[Extended Features Overview]]

## References
→ [[Sources Index]]