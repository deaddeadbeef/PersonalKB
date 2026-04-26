---
tags:
  - csos
  - csos/processes
confidence: verified
up: "[[Processes Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Process Model

> **One-line summary**: A process is the OS abstraction for a running program — an address space, CPU state, and kernel bookkeeping bundled together.

## 🎯 Intuition
**The Core Idea:** A process is a program *in motion* — the OS's container for everything needed to run, pause, and resume a program.
**Analogy:** A process is like a chef in a kitchen: the recipe (program code) is just paper until a chef (CPU) starts following it. The chef's workspace — cutting board, ingredients, notes about which step they're on (registers, PC, stack) — is the process. Multiple chefs can follow the same recipe simultaneously in separate kitchens (separate address spaces).
**Why It Matters:** Every running application is a process. Understanding the process model explains how the OS isolates programs, creates new ones (fork/exec), and cleans up after them.

---

## ⚙️ Core Mechanics
### How It Works
A **process** is the OS abstraction for a running program: an address space containing the program's code, data, and stack, plus the CPU execution state needed to resume it (registers, program counter, stack pointer), and OS bookkeeping in the **Process Control Block (PCB)**.

#### Process vs Program
A program is a static executable file. A process is a running instance — you can have 10 bash processes from one bash binary. The OS distinguishes them by their PID and separate address spaces.

### Key Concepts

| Component | Contents |
|-----------|----------|
| Address space | Text (code), data, heap, stack segments |
| CPU state | PC, SP, general-purpose registers, condition codes |
| PCB (kernel data) | PID, owner, open file table, signal handlers, scheduling info |
| Resources | Open files, network sockets, memory mappings |

### Key Operations

#### Process Creation
- **`fork()`** (POSIX): The parent process is cloned; child gets a copy of parent's address space (via copy-on-write). Both parent and child execute after the `fork()` call.
- **`exec()`**: Replaces the calling process's image with a new program. Typically called after `fork()` in the child to run a different program.
- **Windows `CreateProcess()`**: Combines fork and exec into one call; no intermediate clone.

#### Process Termination
- Normal exit (`exit()` call, or return from `main()`).
- Fatal error (segfault, division by zero — OS sends a signal).
- Killed by another process (`kill(pid, SIGKILL)`).
- Parent calls `waitpid()` to collect exit status; until then the child is a *zombie*.

### Key Facts
- A process = address space + CPU state + PCB. All three are needed.
- `fork()` uses copy-on-write: pages are shared read-only until one process writes, then the written page is copied.
- A zombie is a terminated process whose exit status hasn't been collected by its parent.
- Every process has a unique PID; PID 1 is the init/systemd process (ancestor of all user processes on Linux).

---

## 🔬 Deep Dive
### Implementation Details
- **PCB in Linux (`task_struct`)**: The kernel's `task_struct` (defined in `include/linux/sched.h`) is ~6 KiB and contains: scheduling priority, memory descriptor (`mm_struct`), file descriptor table, signal handlers, cgroup membership, namespace references, and hundreds of other fields. It is allocated from a slab cache for fast creation.
- **Copy-on-write (COW)**: On `fork()`, the parent's page table entries are duplicated and marked read-only in both parent and child. On the first write, a page fault triggers the kernel to copy just that page. This makes `fork()` nearly instant even for large-memory processes.
- **`fork()` return value**: Returns 0 to the child, the child's PID to the parent. This single return value is how both processes distinguish their role.
- **Process table**: The kernel maintains a hash table of `task_struct` pointers indexed by PID for $O(1)$ lookup.

### Edge Cases and Pitfalls
- **Zombie accumulation**: If a parent never calls `wait()`, zombie entries pile up in the process table, eventually exhausting PID space. Solution: double-fork (orphan the child to init) or use `SIGCHLD` handler.
- **Orphan processes**: When a parent dies, its children are reparented to PID 1 (init/systemd), which automatically reaps them.
- **`fork()` in multithreaded programs**: Only the calling thread is cloned. Other threads vanish in the child, potentially leaving locks held → undefined state. POSIX provides `pthread_atfork()` handlers but the safest pattern is `fork()` then immediately `exec()`.
- **PID reuse**: PIDs are recycled. Sending a signal to a stored PID after the process has exited may target a completely different process. Use `pidfd_open()` (Linux 5.3+) for race-free process references.

### Real-World Systems
- **Linux**: `task_struct` represents both processes and threads (threads share `mm_struct`). `clone()` is the unified syscall; `fork()` and `pthread_create()` are wrappers.
- **Windows**: Each process has a `EPROCESS` kernel object containing the PEB (Process Environment Block), handle table, and token (security context). `CreateProcess()` is the single creation API.
- **macOS**: BSD-layer `proc` structure + Mach task ports. `fork()` is POSIX-compatible; `posix_spawn()` is preferred for efficiency.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between a process and a program? Can multiple processes run the same program?
2. After `fork()`, how does the parent distinguish itself from the child?
3. What is a zombie process and why does it exist?

### Core Problems
1. **Fork tree**: Trace the output of this code and draw the process tree:
   ```c
   fork();
   fork();
   printf("hello\n");
   ```
   How many times is "hello" printed? How many total processes exist?
2. **COW analysis**: A process uses 1 GB of memory and calls `fork()`. The child immediately calls `exec()` to run a 10 MB program. (a) How much physical memory is consumed right after `fork()` (before exec)? (b) After `exec()`? (c) What would happen without COW?

### Challenge
Design a process creation API that avoids the fork-exec two-step. Your API should: (a) create a new address space, (b) load a specified executable, (c) set up file descriptor inheritance, (d) set initial environment variables — all in one call. Compare your design to `posix_spawn()` and Windows `CreateProcess()`. What simplifying assumptions does each make? What flexibility do they sacrifice compared to raw `fork()+exec()`?

---

*See also:* [[Process States and Transitions]], [[Threads and Multithreading]], [[Address Spaces]]

## Supporting Chunks

- [[Processes - The process model gives each program the illusion of an exclusive CPU]]
- [[Processes - Process states form a three-state lifecycle driven by scheduler and IO events]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 2.
