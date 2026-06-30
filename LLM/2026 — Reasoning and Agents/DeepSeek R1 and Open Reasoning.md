---
tags: [llm, reasoning-agents]
up: "[[2026 — Reasoning and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# DeepSeek R1 and Open Reasoning

> **One-line summary** DeepSeek R1 demonstrated that reasoning capabilities can be developed through reinforcement learning alone and released as open weights, making advanced reasoning accessible to the broader community.

## 🎯 Intuition

### Core Idea

DeepSeek R1 showed that frontier-style reasoning was not locked inside closed labs. It matched or exceeded OpenAI's o1 on several benchmarks while being released as open weights, and it showed that reinforcement learning alone could produce strong reasoning behaviour.

### Analogy

DeepSeek R1 is like an open-source recipe matching a Michelin chef's dish: the performance was close enough to prove that elite results were reproducible outside the original kitchen.

### Why It Matters

That changed both access and theory. Practically, more people could use strong reasoning models. Scientifically, R1-Zero suggested that structured reasoning can emerge from RL without supervised fine-tuning.

---

## ⚙️ Core Mechanics

### How It Works

DeepSeek AI released R1 in January 2025 as an open-weights reasoning model. The training story has two key stages:

- **R1-Zero** used pure reinforcement learning with no supervised fine-tuning (SFT), and it developed chain-of-thought reasoning, self-verification, and even apparent "aha moments" in reasoning traces.
- The full **R1** model added a cold-start SFT phase to improve readability and reduce language mixing.

DeepSeek used **Group Relative Policy Optimization (GRPO)**, a PPO variant that removes the need for a separate critic model, helping reduce training cost.

### Key Specs

- Release: **January 2025**
- Weights: **open**, under the **MIT license**
- Training method: **RL**, then **RL + cold-start SFT** for the full model
- Distilled sizes: **1.5B / 7B / 8B / 14B / 32B / 70B**

### Key Facts

- **R1-Zero**: pure RL (no SFT), emergent chain-of-thought reasoning
- **AIME 2024**: R1 scored 79.8% (vs o1's 83.3%)
- **MATH-500**: R1 scored 97.3%
- **Open weights** under MIT license — fully permissive commercial use
- **GRPO**: Group Relative Policy Optimization eliminates critic model
- **Distilled variants**: 1.5B / 7B / 8B / 14B / 32B / 70B parameters
- **Training cost**: approximately $5.6M (fraction of frontier model budgets)
- **14B distilled model** outperformed o1-mini on multiple benchmarks

| Aspect | DeepSeek R1 | OpenAI o1 |
|--------|-------------|-----------|
| Weights | Open (MIT license) | Closed |
| Training | RL + cold-start SFT | Undisclosed |
| Distillation | 6 public variants | o1-mini only |
| AIME 2024 | 79.8% | 83.3% |
| MATH-500 | 97.3% | 96.4% |
| Training cost | ~$5.6M (reported) | Undisclosed |

---

## 🔬 Deep Dive

### Technical Details

Perhaps the most consequential result was distillation. DeepSeek released smaller R1-derived models at six sizes, and the **14B distilled model outperformed o1-mini on several benchmarks**. That showed that reasoning behaviour could transfer effectively into much smaller architectures.

### Limitations

- Reported comparisons still depend on benchmark selection
- R1-Zero needed refinement because pure RL traces were less readable and had language-mixing issues
- Open access does not remove the broader costs of deployment and inference

### Impact

R1 weakened the assumption that advanced reasoning requires closed, frontier-scale infrastructure. It also pushed the field toward open reasoning research, cheaper replication, and stronger small-model distillation.

### Related Notes

- [[Reasoning Models and Test-Time Compute]] — the paradigm R1 replicates
- [[Reasoning Distillation]] — the technique enabling small model reasoning
- [[Open-Weight Model Ecosystem]] — R1's place in the open model landscape
- [[Reinforcement Learning from Human Feedback]] — RL techniques in LLM training
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]] — local harness for R1-style thinking traces, reasoning parsers, effort sweeps, latency, quality, and trace policy.

---

## 🏋️ Practice

### Warm-Up

1. What was unusual about R1-Zero's training setup?
2. Why did DeepSeek add a cold-start SFT phase after pure RL?

### Core Problems

1. Explain the significance of GRPO in the R1 training story.
2. Compare DeepSeek R1 and OpenAI o1 on openness, training disclosure, and benchmark performance.
3. Describe why the 14B distilled model mattered for the broader ecosystem.

### Challenge

Argue whether DeepSeek R1's bigger contribution was scientific insight about reasoning emergence or practical democratization through open weights and distillation.

---

## Supporting Chunks

- [[LLM/_chunks/chunk-llm-244 DeepSeek R1-Zero develops chain-of-thought reasoning through pure reinforcement learning without SFT|chunk-llm-244 DeepSeek R1-Zero develops chain-of-thought reasoning through pure reinforcement learning without supervised fine-tuning]]
- [[LLM/_chunks/chunk-llm-245 DeepSeek R1 uses GRPO to eliminate the critic model reducing training cost|chunk-llm-245 DeepSeek R1 matches o1 on benchmarks using GRPO training at fraction of frontier cost]]
- [[LLM/_chunks/chunk-llm-246 DeepSeek R1 distilled 14B model outperforms o1-mini on reasoning benchmarks|chunk-llm-246 R1 distilled 14B model outperforms o1-mini demonstrating effective reasoning transfer to smaller architectures]]

## References

→ [[Sources Index]]
