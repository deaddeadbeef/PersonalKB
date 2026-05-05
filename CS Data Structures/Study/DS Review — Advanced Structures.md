---
tags: [cs-ds, study, drill]
up: "[[CS Data Structures Study Index]]"
confidence: verified
---

# DS Review — Advanced Structures

## Quick-Fire Questions

1. How do skip lists achieve $O(\log n)$ without rotations?
2. What is path compression in Union-Find? Why is it important?
3. When would you use a segment tree vs a Fenwick tree?
4. How does a Fenwick tree use the lowest set bit?
5. What is a k-d tree and when does it degrade?

## Study Answers

1. [[Skip Lists]] use probabilistic express lanes, so search descends through multiple linked levels and stays at expected $O(\log n)$ without tree rotations.
2. In [[Disjoint Sets and Union-Find]], path compression rewires nodes visited during `Find` so they point closer to the root; with union by rank, this gives amortized $O(\alpha(n))$ operations.
3. Use [[Segment Trees]] when you need more general range queries or lazy range updates; use [[Fenwick Trees]] when prefix sums and point updates are enough and you want a smaller, simpler structure.
4. [[Fenwick Trees]] jump between responsible ranges with the lowest set bit: `i & -i` isolates that bit to move to the next aggregate bucket.
5. [[k-d Trees and Spatial Data Structures]] partition low-dimensional space with recursive splits; they degrade under skew, many dynamic inserts, or high-dimensional data where pruning becomes weak.

## Compare and Contrast

| Structure | Build | Query | Update | Space | Best For |
|-----------|-------|-------|--------|-------|----------|
| [[Segment Trees]] | $O(n)$ | $O(\log n)$ range query | $O(\log n)$ point update; $O(\log n)$ lazy range update | $O(n)$, often stored as about $4n$ | General associative range queries and updates |
| [[Fenwick Trees]] | $O(n)$ | $O(\log n)$ prefix/range sum | $O(\log n)$ point update | $O(n)$ | Prefix sums with simple bit-based indexing |
| [[Skip Lists]] | $O(n \log n)$ by repeated insert | expected $O(\log n)$ | expected $O(\log n)$ insert/delete | expected $O(n)$ | Ordered sets/maps with simple local pointer changes |
| [[Disjoint Sets and Union-Find]] | $O(n)$ MakeSet setup | amortized $O(\alpha(n))$ Find | amortized $O(\alpha(n))$ Union | $O(n)$ | Dynamic connectivity and component tracking |
| [[k-d Trees and Spatial Data Structures]] | $O(n \log n)$ | average $O(\log n)$ nearest-neighbor, worst $O(n)$ | dynamic inserts can degrade structure | $O(n)$ | Low-dimensional spatial search |

## Selection Cues

- Reach for [[Skip Lists]] when you want ordered search with expected logarithmic behavior and no rotation logic.
- Reach for [[Disjoint Sets and Union-Find]] when the problem is connectivity under merges rather than arbitrary updates or deletions.
- Reach for [[Segment Trees]] over [[Fenwick Trees]] when the operation is more general than prefix sums or when lazy propagation matters.
- Treat [[k-d Trees and Spatial Data Structures]] as strongest in low dimensions; performance weakens as dimensionality rises.

## References

- [[Skip Lists]]
- [[Disjoint Sets and Union-Find]]
- [[Segment Trees]]
- [[Fenwick Trees]]
- [[k-d Trees and Spatial Data Structures]]
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
