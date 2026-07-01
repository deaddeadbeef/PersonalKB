---
tags:
  - csos
  - csos/study
  - csos/processes
up: "[[OS Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Processes and Scheduling — Review Drill

Active-recall drill for the process and thread abstractions, the process lifecycle, CPU scheduling algorithms, and interprocess communication.

**Canon pages:** [[Process Model]] · [[Process States and Transitions]] · [[Threads and Multithreading]] · [[CPU Scheduling]] · [[Interprocess Communication]] · [[Processes Overview]]

---

## How to Use

Answer each question aloud or in writing before revealing the answer. The goal is retrieval, not re-reading.

---

## Core Recall

**The Process Model**

Q: What four things does a process contain, and where does each live?
A: (1) **Address space** — text (code), data, heap, and stack segments. (2) **CPU state** — PC, SP, and general-purpose registers. (3) **PCB** (kernel data structure) — PID, owner, open file table, scheduling info. (4) **Resources** — open files, network sockets, memory mappings. The PCB lives in kernel memory; the address space lives in physical frames mapped through the page table.

Q: What is the difference between a program and a process?
A: A program is a static executable file on disk. A process is a running instance of that program with its own address space and CPU state. Ten bash processes can run simultaneously from one bash binary; they share the text segment (copy-on-write) but have independent stacks and heaps.

Q: What happens in a `fork()` / `exec()` sequence?
A: `fork()` clones the calling process — the child gets a copy of the parent's address space (implemented as copy-on-write; pages are shared until one side writes). Both parent and child continue executing from after the fork call. `exec()` then replaces the calling process's image with a new program — the address space is discarded and rebuilt from the new executable. Together they allow a shell to spawn an arbitrary program.

Q: What is a zombie process?
A: A process that has called `exit()` (or whose main() returned) but whose parent has not yet called `waitpid()` to collect the exit status. The process's resources are released, but its PCB entry remains until the parent harvests it. Long-lived zombies indicate a bug in the parent.

---

**Process States and Transitions**

Q: Name the three core process states and the events that cause each transition.
A: **Running** (on CPU), **Ready** (runnable but waiting for CPU), **Blocked** (waiting for I/O or event).
- Running → Ready: preemption (quantum expires or higher-priority process becomes ready).
- Running → Blocked: process issues I/O or waits on a semaphore/event.
- Blocked → Ready: I/O completes or the waited event occurs.
- Ready → Running: scheduler dispatches the process.

Q: Why can a process not transition directly from Blocked to Running?
A: The scheduler only selects from the **ready queue**. When the event a blocked process was waiting for occurs, the OS moves it to ready; the scheduler then picks it for the CPU at its next opportunity. This separation keeps the scheduler simple — it only needs to examine the ready queue.

---

**Threads and Multithreading**

Q: What do threads within a process share, and what is private to each thread?
A: Shared: address space (code, global data, heap), open file descriptors, signal handlers. Private: stack, program counter, registers, thread-local storage. Threads are lightweight because context switches do not require switching the address space.

Q: What is the difference between user-space threads and kernel-space threads?
A: **User-space threads** (N:1 model): the thread library multiplexes many user threads onto one kernel thread. Thread creation and switching are fast (no syscall). Problem: one blocking syscall blocks all threads in the process. **Kernel-space threads** (1:1 model): each user thread has a kernel thread. Blocking one thread doesn't block others; true parallelism on multicore. Higher creation cost. Most modern OSes (Linux pthreads, Windows threads) use 1:1.

---

**CPU Scheduling**

Q: What are the five key scheduling metrics?
A: (1) **Throughput** — jobs completed per unit time. (2) **Turnaround time** — job submission to completion. (3) **Response time** — request to first response (matters for interactive). (4) **Waiting time** — time in ready queue. (5) **CPU utilisation** — fraction of time CPU is busy.

Q: Describe FCFS, SJF, Round-Robin, and Priority scheduling in one sentence each.
A: **FCFS**: run jobs in arrival order; non-preemptive; simple but convoy effect hurts short jobs behind long ones. **SJF**: run shortest estimated burst first; minimises average waiting time but requires burst prediction. **Round-Robin**: each process gets a fixed quantum (10–100 ms); preempted at expiry, queued at the back; good for interactive response. **Priority**: highest-priority process runs next; risks starvation for low-priority processes — solved by aging.

