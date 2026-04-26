---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Binary Heaps and Priority Queues"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Binary Heaps and Priority Queues

## Summary

Binary heaps are complete binary trees stored in arrays with heap property (parent <= children for min-heap). Insert via heapify-up O(log n), extract-min via heapify-down O(log n). Build-heap is O(n) bottom-up. Heapsort achieves O(n log n) in-place.

## Key Claims

1. Binary heaps achieve O(log n) insert and extract-min using array storage
2. Build-heap from unordered array takes O(n), not O(n log n)
3. Heap property is weaker than BST ordering
4. Heapsort is O(n log n) worst case and in-place but not stable
5. Array storage eliminates pointer overhead with excellent cache performance

## Atomic Facts

1. Parent of node i: floor((i-1)/2)
2. Children of node i: 2i+1 (left), 2i+2 (right)
3. Build-heap: process from n/2-1 down to 0 with heapify-down
4. Heapsort: build max-heap, repeatedly extract max
5. d-ary heap: d children per node, shallower tree
6. Priority queue: binary heap O(log n), Fibonacci heap O(1) amortized insert

## Significance

Binary heaps provide the simplest efficient implementation of priority queues, underpinning algorithms from Dijkstra to Huffman coding.

## Chunks Extracted

*Pending*
