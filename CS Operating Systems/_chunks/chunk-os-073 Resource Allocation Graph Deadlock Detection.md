---
tags: [cs-os, chunk]
source: "[[raw-os-006]]"
confidence: high
supports:
  - "[[Deadlock Theory]]"
qna_seeds:
  - "Q: How does a resource allocation graph detect deadlock? A: The graph contains process nodes, resource nodes, request edges (process→resource), and assignment edges (resource→process). A cycle is necessary for deadlock and sufficient when all resource types have single instances. Recovery options include terminating deadlocked processes or rolling back to checkpoints."
---

# Resource Allocation Graph Deadlock Detection

A resource allocation graph models deadlock by containing process nodes, resource nodes, request edges (process→resource), and assignment edges (resource→process). A cycle in this graph is a necessary condition for deadlock, and sufficient when all resource types have single instances. Detection finds deadlocks after they occur; recovery options include terminating all deadlocked processes (crude but effective), terminating one at a time until the cycle breaks (requires choosing an optimal victim), or rolling back processes to saved checkpoints. Each recovery strategy imposes costs on affected processes.
