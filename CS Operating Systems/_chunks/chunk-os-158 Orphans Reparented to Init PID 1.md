---
id: chunk-csos-158
type: chunk
source: "[[raw-os-027]]"
source_loc: "Process Creation: fork/exec Model"
topic: "processes"
claim: "Orphaned processes are reparented to init (PID 1), which periodically reaps them, preventing permanent zombie accumulation when parent processes terminate first"
confidence: verified
supports:
  - "[[Process Creation]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Orphans reparented to init PID 1

## Context

If a parent terminates before its children, the children become orphans and are automatically reparented to PID 1 (init or systemd). PID 1 is responsible for periodically calling wait() to reap these orphans, preventing permanent zombie accumulation. This design ensures the process table is eventually cleaned up regardless of application behavior.

## Why It Matters

The reparenting mechanism is a critical OS safety net. It explains why PID 1 has special responsibilities, why init/systemd must handle SIGCHLD, and why container init processes (like tini or dumb-init) exist to prevent zombie accumulation in containers.

## QnA Seeds

- Q: What happens to a child process when its parent terminates?
- Q: Why must PID 1 (init) periodically call wait()?
- Q: Why do containers often need a dedicated init process?
