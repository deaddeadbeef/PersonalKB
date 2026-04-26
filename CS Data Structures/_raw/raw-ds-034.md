---
tags: [cs-ds, raw]
id: raw-ds-034
source: "Various (rope literature, Boehm et al. 1995)"
up: "[[CS Data Structures]]"
---

# Rope Data Structure for Strings

## Key Ideas
- Rope: balanced binary tree of string fragments (leaves hold short strings)
- Concatenation: O(1) — create new root with left and right subtrees
- Split: O(log n) — split at position by traversing tree
- Insert: split + concatenate — O(log n)
- Delete: two splits + concatenate — O(log n)
- Character access: O(log n) — traverse tree using subtree lengths
- vs String/StringBuilder: strings are O(n) for insert/delete, ropes are O(log n)
- Rebalancing: Fibonacci-based length thresholds or periodic rebuild
- Memory: overhead per node, but avoids copying on mutation
- Used in: text editors (Xi editor, VS Code exploration), Cedar/Mesa at Xerox PARC
- Gap buffer: alternative for text editing — single array with gap at cursor position
- Piece table: another alternative — table of pieces pointing into original + add buffers (VS Code uses this)

## Trade-offs
- Rope: best for frequent large insertions/deletions in middle of long strings
- String/array: best for short strings or mostly sequential access
- Gap buffer: best for single-cursor editing (simple, cache-friendly)
