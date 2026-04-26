---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Disk Scheduling Algorithms"
authors: Silberschatz, Galvin, Gagne; Tanenbaum, Bos
year: 2018
---

# Disk Scheduling Algorithms

## Summary

Disk scheduling algorithms determine the order in which pending I/O requests to a hard disk drive are serviced, with the primary goal of minimizing seek time—the time to move the read/write head to the correct track. The total disk access time for a request comprises three components: seek time (head movement, typically 3–15 ms), rotational latency (waiting for the correct sector to rotate under the head, averaging half a rotation period), and transfer time (reading or writing the data, usually under 1 ms).

FCFS (First-Come, First-Served) processes requests in arrival order. It is fair but produces large total head movements when requests are scattered. SSTF (Shortest Seek Time First) selects the request nearest to the current head position, reducing average seek time but risking starvation for distant requests. SCAN (elevator algorithm) moves the head in one direction, servicing all requests along the way, then reverses. C-SCAN (Circular SCAN) moves in one direction only, jumping back to the beginning without servicing on the return sweep, providing more uniform wait times. LOOK and C-LOOK are practical variants of SCAN and C-SCAN that reverse direction at the last pending request rather than traveling to the physical end of the disk.

For modern SSDs, traditional disk scheduling is largely irrelevant because solid-state drives have no mechanical head or rotational platter. SSD access times are uniform regardless of address, typically 25–100 microseconds. SSDs benefit instead from I/O scheduling that optimizes for queue depth and parallelism across internal flash channels. Linux's default I/O scheduler for NVMe SSDs is `none` (also called `noop`), which performs no reordering, simply passing requests directly to the device. For SATA SSDs, the `mq-deadline` scheduler provides deadline guarantees while minimizing scheduler overhead. The BFQ (Budget Fair Queueing) scheduler offers better interactive latency for slower storage devices at the cost of throughput.

## Key Claims

- Seek time dominates disk access latency for HDDs, making the order of request servicing far more important than the raw transfer speed
- SSTF minimizes average seek distance but can starve requests at extreme track positions if new nearby requests continuously arrive
- SCAN and C-SCAN provide bounded waiting times by ensuring the head systematically sweeps across the disk, preventing indefinite starvation
- LOOK/C-LOOK optimize SCAN/C-SCAN by reversing at the last actual request rather than the physical disk boundary, eliminating unnecessary empty sweeps
- SSD scheduling focuses on queue depth parallelism rather than seek optimization, rendering traditional algorithms like SCAN irrelevant for flash storage

## Atomic Facts

1. Average rotational latency for a 7200 RPM drive is approximately 4.17 ms (half of one 8.33 ms revolution)
2. FCFS can produce head movement exceeding the full disk width multiple times if requests alternate between inner and outer tracks
3. SCAN is called the "elevator algorithm" because its behavior mirrors an elevator servicing floors in one direction before reversing
4. C-SCAN provides more uniform response times than SCAN because every request waits for at most one full sweep rather than potentially two
5. Linux kernel 5.0 removed the legacy single-queue CFQ and deadline schedulers in favor of multi-queue blk-mq schedulers (mq-deadline, BFQ, kyber, none)
6. NVMe drives support hardware queues of up to 65,535 entries per queue with up to 65,535 queues, making software-level reordering unnecessary

## Significance

Disk scheduling algorithms are foundational to I/O subsystem design and remain essential for HDD-based storage systems. Understanding them illuminates the broader OS principle that software-level reordering can compensate for physical hardware constraints. The transition to SSDs demonstrates how hardware evolution can obsolete entire classes of algorithms, shifting optimization from mechanical seek reduction to parallelism and queue management.

## Chunks Extracted

*Pending*
