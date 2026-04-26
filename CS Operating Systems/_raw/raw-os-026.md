---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Signals and Signal Handling"
authors: Kerrisk; Stevens, Rago
year: 2010
---

# Signals and Signal Handling

## Summary

Signals are a software interrupt mechanism in Unix/POSIX operating systems used to notify processes of asynchronous events. When a signal is delivered to a process, the process either executes a registered signal handler, performs the default action (terminate, core dump, stop, or ignore), or ignores the signal if it has been explicitly masked. Signals originate from various sources: the kernel (hardware exceptions like SIGSEGV for invalid memory access), other processes (via the `kill()` system call), terminal input (Ctrl+C generates SIGINT, Ctrl+Z generates SIGTSTP), or the process itself (e.g., `raise()` or `abort()`).

Key POSIX signals include: SIGINT (2, interrupt from keyboard), SIGTERM (15, polite termination request), SIGKILL (9, forced termination—cannot be caught or ignored), SIGSEGV (11, segmentation fault), SIGCHLD (17, child process status change), SIGSTOP (cannot be caught—pauses a process), SIGALRM (timer expiration), and SIGPIPE (write to a broken pipe). SIGKILL and SIGSTOP are the only two signals that cannot be caught, blocked, or ignored.

The original `signal()` function had unreliable semantics: the handler was reset to the default after each delivery, creating a race window. The POSIX `sigaction()` function replaced it with reliable semantics: the handler remains installed, and additional signals can be blocked during handler execution via the `sa_mask` field. Signal masks (manipulated via `sigprocmask()`) allow a process to temporarily block delivery of specific signals, which is essential for protecting critical sections from interruption.

Real-time signals (SIGRTMIN to SIGRTMAX) extend the standard signal model by guaranteeing delivery order (FIFO), supporting queuing (multiple instances are not lost), and allowing integer or pointer payloads via `sigqueue()`. Standard signals, by contrast, are not queued—if the same signal is pending multiple times, only one instance is delivered. The `sigwaitinfo()` and `signalfd()` interfaces allow synchronous signal handling, which is often preferred in event-driven architectures because it avoids the reentrancy complications of asynchronous signal handlers.

## Key Claims

- Signals provide an asynchronous notification mechanism that interrupts normal process execution, analogous to hardware interrupts but delivered by the kernel to user-space processes
- SIGKILL and SIGSTOP cannot be caught, blocked, or ignored, ensuring the kernel always retains the ability to forcibly terminate or pause any process
- The `sigaction()` interface provides reliable signal handling by keeping handlers installed across deliveries and allowing atomic specification of signal masks during handler execution
- Signal masks via `sigprocmask()` are essential for preventing race conditions in signal handlers by blocking specified signals during critical code regions
- Real-time signals guarantee FIFO delivery ordering and queuing, addressing the fundamental limitations of standard signals where multiple pending instances coalesce into one

## Atomic Facts

1. Linux defines 31 standard signals (1–31) plus typically 33 real-time signals (32–64), for a total of 64 signal numbers
2. SIGCHLD is sent to a parent process when a child terminates, stops, or resumes; ignoring SIGCHLD causes children to be automatically reaped without becoming zombies
3. The `sa_flags` field in `sigaction()` supports SA_RESTART (auto-restart interrupted system calls), SA_SIGINFO (three-argument handler with siginfo_t), and SA_NOCLDSTOP
4. Writing to a pipe or socket whose reading end is closed delivers SIGPIPE to the writing process; servers typically ignore SIGPIPE and handle EPIPE errors instead
5. Signal handlers must only call async-signal-safe functions (defined by POSIX); calling malloc(), printf(), or mutex operations from a signal handler risks deadlock or corruption
6. The `signalfd()` Linux-specific system call converts signals into file descriptor events, enabling integration with `select()`/`poll()`/`epoll()` event loops

## Significance

Signals are one of the oldest IPC mechanisms in Unix and remain fundamental to process lifecycle management, job control, and error handling. Understanding signal semantics is critical for writing correct concurrent programs—improper signal handling is a common source of race conditions, zombie processes, and security vulnerabilities. The evolution from unreliable to reliable signals and from asynchronous handlers to synchronous interfaces reflects the broader OS trend toward safer, more predictable concurrency primitives.

## Chunks Extracted

*Pending*
