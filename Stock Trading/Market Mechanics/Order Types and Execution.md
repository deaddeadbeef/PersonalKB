---
tags: [stock-trading, market-mechanics, orders]
up: "[[Stock Trading]]"
confidence: verified
freshness: current-sensitive
last-verified: 2026-07-01
tier-coverage: [core, practice]
---
# Order Types and Execution

## One-Line Summary

Order types control execution behavior; they do not turn an uncertain trade into a certain profit.

## Core Order Types

| Order | What it asks for | Main risk |
| --- | --- | --- |
| Market order | Execute immediately at available prices | Execution price is not guaranteed |
| Limit order | Execute only at the limit price or better | Execution is not guaranteed |
| Stop order | Trigger a market order after stop price is reached | Triggered execution price can slip |
| Stop-limit order | Trigger a limit order after stop price is reached | May not execute after triggering |

Investor.gov's order-type guidance is the key beginner source: a market order generally prioritizes execution, while a limit order prioritizes price constraints. A stop order can become a market order after the stop price is reached, so the stop price is not a guaranteed exit price.

## Market Orders

Use a market order only when immediate execution matters more than exact price. This is usually safer in highly liquid securities during normal conditions than in thin, volatile, or news-driven securities. The last traded price is not the guaranteed execution price.

## Limit Orders

Use a limit order when price control matters. A buy limit says "no higher than this price." A sell limit says "no lower than this price." The cost of that control is non-execution or partial execution.

## Stop Orders

Use stops as risk-management triggers, not as magic loss caps. A sell stop below market can help define an exit plan for a long position, but if the market gaps below the stop, the resulting market order may execute far below the stop price.

## Execution Checklist

Before placing even a paper trade, answer:

1. What exact order type am I using?
2. Which risk am I choosing: price uncertainty or execution uncertainty?
3. What happens if only part of the order fills?
4. What happens if price gaps through the planned stop?
5. What account rule or settlement rule applies after execution?

## Common Beginner Error

The stop price is a trigger, not a guaranteed sale price. The limit price is a constraint, not a promise that someone will trade with you.

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [Investor.gov - Types of Orders](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov - Understanding Order Types](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14)
- [Investor.gov - Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15)
