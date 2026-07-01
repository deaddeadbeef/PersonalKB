---
tags: [cs-ds, linear]
up: "[[Linear Structures Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Arrays and Dynamic Arrays

> **One-line summary**: Arrays and dynamic arrays are the most fundamental contiguous data structures in computer science, providing direct index-based access to elements stored sequentially in memory.

## 🎯 Intuition
**The Core Idea:** Elements sit side-by-side in memory so any one can be reached instantly by its index.
**Analogy:** Think of a row of numbered mailboxes in an apartment lobby—knowing the number lets you go straight to the right box without checking every one in sequence. A dynamic array is like a lobby that builds a bigger row of mailboxes whenever it runs out, copying all letters over.
**Why It Matters:** Arrays underpin nearly every higher-level data structure—hash tables, heaps, and even graph adjacency lists are typically backed by arrays. Understanding their memory layout and resizing behavior is essential for writing cache-efficient, allocation-aware code.

---

## ⚙️ Core Mechanics
### How It Works
A **fixed-size array** allocates a single contiguous block of memory at creation time. Because elements are laid out at equal-width offsets from a base address, any element can be accessed in $O(1)$ time by computing `base + index * element_size`. This spatial locality also makes arrays highly cache-friendly, which is why they outperform pointer-based structures in practice for sequential access patterns.

A **dynamic array** (Java `ArrayList`, C++ `std::vector`, Python `list`) wraps a fixed array with automatic resizing. When the internal buffer is full, the runtime allocates a new buffer—typically twice the previous capacity—copies existing elements over, and releases the old buffer. Although a single resize costs $O(n)$, it occurs infrequently enough that appending is **amortized $O(1)$** by the aggregate or banker's method. The growth factor of 2x is the most common choice, though some implementations use 1.5x to trade slightly higher amortized cost for lower peak memory waste.

Capacity management is a key design concern. Shrinking too eagerly causes thrashing (repeated grow/shrink cycles), so most libraries only shrink on explicit request. Pre-allocating with a known capacity (`reserve`, `ensureCapacity`) avoids unnecessary copies when the final size is predictable.

### Key Operations

| Operation         | Fixed Array | Dynamic Array (amortized) |
|-------------------|:-----------:|:-------------------------:|
| Access by index   | $O(1)$        | $O(1)$                      |
| Search (unsorted) | $O(n)$        | $O(n)$                      |
| Append            | N/A         | $O(1)$ amortized            |
| Insert at index   | $O(n)$        | $O(n)$                      |
| Delete at index   | $O(n)$        | $O(n)$                      |
| Resize            | N/A         | $O(n)$ worst-case per event |

### Pseudocode
```
// Dynamic Array — append with amortized resize
function append(arr, item):
    if arr.size == arr.capacity:
        newCap = arr.capacity * 2
        newBuf = allocate(newCap)
        copy arr.buffer[0..size-1] → newBuf
        free arr.buffer
        arr.buffer = newBuf
        arr.capacity = newCap
    arr.buffer[arr.size] = item
    arr.size += 1

// Insert at index — shift right
function insertAt(arr, index, item):
    if arr.size == arr.capacity: resize(arr)
    for i = arr.size down to index + 1:
        arr.buffer[i] = arr.buffer[i - 1]
    arr.buffer[index] = item
    arr.size += 1

// Delete at index — shift left
function deleteAt(arr, index):
    for i = index to arr.size - 2:
        arr.buffer[i] = arr.buffer[i + 1]
    arr.size -= 1
```

### Key Facts
- Elements are stored in contiguous memory, enabling $O(1)$ random access via pointer arithmetic.
- Fixed arrays have a compile-time or allocation-time size that cannot change.
- Dynamic arrays grow by a multiplicative factor (commonly 2x) when capacity is exceeded.
- Amortized analysis (aggregate or potential method) proves append is $O(1)$ amortized.
- Insertion or deletion in the middle requires shifting elements, costing $O(n)$.
- Memory overhead for a dynamic array is at most 2x the number of stored elements (worst case right after doubling).
- Cache performance is superior to linked structures due to spatial locality.
- Most languages provide built-in dynamic arrays: Python `list`, Java `ArrayList`, C++ `std::vector`, Go `slice`.

---

