---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "RAID Levels"
authors: Patterson, Gibson, Katz; Tanenbaum, Bos
year: 1988
---

# RAID Levels

## Summary

RAID (Redundant Array of Independent Disks) combines multiple physical disks into a logical unit to improve performance, reliability, or both. Originally proposed by Patterson, Gibson, and Katz at Berkeley in 1988, RAID replaces a single expensive disk with an array of inexpensive drives while providing comparable or superior reliability through redundancy techniques.

RAID 0 (striping) distributes data across multiple disks in fixed-size strips, maximizing throughput by parallelizing reads and writes. It offers no redundancy—any single disk failure destroys the entire array. RAID 1 (mirroring) writes identical copies of all data to two or more disks. It tolerates single-disk failures with no rebuild penalty, provides excellent read performance (reads can be distributed), but has a 100% storage overhead. RAID 5 uses block-level striping with distributed parity, rotating the parity block across all drives so no single disk becomes a write bottleneck. It tolerates one disk failure and has a storage overhead of 1/N (one disk's worth of parity). However, RAID 5 suffers from the "write hole" problem: a crash between writing data and parity can leave the array inconsistent. RAID 6 extends RAID 5 with double distributed parity (using two independent parity calculations, such as P+Q), tolerating two simultaneous disk failures. This is increasingly important as disk capacities grow because rebuild times for large disks can exceed 24 hours, during which a second failure would cause data loss in RAID 5. RAID 10 (1+0) stripes across mirrored pairs, combining RAID 1 redundancy with RAID 0 performance. It tolerates multiple failures as long as both disks in a mirror pair do not fail simultaneously.

Hot spares are idle disks kept ready in a RAID array; when a disk fails, the controller automatically begins rebuilding onto the spare, reducing the vulnerable window. Modern hardware RAID controllers maintain battery-backed write caches to safely cache writes and mitigate the RAID 5 write hole.

## Key Claims

- RAID 0 maximizes throughput through parallel striping but provides zero fault tolerance—any single disk failure results in complete data loss
- RAID 5 distributes parity across all disks to avoid the parity-disk bottleneck but is vulnerable during rebuilds because a second failure during reconstruction causes total array loss
- RAID 6 with double parity is becoming the minimum acceptable redundancy level for large-capacity drives where rebuild times measured in hours increase the probability of a second failure
- RAID 10 offers the best combination of performance and reliability for write-intensive workloads, at the cost of 50% storage overhead
- Hot spares reduce the mean time to recovery by allowing automatic rebuild to begin immediately upon failure detection, without human intervention

## Atomic Facts

1. RAID was introduced in the 1988 paper "A Case for Redundant Arrays of Inexpensive Disks" by Patterson, Gibson, and Katz at UC Berkeley
2. RAID 5 requires a minimum of three disks and provides (N-1)/N usable capacity where N is the number of disks
3. The RAID 5 write penalty requires four I/O operations for each small write: read old data, read old parity, write new data, write new parity
4. RAID 6 typically uses Reed-Solomon coding or a combination of XOR parity (P) and Galois-field parity (Q) for dual redundancy
5. RAID 10 can survive multiple simultaneous disk failures as long as failures do not occur within the same mirrored pair
6. A 10 TB RAID 5 array with 200 MB/s rebuild throughput requires approximately 14 hours to reconstruct, during which the array operates in degraded mode

## Significance

RAID fundamentally shaped how storage systems balance performance and reliability. The concept of using redundancy across commodity hardware rather than relying on expensive specialized components became a template for distributed systems design broadly. Understanding RAID levels remains essential for systems administration, database design, and any application where data durability and I/O performance intersect.

## Chunks Extracted

*Pending*
