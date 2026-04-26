---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Stacks Queues and Deques"
authors: [Allen Downey]
year: 2017
up: "[[Sources Index]]"
---

# Stacks, Queues, and Deques

## Summary

Stacks (LIFO), queues (FIFO), and deques (double-ended queues) are fundamental ADTs. All operations are O(1). Circular buffers provide efficient array-based queue implementation using modular arithmetic.

## Key Claims

1. Stack and queue operations are all O(1) regardless of implementation
2. Array-based stacks are simpler and more cache-friendly than linked-list stacks
3. Circular buffers eliminate wasted space in array queues
4. Deques can simulate both stacks and queues
5. Function call stacks use the stack ADT for activation records

## Atomic Facts

1. Stack apps: DFS, undo/redo, parenthesis matching, expression evaluation
2. Queue apps: BFS, task scheduling, buffering, print spooling
3. Python collections.deque: doubly-linked list of fixed-size blocks
4. Java ArrayDeque: circular buffer, preferred over LinkedList
5. Ring buffer: synonym for circular buffer, common in kernel I/O
6. Circular buffer full detection: count field or sacrifice one slot

## Significance

These three ADTs form the building blocks for graph traversal, scheduling, and buffering in virtually all software systems.

## Chunks Extracted

*Pending*
