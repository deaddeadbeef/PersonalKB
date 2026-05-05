---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
confidence: verified
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
| Linear Probing | $O(1/(1-\alpha))$ average | $O(m)$ | Tombstones | Good |
| Cuckoo | $O(1)$ worst | $O(2n)$ | Easy | Good |
| Robin Hood | $O(1)$ expected | $O(m)$ | Complex | Good |

## Orientation

- Start with the workload question: do you need exact membership, approximate membership, or stable key distribution across machines?
- Translate load factor into intuition: as $\alpha$ rises, probes and collisions become more expensive, especially for open addressing.
- Use the table as a trade-off map, not a proof sheet; deletion behavior and cache locality often decide the practical choice.

## Common Traps

- Forgetting that "expected $O(1)$" depends on hash quality and resize policy.
- Treating Bloom filters like exact sets; they allow false positives, not false negatives.
- Ignoring clustering in linear probing when the table gets too full.

## Practice Loop

1. Explain when you would choose chaining over open addressing.
2. State what tombstones are and why they matter for deletion.
3. Give one sentence each for [[Cuckoo Hashing]] and [[Consistent Hashing]].

## References

- [[Hash-Based Structures Overview]]
- [[Hash Tables and Hash Functions]]
- [[Collision Resolution Strategies]]
- [[Cuckoo Hashing]]
- [[Bloom Filters and Probabilistic Structures]]
- [[Consistent Hashing]]
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
- [[raw-ds-007]] — load factor, collision handling, expected hash-table operations, Robin Hood hashing, and tombstone deletion.
- [[raw-ds-028]] — open addressing, linear probing probe bounds, cache behavior, and deletion strategies.
- [[raw-ds-036]] — cuckoo hashing worst-case lookup and insertion behavior.
