---
tags: [llm, pretraining]
up: "[[2020–2021 — The Scaling Era Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Training Infrastructure and Parallelism

> **Large-model training works by splitting computation, memory, and communication across many accelerators without losing efficiency.**

## 🎯 Intuition
**The Core Idea:** Training infrastructure scales frontier models by coordinating many GPUs so they act like one much larger training system.

**Analogy:** Training infrastructure is like an orchestra conductor coordinating thousands of GPU musicians: some play the same part in parallel, some play different sections, and everything only works if timing and communication stay synchronized.

**Why It Matters:** Frontier models cannot fit, train, or recover reliably on a single accelerator. Parallelism strategies determine whether a run reaches high utilization or wastes massive amounts of money in communication stalls and failures. At large scale, infrastructure is not just support machinery; it is a core determinant of what models can be trained at all.

---

## ⚙️ Core Mechanics
### How It Works
Training infrastructure and parallelism strategies enable scaling to thousands of GPUs and trillion-parameter models by distributing computation, memory, and communication efficiently across accelerators.

Training large models requires parallelism across multiple dimensions. **Data parallelism** replicates the model on each GPU, splits the batch, computes gradients independently, then averages gradients via all-reduce. This scales well to ~100s of GPUs but is memory-limited: each GPU must fit the entire model. **Tensor parallelism** (Megatron-LM) splits individual layers across GPUs—e.g., split attention heads or FFN across 8 GPUs. This reduces per-GPU memory but requires all-reduce communication within each layer (high bandwidth requirement).

**Pipeline parallelism** splits the model into stages (layers 1-10 on GPU 0, layers 11-20 on GPU 1, etc.) and processes micro-batches in a pipelined fashion to keep all GPUs busy. Naive pipeline parallelism has bubble time (idle GPUs); GPipe and PipeDream reduce bubbles through schedules. **FSDP (Fully Sharded Data Parallelism)** and **ZeRO** shard optimizer states, gradients, and parameters across data-parallel workers, reducing memory redundancy. ZeRO-3 shards everything, enabling models too large for any single GPU.

**3D parallelism** combines data, tensor, and pipeline parallelism: tensor parallel within nodes (8 GPUs via NVLink), pipeline parallel across nodes, data parallel across replicas. At extreme scale (thousands of GPUs), training is a complex dance of communication: **all-reduce** (average gradients in data parallelism), **all-gather** (collect sharded weights in FSDP), **reduce-scatter** (distribute reduction results). Hardware matters: **NVLink** provides 600 GB/s intra-node bandwidth; **InfiniBand** provides 100-400 GB/s inter-node. Memory bandwidth (A100: ~2 TB/s HBM) limits how fast you can feed tensors to compute units.

- **Data parallelism**: Replicate model N ways; all-reduce gradients every step; scales to batch_size × N
- **Tensor parallelism**: Split weight matrices (Q,K,V,FFN) across GPUs; all-reduce within each forward/backward layer
- **Pipeline parallelism**: Split layers into stages; process micro-batches in pipeline; bubble time is ~(P-1)/P without optimization
- **FSDP/ZeRO**: Shard optimizer states (ZeRO-1), gradients (ZeRO-2), parameters (ZeRO-3); all-gather parameters just-in-time
- **3D parallelism**: Tensor parallel = 8 (within node), pipeline parallel = 16 (across nodes), data parallel = 128 (replicas) → 16k GPUs
- **Communication primitives**: all-reduce (ring or tree), all-gather (collect shards), reduce-scatter (reduce and distribute)
- **Hardware**: NVLink (600 GB/s intra-node), InfiniBand (200-400 GB/s inter-node), HBM (A100: 2 TB/s)
- **Checkpointing**: Save model every N steps; use async saves to hide I/O latency; keep last 10-50 checkpoints
- **Fault tolerance**: Detect loss spikes, GPU failures; reload checkpoint; continue training; redundant health checks

### Key Specifications

