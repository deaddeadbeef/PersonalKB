---
id: chunk-csos-095
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 4 — ext4 and Linux File Systems"
topic: "file-systems"
claim: "Journaling (write-ahead logging) replaces the slow, incomplete fsck recovery process with fast journal replay that restores file system consistency in seconds regardless of volume size"
confidence: verified
supports:
  - "[[Journaling File Systems]]"
  - "[[File System Implementation]]"
tags:
  - csos
  - csos/file-systems
  - chunk
up: "[[CS Operating Systems]]"
---
# File Systems — Journaling replaces fsck with fast log replay for crash recovery

## Context

Before journaling, an unclean shutdown (power failure, kernel panic) left the file system in a potentially inconsistent state. Recovery required running fsck, which walks the entire file system metadata checking for corruption — a process that could take hours on large volumes. Journaling records intended metadata changes to a write-ahead log before committing them to their final on-disk locations. After a crash, the OS simply replays the journal (or discards incomplete transactions), restoring consistency in seconds regardless of how large the file system is.

## Why It Matters

Journaling transformed file system reliability from "hope it survives a crash" to a guaranteed recovery mechanism with bounded time. ext3 added journaling to Linux (2001) with three modes: journal (data + metadata logged, safest but slowest), ordered (metadata logged, data written before metadata commit — the default), and writeback (metadata only, fastest but risks stale data exposure). This design tradeoff between safety and performance persists in every journaling file system.

## QnA Seeds

- Q: Why was fsck inadequate for large file systems?
- Q: What are the three journaling modes in ext3 and what tradeoff does each make?
- Q: How does write-ahead logging guarantee crash consistency?
