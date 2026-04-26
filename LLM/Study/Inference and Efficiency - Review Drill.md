---
tags: [study, llm, drill]
up: "[[LLM/Study/LLM Study Index]]"
---

# Inference & Efficiency — Review Drill

## Quick-Fire Questions

1. **What is the KV cache and why is it needed?**
   During autoregressive generation, keys and values for previous tokens don't change. KV cache stores them to avoid recomputation, reducing generation from $O(n²)$ to $O(n)$ per step.

2. **What is PagedAttention?**
   vLLM's approach: manage KV cache like OS virtual memory pages. Eliminates fragmentation from variable-length sequences. Non-contiguous memory blocks mapped to logical KV slots.

3. **GPTQ vs AWQ — what's the difference?**
   Both are weight-only post-training quantization. GPTQ: optimal brain quantization per layer with calibration data. AWQ: protects activation-aware salient weights during quantization.

4. **How does speculative decoding work?**
   Small draft model proposes multiple tokens. Large target model verifies them all in one parallel forward pass. Mathematically lossless — output distribution matches the target model exactly.

5. **Static batching vs continuous batching?**
   Static: group requests, process together, wait for longest. Continuous (Orca): iteration-level scheduling, new requests join mid-batch as others complete. Much better GPU utilization.

6. **What are TTFT and TPOT?**
   Time To First Token (prefill latency) and Time Per Output Token (decode latency). Key serving metrics with different optimization strategies.

7. **Why is autoregressive decoding memory-bandwidth-bound?**
   Each decode step generates one token but must read all model weights. The compute-to-memory ratio is very low, so GPU cores sit idle waiting for data.

8. **Knowledge distillation: soft targets vs hard labels?**
   Soft targets (teacher's probability distribution) carry more information than hard labels (just the correct answer). The "dark knowledge" in non-top probabilities helps the student learn better.

9. **When should you quantize vs use a smaller model?**
   Quantize when you need the larger model's capabilities but want to reduce memory/cost. Use a smaller model when the task doesn't require large-model quality.

10. **What is prefix caching?**
    Reusing KV cache across requests that share the same prefix (e.g., system prompt). Avoids redundant computation for the common prompt portion.
