---
id: chunk-csos-149
type: chunk
source: "[[raw-os-025]]"
source_loc: "System Calls and API"
topic: "foundations"
claim: "POSIX standardizes approximately 200 portable system call interfaces covering processes, files, signals, IPC, and threading, enabling source-level compatibility across Unix-like operating systems"
confidence: verified
supports:
  - "[[System Calls]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — POSIX standardizes portable system call API

## Context

The POSIX standard defines ~200 interfaces ensuring that programs written against POSIX APIs compile and behave consistently across compliant systems (Linux, macOS, BSDs). Key calls include read/write for I/O, fork/execve for processes, mmap for memory mapping, and the socket family for networking. The C library (glibc) wraps these, handling argument marshaling and errno (a thread-local variable) for error reporting.

## Why It Matters

POSIX portability is why the same C program can compile on Linux, macOS, and FreeBSD. Understanding which interfaces are POSIX-standard vs. Linux-specific helps developers write portable code and explains why some features (epoll, signalfd) are Linux-only.

## QnA Seeds

- Q: What does POSIX standardize and why does it matter for portability?
- Q: How does the C library relate to raw system calls?
- Q: Why is errno thread-local in glibc?
