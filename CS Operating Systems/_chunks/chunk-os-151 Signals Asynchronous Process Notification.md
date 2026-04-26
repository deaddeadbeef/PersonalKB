---
id: chunk-csos-151
type: chunk
source: "[[raw-os-026]]"
source_loc: "Signals and Signal Handling"
topic: "processes"
claim: "Signals are a software interrupt mechanism in Unix that notify processes of asynchronous events, with each signal triggering a registered handler, a default action, or being ignored"
confidence: verified
supports:
  - "[[Signals and IPC]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Signals provide asynchronous process notification

## Context

When a signal is delivered, the process either executes a registered handler, performs the default action (terminate, core dump, stop, or ignore), or ignores it if explicitly masked. Signals originate from the kernel (SIGSEGV for invalid memory access), other processes (via kill()), terminal input (Ctrl+C generates SIGINT), or the process itself (raise(), abort()). Linux defines 31 standard signals plus ~33 real-time signals.

## Why It Matters

Signals are one of the oldest IPC mechanisms in Unix and remain fundamental to process lifecycle management, job control, and error handling. Improper signal handling is a common source of race conditions, zombie processes, and security vulnerabilities.

## QnA Seeds

- Q: What are the three possible responses when a signal is delivered to a process?
- Q: What are the common sources of signals in Unix?
- Q: How many standard vs real-time signals does Linux define?
