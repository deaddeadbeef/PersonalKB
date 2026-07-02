---
tags: [stock-trading, strategies, backtesting, simulation]
up: "[[Quantitative Trading]]"
confidence: verified
freshness: current-sensitive
last-verified: 2026-07-02
tier-coverage: [core, deep-dive, practice]
---
# Backtesting and Simulation

## One-Line Summary

Backtesting checks whether a written rule would have survived historical data; it is a rejection tool first and never proof that a strategy will work next.

## What A Backtest Is

A backtest replays a strategy rule over historical data. It should answer a narrow question: "If this exact rule had been applied under these exact assumptions, what would have happened before costs, after costs, and under bad market periods?"

Investor.gov warns that back-tested performance is hypothetical. In this wiki, that warning controls the whole page: a backtest can expose weakness, but it cannot certify future returns.

## Minimum Test Specification

| Field | Required entry |
| --- | --- |
| Hypothesis | State the market claim before seeing results |
| Universe | Define eligible stocks and delisting treatment |
| Data source | Name source, timestamp convention, and adjustment rules |
| Signal | Write the exact formula or rule |
| Portfolio rule | Define ranking, weighting, rebalance date, and holding period |
| Cost model | Include spread, commission, slippage, borrow, and taxes when relevant |
| Risk rule | Define position, sector, leverage, drawdown, and stop conditions |
| In-sample period | Period used to design the rule |
| Out-of-sample period | Period held back for validation |
| Rejection rule | Define what result kills the idea |

## Common Backtest Failures

| Failure | What to check |
| --- | --- |
| Look-ahead bias | Was every input available before the simulated trade? |
| Survivorship bias | Were delisted, merged, failed, and removed companies included? |
| Split or dividend error | Are prices and returns adjusted consistently? |
| Timestamp error | Did filing, earnings, and market data become available at the modeled time? |
| Cost blindness | Do costs erase the apparent edge? |
| Turnover blindness | Does the strategy trade more often than the account can support? |
| Parameter mining | Does the result depend on one tuned threshold? |
| Regime dependence | Does it fail outside one market period? |
| Liquidity mismatch | Could the modeled order size execute without moving the market? |

## Simulation Ladder

Use the weakest safe environment that answers the question:

1. Spreadsheet replay: verify the rule by hand on a tiny sample.
2. Scripted backtest: replay the full universe with explicit assumptions.
3. Walk-forward paper run: generate decisions forward in time without capital.
4. Paper broker simulation: test order handling and logs without live orders.
5. Live capital: out of scope for the first Stock Trading pass.

## Acceptance Rule

A backtest is not acceptable unless another person could reproduce it from the written specification, data source list, and cost assumptions. If the result cannot be reproduced, it is not evidence.

## See Also

- [[Quantitative Trading]]
- [[Market Data and Data Quality]]
- [[Paper Trading Lab]]

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [Investor.gov - Performance Claims](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-47)
- [Federal Reserve - Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm)
- [SEC - Staff Report on Algorithmic Trading in U.S. Capital Markets](https://www.sec.gov/files/algo_trading_report_2020.pdf)
