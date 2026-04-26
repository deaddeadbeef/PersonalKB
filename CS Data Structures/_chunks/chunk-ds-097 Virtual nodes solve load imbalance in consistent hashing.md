---
tags: [cs-ds, chunk]
id: chunk-ds-097
source: "[[raw-ds-018]]"
supports: ["[[Consistent Hashing]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Virtual nodes solve load imbalance in consistent hashing

## Context
With few physical nodes hash ring positions may be unevenly distributed.

## Claim
Assigning 100-200 virtual nodes per physical node spreads load uniformly across the ring. Each virtual node maps to its physical host. Load variance drops from O(1/N) to O(1/VN).

## Why It Matters
Without virtual nodes one node could get 2-3x expected load. Virtual nodes make consistent hashing practical.

## QnA Seeds
- Q: How many virtual nodes per physical? -> A: Typically 100-200 for good balance.
- Q: How does rebalancing work? -> A: Moving a physical node moves all its virtual nodes transferring proportional load.
