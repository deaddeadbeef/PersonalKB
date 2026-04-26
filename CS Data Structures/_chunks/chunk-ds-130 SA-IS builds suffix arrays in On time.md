---
tags: [cs-ds, chunk]
id: chunk-ds-130
source: "[[raw-ds-027]]"
supports: ["[[Suffix Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# SA-IS builds suffix arrays in O(n) time via induced sorting

## Context
Early suffix array construction required O(n log n) or O(n log^2 n) time.

## Claim
The SA-IS algorithm builds suffix arrays in O(n) time and O(n) space by classifying suffixes as S-type or L-type then using induced sorting. It is both theoretically optimal and practically fast.

## Why It Matters
Made suffix arrays competitive with suffix trees for construction time while using much less space.

## QnA Seeds
- Q: What are S-type and L-type suffixes? -> A: S if lexicographically smaller than next suffix. L if larger.
- Q: Why is induced sorting key? -> A: Placing a few seed suffixes correctly induces correct positions of all others.
