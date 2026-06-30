---
tags: [llm, history]
up: "[[2018–2019 — Pretrained Language Models Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# GPT and Decoder-Only Lineage

> **The GPT lineage showed that simple next-token prediction, when scaled and aligned, can become a general-purpose intelligence engine.**

## 🎯 Intuition
**The Core Idea:** Decoder-only models learn by predicting the next token from all previous tokens, and scaling that simple objective unlocked broad capabilities from transfer learning to dialogue and multimodal reasoning.
**Analogy:** Like watching a chatty toddler grow into a brilliant conversationalist using the same basic brain plan—just bigger, better trained, and better taught to behave.
**Why It Matters:** The GPT lineage established decoder-only transformers as the dominant architecture for general-purpose language models. It also showed that capability alone is not enough: alignment and interface design turned raw model power into practical usefulness, reshaping the entire AI field.

---

## ⚙️ Core Mechanics
### How It Works
- The GPT family traces a remarkably consistent arc from a modest 117M-parameter experiment to a multimodal system that passed the bar exam, demonstrating that autoregressive language modeling—simply predicting the next token—scales into general intelligence when combined with enough parameters, data, and alignment techniques.
- **Autoregressive objective**: P(x) = ∏ P(xₜ | x₁, ..., xₜ₋₁); predict next token given all previous tokens; causal (left-to-right) attention mask
- **Causal self-attention**: Lower-triangular mask prevents attending to future tokens; enables parallel training while maintaining autoregressive property
- **Scaling trajectory**: 117M → 1.5B → 175B → ~1.8T (rumored); each jump ~10× brought qualitative capability shifts
- **In-context learning (ICL)**: Zero-shot (task description only), few-shot (task + examples), many-shot; no weight updates; hypothesized as implicit Bayesian inference
- **RLHF pipeline (InstructGPT)**: (1) Supervised fine-tuning on human demonstrations → (2) Train reward model on human preference rankings → (3) Optimize policy via PPO against reward model
- **ChatGPT dialogue format**: System prompt + user/assistant turns; fine-tuned on dialogue trees with multiple ranked responses per turn
- **GPT-4 multimodal**: Accepts interleaved text and image inputs; vision encoder (likely ViT-based) produces token embeddings fed alongside text tokens
- **Emergent capabilities**: Abilities that appear discontinuously at scale—chain-of-thought reasoning, code generation, multilingual transfer—not present in smaller models of the same family

### Key Specifications

| Model | Date | Params | Key Capability | Training Innovation |
|-------|------|--------|---------------|-------------------|
| GPT-1 | Jun 2018 | 117M | Transfer learning proof | Generative pre-training |
| GPT-2 | Feb 2019 | 1.5B | Zero-shot generalization | Scale + WebText data |
| GPT-3 | May 2020 | 175B | In-context learning | 175B scale, few-shot prompting |
| InstructGPT | Jan 2022 | ~1.3B | Instruction following | RLHF alignment |
| ChatGPT | Nov 2022 | ~175B | Multi-turn dialogue | Dialogue fine-tuning on RLHF base |
| GPT-4 | Mar 2023 | ~1.8T* | Multimodal, expert-level reasoning | MoE (rumored), vision encoder |

*\*Unconfirmed; widely reported estimates*

### Key Facts
- GPT-1 used a 12-layer transformer decoder pretrained on BookCorpus and then fine-tuned for downstream tasks.
- GPT-2 was trained on WebText (40GB of high-quality web pages) and demonstrated strong zero-shot performance without downstream fine-tuning.
- GPT-3 was the inflection point that validated scaling and in-context learning.
- InstructGPT showed that a much smaller aligned model could be more useful in practice than a larger unaligned one.
- ChatGPT and GPT-4 extended the lineage into conversational and multimodal systems with mainstream impact.

---

## 🔬 Deep Dive
### Technical Details
**GPT-1** (Radford et al., June 2018, 117M parameters) was a proof of concept: a 12-layer transformer decoder pre-trained on BookCorpus, then fine-tuned for downstream tasks. It showed that generative pre-training could transfer to discriminative tasks, but it was overshadowed by BERT's bidirectional approach.

**GPT-2** (February 2019, 1.5B parameters) made a bolder bet—it was never fine-tuned at all. Trained on WebText (40GB of high-quality web pages), GPT-2 demonstrated zero-shot task performance across summarization, translation, and question answering. OpenAI's staged release, citing concerns about misuse, was the first major AI safety media event and established the pattern of capability announcements doubling as safety communications.

**GPT-3** (Brown et al., May 2020, 175B parameters) was the inflection point. Trained on 300B tokens from a filtered Common Crawl mixture, it demonstrated **in-context learning (ICL)**—the ability to perform tasks specified entirely through prompt examples with zero gradient updates. Few-shot GPT-3 matched or exceeded fine-tuned BERT models on many benchmarks, validating the scaling hypothesis and shifting the field's center of gravity from architecture design to scale and data curation.

**InstructGPT** (Ouyang et al., January 2022) then solved GPT-3's biggest problem—it would follow harmful instructions, hallucinate confidently, and produce unhelpful outputs. Using **Reinforcement Learning from Human Feedback (RLHF)**, InstructGPT aligned the model's behavior with human preferences, making it more helpful, harmless, and honest despite being 100× smaller than GPT-3.

