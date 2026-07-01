---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
confidence: plausible
freshness: stable
tier-coverage:
  - overview
  - core
  - tradeoffs
  - navigation
---

# Hash-Based Structures Overview

Hashing converts keys into array indices, delivering expected $O(1)$ insert, delete, and lookup — performance no comparison-based structure can match. Yet that speed rests on careful choices of hash function, collision strategy, and load-factor management. This hub explores the spectrum from everyday hash tables through theoretical guarantees of universal and perfect hashing to probabilistic and distributed variants used at scale.

## Hash Tables and Collision Handling

A **hash table** pairs a hash function with an array of buckets. When two keys map to the same bucket — a collision — the structure must resolve it. **Chaining** stores colliders in a linked list (or a balanced tree at high load), while **open addressing** probes alternative slots using linear, quadratic, or double-hashing sequences. Each strategy offers distinct trade-offs in cache behaviour, clustering tendency, and deletion complexity. **Cuckoo hashing** takes a different path entirely: it maintains two (or more) tables, evicting existing keys on collision, and guarantees worst-case $O(1)$ lookup at the cost of occasional rehashing cascades.

## Theoretical Foundations

**Universal hashing** selects a function at random from a carefully designed family, bounding the expected collision rate regardless of input distribution — essential for adversary-resistant applications. **Perfect hashing** goes further, constructing a collision-free function for a known key set, achieving true $O(1)$ worst-case access for static dictionaries.

## Probabilistic and Distributed Hashing

Not every query needs an exact answer. **Bloom filters** use multiple hash functions and a bit array to test set membership with tuneable false-positive rates and zero false negatives, saving enormous space in network routers and database engines. **Consistent hashing** distributes keys across a dynamic set of servers so that adding or removing a node reassigns only a small fraction of keys — a cornerstone of distributed caches and storage rings.

## Streaming and Cardinality Estimation

At truly massive scale, even storing all keys becomes impractical. The **Count-Min Sketch** estimates element frequencies in a data stream using sub-linear space, accepting bounded over-counts in exchange for dramatic memory savings. **HyperLogLog** estimates the number of distinct elements (cardinality) in a stream using only a few kilobytes — enabling real-time analytics on billions of events.

## Coverage Map

| Category | Child Page | Source Support |
|----------|-----------|---------------|
| Hash tables and collisions | [[Hash Tables and Hash Functions]], [[Collision Resolution Strategies]] | [[raw-ds-007]] |
| Universal and perfect hashing | [[Universal and Perfect Hashing]] | [[CS Data Structures/_chunks/chunk-ds-066 Universal hashing eliminates adversarial worst-case|chunk-ds-066]], [[CS Data Structures/_chunks/chunk-ds-124 Perfect hashing gives O1 worst-case for static sets|chunk-ds-124]] |
| Probabilistic membership | [[Bloom Filters and Probabilistic Structures]] | [[raw-ds-009]] |
| Alternative exact schemes | [[Cuckoo Hashing]] | [[raw-ds-036]] |
| Distributed hashing | [[Consistent Hashing]] | [[raw-ds-018]] |
| Streaming sketches | [[Count-Min Sketch]], [[HyperLogLog]] | [[CS Data Structures/_chunks/chunk-ds-069 Count-Min Sketch estimates frequency in sublinear space|chunk-ds-069]], [[CS Data Structures/_chunks/chunk-ds-070 HyperLogLog counts distinct elements in 1.5KB|chunk-ds-070]] |

## Pages in This Hub

- [[Hash Tables and Hash Functions]]
- [[Collision Resolution Strategies]]
- [[Universal and Perfect Hashing]]
- [[Cuckoo Hashing]]
- [[Bloom Filters and Probabilistic Structures]]
- [[Consistent Hashing]]
- [[Count-Min Sketch]]
- [[HyperLogLog]]

## Source Coverage

Partly verified source backing for this hub:

- **Hash tables and collision handling** -- [[raw-ds-007]] covers chaining, open addressing, load-factor analysis.
- **Universal and perfect hashing** -- the child note is backed by [[CS Data Structures/_chunks/chunk-ds-066 Universal hashing eliminates adversarial worst-case|chunk-ds-066]] and [[CS Data Structures/_chunks/chunk-ds-124 Perfect hashing gives O1 worst-case for static sets|chunk-ds-124]].
- **Bloom filters / probabilistic membership** -- [[raw-ds-009]] covers false-positive tuning, bit-array sizing.
- **Consistent hashing** -- [[raw-ds-018]] covers ring placement, virtual nodes.
- **Cuckoo hashing** -- [[raw-ds-036]] covers multi-table eviction, worst-case lookup guarantees.
- **Count-Min Sketch / HyperLogLog** -- existing chunks cover the high-level sketch claims, but the child notes still need an explicit supporting-chunks pass.

## References

- [[CS Data Structures/Sources/Sources Index|Sources Index]] — CS Data Structures source map for hash-table and probabilistic-structure raw notes.
- [[raw-ds-007]] — hash-table operations, load factor, chaining, open addressing, and resizing.
- [[raw-ds-009]] — Bloom filters and related probabilistic membership structures.
- [[raw-ds-018]] — consistent hashing for distributed key placement.
- [[raw-ds-028]] — linear probing, open addressing, probe counts, and cache behavior.
- [[raw-ds-036]] — cuckoo hashing lookup guarantees and insertion trade-offs.

## Related Hubs

- [[Foundational Concepts Overview]] — expected-case vs worst-case complexity and memory trade-offs
- [[Linear Structures Overview]] — arrays as the backbone of hash-table storage
- [[Tries and String Structures Overview]] — alternative $O(L)$ key lookup for string-heavy workloads
