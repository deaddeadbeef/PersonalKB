---
tags: [cs-ds, raw]
source_type: technical_analysis
source_title: "Consistent Hashing"
authors: [Various]
year: 2020
up: "[[Sources Index]]"
---

# Consistent Hashing and Distributed Systems

## Summary

Consistent hashing maps keys and nodes to a circular hash ring. Keys assigned to first clockwise node. Adding/removing a node remaps only O(K/N) keys. Virtual nodes smooth load distribution. Foundational to Dynamo, Cassandra, Chord.

## Key Claims

1. Only O(K/N) keys remapped when a node changes
2. Virtual nodes solve load imbalance
3. Foundational to partition-tolerant distributed storage
4. Hash ring enables elastic scaling without full rehash
5. Combined with replication provides fault tolerance

## Atomic Facts

1. Karger et al., 1997: original consistent hashing paper
2. Amazon Dynamo, 2007: consistent hashing for partitioning
3. Apache Cassandra uses virtual nodes (vnodes)
4. Chord: P2P DHT with O(log N) lookup
5. Typical virtual node count: 100-200 per physical node
6. Modular hashing: n=10 to n=11 remaps ~91% of keys

## Significance

Consistent hashing solved the key redistribution problem that made elastic scaling of distributed systems practical.

## Chunks Extracted

*Pending*
