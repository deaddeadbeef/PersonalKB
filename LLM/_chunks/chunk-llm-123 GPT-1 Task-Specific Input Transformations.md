---
tags: [llm, chunk]
source: "[[raw-llm-031]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning]]"
qna_seeds:
  - "Q: How did GPT-1 adapt to different downstream tasks? A: GPT-1 used task-specific input transformations — restructuring inputs for classification, entailment, similarity, and QA into contiguous token sequences with delimiter tokens, allowing a single architecture to handle diverse task formats."
---

# GPT-1 Task-Specific Input Transformations

Rather than designing separate architectures for each task, GPT-1 used task-specific input transformations that converted classification, entailment, similarity, and question-answering inputs into contiguous token sequences separated by delimiter tokens. This allowed the same pre-trained model to be fine-tuned on diverse NLP tasks with minimal architectural changes — only a linear output layer was added per task. This approach anticipated the later "text-to-text" framing used by T5 and the prompt-based formatting of GPT-3.