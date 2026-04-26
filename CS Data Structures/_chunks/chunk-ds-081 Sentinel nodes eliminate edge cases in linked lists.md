---
tags: [cs-ds, chunk]
id: chunk-ds-081
source: "[[raw-ds-002]]"
supports: ["[[Singly Linked Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Sentinel nodes eliminate edge cases in linked list operations

## Context
Linked list insert and delete require special handling for head and tail.

## Claim
Adding a dummy sentinel node that is always present eliminates null checks for empty lists and boundary cases reducing code complexity and bugs without affecting asymptotic performance.

## Why It Matters
Used in Linux kernel linked lists and Java LinkedList. Simplifies implementation significantly.

## QnA Seeds
- Q: What is a sentinel node? -> A: Dummy node always present that simplifies boundary conditions.
- Q: Does it waste memory? -> A: One extra node per list is negligible for all practical use cases.
