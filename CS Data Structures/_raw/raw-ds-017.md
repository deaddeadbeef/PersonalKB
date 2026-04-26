---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Fibonacci Heaps"
authors: [Jeff Erickson]
year: 2019
up: "[[Sources Index]]"
---

# Fibonacci Heaps

## Summary

Fibonacci heaps achieve O(1) amortized insert, merge, decrease-key and O(log n) extract-min. Lazy consolidation and cascading cuts maintain bounded degree. Enable Dijkstra in O(E + V log V). Complex implementation limits practical use.

## Key Claims

1. O(1) amortized insert, merge, decrease-key
2. Extract-min triggers lazy consolidation in O(log n) amortized
3. Cascading cuts ensure tree degrees remain O(log n)
4. Enable theoretically optimal graph algorithms
5. Rarely used in practice due to complexity and constants

## Atomic Facts

1. Fredman and Tarjan, 1987: invented Fibonacci heaps
2. Max node degree: O(log n), related to Fibonacci numbers
3. Marked nodes: cut if they lose a second child
4. Pairing heaps: simpler practical alternative
5. Strict Fibonacci heaps: worst-case O(1) decrease-key
6. In practice: binary or pairing heaps preferred

## Significance

Fibonacci heaps represent a theoretical ideal for priority queues and demonstrate the power of lazy evaluation in data structure design.

## Chunks Extracted

*Pending*
