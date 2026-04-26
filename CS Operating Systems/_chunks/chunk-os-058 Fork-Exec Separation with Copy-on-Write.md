---
tags: [cs-os, chunk]
source: "[[raw-os-002]]"
confidence: high
supports:
  - "[[Process Management]]"
  - "[[Unix Design]]"
qna_seeds:
  - "Q: Why does Unix separate fork() from exec(), and how does copy-on-write optimize this? A: Separation enables composition patterns like I/O redirection and piping between fork and exec. COW defers page duplication until a write occurs, making fork() nearly instantaneous regardless of address space size."
---

# Fork-Exec Separation with Copy-on-Write

The Unix fork() system call creates a child process by duplicating the parent's address space (child gets return value 0, parent gets child's PID), while exec() replaces the current process image with a new program, preserving PID and open file descriptors. This separation enables powerful composition patterns like I/O redirection and shell pipelines. Modern systems use copy-on-write (COW) optimization: fork() shares all pages as read-only, deferring actual page duplication until either process writes, making fork() nearly instantaneous.
