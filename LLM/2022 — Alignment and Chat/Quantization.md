---
tags: [llm, inference]
up: "[[2022 — Alignment and Chat Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Quantization

> **One-line summary** Quantization compresses model weights and sometimes activations into lower-precision formats to cut memory use and inference cost while trying to preserve quality.

## 🎯 Intuition

**The Core Idea:**  
Quantization reduces the numerical precision of model weights and activations, typically from FP16 (16-bit floating point) to INT8, INT4, or even lower bit-widths. This directly reduces memory footprint and bandwidth requirements—the primary bottlenecks in LLM inference. A 7B parameter model in FP16 requires 14GB; quantizing to INT4 reduces this to 3.5GB, enabling inference on consumer GPUs or reducing server costs by fitting more models per GPU.

The challenge is preserving quality while compressing. Naive rounding degrades performance, especially for smaller models or lower bit-widths. Modern quantization methods use calibration data to find optimal scaling factors per layer or even per weight channel. Post-Training Quantization (PTQ) methods like GPTQ use one-shot calibration with layer-wise reconstruction, while AWQ identifies and protects "salient" weights that disproportionately affect accuracy. For extreme compression (INT4, INT3), quality degradation becomes noticeable, requiring careful benchmarking.

**Analogy:**  
It is like shrinking a high-resolution image for faster download: you keep the overall picture, but if you compress too aggressively, fine details and sharp edges start to disappear.

**Why It Matters:**  
Memory bandwidth is the primary bottleneck in LLM inference—the GPU spends most of its time waiting to load weights from memory. Quantization cuts memory transfers proportionally to bit reduction. For a 70B model, INT4 quantization enables inference on 2 GPUs instead of 8, dramatically reducing cost. It also enables on-device deployment for mobile and edge applications. The trade-off is quality: INT8 is nearly lossless for most tasks, INT4 shows measurable but acceptable degradation, lower bit-widths risk significant quality loss. Choosing quantization strategy requires understanding your quality requirements, hardware target, and whether you can afford a smaller high-precision model instead of a larger quantized one.

---

## ⚙️ Core Mechanics

### How It Works

- **GPTQ**: Layer-wise one-shot quantization with Hessian weighting for optimal rounding
- **AWQ**: Activation-aware quantization, scales important weights to preserve accuracy
- **GGUF/llama.cpp**: File format + runtime for CPU inference, mixed 2-8 bit quantization
- **SmoothQuant**: W8A8 quantization, migrates difficulty from activations to weights via smoothing
- **LLM.int8()**: Mixed precision for outlier dimensions (keeps ~0.1% of weights in FP16)
- **Bit-width options**: INT8 (minimal loss), INT4 (2-3% degradation typical), INT3/INT2 (experimental)
- **Calibration**: Use representative data (~128-1024 samples) to set scaling factors

### Key Specifications

Different quantization schemes target different hardware. GGUF and llama.cpp optimize for CPU inference with mixed bit-width schemes. SmoothQuant (W8A8) quantizes both weights and activations for GPU tensor cores. LLM.int8() uses mixed precision, keeping outlier features in FP16 while quantizing the rest to INT8. The format matters: some enable GPU acceleration, others prioritize CPU or portability. Quantization is not free—dequantization adds compute overhead, though this is usually outweighed by memory bandwidth savings.

### Key Facts

| Concept | What It Is | What It's Not |
|---------|-----------|---------------|
| **Post-Training Quantization (PTQ) vs QAT** | No retraining required, uses calibration data | Quantization-Aware Training requires full training loop |
| **Weight-Only vs W+A Quantization** | Quantize weights, keep activations FP16 | Quantize both weights and activations (W8A8) |
| **GPTQ vs AWQ** | GPTQ: Hessian-based optimal rounding | AWQ: Identify and protect important channels |
| **INT4 vs 4-bit NormalFloat** | Standard integer quantization | QLoRA's custom 4-bit format optimized for distributions |
| **Quantize Large Model vs Use Smaller Model** | 70B-INT4 vs 7B-FP16 | Not always equivalent—large quantized often better |
| **GGUF vs GPTQ** | CPU-optimized format with llama.cpp runtime | GPU-optimized, layer-wise calibration |

---

## 🔬 Deep Dive

### Technical Details

Quantization works because many inference bottlenecks are dominated by moving weights, not by floating-point arithmetic alone. If each parameter is stored with fewer bits, the system can move more useful information per unit time. This is especially valuable for large models where memory bandwidth dominates end-to-end latency.

