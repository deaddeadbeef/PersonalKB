---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
confidence: verified
freshness: stable
---

# DS Review — Linear Structures

## Quick-Fire Questions

1. What is the amortized cost of appending to a dynamic array? Why?
2. How does Floyd's cycle detection work? What are the two phases?
3. When would you use a DLL over a SLL?
4. What is the advantage of a circular buffer over a linked queue?
5. How do you implement a queue using two stacks?

## Compare and Contrast

| Structure | Access | Insert Head | Insert Tail | Delete Known | Cache |
|-----------|--------|-------------|-------------|-------------|-------|
| Array | $O(1)$ | $O(n)$ | $O(1)$* | $O(n)$ | Excellent |
| SLL | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ | Poor |
| DLL | $O(n)$ | $O(1)$ | $O(1)$ | $O(1)$ | Poor |
| Circular Buffer | $O(1)$ | $O(1)$ | $O(1)$ | N/A | Excellent |

*Amortized for dynamic arrays

## Orientation

- Separate abstract operations from concrete layout: arrays win on indexing and locality, while linked structures win when pointer updates are the real task.
- Ask whether the interface is stack-like, queue-like, or random-access before choosing an implementation.
- Remember that circular buffers are often the practical queue/deque answer when fixed-capacity or bounded growth is acceptable.

## Common Traps

- Confusing amortized append for worst-case append in dynamic arrays.
- Assuming linked lists are "faster inserts" without asking whether the target position is already known.
- Ignoring cache behavior when comparing pointer-heavy nodes against contiguous arrays.

## Practice Loop

1. Justify when a [[Doubly Linked Lists and Circular Lists|doubly linked list]] is worth the extra pointers.
2. Explain why a [[Circular Buffers|circular buffer]] can outperform a linked queue in practice.
3. Sketch how [[Queues and Deques|a queue]] can be implemented with two [[Stacks|stacks]].

## References

- [[Linear Structures Overview]]
- [[Arrays and Dynamic Arrays]]
- [[Singly Linked Lists]]
- [[Doubly Linked Lists and Circular Lists]]
- [[Stacks]]
- [[Queues and Deques]]
- [[Circular Buffers]]
- [[Memory Layout and Cache Performance]]
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
