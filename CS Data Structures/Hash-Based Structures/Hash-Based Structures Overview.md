---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
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

## Pages in This Hub

- [[Hash Tables and Hash Functions]]
- [[Collision Resolution Strategies]]
- [[Universal and Perfect Hashing]]
- [[Cuckoo Hashing]]
- [[Bloom Filters and Probabilistic Structures]]
- [[Consistent Hashing]]
- [[Count-Min Sketch]]
- [[HyperLogLog]]

## Related Hubs

- [[Foundational Concepts Overview]] — expected-case vs worst-case complexity and memory trade-offs
- [[Linear Structures Overview]] — arrays as the backbone of hash-table storage
- [[Tries and String Structures Overview]] — alternative $O(L)$ key lookup for string-heavy workloads