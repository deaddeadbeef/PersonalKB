---
tags: [chunk, llm]
id: "chunk-llm-177"
source: "[[LLM/_raw/raw-llm-045 PyTorch FSDP]]"
source_loc: "What Is This, Chunk Candidates"
topic: "FSDP sharding strategy"
claim: "PyTorch FSDP shards model parameters, gradients, and optimizer states across all GPUs, equivalent to ZeRO Stage 3, so each GPU holds only a fraction of the total memory footprint."
confidence: "verified"
supports:
  - "[[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era]]"
qna_seeds:
  - "Q: What does FSDP shard across GPUs? A: Parameters, gradients, and optimizer states — all three are partitioned across ranks so each GPU stores only 1/N of each, enabling models much larger than single-GPU memory."
  - "Q: How does FSDP relate to ZeRO? A: FSDP is PyTorch's native implementation equivalent to DeepSpeed ZeRO Stage 3, which shards all three components. ZeRO Stages 1 and 2 shard only optimizer states or optimizer states plus gradients."
up: "[[LLM/LLM]]"
---

# FSDP Shards Parameters Gradients and Optimizer States

Fully Sharded Data Parallel (FSDP) extends data parallelism by sharding not just gradients but also model parameters and optimizer states across all participating GPUs. In standard data parallelism, each GPU holds a full copy of the model; FSDP partitions each layer's parameters so each GPU stores only its shard (1/N of total). This is equivalent to DeepSpeed's ZeRO Stage 3 optimization. The result is a dramatic reduction in per-GPU memory, enabling training of models that would not fit on any single GPU. Parameters are gathered just-in-time before computation and discarded after.
