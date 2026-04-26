---
tags: [chunk, llm]
id: "chunk-llm-238"
source: "[[LLM/_raw/raw-llm-060 Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena]]"
source_loc: "Chunk Candidates"
topic: "Chatbot Arena Elo rating system"
claim: "Chatbot Arena uses crowdsourced pairwise human preferences with Elo ratings to rank LLMs, becoming the most trusted open LLM leaderboard."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/LLM-as-Judge]]", "[[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]"]
qna_seeds:
  - q: "How does Chatbot Arena work?"
    a: "Users submit prompts to two anonymous models, see both responses side by side, and vote for the better one. Votes are aggregated into Elo ratings (borrowed from chess) that produce a continuously updated ranking of LLMs."
  - q: "Why is Chatbot Arena considered more trustworthy than static benchmarks?"
    a: "It uses real user prompts (not curated test sets), blind evaluation (model identities hidden), and crowdsourced diversity of preferences — making it resistant to benchmark gaming and more reflective of real-world user satisfaction."
up: "[[LLM/LLM]]"
---
# Chatbot Arena Ranks LLMs via Crowdsourced Elo Ratings

Chatbot Arena is a live evaluation platform where users submit arbitrary prompts to two anonymous LLMs, view both responses side by side, and vote for the preferred response. These pairwise preferences are aggregated into Elo ratings — the same system used in chess rankings — producing a continuously updated leaderboard of LLM capabilities as perceived by real users.

Chatbot Arena has become the most trusted open leaderboard for comparing LLMs because it addresses key weaknesses of static benchmarks: prompts come from real users (not curated test sets), evaluation is blind (model identities are hidden until after voting), and the diversity of users and prompts resists systematic gaming. With over 1 million votes collected, the Elo ratings provide statistically robust rankings that correlate strongly with expert evaluations and have become the de facto reference for comparing frontier model capabilities.
