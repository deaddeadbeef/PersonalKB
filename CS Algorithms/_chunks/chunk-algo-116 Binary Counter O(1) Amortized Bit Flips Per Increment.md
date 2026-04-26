---
id: chunk-algo-116
type: chunk
source: "[[raw-algo-019]]"
source_loc: "Amortized Analysis - Atomic Facts"
topic: "amortized-analysis"
claim: "Incrementing an n-bit binary counter costs O(1) amortized bit flips because bit i flips every 2^i increments; total flips over n increments = sum of floor(n/2^i) < 2n, giving amortized cost < 2 per increment."
confidence: verified
supports:
  - "[[Amortized Analysis]]"
tags:
  - cs-algorithms
  - cs-algorithms/amortized-analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Binary Counter O(1) Amortized Bit Flips Per Increment

## Context

By the aggregate method: bit 0 flips n times, bit 1 flips n/2 times, bit 2 flips n/4 times, etc. Total = n + n/2 + n/4 + ... < 2n. The accounting method charges $2 per increment: $1 for flipping 0->1, $1 banked for the future 1->0 flip. Since each bit flipping back to 0 pays with stored credit, total cost is covered. This is the canonical introductory example for all three amortized methods.

## Why It Matters

The binary counter is the simplest complete example of amortized analysis, cleanly illustrating aggregate, accounting, and potential methods on one problem. The geometric series argument generalizes to any doubling structure.

## QnA Seeds

- Q: How many total bit flips occur over n increments?
- Q: How does the accounting method prove O(1) amortized per increment?
- Q: Why does bit i flip exactly floor(n/2^i) times?