Q: How does MLFQ (Multilevel Feedback Queue) adapt to process behaviour?
A: Jobs start in the highest-priority queue. If they use their full quantum (CPU-bound behaviour), they drop to a lower queue with a larger quantum. I/O-bound processes that yield before the quantum expires stay at high priority naturally. Result: interactive processes get low latency; CPU-bound batches don't starve but run less frequently.

Q: What is the convoy effect in FCFS, and why does it harm performance?
A: A single long CPU-bound job at the head of the ready queue forces all subsequent short jobs to wait, inflating their average waiting and turnaround times. A 10-ms interactive job must wait behind a 10-second batch job that arrived first.

---

**Interprocess Communication**

Q: Name four IPC mechanisms and characterise each by coupling and latency.
A: **Pipes**: unidirectional byte stream; tightly coupled (shared file descriptor); low latency within a machine. **Shared memory**: processes map the same physical pages into their address spaces; zero-copy, lowest latency; requires explicit synchronisation (semaphores/mutexes). **Message queues**: kernel-buffered discrete messages; moderate latency; loose coupling. **Sockets**: bidirectional; cross-machine capable; highest latency but maximum generality.

Q: Why does shared memory require explicit synchronisation but pipes do not?
A: A pipe is a kernel-managed FIFO with built-in blocking semantics — a reader blocks until data is available, and a writer blocks when the pipe is full. Shared memory has no such built-in ordering; both processes can read and write simultaneously, creating race conditions unless the programmer adds semaphores or mutexes.

---

## Compare and Contrast

**Scheduling Algorithms**

| Algorithm | Preemptive | Optimal for | Weakness |
|-----------|-----------|-------------|---------|
| FCFS | No | Batch throughput | Convoy effect; poor interactive |
| SJF | No (or yes) | Average waiting time | Requires burst prediction |
| Round-Robin | Yes | Interactive response | Quantum choice critical |
| Priority | Yes/No | Differentiated service | Starvation of low-priority |
| MLFQ | Yes | Mixed workloads | Complex; gaming by processes |

**User Threads vs Kernel Threads**

| Property | User threads (N:1) | Kernel threads (1:1) |
|----------|-------------------|---------------------|
| Context switch cost | Low (no syscall) | Higher (kernel involved) |
| Blocking syscall | Blocks all threads | Blocks only that thread |
| Multicore parallelism | No (one kernel thread) | Yes |
| Common use today | Green threads (e.g., early Java) | POSIX pthreads, Windows threads |

**fork() vs CreateProcess()**

| Property | POSIX fork()+exec() | Windows CreateProcess() |
|----------|--------------------|-----------------------|
| Clone first | Yes | No |
| Address space copy | Yes (COW) | No (fresh) |
| Intermediate state | Child inherits parent context | No intermediate state |
| Flexibility | Very high (exec optional) | Single call |

---

## Common Mistakes

1. **Conflating process and thread** — threads share the address space; processes do not. A context switch between threads in the same process is cheaper than between processes because the TLB and page tables are not flushed.

2. **SJF requires prediction** — SJF is theoretically optimal but is not directly implementable because burst lengths are unknown. In practice, exponential averaging of past bursts approximates next burst.

3. **Zombie vs orphan** — a *zombie* is a dead process whose parent hasn't called waitpid. An *orphan* is a process whose parent died first; the OS re-parents it to `init`/`systemd`, which calls waitpid automatically.

4. **Round-Robin quantum size** — a quantum that is too small causes excessive context-switch overhead; too large degrades interactive response time. Typical sweet spot: 10–100 ms.

5. **MLFQ can be gamed** — a process that yields 1 ms before its quantum expires stays in the high-priority queue forever. Real MLFQ implementations add priority boosting (periodically move all jobs to the top queue) to prevent this.

---

## Links Back

- [[Process Model]] — PCB, fork/exec, zombie lifecycle
- [[Process States and Transitions]] — running/ready/blocked; transition triggers
- [[Threads and Multithreading]] — shared vs private per thread; user vs kernel threads
- [[CPU Scheduling]] — scheduling metrics; FCFS/SJF/RR/Priority/MLFQ
- [[Interprocess Communication]] — pipes, shared memory, message queues, sockets
- [[Processes Overview]] — hub for the entire domain

## References

- [[CS Operating Systems/CS Operating Systems]]
- [[CS Operating Systems/Sources/Sources Index]]
