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
# OS Fundamentals

> **One-line summary**: An operating system is a software layer that hides hardware complexity (extended machine) and shares hardware fairly among programs (resource manager).

## 🎯 Intuition
**The Core Idea:** The OS is the middleman between your programs and the raw hardware — it translates and arbitrates.
**Analogy:** Think of the OS as a hotel concierge: guests (programs) never deal with plumbing, electricity, or room allocation directly — they ask the concierge (OS) who handles the messy details and makes sure no guest hogs all the towels.
**Why It Matters:** Without an OS, every programmer would need to write disk drivers, memory allocators, and scheduling code from scratch — and programs would crash each other constantly.

---

## ⚙️ Core Mechanics
### How It Works
An **operating system** is a layer of software that sits between application programs and bare hardware. It serves two complementary roles: an **extended machine** that hides hardware complexity behind clean abstractions, and a **resource manager** that multiplexes CPU, memory, disk, and network among competing processes.

#### The Extended-Machine View
Programs should not need to know how a disk controller speaks SATA, or how a network card does DMA. The OS presents idealised abstractions — files, sockets, address spaces, processes — that remain uniform across wildly different hardware. This is the *extended machine* or *virtual machine* view popularised by Tanenbaum.

#### The Resource-Manager View
Multiple programs run simultaneously (or apparently so). The OS decides who gets the CPU next (scheduling), how much physical memory each process can use (memory management), and which process's I/O request gets serviced first. This is the *resource manager* view: the OS as a referee enforcing fair or priority-based sharing.

### Key Concepts

| Abstraction | Hides |
|-------------|-------|
| Process | CPU scheduling, context switching |
| Virtual address space | Physical memory layout, protection |
| File | Disk sectors, controller protocol |
| Socket | Network stack, routing |

### Key Facts
- The OS provides **protection** — programs cannot corrupt each other or the kernel.
- The OS provides **abstraction** — uniform interfaces regardless of underlying hardware.
- The OS provides **multiplexing** — the illusion of dedicated resources for each program.
- Every modern OS fills both the extended-machine and resource-manager roles simultaneously.

---

## 🔬 Deep Dive
### Historical Evolution

| Era | Model | Key Advance |
|-----|-------|-------------|
| 1940s–50s | No OS | Operator loads one job at a time |
| Late 1950s | Batch systems | Job queues; operator overhead removed |
| 1960s | Multiprogramming | Multiple jobs in memory; CPU switches on I/O wait |
| 1960s–70s | Timesharing | Interactive users; illusion of dedicated machine |
| 1980s | Personal computers | Single-user; DOS → Mac → Windows |
| 1990s–2000s | Networked / Internet | Client-server; UNIX widespread; Windows NT |
| 2010s–now | Mobile / Cloud | ARM smartphones; virtualised data centres |

### Implementation Details
- **Kernel mode vs user mode**: The CPU provides hardware privilege levels. The OS kernel runs in privileged mode (ring 0 on x86) with full hardware access; applications run in user mode (ring 3) and must trap into the kernel for any privileged operation.
- **Boot sequence**: Firmware (BIOS/UEFI) → bootloader (GRUB) → kernel init → user-space init (systemd/init). The kernel initialises hardware, sets up memory management, and launches the first user process.
- **System call overhead**: Transitioning from user mode to kernel mode costs ~100–1000 ns on modern hardware due to privilege checks, TLB considerations, and register saving.

### Edge Cases and Pitfalls
- On embedded systems, a "bare-metal" program may act as both application and OS — the distinction blurs.
- Real-time operating systems (RTOS) prioritise deterministic timing over throughput — the resource-manager role is governed by deadlines, not fairness.
- Hypervisors add another layer: the OS itself becomes a "guest" managed by a virtual machine monitor.

### Real-World Systems
- **Linux**: Monolithic kernel serving both roles; dominates servers, mobile (Android), and embedded.
- **Windows**: Hybrid kernel; the Win32 subsystem provides the extended-machine abstraction for desktop applications.
- **macOS/iOS**: XNU kernel (Mach microkernel + BSD); Darwin provides POSIX abstractions over Apple hardware.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What are the two complementary roles of an operating system? Give a one-sentence description of each.
2. Why is it important that a process cannot directly access hardware — what could go wrong?
3. Name three OS abstractions and what hardware detail each one hides.

### Core Problems
1. **Convoy effect scenario**: Three jobs arrive at time 0 with CPU bursts of 100 ms, 2 ms, and 3 ms (in that order). Calculate the average waiting time under FCFS. How would the result differ if the OS could preempt? Relate this to the resource-manager role.
2. **Abstraction design**: Design a minimal abstraction for a "network connection" that hides whether the underlying link is Wi-Fi, Ethernet, or cellular. What operations would your abstraction expose? What details must the OS handle internally?

### Challenge
A unikernel bundles a single application with just the OS components it needs into one address space — no user/kernel split. Analyse the trade-offs: what do you gain in performance? What do you lose in protection and multi-tenancy? Under what deployment model (hint: cloud VMs) does this make sense?

---

*See also:* [[OS Structure]], [[System Calls]]

## Supporting Chunks

- [[Foundations - OS serves as both extended machine and resource manager]]
- [[Foundations - Kernel mode and user mode enforce the hardware privilege boundary]]
- [[Foundations - System calls are the controlled interface from user space to the kernel]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 1.
