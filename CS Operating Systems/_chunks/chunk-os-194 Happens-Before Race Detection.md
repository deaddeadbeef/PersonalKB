---
id: chunk-csos-194
type: chunk
source: "[[raw-os-036]]"
source_loc: "Concurrency Bugs and Detection"
topic: "synchronization"
claim: "Happens-before analysis defines a partial order on thread events: concurrent accesses with at least one write constitute a data race, forming the theoretical basis for tools like ThreadSanitizer"
confidence: verified
supports:
  - "[[Concurrency Bugs]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Happens-before underpins race detection tools

## Context

The happens-before relation (Lamport 1978) orders events through synchronization: lock release happens-before lock acquire, thread create happens-before first instruction. Events with no happens-before relation are concurrent. ThreadSanitizer uses shadow memory and vector clocks to track this, detecting races with 5-15x overhead and 2x memory overhead. The -fsanitize=thread flag enables it in GCC and Clang.

## Why It Matters

Happens-before is the theoretical foundation of all modern race detectors. Understanding it explains what ThreadSanitizer actually checks, why it can have false negatives (missed orderings), and why the 5-15x overhead makes it suitable for testing but not production.

## QnA Seeds

- Q: What does the happens-before relation define between thread events?
- Q: How does ThreadSanitizer use happens-before for race detection?
- Q: What overhead does ThreadSanitizer impose and why?
