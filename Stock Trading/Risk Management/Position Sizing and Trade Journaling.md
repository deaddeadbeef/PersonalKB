---
tags: [stock-trading, risk-management, journaling]
up: "[[Stock Trading]]"
confidence: policy
freshness: current-sensitive
last-verified: 2026-07-01
tier-coverage: [core, practice]
---
# Position Sizing and Trade Journaling

## One-Line Summary

Position sizing turns "I like this stock" into "I know what I lose if I am wrong"; journaling turns each paper trade into evidence instead of memory.

## Why Position Size Comes Before Entry

The trader does not control the next price. The trader controls whether a trade is taken, how large it is, what invalidates it, and when it is reviewed. Position sizing is the bridge between analysis and survival.

For this wiki, define `1R` as the planned loss on a trade if the invalidation point is reached. Example: if the account allows a maximum paper risk of $50 on a trade, then `1R = $50`. This is a learning convention, not a recommendation.

## Basic Formula

For paper trading:

```text
shares = planned_risk_dollars / abs(entry_price - invalidation_price)
```

Then check whether the resulting position size is reasonable relative to:

- Account size.
- Liquidity.
- Spread.
- Gap risk.
- Earnings or news events.
- Settlement and account rules.

If the size is too large, the answer is not to ignore the invalidation point. The answer is to reduce planned risk, choose a different setup, or skip the trade.

## Practice Batch

Use [[Paper Trading Lab]] after this page. The lab forces ten journal rows to be reviewed as a batch, so one lucky result does not get mistaken for skill.

## Trade Journal Row

| Field | Required entry |
| --- | --- |
| Date | Trade date |
| Ticker | Security symbol |
| Thesis | Why this trade should work |
| Evidence | Filing, chart, news, or market context used |
| Entry plan | Price and order type |
| Invalidation | Price or condition that proves the trade wrong |
| Planned risk | Dollar amount and `R` |
| Position size | Share count |
| Exit plan | Target, trailing logic, time stop, or review event |
| Result | Profit/loss in dollars and `R` |
| Mistake | Process error, if any |
| Lesson | One reusable improvement |

## Paper-Trading Rules

1. No trade without an invalidation point.
2. No trade without a written order type.
3. No trade if the planned loss is unclear.
4. No trade around earnings until earnings-gap behavior is studied separately.
5. No margin, short selling, options, or leveraged products in the first pass.
6. Review process quality separately from profit and loss.

## Review Questions

- Was the thesis specific enough to be wrong?
- Was the invalidation point set before entry?
- Did the order type match the intent?
- Was the position size calculated from risk rather than desire?
- Did the exit follow the plan?
- Did a rule, spread, gap, or liquidity condition appear that was not planned for?

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [[Paper Trading Lab]]
- [FINRA - Risk](https://www.finra.org/investors/investing/investing-basics/risk)
- [FINRA - Frequent Intraday Trading](https://www.finra.org/investors/insights/frequent-intraday-trading)
- [Investor.gov - Types of Orders](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
