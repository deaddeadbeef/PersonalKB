---
tags: [study, llm, papers, research-literacy, synthesis]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [core, deep-dive]
last-verified: 2026-06-15
---

# LLM 20-Paper Fast Path Synthesis Map

> **One-line summary** The 20-paper fast path is one causal story: attention made scalable sequence modeling possible, pretraining made general representations useful, scaling made prompting work, systems made training and inference practical, alignment made assistants usable, adaptation made local customization cheap, retrieval/tools made applications grounded, and evaluation made trade-offs visible.

Use this after [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] and the paper list in [[LLM/Study/LLM Study Index|LLM Study Index]]. This note is the capstone paper map requested by [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]: it connects architecture, scaling, alignment, retrieval, evaluation, and inference instead of treating the papers as isolated milestones. Use [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]] when the next proof needs claim, evidence, limitation, mechanism, and local implication rows for each paper. Use [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]] when those rows need coverage, source-proof, and follow-up-route validation. Use [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] when a paper cluster should become a local proof artifact, and use [[LLM/Study/LLM Serving Systems Paper-to-Local Proof Map|LLM Serving Systems Paper-to-Local Proof Map]] when the cluster is specifically about serving kernels, iteration scheduling, KV-cache management, chunked prefill, prefix reuse, or runtime metrics.

Use this before [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]]. If you can reproduce this map without looking, the academic side of the LLM path is starting to become usable knowledge.

## The One-Page Causal Story

1. **Transformer attention replaced sequence bottlenecks.** [[LLM/_raw/raw-llm-001 Attention Is All You Need|Attention Is All You Need]] showed that self-attention, multi-head projections, residual paths, layer norm, and positional information can model sequences without recurrence or convolution.
2. **Pretraining split into encoder, decoder, and encoder-decoder lineages.** [[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers|BERT]] optimized bidirectional masked prediction for understanding; [[LLM/_raw/raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training|GPT-1]] used left-to-right generative pretraining plus downstream adaptation; [[LLM/_raw/raw-llm-012 T5 Unified Text-to-Text Transformer|T5]] framed tasks as text-to-text transfer.
3. **Decoder-only scaling turned language modeling into a general interface.** [[LLM/_raw/raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners|GPT-2]] made zero-shot task transfer credible, and [[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners|GPT-3]] showed that large models can perform tasks from examples in the prompt.
4. **Scaling laws made capability planning quantitative.** [[LLM/_raw/raw-llm-004 Scaling Laws for Neural Language Models|Kaplan scaling laws]] made loss predictable from parameters, data, and compute; [[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)|Chinchilla]] corrected the recipe toward more data per parameter.
5. **Training and inference systems became part of model quality.** [[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism|Megatron-LM]] showed how tensor parallelism trains models too large for one GPU; [[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention|FlashAttention]] showed that memory movement can dominate attention cost.
6. **Open-weight models moved research into local practice.** [[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models|LLaMA]] combined efficient architecture choices, public data, and heavy token training, making strong local and fine-tuned models practical.
7. **Post-training turned raw models into assistants.** [[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback|InstructGPT]] established SFT, reward modeling, and RLHF; [[LLM/_raw/raw-llm-021 Constitutional AI Harmlessness|Constitutional AI]] used principles and AI feedback for harmlessness; [[LLM/_raw/raw-llm-010 DPO Direct Preference Optimization|DPO]] simplified preference optimization.
8. **Adaptation made customization affordable.** [[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation|LoRA]] trained low-rank adapter matrices while freezing the base model; [[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs|QLoRA]] combined quantized base weights with adapters for single-GPU fine-tuning.
9. **Inference-time behavior became a design surface.** [[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting|Chain-of-Thought]] showed that prompts can elicit multi-step reasoning at sufficient scale.
10. **Systems around the model became as important as the model.** [[LLM/_raw/raw-llm-024 RAG Retrieval-Augmented Generation|RAG]] added retrieval and attribution; [[LLM/_raw/raw-llm-025 ReAct Reasoning and Acting|ReAct]] interleaved reasoning, actions, and observations.
11. **Evaluation became multi-dimensional.** [[LLM/_raw/raw-llm-026 HELM Holistic Evaluation|HELM]] made it clear that accuracy alone is not enough; robustness, calibration, fairness, toxicity, and efficiency also matter.

## Fast Path Matrix

