---
tags: [cs-algorithms, sorting, external-memory]
up: "[[Sorting Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# External Sorting

> **One-line summary** External sorting is sorting for data sets that do not fit in memory, so the main cost is disk or SSD I/O rather than comparisons alone.

## Intuition

Internal sorting assumes the input fits in RAM. External sorting starts from the opposite assumption: the data is too large, so the algorithm must move data between storage and memory in long sequential runs. The central question changes from "how many comparisons?" to "how many passes over the data and how much random I/O?"

The standard pattern is external merge sort. First, read chunks that fit in memory, sort each chunk with an internal algorithm, and write each sorted chunk back as a run. Then repeatedly merge multiple runs at a time until one sorted output remains. If memory can hold buffers for many runs, a multi-way merge reduces the number of full-data passes.

## Core Mechanics

1. Split the input into memory-sized blocks.
2. Sort each block in RAM, usually with a fast internal sort.
3. Write each sorted block as an on-disk run.
4. Merge runs with buffered sequential reads and writes.
5. Increase merge fan-in when memory allows more input buffers.

External sorting is closely related to [[CS Data Structures/Trees/B-Trees and B-Plus Trees|B-trees and B+ trees]] because both are designed around block transfers. B-trees reduce search cost by matching node size to pages; external sort reduces sort cost by making reads and writes sequential and by minimizing the number of passes.

## Why It Matters

Databases, search indexes, analytics engines, log pipelines, and compilers all sort data that may exceed memory. In those systems, asymptotic comparison count is not enough to predict performance. A theoretically good in-memory sort can lose badly if it causes random reads, poor buffering, or too many full scans.

External sorting is also the gateway to the external-memory model of algorithms, where block size, memory size, and I/O count become explicit variables. This is why it connects naturally to [[CS Data Structures/Advanced Structures/External Memory Structures|external memory structures]] and [[CS Operating Systems/IO/Disk Scheduling Algorithms|disk scheduling]].

## Practice

1. Given a 1 TB input, 8 GB of usable memory, and 256 MB run buffers, estimate the number of initial sorted runs.
2. Compare a two-way merge with a k-way merge when the bottleneck is full-data passes over disk.
3. Explain why sequential I/O matters even on SSDs, and why it mattered even more on spinning disks.

## References

- [[CS Algorithms/Sources/Sources Index]]
- [[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Algorithms Unlocked chapter notes]]
- [[CS Data Structures/Advanced Structures/External Memory Structures]]