## 🔬 Deep Dive
### Implementation Variants
- **Fixed / static array** — size set at compile time (C `int a[100]`) or allocation time (`malloc`). No resize capability; caller manages bounds.
- **Dynamic array** — automatic doubling on overflow. C++ `std::vector` uses 2x growth; MSVC's `std::vector` uses 1.5x. Python `list` over-allocates by ~12.5% for small sizes and ramps up.
- **Gap buffer** — variant used in text editors (Emacs). Keeps a moveable gap in the middle of the array so inserts near the cursor are $O(1)$.
- **Hashed Array Tree** — uses a top-level array of pointers to fixed-size leaf arrays; avoids the $O(n)$ copy on resize at the cost of an extra indirection.

### Cache and Memory Analysis
- A contiguous array of 64-bit integers fills a 64-byte cache line with 8 elements. Sequential iteration hits every element without a cache miss, giving ~10× throughput over pointer-chasing in a linked list.
- Dynamic arrays waste up to 50% capacity right after a 2x resize. The 1.5x factor reduces peak waste to ~33% but increases the frequency of copies.
- Memory overhead per element: **0 bytes** beyond the element itself (compared to 8–16 bytes per node in a linked list).

### Edge Cases and Pitfalls
- **Off-by-one errors** — fence-post mistakes in loop bounds are the most common array bug.
- **Empty array** — accessing index 0 on an empty dynamic array is undefined behaviour in C++ and throws in Java/Python.
- **Resize thrashing** — alternating push/pop at the capacity boundary can trigger repeated resizes if the shrink policy is too aggressive.
- **Integer overflow in index arithmetic** — `(low + high) / 2` overflows for large indices; use `low + (high - low) / 2`.

### Real-World Usage
- **Hash tables** — open-addressing and separate-chaining both use arrays as the backing store.
- **Heaps / priority queues** — a binary heap is stored in a flat array with parent at `i/2`, children at `2i` and `2i+1`.
- **Adjacency lists** — graph representations store neighbour lists as dynamic arrays.
- **Columnar databases** — Parquet, Arrow, and DuckDB store columns as contiguous arrays for vectorised SIMD processing.
- **Binary search** — $O(\log n)$ search requires $O(1)$ random access, which only arrays provide efficiently → see [[Binary Search]].

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the amortized cost of `n` consecutive appends to an initially empty dynamic array that doubles on overflow? Explain using the aggregate method.
2. Why is inserting at index 0 of a dynamic array $O(n)$ while appending is $O(1)$ amortized?
3. A dynamic array has capacity 8 and size 8. After one more append, what is the new capacity and how many elements were copied?

### Core Problems
1. **Rotate Array** (LeetCode 189) — Given an array, rotate it to the right by `k` steps. Solve in $O(n)$ time and $O(1)$ space using the three-reverse trick.
2. **Merge Sorted Arrays** (LeetCode 88) — Merge `nums2` into `nums1` in-place. Start from the back to avoid overwriting. Expected approach: two pointers from end.

### Challenge
1. **Median of Two Sorted Arrays** (LeetCode 4) — Find the median of two sorted arrays in $O(\log(min(m,n)$)) time using binary search on partition indices. Connects arrays to [[Binary Search]] in a non-trivial way.

---

*See also:* [[Singly Linked Lists]] | [[Queues and Deques]] | [[CS Data Structures/Hash-Based Structures/Hash Tables and Hash Functions|Hash Tables]] | [[CS Data Structures/Heaps and Priority Queues/Heaps and Priority Queues Overview|Heaps and Priority Queues]] | **CS Algorithms:** [[Binary Search]], [[Merge Sort]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-002 Arrays provide O1 random access via base address arithmetic|Arrays provide O(1) random access via base-address arithmetic]]
- [[CS Data Structures/_chunks/chunk-ds-001 Dynamic arrays achieve amortized O1 append via geometric resizing|Dynamic arrays achieve amortized O(1) append via geometric resizing]]
- [[CS Data Structures/_chunks/chunk-ds-061 Cache locality makes arrays 10-100x faster for iteration|Cache locality makes arrays much faster for iteration]]
- [[CS Data Structures/_chunks/chunk-ds-111 Growth factor 1.5x vs 2x trades memory for copies|Growth factor 1.5x vs 2x trades memory for copy frequency]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
