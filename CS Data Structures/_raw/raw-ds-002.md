---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Linked Lists"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Linked Lists — Singly and Doubly Linked

## Summary

Singly linked lists store elements in nodes with data and next pointer. O(1) head insertion, O(n) random access. Doubly linked lists add prev pointer enabling O(1) deletion at known node. Sentinel nodes eliminate edge cases. Poor cache locality compared to arrays.

## Key Claims

1. Singly linked lists support O(1) head insertion but O(n) random access
2. Doubly linked lists enable O(1) deletion at known node via prev pointer
3. Sentinel nodes eliminate null-pointer edge cases
4. Linked lists have poor cache locality compared to arrays
5. Circular linking simplifies rotation and round-robin scheduling

## Atomic Facts

1. SLL node overhead: 1 pointer (8 bytes on 64-bit)
2. DLL node overhead: 2 pointers (16 bytes)
3. Floyd's cycle detection: slow/fast pointers, O(n) time, O(1) space
4. Reversing SLL: three-pointer technique, O(n) time
5. Java LinkedList is a doubly linked list
6. LRU cache: DLL + hash map gives O(1) get and put

## Significance

Linked lists demonstrate the fundamental trade-off between random access and insertion efficiency.

## Chunks Extracted

*Pending*
