---
id: raw-csa-005
type: raw
title: "Algorithms, 4th Edition — Booksite"
author: "Robert Sedgewick and Kevin Wayne"
year: 2011
publisher: "Addison-Wesley / Princeton booksite"
url: "https://algs4.cs.princeton.edu/home/"
status: processed
chunk_count: 4
tags:
  - csa
  - raw
  - open-access
up: "[[CS Algorithms]]"
---
# Princeton Algorithms 4e — Online Reference

## Bibliographic Reference

Sedgewick, Robert; Wayne, Kevin. *Algorithms*, 4th ed. Addison-Wesley, 2011. Companion booksite freely available at https://algs4.cs.princeton.edu/home/

The booksite includes full chapter summaries, pseudocode, Java implementations, and worked exercises for all major algorithm families.

## Description

Sedgewick and Wayne's *Algorithms* 4th edition is a widely used undergraduate textbook known for its clean pedagogical style and its emphasis on practical analysis. The booksite exposes the full chapter narratives, visual animations, and complexity proofs. Particularly valuable for elementary sorting (insertion sort, selection sort) where the authors articulate the inversion relationship, the low-exchange property of selection sort, and adaptivity arguments with greater clarity than most references.

## Why It Matters

- **Open access**: chapter narratives, figures, and Java code freely available; no registration.
- **Elementary sorting depth**: selection sort's exact swap-count and non-adaptivity, insertion sort's inversion-based analysis, and their practical performance profiles are treated precisely and accessibly.
- **Inversion concept**: the booksite introduces inversions as the canonical measure of "sortedness" and derives insertion sort's running time directly from inversion count — cleaner than many other treatments.
- **Practical framing**: emphasises when to prefer each algorithm (e.g., selection sort when writes are expensive, insertion sort as the hybrid-sort base case).

## Chunk Candidates

| Chunk Topic | Target Wiki Notes |
|---|---|
| Selection sort minimises writes: exactly n−1 swaps regardless of input | [[Selection Sort]], [[Sorting Overview]] |
| Selection sort is non-adaptive: sorted or random input yields the same Θ(n²) comparisons | [[Selection Sort]] |
| Insertion sort performs exactly one shift per inversion | [[Insertion Sort]], [[Inversions]] |
| Insertion sort running time bounded by inversions plus n: near-sorted performance argument | [[Insertion Sort]], [[Inversions]] |

## Related Wiki Notes

- [[Selection Sort]] — primary deepening target
- [[Insertion Sort]] — primary deepening target
- [[Sorting Overview]] — comparison table update
- [[Inversions]] — new page supported by these chunks

## Chunks Created This Wave

- [[Sorting - Selection sort minimizes the number of writes by guaranteeing exactly n-1 swaps regardless of input order]] (chunk-csa-057)
- [[Sorting - Selection sort is non-adaptive and performs identical comparison work on sorted or random inputs]] (chunk-csa-058)
- [[Sorting - Insertion sort performs exactly one element shift per inversion in the input array]] (chunk-csa-059)
- [[Sorting - Insertion sort running time is bounded by the inversion count plus array size giving O(kn) for k-displaced arrays]] (chunk-csa-060)
