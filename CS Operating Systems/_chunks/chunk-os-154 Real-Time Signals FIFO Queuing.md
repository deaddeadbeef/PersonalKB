---
id: chunk-csos-154
type: chunk
source: "[[raw-os-026]]"
source_loc: "Signals and Signal Handling"
topic: "processes"
claim: "Real-time signals (SIGRTMIN to SIGRTMAX) guarantee FIFO delivery ordering and queuing, addressing standard signals' limitation where multiple pending instances coalesce into one"
confidence: verified
supports:
  - "[[Signals and IPC]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Real-time signals guarantee FIFO queuing

## Context

Standard signals are not queued — if the same signal is pending multiple times, only one instance is delivered. Real-time signals fix this by guaranteeing FIFO delivery, supporting queuing of multiple instances, and allowing integer or pointer payloads via sigqueue(). The signalfd() interface converts signals into file descriptor events, enabling synchronous handling in event loops and avoiding reentrancy complications of async handlers.

## Why It Matters

Real-time signals and synchronous signal handling (signalfd) represent the evolution toward safer concurrency. Understanding why standard signals lose information (coalescing) explains bugs in programs that rely on signal counting.

## QnA Seeds

- Q: How do real-time signals differ from standard signals in delivery guarantees?
- Q: What problem does signal coalescing cause for standard signals?
- Q: How does signalfd enable synchronous signal handling in event loops?
