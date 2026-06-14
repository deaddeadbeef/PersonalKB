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

11. **Which runtime should you try first for local experimentation?**
    Ollama or LM Studio for fast setup; llama.cpp when you need GGUF/CPU/edge control; vLLM or SGLang after [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|WSL CUDA setup proof]] when you need production-style GPU serving.

12. **What should you measure before trusting a local model setup?**
    Time to first token, decode tokens/sec, peak RAM/VRAM, context length, answer quality on known prompts, and whether the API shape matches your application.

13. **Why must sampling settings be fixed during local model comparisons?**
    Temperature, candidate filters, penalties, seeds, stop strings, and output caps change the next-token distribution and the returned shape. A benchmark compares model/runtime behavior only after these controls are recorded or intentionally varied.

14. **What should be recorded before downloading a local model?**
    Model card, intended use, license, gated-access decision, exact revision/tag/file, artifact format, unsafe file risk, local cache path, and a digest or revision proof when reproducibility matters.

15. **What proves the downloaded artifact is the one being served?**
    Pinned revision/tag/file, cache or local path, file list, hash or verification result, GGUF/Ollama import or conversion command, runtime-visible model id, and cleanup/rollback plan.

16. **What is the practical context-budget formula for a local LLM request?**
    Runtime context limit must cover system/template tokens, user/task tokens, history, retrieved context, tool schemas, reserved output tokens, and a safety margin. If it does not fit, reduce prompt/context before trusting latency, quality, or truncation behavior.

## Hands-On

- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] — run a local model, expose an API, and benchmark inference.
- [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] — trace a single request through prompt assembly, tokenization, prefill, decode, sampling, stopping, and streaming.
- [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] — tune temperature, top-p, top-k, min-p, penalties, seeds, stop rules, and structured-output controls.
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] — diagnose tokenizer, chat-template, role-boundary, and stop-condition mismatches.
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] — count rendered prompt tokens, reserve output, pack RAG/tool context, and test truncation behavior.
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] — prove model source, license, revision, artifact safety, and local path before serving.
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] — prove pinned downloads, cache paths, hashes, GGUF/Ollama import, conversion provenance, and cleanup before serving.
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] — estimate model weight memory, KV-cache risk, and runtime fit before downloading a model.
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] — prove WSL GPU visibility, vLLM/SGLang Python environments, loopback endpoints, `/v1/models`, Windows client calls, and metrics before runtime comparison.
- [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] — prove native and OpenAI-compatible endpoints, then diagnose serving failures.
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] — prove base URL, route, model id, streaming, error behavior, and feature gaps before client integration.
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] — score local model quality with workload prompts, rubrics, pairwise comparison, and RAG/citation checks.
