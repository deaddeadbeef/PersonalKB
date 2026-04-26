---
tags: [cs-ds, chunk]
id: chunk-ds-122
source: "[[raw-ds-002]]"
supports: ["[[Singly Linked Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Intrusive linked lists embed link pointers inside the element struct

## Context
Standard linked lists allocate separate node wrappers around each element.

## Claim
Intrusive linked lists place next/prev pointers directly inside the data structure element eliminating per-node allocation overhead and improving cache locality. Elements can belong to multiple lists simultaneously.

## Why It Matters
Used extensively in Linux kernel (list_head macro) and real-time systems where allocation overhead is unacceptable.

## QnA Seeds
- Q: What is the Linux list_head? -> A: Circular doubly-linked list embedded in structs via list_head member.
- Q: Main disadvantage? -> A: Elements can only be in one list per embedded list_head field.
