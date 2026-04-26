---
tags: [cs-ds, chunk]
id: chunk-ds-003
source: "[[raw-ds-002]]"
supports: ["[[Singly Linked Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Floyd's algorithm detects linked list cycles in O(n) time O(1) space

## Context
Cycle detection in linked lists is a classic problem.

## Claim
Floyd's tortoise-and-hare uses two pointers at different speeds; if a cycle exists they meet, detecting it in O(n) time and O(1) space.

## Why It Matters
This elegant algorithm avoids the naive O(n) space approach of tracking visited nodes.

## QnA Seeds
- Q: How does Floyd's cycle detection work? -> A: Slow pointer advances 1 step, fast 2 steps; if they meet, there is a cycle.
- Q: Can it find the cycle start? -> A: Yes -- reset one pointer to head, advance both at speed 1; they meet at cycle entry.
