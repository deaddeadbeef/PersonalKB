---
tags: [nes, wiki]
up: "[[Extended Features Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Netplay — UDP Multiplayer

> **OxideNES uses peer-to-peer UDP lockstep networking so both players exchange one frame of input before advancing emulation together.**

## 🎯 Intuition
**The Core Idea:** Peer-to-peer lockstep multiplayer over UDP exchanges input every frame.
**Analogy:** A synchronized dance over the phone — both players call out moves each beat, wait to hear the partner, then step together.
**Why It Matters:** It adds online multiplayer to a local-only console, and lockstep keeps game state identical on both sides.

---

## ⚙️ Core Mechanics
### How It Works
#### Architecture
OxideNES implements peer-to-peer multiplayer over UDP:
- **Player 1 (Host):** Listens on configurable port (default `7777`)
- **Player 2 (Client):** Connects to host `IP:port`
- **Protocol:** Custom binary packets with magic byte identification

#### Packet Types

| Magic | Type | Content |
|-------|------|---------|
| NH | Host Welcome | Handshake initiation |
| NC | Join Request | Client connection |
| NA | Accept | Host acknowledges |
| NP | Input | Frame number + button state + checksum |
| NK | Keepalive | Heartbeat every 2 seconds |

#### Frame Synchronization
Both players advance frames in lockstep:
1. Each frame, local input is sent to the remote player
2. Emulation waits for remote input before advancing
3. Configurable input delay buffers network jitter
4. Desync detection via frame checksum (planned)

### Key Specifications

| Component | Detail |
|-----------|--------|
| Transport | UDP |
| Host port | Default `7777` |
| Session model | Peer-to-peer lockstep |
| Input encoding | `8` buttons packed into `1` byte |
| Keepalive | Heartbeat every `2` seconds |
| Socket mode | Non-blocking via `socket2` crate |

### Key Facts
- The host listens on port `7777` by default.
- The client connects directly to the host `IP:port`.
- `NH`, `NC`, and `NA` form the handshake sequence.
- `NP` packets carry frame number, button state, and checksum.
- `NK` packets keep the session alive every `2` seconds.
- Desync detection is planned via frame checksum.

---

## 🔬 Deep Dive
### `netplay.rs`
The OxideNES implementation lives in `netplay.rs` (`491` lines).

### Session Management
`NetplaySession` manages connection lifecycle.

### Input Encoding
Input encoding packs `8` buttons into a single byte.

### Networking Details
Keepalive heartbeat prevents firewall UDP timeout. The socket is non-blocking via the `socket2` crate.

### Desync Detection
Desync detection via frame checksum is planned.

### Reference Implementations
In OxideNES, `NetplaySession` performs a UDP handshake using `NH`, `NC`, and `NA`, exchanges per-frame `NP` input packets, sends `NK` heartbeats every `2` seconds, and advances emulation in lockstep after both sides have the required input.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Explain why UDP is a better fit than TCP for this lockstep design.
- Describe what should happen when an input packet arrives late.
- Trace the handshake sequence `NH → NC → NA`.

### Core Problems
- Explain why lockstep requires both peers to wait for remote input before advancing.
- Describe how configurable input delay helps buffer network jitter.

### Challenge
- Design a simple desync-detection extension using the planned frame-checksum mechanism and explain when each peer should react.

---

*See also:* [[Achievement System]], [[Input Recording and TAS]], [[Lua Scripting Engine]], [[Extended Features Overview]]

## References
→ [[Sources Index]]