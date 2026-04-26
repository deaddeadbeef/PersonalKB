---
tags: [pl, chunk, type-systems, gradual]
up: "[[Gradual Typing]]"
---

# Gradual Typing Success Stories TypeScript and Python

Gradual typing — adding optional static types to a dynamic language — is one of the most successful language evolution strategies.

## TypeScript: The Gold Standard

TypeScript (2012) proved gradual typing can scale. All JS is valid TS, and the ecosystem provides types for 10K+ npm packages via DefinitelyTyped.

### Results
- VS Code (TypeScript): caught 15% of bugs before runtime
- Airbnb: 38% of bugs would have been prevented by TypeScript
- Google, Microsoft, Slack, Shopify: all migrated major projects to TypeScript

## Python: The Evolving Experiment

Python type hints (PEP 484, 2015) took a different approach with external checkers like mypy and pyright.

## Key Insight
Gradual typing works best when: all existing code is valid without types, types provide immediate IDE benefits, there's one dominant type checker, and the ecosystem provides type definitions.

## References
→ [[Sources Index]]
