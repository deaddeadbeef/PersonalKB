---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Memory Allocation: Buddy System"
authors: Silberschatz, Galvin, Gagne; Tanenbaum, Bos
year: 2018
---

# Memory Allocation: Buddy System

## Summary

The buddy system is a memory allocation algorithm that partitions available memory into blocks whose sizes are powers of two. When a process requests memory, the allocator finds the smallest power-of-two block that satisfies the request. If no block of that size exists, a larger block is recursively split in half—each half being the other's "buddy"—until a block of the correct size is produced. When a block is freed, the allocator checks whether its buddy is also free; if so, the two are coalesced back into a single block of the next larger size, and this coalescing propagates upward as far as possible.

The primary advantage of the buddy system is fast coalescing: computing a buddy's address requires only a single bit-flip operation on the block address, making the merge check O(1). The primary disadvantage is internal fragmentation—a request for 65 KB, for example, receives a 128 KB block, wasting nearly half the space. On average, the buddy system wastes about 25% of allocated memory to internal fragmentation.

Linux uses a buddy allocator as the foundation of its physical page frame allocator. The kernel maintains free lists for orders 0 through 10 (corresponding to 1 page through 1024 contiguous pages, i.e., 4 KB to 4 MB on x86). The `/proc/buddyinfo` file exposes the current state of these free lists per zone (DMA, Normal, HighMem). On top of the buddy allocator, Linux layers the slab allocator, which handles small, frequently-allocated kernel objects (task_struct, inode, dentry). The slab allocator pre-allocates caches of objects at specific sizes, eliminating the per-object overhead of calling the buddy allocator directly. `kmalloc()` is the kernel's general-purpose slab-backed allocator, providing power-of-two-sized allocations from 8 bytes to 8 KB.

Linux has shipped three slab allocator implementations: SLAB (the original, cache-coloring aware), SLUB (the current default, simpler with better NUMA behavior), and SLOB (a minimal allocator for embedded systems with tight memory). SLUB eliminated per-CPU queues and complex bookkeeping from SLAB, improving scalability on modern multicore systems while reducing memory overhead for the allocator metadata itself.

## Key Claims

- The buddy system restricts all allocation sizes to powers of two, enabling O(1) buddy address computation via bit manipulation and efficient coalescing of adjacent free blocks
- Internal fragmentation averages approximately 25% because requests are rounded up to the next power of two, wasting the difference
- Linux's physical page allocator uses a buddy system with orders 0–10, managing contiguous runs of 1 to 1024 pages per allocation
- The slab allocator layers atop the buddy system to efficiently manage small, frequently-allocated kernel objects without per-object buddy overhead
- SLUB replaced SLAB as the default Linux slab allocator due to simpler design, better NUMA scalability, and reduced metadata overhead

## Atomic Facts

1. A buddy pair is two blocks of equal size whose addresses differ by exactly one bit at the position corresponding to the block's order
2. Splitting a 2^k block produces two 2^(k-1) buddies; coalescing reverses this when both buddies are free
3. The Linux buddy allocator manages per-zone free lists (DMA, DMA32, Normal, HighMem) independently to respect hardware addressing constraints
4. kmalloc() allocates from SLUB caches in sizes 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and 8192 bytes
5. SLAB introduced cache coloring to reduce cache line conflicts by offsetting objects within a slab page, but this added complexity that SLUB chose to eliminate
6. SLOB uses a simple first-fit linked-list allocator with approximately 2 KB of code, targeting systems with less than 16 MB RAM

## Significance

The buddy system is one of the most influential memory allocation algorithms in operating systems design. Its combination of fast allocation, deterministic coalescing, and simple address arithmetic has made it the standard for physical page management in production kernels. The layered approach—buddy for pages, slab for objects—demonstrates a fundamental OS design pattern: use a coarse-grained allocator for large units and a specialized cache for fine-grained frequent allocations.

## Chunks Extracted

- [[chunk-os-131 Buddy System Powers of Two Enable O(1) Coalescing]]
- [[chunk-os-132 Buddy System Internal Fragmentation Averages 25 Percent]]
- [[chunk-os-133 Linux Buddy Allocator Per-Zone Free Lists Orders 0-10]]
- [[chunk-os-134 Slab Allocator Layers Atop Buddy for Kernel Objects]]
