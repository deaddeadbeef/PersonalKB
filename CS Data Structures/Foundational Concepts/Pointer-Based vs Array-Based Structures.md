---
tags: [cs-ds, foundational]
up: "[[Foundational Concepts Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
created: 2025-07-14
---
# Pointer-Based vs Array-Based Structures

> **One-line summary**: The choice between contiguous (array-based) and linked (pointer-based) storage is the most fundamental implementation decision in data-structure design, governing access speed, insertion cost, memory overhead, and cache behavior.

## 🎯 Intuition
(2-min read. No jargon. Build mental picture.)

**The Core Idea:** Every data structure stores elements either packed together in a block (array-based) or scattered across memory with links between them (pointer-based). This one decision shapes everything else.

**Analogy:** Think of two ways to organize a music collection. **Array-based** is a CD binder — albums stored in numbered slots, side by side. Want track #47? Flip straight to slot 47 (instant access). Want to insert a new album in the middle? You have to shift everything after it down one slot (expensive). **Pointer-based** is a treasure hunt — each CD case has a note saying "next album is in the kitchen drawer." Finding a specific album means following clues one by one (slow search), but inserting a new album just means rewriting two notes (cheap insertion). The binder is fast to browse; the treasure hunt is easy to rearrange.

**Why It Matters:** Nearly every data-structure implementation question reduces to this choice or a blend of both strategies. Understanding the contiguous-vs-linked tradeoff — and its cache implications — prevents the common mistake of selecting a structure based on Big-O alone while ignoring constant-factor performance gaps that dominate in practice.

---

## ⚙️ Core Mechanics
(Textbook level. Definitions, operations, complexity.)

### How It Works

**Array-based structures** store elements in a single contiguous block of memory. This gives $O(1)$ random access by index — address = base + index × element_size — and superb cache performance because sequential elements share cache lines. The trade-off is rigidity: inserting or deleting in the middle requires shifting $O(n)$ elements, and growing beyond the allocated capacity requires a full reallocation and copy (though amortized doubling keeps appends at $O(1)$). Arrays also waste space when sparsely filled, since the block is allocated to maximum capacity.

**Pointer-based structures** (linked lists, tree nodes, graph adjacency lists) store each element in a separately allocated node connected by pointers. Insertion and deletion at a **known position** are $O(1)$ — just redirect pointers — making them ideal when the structure changes shape frequently and positions are tracked. However, reaching that position via traversal is $O(n)$ for lists and $O(\log n)$ for balanced trees. Each node carries pointer overhead (8 bytes per pointer on 64-bit systems), and nodes scattered across the heap destroy spatial locality, leading to cache-miss-dominated performance.

