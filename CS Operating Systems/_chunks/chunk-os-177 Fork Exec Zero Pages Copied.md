---
id: chunk-csos-177
type: chunk
source: "[[raw-os-032]]"
source_loc: "Copy-on-Write Mechanism"
topic: "memory"
claim: "In the common fork+exec pattern, COW ensures zero data pages are physically copied because exec discards the entire child address space before any writes occur"
confidence: verified
supports:
  - "[[Copy-on-Write]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Fork-exec copies zero pages due to COW

## Context

When fork() is immediately followed by exec(), the child replaces its entire address space with the new program. Since no writes happen to the shared pages before exec, no COW faults are triggered and zero data pages are physically duplicated. Only the page table entries themselves (a few KB) are copied during fork. This makes fork+exec nearly free regardless of parent process size.

## Why It Matters

This is the key insight that makes Unix process creation practical: a multi-gigabyte web server can fork+exec a child process with negligible overhead. It also explains why vfork() (created before COW existed) is now largely obsolete.

## QnA Seeds

- Q: Why does fork+exec result in zero physical page copies with COW?
- Q: What is actually duplicated during a COW fork if exec follows immediately?
- Q: Why did COW make vfork() largely unnecessary?
