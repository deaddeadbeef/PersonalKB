---
id: chunk-csos-007
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "processes"
claim: "A process cycles through running, ready, and blocked states; transitions are triggered by scheduler decisions, I/O requests, and I/O completion events"
confidence: verified
supports:
  - "[[Process States and Transitions]]"
  - "[[Process Model]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Process states form a three-state lifecycle driven by scheduler and IO events

## Context

At any moment a process is in exactly one of three states. Running: actually executing on a CPU right now. Ready: able to run, waiting for the scheduler to assign a CPU. Blocked: waiting for an external event (disk read to complete, semaphore to become available). The scheduler moves processes from ready to running; I/O requests move running processes to blocked; I/O completions move blocked processes back to ready.

## Why It Matters

Understanding the state machine is essential for reasoning about scheduling, throughput, and latency. A CPU-bound process spends most time Running ↔ Ready. An I/O-bound process spends most time Blocked. The mix of process types determines optimal scheduling policy (MLFQ keeps I/O-bound processes at high priority naturally because they always yield quickly).

## QnA Seeds

- Q: Name the three process states and the event that causes each transition.
- Q: What is the difference between a blocked and a ready process?
- Q: Why does an I/O-bound process tend to get scheduled with lower latency than a CPU-bound one in a MLFQ?
