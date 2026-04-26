---
tags: [chunk, llm]
id: "chunk-llm-180"
source: "[[LLM/_raw/raw-llm-045 PyTorch FSDP]]"
source_loc: "Chunk Candidates"
topic: "FSDP memory-communication trade-off"
claim: "FSDP offers configurable sharding strategies that trade memory savings against communication overhead, and integrates with mixed-precision training to further reduce memory and bandwidth."
confidence: "verified"
supports:
  - "[[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era]]"
qna_seeds:
  - "Q: What sharding strategies does FSDP support? A: Full shard (ZeRO-3, maximum memory savings), shard grad+optimizer only (ZeRO-2, less communication), and no shard (standard DDP, no memory savings)."
  - "Q: How does mixed precision interact with FSDP? A: FSDP can store parameters in fp16/bf16 and gather them in reduced precision, halving communication volume and memory while maintaining training stability with loss scaling."
up: "[[LLM/LLM]]"
---

# FSDP Memory vs Communication Trade-offs

FSDP provides configurable sharding policies that let practitioners balance memory savings against communication cost. Full sharding (ZeRO-3) maximizes memory reduction but requires all-gather/reduce-scatter for every layer. Gradient-only sharding (ZeRO-2) reduces communication by keeping parameters unsharded but still distributes gradients and optimizer states. FSDP integrates natively with PyTorch's mixed-precision training (AMP), allowing parameters to be communicated and stored in fp16 or bf16, which halves communication bandwidth and memory. This combination of configurable sharding and mixed precision allows teams to find the optimal operating point for their hardware and model size.
