---
tags: [chunk, llm]
id: "chunk-llm-098"
source: "[[LLM/_raw/raw-llm-025 ReAct Reasoning and Acting]]"
source_loc: "Key Takeaways 2-3"
topic: "ReAct outperforms pure reasoning and pure acting"
claim: "ReAct outperforms both pure reasoning (CoT) and pure acting (tool use without reasoning) on knowledge-intensive and decision-making tasks."
confidence: "verified"
supports: ["[[LLM/Agents and Tool Use/Planning and Task Decomposition]]"]
up: "[[LLM/LLM]]"
---

# ReAct Outperforms Pure Reasoning and Pure Acting

## Context
The ReAct paper systematically compared three approaches: chain-of-thought reasoning only (the model reasons internally but cannot access tools), acting only (the model uses tools but without explicit reasoning traces), and ReAct (interleaved reasoning and acting). Experiments on HotpotQA (multi-hop question answering) and ALFWorld (interactive decision making) showed that ReAct outperformed both baselines.

Chain-of-thought alone struggled on knowledge-intensive tasks because the model would hallucinate facts when it lacked the needed information. Acting alone made errors because without reasoning traces, the model couldn't plan multi-step strategies or learn from intermediate observations. ReAct combined the strengths of both: reasoning traces enabled planning and interpretation, while tool access provided grounded factual information.

## Why It Matters
This result provides the empirical justification for the agent architecture pattern used throughout the industry. It shows that reasoning and tool use are complementary capabilities — neither alone is sufficient for complex tasks — and that the performance gap is significant enough to warrant the additional complexity of the interleaved approach.

## QnA Seeds
- Q: Why does chain-of-thought alone fail on knowledge-intensive tasks?
  A: Without access to external tools, the model must rely on internal knowledge and tends to hallucinate facts when it lacks the needed information.
- Q: What specific benchmarks demonstrated ReAct's superiority?
  A: HotpotQA (multi-hop question answering requiring fact lookup) and ALFWorld (interactive decision making in simulated environments).
