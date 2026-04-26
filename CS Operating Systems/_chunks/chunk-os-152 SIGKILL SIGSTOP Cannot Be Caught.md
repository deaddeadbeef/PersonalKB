---
id: chunk-csos-152
type: chunk
source: "[[raw-os-026]]"
source_loc: "Signals and Signal Handling"
topic: "processes"
claim: "SIGKILL (9) and SIGSTOP are the only two signals that cannot be caught, blocked, or ignored, ensuring the kernel always retains the ability to forcibly terminate or pause any process"
confidence: verified
supports:
  - "[[Signals and IPC]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — SIGKILL and SIGSTOP cannot be caught or blocked

## Context

SIGKILL forces immediate process termination and SIGSTOP pauses a process unconditionally. Unlike SIGTERM (a polite termination request that processes can handle for cleanup) or SIGINT (keyboard interrupt), these two signals bypass all handler registration and signal masks. This guarantees the kernel can always control runaway or unresponsive processes.

## Why It Matters

The uncatchable nature of SIGKILL and SIGSTOP is a deliberate security and reliability design: no userspace process can make itself unkillable. This is why `kill -9` is the last resort for stuck processes and why SIGSTOP is used for job control.

## QnA Seeds

- Q: Which two Unix signals cannot be caught, blocked, or ignored?
- Q: Why is it important that SIGKILL cannot be handled by processes?
- Q: What is the difference between SIGTERM and SIGKILL?
