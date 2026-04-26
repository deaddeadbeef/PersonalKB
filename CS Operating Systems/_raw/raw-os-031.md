---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Memory-Mapped Files"
authors: Kerrisk; Stevens, Rago
year: 2010
---

# Memory-Mapped Files

## Summary

Memory-mapped files use the `mmap()` system call to map a file (or a portion of it) directly into a process's virtual address space. Once mapped, the file's contents can be accessed via ordinary pointer dereferences and memory operations rather than explicit `read()`/`write()` system calls. The kernel handles the underlying I/O through the demand paging mechanism: pages of the file are loaded from disk into physical memory only when first accessed (triggering a page fault), and modified pages are written back to disk by the kernel's page writeback daemon (pdflush/kworker) or explicitly via `msync()`.

The `mmap()` call accepts several key parameters: the file descriptor, offset, length, protection flags (`PROT_READ`, `PROT_WRITE`, `PROT_EXEC`), and mapping flags. `MAP_SHARED` creates a mapping where writes are visible to other processes mapping the same file and are eventually propagated to the underlying file on disk. `MAP_PRIVATE` creates a copy-on-write mapping—writes create private copies of pages and are never written back to the file, useful for loading shared libraries where each process may modify its data segment. `MAP_ANONYMOUS` (with fd=-1) creates a mapping backed by zero-filled pages rather than a file, commonly used by `malloc()` for large allocations.

Memory-mapped files offer several advantages over traditional read/write I/O. They eliminate the double-copy problem: with `read()`, data is copied from the page cache to a user-space buffer, whereas `mmap()` allows the process to access the page cache directly. They simplify random access patterns—seeking to an offset is simply a pointer addition. They also enable efficient shared memory between processes: two processes mapping the same file with `MAP_SHARED` share the same physical pages.

Databases extensively use mmap. SQLite offers an mmap mode for read-heavy workloads. LMDB (Lightning Memory-Mapped Database) maps the entire database file and relies on the OS page cache for caching, using copy-on-write B+ trees for ACID transactions. MongoDB's original storage engine (MMAPv1) used mmap for data file access. However, mmap has limitations: error handling is via SIGBUS signals rather than return codes, writeback timing is controlled by the kernel unless `msync()` is called, and the kernel's page eviction decisions may not align with application-level access patterns.

## Key Claims

- mmap() maps file contents into virtual address space, enabling file I/O through pointer operations backed by the kernel's demand paging mechanism rather than explicit read/write system calls
- MAP_SHARED propagates writes to the underlying file and makes them visible to other processes, while MAP_PRIVATE creates copy-on-write mappings where writes are process-local and never reach the file
- Memory-mapped I/O eliminates one data copy compared to read() by allowing direct access to the kernel page cache, improving performance for random access workloads
- Shared memory between processes is efficiently implemented by having multiple processes mmap the same file with MAP_SHARED, as they share the same physical page frames
- Databases like LMDB rely entirely on mmap for data access, delegating caching to the OS page cache and using COW semantics for transactional isolation

## Atomic Facts

1. The `mmap()` prototype is `void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset)` and returns the mapped address or MAP_FAILED on error
2. `msync(addr, length, MS_SYNC)` forces dirty pages in the specified range to be written to disk synchronously, ensuring durability before the call returns
3. `munmap(addr, length)` removes the mapping; any dirty MAP_SHARED pages not yet flushed are still eventually written back by the kernel
4. On 64-bit systems, the virtual address space (typically 128 TB user space on x86-64) allows mapping files far larger than physical RAM, with the kernel paging portions in and out as needed
5. `MAP_ANONYMOUS | MAP_PRIVATE` is used by glibc's `malloc()` for allocations larger than the `mmap_threshold` (default 128 KB), bypassing the brk-based heap
6. LMDB achieves zero-copy reads by returning pointers directly into mmap'd pages, avoiding any buffer copies for read transactions

## Significance

Memory-mapped files bridge the gap between file I/O and memory operations, representing one of the most powerful abstractions in OS design. They underpin shared library loading, database engines, and inter-process shared memory. Understanding mmap is essential for performance-sensitive systems programming, as it reveals how the OS page cache, virtual memory, and file systems interact to enable efficient data access patterns.

## Chunks Extracted

*Pending*
