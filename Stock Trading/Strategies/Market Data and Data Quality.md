---
tags: [stock-trading, strategies, market-data, data-quality]
up: "[[Quantitative Trading]]"
confidence: verified
freshness: current-sensitive
last-verified: 2026-07-02
tier-coverage: [core, deep-dive, practice]
---
# Market Data and Data Quality

## One-Line Summary

Quantitative trading is only as good as its data definitions, timestamps, adjustments, and missing-data handling.

## Data Is Part Of The Strategy

A model rule is incomplete until it says exactly which data it consumes and when that data was knowable. Price, volume, financial statements, corporate actions, analyst estimates, index membership, and news all have different publication times and revision behavior.

The core question is not "Do I have data?" The core question is "Would this exact data have been available to the strategy at the modeled decision time?"

## Data Checklist

| Check | Required question |
| --- | --- |
| Source | Who publishes or vendors this data? |
| Timestamp | What clock controls availability: trade time, filing time, vendor delivery, or end-of-day batch? |
| Adjustment | Are splits, dividends, mergers, and symbol changes handled consistently? |
| Survivorship | Are failed, delisted, merged, or removed stocks represented? |
| Missing values | Are missing fields skipped, filled, or treated as a signal? |
| Revisions | Can historical fundamentals or estimates change after the decision date? |
| Point-in-time safety | Does the test prevent future information from entering past decisions? |
| Latency | Does the strategy depend on data faster than the learner can obtain or validate? |
| Licensing | Is the data allowed for the intended use? |

## Minimum Dataset Card

Create one dataset card before using a data source:

| Field | Required entry |
| --- | --- |
| Dataset name | Name the exact source or vendor |
| Coverage | Symbols, exchanges, countries, and years covered |
| Granularity | Tick, minute, daily, quarterly, annual, or event-based |
| Timestamp convention | State when the value becomes usable |
| Corporate actions | State split, dividend, merger, and ticker handling |
| Known gaps | List missing periods, excluded securities, or stale fields |
| Refresh rule | State how often it must be updated |
| Permitted use | State whether use is personal research, paper trading, or other |

## Failure Modes

- A model uses adjusted close for signal logic but raw prices for execution.
- A test ranks a company before its filing was publicly available.
- A universe includes today's index members but excludes past removals.
- A vendor silently revises historical fundamentals.
- Missing values are filled with zero and become an accidental signal.
- A paper run uses delayed data but the backtest assumes immediate data.

## Rule For This Wiki

No [[Quantitative Trading|quantitative]] note should cite a result unless it identifies the dataset, timestamp convention, and missing-data rule. If those three fields are unknown, the claim stays `uncertain`.

## See Also

- [[Quantitative Trading]]
- [[Backtesting and Simulation]]
- [[Company Filing Worksheet]]

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [Federal Reserve - Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm)
- [SEC - Staff Report on Algorithmic Trading in U.S. Capital Markets](https://www.sec.gov/files/algo_trading_report_2020.pdf)
- [Investor.gov - Performance Claims](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-47)
