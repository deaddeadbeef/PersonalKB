---
tags: [stock-trading, strategies, algorithmic-trading]
up: "[[Stock Trading]]"
confidence: verified
freshness: current-sensitive
last-verified: 2026-07-02
tier-coverage: [core, deep-dive, practice]
---
# Algorithmic Trading

## One-Line Summary

Algorithmic trading uses software rules to generate, route, modify, or execute orders; it is an automation layer, not proof that the trading idea has an edge.

## Working Definition

FINRA describes algorithmic trading strategies as automated systems that initiate pre-programmed trading instructions based on specified variables. In this wiki, algorithmic trading means a program can affect market orders or order-related messages without a human manually deciding every action at the moment of entry.

That definition includes several different layers:

| Layer | Question it answers | Beginner boundary |
| --- | --- | --- |
| Signal | What condition says a trade might exist? | Must be explainable without code |
| Sizing and risk | How much can the system risk? | Must have hard maximums |
| Execution | How should the order be split, routed, priced, or cancelled? | Paper or simulation only |
| Monitoring | How do we know the system is misbehaving? | Logs and stop rules before any automation |
| Intervention | Who can stop the system and when? | Manual kill switch before live use |

## Algorithmic Does Not Mean Quantitative

Algorithmic trading is about automation. [[Quantitative Trading]] is about data, models, and statistical research. They often overlap, but they answer different questions:

| Term | Core question | Example |
| --- | --- | --- |
| Quantitative trading | Is there a model-backed reason to trade? | A factor model ranks a stock universe |
| Algorithmic trading | How does software place or manage orders? | A program sends limit orders and cancels stale orders |

A discretionary strategy can use an execution algorithm. A quantitative signal can be executed manually. Do not treat the words as interchangeable.

## Why Regulators Care

Automated systems can send many orders quickly, route orders across venues, cancel and replace orders, or react to market data faster than a person can inspect each decision. SEC and FINRA materials focus on controls, supervision, testing, validation, compliance, market access, and stability because a software failure can become a market, firm, or customer problem before a human notices it.

The operational lesson for a learner is simple: automation magnifies process quality. It magnifies bugs too.

## Control Checklist

No algorithm belongs even in paper practice until it has:

| Control | Purpose |
| --- | --- |
| Symbol whitelist | Prevents accidental trading outside the intended universe |
| Max order size | Stops one bad calculation from creating an outsized order |
| Max position size | Prevents hidden accumulation |
| Max daily loss | Turns off the system after damage reaches a pre-set bound |
| Duplicate-order guard | Prevents loops from sending the same intent repeatedly |
| Price and spread checks | Rejects orders in abnormal quote conditions |
| Time-window limits | Prevents orders outside planned sessions |
| Kill switch | Allows immediate manual shutdown |
| Full logs | Preserves inputs, signal state, order intent, order response, and errors |
| Post-run review | Compares intended behavior with actual simulated behavior |

## Beginner Practice Artifact

Before coding, write the algorithm in plain English:

| Field | Required entry |
| --- | --- |
| Strategy name | Write plain-English name |
| Market and symbols | List explicit paper-only universe |
| Data needed | Name data source and timestamp rule |
| Signal rule | Write exact condition |
| Entry rule | Write exact trigger and order type |
| Exit rule | Write exit, stop, or review condition |
| Order type | Choose studied order type only |
| Maximum order size | Define share and notional cap |
| Maximum position size | Define exposure cap |
| Maximum daily loss | Define paper shutoff threshold |
| Conditions that stop the system | List kill-switch and error conditions |
| Logs required for review | List signal, request, response, fill, cancel, and error logs |

If the table cannot be completed, the algorithm is not ready to be coded.

## Failure Modes

- Code defect: the program does what was written, not what was intended.
- Data defect: stale, missing, adjusted, or incorrectly timestamped data triggers false decisions.
- Market-state mismatch: the algorithm assumes liquidity, spreads, or volatility that no longer exists.
- Control failure: size, symbol, order type, or daily-loss limits are missing or bypassed.
- Compliance failure: the strategy creates prohibited, manipulative, or improperly marked trading activity.
- Monitoring failure: the system misbehaves without a log, alert, or human stop path.

## Rule For This Wiki

No live algorithmic trading belongs in the first Stock Trading pass. The first acceptable version is a paper-only, logged, manually reviewed simulation whose output can be checked against [[Position Sizing and Trade Journaling]] and [[Paper Trading Lab]].

## See Also

- [[Quantitative Trading]]
- [[Backtesting and Simulation]]
- [[Market Data and Data Quality]]
- [[Broker APIs and Automation Controls]]
- [[Order Types and Execution]]
- [[Position Sizing and Trade Journaling]]
- [[Paper Trading Lab]]

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [FINRA - Algorithmic Trading](https://www.finra.org/rules-guidance/key-topics/algorithmic-trading)
- [FINRA Regulatory Notice 15-09](https://www.finra.org/rules-guidance/notices/15-09)
- [FINRA Regulatory Notice 15-06](https://www.finra.org/rules-guidance/notices/15-06)
- [SEC - Staff Report on Algorithmic Trading in U.S. Capital Markets](https://www.sec.gov/files/algo_trading_report_2020.pdf)
- [SEC - Rule 15c3-5 Market Access Compliance Guide](https://www.sec.gov/files/rules/final/2010/34-63241-secg.htm)
