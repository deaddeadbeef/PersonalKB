---
tags: [raw, nes-emulation, netplay]
source: "OxideNES main.rs netplay implementation"
---

# Raw NES 007 — Netplay UDP Protocol

OxideNES includes a UDP-based netplay system for two-player gaming over a network. The implementation resides in main.rs using the socket2 crate for low-level socket control.

## Architecture

Netplay uses a lockstep peer-to-peer model. Both peers run the emulation simultaneously, exchanging controller inputs each frame. There is no authoritative server — both instances must produce identical state given identical inputs. This is guaranteed by the deterministic emulation core.

## Connection Setup

One player hosts (binds to a UDP port, default 6502 — a nod to the CPU), the other connects. The handshake exchanges: (1) protocol version byte, (2) ROM CRC32 hash to verify both players have the same ROM, (3) initial save state for synchronization. If the CRC32 doesn't match, the connection is rejected.

## Frame Protocol

Each frame, both peers: (1) read local controller input, (2) send an InputPacket containing frame number and 8-bit controller state, (3) wait for the remote InputPacket for the same frame, (4) advance emulation one frame using both inputs. The frame number prevents out-of-order packet issues. Packets are small (8 bytes: 4-byte frame number + 1-byte input + 3-byte padding/checksum).

## Input Delay and Rollback

To hide network latency, OxideNES implements input delay: local input is scheduled N frames in the future (configurable, default 2). This gives the network N frames to deliver the remote input before it's needed. If a remote packet arrives late, the emulation stalls briefly (frame skip) rather than desyncing. There is no rollback/GGPO-style speculative execution — the lockstep model trades occasional micro-stutters for implementation simplicity and guaranteed sync.

## Desync Detection

Every N frames (default 60), peers exchange a CRC32 of their current RAM state. If the checksums differ, a desync is detected. OxideNES logs the desync but does not currently auto-recover — the session should be restarted. Desyncs are rare in practice due to the deterministic emulation core but can occur if unofficial opcodes behave differently or mapper edge cases diverge.

## NAT Traversal

No built-in NAT traversal or hole punching is implemented. Players on different LANs must configure port forwarding or use a VPN. The UDP socket uses SO_REUSEADDR for flexibility. IPv4 and IPv6 are both supported via socket2's dual-stack capability.

## Latency Considerations

UDP is chosen over TCP for minimal latency — lost packets are preferable to head-of-line blocking. At 60 FPS, each frame is ~16.7ms. With 2 frames of input delay, the system tolerates up to ~33ms round-trip time without stuttering. LAN play is essentially perfect; WAN play works well on connections under 50ms RTT.
