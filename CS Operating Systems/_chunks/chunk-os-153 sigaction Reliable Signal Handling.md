---
id: chunk-csos-153
type: chunk
source: "[[raw-os-026]]"
source_loc: "Signals and Signal Handling"
topic: "processes"
claim: "sigaction() provides reliable signal handling by keeping handlers installed across deliveries and allowing atomic signal mask specification, replacing the racy signal() function"
confidence: verified
supports:
  - "[[Signals and IPC]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — sigaction provides reliable signal handling

## Context

The original signal() function reset the handler to default after each delivery, creating a race window where a second signal could arrive before the handler was reinstalled. POSIX sigaction() fixes this: the handler remains installed, and the sa_mask field specifies which signals to block during handler execution. Signal masks via sigprocmask() allow temporarily blocking signals during critical sections.

## Why It Matters

The unreliable-to-reliable signal evolution is a textbook example of race condition elimination. Using sigaction() instead of signal() is mandatory for correct concurrent programs, and understanding sa_mask explains how to write safe signal handlers.

## QnA Seeds

- Q: What race condition exists in the original signal() function?
- Q: How does sigaction() fix the unreliable signal handling problem?
- Q: What role does sa_mask play in signal handler safety?
