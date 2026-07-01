---
tags: [llm, era-hub]
up: "[[LLM]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# 2018–2019 — Pretrained Language Models

The pretrain-then-fine-tune paradigm emerges. The architecture splits into encoder-only vs decoder-only paths, establishing a divergence that defines the field to this day. Transfer learning — long successful in computer vision — finally works for NLP, and a single pretrained model can be adapted to dozens of downstream tasks with minimal task-specific data.

## The Transfer Learning Breakthrough

Before 2018, NLP models were typically trained from scratch for each task. ELMo (Peters et al., February 2018) showed that deep contextualized word representations from a bidirectional LSTM, used as features, improved performance across tasks. ULMFiT (Howard & Ruder, January 2018) demonstrated that a language model pretrained on a large corpus could be fine-tuned for classification with careful learning rate scheduling. These results proved that transfer learning was viable for NLP, setting the stage for the transformer-based pretraining revolution.

## BERT and the Encoder Revolution

BERT (Devlin et al., October 2018) applied the transformer encoder to bidirectional pretraining using two objectives: masked language modeling (MLM), which predicts randomly masked tokens from both left and right context, and next sentence prediction (NSP). BERT achieved state-of-the-art results on 11 NLP benchmarks simultaneously, making pretrain-then-fine-tune the default paradigm. Its bidirectional attention made it ideal for understanding tasks — classification, NER, question answering — where the full context is available. See [[BERT and Encoder Lineage]] for the full lineage from BERT through RoBERTa, ALBERT, and ELECTRA.

## GPT and the Decoder Path

GPT-1 (Radford et al., June 2018) took the opposite approach: pretrain a unidirectional (left-to-right) transformer decoder on next-token prediction, then fine-tune on downstream tasks. GPT-2 (Radford et al., February 2019) scaled this to 1.5B parameters and demonstrated that a large enough language model could perform tasks zero-shot without any fine-tuning — its release was famously staged due to concerns about misuse. The decoder-only path would ultimately win the generation race, leading to GPT-3 and beyond. See [[GPT and Decoder-Only Lineage]].

## The Architecture Split

The transformer's modular design naturally split into three variants: encoder-only (BERT and descendants), decoder-only (GPT and descendants), and encoder-decoder (T5, BART). Encoder-only models excel at classification and understanding tasks because bidirectional attention captures full-context representations. Decoder-only models excel at generation because causal attention aligns with left-to-right text production. Encoder-decoder models (T5, Raffel et al. 2019) frame all tasks as text-to-text, providing a unified interface. See [[Encoder-Only Models]] and [[Decoder-Only Models]] for detailed comparisons.

## Pretraining Objectives

The choice of pretraining objective defines what a model learns. Causal language modeling (CLM) — predicting the next token — is the foundation of GPT-style models. Masked language modeling (MLM) — predicting randomly masked tokens — is BERT's approach, producing rich bidirectional representations but preventing autoregressive generation. ELECTRA (Clark et al., 2020) replaced MLM with replaced token detection, achieving BERT-level performance with less compute. T5's span corruption objective masks contiguous spans rather than individual tokens. See [[Supervised Fine-Tuning]] for how these pretrained models are adapted to specific tasks.

## The Fine-Tuning Paradigm

Fine-tuning a pretrained model requires adding a task-specific head (e.g., a linear classifier) and training the entire model or upper layers on labeled data. This is dramatically more sample-efficient than training from scratch. The standard recipe — pretrain on a large corpus, then fine-tune on a smaller task dataset — was validated across dozens of NLP tasks and became the default workflow. Domain-specific pretraining (e.g., BioBERT, SciBERT) further improved performance on specialized text. See [[Domain Adaptation]] for domain-specific approaches.

## Benchmarks Define Progress

Standardized benchmarks became essential for comparing models. GLUE (Wang et al., 2018) and its harder successor SuperGLUE (2019) provided multi-task evaluation suites covering sentiment, entailment, question answering, and coreference. SQuAD (Rajpurkar et al.) tested reading comprehension. BERT's simultaneous state-of-the-art across GLUE/SuperGLUE tasks demonstrated the power of the pretrain-fine-tune paradigm and drove rapid model iteration. See [[Knowledge and Reasoning Benchmarks]] for the evolution of evaluation methodology.

## Early Efficiency

As pretrained models grew, efficiency became a concern. DistilBERT (Sanh et al., October 2019) showed that knowledge distillation could compress BERT to 60% of its size while retaining 97% of its performance. ALBERT (Lan et al., 2019) used parameter sharing and factorized embeddings. TinyBERT and MobileBERT targeted edge deployment. These early compression techniques laid the groundwork for the parameter-efficient and quantization methods that would become critical at larger scales. See [[Distillation and Model Compression]] and [[Data Curation and Deduplication]] for how data quality intersects with efficient training.

## Pages in This Era

- [[BERT and Encoder Lineage]]
- [[GPT and Decoder-Only Lineage]]
- [[Encoder-Only Models]]
- [[Decoder-Only Models]]
- [[Supervised Fine-Tuning]]
- [[Domain Adaptation]]
- [[Knowledge and Reasoning Benchmarks]]
- [[Distillation and Model Compression]]
- [[Data Curation and Deduplication]]

## Related Eras

← Previous: [[2017 — The Transformer Overview|2017 — The Transformer]]
→ Next: [[2020–2021 — The Scaling Era Overview|2020–2021 — The Scaling Era]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Corpus Index]]
- [[LLM/LLM Book Reading Spine]]