**ChatGPT** (November 30, 2022) was InstructGPT's conversational descendant, fine-tuned for multi-turn dialogue. It became the fastest-growing consumer application in history, reaching 100 million users in two months.

**GPT-4** (March 2023) introduced multimodal input (text + images), achieved human-level performance on professional exams (90th percentile on the bar exam), and demonstrated substantially improved reasoning. Its architecture details remain undisclosed, though it is widely believed to be a **Mixture of Experts (MoE)** model with ~1.8T total parameters and ~280B active per forward pass.

The lineage also showed why decoder-only models became dominant: autoregressive models have a simple training objective, scale predictably, and develop emergent capabilities that bidirectional models typically do not. The same architecture that generates text also "understands" it, without needing a separate encoder.

More broadly, the GPT arc demonstrated that **alignment matters as much as capability**. GPT-3 was powerful but unreliable; InstructGPT was weaker on paper but far more useful in practice. ChatGPT then showed that interface matters too: a conversational wrapper transformed the same underlying technology from a developer-facing capability into a cultural phenomenon.

### Limitations and Criticisms
- GPT-1 was overshadowed by BERT’s bidirectional encoder approach in the early transfer-learning era.
- GPT-2’s staged release highlighted serious misuse concerns and began a long-running debate about how frontier-model capability disclosure should work.
- GPT-4’s architecture details remain undisclosed, so some widely repeated claims—such as MoE structure and total parameter count—remain unconfirmed.

### Impact and Legacy
The GPT lineage established decoder-only transformers as the winning architecture for general-purpose language models. It validated scaling laws, normalized in-context learning, made RLHF central to model deployment, created the modern alignment research ecosystem, and showed that conversational product design could turn model capability into mass adoption almost overnight.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is next-token prediction considered a simpler training objective than many alternative pretraining schemes?
2. What made GPT-2’s zero-shot behavior so important relative to GPT-1’s fine-tuning-based transfer story?
3. Why did InstructGPT matter even though it was far smaller than GPT-3?

### Core Problems
1. Compare GPT-2, GPT-3, and InstructGPT as three different bets: scale without fine-tuning, scale plus in-context learning, and scale plus alignment. What changed at each stage?
2. Explain how causal masking, in-context learning, and RLHF together support the decoder-only path from language modeling to useful assistants.

### Challenge
1. Evaluate the claim that the most important innovations in the GPT lineage were not architectural but instead came from scale, data curation, alignment, and interface design.

---

*See also:* —

## Supporting Chunks
### Supporting Chunks
- [[LLM/_chunks/chunk-llm-005 In-Context Learning Emerges at Scale|In-context learning emerges at scale]]
- [[LLM/_chunks/chunk-llm-006 Power-Law Scaling of Task Performance|Power-law scaling of task performance]]
- [[LLM/_chunks/chunk-llm-007 Few-Shot Prompting Outperforms Zero-Shot|Few-shot prompting outperforms zero-shot]]
- [[LLM/_chunks/chunk-llm-008 GPT-3 Training Data Composition|GPT-3 training data composition]]
- [[LLM/_chunks/chunk-llm-021 RLHF Three-Stage Pipeline|RLHF three-stage pipeline]]
- [[LLM/_chunks/chunk-llm-022 Alignment Matters More Than Scale for Usefulness|Alignment matters more than scale for usefulness]]
- [[LLM/_chunks/chunk-llm-069 GPT-4 Multimodal Input|GPT-4 multimodal input]]
- [[LLM/_chunks/chunk-llm-070 GPT-4 Reasoning Benchmark Performance|GPT-4 reasoning benchmark performance]]
- [[LLM/_chunks/chunk-llm-071 GPT-4 Closed Research Shift|GPT-4 closed research shift]]
- [[LLM/_chunks/chunk-llm-121 GPT-1 Pre-Train Fine-Tune Paradigm|GPT-1 pre-train/fine-tune paradigm]]
- [[LLM/_chunks/chunk-llm-122 GPT-1 12-Layer Decoder Architecture|GPT-1 12-layer decoder architecture]]
- [[LLM/_chunks/chunk-llm-125 GPT-2 Zero-Shot Task Transfer|GPT-2 zero-shot task transfer]]
- [[LLM/_chunks/chunk-llm-126 WebText Dataset Curation|WebText dataset curation]]
- [[LLM/_chunks/chunk-llm-127 GPT-2 Scaling from 117M to 1.5B|GPT-2 scaling from 117M to 1.5B]]
- [[LLM/_chunks/chunk-llm-128 GPT-2 Staged Release for Safety|GPT-2 staged release for safety]]

## References
- [[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners|raw-llm-002 GPT-3 Language Models are Few-Shot Learners]]
- [[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback|raw-llm-006 InstructGPT Training with Human Feedback]]
- [[LLM/_raw/raw-llm-018 GPT-4 Technical Report|raw-llm-018 GPT-4 Technical Report]]
- [[LLM/_raw/raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training|raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training]]
- [[LLM/_raw/raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners|raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners]]
- [[LLM/Sources/Sources Index]]
