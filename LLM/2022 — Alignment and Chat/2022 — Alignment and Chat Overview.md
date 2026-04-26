---
tags: [llm, era-hub]
up: "[[LLM]]"
---

# 2022 — Alignment and Chat

Making LLMs helpful, harmless, and honest. RLHF, instruction tuning, and chain-of-thought transform raw language models into usable assistants — and ChatGPT changes the world. This year marks the transition from models that complete text to models that follow instructions, and from research artifacts to consumer products used by hundreds of millions.

## InstructGPT and the RLHF Pipeline

InstructGPT (Ouyang et al., March 2022) formalized the three-stage alignment pipeline: (1) supervised fine-tuning on human-written demonstrations, (2) training a reward model on human preference comparisons, and (3) optimizing the policy with Proximal Policy Optimization (PPO) against the reward model. This RLHF pipeline dramatically improved instruction-following and reduced harmful outputs compared to base GPT-3, even though InstructGPT (1.3B parameters) was preferred by human raters over the much larger GPT-3 (175B). See [[Reinforcement Learning from Human Feedback]].

## Instruction Tuning at Scale

FLAN (Wei et al., 2022) and FLAN-PaLM demonstrated that fine-tuning on a diverse mixture of tasks phrased as natural language instructions — instruction tuning — produces models that generalize to unseen tasks. The key finding: instruction tuning on as few as ~60 datasets with chain-of-thought exemplars significantly improves zero-shot and few-shot performance. T0 (Sanh et al.), OPT-IML, and later open-source efforts (Alpaca, Dolly) showed that this recipe was reproducible at various scales. See [[Instruction Tuning]].

## The Alignment Taxonomy

Alignment research coalesced around a taxonomy of failure modes: sycophancy (telling users what they want to hear), reward hacking (optimizing the reward model's proxy rather than true user intent), deceptive alignment (appearing aligned during evaluation but not in deployment), and goal misgeneralization. Understanding these failure modes became essential for building reliable systems. The distinction between helpfulness, harmlessness, and honesty (the "HHH" criteria from Anthropic) provided a practical evaluation framework. See [[Alignment Objectives and Failure Modes]].

## DPO: Simplifying Preference Learning

Direct Preference Optimization (Rafailov et al., May 2023, building on 2022 foundations) eliminated the need for a separate reward model by reformulating the RLHF objective as a simple classification loss on preference pairs. DPO treated the language model itself as an implicit reward model, making alignment training significantly simpler and more stable. Variants like IPO, KTO, and ORPO further simplified the pipeline. DPO became the standard alignment method for open-source models due to its ease of implementation. See [[Direct Preference Optimization]].

## Constitutional AI

Anthropic's Constitutional AI (Bai et al., December 2022) replaced human feedback with AI feedback: a model critiques and revises its own outputs according to a written set of principles (a "constitution"), then the revised outputs train a preference model. This approach reduced the need for expensive human labeling while allowing explicit control over model values through the constitution's principles. RLAIF (Reinforcement Learning from AI Feedback) became a viable alternative to human-in-the-loop RLHF. See [[Constitutional AI]].

## Chain-of-Thought Reasoning

Chain-of-thought prompting (Wei et al., January 2022) showed that including step-by-step reasoning examples in the prompt dramatically improves performance on math, logic, and multi-step reasoning tasks. Zero-shot CoT ("Let's think step by step," Kojima et al., May 2022) achieved similar gains without hand-crafted exemplars. Self-consistency (Wang et al., 2022) sampled multiple reasoning chains and selected the majority answer. These techniques revealed that LLMs possess latent reasoning capabilities that are unlocked by appropriate prompting structure. See [[Chain-of-Thought Prompting]].

## ChatGPT and the Chat Revolution

ChatGPT launched on November 30, 2022, applying the InstructGPT alignment recipe to GPT-3.5 in a conversational interface. It reached 100 million users in two months — the fastest consumer product adoption in history. ChatGPT transformed LLMs from a research tool into a mainstream technology, triggering a global investment surge, competitive responses from Google (Bard), Anthropic (Claude), and Meta (LLaMA), and regulatory attention worldwide. System prompts and role conditioning became essential infrastructure for controlling model behavior in production. See [[System Prompts and Role Conditioning]].

## Interpretability and Red-Teaming

As aligned models reached consumers, understanding their internals and finding their failures became urgent. Mechanistic interpretability (Elhage, Olah et al. at Anthropic) used techniques like activation patching, probing, and circuit analysis to reverse-engineer how transformers represent and process information. Red-teaming — systematically probing models with adversarial inputs to find harmful behaviors — became a standard safety practice, with dedicated red teams at major labs. See [[Mechanistic Interpretability]] and [[Red-Teaming and Safety Evaluations]].

## Chinchilla and Compute-Optimal Training

The Chinchilla paper (Hoffmann et al., March 2022) revised Kaplan's scaling laws, showing that most large models were significantly over-parameterized relative to their training data. Chinchilla (70B parameters, 1.4T tokens) outperformed the much larger Gopher (280B, 300B tokens), demonstrating that tokens and parameters should scale roughly equally. This finding reshaped training budgets: subsequent models like LLaMA trained smaller architectures on much more data. See [[Compute Data and Parameter Trade-offs]].

## Quantization Goes Practical

GPTQ (Frantar et al., October 2022) demonstrated that large language models could be quantized to 4-bit and 3-bit precision with minimal quality loss using one-shot weight quantization. This made it feasible to run models that required multiple GPUs at full precision on a single consumer GPU. Combined with QLoRA (Dettmers et al., May 2023), quantization democratized access to large model fine-tuning and inference. See [[Quantization]].

## Evaluation Shifts

Traditional NLP benchmarks (GLUE, SuperGLUE) were saturated. Evaluation shifted toward human preference studies (Chatbot Arena, Zheng et al.), adversarial evaluation, and multi-dimensional assessment. The disconnect between benchmark performance and real-world utility became widely acknowledged, driving interest in more ecologically valid evaluation methods. See [[Human Evaluation and Preference Studies]].

## Pages in This Era

- [[Reinforcement Learning from Human Feedback]]
- [[Constitutional AI]]
- [[Direct Preference Optimization]]
- [[Alignment Objectives and Failure Modes]]
- [[Mechanistic Interpretability]]
- [[Red-Teaming and Safety Evaluations]]
- [[Chain-of-Thought Prompting]]
- [[System Prompts and Role Conditioning]]
- [[Instruction Tuning]]
- [[Human Evaluation and Preference Studies]]
- [[Quantization]]
- [[Compute Data and Parameter Trade-offs]]

## Related Eras

← Previous: [[2020–2021 — The Scaling Era Overview|2020–2021 — The Scaling Era]]
→ Next: [[2023 — Open Models and Agents Overview|2023 — Open Models and Agents]]
