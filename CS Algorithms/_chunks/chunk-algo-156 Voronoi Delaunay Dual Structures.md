---
id: chunk-csa-156
type: chunk
source: "[[de Berg 2008 - Computational Geometry]]"
source_loc: "Voronoi and Delaunay"
topic: "geometry"
claim: "Voronoi diagrams partition the plane into closest-site regions with at most 2n-5 vertices and 3n-6 edges, and their dual Delaunay triangulation maximizes minimum angles"
confidence: verified
supports:
  - "[[Voronoi Diagram]]"
  - "[[Delaunay Triangulation]]"
tags:
  - csa
  - csa/geometry
  - chunk
up: "[[CS Algorithms]]"
---
# Geometry — Voronoi diagrams and Delaunay triangulations are dual O(n log n) structures

## Context

A Voronoi diagram of n points partitions the plane into regions where each region contains all points closer to its site than to any other. It has at most 2n-5 vertices and 3n-6 edges, computable in O(n log n) via Fortune's sweep-line algorithm. The dual Delaunay triangulation connects sites whose Voronoi regions share an edge, with the property that no point lies inside the circumcircle of any triangle—this maximizes the minimum angle across all possible triangulations, making it ideal for mesh generation and interpolation.

## Why It Matters

Voronoi diagrams and Delaunay triangulations are fundamental in spatial indexing, mesh generation for finite element analysis, and facility location, encoding proximity relationships that underlie many geometric algorithms.

## QnA Seeds

- Q: What is the duality relationship between Voronoi diagrams and Delaunay triangulations?
- Q: What is the empty circumcircle property of Delaunay triangulations?
- Q: What are the size bounds on a Voronoi diagram of n points?
