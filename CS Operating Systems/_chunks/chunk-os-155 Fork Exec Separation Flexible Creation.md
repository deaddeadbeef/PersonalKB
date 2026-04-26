---
id: chunk-csos-155
type: chunk
source: "[[raw-os-027]]"
source_loc: "Process Creation: fork/exec Model"
topic: "processes"
claim: "Unix separates process creation (fork) from program execution (exec), enabling the child to modify file descriptors, signals, and environment between the two calls"
confidence: verified
supports:
  - "[[Process Creation]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Fork-exec separation enables flexible process creation

## Context

fork() creates a child that is a near-exact copy of the parent (same address space, file descriptors, signal dispositions). The child differs only in PID, PPID, and fork return value (0 in child, child PID in parent). Between fork and exec, the child can redirect file descriptors, change signal handling, or modify its environment before loading a new program via execve().

## Why It Matters

This separation is what makes shell I/O redirection, piping, and privilege management possible. The child opens a file, dup2s it onto stdout, then execs the command — a pattern impossible with Windows' combined CreateProcess() model.

## QnA Seeds

- Q: Why does Unix separate process creation from program execution?
- Q: What can a child process do between fork() and exec()?
- Q: How does fork/exec enable shell I/O redirection?
