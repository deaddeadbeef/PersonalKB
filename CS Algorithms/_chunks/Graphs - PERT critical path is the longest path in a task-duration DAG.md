---
id: chunk-csa-026
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 5"
topic: "graphs"
claim: "The PERT critical path is the longest path from start to finish in a task-duration DAG and determines the minimum project completion time; it is computed in Θ(n+m) by relaxing edge weights in topological order"
confidence: verified
supports:
  - "[[DAG and Topological Sort]]"
tags:
  - csa
  - csa/graphs
  - chunk
up: "[[CS Algorithms]]"
---
# Graphs — PERT critical path is the longest path in a task-duration DAG

## Context

In a PERT (Program Evaluation and Review Technique) chart, vertices represent tasks and edge weights represent task durations (or waiting times between tasks). The critical path is the longest path from the source (project start) to the sink (project end). No task on the critical path can be delayed without extending the total project duration. To compute it: process vertices in topological order; for each vertex u, relax all outgoing edges by updating dist[v] = max(dist[v], dist[u] + w(u,v)). This is a longest-path computation — achieved by negating weights to turn it into a shortest-path problem, or by running a DP directly on the topological order. Time: Θ(n+m).

## Why It Matters

Critical path analysis is a direct application of DAG topological sort to project management and scheduling. It demonstrates that graph algorithms have immediate practical utility beyond theoretical interest. The Θ(n+m) runtime means it scales to large project graphs. Understanding the critical path also introduces the concept of slack — tasks not on the critical path have slack time that can be used without delaying the project, which is key to resource allocation.

## QnA Seeds

- Q: What does it mean for a task to lie on the critical path?
- Q: How is finding the critical path different from a standard shortest-path problem?
- Q: Why must the project graph be a DAG for critical path analysis to be well-defined?
