---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "k-d Trees and Spatial Indexing"
authors: [Various]
year: 2020
up: "[[Sources Index]]"
---

# k-d Trees and Spatial Data Structures

## Summary

k-d trees partition k-dimensional space by alternating split dimensions. O(n log n) construction. Nearest neighbor O(log n) average, O(n) worst. Range search O(n^(1-1/k) + output). Alternatives include R-trees (disk-optimized), quad-trees (regular subdivision), and ball trees (high dimensions).

## Key Claims

1. k-d trees alternate splitting dimension at each level
2. Nearest neighbor search averages O(log n) but worst case is O(n)
3. Effective in low dimensions but degrade in high dimensions
4. R-trees use bounding rectangles for disk-optimized spatial indexing
5. Ball trees handle high-dimensional data better than k-d trees

## Atomic Facts

1. Construction: O(n log n) using median selection at each level
2. Nearest neighbor: prune branches whose bounding box is farther
3. Range search: O(n^(1-1/k) + output) for orthogonal queries
4. R-trees: used in PostGIS, spatial databases
5. Quad-trees: regular 4-way subdivision, good for 2D
6. Applications: graphics, GIS, machine learning KNN

## Significance

Spatial data structures enable efficient geometric queries that are fundamental to graphics, mapping, robotics, and machine learning applications.

## Chunks Extracted

*Pending*
