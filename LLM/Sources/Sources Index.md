---
tags: [index, llm, sources]
up: "[[LLM/LLM]]"
confidence: verified
freshness: stable
tier-coverage: [core, deep-dive, provenance]
---

# Sources Index - LLM

> **One-line summary** A provenance map for the LLM wiki, generated from the raw source notes so every paper link points to an existing note.

This note anchors the sources used in the LLM knowledge base. Each row links to a raw source note; use the article pages and book spine for normal reading, and use this index when you need provenance.

Total raw source notes: **71**

## How To Use Sources

| Need | Use | Evidence habit |
|---|---|---|
| Verify an architecture or training claim | Start with the relevant paper row, then return to [[LLM/LLM Book Reading Spine|LLM Book Reading Spine]] | Capture claim, paper, year, mechanism, limitation, and the article that reused it |
| Connect papers to local inference | Pair this index with [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] | State the local implication and the run sheet, benchmark, or evaluation that could test it |
| Compare model families or eras | Use the paper groups below, then read the matching era overview | Keep chronology explicit so later models are not used as evidence for earlier claims |
| Reuse a current model or vendor claim | Check the raw note date and treat product claims as freshness-sensitive | Add an as-of date before using the claim in deployment or model-selection notes |

## Foundational Papers

| # | Title | Authors | Year | Type | Raw Note |
|---:|---|---|---:|---|---|
| 001 | Attention Is All You Need | Vaswani et al. | 2017 | paper | [[LLM/_raw/raw-llm-001 Attention Is All You Need|raw-llm-001]] |
| 002 | Language Models are Few-Shot Learners | Brown et al. | 2020 | paper | [[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners|raw-llm-002]] |
| 003 | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | Devlin et al. | 2018 | paper | [[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers|raw-llm-003]] |
| 004 | Scaling Laws for Neural Language Models | Kaplan et al. | 2020 | paper | [[LLM/_raw/raw-llm-004 Scaling Laws for Neural Language Models|raw-llm-004]] |
| 005 | Training Compute-Optimal Large Language Models | Hoffmann et al. | 2022 | paper | [[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)|raw-llm-005]] |
| 006 | Training language models to follow instructions with human feedback | Ouyang et al. | 2022 | paper | [[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback|raw-llm-006]] |
| 007 | LoRA: Low-Rank Adaptation of Large Language Models | Hu et al. | 2021 | paper | [[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation|raw-llm-007]] |
| 008 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. | 2022 | paper | [[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting|raw-llm-008]] |
| 009 | LLaMA: Open and Efficient Foundation Language Models | Touvron et al. | 2023 | paper | [[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models|raw-llm-009]] |
| 010 | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | Rafailov et al. | 2023 | paper | [[LLM/_raw/raw-llm-010 DPO Direct Preference Optimization|raw-llm-010]] |

## Architecture and Training

| # | Title | Authors | Year | Type | Raw Note |
|---:|---|---|---:|---|---|
| 011 | RoFormer: Enhanced Transformer with Rotary Position Embedding | Su et al. | 2021 | paper | [[LLM/_raw/raw-llm-011 RoFormer Rotary Position Embedding|raw-llm-011]] |
| 012 | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | Raffel et al. | 2019 | paper | [[LLM/_raw/raw-llm-012 T5 Unified Text-to-Text Transformer|raw-llm-012]] |
| 013 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | Dao et al. | 2022 | paper | [[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention|raw-llm-013]] |
| 014 | Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | Shoeybi et al. | 2019 | paper | [[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism|raw-llm-014]] |
| 015 | ZeRO: Memory Optimizations Toward Training Trillion Parameter Models | Rajbhandari et al. | 2019 | paper | [[LLM/_raw/raw-llm-015 ZeRO Memory Optimizations|raw-llm-015]] |
| 016 | Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Fedus et al. | 2021 | paper | [[LLM/_raw/raw-llm-016 Switch Transformers Trillion Parameter MoE|raw-llm-016]] |
| 017 | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | Gu & Dao | 2023 | paper | [[LLM/_raw/raw-llm-017 Mamba Selective State Spaces|raw-llm-017]] |
| 018 | GPT-4 Technical Report | OpenAI | 2023 | paper | [[LLM/_raw/raw-llm-018 GPT-4 Technical Report|raw-llm-018]] |
| 019 | LLaMA 2: Open Foundation and Fine-Tuned Chat Models | Touvron et al. | 2023 | paper | [[LLM/_raw/raw-llm-019 LLaMA 2 Open Chat Models|raw-llm-019]] |
| 020 | The Llama 3 Herd of Models | Dubey et al. | 2024 | paper | [[LLM/_raw/raw-llm-020 Llama 3 Herd of Models|raw-llm-020]] |

## Methods and Applications

