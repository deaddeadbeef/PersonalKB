---
tags: [cs-ds, chunk]
id: chunk-ds-132
source: "[[raw-ds-031]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Bellman-Ford detects negative cycles by checking for relaxation in round V

## Context
Dijkstra fails with negative edge weights.

## Claim
Bellman-Ford runs V-1 relaxation rounds. If any edge can still be relaxed in round V a negative cycle exists. This detection is O(VE) and is the only polynomial shortest-path algorithm handling negative weights.

## Why It Matters
Required for currency arbitrage detection and network routing protocols like RIP.

## QnA Seeds
- Q: Why V-1 rounds? -> A: Shortest path has at most V-1 edges. Each round propagates one edge further.
- Q: How to find the negative cycle? -> A: Track predecessors from any relaxable edge in round V and follow back.
