---
tags: [cs-ds, chunk]
id: chunk-ds-148
source: "[[raw-ds-020]]"
supports: ["[[k-d Trees and Spatial Data]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Ball trees handle high dimensions better than k-d trees

## Context
K-d trees degrade in dimensions above 20.

## Claim
Ball trees use hyperspheres instead of hyperplanes to partition space. The triangle inequality enables effective pruning even in moderate-to-high dimensions where k-d trees fail.

## Why It Matters
Used in scikit-learn for nearest neighbor in 20-100 dimensions where k-d trees are ineffective.

## QnA Seeds
- Q: Why spheres instead of planes? -> A: Triangle inequality gives tighter distance bounds for pruning in high dimensions.
- Q: When does ball tree also fail? -> A: Very high dimensions (100+). Need approximate methods like LSH.
