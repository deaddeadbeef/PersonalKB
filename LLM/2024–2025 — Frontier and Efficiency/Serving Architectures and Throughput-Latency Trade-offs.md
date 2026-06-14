---
tags: [llm, inference]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Serving Architectures and Throughput-Latency Trade-offs

> **One-line summary**: LLM serving is a constant balancing act between serving more work per second and keeping each user’s wait time low enough to feel responsive.

---

## 🎯 Intuition

### Core Idea
Serving systems must balance **throughput** (how much total work gets done) against **latency** (how long each request waits). Bigger batches keep GPUs busier and reduce cost per token, but they also make each request wait longer. Smaller batches feel snappier, but waste expensive hardware.

### Analogy
Serving is like **running a restaurant kitchen — balance orders at once (throughput) vs. wait time (latency)**.

### Why It Matters
The best operating point depends on workload. Chatbots need low latency to feel interactive. Batch pipelines care more about throughput. Multi-tenant systems need both, plus quality-of-service guarantees. Since GPU inference is expensive, the wrong serving setup burns money or frustrates users.

---

## ⚙️ Core Mechanics

### How It Works
Production serving stacks schedule requests, batch them, manage KV cache memory, and optimize decode kernels to navigate this trade-off. vLLM emphasizes throughput through PagedAttention and continuous batching. TensorRT-LLM pushes low-latency execution with optimized CUDA kernels and FP8. TGI focuses on deployment ergonomics plus built-in quantization and speculative decoding. SGLang adds structured generation and prefix-aware optimizations. All of them expose latency and throughput metrics so operators can tune the system for the workload.

### Key Specs
- **TTFT (Time-To-First-Token)**: latency from request arrival to the first generated token.
- **TPOT (Time-Per-Output-Token)**: average latency for each later token during decode.
- **Throughput**: tokens/sec or requests/sec per GPU.
- **Request completion time**: `TTFT + (num_output_tokens × TPOT)`.
- **GPU utilization**: share of time the GPU is computing instead of sitting idle.
- **Queue time**: time spent waiting before processing begins.

### Key Facts
- **vLLM**: PagedAttention + continuous batching; often **2–4×** higher throughput than naive batching.
- **TensorRT-LLM**: optimized CUDA kernels and FP8 support for low single-request latency.
- **TGI**: Hugging Face serving stack with built-in quantization and speculative decoding.
- **SGLang**: structured generation and **RadixAttention** for prefix caching.
- **llama.cpp**: CPU-optimized, GGUF-based, and suited to edge or mobile deployment.
- **A100** inference often costs about **$1–3/hour**; **H100** about **$3–8/hour**.
- **CPU inference** via llama.cpp or GGUF is roughly **10–50× cheaper per token** but **10–100× slower**.
- Auto-scaling new GPU instances often takes **30–60 seconds**, so bursty workloads need warm capacity or predictive scaling.
- Typical cost breakdown: **GPU rental 70–85%**, **networking 5–10%**, **storage/ops 5–10%**.


| Concept | What It Is | What It's Not |
| --- | --- | --- |
| **Throughput vs Latency** | Throughput: total work per time | Latency: time per individual request |
| **TTFT vs TPOT** | TTFT: prefill time (first token) | TPOT: decode time per token |
| **GPU vs CPU Inference** | GPU: 10-100× faster, 10-50× more expensive | CPU: slower but cheaper, good for batch/edge |
| **Batch Size vs Concurrency** | Batch size: requests per iteration | Concurrency: total active requests in system |
| **Auto-Scaling vs Over-Provisioning** | Auto-scale: dynamic capacity, cold-start delays | Over-provision: always-on headroom, higher baseline cost |
| **vLLM vs TensorRT-LLM** | vLLM: throughput-optimized, PagedAttention | TensorRT-LLM: latency-optimized, FP8, CUDA kernels |

---

## 🔬 Deep Dive

### Technical Details
Larger batches increase throughput but raise latency through queueing and slower per-token generation. Smaller batches reduce latency but underutilize the GPU. Chunked prefill can smooth the transition between prefill and decode phases. Speculative decoding can cut latency with roughly neutral throughput impact, though it adds some overhead. Quantization usually improves throughput by reducing memory bandwidth pressure and can slightly reduce latency, although dequantization introduces its own costs.

### Limitations
- A single serving configuration rarely fits every workload.
- Auto-scaling helps with spikes but introduces complexity and cold-start pain.
- Tokens-per-dollar optimization depends on the real bottleneck: compute, memory bandwidth, or idle time.
- CPU inference is cheaper, but often too slow for interactive use.

### Impact
Understanding these trade-offs is central to production deployment. A chatbot may need **<200ms TTFT** for responsiveness, while a document pipeline may happily accept **5-second** latency if throughput rises dramatically. Framework choice matters: vLLM usually wins on throughput, TensorRT-LLM on raw latency, and llama.cpp on cost efficiency for low-traffic or edge settings.

---

## 🏋️ Practice

### Warm-Up
- What is the difference between throughput and latency?
- Why can a larger batch improve cost efficiency but hurt user experience?

### Core Problems
- Explain the difference between **TTFT** and **TPOT**.
- Why might a batch-processing pipeline choose a different operating point than a chatbot?
- When would CPU inference be a reasonable choice?

### Challenge
- A service has low GPU utilization but good latency. What does that suggest about batch sizing?
- A service has great throughput but poor chat responsiveness. Which trade-off is likely being pushed too far?

For a practical local experiment, use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] to compare single-request latency against a controlled concurrency ladder. Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] when a latency or throughput claim needs request logs, server metrics, queue/KV/cache state, and resource-pressure evidence. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] when the serving question becomes "can this setup survive a restart, upgrade, rollback, cache move, or UI update?"

## Supporting Chunks

- [[chunk-llm-120 vLLM De Facto Serving Framework]] — why vLLM became the baseline open serving stack
- [[chunk-llm-118 vLLM Continuous Batching Throughput]] — throughput evidence for continuous batching
- [[LLM/Study/Local LLM Observability and Operations Runbook]] — practical local metrics, logs, resource counters, and operations rows
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]] — practical startup, upgrade, backup, rollback, and post-change validation rows
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]] — memory-management mechanism behind high concurrency
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]] — decode-stage hardware bottleneck
- [[chunk-llm-223 Speculative Decoding Speedup Analysis]] — latency gains from draft-target verification
- [[chunk-llm-224 Speculative Decoding Production Adoption]] — production adoption context for speculative decoding
- [[chunk-llm-208 GPTQ Standard for Open-Source Deployment]] — quantization as a serving-cost lever

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/_raw/raw-llm-030 vLLM PagedAttention Serving|vLLM PagedAttention Serving]]
- [[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA|Fast Transformer Decoding: One Write-Head Is All You Need]]
- [[LLM/_raw/raw-llm-056 Speculative Sampling for LLM Decoding|Speculative Sampling for LLM Decoding]]
- [[Quantization]]
- [[KV Cache and Context Reuse]]
- [[Batching and Continuous Batching]]
- [[Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
