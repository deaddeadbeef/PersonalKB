---
tags: [cs-os, chunk]
source: "[[raw-os-002]]"
confidence: high
supports:
  - "[[Process Management]]"
  - "[[CPU Scheduling]]"
qna_seeds:
  - "Q: What are the direct and indirect costs of a context switch? A: Direct costs (1–10 μs) include saving and restoring CPU registers. Indirect costs — TLB flushes, cache pollution, and pipeline flushes — can multiply the effective cost by 10× or more."
---

# Context Switch Overhead Model

Context switching between processes incurs both direct and indirect costs. Direct costs include saving and restoring the full CPU register set, taking approximately 1–10 microseconds on modern hardware. Indirect costs — TLB flush invalidating cached address translations, cache pollution evicting hot cache lines, and pipeline flush discarding in-flight instructions — can multiply the effective performance penalty by 10× or more, making context switch frequency a critical scheduling parameter.
