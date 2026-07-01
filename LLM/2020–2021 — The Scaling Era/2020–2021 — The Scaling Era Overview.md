---
tags: [llm, era-hub]
up: "[[LLM]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# 2020–2021 — The Scaling Era

GPT-3 proves that scale is a strategy. Few-shot learning, scaling laws, and parameter-efficient methods rewrite the rules. Models jump from 1.5B to 175B parameters in a single generation, and the field discovers that emergent capabilities — abilities not present in smaller models — appear as scale increases. The investment thesis for building ever-larger models takes hold.

## GPT-3 and the Shock of Scale

GPT-3 (Brown et al., May 2020) scaled the decoder-only transformer to 175 billion parameters, trained on 300B tokens from a filtered web corpus. Its defining revelation was few-shot learning: by providing a handful of input-output examples in the prompt, GPT-3 could perform translation, arithmetic, code generation, and reasoning without any gradient updates. This "in-context learning" ability was qualitatively different from anything seen at smaller scales and shifted the field's focus from fine-tuning to prompting. See [[Few-Shot Prompting]] for prompting techniques that emerged from this work.

## Scaling Laws

Kaplan et al. ("Scaling Laws for Neural Language Models," January 2020) empirically demonstrated that test loss follows smooth power-law relationships with model parameters, dataset size, and compute budget. These laws enabled researchers to predict performance before training and to allocate compute optimally. The key insight: for a fixed compute budget, it is better to train a larger model for fewer steps than a smaller model for longer. This work was later refined by the Chinchilla paper (Hoffmann et al., 2022), which showed the original laws under-estimated the importance of data. See [[Scaling Laws]].

## In-Context Learning

GPT-3 revealed that large language models can learn from examples provided in the prompt without weight updates — a phenomenon called in-context learning (ICL). Research into ICL mechanisms showed that transformers implicitly implement learning algorithms (e.g., gradient descent) within their forward pass. The number and format of in-context examples significantly affect performance, and ICL scales with model size. This discovery reframed the role of the prompt from simple instruction to a form of soft programming. See [[In-Context Learning Mechanisms]].

## Parameter-Efficient Fine-Tuning

As models grew to hundreds of billions of parameters, full fine-tuning became impractical. Adapters (Houlsby et al., 2019) inserted small bottleneck layers into each transformer block. Prefix tuning (Li & Liang, 2021) and prompt tuning (Lester et al., 2021) learned continuous prompt embeddings while freezing the base model. LoRA (Hu et al., June 2021) decomposed weight updates into low-rank matrices, enabling fine-tuning with a fraction of the trainable parameters. These methods made it feasible to customize massive models for specific tasks and domains. See [[Parameter-Efficient Fine-Tuning]] and [[LoRA and QLoRA]].

## Vision Meets Language

CLIP (Radford et al., January 2021) trained a vision encoder and text encoder jointly on 400M image-text pairs using contrastive learning, producing aligned embeddings that enabled zero-shot image classification and powerful cross-modal retrieval. DALL·E (January 2021) generated images from text descriptions. These models demonstrated that the language modeling paradigm could extend beyond text, and the CLIP embedding space became foundational infrastructure for later vision-language models. See [[Vision-Language Models]].

## Retrieval-Augmented Generation

RAG (Lewis et al., May 2020) combined a pretrained retriever (DPR) with a pretrained generator (BART), allowing the model to ground its outputs in retrieved documents. This addressed hallucination and knowledge currency — two fundamental limitations of parametric-only models. REALM (Guu et al., 2020) showed that retrieval could be integrated into pretraining itself. RAG laid the architectural foundation for the production retrieval systems that would become critical infrastructure by 2023. See [[Retrieval Pipelines and Context Assembly]].

## MoE Returns

Mixture-of-Experts models, originally proposed by Jacobs et al. (1991), returned at transformer scale. Switch Transformer (Fedus et al., January 2021) demonstrated that sparsely-activated MoE layers could scale to 1.6 trillion parameters while keeping per-example compute manageable — each token activates only a subset of expert FFN blocks. This established MoE as a viable path to scaling beyond dense model limits and foreshadowed later production MoE models like Mixtral. See [[Mixture-of-Experts Models]].

## Infrastructure for Scale

Training 175B-parameter models required new infrastructure. Data parallelism, tensor parallelism (Megatron-LM, Shoeybi et al. 2019), pipeline parallelism (GPipe, PipeDream), and ZeRO (Rajbhandari et al., 2020) enabled distributed training across thousands of GPUs. Mixed-precision training (FP16/BF16 with loss scaling) reduced memory and accelerated computation. DeepSpeed and Megatron-DeepSpeed became standard toolkits. These engineering advances were as essential to the scaling era as the architectural innovations. See [[Training Infrastructure and Parallelism]].

## Emerging Concerns

Scale brought new problems. Benchmark contamination — where training data inadvertently includes evaluation examples — became a growing concern as web-scraped corpora expanded. Models also exhibited catastrophic forgetting when fine-tuned sequentially on different tasks, losing previously acquired knowledge. These issues drove research into decontamination methods, continual learning, and more robust evaluation practices. See [[Contamination and Data Leakage]] and [[Continual Fine-Tuning and Catastrophic Forgetting]].

## Pages in This Era

- [[Scaling Laws]]
- [[Few-Shot Prompting]]
- [[In-Context Learning Mechanisms]]
- [[Parameter-Efficient Fine-Tuning]]
- [[LoRA and QLoRA]]
- [[Vision-Language Models]]
- [[Retrieval Pipelines and Context Assembly]]
- [[Training Infrastructure and Parallelism]]
- [[Contamination and Data Leakage]]
- [[Mixture-of-Experts Models]]
- [[Continual Fine-Tuning and Catastrophic Forgetting]]

## Related Eras

← Previous: [[2018–2019 — Pretrained Language Models Overview|2018–2019 — Pretrained Language Models]]
→ Next: [[2022 — Alignment and Chat Overview|2022 — Alignment and Chat]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Corpus Index]]
- [[LLM/LLM Book Reading Spine]]
