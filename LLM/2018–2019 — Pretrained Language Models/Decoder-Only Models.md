---
tags: [llm, architecture]
up: "[[2018–2019 — Pretrained Language Models Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Decoder-Only Models

> **Decoder-only transformers win by doing one thing extremely well: predicting the next token from everything that came before it.**

## 🎯 Intuition
**The Core Idea:** A decoder-only transformer reads left-to-right under a causal mask, making next-token prediction and text generation the same basic operation.
**Analogy:** A decoder-only model is like an author writing one word at a time while only looking backward at what has already been written.
**Why It Matters:** Decoder-only models generate text autoregressively using causal masking, and this architecture became the dominant paradigm for modern LLMs. The same stack handles prompt processing, generation, chat, code, and reasoning without task-specific architectural changes. Its simplicity, combined with strong scaling behavior, is why GPT, LLaMA, Claude, Gemini, Mistral, and DeepSeek all follow this pattern.

---

## ⚙️ Core Mechanics
### How It Works
- A decoder-only transformer applies a causal attention mask that prevents each position from attending to future positions.
- This means the model processes tokens left-to-right, making it naturally suited for text generation: predict the next token, append it, repeat.
- The same architecture handles both "understanding" (processing the input) and "generation" (producing the output) in a unified forward pass.
- **Causal masking**: lower-triangular attention mask; position i only attends to positions ≤ i.
- **Autoregressive generation**: sample token from P(x_t | x_{<t}), append, repeat.
- **KV cache**: store key/value tensors for past tokens to avoid recomputation during generation.
- **Pre-fill vs decode**: pre-fill processes the prompt in parallel; decode generates one token at a time.
- **Modern architecture choices**: pre-norm, RoPE, SwiGLU FFN, GQA, RMSNorm (LLaMA recipe).
- **Context window**: maximum sequence length the model can process (4K → 128K → 1M+).

### Key Specifications

| Model | Parameters | Key Milestone |
|-------|------------|---------------|
| GPT-1 | 117M | Showed generative pretraining + fine-tuning works |
| GPT-2 | 1.5B | Showed zero-shot task performance emerges with scale |
| GPT-3 | 175B | Demonstrated in-context learning |
| GPT-4 | Not specified here | Extended to multimodal input and dramatically improved reasoning |

### Key Facts
- The GPT lineage demonstrated that decoder-only models scale remarkably well.
- Each generation showed that scaling decoder-only models produces qualitative capability jumps.
- Decoder-only won over encoder-only and encoder-decoder architectures because of architectural simplicity, natural fit for generation, and better scaling properties.
- Decoder-only is the architecture behind every frontier LLM named on this page: GPT-4, Claude, Gemini, LLaMA 3, Mistral, and DeepSeek.
- Understanding decoder-only models is effectively understanding modern large language models.

---

## 🔬 Deep Dive
### Technical Details
Decoder-only models are the dominant modern LLM architecture because the causal mask aligns perfectly with the language modeling objective: predict the next token from previous tokens. This makes training and inference conceptually unified. During inference, prompt tokens are processed in parallel in the pre-fill stage, after which generation switches into token-by-token decode mode, usually accelerated by a KV cache that stores prior attention state.

The architecture's minimalism is part of its strength. Rather than maintaining separate encoder and decoder stacks or alternating between bidirectional understanding and left-to-right generation, decoder-only models use one repeating block pattern with causal masking. Modern implementations refine that basic pattern through choices such as pre-norm, RoPE, SwiGLU feed-forward layers, grouped-query attention (GQA), RMSNorm, and ever-larger context windows.

Why decoder-only won over encoder-only and encoder-decoder is therefore not just historical accident: the architecture is simpler, maps directly onto generation, and scales well enough that task-specific distinctions blur as model size rises. The same stack can handle chat, code, reasoning, and instruction-following without architectural modification.