**Hybrid approaches** combine the strengths of both. An **unrolled linked list** stores a small array in each node, preserving some locality while keeping $O(1)$ link-based insertion between blocks. A **B-tree** packs many keys per node (array-based) and links nodes with pointers, delivering cache-friendly search with dynamic structure. **Array-mapped tries** (used in Clojure's persistent vectors) use a tree of small arrays. **Memory pools** allocate linked-structure nodes from a contiguous arena, recovering spatial locality. In practice, profiling often reveals that a simple dynamic array outperforms a linked list even for workloads that theoretically favor the latter, purely due to cache effects.

### Key Operations

| Operation                  | Dynamic Array        | Singly Linked List     | Doubly Linked List     |
|----------------------------|----------------------|------------------------|------------------------|
| Access by index            | $O(1)$                 | $O(n)$                   | $O(n)$                   |
| Append (end)               | $O(1)$ amortized       | $O(1)$ with tail pointer | $O(1)$                   |
| Prepend (front)            | $O(n)$                 | $O(1)$                   | $O(1)$                   |
| Insert at position *i*     | $O(n)$                 | $O(n)$ find + $O(1)$ link  | $O(n)$ find + $O(1)$ link  |
| Delete at position *i*     | $O(n)$                 | $O(n)$ find + $O(1)$ unlink| $O(n)$ find + $O(1)$ unlink|
| Search (unsorted)          | $O(n)$                 | $O(n)$                   | $O(n)$                   |
| Memory per element         | element size only    | element + 1 pointer    | element + 2 pointers   |
| Cache performance          | Excellent            | Poor                   | Poor                   |

### Key Facts

- Array index access is $O(1)$ and touches one cache line; pointer dereference is $O(1)$ but may trigger a cache miss.
- Mid-array insertion is $O(n)$ due to shifting; linked-list insertion at a known node is $O(1)$.
- Pointer overhead: each pointer costs 8 bytes (64-bit), so a doubly linked list of 4-byte integers wastes 16 bytes per 4 bytes of payload.
- Dynamic arrays (vector, ArrayList) amortize growth cost to $O(1)$ per append via capacity doubling.
- Linked lists excel when you splice, merge, or reorder frequently and already hold node references (e.g., LRU caches with a hash map of node pointers).
- Arrays are strictly superior for iteration-heavy, read-heavy, and small-collection workloads.
- **Unrolled linked lists** and **B-trees** are the most common hybrids, bridging the locality gap.
- Language-level defaults reflect this: C++ `std::vector`, Java `ArrayList`, Python `list` are all array-based; linked lists are opt-in for specific needs.

---

## 🔬 Deep Dive
(Proofs, edge cases, real-world tradeoffs)

### Formal Properties

- **Random access theorem**: Array-based access is $\Theta(1)$ because address computation is a single arithmetic operation. Pointer-based access requires traversal, giving $\Theta(k)$ to reach the k-th element — this is an inherent property of the data layout, not an implementation artifact.
- **Amortized doubling proof**: Starting from capacity 1, after *n* appends, total copy cost = 1 + 2 + 4 + ... + n ≤ 2n. Amortized cost per append = (n + 2n) / n = 3 = $O(1)$. This fails for additive growth (capacity += k): total copy cost becomes $\Theta(n²/k)$ = $\Theta(n²)$.
- **Space overhead bounds**: An array-based structure with doubling wastes at most 50% space (capacity up to 2× size). A singly linked list wastes exactly one pointer per element. A doubly linked list wastes two pointers per element. For small elements, pointer overhead can exceed payload size.
- **Lower bound on list search**: Without additional indexing structure, any linked list search requires $\Omega(n)$ comparisons in the worst case because there is no way to skip nodes without examining them.

### Edge Cases and Pitfalls

- **Iterator invalidation**: Dynamic arrays invalidate all iterators and pointers on reallocation. Linked lists never invalidate iterators to other nodes during insertion/deletion. This is a critical correctness concern in C++ (dangling pointers) and Java (ConcurrentModificationException).
- **Memory fragmentation**: Per-node allocation of linked structures fragments the heap over time, increasing allocator overhead and GC pause times. Arena allocation or memory pools mitigate this.
- **Doubling waste with large elements**: If each element is 1 KB and the array doubles from 10,000 to 20,000, you've just allocated 10 MB of unused space. For large elements, consider storing pointers-to-elements in the array instead.
- **The "linked list is dead" argument**: Bjarne Stroustrup (C++ creator) demonstrated in benchmarks that `std::vector` (array-based) beats `std::list` (linked) even for mid-list insertions up to millions of elements, because the cache-miss cost of traversal dominates the shift cost.
- **Persistent data structures**: Linked structures enable cheap persistence (sharing structure between versions) via path copying. Arrays require full copy for persistence, making them $O(n)$ per version.

### Real-World Usage

- **C++ STL defaults**: `std::vector` is the default container per C++ Core Guidelines; `std::list` and `std::forward_list` are reserved for specific use cases (constant-time splice, iterator stability).
- **Java `ArrayList` vs `LinkedList`**: Java's own documentation recommends `ArrayList` as the general-purpose `List` implementation. `LinkedList` implements `Deque` and is used primarily as a queue/deque.
- **Linux kernel `list_head`**: The kernel uses intrusive doubly linked lists extensively — nodes embed the link pointers directly, avoiding separate allocation and enabling $O(1)$ insertion/removal in scheduler queues, driver lists, etc.
- **Clojure persistent vectors**: Use a 32-way branching array-mapped trie — essentially a tree of small arrays — achieving $O(log₃₂ n)$ ≈ $O(1)$ practical access with structural sharing for persistence.
- **Game engines**: Almost universally prefer array-based storage (contiguous buffers, SOA layouts) for entity data to maximize cache throughput during frame updates.

---

## 🏋️ Practice

### Warm-Up (5 min)
1. A doubly linked list stores 4-byte integers. On a 64-bit system, what fraction of each node's memory is actual data vs. pointer overhead?
2. You need a container that supports fast prepend and fast index access. Neither array nor linked list excels at both. What hybrid structure could help?
3. Why does C++ default to `std::vector` even for workloads with occasional mid-list insertions? What hardware property makes this rational?

### Core Problems
1. **Break-Even Analysis** — Given an array of *n* 4-byte integers with appends and random mid-list insertions, calculate the break-even point where a linked list's $O(1)$ insertion advantage overcomes the array's cache advantage. Assume: array shift = 1 ns/element (cache-hot); linked list node allocation + cache miss = 100 ns per insertion. At what *n* does the linked list win? (Expected approach: Array insertion cost at position n/2 ≈ n/2 ns. Linked list cost ≈ 100 + traversal. Break-even at n ≈ 200, but traversal cost makes the linked list lose until n is very large and insertions are at known positions.)
2. **Memory Pool Design** — Implement a fixed-size memory pool (arena allocator) for linked-list nodes. The pool pre-allocates a contiguous block of *N* nodes. `alloc()` returns the next free node in $O(1)$; `free()` returns it to a free list in $O(1)$. Measure the cache performance improvement vs. `malloc`-per-node for 1,000,000 insertions. (Expected approach: free list as a singly linked list within the pool array; benchmark with `perf stat` cache-miss counters.)

### Challenge
**Unrolled Linked List Implementation** — Implement an unrolled linked list where each node holds an array of up to *K* elements. Support `insert(i, val)`, `delete(i)`, `get(i)`, and `iterate()`. Choose *K* to optimize for 64-byte cache lines with 4-byte integers. Analyze the time complexity of each operation and benchmark against `std::vector` and `std::list` for a mixed insertion/iteration workload.

---

*See also:* [[Memory Layout and Cache Performance]] | [[Abstract Data Types]] | [[Arrays and Dynamic Arrays|Dynamic Arrays]] | Linked Lists | [[Data Structure Comparison and Selection]] | **CS Algorithms:** Algorithm Implementation Strategies | Cache-Aware Algorithm Design

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-002 Arrays provide O1 random access via base address arithmetic|Arrays provide O(1) random access via address arithmetic]]
- [[CS Data Structures/_chunks/chunk-ds-001 Dynamic arrays achieve amortized O1 append via geometric resizing|Dynamic arrays achieve amortized O(1) append]]
- [[CS Data Structures/_chunks/chunk-ds-061 Cache locality makes arrays 10-100x faster for iteration|Cache locality makes arrays much faster for iteration]]
- [[CS Data Structures/_chunks/chunk-ds-122 Intrusive linked lists embed pointers inside elements|Intrusive linked lists embed pointers inside elements]]
- [[CS Data Structures/_chunks/chunk-ds-139 Arena allocation frees all memory in one shot|Arena allocation can recover locality for node-heavy structures]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
