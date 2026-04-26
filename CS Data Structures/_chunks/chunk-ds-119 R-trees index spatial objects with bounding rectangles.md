---
tags: [cs-ds, chunk]
id: chunk-ds-119
source: "[[raw-ds-035]]"
supports: ["[[k-d Trees and Spatial Data]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# R-trees index spatial objects with minimum bounding rectangles

## Context
K-d trees and range trees index points not objects with extent.

## Claim
R-trees group nearby spatial objects into minimum bounding rectangles forming a balanced tree. Queries check overlap with bounding rectangles pruning non-overlapping subtrees.

## Why It Matters
Standard spatial index in PostGIS, Oracle Spatial, and SQLite RTree. Handles polygons not just points.

## QnA Seeds
- Q: What is stored at each node? -> A: Minimum bounding rectangle enclosing all objects in the subtree.
- Q: How does insertion work? -> A: Choose subtree requiring least MBR enlargement then split if overflow.