| Parallelism Type | What's Split | Communication | Best For |
|------------------|--------------|---------------|----------|
| Data parallelism | Batch | All-reduce gradients per step | Small-medium models |
| Tensor parallelism | Layers/weights | All-reduce per layer | Medium models, high bandwidth |
| Pipeline parallelism | Model stages | Point-to-point activations | Large models, limited bandwidth |
| FSDP/ZeRO | Parameters, grads, optimizer | All-gather params, reduce-scatter grads | Memory-constrained, large models |
| 3D parallelism | All dimensions | Hierarchical communication | Extreme scale (1000+ GPUs) |

### Key Facts
- Data parallelism is simple and effective, but each GPU must still hold the full model.
- Tensor parallelism reduces per-GPU memory pressure but raises the cost of intra-layer communication.
- Pipeline parallelism improves scale for deep models, though poor scheduling creates bubble-time inefficiency.
- ZeRO and FSDP reduce redundancy by sharding states instead of replicating everything on every worker.
- At 10k-GPU scale, checkpointing and fault tolerance become mandatory rather than optional engineering extras.

---

## 🔬 Deep Dive
### Technical Details
The difference between 1 GPU and 10,000 GPUs isn't just 10,000× faster—it's qualitatively different capabilities. GPT-3 (175B) couldn't be trained on a single GPU; it required thousands. Modern infrastructure enables training in weeks what would take decades on a single accelerator. But parallelism isn't free: communication overhead grows, synchronization becomes complex, and failure rates increase (10,000 GPUs → higher failure probability).

The choice of parallelism strategy depends on model size and cluster shape. Small models (<10B): data parallelism suffices. Medium models (10-100B): tensor + data parallelism (Megatron-LM style). Huge models (100B-1T): 3D parallelism with FSDP. The engineering challenge is balancing compute (keep GPUs busy) with communication (minimize idle time waiting for gradients). NVLink and InfiniBand bandwidth determine how large you can scale tensor and pipeline parallelism before communication becomes the bottleneck.

Checkpointing and fault tolerance aren't optional at scale—they're survival. On a 10k GPU cluster, something fails every few hours (GPU error, network blip, cosmic ray). The ability to detect, isolate, and recover from failures without restarting from scratch is what makes trillion-token training economically viable. Companies invest heavily in orchestration systems (Google's Pathways, Meta's FSDP, Microsoft's DeepSpeed) because the difference between 50% and 80% GPU utilization is hundreds of millions of dollars.

### Limitations and Criticisms
- Communication overhead rises with scale, so adding more GPUs does not translate into linear speedups.
- Strategy choice is hardware-dependent: limited NVLink or InfiniBand bandwidth can make theoretically attractive parallelism schemes impractical.
- Extreme-scale training is operationally fragile, requiring elaborate checkpointing, orchestration, and recovery systems to remain economically viable.

### Impact and Legacy
Modern training infrastructure made GPT-3-scale and larger runs practical by combining multiple forms of parallelism instead of relying on simple model replication. Systems such as Megatron-LM, DeepSpeed, FSDP, and Pathways defined the engineering stack for thousand-GPU and trillion-token training. This infrastructure foundation also shaped later open-weight efforts, efficient training strategies, and the economics of the frontier model race.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does data parallelism stop being sufficient as model size grows?
2. What problem do ZeRO and FSDP solve that ordinary data parallelism does not?
3. Why is bandwidth as important as raw FLOPs in large training clusters?

### Core Problems
1. A team has a 100B+ model and a multi-node GPU cluster with strong intra-node NVLink but weaker inter-node links. Analyze how tensor, pipeline, and data parallelism should be combined.
2. Explain why GPU utilization can remain poor even when a cluster has enough raw compute, and relate your answer to bubble time, all-reduce costs, and checkpoint recovery.

### Challenge
1. Design a parallelism strategy for a trillion-parameter training run and justify how you would trade off memory savings, communication cost, and fault tolerance.

---

*See also:* [[Transformer Architecture]], [[Compute Data and Parameter Trade-offs]], [[Quantization]], [[Open-Weight Model Ecosystem]], [[Batching and Continuous Batching]], [[LLM/Sources/Sources Index]]

## Supporting Chunks
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

## References
- [[LLM/Sources/Sources Index]]
