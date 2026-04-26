---
tags: [chunk, llm]
id: "chunk-llm-181"
source: "[[LLM/_raw/raw-llm-046 Training a Helpful and Harmless Assistant with RLHF]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Helpfulness-harmlessness trade-off"
claim: "Training for harmlessness via RLHF can reduce a model's helpfulness, creating a fundamental tension that requires careful balancing of multiple reward objectives."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: What is the helpfulness-harmlessness trade-off? A: Optimizing a model to refuse harmful requests can make it overly cautious and less helpful for legitimate queries — excessive safety training degrades utility."
  - "Q: How did Bai et al. address this trade-off? A: They studied the Pareto frontier between helpfulness and harmlessness scores, showing that careful reward model design and PPO hyperparameter tuning can improve both simultaneously up to a point."
up: "[[LLM/LLM]]"
---

# Helpfulness and Harmlessness Trade-Off in RLHF

Bai et al. demonstrated a fundamental tension in RLHF alignment: training a model to be harmless (refusing dangerous requests, avoiding toxic content) can make it overly cautious and less helpful for legitimate queries. Their empirical analysis mapped the Pareto frontier between helpfulness and harmlessness reward scores, showing that naive optimization for one objective degrades the other. However, they also found that with careful reward model design and PPO tuning, both objectives can be improved simultaneously up to a certain point before trade-offs become unavoidable. This framing of alignment as multi-objective optimization became foundational for subsequent work.
