---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-008]]"
confidence: high
supports:
  - "[[Binary Search]]"
  - "[[Parametric Search]]"
qna_seeds:
  - "Q: What is binary search on the answer? A: A technique that transforms optimization problems into decision problems by binary searching over the answer space, applicable whenever the feasibility function is monotonic."
---

# Binary Search on the Answer Technique

Binary search on the answer (parametric search) transforms optimization problems into decision problems by binary searching over the answer space. This is applicable whenever the feasibility function is monotonic—if a value x is feasible, then all values less restrictive than x are also feasible. Exponential search (galloping) complements this by first finding the range in O(log k) where k is the target position, then applying binary search for O(log k) total.