| Cluster               | Papers                                                                           | What changed                                                                                     | Mechanism to understand                                                        | Local/practical implication                                                                        |                                                                                                         |                                                                                                                                                                  |                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Architecture base     | [[LLM/_raw/raw-llm-001 Attention Is All You Need                                 | Transformer]]                                                                                    | Sequence modeling became parallel and attention-centered.                      | Scaled dot-product attention, multi-head attention, positional encoding, residual/norm stack.      | Explains why every local decoder spends time in prefill, attention, decode, and KV-cache growth.        |                                                                                                                                                                  |                                                                                                        |
| Pretraining lineages  | [[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers      | BERT]], [[LLM/_raw/raw-llm-031 GPT-1 Improving Language Understanding by Generative Pre-Training | GPT-1]], [[LLM/_raw/raw-llm-012 T5 Unified Text-to-Text Transformer            | T5]]                                                                                               | The field split into encoder-only, decoder-only, and encoder-decoder transfer patterns.                 | MLM, causal LM, span corruption, task framing, pretrain-then-adapt.                                                                                              | Helps choose model families: embeddings/encoders, chat decoders, or seq2seq summarization/translation. |
| Promptable scale      | [[LLM/_raw/raw-llm-032 GPT-2 Language Models are Unsupervised Multitask Learners | GPT-2]], [[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners                      | GPT-3]]                                                                        | Tasks moved from fine-tuning every dataset to prompting a general model.                           | Zero-shot transfer, few-shot prompting, in-context learning, scale-dependent behavior.                  | Explains why local small models may need stronger prompts, examples, RAG, tools, or adaptation.                                                                  |                                                                                                        |
| Compute planning      | [[LLM/_raw/raw-llm-004 Scaling Laws for Neural Language Models                   | Scaling Laws]], [[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)                | Chinchilla]]                                                                   | Model training became a resource allocation problem.                                               | Power-law loss, data/parameter/compute coupling, compute-optimal tokens per parameter.                  | Explains why a smaller overtrained open model can beat a larger undertrained model for local inference.                                                          |                                                                                                        |
| Large-scale systems   | [[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism                             | Megatron-LM]], [[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention                    | FlashAttention]]                                                               | Hardware and memory hierarchy became first-class research objects.                                 | Tensor parallelism, all-reduce placement, SRAM/HBM tiling, online softmax.                              | Explains runtime differences, attention kernels, context-length cost, and why hardware fit matters; use [[LLM/Study/LLM Serving Systems Paper-to-Local Proof Map | LLM Serving Systems Paper-to-Local Proof Map]] for serving-specific proof cards.                       |
| Open model practice   | [[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models                     | LLaMA]]                                                                                          | Strong open-weight bases made local and community fine-tuning practical.       | Public-data training, Chinchilla-style token scale, RoPE, SwiGLU, pre-norm, efficient size ladder. | Justifies the local model acquisition, provenance, runtime compatibility, and benchmark labs.           |                                                                                                                                                                  |                                                                                                        |
| Assistant alignment   | [[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback                  | InstructGPT]], [[LLM/_raw/raw-llm-021 Constitutional AI Harmlessness                             | Constitutional AI]], [[LLM/_raw/raw-llm-010 DPO Direct Preference Optimization | DPO]]                                                                                              | Raw completion models became instruction-following assistants.                                          | SFT, reward models, PPO, KL penalty, constitutional critique/revision, preference-pair loss.                                                                     | Explains why base models, instruct models, chat templates, and refusal behavior differ.                |
| Cheap adaptation      | [[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation                                  | LoRA]], [[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs                         | QLoRA]]                                                                        | Fine-tuning moved from full-weight training to adapter and quantized workflows.                    | Low-rank update matrices, frozen base weights, NF4, double quantization, paged optimizers.              | Explains when to use prompting, RAG, LoRA/QLoRA, or no training in [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide                                     | Adaptation and Fine-Tuning Decision Guide]].                                                           |
| Reasoning behavior    | [[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting                                | Chain-of-Thought]]                                                                               | Prompt format became a way to expose latent reasoning behavior.                | Few-shot worked examples, step-by-step traces, scale dependence, self-consistency.                 | Explains why reasoning quality changes with model size, sampling, output budget, and evaluation method. |                                                                                                                                                                  |                                                                                                        |
| Grounded applications | [[LLM/_raw/raw-llm-024 RAG Retrieval-Augmented Generation                        | RAG]], [[LLM/_raw/raw-llm-025 ReAct Reasoning and Acting                                         | ReAct]]                                                                        | Applications started coupling models to retrievers, tools, and observations.                       | Retriever-generator pipeline, top-k evidence, citation support, thought-action-observation loop.        | Explains the local RAG harness, tool-calling lab, context budget, and security boundary.                                                                         |                                                                                                        |
| Evaluation discipline | [[LLM/_raw/raw-llm-026 HELM Holistic Evaluation                                  | HELM]]                                                                                           | Model comparison moved beyond a single benchmark score.                        | Scenario taxonomy, multiple metrics, robustness, calibration, fairness, toxicity, efficiency.      | Explains why local model choice needs [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide       | metric interpretation]], quality, latency, memory, safety, and workload-specific gates.                                                                          |                                                                                                        |

