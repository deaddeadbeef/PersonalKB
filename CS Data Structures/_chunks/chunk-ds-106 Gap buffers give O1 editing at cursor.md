---
tags: [cs-ds, chunk]
id: chunk-ds-106
source: "[[raw-ds-034]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Gap buffers give O1 editing at cursor with O(n) worst-case cursor jump

## Context
Text editors need fast insert/delete at the cursor position.

## Claim
A gap buffer maintains a contiguous gap at the cursor position. Insert/delete at the cursor is O(1). Moving the cursor requires shifting the gap which is O(distance moved).

## Why It Matters
Used in Emacs. Extremely simple and cache-friendly for single-cursor editing where cursor movement is local.

## QnA Seeds
- Q: What is the gap? -> A: Unused space in the middle of the array at the cursor position.
- Q: Why fast at cursor? -> A: Insert just fills gap space. Delete extends the gap. No shifting needed.
