---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Computational Geometry: Convex Hulls, Intersections, and Proximity"
authors: [Mark de Berg, Otfried Cheong, Marc van Kreveld, Mark Overmars]
year: 2008
---

## Summary

Computational geometry studies algorithms for problems defined in geometric spaces. The convex hull—the smallest convex polygon enclosing a set of points—is the foundational problem. Graham scan computes the 2D convex hull in O(n log n) by sorting points by polar angle relative to a bottom-most point, then processing them in order while maintaining the convex hull invariant using a stack. Points causing left turns are pushed; right turns trigger pops. Jarvis march (gift wrapping) runs in O(nh) where h is the number of hull vertices, making it output-sensitive—faster than Graham scan when h is small. The line segment intersection problem asks whether any pair among n segments intersects. The sweep-line algorithm (Bentley-Ottmann) solves this in O((n + k) log n) time where k is the number of intersections, using an event queue and a status structure to track active segments as a vertical line sweeps left to right. The closest pair problem finds the two nearest points among n points. A divide-and-conquer approach achieves O(n log n): split points by x-coordinate, recurse on halves, and combine by examining only points within distance δ of the dividing line, where δ is the smaller of the two recursive results. The key insight is that at most O(1) points per side need examination in the strip. Voronoi diagrams partition the plane into regions closest to each of n sites, computed in O(n log n) via Fortune's sweep-line algorithm. The dual Delaunay triangulation maximizes minimum angles and is used in mesh generation, terrain modeling, and interpolation.

## Key Claims

1. Graham scan computes the 2D convex hull in O(n log n) time—optimal since computing the hull reduces to sorting—using a stack-based approach after polar-angle sorting.
2. Jarvis march achieves O(nh) time where h is the hull size, making it superior when h = o(log n) but inferior for large hulls compared to Graham scan's O(n log n).
3. The Bentley-Ottmann sweep-line algorithm finds all k intersections among n segments in O((n + k) log n) time, improving over the O(n²) brute-force approach.
4. Closest pair in O(n log n) via divide and conquer relies on the geometric insight that the strip near the dividing line contains at most O(n) candidate pairs with O(1) per-point comparisons.
5. Voronoi diagrams and Delaunay triangulations are dual structures encoding proximity and triangulation information, both computable in O(n log n).

## Atomic Facts

1. Graham scan processes points in polar-angle order: three consecutive points making a right (clockwise) turn indicate the middle point is not on the convex hull and should be removed.
2. The lower bound Ω(n log n) for convex hull follows from a reduction from sorting: given n numbers, create points (xᵢ, xᵢ²) whose convex hull reveals the sorted order.
3. In the closest-pair algorithm, the strip of width 2δ around the dividing line is partitioned into δ×δ boxes, each containing at most one point, limiting per-point comparisons to at most 7.
4. The sweep-line paradigm reduces 2D problems to 1D by processing events (endpoints, intersections) left to right while maintaining a dynamic data structure of active objects.
5. A Voronoi diagram of n points in the plane has at most 2n−5 vertices and 3n−6 edges, and each face is a convex polygon (possibly unbounded).
6. The Delaunay triangulation has the property that no point lies inside the circumcircle of any triangle, maximizing the minimum angle across all triangulations.

## Significance

Computational geometry algorithms are essential in computer graphics, geographic information systems, robotics, and scientific computing. Convex hulls are used in collision detection and shape analysis; line segment intersection algorithms power map overlay in GIS; closest pair algorithms appear in clustering and molecular simulation; Voronoi diagrams are fundamental in spatial indexing, mesh generation for finite element analysis, and facility location optimization. The sweep-line paradigm introduced in computational geometry has influenced algorithm design across many domains, demonstrating the power of reducing dimensional complexity through systematic processing.

## Chunks Extracted

chunk-algo-153 through chunk-algo-156
