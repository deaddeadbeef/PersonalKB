---
tags: [chunk, nes-emulation, netplay]
source: "[[raw-nes-007]]"
up: "[[Netplay — UDP Multiplayer]]"
---

# Chunk NES 094 — Netplay Desync Detection

Every 60 frames during netplay, both peers exchange CRC32 checksums of their current CPU RAM state. If checksums differ, a desync is detected and logged. OxideNES does not auto-recover from desyncs — the session must be restarted. Desyncs are rare due to the deterministic emulation core but can occur from unofficial opcode behavioral differences or mapper edge cases. No NAT traversal or hole punching is implemented; players on different LANs need port forwarding or VPN. The default port is 6502 (a nod to the CPU). IPv4 and IPv6 are both supported via socket2 dual-stack capability.
