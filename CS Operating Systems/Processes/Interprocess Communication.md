---
tags:
  - csos
  - csos/processes
confidence: verified
freshness: stable
up: "[[Processes Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Interprocess Communication

> **One-line summary**: IPC mechanisms let separate processes exchange data and coordinate actions despite having isolated address spaces.

## 🎯 Intuition
**The Core Idea:** Processes live in separate apartments (address spaces) — IPC is the postal system, phone line, or shared bulletin board that lets them talk.
**Analogy:** Shared memory = a whiteboard in a common hallway (fast, but people must take turns writing). Pipes = a pneumatic tube (one-way, FIFO). Message passing = sending letters through a mail room (structured, works across buildings). Signals = a fire alarm (no data, just "something happened"). Sockets = a telephone line (two-way, works across cities).
**Why It Matters:** Nearly every real system — web servers, databases, shell pipelines — relies on IPC. Choosing the right mechanism determines performance, complexity, and correctness.

---

## ⚙️ Core Mechanics
### How It Works
**IPC** mechanisms let separate processes exchange data and coordinate actions. The OS must provide these because processes have separate address spaces and cannot share memory directly by default.

#### Shared Memory
A region of physical memory is mapped into two or more processes' address spaces. Once set up (via `shmget`/`shmat` on POSIX, or `CreateFileMapping` on Windows), communication is as fast as ordinary memory access. Synchronisation (to prevent races on the shared region) must be handled separately — typically with semaphores or mutexes.

**Use cases:** High-bandwidth producer-consumer within the same machine; database buffer pools.

#### Pipes
A unidirectional byte stream kernel buffer. Writer pushes data in; reader pulls it out. `pipe()` creates a pipe; `fork()` allows the child to inherit the file descriptors. Data is FIFO; the pipe blocks the writer when full and the reader when empty.

Named pipes (FIFOs) allow unrelated processes to communicate via a file-system name.

#### Message Passing
Processes exchange discrete messages via `send()` and `receive()` primitives. The OS (or middleware) handles buffering, routing, and synchronisation. Can be synchronous (blocking send until receiver picks up) or asynchronous (buffered). Natural fit for networked or distributed systems.

#### Signals
Signals are asynchronous software interrupts delivered to a process by the OS or another process. Predefined signal numbers (SIGINT, SIGTERM, SIGSEGV, etc.) trigger registered handler functions or default actions (termination, core dump). Signals are not a data channel — they carry only the signal number.

#### Sockets
A socket provides a bidirectional communication channel. UNIX domain sockets work within a single host (very fast); TCP/IP sockets work across machines. Used for client-server communication and as Android's replacement for POSIX IPC (via Binder).

### Key Concepts

| Mechanism | Direction | Data Unit | Scope | Speed |
|-----------|-----------|-----------|-------|-------|
| Shared Memory | Bidirectional | Raw bytes | Same host | Fastest (memory speed) |
| Pipe | Unidirectional | Byte stream | Parent-child (or named) | Fast (kernel buffer) |
| Message Passing | Bidirectional | Discrete messages | Local or networked | Medium (kernel-mediated) |
| Signals | One-way notification | Signal number only | Same host | Fast (no data) |
| Sockets | Bidirectional | Byte stream / datagrams | Same host or networked | Variable (protocol-dependent) |

### Key Facts
- Shared memory is the fastest IPC but requires explicit synchronisation (semaphores, mutexes).
- Pipes are simple and FIFO; they block when full (writer) or empty (reader).
- Message passing naturally fits distributed systems; can be synchronous or asynchronous.
- Signals carry no data — only a signal number — and are best for notifications, not communication.
- UNIX domain sockets are significantly faster than TCP sockets for same-host communication.

---

## 🔬 Deep Dive
### Implementation Details
- **Shared memory setup (POSIX)**: `shmget()` allocates a shared segment; `shmat()` maps it into the calling process's address space. The kernel maintains a reference count; the segment persists until explicitly removed with `shmctl(IPC_RMID)`. Modern alternative: `shm_open()` + `mmap()` (simpler, file-descriptor-based).
- **Pipe buffer size**: Linux default pipe buffer is 64 KiB (16 pages). Writes larger than `PIPE_BUF` (4 KiB) are not guaranteed to be atomic. The `fcntl(F_SETPIPE_SZ)` call can resize up to `/proc/sys/fs/pipe-max-size`.
- **Signal safety**: Only async-signal-safe functions may be called inside signal handlers (e.g., `write()` is safe; `printf()` is NOT). The set of safe functions is defined by POSIX.
- **Android Binder**: A custom IPC mechanism replacing POSIX IPC. Uses a kernel driver (`/dev/binder`) with a transaction-based protocol. Supports object references, death notifications, and permission enforcement. Designed for high-frequency short messages between apps and system services.

### Edge Cases and Pitfalls
- **Shared memory without synchronisation** = data races. The shared region looks like normal memory, so it's easy to forget that another process is writing concurrently.
- **Pipe deadlock**: If a process holds both read and write ends and fills the buffer, it blocks itself forever.
- **Signal handler re-entrancy**: A signal delivered while inside a signal handler can corrupt state. Use `sigaction()` with `SA_RESTART` and keep handlers minimal.
- **SIGKILL/SIGSTOP cannot be caught**: These signals bypass handler registration — the kernel handles them directly.

### Real-World Systems
- **Linux**: Full POSIX IPC (shared memory, semaphores, message queues) + UNIX domain sockets + pipes + eventfd + io_uring for async I/O.
- **Windows**: Named pipes, mailslots, COM/DCOM, shared memory via file mappings, WM_COPYDATA messages.
- **Android**: Binder for app-to-system-service IPC; shared memory (ashmem/memfd) for large data transfers; intents for inter-app messaging.
- **macOS**: Mach ports (message passing) as the fundamental IPC; XPC for structured inter-process services; UNIX sockets for POSIX compatibility.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can't two processes simply share data through global variables?
2. A UNIX shell command `ls | grep ".txt"` uses what IPC mechanism? What happens if `grep` reads faster than `ls` writes?
3. Why is `printf()` unsafe inside a signal handler but `write()` is safe?

### Core Problems
1. **Producer-consumer with shared memory**: Two processes share a 1024-byte circular buffer via POSIX shared memory. Design the data structure (head, tail pointers, buffer) and the synchronisation protocol using POSIX semaphores. Handle the edge cases: buffer full, buffer empty, and producer/consumer exit.
2. **IPC selection matrix**: You're designing a system with three components: (a) a real-time sensor reader producing 10 MB/s of data, (b) a processing daemon on the same host, (c) a remote monitoring dashboard. Choose and justify the optimal IPC mechanism for each pair. Consider latency, throughput, and failure isolation.

### Challenge
Design a hybrid IPC mechanism that combines shared memory for data transfer with a pipe for signalling (avoiding polling). The sender writes data to shared memory and then writes a single byte to the pipe to wake the receiver. Implement the protocol in pseudocode. Analyse: what synchronisation is still needed? How does this compare to eventfd on Linux? Could you achieve the same with `futex()` — and what would change?

---

*See also:* [[Race Conditions and Mutual Exclusion]] — shared-memory IPC requires explicit synchronisation to prevent races · [[Semaphores]] — classic mechanism for coordinating shared-memory producers and consumers · [[Address Spaces]] — separate address spaces are the reason IPC mechanisms are needed · [[Deadlock Fundamentals]] — blocking send/receive can create circular waits

## Supporting Chunks

- [[Processes - IPC mechanisms differ in coupling, latency, and scope]]
- [[Case Studies - Android extends Linux with Binder IPC and a permission-based app sandbox]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 2.
