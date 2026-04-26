---
tags: [raw, llm]
id: "raw-llm-050"
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
author: "Schick et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2302.04761"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

## What Is This?
A self-supervised method where an LM learns to insert API calls (calculator, search engine, translator, calendar, QA system) into text by generating candidates, filtering by loss reduction, and fine-tuning on the successful tool-use examples.

## Why It Matters
Showed that LLMs can autonomously learn when and how to use external tools without explicit human annotation of tool use — a key step toward practical agentic systems that know their own limitations and augment themselves with external capabilities.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Self-supervised tool-use annotation: candidate generation and loss-based filtering
- [ ] Five tool APIs: calculator, Q&A, search, translator, calendar
- [ ] When to call vs. not call a tool: the model's learned decision boundary
