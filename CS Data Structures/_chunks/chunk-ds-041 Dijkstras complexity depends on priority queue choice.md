---
tags: [cs-ds, chunk]
id: chunk-ds-041
source: "[[raw-ds-031]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Dijkstras complexity depends entirely on the priority queue choice

## Context
Dijkstra's algorithm extracts minimum-distance vertex repeatedly.

## Claim
With binary heap: O((V+E) log V). With Fibonacci heap: O(V log V + E). With unsorted array: O(V^2). The priority queue is the sole variable determining Dijkstra's runtime.

## Why It Matters
Demonstrates how data structure choice is often more impactful than algorithm choice.

## QnA Seeds
- Q: Best PQ for sparse graphs? -> A: Binary heap — O((V+E) log V) where E is close to V.
- Q: Best PQ for dense graphs? -> A: Unsorted array — O(V^2) matches O(V^2) edges with no PQ overhead.
