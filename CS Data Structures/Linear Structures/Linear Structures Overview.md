---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
confidence: verified
---
# Linear Structures Overview

Linear structures arrange elements in a sequential order where each item has at most one predecessor and one successor. They are the workhorses of everyday programming: function-call stacks, task queues, resizable lists, and streaming buffers all rely on some form of linear storage. This hub traces the family from the simplest contiguous array to specialised queue variants tuned for concurrency and bounded memory.

## Arrays and Linked Lists

The **array** offers $O(1)$ random access and excellent cache locality but pays $O(n)$ for insertions in the middle. **Dynamic arrays** (e.g., `std::vector`, Python's `list`) amortise resizing to $O(1)$ append. When frequent insertions or deletions at arbitrary positions dominate, **singly linked lists** trade random access for $O(1)$ pointer surgery. **Doubly linked lists** add backward traversal and $O(1)$ removal given a node reference, while **circular lists** elegantly model round-robin schedules and ring topologies.

## Stacks, Queues, and Deques

**Stacks** enforce last-in-first-out access — central to expression evaluation, undo systems, and DFS traversal. **Queues** provide first-in-first-out order for BFS, task scheduling, and message passing. The **deque** (double-ended queue) generalises both, supporting efficient push and pop at either end. Each can be backed by an array or a linked list, and the choice hinges on workload patterns and memory constraints explored in the Foundational Concepts hub.

## Circular Buffers

A **circular buffer** (ring buffer) wraps a fixed-size array so that producers and consumers chase each other around the same block of memory. It avoids shifting elements on dequeue, delivers predictable latency, and is a staple of embedded systems, audio pipelines, and lock-free inter-thread communication. Understanding its modular arithmetic is a gateway to bounded-memory streaming designs.

## Lock-Free Linear Structures

In concurrent systems, traditional locks introduce contention and potential deadlock. **Lock-free queues and stacks** use atomic compare-and-swap (CAS) operations to allow multiple threads to push and pop without mutual exclusion. These structures are critical in high-throughput message-passing systems, real-time schedulers, and garbage collectors.

## Pages in This Hub

- [[Arrays and Dynamic Arrays]]
- [[Singly Linked Lists]]
- [[Doubly Linked Lists and Circular Lists]]
- [[Stacks]]
- [[Queues and Deques]]
- [[Circular Buffers]]
- [[Lock-Free Queues and Stacks]]

## Related Hubs

- [[Foundational Concepts Overview]] — ADTs, complexity, and memory trade-offs underlying every linear structure
- [[Hash-Based Structures Overview]] — arrays as the backbone of hash tables
- [[Heaps and Priority Queues Overview]] — array-backed heaps as a specialised linear layout

## References
- [[CS Data Structures/Sources/Sources Index|CS Data Structures Sources Index]]
