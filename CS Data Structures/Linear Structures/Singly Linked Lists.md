---
tags: [cs-ds, linear]
up: "[[Linear Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Singly Linked Lists

> **One-line summary**: A singly linked list is a linear collection of nodes where each node stores a data element and a pointer to the next node, enabling efficient insertion at the head but requiring sequential traversal for search.

## 🎯 Intuition
**The Core Idea:** Nodes are scattered in memory, each one holding a clue to where the next one lives—follow the chain to traverse the list.
**Analogy:** Imagine a scavenger hunt: each clue card has a fun fact *and* directions to the next clue. You can't jump to clue #7 directly—you have to follow every clue in order. But adding a brand-new first clue is instant: just write "go here first" on a new card and hand it to the next player.
**Why It Matters:** Singly linked lists are the building block for stacks, queues, adjacency lists, and hash-table chaining. They introduce the pointer-based thinking essential for trees, graphs, and memory management.

---

## ⚙️ Core Mechanics
### How It Works
Each **node** in a singly linked list contains two fields: a `data` payload and a `next` pointer referencing the subsequent node (or `null` at the tail). The list itself is represented by a `head` pointer. Unlike arrays, linked lists do not require contiguous memory, so insertions and deletions at the head take $O(1)$ time without any shifting. However, accessing the k-th element requires walking k pointers, making random access $O(n)$.

**Figure:** Singly linked list — each node holds data and a pointer to the next node

```mermaid
flowchart LR
    Head --> A["10 | next"] --> B["20 | next"] --> C["30 | next"] --> Null["null"]
    style Head fill:#4CAF50,color:#fff
    style Null fill:#999,color:#fff
```

**Floyd's cycle detection** (tortoise and hare) is the classic algorithm for detecting loops: a slow pointer advances one step per iteration while a fast pointer advances two. If they meet, a cycle exists; the meeting point can then be used to find the cycle's entry node. This runs in $O(n)$ time and $O(1)$ space.

