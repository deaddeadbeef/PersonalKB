---
tags:
  - csos
  - csos/filesystems
confidence: verified
up: "[[File Systems Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Journaling File Systems

## 🎯 Intuition
**The Core Idea:** A crash during a multi-block metadata update can leave the file system inconsistent, so journaling writes down intended changes before applying them.
**Analogy:** It is like a pilot's pre-flight checklist: even if the process is interrupted, you can tell what was completed and what still must be done.
**Why It Matters:** Without journaling, recovery may require an `fsck` scan over the entire disk, which can take minutes instead of seconds.

## ⚙️ Core Mechanics
### The Failure Problem
Creating or updating a file may require multiple metadata writes, such as updating the inode, directory entry, and free-space bitmap. If the system crashes in the middle, those structures can disagree.

### Journaling as Write-Ahead Logging
**Journaling** records intended changes in a sequential log before applying them to final on-disk locations. After a crash, the file system can replay completed transactions or discard incomplete ones, restoring consistency quickly.

### Write-Ahead Log Protocol
1. Write the changes to the journal (a circular log).
2. Flush the journal to disk.
3. Write the actual data and metadata to their final locations.
4. Mark the transaction committed and free the log space.

## 🔬 Deep Dive
### Crash Cases
- **Crash during steps 1-2:** the journal record is incomplete, so the file system discards it.
- **Crash during steps 3-4:** the journal contains a complete record, so the file system replays it.

### Journal Modes

| Mode | What is Journaled | Performance | Safety |
|------|------------------|-------------|--------|
| **Writeback** | Metadata only | Highest | Data may be old after crash |
| **Ordered** (default ext3/4) | Metadata journaled; data flushed before commit | Good | Data is written before metadata is committed |
| **Data** | Metadata + data | Lowest | Full consistency |

### Examples
- **ext3/ext4**: mature journaling file systems; ext4 also adds extents and delayed allocation
- **XFS**: high-performance design for large files and parallel I/O
- **NTFS**: uses `$LogFile` for journaling
- **APFS**: uses copy-on-write instead of a traditional journal

## 🏋️ Practice
### Warm-Up
What happens if the system crashes after the journal is flushed but before the metadata is written to its final location?

### Core Problems
Why is ordered mode the default in ext4?

### Challenge
Compare journaling with copy-on-write file systems such as APFS or ZFS for crash consistency and write behavior.

## Supporting Chunks

- [[File Systems - Journaling uses write-ahead logging to guarantee crash-consistent metadata]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 4.