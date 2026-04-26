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
# OS Structure

> **One-line summary**: OS architecture determines which code runs in privileged kernel space vs. user space, trading off performance, reliability, and security.

## 🎯 Intuition
**The Core Idea:** The kernel's internal structure decides the blast radius of bugs and the cost of communication between OS components.
**Analogy:** A monolithic kernel is like an open-plan office — everyone can shout across the room (fast communication), but one person's fire burns the whole floor. A microkernel is like separate offices with a mail room — slower to exchange messages, but a fire in one office stays contained.
**Why It Matters:** Choosing monolithic vs. micro vs. hybrid shapes every trade-off in OS design: a Linux driver bug can kernel-panic the whole machine, while QNX can restart a crashed driver without rebooting.

---

## ⚙️ Core Mechanics
### How It Works
The internal organisation of an operating system — which code runs where and with what privileges — has enormous consequences for performance, reliability, and security. Four main structural styles are widely used.

#### Monolithic Kernels
All OS services (scheduling, memory management, file systems, device drivers, networking) run together in a single kernel address space with full hardware privilege. A bug in a device driver can crash the entire system, but there is no inter-component IPC overhead.

**Examples:** Linux, traditional BSD UNIX, early Windows.

**Pros:** High performance; direct function calls between subsystems.
**Cons:** A fault in any module can corrupt shared kernel state; large attack surface.

#### Microkernels
The kernel retains only the absolute minimum: inter-process communication, basic scheduling, and address-space management. Everything else (file systems, drivers, network stacks) runs as ordinary user-space server processes. Components communicate via message passing through the microkernel.

**Examples:** MINIX 3, QNX, seL4, early Mach.

**Pros:** Fault isolation; a crashed driver can be restarted without rebooting; smaller trusted computing base.
**Cons:** IPC overhead between components; slower than monolithic for I/O-intensive workloads.

#### Hybrid Kernels
Most production systems adopt a hybrid: a kernel that is larger than a microkernel (for performance) but has better structure than a pure monolith. Windows NT runs a minimal kernel plus in-kernel executive services; macOS has a Mach-based microkernel core with BSD services compiled in.

#### Exokernels
Exokernels expose hardware resources directly to applications with minimal abstraction, delegating resource management to user-space library OSes. Designed for research/specialisation; rare in production.

### Key Concepts

| Architecture | Kernel Contains | IPC Cost | Fault Isolation |
|-------------|----------------|----------|-----------------|
| Monolithic | Everything | None (direct calls) | None — one bug crashes all |
| Microkernel | IPC, scheduling, MMU | High (message passing) | Strong — restart failed servers |
| Hybrid | Core + performance-critical services | Medium | Partial |
| Exokernel | Minimal multiplexer | N/A (library OS) | Application-level |

### Key Facts
- Monolithic kernels use direct function calls between subsystems — zero IPC overhead.
- Microkernels move file systems, drivers, and network stacks to user space as server processes.
- Hybrid kernels are the pragmatic middle ground used by Windows NT and macOS.
- Exokernels delegate abstraction to user-space library OSes for maximum specialisation.

---

## 🔬 Deep Dive
### Loadable Kernel Modules
Linux achieves extensibility by allowing kernel code to be compiled separately and loaded at runtime (e.g., file system drivers, hardware drivers). The module runs in kernel space with full privilege, so this is still monolithic in terms of fault isolation.

### Implementation Details
- **Linux module system**: `insmod` / `modprobe` load `.ko` files into kernel address space at runtime. Modules can register callbacks (e.g., `file_operations` struct) and access all kernel symbols. Unloading is possible but risky if references remain.
- **Windows HAL**: The Hardware Abstraction Layer isolates the kernel from platform-specific hardware details. The NT executive (object manager, I/O manager, memory manager) runs in kernel space above the HAL.
- **seL4 formal verification**: seL4 is the first OS kernel with a machine-checked proof of functional correctness — proving that the C implementation matches its formal specification. This is only feasible because the microkernel is ~10,000 lines of C.

### Edge Cases and Pitfalls
- Loadable modules give monolithic kernels extensibility but not fault isolation — a buggy module still runs in ring 0.
- First-generation microkernels (Mach) were slow due to excessive IPC; modern ones (seL4, L4) drastically reduced IPC cost.
- Hybrid is a spectrum, not a fixed design — "how much goes in the kernel" is an engineering judgement call.

### Real-World Systems
- **Linux**: Monolithic with ~30,000+ loadable modules; dominates servers and Android.
- **Windows NT/10/11**: Hybrid — microkernel core + in-kernel executive services + HAL.
- **macOS (XNU)**: Mach microkernel messages + BSD monolithic services compiled into one binary.
- **QNX**: True microkernel; used in automotive (BlackBerry QNX), medical devices, nuclear plants.
- **seL4**: Formally verified microkernel; used in high-assurance defence and aerospace systems.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the key trade-off between monolithic and microkernel architectures?
2. Why does a buggy device driver in Linux risk crashing the entire system, while in MINIX 3 it does not?
3. Name one real-world OS for each of the four architecture styles.

### Core Problems
1. **IPC overhead analysis**: A microkernel file read requires: app → kernel (message) → file server (process) → kernel (message) → disk driver (process) → kernel (message) → back. Count the user/kernel boundary crossings. A monolithic kernel does this with one system call. If each crossing costs 1 μs, what is the overhead difference for reading 1000 files?
2. **Module safety design**: Propose a mechanism that gives Linux loadable modules some fault isolation without the full IPC cost of a microkernel. Consider: separate kernel address space regions, watchdog timers, or shadow page tables. What are the trade-offs?

### Challenge
Google's Fuchsia uses the Zircon microkernel. Research its architecture: what runs in the kernel vs. user space? How does it handle driver isolation differently from Linux? Compare its IPC mechanism (channels + FIDL) to classic Mach ports and argue whether Fuchsia's approach resolves the first-generation microkernel performance problem.

---

*See also:* [[OS Fundamentals]], [[System Calls]]

## Supporting Chunks

- [[Foundations - Monolithic kernels colocate all OS services for performance]]
- [[Foundations - Microkernels move services to user space for reliability at a performance cost]]
- [[Case Studies - Linux uses a monolithic kernel with loadable modules as a performance-reliability compromise]]
- [[Case Studies - Windows NT uses a hybrid architecture with a HAL and an in-process executive]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 1.
