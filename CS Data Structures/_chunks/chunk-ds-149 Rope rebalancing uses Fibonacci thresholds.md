---
tags: [cs-ds, chunk]
id: chunk-ds-149
source: "[[raw-ds-034]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Rope rebalancing uses Fibonacci thresholds from Boehm 1995

## Context
Without rebalancing ropes can degenerate into long chains.

## Claim
Boehm 1995 defined rope balance by Fibonacci length thresholds: a rope of depth d is balanced if length >= F(d+2). Rebalancing flattens and rebuilds when violated ensuring O(log n) depth.

## Why It Matters
The original rope paper's rebalancing strategy is still used in modern implementations like libcord.

## QnA Seeds
- Q: Why Fibonacci thresholds? -> A: They mirror the worst-case structure of concatenation trees analogous to Fibonacci heaps.
- Q: How is rebalancing done? -> A: Collect all leaves flatten into array then rebuild balanced tree.
