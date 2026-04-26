---
tags: [chunk, llm]
id: "chunk-llm-178"
source: "[[LLM/_raw/raw-llm-045 PyTorch FSDP]]"
source_loc: "Chunk Candidates"
topic: "FSDP communication primitives"
claim: "FSDP uses all-gather to reconstruct full parameters before each forward/backward layer computation and reduce-scatter to distribute gradient shards, overlapping communication with computation."
confidence: "verified"
supports:
  - "[[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era]]"
qna_seeds:
  - "Q: What communication operations does FSDP use? A: All-gather before each layer's forward and backward pass (to reconstruct full parameters), and reduce-scatter after backward (to average and shard gradients)."
  - "Q: How does FSDP overlap communication with computation? A: It prefetches the next layer's parameters via all-gather while the current layer is computing, hiding communication latency behind useful compute."
up: "[[LLM/LLM]]"
---

# FSDP Uses All-Gather and Reduce-Scatter Communication

FSDP's communication pattern is built on two NCCL collective operations. Before computing a layer's forward or backward pass, an all-gather operation reconstructs the full parameters from shards across all GPUs. After the backward pass computes gradients, a reduce-scatter operation averages and re-shards the gradients so each GPU stores only its gradient shard. FSDP overlaps these communications with computation by prefetching the next layer's parameters while the current layer executes, minimizing idle time. The full parameters are discarded immediately after use to maintain the memory savings of sharding.
