---
tags: [cs-ds, chunk]
id: chunk-ds-103
source: "[[raw-ds-028]]"
supports: ["[[Collision Resolution Strategies]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Backward-shift deletion avoids tombstones in open addressing

## Context
Tombstones waste space and slow lookups in open-addressing hash tables.

## Claim
Backward-shift deletion fills the gap by shifting subsequent entries backward toward their ideal positions. This eliminates tombstones entirely maintaining probe chain integrity without dead slots.

## Why It Matters
Used in Robin Hood and Swiss Table implementations. Keeps load factor meaningful and avoids table pollution.

## QnA Seeds
- Q: How does backward shift work? -> A: After removing an entry shift subsequent entries back if they are displaced from ideal.
- Q: When to stop shifting? -> A: When reaching an empty slot or an entry already at its ideal position.
