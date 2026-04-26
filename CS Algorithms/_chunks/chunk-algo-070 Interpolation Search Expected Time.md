---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-008]]"
confidence: high
supports:
  - "[[Binary Search]]"
  - "[[Interpolation Search]]"
qna_seeds:
  - "Q: When does interpolation search outperform binary search? A: On uniformly distributed data it achieves O(log log n) expected comparisons—for n = 10⁹, roughly 5 vs 30 for binary search—but degrades to O(n) on adversarial inputs."
---

# Interpolation Search Expected Time

Interpolation search achieves O(log log n) expected time on uniformly distributed data by estimating the target's position proportionally rather than always bisecting. For n = 10⁹, this is roughly 5 comparisons compared to 30 for binary search. However, it degrades to O(n) on adversarial inputs. The O(log log n) average bound was proved by Perl, Itai, and Avni (1978).