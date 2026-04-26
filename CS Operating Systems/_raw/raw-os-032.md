---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Copy-on-Write Mechanism"
authors: Silberschatz, Galvin, Gagne; Love
year: 2018
---

# Copy-on-Write Mechanism

## Summary

Copy-on-Write (COW) is a resource management optimization technique where a copy of a resource is deferred until a write operation actually occurs. In the context of operating systems, COW is most prominently used in the implementation of `fork()`: rather than immediately duplicating the parent process's entire address space, the kernel sets both parent and child page table entries to point to the same physical page frames and marks them read-only. When either process subsequently writes to a page, a page fault is triggered. The page fault handler detects the COW condition (by checking a COW bit or reference count), allocates a new physical frame, copies the original page content into it, updates the faulting process's page table to point to the new frame with write permissions, and resumes execution. The non-faulting process retains its mapping to the original page.

The page table implementation of COW typically uses a combination of the present bit, the read/write permission bit, and either a dedicated COW bit in a software-defined PTE field or the page frame's reference count. When a page fault occurs on a read-only page, the handler checks whether the page was originally writable (COW) or is genuinely read-only (true protection fault/segfault). If the reference count on the physical frame is 1 (no other process shares it), the kernel can simply re-enable write permission without copying.

COW is critical for fork+exec performance. In the common pattern where fork() is immediately followed by exec(), the child process replaces its entire address space, meaning none of the parent's pages are ever written by the child. Without COW, fork would needlessly copy potentially gigabytes of memory. With COW, only the page table entries themselves are duplicated (a few KB), and the exec replaces them entirely.

Beyond process creation, COW appears in several other OS contexts. Snapshot filesystems like Btrfs and ZFS use COW for metadata and data blocks: modifications create new blocks rather than overwriting existing ones, enabling instant snapshots and transactional writes. Virtual machine memory deduplication (KSM—Kernel Same-page Merging in Linux) identifies identical pages across VMs, merges them with COW protection, and only duplicates upon write. Private mmap mappings (`MAP_PRIVATE`) also use COW: writes create process-local copies of shared file-backed pages.

## Key Claims

- Copy-on-Write defers physical page duplication until a write actually occurs, transforming fork() from an O(n) memory copy into an O(page-table-size) operation
- The COW page fault handler distinguishes between COW faults (originally writable pages shared between processes) and genuine protection faults by checking reference counts or COW bits in page table entries
- In the common fork+exec pattern, COW ensures that zero data pages are physically copied because the child's exec() discards the entire address space before any writes occur
- COW extends beyond process creation to file systems (Btrfs, ZFS snapshots), VM memory deduplication (KSM), and private memory mappings, making it one of the most widely applied optimization techniques in OS design
- When a COW page's reference count drops to 1, the kernel can upgrade it to writable in place without copying, avoiding unnecessary duplication for the last remaining reference

## Atomic Facts

1. On Linux, fork() internally calls `copy_page_range()` which copies page table entries but increments reference counts on physical frames rather than allocating new frames
2. The x86 page table entry uses bit 1 (R/W) for write permission; the kernel clears this bit for COW pages and uses software-defined bits or struct page flags to distinguish COW from true read-only
3. KSM (Kernel Same-page Merging) scans for identical pages using content hashing, merges them to a single COW-protected frame, and is widely used in KVM virtualization to reduce host memory usage by 30–50% across similar VMs
4. Btrfs COW semantics mean that writing to a file block allocates a new block and updates the parent pointer, enabling instant snapshots by simply preserving the old root pointer
5. The `vfork()` system call was created before COW was implemented to avoid the cost of duplicating the address space; with COW, `vfork()` provides minimal additional benefit
6. A COW fault on a page in the zero page (a single kernel page of all zeros used for anonymous MAP_PRIVATE mappings) always allocates a new frame, since the zero page is never physically duplicated

## Significance

Copy-on-Write is one of the most important optimization techniques in operating systems, fundamentally enabling efficient process creation, filesystem snapshots, and memory deduplication. It exemplifies the lazy evaluation principle—deferring expensive work until absolutely necessary—which recurs throughout OS design. Without COW, the fork/exec process model would be impractically expensive for large processes, and modern containerization and virtualization workloads would require significantly more physical memory.

## Chunks Extracted

*Pending*
