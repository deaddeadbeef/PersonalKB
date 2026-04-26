---
tags: [chunk, llm]
id: "chunk-llm-067"
source: "[[LLM/_raw/raw-llm-017 Mamba Selective State Spaces]]"
source_loc: "Key Takeaways 3"
topic: "Mamba KV-cache-free inference"
claim: "Mamba uses no KV cache — its fixed-size state means constant memory per token regardless of sequence length."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/State Space Models and Mamba]]"]
up: "[[LLM/LLM]]"
---

# Mamba No KV Cache Constant Memory

## Context
Transformer inference requires storing key-value pairs for every previous token in every layer — the KV cache. For a model with L layers, d dimensions, and context length n, the KV cache grows as O(L × n × d), often dominating GPU memory during serving. A 70B parameter model serving a 128K context can require 40+ GB just for KV cache, limiting batch sizes and throughput.

Mamba eliminates this entirely. During autoregressive inference, the SSM maintains a fixed-size hidden state (typically dimension d_state × d_model, e.g., 16 × 4096 ≈ 64K values per layer). This state summarizes all previous tokens and is updated incrementally with each new token. The memory required for this state is constant regardless of sequence length — processing token 1,000 requires exactly the same memory as processing token 100,000. This is a fundamental structural advantage over transformers for long-sequence applications.

## Why It Matters
KV cache memory is the primary bottleneck in transformer serving at long context lengths. Mamba's constant-memory inference means it can process arbitrarily long sequences without the memory scaling that limits transformer context windows. This makes it particularly attractive for applications like long document processing, continuous dialogue, and streaming scenarios where context length is unbounded.

## QnA Seeds
- Q: Why does Mamba not need a KV cache for autoregressive inference?
  A: Mamba's SSM maintains a fixed-size hidden state that summarizes all previous tokens. Each new token updates this state incrementally. Unlike attention, which must reference all previous keys and values explicitly, the SSM compresses history into a fixed-size representation that doesn't grow with sequence length.
- Q: How does Mamba's inference memory compare to a transformer's at different context lengths?
  A: Mamba's memory is constant — the same fixed-size state regardless of sequence length. A transformer's KV cache grows linearly with context length (O(L × n × d)). At 128K tokens, a 70B transformer may need 40+ GB for KV cache alone, while Mamba's state remains a few MB.
