---
tags:
  - csos
  - csos/foundations
confidence: verified
up: "[[OS Foundations Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# System Calls

> **One-line summary**: A system call is the controlled trap mechanism through which user-space programs request privileged services from the OS kernel.

## 🎯 Intuition
**The Core Idea:** System calls are the only legal doorway from your program into the kernel — every file read, process creation, and memory mapping goes through this gate.
**Analogy:** Imagine a bank vault (kernel) with a service window (system call interface). Customers (programs) can't walk into the vault — they fill out a form at the window, the teller (trap handler) validates it, does the work inside, and slides the result back out.
**Why It Matters:** Without system calls, programs could directly manipulate hardware and each other's memory — there would be no security, no isolation, and no stability.

---

## ⚙️ Core Mechanics
### How It Works
A **system call** is the controlled mechanism through which a user-space program requests a service from the operating system kernel. Because the kernel runs in a privileged CPU mode that user programs cannot access directly, the hardware provides a software-interrupt or trap instruction that transfers control to a pre-defined kernel entry point.

#### The Trap Mechanism
1. User program executes a special instruction (e.g., `syscall` on x86-64, `svc` on ARM).
2. The CPU switches from user mode to kernel mode and jumps to the kernel's trap handler.
3. The kernel reads the system call number and arguments from registers.
4. The kernel performs the requested service and returns the result.
5. Control returns to user mode; the instruction after the trap resumes.

This means user code can *never* directly issue disk writes or manipulate another process's memory — it must always ask the kernel, which validates the request.

### Key Concepts / Operations

| Call | Purpose |
|------|---------|
| `open(path, flags)` | Open a file; returns a file descriptor |
| `read(fd, buf, n)` | Read up to n bytes from an open file |
| `write(fd, buf, n)` | Write n bytes to an open file |
| `fork()` | Create a child process that is a copy of the caller |
| `exec(path, args)` | Replace the calling process image with a new program |
| `wait(status)` | Block until a child process exits |
| `exit(code)` | Terminate the calling process |
| `mmap(addr, len, …)` | Map a file or anonymous memory into the address space |
| `kill(pid, sig)` | Send a signal to a process |

### Key Facts
- System calls cross the user/kernel privilege boundary — this is their defining characteristic.
- A C library function like `printf` is *not* a system call — it is a library wrapper that may internally invoke `write`.
- Library calls are cheap (nanoseconds); system calls carry significant overhead (hundreds of nanoseconds) due to the mode switch.
- The system call number (e.g., `read` = 0 on Linux x86-64) indexes into the kernel's syscall dispatch table.

---

## 🔬 Deep Dive
### Implementation Details
- **x86-64 Linux convention**: Syscall number in `rax`; arguments in `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9`. The `syscall` instruction saves `rip` to `rcx` and `rflags` to `r11`, then jumps to the kernel entry point at `MSR_LSTAR`.
- **ARM64 convention**: Syscall number in `x8`; arguments in `x0`–`x5`. The `svc #0` instruction traps to EL1 (kernel exception level).
- **vDSO (virtual Dynamic Shared Object)**: Linux maps a kernel-provided shared library into every process's address space containing frequently-used calls (`gettimeofday`, `clock_gettime`) that can execute without a full trap — reading kernel-maintained memory from user space.
- **Spectre/Meltdown mitigations**: KPTI (Kernel Page Table Isolation) unmaps most kernel memory from user-space page tables, adding TLB flush overhead to every system call (~100–400 ns extra).

### Edge Cases and Pitfalls
- **EINTR**: A system call blocked on I/O can be interrupted by a signal; the caller must check for `EINTR` and retry.
- **TOCTOU races**: Checking a file's permissions then opening it is two syscalls — the file can change between them. Use `openat()` with flags for atomic checks.
- **Syscall overhead accumulation**: A naïve file copy doing 1-byte `read`/`write` calls makes millions of syscalls. Buffered I/O (`fread`/`fwrite`) or `sendfile()` drastically reduces crossings.

### Real-World Systems
- **Linux**: ~450 syscalls (v6.x); uses `syscall` instruction on x86-64, `svc` on ARM64.
- **Windows**: Uses `int 0x2e` or `syscall` instruction; the NT API (NtCreateFile, etc.) is the true syscall layer; Win32 API is a user-space wrapper.
- **macOS**: Mach traps (negative syscall numbers) for microkernel services + BSD syscalls (positive numbers) for POSIX compatibility.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What hardware mechanism prevents a user program from directly executing privileged instructions?
2. Why must a programmer check for `EINTR` when calling blocking system calls like `read()`?
3. Explain the difference between `printf()` and `write()` in terms of system call involvement.

### Core Problems
1. **Syscall tracing**: On a Linux system, run `strace ls` and identify: (a) which syscall opens the directory, (b) which syscall reads directory entries, (c) how many total syscalls are made. Explain why the count is much higher than you might expect.
2. **Performance analysis**: A program copies a 1 MB file using `read(fd, buf, 1)` and `write(fd, buf, 1)` — one byte at a time. Calculate the total number of system calls. If each syscall costs 500 ns, what is the total syscall overhead? Redesign the code to minimise crossings and estimate the improvement.

### Challenge
The vDSO mechanism lets `gettimeofday()` execute without a kernel trap by reading a kernel-maintained time value from a shared memory page. Design a similar mechanism for a hypothetical `getpid_fast()` call. What data must the kernel expose? What consistency guarantees are needed? Could this approach work for `read()` — why or why not?

---

*See also:* [[Processes Overview]] — fork, exec, wait, and exit are process-management system calls · [[File System Fundamentals]] — open, read, write, and close are file-system system calls · [[Virtual Memory and Paging]] — mmap maps files or anonymous memory into the address space via a system call · [[Interrupts and DMA]] — the syscall trap mechanism is architecturally related to hardware interrupts · [[OS Structure]] — the kernel boundary that system calls cross is shaped by OS architecture (monolithic vs micro)

## Supporting Chunks

- [[Foundations - System calls are the controlled interface from user space to the kernel]]
- [[Foundations - Kernel mode and user mode enforce the hardware privilege boundary]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 1.
