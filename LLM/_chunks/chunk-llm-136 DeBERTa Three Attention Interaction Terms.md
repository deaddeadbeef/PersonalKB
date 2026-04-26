---
tags: [llm, chunk]
source: "[[raw-llm-034]]"
confidence: high
supports:
  - "[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"
qna_seeds:
  - "Q: Why does DeBERTa omit the position-to-position attention term? A: DeBERTa uses only 3 of 4 possible disentangled attention terms (content-to-content, content-to-position, position-to-content), omitting position-to-position because relative position interactions without content provide limited additional signal and add unnecessary computation."
---

# DeBERTa Uses Three of Four Possible Attention Interaction Terms

In DeBERTa's disentangled attention, four interaction terms are theoretically possible: content-to-content, content-to-position, position-to-content, and position-to-position. DeBERTa uses only the first three, omitting position-to-position because the relative distance between two positions provides limited additional signal without content context, and including it would increase computation without meaningful accuracy gains. This design choice shows that principled ablation of attention components can reduce cost while maintaining or improving quality.