---
tags: [chunk, llm]
id: "chunk-llm-186"
source: "[[LLM/_raw/raw-llm-047 Red Teaming Language Models to Reduce Harms]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "Red teaming scaling behavior"
claim: "Larger RLHF-trained models are harder to red-team successfully, but larger base models (before alignment) are more capable of generating harmful content — a dual scaling finding critical for safety planning."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: How does model size affect red teaming success? A: After RLHF, larger models are harder to red-team (better safety). But before RLHF, larger models generate more convincing harmful content (higher capability for misuse)."
  - "Q: Why is this dual scaling behavior important? A: It means that while alignment improves with scale, the potential damage from alignment failure also increases — making robust alignment increasingly critical as models grow."
up: "[[LLM/LLM]]"
---

# Larger Models Are Harder to Red-Team After RLHF

A key finding from Ganguli et al. is a dual scaling behavior in red teaming outcomes. After RLHF alignment, larger models are harder to red-team — they refuse harmful requests more consistently and are less susceptible to jailbreaking attempts. However, before alignment, larger base models are more capable of producing convincing harmful content, including detailed instructions and persuasive manipulation. This creates a critical safety dynamic: as models scale up, the gap between aligned and unaligned behavior widens, making robust alignment increasingly important because the consequences of alignment failure grow with model capability.
