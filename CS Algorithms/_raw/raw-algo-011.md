---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Heaps, Priority Queues, and Heapsort"
authors: "J.W.J. Williams, Robert W. Floyd"
year: 1964
---

# Heap and Priority Queue

## Summary
A binary heap is a complete binary tree stored in an array that satisfies the heap property: each node's key is less than or equal to (min-heap) or greater than or equal to (max-heap) its children's keys. The heap supports insert and extract-min in O(log n) time, and the crucial insight is that building a heap from an unsorted array takes only O(n) time via bottom-up heapify—not O(n log n) as naive analysis suggests. Heapsort leverages this structure to sort in O(n log n) worst-case time using O(1) auxiliary space, while Fibonacci heaps optimize decrease-key to O(1) amortized, enabling faster graph algorithms.

## Key Claims
- Binary heap insert (sift-up) and extract-min (sift-down) each take O(log n) time in the worst case, where the heap has height ⌊log₂ n⌋
- Bottom-up heap construction (Floyd's algorithm) runs in O(n) time by calling sift-down on each non-leaf node from the bottom up; the tight analysis shows the total work is Σ_{h=0}^{⌊log n⌋} ⌈n/2^{h+1}⌉ · O(h) = O(n)
- Heapsort achieves O(n log n) worst-case time and O(1) auxiliary space, making it the only comparison sort that is simultaneously optimal in time and in-place, though it is not stable
- Fibonacci heaps support decrease-key in O(1) amortized time and extract-min in O(log n) amortized time, reducing Dijkstra's algorithm from O((V + E) log V) to O(V log V + E)
- The binary heap is implicit—stored in an array with parent at index ⌊i/2⌋ and children at 2i and 2i+1—requiring zero pointers and achieving excellent cache locality

## Atomic Facts
1. Floyd's heap construction performs at most 2n − 2⌊log₂ n⌋ − 2 comparisons, which for n = 1,000,000 is approximately 1,999,960 comparisons—dramatically fewer than the 19.9 million for n repeated insertions
2. Heapsort makes at most 2n log₂ n + O(n) comparisons; the exact worst case is 2n⌊log₂ n⌋ − 2^{⌊log₂ n⌋+1} + n + 2, which is about 39% more than the theoretical minimum of n log₂ n − 1.44n
3. A d-ary heap (with d children per node) reduces tree height to log_d n, optimizing decrease-key to O(log_d n) at the cost of O(d log_d n) for extract-min; optimal d = E/V for Dijkstra yields O(E log_{E/V} V)
4. Fibonacci heaps use a collection of heap-ordered trees with lazy consolidation; the potential function Φ = t + 2m (t = number of trees, m = number of marked nodes) proves the amortized bounds
5. A binary heap of n = 10⁷ elements fits in approximately 40 MB (4 bytes per integer key), and extract-min touches at most ⌊log₂ 10⁷⌋ = 23 cache lines in the worst case
6. Pairing heaps are a simpler alternative to Fibonacci heaps with O(1) amortized insert, O(log n) amortized extract-min, and conjectured O(1) amortized decrease-key, though the O(log log n) upper bound by Iacono (2000) remains the best proven

## Significance
The binary heap is one of the most space-efficient and cache-friendly data structures, making it the default priority queue implementation in virtually every standard library (C++ std::priority_queue, Python heapq, Java PriorityQueue). Floyd's O(n) heapify algorithm is a beautiful example of how careful amortized analysis reveals non-obvious efficiency. Fibonacci heaps, while rarely implemented in practice due to large constant factors, represent a theoretical breakthrough that improved the asymptotic complexity of Dijkstra's and Prim's algorithms and inspired simpler alternatives like pairing heaps and rank-pairing heaps.

## Chunks Extracted
*Pending*
