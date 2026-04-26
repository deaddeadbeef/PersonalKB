---
id: chunk-csos-210
type: chunk
source: "[[raw-os-040]]"
source_loc: "Kernel Synchronization Primitives"
topic: "synchronization"
claim: "Seqlocks favor writers by using a sequence counter that writers increment before and after writing; readers retry if the counter changed, meaning writers never block even with active readers"
confidence: verified
supports:
  - "[[Kernel Synchronization]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Seqlocks favor writers via sequence counter retry

## Context

A seqlock writer increments a sequence counter before and after writing. Readers read the counter before and after their read, retrying if it changed (indicating concurrent write). Writers never block, even with active readers. Linux uses seqlocks for jiffies (timer tick count) and xtime (wall-clock time) where timer interrupts write frequently but many consumers need consistent timestamps. Memory barriers (mb, rmb, wmb, smp_mb) enforce ordering for correctness.

## Why It Matters

Seqlocks solve the specific problem of protecting data written rarely by high-priority writers (interrupts) and read frequently by lower-priority threads. Understanding the retry mechanism explains how the kernel maintains consistent time values without ever blocking timer interrupts.

## QnA Seeds

- Q: How does the seqlock sequence counter mechanism work?
- Q: Why do seqlocks favor writers over readers?
- Q: What kernel data is protected by seqlocks and why?
