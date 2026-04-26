---
id: chunk-csos-192
type: chunk
source: "[[raw-os-036]]"
source_loc: "Concurrency Bugs and Detection"
topic: "synchronization"
claim: "Data races are necessary but not sufficient for most concurrency bugs — atomicity violations can occur even when individual accesses are properly synchronized but compound operations are not"
confidence: verified
supports:
  - "[[Concurrency Bugs]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Data races necessary but not sufficient for bugs

## Context

A data race occurs when two threads access the same memory concurrently, at least one writes, and no synchronization orders the accesses. However, some races are benign, while some bugs occur without data races: individual accesses may be locked but the compound operation (read-then-modify) is unprotected. This distinction matters for detection tools.

## Why It Matters

Understanding this subtlety prevents false confidence from race-free code. A program can pass ThreadSanitizer (which detects data races) yet still have atomicity violations. This insight drives the need for higher-level correctness specifications beyond data-race freedom.

## QnA Seeds

- Q: Why are data races necessary but not sufficient for concurrency bugs?
- Q: Can a program with no data races still have concurrency bugs?
- Q: How do atomicity violations differ from simple data races?
