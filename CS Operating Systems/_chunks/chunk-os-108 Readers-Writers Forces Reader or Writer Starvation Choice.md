---
id: chunk-csos-108
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Classic Synchronization Problems"
topic: "synchronization"
claim: "The readers-writers problem has two standard variants: the first gives readers priority (writers may starve indefinitely), the second gives writers priority (readers may starve) — no solution simultaneously prevents starvation for both without additional fair-queuing mechanisms"
confidence: verified
supports:
  - "[[Classic Synchronization Problems]]"
  - "[[Synchronization Overview]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Readers-writers forces a choice between reader and writer starvation

## Context

The readers-writers problem allows multiple concurrent readers but requires exclusive writer access. In the first variant (reader priority), readers maintain a read_count protected by a mutex; the first reader locks the resource and the last unlocks it. While any readers are active, writers are blocked indefinitely — a continuous stream of readers starves writers. The second variant reverses this: once a writer is waiting, new readers are blocked, potentially starving them. Fair solutions exist (e.g., using a FIFO turnstile that alternates between accumulated readers and writers) but add complexity.

## Why It Matters

This tradeoff governs database locking strategies directly: shared locks (readers) vs. exclusive locks (writers). PostgreSQL's MVCC and Java's ReadWriteLock both address this fundamental tension. Understanding which variant is implemented reveals the system's bias toward read throughput or write freshness.

## QnA Seeds

- Q: Why can't a single solution prevent both reader and writer starvation?
- Q: How does the first readers-writers solution cause writer starvation?
- Q: How does this problem relate to database shared/exclusive locking?
