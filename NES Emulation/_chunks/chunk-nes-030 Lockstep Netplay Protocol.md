---
tags: [chunk, nes-emulation, netplay]
source: "[[raw-nes-007]]"
up: "[[Netplay — UDP Multiplayer]]"
---

# Chunk NES 030 — Lockstep Netplay Protocol

OxideNES netplay uses a lockstep peer-to-peer model over UDP. Both peers run identical emulation, exchanging controller inputs each frame via 8-byte InputPackets (4-byte frame number + 1-byte input + checksum). Connection setup exchanges protocol version, ROM CRC32 (rejecting mismatches), and an initial save state for synchronization. Input delay (default 2 frames) hides latency by scheduling local input N frames ahead. Every 60 frames, peers exchange RAM CRC32 checksums for desync detection. UDP is chosen over TCP for minimal latency — at 60 FPS each frame is 16.7ms, tolerating up to 33ms RTT with 2-frame delay.