## What Each Paper Teaches You To Ask

| Paper | The mastery question |
|---|---|
| Transformer | Can I derive attention shapes and explain why attention made parallel training possible? |
| BERT | Do I know when bidirectional encoders are better than decoder-only generators? |
| GPT-1 | Can I explain pretraining plus downstream adaptation before chat-style prompting existed? |
| GPT-2 | Can I explain zero-shot transfer as a scaling/data effect rather than magic? |
| GPT-3 | Can I separate in-context learning from weight updates? |
| Scaling Laws | Can I reason about model size, data, compute, and loss as coupled variables? |
| Chinchilla | Can I explain why more parameters are not always compute-optimal? |
| Megatron-LM | Can I name the communication/memory problem solved by tensor parallelism? |
| FlashAttention | Can I explain why exact attention can be faster by reducing memory traffic? |
| LLaMA | Can I connect open weights, training data, architecture choices, and local deployment? |
| T5 | Can I explain the encoder-decoder/text-to-text branch and why it still matters? |
| InstructGPT | Can I trace SFT, reward modeling, PPO, and human preference evaluation? |
| Constitutional AI | Can I explain how principles and AI feedback change the data pipeline? |
| DPO | Can I explain why preference optimization can avoid an explicit reward model? |
| LoRA | Can I explain low-rank adapters and why they add no merged-inference latency? |
| QLoRA | Can I explain how quantized bases and adapters reduce memory enough for local fine-tuning? |
| Chain-of-Thought | Can I explain why reasoning traces are prompt-time behavior, not proof of faithful cognition? |
| RAG | Can I separate retrieval recall, context assembly, generation, citation, and refusal failures? |
| ReAct | Can I explain the difference between reasoning-only prompting and action-grounded agent loops? |
| HELM | Can I defend a model decision across accuracy, robustness, safety, fairness, and efficiency? |

## Bridge To Local Hosting

Academic papers become practical when they explain an operational symptom.

| Local symptom | Paper cluster that explains it | Use this vault lab |
|---|---|---|
| Prompt is long and first token is slow | Transformer, FlashAttention, KV/cache systems | [[LLM/Study/LLM Inference Request Lifecycle Lab]], [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| Small local model ignores instructions | GPT-3, InstructGPT, DPO, LLaMA | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]], [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Larger model does not fit memory | Chinchilla, LLaMA, QLoRA, systems papers | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]], [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]] |
| RAG answer cites the wrong source | RAG, HELM, ReAct | [[LLM/Study/Local RAG Assistant Lab]], [[LLM/Study/Local RAG Minimal Python Harness]] |
| Tool loop takes unsafe action | ReAct, function-calling lineage, alignment papers | [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]], [[LLM/Study/Local LLM Security and Privacy Runbook]] |
| Benchmark is fast but answer is wrong | HELM, InstructGPT, RAG evaluation | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]], [[LLM/Study/Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Fine-tuning feels tempting but unclear | LoRA, QLoRA, DPO, RAG | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]] |

## Oral Recall Gate

You pass the paper-map gate when you can answer these without opening the note:

- What did the Transformer remove from the dominant sequence-model pipeline?
- Why are BERT, GPT, and T5 three different pretraining lineages?
- What is the difference between fine-tuning, prompting, and in-context learning?
- Why did Chinchilla change the interpretation of scaling laws?
- Why are Megatron-LM and FlashAttention part of LLM knowledge, not only infrastructure trivia?
- Why did LLaMA matter for local LLM practice?
- How do RLHF, Constitutional AI, and DPO differ as alignment/post-training methods?
- Why do LoRA and QLoRA change the economics of adaptation?
- How do RAG and ReAct move capability outside the model weights?
- Why does HELM argue against single-number model selection?

## Completion Gate

The fast-path paper map is complete when:

- [ ] you can reproduce the causal story from attention to evaluation without notes
- [ ] every paper has a one-sentence "what changed" answer
- [ ] every paper is tied to at least one mechanism, one evidence type, and one limitation
- [ ] every cluster has a local deployment implication
- [ ] the paper claim audit runner has a pass output or a remediation row for missing claim/source/route fields
- [ ] the current capstone claim set has a paper-to-local proof route
- [ ] missed oral-recall answers are remediated with [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Serving Systems Paper-to-Local Proof Map]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
