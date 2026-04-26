---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "I/O Systems Architecture"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# I/O Systems Architecture

## Summary
The I/O subsystem manages the vast diversity of hardware devices through a layered architecture: applications issue high-level requests, the kernel translates them through device-independent I/O layers, device drivers handle hardware-specific protocols, and interrupt handlers deal with asynchronous device completions. Direct Memory Access (DMA) offloads bulk data transfer from the CPU, while I/O scheduling algorithms reorder disk requests to minimize seek time and maximize throughput.

## Key Claims
- Device drivers are the largest and most bug-prone component of modern operating system kernels—Linux has millions of lines of driver code, and studies show drivers are 3–7 times more likely to contain bugs than core kernel code
- DMA enables devices to transfer data directly to/from main memory without CPU involvement per byte, freeing the CPU to execute other processes during bulk transfers—without DMA, the CPU would spend most of its time copying data between device registers and memory
- The interrupt handling model splits work into a top-half (runs in interrupt context with interrupts disabled, must be fast) and a bottom-half (deferred work that runs with interrupts enabled, handles complex processing)—this split prevents long interrupt handlers from causing unacceptable latency
- I/O scheduling for rotating disks is essentially an optimization of mechanical seek time; the elevator algorithm (SCAN) and its variants (C-SCAN, LOOK) reduce total head movement by servicing requests in a sweep pattern rather than FCFS order
- The transition from rotating disks (HDDs) to solid-state drives (SSDs) has reduced the importance of I/O scheduling since SSDs have no seek time, but scheduling still matters for reducing write amplification and managing queue depth on NVMe devices

## Atomic Facts
1. A DMA transfer proceeds as follows: the CPU programs the DMA controller with source address, destination address, and byte count; the DMA controller transfers data in bursts while the CPU executes other instructions; upon completion, the DMA controller raises an interrupt to notify the CPU
2. Linux implements bottom-half processing through three mechanisms: softirqs (statically allocated, per-CPU, used for high-frequency events like networking), tasklets (dynamically allocated, built on softirqs), and workqueues (run in kernel thread context, can sleep)
3. The Completely Fair Queuing (CFQ) I/O scheduler assigns each process its own request queue and services them round-robin, providing fairness; it was the default Linux I/O scheduler for HDDs until being replaced by mq-deadline and BFQ in newer kernels
4. The deadline I/O scheduler maintains separate read and write queues sorted by sector number plus a FIFO deadline queue for each; reads are given a 500ms deadline and writes 5000ms, preventing read starvation common in write-heavy workloads
5. NVMe (Non-Volatile Memory Express) bypasses the traditional SCSI/AHCI storage stack, communicating directly via PCIe with up to 65,535 I/O queues of 65,536 entries each, achieving microsecond-level latency and millions of IOPS
6. Memory-mapped I/O maps device registers into the processor's physical address space, allowing the CPU to communicate with devices using regular load/store instructions; port-mapped I/O (used by legacy x86 devices) uses separate IN/OUT instructions on a dedicated I/O address space

## Significance
The I/O subsystem demonstrates the principle of abstraction at industrial scale—the same read() system call works whether the underlying device is a mechanical hard drive, an NVMe SSD, a network socket, or a virtual device in a container. The driver model's layered architecture enables hardware vendors to support new devices without modifying the kernel core, which is essential for an ecosystem with thousands of device types.

## Chunks Extracted
- [[chunk-os-099 Device Drivers Are the Largest Most Bug-Prone Kernel Component]]
- [[chunk-os-100 Interrupt Handling Splits Into Top-Half and Bottom-Half]]
- [[chunk-os-101 IO Scheduling Optimizes Mechanical Seek Time]]
- [[chunk-os-102 NVMe Bypasses Legacy Storage Stack for Microsecond Latency]]