| # | Title | Authors | Year | Type | Raw Note |
|---:|---|---|---:|---|---|
| 021 | Constitutional AI: Harmlessness from AI Feedback | Bai et al. | 2022 | paper | [[LLM/_raw/raw-llm-021 Constitutional AI Harmlessness|raw-llm-021]] |
| 022 | QLoRA: Efficient Finetuning of Quantized LLMs | Dettmers et al. | 2023 | paper | [[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs|raw-llm-022]] |
| 023 | Finetuned Language Models Are Zero-Shot Learners | Wei et al. | 2021 | paper | [[LLM/_raw/raw-llm-023 FLAN Instruction Tuning Zero-Shot|raw-llm-023]] |
| 024 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Lewis et al. | 2020 | paper | [[LLM/_raw/raw-llm-024 RAG Retrieval-Augmented Generation|raw-llm-024]] |
| 025 | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | 2022 | paper | [[LLM/_raw/raw-llm-025 ReAct Reasoning and Acting|raw-llm-025]] |
| 026 | Holistic Evaluation of Language Models | Liang et al. | 2022 | paper | [[LLM/_raw/raw-llm-026 HELM Holistic Evaluation|raw-llm-026]] |
| 027 | Learning Transferable Visual Models From Natural Language Supervision | Radford et al. | 2021 | paper | [[LLM/_raw/raw-llm-027 CLIP Visual Models Language Supervision|raw-llm-027]] |
| 028 | Robust Speech Recognition via Large-Scale Weak Supervision | Radford et al. | 2022 | paper | [[LLM/_raw/raw-llm-028 Whisper Robust Speech Recognition|raw-llm-028]] |
| 029 | A Survey of Large Language Models | Zhao et al. | 2023 | paper | [[LLM/_raw/raw-llm-029 Survey of Large Language Models|raw-llm-029]] |
| 030 | Efficient Memory Management for Large Language Model Serving with PagedAttention | Kwon et al. | 2023 | paper | [[LLM/_raw/raw-llm-030 vLLM PagedAttention Serving|raw-llm-030]] |

## Extended Catalog

| # | Title | Authors | Year | Type | Raw Note |
|---:|---|---|---:|---|---|
| 031 | Improving Language Understanding by Generative Pre-Training | Radford et al. | 2018 | paper | [[LLM/_raw/raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training|raw-llm-031]] |
| 032 | Language Models are Unsupervised Multitask Learners | Radford et al. | 2019 | paper | [[LLM/_raw/raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners|raw-llm-032]] |
| 033 | RoBERTa: A Robustly Optimized BERT Pretraining Approach | Liu et al. | 2019 | paper | [[LLM/_raw/raw-llm-033 RoBERTa A Robustly Optimized BERT Pretraining Approach|raw-llm-033]] |
| 034 | DeBERTa: Decoding-enhanced BERT with Disentangled Attention | He et al. | 2020 | paper | [[LLM/_raw/raw-llm-034 DeBERTa Decoding-enhanced BERT with Disentangled Attention|raw-llm-034]] |
| 035 | BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension | Lewis et al. | 2019 | paper | [[LLM/_raw/raw-llm-035 BART Denoising Sequence-to-Sequence Pre-training|raw-llm-035]] |
| 036 | PaLM: Scaling Language Modeling with Pathways | Chowdhery et al. | 2022 | paper | [[LLM/_raw/raw-llm-036 PaLM Scaling Language Modeling with Pathways|raw-llm-036]] |
| 037 | Gemini: A Family of Highly Capable Multimodal Models | Gemini Team | 2023 | paper | [[LLM/_raw/raw-llm-037 Gemini A Family of Highly Capable Multimodal Models|raw-llm-037]] |
| 038 | Mistral 7B | Jiang et al. | 2023 | paper | [[LLM/_raw/raw-llm-038 Mistral 7B|raw-llm-038]] |
| 039 | Mixtral of Experts | Jiang et al. | 2024 | paper | [[LLM/_raw/raw-llm-039 Mixtral of Experts|raw-llm-039]] |
| 040 | DeepSeek-V3 Technical Report | DeepSeek-AI | 2024 | paper | [[LLM/_raw/raw-llm-040 DeepSeek-V3 Technical Report|raw-llm-040]] |
| 041 | Layer Normalization | Ba et al. | 2016 | paper | [[LLM/_raw/raw-llm-041 Layer Normalization|raw-llm-041]] |
| 042 | Train Short, Test Long: Attention with Linear Biases Enables Input Length Generalization | Press et al. | 2021 | paper | [[LLM/_raw/raw-llm-042 ALiBi Train Short Test Long|raw-llm-042]] |
| 043 | SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing | Kudo et al. | 2018 | paper | [[LLM/_raw/raw-llm-043 SentencePiece|raw-llm-043]] |
| 044 | The Pile: An 800GB Dataset of Diverse Text for Language Modeling | Gao et al. | 2021 | paper | [[LLM/_raw/raw-llm-044 The Pile An 800GB Dataset|raw-llm-044]] |
| 045 | PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel | Zhao et al. | 2023 | paper | [[LLM/_raw/raw-llm-045 PyTorch FSDP|raw-llm-045]] |
| 046 | Training a Helpful and Harmless Assistant from Human Feedback | Bai et al. | 2022 | paper | [[LLM/_raw/raw-llm-046 Training a Helpful and Harmless Assistant with RLHF|raw-llm-046]] |
| 047 | Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned | Ganguli et al. | 2022 | paper | [[LLM/_raw/raw-llm-047 Red Teaming Language Models to Reduce Harms|raw-llm-047]] |
| 048 | Towards Monosemanticity: Decomposing Language Models With Dictionary Learning | Bricken et al. | 2023 | paper | [[LLM/_raw/raw-llm-048 Towards Monosemanticity Sparse Autoencoders|raw-llm-048]] |
| 049 | Universal and Transferable Adversarial Attacks on Aligned Language Models | Zou et al. | 2023 | paper | [[LLM/_raw/raw-llm-049 Universal Adversarial Attacks on Aligned LLMs|raw-llm-049]] |
| 050 | Toolformer: Language Models Can Teach Themselves to Use Tools | Schick et al. | 2023 | paper | [[LLM/_raw/raw-llm-050 Toolformer Language Models Can Teach Themselves to Use Tools|raw-llm-050]] |
| 051 | Self-Instruct: Aligning Language Models with Self-Generated Instructions | Wang et al. | 2022 | paper | [[LLM/_raw/raw-llm-051 Self-Instruct Aligning LMs with Self-Generated Instructions|raw-llm-051]] |
| 052 | GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | Frantar et al. | 2022 | paper | [[LLM/_raw/raw-llm-052 GPTQ Accurate Post-Training Quantization|raw-llm-052]] |
| 053 | AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | Lin et al. | 2023 | paper | [[LLM/_raw/raw-llm-053 AWQ Activation-aware Weight Quantization|raw-llm-053]] |
| 054 | Fast Transformer Decoding: One Write-Head is All You Need | Shazeer | 2019 | paper | [[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA|raw-llm-054]] |
| 055 | GQA: Training Generalized Multi-Query Attention Models from Multi-Head Checkpoints | Ainslie et al. | 2023 | paper | [[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models|raw-llm-055]] |
| 056 | Accelerating Large Language Model Decoding with Speculative Sampling | Chen et al. | 2023 | paper | [[LLM/_raw/raw-llm-056 Speculative Sampling for LLM Decoding|raw-llm-056]] |
| 057 | Dense Passage Retrieval for Open-Domain Question Answering | Karpukhin et al. | 2020 | paper | [[LLM/_raw/raw-llm-057 Dense Passage Retrieval DPR|raw-llm-057]] |
| 058 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | Asai et al. | 2023 | paper | [[LLM/_raw/raw-llm-058 Self-RAG Learning to Retrieve Generate and Critique|raw-llm-058]] |
| 059 | Visual Instruction Tuning | Liu et al. | 2023 | paper | [[LLM/_raw/raw-llm-059 Visual Instruction Tuning LLaVA|raw-llm-059]] |
| 060 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | 2023 | paper | [[LLM/_raw/raw-llm-060 Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena|raw-llm-060]] |

