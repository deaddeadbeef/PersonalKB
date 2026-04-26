---
tags: [cs-ds, chunk]
id: chunk-ds-151
source: "[[raw-ds-001]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Memory alignment constraints affect struct layout and padding

## Context
CPUs access memory most efficiently at aligned addresses.

## Claim
Struct fields are padded to satisfy alignment requirements (typically natural alignment: 4-byte int on 4-byte boundary). This can cause significant hidden memory waste that reordering fields can eliminate.

## Why It Matters
A struct with char, double, char could use 24 bytes instead of 10 due to padding. Field ordering matters.

## QnA Seeds
- Q: What is natural alignment? -> A: An n-byte type must start at an address divisible by n.
- Q: How to minimize padding? -> A: Order fields from largest to smallest alignment requirement.
