---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
---

# DS Review — Hash Tables

## Quick-Fire Questions

1. What is load factor and why does it matter?
2. Compare chaining vs open addressing: pros and cons of each.
3. What is Robin Hood hashing?
4. How does a Bloom filter work? Can it have false negatives?
5. What problem does consistent hashing solve?
6. What is cuckoo hashing's worst-case lookup time?

## Compare and Contrast

| Method | Lookup | Space | Deletion | Cache |
|--------|--------|-------|----------|-------|
| Chaining | $O(1+alpha)$ | $O(n + m)$ | Easy | Poor |
| Linear Probing | $O(1/(1-alpha)$) | $O(m)$ | Tombstones | Good |
| Cuckoo | $O(1)$ worst | $O(2n)$ | Easy | Good |
| Robin Hood | $O(1)$ expected | $O(m)$ | Complex | Good |
