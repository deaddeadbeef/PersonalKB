---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "System Calls and API"
authors: Silberschatz, Galvin, Gagne; Tanenbaum, Bos
year: 2018
---

# System Calls and API

## Summary

System calls are the programmatic interface through which user-space processes request services from the operating system kernel. They represent the boundary between user mode and kernel mode—the two privilege levels enforced by hardware. In user mode, a process cannot directly access hardware, modify page tables, or execute privileged instructions. When a process needs to perform a privileged operation (file I/O, process creation, network access), it issues a system call that triggers a mode switch into kernel mode.

On x86 architectures, the traditional mechanism uses the `int 0x80` software interrupt (Linux) or `sysenter`/`syscall` instructions for faster entry. The process places the system call number in a register (e.g., `eax` on x86) and arguments in additional registers (`ebx`, `ecx`, `edx`, `esi`, `edi`) or on the stack. The trap instruction switches to kernel mode and transfers control to the system call handler, which indexes into a system call table (an array of function pointers) to dispatch the appropriate kernel function. After execution, the kernel places the return value in a register and returns to user mode.

Linux defines over 400 system calls. The most fundamental include: `read()` and `write()` for I/O, `open()` and `close()` for file descriptor management, `fork()` for process creation, `execve()` for program execution, `wait()`/`waitpid()` for process synchronization, `mmap()` for memory mapping, `ioctl()` for device control, and `socket()`/`bind()`/`listen()`/`accept()` for networking. The POSIX standard defines a portable subset of these interfaces, ensuring that programs written against POSIX APIs compile and behave consistently across compliant operating systems (Linux, macOS, BSDs).

User-space programs rarely invoke system calls directly. Instead, they call wrapper functions in the C library (glibc on Linux), which handle argument marshaling, invoke the appropriate trap instruction, check error return values, and set `errno`. The `strace` utility traces all system calls made by a process, providing a powerful debugging and profiling tool. The vDSO (virtual dynamic shared object) optimization maps frequently-called, read-only kernel data into user space, allowing calls like `gettimeofday()` to execute without an actual mode switch.

## Key Claims

- System calls are the only legal mechanism for user-space processes to request kernel services, enforced by hardware privilege levels that prevent direct access to privileged operations
- The trap instruction atomically switches from user mode to kernel mode and transfers control to the kernel's system call dispatcher, which uses a system call table for routing
- POSIX standardizes a portable system call API that enables source-level compatibility across conforming Unix-like operating systems
- The C library provides wrapper functions that abstract the raw system call mechanism, handling register setup, trap invocation, and error propagation transparently
- The vDSO optimization eliminates kernel mode transitions for frequently-called read-only operations like time queries, reducing overhead from ~1 μs to ~20 ns

## Atomic Facts

1. The x86-64 `syscall` instruction is faster than `int 0x80` because it avoids the overhead of interrupt descriptor table lookup, reducing entry cost to approximately 100–200 cycles
2. Linux assigns each system call a unique number: `read` is 0, `write` is 1, `open` is 2, `close` is 3, `fork` is 57, `execve` is 59 on x86-64
3. The system call table on Linux x86-64 is defined in `arch/x86/entry/syscall_64.c` and maps numbers to kernel function pointers
4. `strace -c` provides a statistical summary of system call counts and time consumed, useful for identifying I/O bottlenecks
5. `errno` is a thread-local variable in glibc, ensuring that system call error codes from one thread do not interfere with another
6. The POSIX standard defines approximately 200 interfaces covering process control, file operations, signals, IPC, and threading (pthreads)

## Significance

System calls are the fundamental abstraction boundary in operating systems—the contract between user programs and the kernel. Every higher-level API, library, and framework ultimately reduces to system calls. Understanding this interface is essential for performance optimization (minimizing mode switches), security analysis (system call filtering via seccomp), and debugging (strace-driven diagnosis). The design of the system call interface also illustrates the mechanism-vs-policy separation principle.

## Chunks Extracted

*Pending*
