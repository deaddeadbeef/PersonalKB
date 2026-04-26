---
tags: [llm, chunk]
source: "[[raw-llm-034]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models]]"
qna_seeds:
  - "Q: What is the Enhanced Mask Decoder in DeBERTa? A: The Enhanced Mask Decoder incorporates absolute position information in the final decoding layer before the softmax prediction, complementing the relative position information used throughout the Transformer layers to provide the full positional context needed for masked token prediction."
---

# DeBERTa Enhanced Mask Decoder Adds Absolute Position

DeBERTa's disentangled attention uses only relative positions throughout the Transformer layers, but some tasks require absolute position information (e.g., in "a new store opened beside the new mall," the model needs absolute positions to correctly predict masked tokens). The Enhanced Mask Decoder addresses this by incorporating absolute position embeddings in the final decoding layer, just before the softmax prediction head. This two-stage approach — relative positions in attention, absolute positions in decoding — captures both types of positional information more effectively than either alone.