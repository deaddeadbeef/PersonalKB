---
tags: [stock-trading, strategies, quantitative-trading, model-risk]
up: "[[Stock Trading]]"
confidence: verified
freshness: current-sensitive
last-verified: 2026-07-02
tier-coverage: [core, deep-dive, practice]
---
# Quantitative Trading

## One-Line Summary

Quantitative trading turns a market hypothesis into a data-defined, testable model; the model is evidence to inspect, not a machine that removes uncertainty.

## Working Definition

In this wiki, quantitative trading means using numeric data, explicit rules, and statistical or mathematical models to decide what to trade, when to trade, how much to hold, or how to manage risk. It can be simple, such as a rank rule over valuation and momentum metrics, or complex, such as a multi-factor portfolio model.

Quantitative trading is not automatically [[Algorithmic Trading]]. A quant model can produce a watchlist for manual review, and an algorithm can execute a non-quant discretionary order. The overlap begins when model output drives software orders.

## The Research Loop

| Step | Question | Output |
| --- | --- | --- |
| Hypothesis | What should be true about the market? | One falsifiable claim |
| Universe | Which securities are eligible? | Inclusion and exclusion rules |
| Data | What fields are needed? | Source list and data-quality checks |
| Signal | How is the thesis converted into a number or rule? | Formula or model description |
| Backtest | How would the rule have behaved historically? | Reproducible test and assumptions |
| Cost model | What happens after spreads, commissions, slippage, borrow, and taxes? | Net performance estimate |
| Robustness | Does it survive different periods, parameters, and markets? | Out-of-sample and stress checks |
| Paper run | Does the process work forward in time without capital? | Journaled simulated decisions |
| Review | What changed between model, simulation, and reality? | Keep, revise, or reject decision |

## Backtesting Boundary

Investor.gov warns that back-tested performance is hypothetical and does not show actual performance. For this wiki, a backtest is only a filter:

- It can reject a bad idea.
- It can reveal cost, turnover, drawdown, liquidity, and exposure problems.
- It cannot prove the future.
- It cannot replace out-of-sample testing, paper trading, and live operational controls.

## Model Risk

Model risk is the risk that decisions based on a model produce adverse financial consequences because the model is flawed, misused, no longer fit for purpose, or misunderstood. The Federal Reserve's model-risk guidance is written for banking organizations, but the principle maps cleanly to a personal quant-trading wiki: the model must be documented, challenged, monitored, and treated as a source of risk.

For a learner, model risk usually appears as one of these mistakes:

| Mistake | What it means |
| --- | --- |
| Look-ahead bias | The test uses information that was not available at decision time |
| Survivorship bias | The test excludes failed, delisted, or removed securities |
| Data snooping | The rule is chosen because it fit one historical sample |
| Overfitting | Too many parameters explain the past but fail forward |
| Cost blindness | Transaction costs, spread, borrow cost, slippage, or taxes erase the edge |
| Liquidity blindness | The assumed trade size could not actually execute near the modeled price |
| Regime dependence | The model works only in one market environment |
| Capacity limit | The edge disappears when too much capital follows it |
| Operational mismatch | The modeled rule cannot be executed with the available broker, account, or data |

## Minimal Research Journal

Every quant idea should leave a journal row before any code is trusted:

| Field | Required entry |
| --- | --- |
| Hypothesis | Write one falsifiable claim |
| Economic or behavioral rationale | Explain why the effect might exist |
| Universe | Define eligible symbols and exclusions |
| Data sources | Link dataset cards or source notes |
| Signal formula | Write exact formula or rule |
| Rebalance or holding period | Define timing before testing |
| Cost assumptions | Include spread, commission, slippage, borrow, and taxes when relevant |
| Risk limit | Define position, portfolio, and drawdown limits |
| In-sample period | State design period |
| Out-of-sample period | State validation period |
| Largest drawdown | Fill in after test or write `not tested` |
| Failure condition | Define rejection threshold |
| Reason to reject | Write rejection reason before revision |

## Red Flags

- The strategy has no reason to work beyond "the chart went up in the backtest."
- The result disappears after realistic costs.
- One date, symbol, sector, or parameter choice explains most of the return.
- The model cannot be explained without hiding behind code.
- The paper run diverges from the backtest and there is no diagnosis.
- The strategy needs margin, shorting, leverage, options, or rapid intraday trading before the learner understands the simpler stock-trading path.

## Rule For This Wiki

Quantitative trading belongs after the learner can complete [[Company Filing Worksheet]], explain [[Price Action Momentum and Volatility]], and run [[Paper Trading Lab]] without violating the process rules. The first quant artifact is a research note, not a live trading system.

## See Also

- [[Algorithmic Trading]]
- [[Backtesting and Simulation]]
- [[Market Data and Data Quality]]
- [[Broker APIs and Automation Controls]]
- [[Company Filing Worksheet]]
- [[Price Action Momentum and Volatility]]
- [[Position Sizing and Trade Journaling]]
- [[Paper Trading Lab]]

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [Investor.gov - Performance Claims](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-47)
- [SEC - Staff Report on Algorithmic Trading in U.S. Capital Markets](https://www.sec.gov/files/algo_trading_report_2020.pdf)
- [Federal Reserve - Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm)
- [FINRA - Algorithmic Trading](https://www.finra.org/rules-guidance/key-topics/algorithmic-trading)
