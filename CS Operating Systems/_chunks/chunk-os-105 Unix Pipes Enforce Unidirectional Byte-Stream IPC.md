---
id: chunk-csos-105
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Inter-Process Communication"
topic: "processes"
claim: "Unix pipes enforce a simple unidirectional byte-stream protocol between related processes; named pipes (FIFOs) extend this to unrelated processes via a filesystem entry"
confidence: verified
supports:
  - "[[Interprocess Communication]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Unix pipes enforce unidirectional byte-stream IPC

## Context

Pipes are the original Unix IPC mechanism. An anonymous pipe created by pipe() returns two file descriptors (read end and write end) and works only between related processes — typically parent-child. The shell implements command pipelines (cmd1 | cmd2) by connecting stdout of cmd1 to stdin of cmd2 via a pipe. Named pipes (FIFOs), created with mkfifo(), place an entry in the filesystem that any process can open, extending the pipe abstraction to unrelated processes. Both enforce unidirectional, byte-stream semantics with no message boundaries.

## Why It Matters

Pipes embody the Unix philosophy of composing simple tools into complex pipelines. Their byte-stream abstraction is deliberately minimal — no message framing, no seek, no random access — which makes them universally composable but unsuitable for structured IPC where message boundaries matter (for which Unix domain sockets or message queues are used).

## QnA Seeds

- Q: What is the difference between anonymous pipes and named pipes (FIFOs)?
- Q: How does the shell implement cmd1 | cmd2 using pipe()?
- Q: Why are pipes unsuitable for structured message-based IPC?