## Reasoning and Agents

| # | Title | Authors | Year | Type | Raw Note |
|---:|---|---|---:|---|---|
| 061 | Learning to Reason with LLMs | OpenAI | 2024 | technical_report | [[LLM/_raw/raw-llm-061|raw-llm-061]] |
| 062 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | DeepSeek AI | 2025 | technical_paper | [[LLM/_raw/raw-llm-062|raw-llm-062]] |
| 063 | Claude Model Family: Sonnet 4 through Opus 4.6 | Anthropic | 2025 | technical_report | [[LLM/_raw/raw-llm-063|raw-llm-063]] |
| 064 | GPT-5 Family: Unified Reasoning and Knowledge | OpenAI | 2025 | technical_report | [[LLM/_raw/raw-llm-064|raw-llm-064]] |
| 065 | Gemini 2.0 and 2.5: Native Multimodal Intelligence | Google DeepMind | 2025 | technical_report | [[LLM/_raw/raw-llm-065|raw-llm-065]] |
| 066 | Model Context Protocol Specification | Anthropic | 2024 | specification | [[LLM/_raw/raw-llm-066|raw-llm-066]] |
| 067 | Claude Code and the Rise of Agentic Coding | Anthropic | 2025 | product_analysis | [[LLM/_raw/raw-llm-067|raw-llm-067]] |
| 068 | Computer Use and GUI Agents | Various | 2025 | technical_analysis | [[LLM/_raw/raw-llm-068|raw-llm-068]] |
| 069 | Llama 4 and the Evolution of Open Models | Meta AI | 2025 | technical_report | [[LLM/_raw/raw-llm-069|raw-llm-069]] |
| 070 | Reasoning Distillation: From Frontier to Compact Models | Various | 2025 | technical_analysis | [[LLM/_raw/raw-llm-070|raw-llm-070]] |
| 071 | The Hitchhiker's Guide to Agentic AI: From Foundations to Systems | Haggai Roitman | 2026 | survey_pdf | [[LLM/_raw/raw-llm-071|raw-llm-071]] |

## References

- [[LLM/LLM|Large Language Models - A Chronicle]]
- [[LLM/LLM Corpus Index]]
- [[LLM/LLM Book Reading Spine]]

Refresh with `python _ops\generate_llm_sources_index.py` after adding or renaming raw LLM source notes.
