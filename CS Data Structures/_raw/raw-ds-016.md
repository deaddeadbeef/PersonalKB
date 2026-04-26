---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Splay Trees"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Splay Trees — Self-Adjusting BSTs

## Summary

Splay trees restructure on every access by rotating accessed node to root via zig, zig-zig, zig-zag. No balance info stored. O(log n) amortized. Working set property: recent elements near root. Conjectured dynamically optimal.

## Key Claims

1. O(log n) amortized without storing balance information
2. Splay moves accessed node to root via three rotation types
3. Working set property adapts to access patterns
4. Conjectured dynamically optimal (unproven)
5. Simpler nodes due to no balance metadata

## Atomic Facts

1. Sleator and Tarjan, 1985: introduced splay trees
2. Three cases: zig, zig-zig, zig-zag
3. Static optimality: constant factor of optimal static BST
4. Worst-case single operation: O(n)
5. Applications: caches, garbage collectors, routing
6. Amortized analysis via potential method

## Significance

Splay trees show that self-adjustment without explicit balance information can achieve optimal amortized performance.

## Chunks Extracted

*Pending*