Common operations include **in-place reversal** (iteratively reassigning `next` pointers using three tracking variables: `prev`, `curr`, `next`) and **merging two sorted lists** (a two-pointer merge identical in spirit to merge sort's merge step, running in $O(n + m)$ time). These patterns recur frequently in both algorithmic problems and production code such as memory allocators.

### Key Operations

| Operation               | Time | Space |
|-------------------------|:----:|:-----:|
| Insert at head          | $O(1)$ | $O(1)$  |
| Insert at tail (no ref) | $O(n)$ | $O(1)$  |
| Search                  | $O(n)$ | $O(1)$  |
| Delete at head          | $O(1)$ | $O(1)$  |
| Delete by value         | $O(n)$ | $O(1)$  |
| Cycle detection         | $O(n)$ | $O(1)$  |
| Reverse                 | $O(n)$ | $O(1)$  |

### Pseudocode
```
// Insert at head
function insertHead(list, item):
    newNode = new Node(item)
    newNode.next = list.head
    list.head = newNode

// Delete at head
function deleteHead(list):
    if list.head == null: error "List empty"
    item = list.head.data
    list.head = list.head.next
    return item

// In-place reversal (iterative)
function reverse(list):
    prev = null
    curr = list.head
    while curr != null:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    list.head = prev

// Floyd's cycle detection
function hasCycle(head):
    slow = head
    fast = head
    while fast != null and fast.next != null:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return true
    return false
```

### Key Facts
- Each node holds `data` and a single `next` pointer; the list is accessed via a `head` reference.
- Insertion at the head is $O(1)$; insertion at an arbitrary position requires $O(n)$ traversal to find the predecessor.
- Search is $O(n)$ since elements must be visited sequentially.
- Deletion of a node requires access to its predecessor, also $O(n)$ in the worst case.
- Floyd's tortoise-and-hare algorithm detects cycles in $O(n)$ time and $O(1)$ space.
- In-place reversal uses three pointers (`prev`, `curr`, `next`) and runs in $O(n)$.
- Merging two sorted linked lists is $O(n + m)$ with $O(1)$ extra space.
- Memory overhead per element is one pointer (typically 4–8 bytes) compared to zero for arrays.

---

## 🔬 Deep Dive
### Implementation Variants
- **Plain head pointer** — simplest form. Requires null checks for empty list on every operation.
- **Head + tail pointer** — adding a `tail` reference makes append $O(1)$ at the cost of maintaining one extra pointer on insert/delete-at-tail.
- **Dummy head (sentinel)** — a sentinel node before the real first element eliminates special-case code for head operations. Widely used in interview solutions.
- **Self-organising lists** — move-to-front, transpose, or count-based heuristics improve average search time for skewed access patterns.
- **Skip list** — a probabilistic extension of linked lists with $O(\log n)$ search. Used in Redis sorted sets and LevelDB/RocksDB memtables.

### Cache and Memory Analysis
- Per-node overhead: one pointer (8 bytes on 64-bit) plus allocator metadata (typically 16 bytes for `malloc`). A list of 1M 8-byte integers costs ~32 MB vs. ~8 MB in a flat array.
- Each `node.next` dereference is likely a cache miss because nodes are heap-allocated at arbitrary addresses. This makes linked-list traversal 5–10× slower than array iteration for sequential access.
- **Arena/pool allocation** — allocating all nodes from a contiguous arena restores some spatial locality. Practical in game engines and embedded systems.
- Prefetching doesn't help: the CPU can't predict the next address until the current node is loaded.

### Edge Cases and Pitfalls
- **Null pointer dereference** — accessing `node.next` when `node` is null is the #1 linked-list bug. Always guard with null checks or use a sentinel.
- **Losing the list** — overwriting `head` without saving `head.next` first during reversal or deletion orphans the rest of the list.
- **Cycle creation** — accidentally setting a node's `next` to an earlier node creates an infinite loop. Floyd's algorithm is the canonical check.
- **Off-by-one on tail** — deleting the last node when using a head+tail design requires updating `tail`, which needs traversal ($O(n)$) since there's no `prev` pointer.

### Real-World Usage
- **Hash-table chaining** — each bucket is a singly linked list of entries with the same hash. Used in Java `HashMap` (up to a threshold; then switches to a tree).
- **Free lists in memory allocators** — `malloc` implementations (ptmalloc, jemalloc) maintain free-block lists as singly linked lists threaded through the free blocks themselves.
- **Adjacency lists** — graph representations where each vertex stores a linked list of its neighbors.
- **Polynomial representation** — each term is a node with coefficient and exponent; addition is a sorted merge → connects to [[Merge Sort]].
- **Undo stacks** — a stack implemented as a singly linked list where each node is an action; the head is the most recent action.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the time complexity of accessing the k-th element in a singly linked list? Why can't you do better?
2. Why is insertion at the head $O(1)$ but insertion at an arbitrary index $O(n)$?
3. How does Floyd's algorithm detect a cycle without using extra space?

### Core Problems
1. **Reverse Linked List** (LeetCode 206) — Reverse a singly linked list iteratively and recursively. The iterative approach uses the `prev/curr/next` pattern from the pseudocode above. $O(n)$ time, $O(1)$ space.
2. **Merge Two Sorted Lists** (LeetCode 21) — Two-pointer merge identical to the merge step in [[Merge Sort]]. Use a dummy head to simplify the code. $O(n + m)$ time, $O(1)$ space.

### Challenge
1. **Reverse Nodes in k-Group** (LeetCode 25) — Reverse every group of `k` nodes in a linked list. If the remaining nodes are fewer than `k`, leave them as-is. Combines reversal, length counting, and pointer reconnection in one problem. Tests mastery of all singly-linked-list pointer manipulations.

---

*See also:* [[Doubly Linked Lists and Circular Lists]] | [[Stacks]] | [[Arrays and Dynamic Arrays]] | [[Hash Tables]] | **CS Algorithms:** [[Merge Sort]], [[BFS and DFS]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-003 Floyds cycle detection in On time O1 space|Floyd's cycle detection in O(n) time and O(1) space]]
- [[CS Data Structures/_chunks/chunk-ds-081 Sentinel nodes eliminate edge cases in linked lists|Sentinel nodes eliminate linked-list edge cases]]

## References

- [[CS Data Structures/Sources/Sources Index|Sources Index]]
