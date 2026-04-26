---
tags: [cs-ds, chunk]
id: chunk-ds-020
source: "[[raw-ds-018]]"
supports: ["[[Consistent Hashing]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Consistent hashing remaps only K over N keys when nodes change

## Context
Modular hashing remaps nearly all keys when N changes.

## Claim
Consistent hashing maps keys and nodes to a hash ring, so adding or removing a node affects only O(K/N) keys -- vs modular hashing where N=10 to N=11 remaps 91 percent.

## Why It Matters
Enabled elastic scaling in distributed systems like Dynamo, Cassandra, and CDNs.

## QnA Seeds
- Q: Why does modular hashing cause massive redistribution? -> A: key mod N produces different indices for most keys when N changes.
- Q: What are virtual nodes? -> A: Multiple ring positions per physical node for load balance.
