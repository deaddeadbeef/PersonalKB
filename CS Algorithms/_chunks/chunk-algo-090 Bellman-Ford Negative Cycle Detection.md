---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-013]]"
confidence: high
supports:
  - "[[Bellman-Ford Algorithm]]"
  - "[[Negative Cycles]]"
qna_seeds:
  - "Q: How does Bellman-Ford detect negative cycles? A: Run a Vth round of relaxation; if any distance value decreases, a negative-weight cycle reachable from the source exists."
---

# Bellman-Ford Negative Cycle Detection

Bellman-Ford detects negative-weight cycles by running one additional (Vth) round of relaxation after the standard V − 1 rounds: if any distance value decreases, a negative cycle exists reachable from the source. This capability has direct applications in financial arbitrage (detecting profitable currency exchange loops) and in network flow algorithms where residual graph edges can be negative.