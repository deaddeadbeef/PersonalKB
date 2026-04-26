---
tags: [cs-ds, chunk]
id: chunk-ds-133
source: "[[raw-ds-033]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Alpha parameter in scapegoat trees controls rebalance frequency

## Context
Scapegoat tree balance tolerance is configurable.

## Claim
The alpha parameter (typically 0.55-0.75) sets the balance threshold. Smaller alpha means stricter balance with more frequent rebuilds. Larger alpha tolerates more imbalance with rarer but more expensive rebuilds.

## Why It Matters
Tunable trade-off between lookup speed and insertion cost unique among self-balancing BSTs.

## QnA Seeds
- Q: What is the height bound? -> A: height <= log_{1/alpha}(n). For alpha=0.5 this is log2(n).
- Q: Best alpha value? -> A: 2/3 is common. Gives height at most 1.71 log2(n) with moderate rebuild frequency.
