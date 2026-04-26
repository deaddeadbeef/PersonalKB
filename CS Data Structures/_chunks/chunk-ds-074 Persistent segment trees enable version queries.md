---
tags: [cs-ds, chunk]
id: chunk-ds-074
source: "[[raw-ds-013]]"
supports: ["[[Segment Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Persistent segment trees enable version queries in Ologn extra space

## Context
Standard segment trees cannot answer queries about historical states.

## Claim
Persistent segment trees use path copying to create new versions sharing unchanged nodes. Each update costs O(log n) extra nodes enabling queries on any past version.

## Why It Matters
Essential for offline algorithms and competitive programming problems with version queries.

## QnA Seeds
- Q: How much space per update? -> A: O(log n) new nodes created via path copying.
- Q: Can you query any version? -> A: Yes by keeping the root pointer of each version.
