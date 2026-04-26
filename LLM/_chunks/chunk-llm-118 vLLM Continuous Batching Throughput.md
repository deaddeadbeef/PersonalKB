---
tags: [chunk, llm]
id: "chunk-llm-118"
source: "[[LLM/_raw/raw-llm-030 vLLM PagedAttention Serving]]"
source_loc: "Why It Matters, Key Takeaways 4"
topic: "vLLM continuous batching throughput"
claim: "vLLM's continuous batching with PagedAttention achieves 2-4× higher throughput than static batching approaches (HuggingFace TGI at the time)."
confidence: "verified"
supports: ["[[LLM/Inference and Serving/Batching and Continuous Batching]]"]
up: "[[LLM/LLM]]"
---

# vLLM Continuous Batching Achieves 2-4× Throughput Gain

## Context
Traditional LLM serving uses static batching: a batch of requests is formed, all sequences are padded to the same length, and the batch processes together until all sequences complete. This wastes compute on padding tokens and forces the entire batch to wait for the slowest request. vLLM combines PagedAttention with continuous (or iteration-level) batching, where new requests can join the batch at every decoding step and completed requests leave immediately.

The combination of efficient memory management (PagedAttention eliminates waste, allowing more requests in flight) and continuous batching (no idle GPU cycles waiting for slow requests) produced 2-4× higher throughput than HuggingFace Text Generation Inference and up to 24× higher throughput than naive implementations. These gains come without any quality degradation — the outputs are bit-identical to non-optimized serving.

## Why It Matters
A 2-4× throughput improvement translates directly to 2-4× lower serving cost per token at production scale. For companies serving millions of LLM requests per day, this represents enormous cost savings. vLLM's throughput advantage made it the default choice for cost-conscious LLM deployments and set the performance bar that all subsequent serving systems must meet.

## QnA Seeds
- Q: How does continuous batching differ from static batching in LLM serving?
  A: Static batching pads all sequences to equal length and waits for the slowest request; continuous batching adds new requests and removes completed ones at every decoding step, eliminating idle GPU cycles.
- Q: What throughput improvement does vLLM achieve and why?
  A: 2-4× over HuggingFace TGI (up to 24× over naive), by combining PagedAttention (near-zero memory waste enabling more concurrent requests) with continuous batching (no idle compute from padding or waiting).
