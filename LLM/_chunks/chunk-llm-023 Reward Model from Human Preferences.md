---
tags: [chunk, llm]
id: "chunk-llm-023"
source: "[[LLM/_raw/raw-llm-006 InstructGPT Training with Human Feedback]]"
source_loc: "Section 3.2"
topic: "reward model"
claim: "The reward model takes (prompt, response) pairs and outputs a scalar score, trained on human pairwise preference comparisons"
confidence: "verified"
supports: ["[[LLM/Alignment and Safety/Reinforcement Learning from Human Feedback]]"]
up: "[[LLM/LLM]]"
---

# Reward Model from Human Preferences

## Context

The reward model (RM) in the RLHF pipeline is a Transformer that takes a (prompt, response) pair as input and outputs a single scalar score representing response quality. It is trained on comparison data: for each prompt, human labelers rank K outputs from best to worst. These rankings are converted into (K choose 2) pairwise comparisons, and the RM is trained using a cross-entropy loss to assign higher scores to preferred responses.

Specifically, the loss function is: L(θ) = -E[log σ(r_θ(x, y_w) - r_θ(x, y_l))], where y_w is the preferred response and y_l is the rejected response. InstructGPT used K=4 to K=9 rankings per prompt, generating 6 to 36 pairwise comparisons from each annotation task. The reward model was initialized from the SFT model (with the unembedding layer replaced by a scalar projection head) to leverage the language understanding already learned.

## Why It Matters

The reward model is the critical bridge between expensive human judgment and scalable optimization. Once trained, it can evaluate millions of (prompt, response) pairs without human involvement, providing the training signal for PPO. The quality of the reward model directly determines the quality of the final aligned model — a flawed RM leads to reward hacking. This has driven significant research into reward model training, including scaling RM size, ensembling, and using process-based rewards.

## QnA Seeds
- Q: Why train on pairwise comparisons rather than absolute ratings?
  A: Pairwise comparisons are more reliable because different annotators have different internal scales for absolute scores. Asking "which response is better?" produces much higher inter-annotator agreement than asking "rate this response 1-5." The ranking approach also generates multiple training pairs from a single annotation task (K rankings yield (K choose 2) pairs), improving data efficiency.
- Q: What is reward hacking and how does it relate to the reward model?
  A: Reward hacking occurs when the policy finds outputs that score highly on the reward model but are not genuinely good responses — exploiting gaps in the RM's understanding. For example, the model might learn to produce verbose, confident-sounding but incorrect responses if the RM associates length and confidence with quality. This is why the KL penalty is crucial: it constrains the policy to stay near the SFT distribution, limiting its ability to exploit RM weaknesses.
