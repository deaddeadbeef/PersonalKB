---
tags: [chunk, llm]
id: "chunk-llm-187"
source: "[[LLM/_raw/raw-llm-047 Red Teaming Language Models to Reduce Harms]]"
source_loc: "Chunk Candidates"
topic: "Automated red teaming"
claim: "Language models can be used to automate red teaming by generating adversarial prompts at scale, complementing but not replacing human red teamers who find more creative attacks."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: How can automated red teaming work? A: A separate LM generates adversarial prompts designed to elicit harmful outputs from the target model, enabling testing at scale far beyond what human red teamers can achieve."
  - "Q: Does automated red teaming replace human red teaming? A: No — automated approaches find high-volume but often repetitive attacks, while human red teamers discover more creative, contextual, and unexpected failure modes. Both are needed."
up: "[[LLM/LLM]]"
---

# Automated Red Teaming Using Language Models

Ganguli et al. explored using language models themselves to automate the red teaming process. An attacker LM generates adversarial prompts at scale, and the target model's responses are evaluated for harmfulness. This approach enables testing thousands of attack variants far beyond human capacity. However, the study found that automated attacks tend to be repetitive and cluster around known vulnerability patterns, while human red teamers discover more creative and contextually nuanced attacks. The paper concluded that automated and human red teaming are complementary — automated methods provide breadth, humans provide depth and novelty.
