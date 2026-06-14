---
tags: [study, llm, cheatsheet]
up: "[[LLM/Study/LLM Study Index]]"
---

# LLM Architecture Cheatsheet

Quick-reference for key architectural decisions, formulas, and model specifications.

Use [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]] when a formula here needs the tensor-shape or local-inference explanation behind it.

## Core Formulas

| Formula | Meaning |
|---------|---------|
| softmax(QK^T/$\sqrt{d_k}$)V | Scaled dot-product attention |
| C ≈ 6ND | Training FLOPs ≈ 6 × params × tokens |
| PPL = exp(-1/N × Σ log P(x_i)) | Perplexity |
| W = W_0 + BA | LoRA weight decomposition |
| tokens ≈ 20 × params | Chinchilla compute-optimal ratio |
| KV memory = 2 × L × H × d × seq × dtype | KV cache size per sequence |

## Model Architecture Comparison

| Model | Type | Params | Context | Key Innovation |
|-------|------|--------|---------|---------------|
| BERT-base | Encoder | 110M | 512 | Masked LM, pre-train/fine-tune |
| GPT-3 | Decoder | 175B | 2K | In-context learning at scale |
| T5-11B | Enc-Dec | 11B | 512 | Text-to-text unified framework |
| LLaMA 2 | Decoder | 7-70B | 4K | Open-weight, RoPE, SwiGLU |
| Mixtral 8×7B | MoE | 47B (13B active) | 32K | Open sparse MoE |
| GPT-4 | Decoder (MoE?) | undisclosed | 128K | Multimodal, frontier reasoning |
| Mamba | SSM | 130M-2.8B | unlimited | Linear complexity, selective states |

## Position Encoding Quick Reference

| Method | Type | Extrapolation | Dominant In |
|--------|------|--------------|-------------|
| Sinusoidal | Fixed absolute | Limited | Original transformer |
| Learned | Trained absolute | None | BERT, GPT-2 |
| RoPE | Relative (rotation) | Good + extensions | LLaMA, Mistral, Qwen, most modern |
| ALiBi | Relative (bias) | Good | BLOOM, MPT |

## Attention Variants

| Variant | KV Heads | Memory | Quality |
|---------|----------|--------|---------|
| Multi-Head (MHA) | H (one per head) | High | Best |
| Multi-Query (MQA) | 1 (shared) | Lowest | Slight degradation |
| Grouped-Query (GQA) | G groups (1 < G < H) | Medium | Near-MHA quality |

## Quantization Methods

| Method | Precision | Type | Speed | Quality Loss |
|--------|-----------|------|-------|-------------|
| FP16/BF16 | 16-bit | Baseline | 1× | None |
| SmoothQuant | W8A8 | Weight+Activation | ~2× | Minimal |
| GPTQ | W4A16 | Weight-only, calibrated | ~3× | Small |
| AWQ | W4A16 | Weight-only, salient-aware | ~3× | Small |
| GGUF (Q4) | 4-bit | CPU-optimized | Varies | Small-moderate |

## Alignment Pipeline Comparison

| Method | Components | Complexity | Key Advantage |
|--------|-----------|-----------|---------------|
| SFT only | Demonstration data | Low | Simple, good baseline |
| RLHF | SFT + RM + PPO | High | Most flexible, online learning |
| DPO | Preference pairs + BCE loss | Medium | Simple, no RM/PPO needed |
| Constitutional AI | Principles + self-critique + RLAIF | Medium | Scales without human annotation |

## Key Benchmarks

| Benchmark | Tests | Format | Notable For |
|-----------|-------|--------|------------|
| MMLU | Broad knowledge (57 subjects) | Multiple choice | Standard knowledge test |
| GSM8K | Grade-school math | Open-ended | CoT showcase |
| HumanEval | Python coding (164 problems) | Code execution | pass@k metric |
| SWE-Bench | Real GitHub issues | Patch generation | Real-world software engineering |
| Chatbot Arena | Overall chat quality | Pairwise human preference | ELO-based, crowdsourced |
| MT-Bench | Multi-turn conversation | LLM-as-judge (1-10) | Automated eval standard |

## Serving Stack Quick Reference

| System | Key Feature | Best For |
|--------|------------|----------|
| vLLM | PagedAttention + continuous batching | High-throughput serving |
| TensorRT-LLM | Custom CUDA kernels | Maximum single-request speed |
| TGI | HuggingFace integration | Quick deployment |
| SGLang | Structured generation focus | Constrained output |
| llama.cpp | CPU inference, GGUF quantization | Local/edge deployment |
