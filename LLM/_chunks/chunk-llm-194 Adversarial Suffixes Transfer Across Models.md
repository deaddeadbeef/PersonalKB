---
tags: [chunk, llm]
id: "chunk-llm-194"
source: "[[LLM/_raw/raw-llm-049 Universal Adversarial Attacks on Aligned LLMs]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Adversarial transferability"
claim: "Adversarial suffixes optimized on open-source models transfer to attack closed-source models like ChatGPT and Claude, demonstrating cross-architecture vulnerability."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: Do adversarial suffixes transfer between different LLMs? A: Yes — suffixes optimized on open-source models (LLaMA, Vicuna) successfully attacked closed-source systems (ChatGPT, Claude, Bard) that the attacker had no gradient access to."
  - "Q: Why is transferability concerning? A: It means attackers can use open-source models as white-box proxies to develop attacks against proprietary models, eliminating the protection that closed weights were thought to provide."
up: "[[LLM/LLM]]"
---

# Adversarial Suffixes Transfer Across Models

A critical finding of the GCG paper is that adversarial suffixes exhibit strong transferability across model architectures and training pipelines. Suffixes optimized on open-source models (LLaMA-2, Vicuna) successfully caused closed-source commercial systems (ChatGPT, Claude, Bard) to generate harmful content — despite the attacker having no access to those models' weights or gradients. This transferability suggests that different aligned LLMs share common vulnerabilities in how their safety training manifests in token space. It also means that keeping model weights proprietary does not protect against adversarial attacks, since open-source proxies can serve as attack development platforms.
