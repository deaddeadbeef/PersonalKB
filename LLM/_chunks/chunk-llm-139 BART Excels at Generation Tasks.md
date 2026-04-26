---
tags: [llm, chunk]
source: "[[raw-llm-035]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/2018–2019 — Pretrained Language Models Overview]]"
qna_seeds:
  - "Q: What types of tasks does BART's architecture excel at? A: BART excels at text generation tasks — particularly abstractive summarization, where it achieved state-of-the-art on CNN/DailyMail (44.16 ROUGE-L) and XSum (25.17 ROUGE-L) — because its encoder-decoder design naturally maps corrupted inputs to clean outputs."
---

# BART Achieved State-of-the-Art on Summarization Benchmarks

BART's encoder-decoder architecture naturally excels at text generation tasks because the denoising pre-training objective directly trains the model to produce fluent text from corrupted input. BART achieved state-of-the-art results on abstractive summarization benchmarks CNN/DailyMail (44.16 ROUGE-L) and XSum (25.17 ROUGE-L), substantially outperforming prior models. Its strong generation capability made BART the foundation for many subsequent summarization and conditional generation systems.