### Limitations and Criticisms
- Generation remains autoregressive at decode time, so inference is inherently sequential and slower than fully parallel token processing.
- Decoder-only models are optimized around next-token prediction, so they may rely on scale rather than specialized structure for some understanding-heavy tasks.
- The architecture is simple, but its emergent capabilities can obscure the engineering complexity needed for stable scaling, long contexts, and efficient serving.

### Impact and Legacy
Decoder-only transformers became the foundation of frontier AI. GPT-1 established generative pretraining plus fine-tuning, GPT-2 revealed zero-shot emergence, GPT-3 demonstrated in-context learning, and GPT-4 extended the paradigm into multimodality and stronger reasoning. This lineage made decoder-only transformers the default architecture for modern chatbots, code assistants, reasoning models, and open-weight LLM ecosystems.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does causal masking make decoder-only transformers naturally suited for generation?
2. What is the difference between the pre-fill stage and the decode stage?
3. Why does a KV cache help at inference time?

### Core Problems
1. Compare decoder-only with encoder-only and encoder-decoder architectures: which design choices most directly explain why decoder-only became dominant?
2. Trace the GPT lineage from GPT-1 to GPT-4 and explain what each milestone suggests about scaling behavior.

### Challenge
1. Make the strongest case you can that decoder-only simplicity—not just compute scale—was decisive in making it the dominant architecture for modern AI systems.

---

*See also:* [[2018–2019 — Pretrained Language Models Overview]], [[Transformer Architecture]], [[Scaling Laws]], [[Few-Shot Prompting]], [[Reinforcement Learning from Human Feedback]], [[Open-Weight Model Ecosystem]], [[LLM/Sources/Sources Index]]

## Supporting Chunks / References
### Supporting Chunks
- [[LLM/_chunks/chunk-llm-005 In-Context Learning Emerges at Scale|In-context learning emerges at scale]]
- [[LLM/_chunks/chunk-llm-007 Few-Shot Prompting Outperforms Zero-Shot|Few-shot prompting outperforms zero-shot]]
- [[LLM/_chunks/chunk-llm-008 GPT-3 Training Data Composition|GPT-3 training data composition]]
- [[LLM/_chunks/chunk-llm-012 Bidirectional Context Produces Richer Representations|Bidirectional vs decoder-only trade-off]]
- [[LLM/_chunks/chunk-llm-035 LLaMA Architecture Choices Became Standard|LLaMA architecture choices became standard]]
- [[LLM/_chunks/chunk-llm-121 GPT-1 Pre-Train Fine-Tune Paradigm|GPT-1 pre-train/fine-tune paradigm]]
- [[LLM/_chunks/chunk-llm-122 GPT-1 12-Layer Decoder Architecture|GPT-1 12-layer decoder architecture]]
- [[LLM/_chunks/chunk-llm-125 GPT-2 Zero-Shot Task Transfer|GPT-2 zero-shot task transfer]]
- [[LLM/_chunks/chunk-llm-127 GPT-2 Scaling from 117M to 1.5B|GPT-2 scaling from 117M to 1.5B]]
- [[LLM/_chunks/chunk-llm-213 Multi-Query Attention Shared KV Heads|Multi-query attention shared KV heads]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck|KV cache memory bandwidth bottleneck]]
- [[LLM/_chunks/chunk-llm-220 GQA Default Attention Modern LLMs|Grouped-query attention as a modern default]]

### References
- [[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners|raw-llm-002 GPT-3 Language Models are Few-Shot Learners]]
- [[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models|raw-llm-009 LLaMA Open Foundation Language Models]]
- [[LLM/_raw/raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training|raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training]]
- [[LLM/_raw/raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners|raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners]]
- [[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA|raw-llm-054 Fast Transformer Decoding One Write-Head MQA]]
- [[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models|raw-llm-055 GQA Training Generalized Multi-Query Transformer Models]]
- [[LLM/Sources/Sources Index]]

### Evidence Gaps
- The current frontier-model examples and context-window ranges should be refreshed from current model cards before future edits treat them as up-to-date.
