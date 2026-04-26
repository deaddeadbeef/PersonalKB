---
tags: [cs-ds, raw]
id: raw-ds-028
source: "Open Data Structures (Morin, Ch. 5)"
up: "[[CS Data Structures]]"
---

# Linear Probing and Open Addressing Deep Dive

## Key Ideas
- Open addressing: all elements stored in the table array itself (no chaining)
- Linear probing: on collision, try next slot sequentially — h(k), h(k)+1, h(k)+2, ...
- Primary clustering: long runs of occupied slots degrade performance
- Expected probes (successful): ~1/(1-alpha) for load factor alpha
- Expected probes (unsuccessful): ~1/(1-alpha)^2
- Quadratic probing: try h(k)+1, h(k)+4, h(k)+9, ... — reduces primary clustering
- Double hashing: h(k) + i*h2(k) — eliminates clustering entirely
- Robin Hood: displace existing if new key has longer probe distance — equalizes probe lengths
- Deletion problem: can't just empty slots — use tombstones or backward-shift deletion
- Backward-shift deletion: fill gap by shifting subsequent entries back — no tombstones needed
- Swiss Table (Google): SIMD parallel probe, metadata byte per slot, state-of-art performance
- Load factor sweet spot: 0.5-0.7 for linear probing, up to 0.9 for Robin Hood

## Cache Performance
- Linear probing has excellent cache behavior: sequential memory access
- This often outweighs theoretical advantages of double hashing in practice
