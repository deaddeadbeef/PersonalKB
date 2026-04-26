---
id: chunk-csa-043
type: chunk
source: "[[Erickson 2019 - Algorithms]]"
source_loc: "Chapter 8 — Shortest Paths"
topic: "graphs"
claim: "Dijkstra's algorithm is correct because it maintains a cut invariant: every vertex extracted from the priority queue has a finalised shortest-path distance, provided all edge weights are non-negative"
confidence: verified
supports:
  - "[[Dijkstra's Algorithm]]"
  - "[[Shortest Path Overview]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — Dijkstra's algorithm maintains a cut invariant that guarantees correctness on non-negative graphs

## Context

Erickson formalises Dijkstra's correctness using a **cut invariant**: at every step of the algorithm, the set S of already-extracted (finalised) vertices and the remaining queue form a cut of the graph. The invariant states that for every vertex u already in S, d[u] equals the true shortest-path distance from the source s to u.

**Proof structure (induction on |S|)**:
- **Base case**: when S = {s}, d[s] = 0 = true distance. ✓
- **Inductive step**: when the algorithm extracts vertex v (minimum d[v] in queue), suppose d[v] > true distance δ(s,v). Then some path P achieves a shorter distance. Let (x, y) be the first edge of P crossing the cut from S to V\S. Since x ∈ S, d[x] = δ(s,x) by induction. Since all weights are non-negative, δ(s,y) ≤ d[x] + w(x,y) ≤ δ(s,v) < d[v]. But v was chosen as the minimum in the queue, so d[v] ≤ d[y] ≤ δ(s,y) ≤ δ(s,v) — contradiction. So d[v] = δ(s,v) when v is extracted. ✓

**Why non-negative weights are essential**: A negative edge from a vertex outside S to a vertex already in S could invalidate a finalised distance — there might be a shorter path through an unprocessed vertex. The cut invariant breaks.

## Why It Matters

The cut invariant proof reveals *why* the greedy choice works: the minimum-distance frontier vertex must already have its true distance, because any alternative path through unprocessed vertices cannot be shorter (non-negative weights mean more hops = more cost). This structure is shared with Prim's minimum spanning tree algorithm, making the cut invariant a broadly reusable proof technique in greedy algorithm analysis.

## QnA Seeds

- Q: State the cut invariant for Dijkstra's algorithm.
- Q: What assumption about edge weights makes the cut invariant proof work, and why does it fail without it?
- Q: How does the cut invariant proof resemble the proof of Prim's MST algorithm?
- Q: Why does extracting the minimum-distance vertex from the queue preserve the cut invariant?
