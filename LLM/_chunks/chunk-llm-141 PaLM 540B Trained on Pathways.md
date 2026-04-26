---
tags: [llm, chunk]
source: "[[raw-llm-036]]"
confidence: high
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat Overview]]"
  - "[[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism]]"
qna_seeds:
  - "Q: What hardware did PaLM use for training? A: PaLM was a 540B parameter dense decoder-only Transformer trained on Google's Pathways system across 6,144 TPU v4 chips in two TPU v4 pods, achieving 57.8% hardware FLOPs utilization — a record for models of that scale."
---

# PaLM 540B Trained on 6,144 TPU v4 Chips via Pathways

PaLM (Chowdhery et al., 2022) was a 540-billion parameter dense decoder-only Transformer trained on Google's Pathways system across 6,144 TPU v4 chips arranged in two TPU v4 pods. The training achieved 57.8% hardware FLOPs utilization at that scale, a record at the time. Pathways enabled efficient orchestration of computation across multiple pods connected via data center network, demonstrating that single-model training could effectively span thousands of accelerators.