Modern methods differ in how they minimize the damage from lower precision. PTQ methods avoid retraining by calibrating on representative inputs. GPTQ uses Hessian-informed reconstruction to make better rounding decisions. AWQ focuses on protecting especially important weights or channels. SmoothQuant changes the balance between activation difficulty and weight difficulty so both can be quantized more effectively. Mixed-precision schemes like LLM.int8() recognize that most values can be compressed safely, while a small set of outliers needs higher precision.

The choice of format is therefore a systems decision as much as a numerical one. Some formats are built around CPU-friendly runtimes, while others are designed for GPU kernels and tensor-core acceleration.

### Limitations and Criticisms

- Naive rounding can significantly degrade model quality
- Lower bit-widths, especially INT3 and INT2, remain experimental and require careful benchmarking
- Dequantization introduces extra compute overhead
- The best method depends heavily on hardware target and runtime support
- A larger quantized model is not always the right choice relative to a smaller high-precision model, even if it often performs surprisingly well

### Impact and Legacy

Quantization is one of the key techniques that made local and cost-efficient LLM inference practical. It enabled consumer-GPU deployment, lower serving cost, and wider experimentation with open-weight models.

It also created an ecosystem of specialized formats and runtimes, making deployment strategy inseparable from model architecture and hardware planning. In practice, quantization is now a standard knob in inference engineering, not a niche optimization.

### Local Inference Bridge

For local hosting, quantization must be tested as a deployment variable, not accepted from the filename alone. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] to compare a higher-precision or less aggressive baseline against the practical candidate, sweep CPU/GPU offload, record KV-cache precision, and run the same quality prompts. The keep/reject decision should name the exact artifact, runtime, offload setting, context target, memory headroom, and quality result.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. Why does quantization help inference even though it may add some dequantization overhead?
2. What is the rough memory change when moving a model from FP16 to INT4?
3. Why is INT4 usually riskier than INT8?

### Core Problems

1. Compare GPTQ, AWQ, SmoothQuant, GGUF, and LLM.int8() by target hardware and main idea.
2. Explain the difference between weight-only quantization and quantizing both weights and activations.
3. Suppose you need to deploy a 70B model cheaply. How would quantization change your hardware plan, and what benchmarks would you run before shipping?
4. When might a smaller FP16 model be preferable to a larger INT4 model?

### Challenge

Choose a deployment target (consumer laptop CPU, single consumer GPU, or multi-GPU server) and propose a quantization strategy. Justify the bit-width, runtime, and evaluation metrics you would use to decide whether the quality trade-off is acceptable.

## See Also

- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|QLoRA]] — combining quantization with fine-tuning
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Trade-offs]] — quantization's impact on serving economics
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] — choosing a model format and runtime for local inference
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] — estimating memory and quantization trade-offs before serving
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] — validating GGUF/AWQ/GPTQ/FP8/INT8 choices, GPU offload, KV-cache precision, speed, and quality

## References
### Supporting Chunks

- [[LLM/_chunks/chunk-llm-205 GPTQ Hessian-Based Weight Quantization|chunk-llm-205]] — GPTQ's second-order rounding method
- [[LLM/_chunks/chunk-llm-207 GPTQ 3-4 Bit Accuracy vs FP16|chunk-llm-207]] — 4-bit and 3-bit quality trade-offs
- [[LLM/_chunks/chunk-llm-208 GPTQ Standard for Open-Source Deployment|chunk-llm-208]] — why GPTQ became common in open-weight deployment
- [[LLM/_chunks/chunk-llm-209 AWQ Activation-Aware Salient Channels|chunk-llm-209]] — AWQ's activation-aware saliency criterion
- [[LLM/_chunks/chunk-llm-211 AWQ INT4 Edge Deployment Performance|chunk-llm-211]] — AWQ's edge and on-device deployment relevance
- [[LLM/_chunks/chunk-llm-085 QLoRA 4-bit Quantization with LoRA|chunk-llm-085]] — quantization for parameter-efficient fine-tuning

### References

- [[LLM/Sources/Sources Index]]
- [[LLM/_raw/raw-llm-052 GPTQ Accurate Post-Training Quantization|GPTQ Accurate Post-Training Quantization]]
- [[LLM/_raw/raw-llm-053 AWQ Activation-aware Weight Quantization|AWQ Activation-aware Weight Quantization]]
- [[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs|QLoRA Efficient Finetuning Quantized LLMs]]
- [[Serving Architectures and Throughput-Latency Trade-offs]]
- [[Open-Weight Model Ecosystem]]
