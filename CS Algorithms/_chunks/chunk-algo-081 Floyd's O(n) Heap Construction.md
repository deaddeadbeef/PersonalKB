---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-011]]"
confidence: high
supports:
  - "[[Binary Heaps]]"
  - "[[Heapify]]"
qna_seeds:
  - "Q: Why is bottom-up heap construction O(n) instead of O(n log n)? A: Floyd's algorithm calls sift-down from the bottom up; the sum Σ ⌈n/2^{h+1}⌉ · O(h) telescopes to O(n), performing at most 2n − 2⌊log₂ n⌋ − 2 comparisons."
---

# Floyd's O(n) Heap Construction

Floyd's bottom-up heap construction runs in O(n) time by calling sift-down on each non-leaf node from the bottom up. The tight analysis shows total work is Σ_{h=0}^{⌊log n⌋} ⌈n/2^{h+1}⌉ · O(h) = O(n), with at most 2n − 2⌊log₂ n⌋ − 2 comparisons. For n = 1,000,000 this is approximately 1,999,960 comparisons—dramatically fewer than the ~19.9 million for n successive insertions.