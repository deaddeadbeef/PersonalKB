---
tags: [cs-os, chunk]
source: "[[raw-os-006]]"
confidence: high
supports:
  - "[[Deadlock Theory]]"
qna_seeds:
  - "Q: How does the Banker's algorithm avoid deadlock and why is it impractical? A: It maintains matrices of maximum claims, current allocations, and available resources. Before granting a request, it simulates whether a safe sequence exists (all processes can complete). Its O(m×n²) complexity and requirement for advance maximum resource declarations make it impractical for general-purpose OSes."
---

# Bankers Algorithm Safe State Check

Dijkstra's Banker's algorithm (1965) provides deadlock avoidance by simulating resource allocation before granting each request. It maintains matrices of maximum claims, current allocations, and available resources. A state is safe if there exists a sequence in which every process can acquire its maximum resources and complete; requests that would transition to an unsafe state are denied. Despite its theoretical elegance, the algorithm's O(m×n²) time complexity and requirement that processes declare maximum resource needs in advance make it impractical for general-purpose operating systems.
