---
tags:
  - csos
  - csos/study
  - csos/filesystems
  - csos/io
up: "[[OS Study Index]]"
confidence: policy
---
# File Systems and IO — Review Drill

Active-recall drill for file and directory abstractions, on-disk implementation (inodes, allocation, free-space), journaling, I/O hardware (interrupts, DMA), the I/O software stack, and disk scheduling.

**Canon pages:** [[File System Fundamentals]] · [[Directory Structures]] · [[File System Implementation]] · [[Journaling File Systems]] · [[IO Hardware Fundamentals]] · [[Interrupts and DMA]] · [[IO Software Layers]] · [[Disk Scheduling Algorithms]] · [[File Systems Overview]] · [[IO Overview]]

---

## How to Use

Answer each question without referring to canonical pages. File systems and I/O have many mechanical details — focus on precision in your answers.

---

## Core Recall

**File System Fundamentals**

Q: What is a file from the OS's perspective?
A: A **named, persistent byte sequence** managed by the OS. The OS provides the illusion of a contiguous byte stream regardless of how blocks are scattered on disk. Associated metadata (size, permissions, timestamps, type) is stored separately from the data content, typically in an inode.

Q: What is a directory entry, and what does it contain?
A: A directory is a special file that maps **human-readable names** to inode numbers (in POSIX) or to first-block entries (in FAT). A directory entry typically contains: the filename, the inode number (POSIX) or first cluster (FAT), and sometimes file type. The directory structure is how the user-visible name hierarchy is imposed on the flat namespace of inodes.

---

**Inodes and Block Allocation**

Q: Describe the inode structure. How does it support very large files?
A: An inode is a fixed-size metadata block containing: file type, permissions, owner, size, timestamps, and an array of block pointers. The pointer array has: **12 direct pointers** (address the first 12 data blocks directly), **1 single-indirect pointer** (points to a block containing up to 1024 block addresses), **1 double-indirect** (block of blocks), and **1 triple-indirect**. For a 4 KiB block and 4-byte pointers: maximum file size = 12 + 1024 + 1024² + 1024³ blocks — several terabytes. Small files (≤ 12 blocks) are accessed with a single lookup.

Q: Why does contiguous allocation suffer, and how does linked allocation address it?
A: **Contiguous**: simple and fast random access, but causes **external fragmentation** and cannot grow a file without copying it. **Linked allocation**: each block contains a pointer to the next; no fragmentation. But random access is $O(n)$ — you must traverse the chain. **FAT** (File Allocation Table) improves this by moving the pointers out of data blocks into a separate in-memory table; the entire chain can be traversed in memory without extra disk reads per pointer block, but following a chain of k blocks is still $O(k)$ — the gain is practical (memory vs. disk latency), not asymptotic.

Q: How do bitmaps and free lists manage free blocks?
A: **Bitmap**: one bit per block (0 = free, 1 = allocated). Compact (4 KiB bitmap tracks 32,768 blocks). Efficient for finding runs of contiguous free blocks; easy to compute remaining space. **Free list**: linked chain of free blocks, with pointers stored in the blocks themselves. Simple; no extra structure. Slower for finding contiguous runs; fragmented.

---

**Journaling**

Q: What problem does journaling solve?
A: Creating a file requires writing multiple structures (inode, directory entry, free-space bitmap). A crash partway through leaves the file system inconsistent. Without journaling, recovery requires a full `fsck` scan — $O(disk size)$, potentially minutes. Journaling records intended changes in a sequential log *before* writing to final locations. After a crash, the OS replays or discards incomplete journal transactions — $O(\log size)$, seconds.

Q: What are the three journaling modes, and what is the default trade-off?
A: **Writeback**: only metadata journaled; data can be older than metadata after a crash — some file corruption possible. **Ordered** (ext3/4 default): metadata journaled; data blocks are written to final location *before* the metadata journal entry is committed — safe for most use cases; good performance. **Data**: both metadata and data journaled — full consistency guarantee; lowest performance; rarely used in practice.

Q: Describe the write-ahead log protocol.
A: (1) Write the change record to the journal. (2) Flush to disk (ensure durability). (3) Apply changes to final locations. (4) Mark transaction committed; free journal space. Crash between steps 1–2: incomplete record — discard on recovery. Crash between steps 3–4: complete record in journal — replay on recovery. The journal entry is the ground truth until the transaction is committed.

---

**I/O Hardware: Interrupts and DMA**

Q: What is an interrupt, and why is it better than polling?
A: An interrupt is an asynchronous hardware signal telling the CPU that a device event occurred. The CPU saves its state, jumps to the interrupt handler (via the interrupt vector table), services the device, and resumes. Without interrupts, the CPU would busy-wait (poll) — executing a tight loop checking device status registers — wasting cycles when the device is slow (milliseconds) compared to CPU speed (nanoseconds).

