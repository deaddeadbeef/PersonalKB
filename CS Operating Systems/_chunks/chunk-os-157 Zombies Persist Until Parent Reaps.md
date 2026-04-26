---
id: chunk-csos-157
type: chunk
source: "[[raw-os-027]]"
source_loc: "Process Creation: fork/exec Model"
topic: "processes"
claim: "A terminated child becomes a zombie retaining only PID and exit status until the parent calls wait/waitpid; failing to reap children leaks process table entries"
confidence: verified
supports:
  - "[[Process Creation]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Zombie processes persist until parent reaps

## Context

When a child terminates, it becomes a zombie (status Z in ps) — its exit status is retained in the process table but it holds no memory or file descriptors. The parent must call wait() or waitpid() to retrieve the exit status and free the entry. Accumulating zombies wastes process table entries and can exhaust the system's PID space in long-running server processes.

## Why It Matters

Zombie accumulation is a classic resource leak in server programming. Understanding the zombie mechanism explains why SIGCHLD handling matters, why ignoring SIGCHLD auto-reaps on Linux, and why orphans are reparented to init.

## QnA Seeds

- Q: What resources does a zombie process retain?
- Q: How does a parent process reap a zombie?
- Q: What happens if a server process never calls wait() on its children?
