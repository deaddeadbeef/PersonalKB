---
id: chunk-algo-123
type: chunk
source: "[[raw-algo-021]]"
source_loc: "Floyd-Warshall - Atomic Facts"
topic: "graphs"
claim: "Floyd-Warshall requires k (intermediate vertex) as the outermost loop; swapping loop order produces incorrect results because D^(k)[i][j] depends on the complete k-1 layer, while all (i,j) pairs for fixed k are independent and parallelizable."
confidence: verified
supports:
  - "[[Floyd-Warshall Algorithm]]"
tags:
  - cs-algorithms
  - cs-algorithms/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Floyd-Warshall Loop Order k-i-j Is Critical for Correctness

## Context

D^(k)[i][j] depends on D^(k-1)[i][j], D^(k-1)[i][k], and D^(k-1)[k][j]. With k outermost, in-place updates are safe because row k and column k are invariant between layers. If i or j were outermost, entries might be overwritten before they are needed. For fixed k, all V^2 (i,j) pairs are independent, enabling GPU acceleration and SIMD parallelization. Path reconstruction requires a predecessor matrix Pi[i][j] updated alongside distances.

## Why It Matters

Understanding loop order is essential for correct Floyd-Warshall implementation. The independence of (i,j) pairs for fixed k enables straightforward parallelization on modern hardware.

## QnA Seeds

- Q: Why must k be the outermost loop in Floyd-Warshall?
- Q: Why are in-place updates safe in Floyd-Warshall?
- Q: How is Floyd-Warshall parallelized?