---
tags:
  - csos
  - csos/filesystems
confidence: verified
freshness: stable
up: "[[File Systems Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# File System Fundamentals

## 🎯 Intuition
**The Core Idea:** A **file** is the OS abstraction for persistent, named storage. It hides disk sectors and block allocation behind named byte sequences that survive process termination and system reboot.
**Analogy:** A file is like a labeled folder in a filing cabinet: users care about the name and contents, not which exact shelf slot or drawer hardware stores it.
**Why It Matters:** Files are the universal abstraction for persistent data, so every program depends on them for code, configuration, input, output, and long-term state.

## ⚙️ Core Mechanics
### File Attributes

| Attribute | Description |
|-----------|-------------|
| Name | Human-readable identifier |
| Type | Regular, directory, symbolic link, device, pipe, socket |
| Size | Current length in bytes |
| Timestamps | Created, modified, accessed (ctime, mtime, atime) |
| Owner / Group | User and group owning the file |
| Permissions | Read / write / execute for owner, group, others |
| Inode number | Unique identifier within the file system |

### Access Modes
- **Sequential access**: read/write from the current position; the position advances automatically.
- **Random access**: `lseek()` moves to any byte offset before reading or writing.
- **Memory-mapped access**: `mmap()` maps file pages into virtual memory so programs use ordinary load/store operations.

### File Operations
Common POSIX operations are `open`, `read`, `write`, `lseek`, `close`, `unlink` (delete), `rename`, `stat` (get metadata), `chmod`, and `chown`.

## 🔬 Deep Dive
### File Types

| POSIX type | Description |
|------------|-------------|
| Regular file | Ordinary byte sequence |
| Directory | Contains name-to-inode mappings |
| Symbolic link | Stores path to another file |
| Block device | Addressable in blocks (disk) |
| Character device | Byte stream (terminal, serial port) |
| Named pipe (FIFO) | IPC via file-system path |
| Socket | Network/local IPC endpoint |

### Why Byte Sequences Matter
The power of the file abstraction is that programs can treat persistent storage as a sequence of bytes instead of reasoning about sectors, tracks, or flash pages. The OS and file system translate high-level file operations into low-level storage operations.

### Why UNIX Treats Many Things as Files
UNIX extends the file model beyond ordinary documents. Devices, pipes, and sockets appear in the same namespace so programs can often reuse familiar operations like `open`, `read`, and `write` across very different resources.

## 🏋️ Practice
### Warm-Up
What happens if you call `read()` repeatedly without `lseek()` on a random-access file descriptor?

### Core Problems
Why does UNIX represent devices as files?

### Challenge
Compare sequential I/O and `mmap()` for scanning a 1 GB file. What trade-offs change for performance and programming style?

## Supporting Chunks

- [[File Systems - Files are named persistent byte sequences managed by the OS]]
- [[File Systems - Directory trees impose hierarchy on flat storage via name-to-inode mappings]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 4.