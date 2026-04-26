---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Process Creation: fork/exec Model"
authors: Silberschatz, Galvin, Gagne; Stevens, Rago
year: 2018
---

# Process Creation: fork/exec Model

## Summary

The Unix process creation model separates process duplication from program execution into two distinct system calls: `fork()` and `exec()`. This separation is a fundamental Unix design decision that provides maximum flexibility—between fork and exec, the child process can modify its file descriptors, signal handlers, environment, or other attributes before loading a new program.

`fork()` creates a new child process that is a near-exact copy of the parent. The child receives a copy of the parent's address space, open file descriptors, signal dispositions, and environment variables. The only differences are the PID (new for child), PPID (set to parent's PID), and the return value of fork itself (0 in child, child's PID in parent). Modern implementations use copy-on-write (COW) semantics: rather than physically duplicating all memory pages, both processes share the same physical pages marked read-only. Only when either process writes to a page is a physical copy made, dramatically reducing fork overhead.

The `exec()` family of functions (execve, execvp, execlp, execl, execv, execle) replaces the current process image with a new program. `execve()` is the underlying system call; the others are library wrappers. After exec, the process retains its PID and open file descriptors (unless marked `FD_CLOEXEC`) but receives a fresh address space loaded from the new executable.

When a child process terminates, it becomes a zombie—its exit status is retained in the process table until the parent calls `wait()` or `waitpid()`. If the parent terminates first, the child becomes an orphan, which is reparented to PID 1 (init/systemd), which periodically reaps zombies. Accumulating zombies wastes process table entries and can exhaust the system's PID space.

`vfork()` was an optimization predating COW: it shared the parent's address space directly with the child and suspended the parent until the child called exec or _exit. It is now largely obsolete because COW fork is nearly as efficient without the dangerous address space sharing. Windows uses a different model: `CreateProcess()` combines process creation and program loading into a single API call, making the fork/exec separation unavailable.

## Key Claims

- Unix separates process creation (fork) from program execution (exec), enabling the child to modify its execution context between the two calls—a design pattern that underpins shell I/O redirection, piping, and privilege management
- Copy-on-write makes fork() nearly free regardless of process size because physical page copying is deferred until a write occurs, reducing fork from O(n) to approximately O(1) in the common fork+exec case
- Zombie processes consume process table entries until reaped by the parent via wait/waitpid; failure to reap children is a common resource leak in long-running server processes
- Orphaned processes are reparented to init (PID 1), which is responsible for reaping them, preventing permanent zombie accumulation
- Windows' CreateProcess() model is fundamentally different from Unix fork/exec, combining process creation and program loading into a single atomic operation without an intermediate fork state

## Atomic Facts

1. `fork()` returns 0 to the child process and the child's PID to the parent; a return value of -1 indicates failure (e.g., exceeding the per-user process limit)
2. `execve()` takes three arguments: the path to the executable, an argument vector (argv), and an environment vector (envp)
3. File descriptors without the `FD_CLOEXEC` flag survive across exec, which is how shells implement I/O redirection: open a file, dup2 it onto stdin/stdout, then exec the command
4. `waitpid(-1, &status, WNOHANG)` performs a non-blocking check for any terminated child, returning 0 if no child has exited
5. On Linux, `fork()` is implemented via the `clone()` system call with flags specifying which resources to share, making fork/vfork/threads all variants of the same underlying mechanism
6. A zombie process is visible in `ps` output with status `Z` and retains only its PID, exit status, and resource usage statistics—no memory pages or file descriptors

## Significance

The fork/exec model is one of the most consequential design decisions in Unix history. Its simplicity and composability enabled the Unix pipe-and-filter philosophy that became the foundation of shell scripting and process orchestration. Understanding fork/exec is essential for systems programming, shell implementation, container runtimes (which use clone with namespace flags), and comprehending how process isolation works in modern operating systems.

## Chunks Extracted

*Pending*
