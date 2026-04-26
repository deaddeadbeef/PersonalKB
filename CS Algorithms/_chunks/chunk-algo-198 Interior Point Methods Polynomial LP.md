---
id: chunk-csa-198
type: chunk
source: "[[Cormen 2022 - Linear Programming]]"
source_loc: "Interior Point Methods"
topic: "optimization"
claim: "Interior point methods achieve polynomial worst-case O(n^3.5 L) for LP by traversing the feasible region's interior using barrier functions and Newton's method"
confidence: verified
supports:
  - "[[Linear Programming]]"
  - "[[Interior Point Method]]"
tags:
  - csa
  - csa/optimization
  - chunk
up: "[[CS Algorithms]]"
---
# Optimization — Interior point methods polynomial O(n^3.5 L) worst case

## Context

Interior point methods (Karmarkar, 1984) traverse the interior of the feasible region rather than its boundary, achieving polynomial worst-case time O(n^3.5 L) where L is the input bit length. They follow a central path through the interior using Newton's method on a barrier function that penalizes approaching constraint boundaries. Modern LP solvers implement both simplex and barrier methods, selecting based on problem structure—interior point methods are often superior for large, sparse problems. The ellipsoid method (Khachiyan, 1979) first proved LP is in P but is impractical.

## Why It Matters

Interior point methods resolved the theoretical question of LP's polynomial solvability and provide the competitive alternative to simplex in modern optimization solvers.

## QnA Seeds

- Q: How do interior point methods differ from simplex geometrically?
- Q: What is the role of the barrier function in interior point methods?
- Q: When are interior point methods preferred over simplex?
