---
tags: [cs-os, chunk]
source: "[[raw-os-008]]"
confidence: high
supports:
  - "[[Page Replacement]]"
qna_seeds:
  - "Q: How does the Clock (second-chance) algorithm work? A: Pages are arranged in a circular buffer. The hand inspects each page's reference bit: if set, it clears the bit and advances (second chance); if clear, that page is evicted. This approximates LRU at near-FIFO implementation cost. Linux uses a variant with active/inactive two-list LRU."
---

# Clock Algorithm Approximates LRU Cheaply

The Clock algorithm (second-chance) arranges pages in a circular buffer with a hand pointer. On eviction, the hand inspects the reference bit: pages with the bit set receive a second chance (bit cleared, hand advances), while pages with the bit clear are evicted. This approximates LRU behavior at near-FIFO implementation cost. The NRU variant extends this by also considering the dirty (modified) bit, classifying pages into four priority classes. Linux uses a two-list LRU variant with active and inactive lists, where pages are promoted to the active list on second access, approximating LRU-2 behavior.
