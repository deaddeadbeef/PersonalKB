---
tags: [cs-ds, chunk]
id: chunk-ds-011
source: "[[raw-ds-007]]"
supports: ["[[Collision Resolution Strategies]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Robin Hood hashing reduces probe variance by stealing from rich

## Context
In open addressing, some keys have much longer probe sequences than others.

## Claim
Robin Hood hashing displaces existing keys with shorter probe distances during insertion, ensuring no key is much farther from its ideal position than any other.

## Why It Matters
This dramatically reduces worst-case lookup time in open-addressing hash tables.

## QnA Seeds
- Q: How does Robin Hood hashing work? -> A: New key with longer displacement swaps with occupant having shorter displacement.
- Q: What metric determines displacement? -> A: Probe distance from originally hashed position.