Q: Describe DMA and explain why it is useful for large I/O transfers.
A: **DMA (Direct Memory Access)**: the CPU programs a DMA controller with source address, destination address, transfer count, and direction. The DMA controller then moves data between device and memory autonomously, using the system bus without CPU involvement. The CPU is interrupted only *once* when the entire block is transferred. Contrast with programmed I/O where the CPU executes one instruction per byte/word — copying a 4 KiB disk sector with programmed I/O costs ~4096 CPU cycles; with DMA it costs 1 interrupt.

Q: What is bus arbitration in DMA, and what are the two modes?
A: The DMA controller must negotiate bus access with the CPU. **Cycle stealing**: the DMA takes one bus cycle at a time; the CPU slows slightly but continues. **Burst mode**: the DMA holds the bus for the entire transfer — maximum throughput but the CPU is fully stalled during the transfer.

---

**I/O Software Stack**

Q: Name the four layers of the I/O software stack from bottom to top, and state each layer's job.
A: (1) **Interrupt handlers**: save CPU state, acknowledge device, wake the waiting driver process. (2) **Device drivers**: translate generic OS requests (read sector 1024) into device-specific register commands; manage hardware quirks. (3) **Device-independent OS layer**: uniform interface (open/read/write/close), buffering, error reporting, device naming. (4) **User-space I/O library / spooler**: printf/scanf formatting; spooled devices (printers); applications call this layer.

---

**Disk Scheduling**

Q: Compare FCFS, SSTF, and SCAN disk scheduling.
A: **FCFS**: service requests in arrival order; fairness but high seek time if requests are scattered. **SSTF** (Shortest Seek Time First): always service the closest request next; minimises seek time overall but can **starve** requests at the outer tracks. **SCAN** (elevator): head sweeps in one direction servicing all requests it passes, then reverses; eliminates starvation; good average seek time. **C-SCAN**: only service during one direction of sweep; uniform wait times.

---

## Compare and Contrast

**Block Allocation Methods**

| Method | Random access | Fragmentation | Grow file | Notes |
|--------|--------------|---------------|-----------|-------|
| Contiguous | $O(1)$ | External | Hard (copy) | Fast streaming |
| Linked | $O(n)$ | None | Easy (append block) | FAT: chain in memory, no extra disk seeks per pointer; $O(n)$ traversal still |
| Indexed (inode) | $O(1)$ for small files | None | Easy | Universal in POSIX OSes |

**Journaling Modes**

| Mode | What is journaled | Performance | Crash safety |
|------|------------------|-------------|-------------|
| Writeback | Metadata only | Highest | Metadata consistent; data may be stale |
| Ordered | Metadata + ordered data flush | Good | Data written before commit |
| Data | Metadata + data | Lowest | Fully consistent |

**Interrupt vs Polling vs DMA**

| Mechanism | CPU involvement | Overhead | Best for |
|-----------|----------------|----------|---------|
| Polling | High (busy loop) | Wastes cycles | Ultra-low-latency devices |
| Interrupt-driven | Low (one interrupt) | Context switch per event | General I/O |
| DMA | Minimal (program + one interrupt) | DMA setup | Large bulk transfers |

---

## Common Mistakes

1. **Inode vs directory entry** — the inode holds metadata and block pointers; the directory entry maps a name to an inode number. A file can have multiple directory entries (hard links) all pointing to the same inode — this is how `ln` works.

2. **Journaling does not prevent data loss** — journaling guarantees **file system consistency** (no orphaned inodes, no double-allocated blocks). It does not guarantee that data written to a file is durable unless `fsync()` is called. Ordered journaling only ensures data written to disk before the metadata commit — not before an application crash.

3. **DMA does not make I/O instantaneous** — DMA overlaps the transfer with CPU computation, but the transfer itself still takes time. The CPU only avoids doing the byte-by-byte copy; latency of the device is unchanged.

4. **SSTF starvation** — SSTF is optimal for average seek time in isolation but starves requests far from the current head position if new requests keep arriving nearby. SCAN/C-SCAN are fairer.

5. **FAT is not the same as linked allocation** — FAT moves the block-pointer chain out of the data blocks into a separate in-memory table. This eliminates the need to read pointer blocks from disk when traversing the chain (a big practical win), but following a chain of k blocks still requires $O(k)$ in-memory table lookups — it is not $O(1)$. Naive linked allocation leaves pointers in data blocks, so random access requires $O(n)$ disk reads.

---

## Links Back

- [[File System Fundamentals]] — file abstraction; directory as name-to-inode map
- [[Directory Structures]] — hierarchical directory trees; path traversal
- [[File System Implementation]] — inode layout; contiguous/linked/indexed allocation; free-space bitmaps
- [[Journaling File Systems]] — write-ahead logging; writeback/ordered/data modes; ext3/ext4, NTFS
- [[IO Hardware Fundamentals]] — device controllers; port-mapped vs memory-mapped I/O
- [[Interrupts and DMA]] — interrupt vector table; DMA cycle-stealing vs burst mode
- [[IO Software Layers]] — four-layer stack; interrupt handlers; device drivers
- [[Disk Scheduling Algorithms]] — FCFS, SSTF, SCAN, C-SCAN; seek time optimisation
- [[File Systems Overview]] — hub for file systems
- [[IO Overview]] — hub for I/O

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
